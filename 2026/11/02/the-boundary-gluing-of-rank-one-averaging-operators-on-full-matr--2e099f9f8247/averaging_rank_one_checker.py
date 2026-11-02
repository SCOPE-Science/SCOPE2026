"""Independent finite-field enumeration for rank-one averaging operators on M_n.
No external dependencies.  Uses the original two-sided operator identities.
"""
from itertools import product
from math import prod

class Field:
    def __init__(self, q):
        assert q in (2,3,4)
        self.q = q
    def add(self,a,b):
        return a^b if self.q==4 else (a+b)%self.q
    def mul(self,a,b):
        if self.q!=4: return (a*b)%self.q
        r=0
        while b:
            if b&1: r^=a
            b>>=1; a<<=1
            if a&4: a^=7
        return r
    def inv(self,a):
        assert a
        return next(b for b in range(1,self.q) if self.mul(a,b)==1)
    def scalar(self, a, M):
        return tuple(self.mul(a,x) for x in M)
    def sum(self,items):
        s=0
        for x in items:s=self.add(s,x)
        return s
    def mm(self,A,B,n):
        return tuple(self.sum(self.mul(A[i*n+k],B[k*n+j]) for k in range(n))
                     for i in range(n) for j in range(n))
    def linear(self,phi,A):
        return self.sum(self.mul(x,y) for x,y in zip(phi,A))

def gl(n,q):
    return prod(q**n-q**j for j in range(n))
def gauss(n,r,q):
    if r<0 or r>n:return 0
    return prod(q**(n-i)-1 for i in range(r))//prod(q**(r-i)-1 for i in range(r))
def predicted(n,q):
    by_id={r:gauss(n,r,q)*q**(r*(n-r))*(q**(r*r)-1) for r in range(1,n+1)}
    by_nil={r:gauss(n,r,q)*gauss(n-r,r,q)*gl(r,q)*(q**((n-r)**2)-1)//(q-1)
            for r in range(1,n//2+1)}
    return by_id,by_nil

def rank_matrix(A,n,F):
    a=[list(A[i*n:(i+1)*n]) for i in range(n)]
    r=0
    for j in range(n):
        p=next((i for i in range(r,n) if a[i][j]),None)
        if p is None:continue
        a[r],a[p]=a[p],a[r]
        z=F.inv(a[r][j]);a[r]=[F.mul(z,x) for x in a[r]]
        for i in range(n):
            if i==r or not a[i][j]:continue
            m=a[i][j]
            a[i]=[F.add(x,F.mul(m,y)) if F.q==4 or F.q==2 else (x-F.mul(m,y))%F.q
                  for x,y in zip(a[i],a[r])]
        r+=1
        if r==n:break
    return r

def direct_check(n,q):
    F=Field(q);d=n*n;zero=(0,)*d
    units=[tuple(int(k==t) for k in range(d)) for t in range(d)]
    seen={}; count=0; squarezero=0; nonzero_p2=0
    total_rep=0
    for U in product(range(q),repeat=d):
        if U==zero:continue
        U2=F.mm(U,U,n)
        left=[F.mm(U,E,n) for E in units]
        right=[F.mm(E,U,n) for E in units]
        for phi in product(range(q),repeat=d):
            if phi==zero: continue
            # A is represented by phi(X)U. All d^2 original basis-pair equations.
            valid=True
            lp=[F.linear(phi,z) for z in left]
            rp=[F.linear(phi,z) for z in right]
            for i in range(d):
                for j in range(d):
                    rhs=F.scalar(F.mul(phi[i],lp[j]),U)
                    rhs2=F.scalar(F.mul(phi[j],rp[i]),U)
                    lhs=F.scalar(F.mul(phi[i],phi[j]),U2)
                    if lhs!=rhs or lhs!=rhs2:
                        valid=False;break
                if not valid:break
            if not valid:continue
            # Normalize (U,phi) under (U,phi) -> (aU,a^-1phi) for all a != 0.
            reps=[(F.scalar(a,U),F.scalar(F.inv(a),phi)) for a in range(1,q)]
            key=min(reps)
            if key in seen:continue
            r=rank_matrix(U,n,F)
            branch='nil' if U2==zero else 'idem'
            # Direct structure check: every nonnilpotent admissible U is quasi-idempotent.
            if branch=='idem':
                assert any(U2==F.scalar(a,U) for a in range(1,q))
            seen[key]=(branch,r)
            count+=1
            if F.linear(phi,U)==0: squarezero+=1
            else:nonzero_p2+=1
    actual_id={r:sum(v==('idem',r) for v in seen.values()) for r in range(1,n+1)}
    actual_nil={r:sum(v==('nil',r) for v in seen.values()) for r in range(1,n//2+1)}
    ei,ni=predicted(n,q)
    assert actual_id==ei,(n,q,actual_id,ei)
    assert actual_nil==ni,(n,q,actual_nil,ni)
    assert count==sum(ei.values())+sum(ni.values())
    print('DIRECT_AVERAGING',n,q,'TOTAL',count,'IDEMPOTENT_IMAGE_RANKS',actual_id,'NILPOTENT_IMAGE_RANKS',actual_nil,'SQUARE_ZERO_OPERATOR',squarezero,'P2_NONZERO',nonzero_p2)

if __name__=='__main__':
    for q in (2,3,4):direct_check(2,q)
    print('PREDICTED_M3_Q2',predicted(3,2))
    print('RANK_ONE_AVERAGING_DIRECT_CHECKS_OK')

# The ambient 3x3 binary rank-one census is additionally enumerated by
# computing the defining identities for a basis and a nonzero probe.
def direct_check_binary_three():
    F=Field(2); n=3; d=9; units=[tuple(int(k==t) for k in range(d)) for t in range(d)]
    counts={'idem':{},'nil':{}}
    for ucode in range(1,1<<d):
        U=tuple((ucode>>i)&1 for i in range(d))
        U2=F.mm(U,U,n)
        if any(U2) and U2!=U:continue
        typ='nil' if not any(U2) else 'idem'
        left=[F.mm(U,E,n) for E in units]
        right=[F.mm(E,U,n) for E in units]
        L=[sum((z[i]<<i) for i in range(d)) for z in left]
        R=[sum((z[i]<<i) for i in range(d)) for z in right]
        lam=0 if typ=='nil' else 1
        accepted=0
        for phi in range(1,1<<d):
            if all(((phi&z).bit_count()&1)==(lam*((phi>>i)&1)) for i,z in enumerate(L)) and all(((phi&z).bit_count()&1)==(lam*((phi>>i)&1)) for i,z in enumerate(R)):
                accepted+=1
        if accepted:
            rank=rank_matrix(U,n,F)
            counts[typ][rank]=counts[typ].get(rank,0)+accepted
    ei,ni=predicted(3,2)
    assert counts=={'idem':ei,'nil':ni},(counts,ei,ni)
    print('DIRECT_BINARY_THREE',counts,'TOTAL',sum(sum(z.values()) for z in counts.values()))
    print('BINARY_THREE_BASIS_IDENTITY_CHECKS_OK')

if __name__=='__main__':
    direct_check_binary_three()

def asymptotic_identity_checks():
    from decimal import Decimal,getcontext
    getcontext().prec=60
    for q in (2,3,4):
        Q=Decimal(1)/Decimal(q)
        d=Decimal(1);rr=Decimal(1)
        for k in range(1,40):
            d*=1-Q**k
            rr+=Q**(k*k)/d
        product_value=Decimal(1)
        for j in range(100):
            product_value/=((1-Q**(5*j+1))*(1-Q**(5*j+4)))
        assert abs(rr-product_value)<Decimal('1e-42')
        limit=(Decimal(q)*rr-1)/(q-1)
        a,b=predicted(24,q)
        finite=Decimal(sum(a.values())+sum(b.values()))/(Decimal(q)**(24**2))
        assert abs(finite-limit)<Decimal('0.000002')
        print('ROGERS_RAMANUJAN',q,'N24_NORMALIZED',f'{finite:.12f}','LIMIT',f'{limit:.12f}')
    print('ROGERS_RAMANUJAN_OPERATOR_LIMIT_CHECKS_OK')
if __name__=='__main__':
    asymptotic_identity_checks()
