"""Independent finite-field tests for the three-dimensional algebra A(t).
Run: python verify.py
No third-party dependencies.
"""
from itertools import product

class Field:
    def __init__(self,q):
        self.q=q
        self.bits={4:0b111,8:0b1011}.get(q)
        if self.bits is None:
            if q<2 or any(q%d==0 for d in range(2,int(q**.5)+1)):
                raise ValueError('prime or supported binary extension required')
        self.Z=range(q)
    def add(self,a,b):return a^b if self.bits is not None else (a+b)%self.q
    def neg(self,a):return a if self.bits is not None else (-a)%self.q
    def sub(self,a,b):return self.add(a,self.neg(b))
    def mul(self,a,b):
        if self.bits is None:return (a*b)%self.q
        x=0; aa=a; bb=b; deg=self.q.bit_length()-1
        while bb:
            if bb&1:x^=aa
            bb>>=1; aa<<=1
            if aa & self.q: aa^=self.bits
        return x
    def pow(self,a,n):
        r=1
        while n:
            if n&1:r=self.mul(r,a)
            a=self.mul(a,a);n>>=1
        return r
    def inv(self,a):
        assert a!=0
        return self.pow(a,self.q-2)
    def mvec(self,a,x):return tuple(self.mul(a,u) for u in x)
    def vadd(self,x,y):return tuple(self.add(a,b) for a,b in zip(x,y))
    def mulA(self,x,y,t):
        a,b,c=x;d,e,f=y
        return (self.sub(self.sub(self.mul(a,d),self.mul(b,e)),self.mul(c,f)),
                self.add(self.add(self.mul(a,e),self.mul(b,d)),self.mul(t,self.mul(c,e))),
                self.add(self.add(self.mul(a,f),self.mul(c,d)),self.mul(t,self.mul(c,e))))
    def projective(self):
        n=self.q
        return [(1,b,c) for b,c in product(self.Z,repeat=2)] + [(0,1,c) for c in self.Z]+[(0,0,1)]
    def is_sub1(self,v,t):return self.mulA(v,v,t) in {self.mvec(a,v) for a in self.Z}
    def is_sub2(self,x,y,t):
        xy={self.vadd(self.mvec(a,x),self.mvec(b,y)) for a,b in product(self.Z,repeat=2)}
        return all(self.mulA(u,v,t) in xy for u,v in [(x,x),(x,y),(y,x),(y,y)])
    def rank(self, vectors):
        if not vectors:return 0
        A=[list(v) for v in vectors]
        m=len(A);r=0
        for col in range(3):
            j=next((j for j in range(r,m) if A[j][col]),None)
            if j is None:continue
            A[r],A[j]=A[j],A[r]
            inv=self.inv(A[r][col]);A[r]=[self.mul(inv,z) for z in A[r]]
            for ii in range(m):
                if ii!=r and A[ii][col]:
                    z=A[ii][col]
                    A[ii]=[self.sub(u,self.mul(z,v)) for u,v in zip(A[ii],A[r])]
            r+=1
            if r==3:break
        return r
    def generated_dimension(self,x,t):
        if x==(0,0,0):return 0
        basis=[x]
        while True:
            products=[self.mulA(v,w,t) for v in basis for w in basis]
            old=len(basis)
            for y in products:
                if self.rank(basis+[y])>len(basis):basis.append(y)
            if len(basis)==old:return old
    def solve(self,mat,rhs):
        # Linear system with any number of equations and three unknowns.
        A=[list(row)+[r] for row,r in zip(mat,rhs)]
        m=len(A);rank=0
        for col in range(3):
            j=next((j for j in range(rank,m) if A[j][col]),None)
            if j is None:continue
            A[rank],A[j]=A[j],A[rank]
            fac=self.inv(A[rank][col]);A[rank]=[self.mul(fac,z) for z in A[rank]]
            for i in range(m):
                if i==rank:continue
                fac=A[i][col]
                if fac:
                    A[i]=[self.sub(z,self.mul(fac,w)) for z,w in zip(A[i],A[rank])]
            rank+=1
        return not any(not any(row[:3]) and row[3] for row in A)
    def has_two_sided_inverse(self,x,t):
        base=[(1,0,0),(0,1,0),(0,0,1)]
        mats=[self.mulA(x,y,t) for y in base]
        revs=[self.mulA(y,x,t) for y in base]
        rows=[[v[k] for v in mats] for k in range(3)] + [[v[k] for v in revs] for k in range(3)]
        return self.solve(rows,[1,0,0,1,0,0])
    def quadratic_units(self,typ):
        return {'split':(self.q-1)**2,'inert':self.q*self.q-1,'double':self.q*(self.q-1)}[typ]
    def quadtype(self,disc):
        if disc==0:return 'double'
        return 'split' if self.pow(disc,(self.q-1)//2)==1 else 'inert'

def test(q,t):
    F=Field(q);zero=(0,0,0);one=(1,0,0);i=(0,1,0);j=(0,0,1);k=(0,1,1)
    assert t!=0
    assert F.mulA(i,i,t)==(F.neg(1),0,0)
    L=F.projective(); line_set=[v for v in L if F.is_sub1(v,t)]
    planes=set()
    # Every projective plane is kernel of exactly one projective covector.
    for a,b,c in L:
        cov=(a,b,c)
        ker=[v for v in L if F.add(F.add(F.mul(a,v[0]),F.mul(b,v[1])),F.mul(c,v[2]))==0]
        # choose independent vectors from kernel
        x=ker[0]
        y=next(v for v in ker[1:] if v not in {F.mvec(u,x) for u in F.Z})
        if F.is_sub2(x,y,t):planes.add(cov)
    expected_planes={(0,0,1),(0,1,0),(0,1,F.neg(1))}
    # projective normalization of the last covector, with first nonzero 1.
    assert planes==expected_planes,(q,t,'planes',planes,expected_planes)
    eight=0
    for _ in range(8):eight=F.add(eight,1)
    delta=F.sub(F.mul(t,t),eight)
    if q%2:

        axis_type=F.quadtype(F.neg(1)); diag_type=F.quadtype(delta)
    else:
        axis_type='double'; diag_type='split'
    expected_lines=1 + 2*{'split':2,'double':1,'inert':0}[axis_type] + {'split':2,'double':1,'inert':0}[diag_type]
    assert len(line_set)==expected_lines,(q,t,'lines',len(line_set),expected_lines)
    units=sum(F.has_two_sided_inverse(x,t) for x in product(F.Z,repeat=3))
    expected_units=2*F.quadratic_units(axis_type)+F.quadratic_units(diag_type)-2*(q-1)
    assert units==expected_units,(q,t,'units',units,expected_units)
    # Directly test that nonscalar nonunits are not among three algebraic planes.
    for x in product(F.Z,repeat=3):
        _,b,c=x
        if b and c and b!=c:assert not F.has_two_sided_inverse(x,t)
    # All generators are exactly those not in the three planes; compare direct spanning test.
    generators=sum(1 for x in product(F.Z,repeat=3) if x[1] and x[2] and x[1]!=x[2])
    assert generators==q*(q-1)*(q-2)
    actual_generators=sum(F.generated_dimension(x,t)==3 for x in product(F.Z,repeat=3))
    assert generators==actual_generators,(q,t,'generated',generators,actual_generators)
    squares=[F.mulA(x,x,t) for x in product(F.Z,repeat=3)]
    idempotents=sum(x==y for x,y in zip(product(F.Z,repeat=3),squares))
    nilpotents=sum(y==zero for y in squares)
    extras={'split':2,'double':1,'inert':0}
    expected_idempotents=2+2*(2 if axis_type=='split' else 0)+(2 if diag_type=='split' else 0)
    expected_nilpotents=1+(q-1)*(2*(axis_type=='double')+(diag_type=='double'))
    assert (idempotents,nilpotents)==(expected_idempotents,expected_nilpotents),(q,t,'idempotent/nilpotent',idempotents,nilpotents,expected_idempotents,expected_nilpotents)
    print('PASS q=%d t=%d: 1D=%d 2D=%d units=%d monogenic=%d idempotents=%d nilpotents=%d types=%s/%s'%
          (q,t,len(line_set),len(planes),units,generators,idempotents,nilpotents,axis_type,diag_type))

if __name__=='__main__':
    for q in [2,3,4,5,7,8,11,13]:
        for t in ([1] if q==2 else [1,2] if q in (3,4,5,7,8) else [1]):
            test(q,t)
    print('ALL TESTS PASSED')
