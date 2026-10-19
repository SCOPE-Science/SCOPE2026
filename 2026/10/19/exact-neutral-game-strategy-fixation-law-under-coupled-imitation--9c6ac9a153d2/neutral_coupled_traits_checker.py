"""Standalone exact-rational checks for the neutral two-attribute imitation law.

No external dependencies: Python >= 3.9 standard library only.
"""
from fractions import Fraction as F
from itertools import product


def compositions(n, k=4):
    if k == 1:
        yield (n,)
    else:
        for v in range(n+1):
            for tail in compositions(n-v, k-1):
                yield (v,)+tail


def transition(c, a, b, distinct=False):
    n = sum(c)
    assert n >= 2 and 0 < a <= 1 and 0 < b <= 1
    denom = n*(n-1) if distinct else n*n
    out = {}
    for i in range(4):
        if not c[i]: continue
        for j in range(4):
            pairs = c[i]*(c[j]-(i==j)) if distinct else c[i]*c[j]
            if pairs <= 0: continue
            f = F(pairs, denom)
            for ss, pp in ((0, 1-a), (1, a)):
                for gg, qq in ((0, 1-b), (1, b)):
                    xx = j//2 if ss else i//2
                    yy = j%2 if gg else i%2
                    z = 2*xx+yy
                    d=list(c)
                    d[i]-=1;d[z]+=1
                    d=tuple(d)
                    out[d] = out.get(d,F(0))+f*pp*qq
    assert sum(out.values())==1
    return out


def theoretical(c,a,b):
    n = sum(c)
    xs = F(c[2]+c[3],n)
    ys = F(c[1]+c[3],n)
    cross = F(c[3],n)
    theta = 2*a*b/(n*(a+b-2*a*b)+2*a*b)
    return xs*ys+theta*(cross-xs*ys)



def solve(A, b):
    """Independent exact Gaussian elimination over the rationals."""
    n=len(A)
    M=[list(A[i])+[b[i]] for i in range(n)]
    for j in range(n):
        pivot=next(i for i in range(j,n) if M[i][j])
        M[j],M[pivot]=M[pivot],M[j]
        z=M[j][j]
        M[j]=[v/z for v in M[j]]
        for i in range(n):
            if i != j and M[i][j]:
                z=M[i][j]
                M[i]=[u-z*v for u,v in zip(M[i],M[j])]
    return [row[-1] for row in M]


def independent_absorption_checks():
    cases=0
    for n in (2,3):
        for a,b in ((F(1,2),F(1,2)),(F(1,4),F(1,3))):
            for distinct in (False,True):
                states=list(compositions(n))
                transients=[c for c in states if max(c) < n]
                ix={c:i for i,c in enumerate(transients)}
                A=[];rhs=[]
                for c in transients:
                    row=[F(int(c==d)) for d in transients]
                    target=F(0)
                    for d,prob in transition(c,a,b,distinct).items():
                        if d in ix:
                            row[ix[d]]-=prob
                        elif d[3]==n:
                            target+=prob
                    A.append(row);rhs.append(target)
                vals=solve(A,rhs)
                for c,val in zip(transients,vals):
                    assert val==theoretical(c,a,b), (n,a,b,distinct,c,val)
                    cases+=1
    print('Independent exact absorbing-chain checks:',cases)

def test():
    count = 0
    for n in range(2,7):
        for (a,b) in ((F(1,2),F(1,2)),(F(1,4),F(1,3)),(F(1,5),F(1,2))):
            for distinct in (False,True):
                for c in compositions(n):
                    f=theoretical(c,a,b)
                    expected=sum(prob*theoretical(d,a,b) for d,prob in transition(c,a,b,distinct).items())
                    assert f == expected, (n,c,a,b,distinct,f,expected)
                    if any(v==n for v in c):
                        assert f==int(c[3]==n)
                    count+=1
    print('Exact harmonic and boundary checks:',count)
    c=(0,1,1,0)  # anti-aligned two-agent data
    assert theoretical(c,F(1,2),F(1,2))==F(1,6)
    c=(1,0,0,1)  # aligned two-agent data
    assert theoretical(c,F(1,2),F(1,2))==F(1,3)
    c=(1,0,0,2)  # aligned three-agent data
    assert theoretical(c,F(1,2),F(1,2))==F(1,2)
    print('Endpoint examples: anti-aligned N=2: 1/6; aligned N=2: 1/3; aligned N=3: 1/2')
    independent_absorption_checks()
    print('PASS')

if __name__=='__main__':test()
