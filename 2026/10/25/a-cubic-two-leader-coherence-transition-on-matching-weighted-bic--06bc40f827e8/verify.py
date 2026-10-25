"""Exact reproducibility checks for weighted matched biclique two-leader coherence.

Requires SymPy >= 1.11. Run: python verify.py
This finite replay supplements, and does not replace, the analytical proof.
"""
import sympy as s
from itertools import combinations

n, t = s.symbols('n t', integer=True, positive=True)
p = n - 2 + 2*t
q = 2*(n - 1 + t)
R = {
    'same': 1/p + 1/n,
    'matched': (2-2/n)/p + 2/(n*q),
    'cross': (1-2/n)/p + 1/n + 2/(n*q),
}
B = {
    'same': 1/p**2 + 1/n**2,
    'matched': (2-2/n)/p**2 + 2/(n*q**2),
    'cross': (1-2/n)/p**2 + 1/n**2 + 2/(n*q**2),
}
score = {typ: B[typ]/R[typ]+n*R[typ]/2 for typ in R}
P = (2*(n+2)*t**3 + (4*n*n-n-14)*t*t
     + 2*(n-2)*(n*n-n-4)*t - (n-2)*(n*n-3))
Q = 2*t*t + 2*(n-2)*t - (n-2)
D = n*(n+t-1)*(n+2*t-2)*(2*n+2*t-3)
Xnum = (n-2)*t*t + (2*n*(n-1)+4)*t + n*(n-1)**2-2
Xden = ((n+t-1)*(n+2*t-2)
        *(2*n*n+4*n*t-5*n+2*t*t-4*t+2))
assert s.simplify(score['matched']-score['same']+P/D)==0
assert s.simplify(score['same']-score['cross']-Xnum/Xden)==0
assert s.simplify(R['matched']-R['same']+Q/(n*(n+t-1)*(n+2*t-2)))==0
assert s.simplify(R['same']-R['cross']-1/((n+t-1)*(n+2*t-2)))==0
assert s.simplify(s.rem(P,Q,t)+n*(n-2)/2)==0
assert s.simplify(P.subs(t,s.Rational(1,2))-(n-1))==0
assert s.simplify(P.subs(t,0)+(n-2)*(n*n-3))==0
print('SYMBOLIC_OK: spectral-score gaps, resistance gaps, cubic root ordering')

def laplacian(nn, tt):
    N=2*nn
    M=s.zeros(N)
    for i in range(nn):
        for j in range(nn):
            w=tt if i==j else s.Integer(1)
            M[i,i]+=w;M[nn+j,nn+j]+=w
            M[i,nn+j]-=w;M[nn+j,i]-=w
    return M

def typ(nn,i,j):
    if i>=nn and j>=nn or i<nn and j<nn:
        return 'same'
    a=i%nn;b=j%nn
    return 'matched' if a==b else 'cross'

def grounded_trace(L,i,j):
    ids=[x for x in range(L.rows) if x not in (i,j)]
    return s.trace(L.extract(ids,ids).inv())

count=0
for nn in range(3,8):
    for tt in [s.Rational(0),s.Rational(1,10),s.Rational(2,5),
               s.Rational(1,2),s.Rational(1),s.Rational(3)]:
        L=laplacian(nn,tt)
        vals={}
        for i,j in combinations(range(2*nn),2):
            kind=typ(nn,i,j)
            actual=grounded_trace(L,i,j)
            rr={v:s.simplify(z.subs({n:nn,t:tt})) for v,z in R.items()}
            bb={v:s.simplify(z.subs({n:nn,t:tt})) for v,z in B.items()}
            T=2*(s.Rational(nn-1,1)/(nn-2+2*tt)+s.Rational(nn-1,nn)
                   +s.Rational(1,2)/(nn-1+tt))
            expected=s.factor(T-bb[kind]/rr[kind]-nn*rr[kind]/2)
            assert s.simplify(actual-expected)==0,(nn,tt,i,j,kind,actual,expected)
            vals[(i,j)]=actual
            count+=1
        optimal=min(vals.values())
        classes={typ(nn,*edge) for edge,value in vals.items() if value==optimal}
        Pval=s.sign(P.subs({n:nn,t:tt}))
        expected_classes={'matched'} if Pval<0 else ({'same'} if Pval>0 else {'matched','same'})
        assert classes==expected_classes,(nn,tt,classes,expected_classes)
print('FINITE_OK:',count,'exact grounded inverses and exhaustive pair comparisons')
assert s.simplify((R['same']-R['matched']).subs({n:3,t:s.Rational(2,5)}))==s.Rational(1,108)
assert s.simplify((score['matched']-score['same']).subs({n:3,t:s.Rational(2,5)}))==s.Rational(5,342)
print('COUNTEREXAMPLE_OK: n=3, t=2/5; resistance gap 1/108, coherence gap 5/342')
print('VERIFY_OK')
