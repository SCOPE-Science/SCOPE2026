#!/usr/bin/env python3
"""Independent elementary finite-field point-count checks (Python standard library)."""
import itertools
P=7
# Monic irreducibles over F7: x+1, x^2+1, x^3+x^2+1, x^4+x^3+1.
FIELD_POLYS={1:(1,1),2:(1,0,1),3:(1,0,1,1),4:(1,0,0,1,1)}
class Field:
    def __init__(self,n):
        self.n=n; self.poly=FIELD_POLYS[n]; self.zero=(0,)*n
        self.one=(1,)+(0,)*(n-1)
    def scalar(self,c):return (c%P,)+(0,)*(self.n-1)
    def add(self,a,b):return tuple((u+v)%P for u,v in zip(a,b))
    def mul(self,a,b):
        n=self.n;t=[0]*(2*n-1)
        for i,u in enumerate(a):
            for j,v in enumerate(b):t[i+j]=(t[i+j]+u*v)%P
        for k in range(2*n-2,n-1,-1):
            for j in range(n):t[k-n+j]=(t[k-n+j]-t[k]*self.poly[j])%P
        return tuple(t[:n])
    def pow(self,a,k):
        r=self.one
        while k:
            if k&1:r=self.mul(r,a)
            a=self.mul(a,a);k>>=1
        return r

def count(n,u,v):
    F=Field(n);q=7**n;U=F.scalar(u);V=F.scalar(v)
    count=1 # unique point at infinity, because gcd(3,5)=1
    for t in itertools.product(range(7),repeat=n):
        t2=F.mul(t,t);t3=F.mul(t2,t);t5=F.mul(t2,t3)
        rhs=F.add(F.add(F.add(t5,F.mul(U,t3)),F.mul(V,t)),F.one)
        if rhs==F.zero:count+=1
        elif F.pow(rhs,(q-1)//3)==F.one:count+=3
    return count

def weil_mod7(u,v):
    counts=[count(n,u,v) for n in range(1,5)]
    traces=[7**(j+1)+1-counts[j] for j in range(4)]
    coeff=[1]
    for k in range(1,5):
        numerator=-sum(coeff[k-j]*traces[j-1] for j in range(1,k+1))
        assert numerator%k==0
        coeff.append(numerator//k)
    return counts,coeff

cases={
    (0,0):([8,50,344,2094],[1,0,0,0,-77]),
    (6,3):([8,50,344,2346],[1,0,0,0,-14]),
    (2,5):([8,86,344,2454],[1,0,18,0,175]),
    (2,0):([5,45,398,2169],[1,-3,2,21,-117]),
}
for params,expected in cases.items():
    observed=weil_mod7(*params)
    assert observed==(expected[0],expected[1]),(params,observed,expected)
    # Rank-zero cases: polynomial mod 7 has degree zero; rank-two case
    # has degree two; ordinary case has degree four.
    p_degree=max(k for k,c in enumerate(observed[1]) if c%7)
    assert p_degree=={(0,0):0,(6,3):0,(2,5):2,(2,0):4}[params]
    print('params',params,'N1..N4',observed[0], 'L0..L4',observed[1], 'rank',p_degree)
print('INDEPENDENT_POINT_COUNTS_OK')
