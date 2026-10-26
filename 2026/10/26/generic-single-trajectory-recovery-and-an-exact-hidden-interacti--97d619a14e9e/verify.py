from itertools import combinations
from fractions import Fraction
from math import prod
import sympy as sp

def det_rat(mat):
    m=[list(map(Fraction,row)) for row in mat]
    n=len(m); d=Fraction(1)
    for k in range(n):
        q=next((i for i in range(k,n) if m[i][k]),None)
        if q is None:return Fraction(0)
        if q!=k: m[k],m[q]=m[q],m[k];d=-d
        piv=m[k][k]; d*=piv
        for i in range(k+1,n):
            c=m[i][k]/piv
            for j in range(k+1,n): m[i][j]-=c*m[k][j]
            m[i][k]=Fraction(0)
    return d

for n in range(3,7):
    rates=[2**j for j in range(n)]
    for i in range(n):
        exps=sorted([0]+rates+[rates[j]+rates[k] for j,k in combinations(range(n),2) if i not in (j,k)])
        p=1+n+(n-1)*(n-2)//2
        assert len(exps)==p==len(set(exps)),(n,i,exps)
        matrix=[[e**d for e in exps] for d in range(p)]
        actual=det_rat(matrix)
        expected=prod(exps[k]-exps[j] for j in range(p) for k in range(j+1,p))
        assert actual==expected and actual!=0
    print('exact uncoupled trajectory Wronskian nonzero, n=',n,', per-row p=',p)

# An explicit HARD triadic coefficient, rather than a zero-coefficient witness.
n=3
xs=sp.symbols('x1 x2 x3'); x1,x2,x3=xs
Fs=[sp.Rational(1)+x2*x3/sp.Integer(20),sp.Rational(2)+x1*x3/sp.Integer(20),sp.Rational(4)+x1*x2/sp.Integer(20)]
field=[xs[i]*Fs[i] for i in range(n)]
for i in range(n):
    mon=[sp.Integer(1),*xs,prod(xs[j] for j in range(n) if j!=i)]
    assert len(mon)==5
    rows=[]; current=mon
    for k in range(5):
        rows.append([sp.expand(f).subs(dict.fromkeys(xs,1)) for f in current])
        current=[sp.expand(sum(sp.diff(f,x)*v for x,v in zip(xs,field))) for f in current]
    det=sp.det(sp.Matrix(rows))
    assert det!=0,(i,det)
    print('nonzero hard-triad Wronskian for i=',i+1,' determinant=',det)

# A global positive nonstationary orbit with exact structural ambiguity.
f1=1-x1+x2
f2=-1+x1-x2
f3_pair=2-x3
f3_hard=1-x3+x1*x2
assert sp.expand(x1*f1*x2+x2*f2*x1)==0
assert sp.expand(f3_hard-f3_pair-(x1*x2-1))==0
initial={x1:1,x2:1,x3:1}
assert any(sp.expand(v).subs(initial)!=0 for v in [x1*f1,x2*f2,x3*f3_hard])
print('exact invariant surface and nonstationarity checked')
print('all checks PASS')
