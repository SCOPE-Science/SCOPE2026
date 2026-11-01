"""Independent exact checks of Catalan-tree cherry–Sackin mixed moments.

No external packages are required. This finite checker does not replace the
formal-power-series and asymptotic proofs.
"""
from fractions import Fraction
from functools import lru_cache
from math import comb, exp, lgamma, log, pi, sqrt

@lru_cache(None)
def trees(n):
    if n == 1:
        return (None,)
    return tuple((l, r) for i in range(1, n)
                 for l in trees(i) for r in trees(n-i))

def stats(tree):
    if tree is None:
        return 1, 0, 0
    nl, cl, sl = stats(tree[0])
    nr, cr, sr = stats(tree[1])
    return nl+nr, cl+cr+int(tree[0] is None and tree[1] is None), sl+sr+nl+nr

def formulas(n):
    B = comb(2*n-2, n-1)
    q = Fraction(4**(n-1), B)
    ec = Fraction(n*(n-1), 2*(2*n-3))
    es = n*(q-1)
    ecs = Fraction(n*n, 4)*q - Fraction(n*(n-1)*(n-2), 2*(2*n-3))
    cov = Fraction(n, 2*n-3)*(n-1-Fraction(n, 4)*q)
    vc = Fraction(n*(n-1)*(n-2)*(n-3), 2*(2*n-5)*(2*n-3)**2)
    return ec, es, ecs, cov, vc

def exact_dynamic(nmax=100):
    # Independent root-composition recurrences for counts and raw moments.
    t=[0]*(nmax+1)
    c=[0]*(nmax+1)
    s=[0]*(nmax+1)
    m=[0]*(nmax+1)
    f=[0]*(nmax+1) # sum of C(C-1)
    t[1]=1
    for n in range(2,nmax+1):
        for i in range(1,n):
            j=n-i
            t[n] += t[i]*t[j]
            c[n] += c[i]*t[j]+t[i]*c[j]
            s[n] += s[i]*t[j]+t[i]*s[j]+n*t[i]*t[j]
            m[n] += m[i]*t[j]+t[i]*m[j]+c[i]*s[j]+s[i]*c[j]+n*(c[i]*t[j]+t[i]*c[j])
            f[n] += f[i]*t[j]+t[i]*f[j]+2*c[i]*c[j]
        if n==2:
            c[n]+=1
            m[n]+=2
    return t,c,s,m,f

def main():
    assertions=0
    for n in range(2,12):
        sample=trees(n)
        ct=Fraction(len(sample))
        assert len(sample)==comb(2*n-2,n-1)//n; assertions+=1
        ec=sum(stats(t)[1] for t in sample)/ct
        es=sum(stats(t)[2] for t in sample)/ct
        ecs=sum(stats(t)[1]*stats(t)[2] for t in sample)/ct
        ec2=sum(stats(t)[1]**2 for t in sample)/ct
        EC,ES,ECS,COV,VC=formulas(n)
        assert (ec,es,ecs)==(EC,ES,ECS); assertions+=3
        assert ecs-ec*es==COV; assertions+=1
        assert ec2-ec**2==VC; assertions+=1
        assert COV<0 if n>=4 else COV==0; assertions+=1
    t,c,s,m,f=exact_dynamic(120)
    for n in range(2,121):
        ec,es,ecs,cov,vc=formulas(n)
        assert t[n]==comb(2*n-2,n-1)//n; assertions+=1
        assert Fraction(c[n],t[n])==ec; assertions+=1
        assert Fraction(s[n],t[n])==es; assertions+=1
        assert Fraction(m[n],t[n])==ecs; assertions+=1
        assert Fraction(m[n],t[n])-ec*es==cov; assertions+=1
        assert Fraction(f[n]+c[n],t[n])-ec**2==vc; assertions+=1
    for n in range(121,201):
        ec,es,ecs,cov,vc=formulas(n)
        assert cov<0 and vc>0; assertions+=1
    for n in (100,1000,10000,100000):
        # Evaluation from the exact closed formula using log-gamma.
        q=exp((n-1)*log(4)-lgamma(2*n-1)+2*lgamma(n))
        cov=n/(2*n-3)*(n-1-n*q/4)
        limit=-sqrt(pi)*n**1.5/8
        assert abs(cov/limit-1)<(0.25 if n==100 else 0.08); assertions+=1
    print('PASS:', assertions, 'independent finite exact and asymptotic checks')

if __name__=='__main__': main()
