from itertools import product
from math import gcd

class PrimeField:
    def __init__(self,p): self.q=p; self.p=p
    def add(self,a,b): return (a+b)%self.p
    def mul(self,a,b): return (a*b)%self.p
    def neg(self,a): return (-a)%self.p
    def inv(self,a):
        if not a: raise ZeroDivisionError
        return pow(a,self.p-2,self.p)
    def div(self,a,b): return self.mul(a,self.inv(b))
    def pow(self,a,n): return pow(a,n,self.p)
    def elems(self): return range(self.q)

class GF4:
    # a+b*x represented by a+2b, with x^2=x+1 over F2.
    q=4
    def add(self,a,b): return a^b
    def neg(self,a): return a
    def mul(self,a,b):
        a0,a1=a&1,(a>>1)&1; b0,b1=b&1,(b>>1)&1
        c0=(a0*b0) ^ (a1*b1)          # x^2 contributes 1
        c1=(a0*b1) ^ (a1*b0) ^ (a1*b1) # x^2 contributes x
        return c0 | (c1<<1)
    def pow(self,a,n):
        r=1
        while n:
            if n&1:r=self.mul(r,a)
            a=self.mul(a,a); n//=2
        return r
    def inv(self,a):
        if not a: raise ZeroDivisionError
        return self.pow(a,2)
    def div(self,a,b): return self.mul(a,self.inv(b))
    def elems(self): return range(4)

def rank_matrix(F, flat, n):
    A=[list(flat[i*n:(i+1)*n]) for i in range(n)]
    r=0
    for c in range(n):
        piv=next((i for i in range(r,n) if A[i][c]),None)
        if piv is None: continue
        A[r],A[piv]=A[piv],A[r]
        z=F.inv(A[r][c]); A[r]=[F.mul(z,x) for x in A[r]]
        for i in range(n):
            if i!=r and A[i][c]:
                z=A[i][c]
                A[i]=[F.add(A[i][j],F.neg(F.mul(z,A[r][j]))) for j in range(n)]
        r+=1
    return r

def gl_matrices(F,n):
    for flat in product(F.elems(), repeat=n*n):
        if rank_matrix(F,flat,n)==n:
            yield flat

def ea_product(F,d,x,y):
    n=len(d); out=[0]*n
    for j in range(n):
        out[(j+1)%n]=F.add(out[(j+1)%n],F.mul(d[j],F.mul(x[j],y[j])))
    return tuple(out)

def col(P,n,i): return tuple(P[r*n+i] for r in range(n))

def mat_vec(F,P,n,v):
    return tuple(sum_field(F,[F.mul(P[r*n+j],v[j]) for j in range(n)]) for r in range(n))

def sum_field(F,xs):
    s=0
    for x in xs:s=F.add(s,x)
    return s

def is_iso_matrix(F,c,d,P):
    n=len(c)
    cols=[col(P,n,i) for i in range(n)]
    for i in range(n):
        left=[0]*n; left[(i+1)%n]=c[i]
        left=mat_vec(F,P,n,left)
        if ea_product(F,d,cols[i],cols[i]) != left: return False
        for j in range(i):
            if any(ea_product(F,d,cols[i],cols[j])): return False
    return True

def theta(F,c):
    n=len(c); t=1
    for i,a in enumerate(c): t=F.mul(t,F.pow(a,2**(n-1-i)))
    return t

def rotate(c,k):
    n=len(c); return tuple(c[(i+k)%n] for i in range(n))

def predicted_iso(F,c,d):
    n=len(c); N=2**n-1
    nth={F.pow(a,N) for a in F.elems() if a}
    tc=theta(F,c)
    for k in range(n):
        td=theta(F,rotate(d,k))
        if F.div(tc,td) in nth: return True
    return False

def predicted_count(q,n):
    g=gcd(2**n-1,q-1)
    return sum(gcd(g,2**k-1) for k in range(n))//n

def stabilizer_count(F,c):
    n=len(c); N=2**n-1; tc=theta(F,c)
    nth={F.pow(a,N) for a in F.elems() if a}
    h=0
    for k in range(n):
        td=theta(F,rotate(c,k))
        if F.div(tc,td) in nth:h+=1
    return h

def test_field(F,n,full_gl=True):
    nz=[a for a in F.elems() if a]
    algs=list(product(nz, repeat=n))
    mats=list(gl_matrices(F,n)) if full_gl else []
    actual=[[False]*len(algs) for _ in algs]
    aut=[]
    if full_gl:
        for i,c in enumerate(algs):
            ac=0
            for j,d in enumerate(algs):
                ok=False
                for P in mats:
                    if is_iso_matrix(F,c,d,P):
                        ok=True
                        if i==j: ac+=1
                        break
                actual[i][j]=ok
            # recompute exact aut count: above counted one witness per d, not auts
            ac=sum(1 for P in mats if is_iso_matrix(F,c,c,P))
            aut.append(ac)
        for i,c in enumerate(algs):
            for j,d in enumerate(algs):
                pr=predicted_iso(F,c,d)
                if actual[i][j]!=pr:
                    raise AssertionError((F.q,n,c,d,actual[i][j],pr))
        # compare isomorphism class number
        reps=[]
        for i,c in enumerate(algs):
            if not any(actual[i][j] for j in reps): reps.append(i)
        pc=predicted_count(F.q,n)
        if len(reps)!=pc: raise AssertionError(('classcount',F.q,n,len(reps),pc))
        g=gcd(2**n-1,F.q-1)
        for c,a in zip(algs,aut):
            pa=g*stabilizer_count(F,c)
            if a!=pa: raise AssertionError(('aut',F.q,n,c,a,pa))
        return len(algs),len(mats),len(reps),sorted(set(aut))

# Full GL brute-force tests, including non-prime GF(4).
results=[]
for F,n in [(PrimeField(3),2),(PrimeField(5),2),(GF4(),2),(PrimeField(3),3)]:
    results.append((F.q,n,*test_field(F,n)))

# Pure orbit/Burnside consistency over a wider grid.
for q in [2,3,4,5,7,8,9,11,13,16,17,19,23,25,27,29,31]:
    for n in range(2,9):
        g=gcd(2**n-1,q-1)
        # Direct orbit count on Z/gZ under doubling.
        unseen=set(range(g)); orbits=0
        while unseen:
            x=next(iter(unseen)); y=x; orb=set()
            while y not in orb:
                orb.add(y); y=(2*y)%g
            unseen-=orb; orbits+=1
        if orbits!=predicted_count(q,n):
            raise AssertionError(('Burnside',q,n,g,orbits,predicted_count(q,n)))

print('VERIFY_OK')
for row in results:
    print('q=%d m=%d tuples=%d GL=%d classes=%d aut_orders=%s'%row)
print('BURNSIDE_GRID_OK q=17-values m=2..8')
