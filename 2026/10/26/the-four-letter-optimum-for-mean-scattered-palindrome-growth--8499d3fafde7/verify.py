"""Independent finite checks for mean distinct scattered palindromes.

The mathematical proof handles arbitrary finite support and all lengths. This
checker samples exact rational distributions and exhaustive source words only.
"""
from fractions import Fraction as F
from itertools import product


def cauchy(a, b, n):
    return [sum((a[j]*b[k-j] for j in range(k+1)), F(0))
            for k in range(n+1)]


def predicted(weights, nmax):
    s1 = [F(0)]*(nmax+1)
    s2 = [F(0)]*(nmax+1)
    for p in weights:
        g=[F(0)]+[p*(1-p)**(j-1) for j in range(1,nmax+1)]
        for j in range(nmax+1): s1[j]+=g[j]
        gg=cauchy(g,g,nmax)
        for j in range(nmax+1): s2[j]+=gg[j]
    # H(z) = (S1+S2)/(1-S2), G(z) = H(z)/(1-z)
    h=[F(0)]*(nmax+1)
    for j in range(1,nmax+1):
        h[j]=s1[j]+s2[j]+sum((s2[t]*h[j-t] for t in range(1,j+1)), F(0))
    g=[];running=F(0)
    for x in h:
        running+=x;g.append(running)
    return g


def actual(weights,n):
    counts=F(0)
    cases=0
    for w in product(range(len(weights)),repeat=n):
        prob=F(1)
        for v in w:prob*=weights[v]
        # Independent subsequence set enumeration, positional masks.
        subseq=set()
        for mask in range(1,1<<n):
            u=tuple(w[j] for j in range(n) if mask & (1<<j))
            if u==u[::-1]: subseq.add(u)
        counts+=prob*len(subseq);cases+=1
    return counts,cases


def run():
    dist=[([F(1,2),F(1,2)],10),
          ([F(1,3),F(2,3)],9),
          ([F(1,3)]*3,7),
          ([F(1,2),F(1,3),F(1,6)],7),
          ([F(1,4)]*4,6)]
    checked=0
    for weights,nmax in dist:
        p=predicted(weights,nmax)
        assert p[0]==0
        for n in range(nmax+1):
            v,c=actual(weights,n)
            assert v==p[n], (weights,n,v,p[n])
            checked+=c
    # Sharp identity at z=4/5, exact rational arithmetic.
    trials=[[F(1,4)]*4,[F(1,2)]*2,[F(1,3)]*3,
            [F(1,2),F(1,4),F(1,4)],
            [F(2,5),F(1,5),F(1,5),F(1,5)],
            [F(1,5)]*5,[F(1,6)]*6]
    equality=[]
    for ps in trials:
        score=sum(((4*p/(1+4*p))**2 for p in ps),F(0))
        assert score<=1
        equality.append(score==1)
    assert equality==[True,False,False,False,False,False,False]
    from sympy import symbols, factor
    z=symbols('z')
    g=z/(4-3*z)
    gf=factor((4*g+4*g*g)/((1-z)*(1-4*g*g)))
    assert factor(gf-8*z*(2-z)/((1-z)*(4-5*z)*(4-z)))==0
    print(f'VERIFY_OK distributions={len(dist)} exhaustive_source_words={checked} '
          'sharp_bound_trials=7 exact_q4_gf=true')

if __name__=='__main__':run()
