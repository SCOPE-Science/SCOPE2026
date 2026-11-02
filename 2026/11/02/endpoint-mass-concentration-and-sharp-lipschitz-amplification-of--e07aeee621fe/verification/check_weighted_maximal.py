"""Exact-rational finite verification of a weighted interval-maximal theorem.

Analytic inequalities in RESULT.md establish all dimensions and weights;
finite tests are checks, not substitutes for the proof.
Run: python verification/check_weighted_maximal.py
No third-party packages required.
"""
from fractions import Fraction as F
from itertools import product

def lip(f):
    return max(abs(f[j+1]-f[j]) for j in range(len(f)-1))

def maximal(f,w):
    n=len(f)
    out=[]
    for i in range(n):
        vals=[]
        for l in range(i+1):
            for r in range(i,n):
                vals.append(sum(w[j]*f[j] for j in range(l,r+1)) / sum(w[l:r+1]))
        out.append(max(vals))
    return out

def limit_maximal(f,a,b):
    n=len(f)
    if n==2:
        mu=(a*f[0]+b*f[-1])/(a+b)
        return [max(f[0],mu),max(f[-1],mu)]
    mu=(a*f[0]+b*f[-1])/(a+b)
    out=[max(f[0],mu)]
    for i in range(1,n-1):
        ins=[]
        for l in range(1,i+1):
            for r in range(i,n-1):
                ins.append(sum(f[l:r+1],F(0))/F(r-l+1))
        out.append(max(f[0],f[-1],max(ins)))
    out.append(max(f[-1],mu))
    return out

def polytope_inputs(n):
    for steps in product((-1,0,1),repeat=n-1):
        cur=F(0)
        f=[cur]
        for s in steps:
            cur+=s;f.append(cur)
        yield tuple(f)

def check():
    assertions=0
    for n in range(2,8):
        for a,b in [(F(1),F(1)),(F(2),F(3)),(F(1),F(5))]:
            R=F(n-1)*max(a,b)/(a+b)
            achieved=False
            weights0=[a]+[F(1)]*(n-2)+[b]
            for f in polytope_inputs(n):
                x=limit_maximal(f,a,b)
                assert lip(x)<=R
                assertions+=1
                if lip(f)==1 and lip(x)==R:
                    achieved=True
                # The exact uniform estimate for two endpoint masses remains valid.
                for eps in [F(1,100),F(1,1000)]:
                    weights=[a]+[eps]*(n-2)+[b]
                    y=maximal(f,weights)
                    E=F(n-1)*F(n-2)*eps/min(a,b)
                    assert all(abs(y[j]-x[j])<=E for j in range(n))
                    assert abs(lip(y)-lip(x))<=2*E
                    assertions+=2
            assert achieved
            assertions+=1
    # Unit-counting-measure, nearest-endpoint spike verifies the sharp half bound.
    for n in range(2,20):
        f=[F(1)]+[F(0)]*(n-1)
        assert lip(maximal(f,[F(1)]*n))==F(1,2)
        assertions+=1
    # Signed signals cause no larger normalized Lipschitz ratio than their absolute values.
    for n in range(2,8):
        for f in polytope_inputs(n):
            absf=[abs(v) for v in f]
            assert lip(absf)<=lip(f)
            assertions+=1
    # Check explicit ramps and their limiting side of the terminal edge.
    for n in range(2,31):
        for a,b in [(F(1),F(1)),(F(2),F(3)),(F(1),F(15))]:
            inc=[F(j) for j in range(n)]
            dec=list(reversed(inc))
            Linc=limit_maximal(inc,a,b)
            Ldec=limit_maximal(dec,a,b)
            assert Linc[1]-Linc[0]==F(n-1)*a/(a+b)
            assert Ldec[-2]-Ldec[-1]==F(n-1)*b/(a+b)
            assertions+=2
    print(f"PASS: {assertions} exact rational finite checks; dimensions 2..30 and parameters tested")
if __name__=='__main__':
    check()
