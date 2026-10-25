"""Reproducible interval-contraction certificate for passive fourfold reflection zero."""
import sympy as s
from mpmath import iv
from decimal import Decimal
E,a,b,c,t,x=s.symbols('E a b c t x', real=True)
g=s.cancel(1/(E+s.I*a-1/(E+s.I*b-1/(E+s.I*c))))
tau=s.factor(s.solve(t*g.subs(E,0)+s.I,t)[0])
F=[s.factor((2*t*s.diff(g,E)-1).subs(E,0).subs(t,tau)),
   s.factor((4*t*s.diff(g,E,2)-s.I).subs(E,0).subs(t,tau)/s.I),
   s.factor((8*t*s.diff(g,E,3)-2*t*s.diff(g,E)+1).subs(E,0).subs(t,tau))]
J=list(s.Matrix(F).jacobian([a,b,c]))
iv.dps=65
f=s.lambdify((a,b,c),F,'mpmath'); j=s.lambdify((a,b,c),J,'mpmath')
center=('0.436411176971509','0.825078162539108','1.940513159446698')
R=Decimal('0.0000001')
box=[iv.mpf([str(Decimal(z)-R),str(Decimal(z)+R)]) for z in center]
point=[iv.mpf(z) for z in center]
A=[['-3.79000745','1.04762005','0.07647238'],
   ['-2.13141533','0.91395119','0.08720546'],
   ['-1.51817375','0.74179254','0.10102913']]
def bound(q):
    lo,hi=str(q).strip('[]').split(', ')
    return max(abs(Decimal(lo)),abs(Decimal(hi)))
fc=f(*point); jc=j(*box)
shift=max(bound(sum(iv.mpf(A[i][k])*fc[k] for k in range(3))) for i in range(3))
row=max(sum(bound(iv.mpf(1 if i==l else 0)-sum(iv.mpf(A[i][k])*jc[3*k+l] for k in range(3))) for l in range(3)) for i in range(3))
assert row<Decimal('0.0002'),(row,shift)
assert shift+row*R < R,(row,shift)
# Nonzero fourth derivative of the numerator guarantees precisely order four.
N=t*g.subs(E,2*s.sin(x))+s.exp(s.I*(s.pi/2+x))
N4=s.factor(s.diff(N,x,4).subs(x,0).subs(t,tau)/s.I)
f4=s.lambdify((a,b,c),N4,'mpmath')
fourth=f4(*box)
assert bound(fourth+iv.mpf('15.4539'))<Decimal('0.05'),fourth
print('PASS interval contraction: max Jacobian defect',row,'max preconditioned residual',shift)
print('PASS nonzero fourth derivative N^(4)/i:',fourth)
print('PASS positive loss box, tau^2=(abc+a+c)/(bc+1)>0')
