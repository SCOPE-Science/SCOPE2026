"""Independent finite checks for colour-necklace component limits."""
from math import gcd
from fractions import Fraction

def necklace_count(q,d):
    return sum(sum(1 for a in range(1,e+1) if gcd(a,e)==1)*q**(d//e) for e in range(1,d+1) if d%e==0)//d

def partitions(q,N,omit=None):
    f=[0]*(N+1)
    f[0]=1
    for d in range(1,N+1):
        k=necklace_count(q,d)-(1 if omit is not None and d==omit else 0)
        # multiply by (1-z^d)^(-k): count multiplicity via complete homogeneous combinatorial factors
        from math import comb
        new=[0]*(N+1)
        for j in range(N//d+1):
            a=comb(k+j-1,j) if k else int(j==0)
            if not a: continue
            for i in range(N-j*d+1):
                new[i+j*d]+=f[i]*a
        f=new
    return f

def run():
    for q in (1,2,3):
        n=35
        c=partitions(q,n)
        assert c[0]==1 and c[1]==q
        for d in range(1,5):
            assert necklace_count(q,d)==sum(1 for w in __import__('itertools').product(range(q),repeat=d) if w==min(w[i:]+w[:i] for i in range(d)))
        for d in (1,2):
            # geometric multiplicity exact: zero count through omitting one named necklace
            omit=partitions(q,n,omit=d)
            assert all(omit[k]==c[k]-(c[k-d] if k>=d else 0) for k in range(n+1))
            assert Fraction(omit[n],c[n])>=0
        if q>=2:
            # observed zero multiplicity of fixed chosen colour tends to (1-1/q)
            t=Fraction(c[n]-c[n-1],c[n]); assert abs(float(t)- (1-1/q))<0.002
            # exact two specified distinct fixed colors probability independent asymptotically
            z=(c[n]-2*c[n-1]+c[n-2])/c[n]
            assert abs(z-(1-1/q)**2)<0.005
        else:
            assert c[10]==42 and c[20]==627 and c[30]==5604
    print('ALL_CHECKS_OK')
if __name__=='__main__': run()
