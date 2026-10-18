#!/usr/bin/env python3
"""Exact symbolic and independent small-matrix checks for the two-row rook Padé positivity theorem.
Requires SymPy; NumPy is used only for an optional larger-matrix check.
"""
import sympy as S

h,n=S.symbols('h n', real=True)
D=lambda t:t*t+6*t+12
g=lambda t:t/D(t)
r=lambda t:(t*t-6*t+12)/D(t)
A=lambda q:(q**3+8)*h**4+24*(q+2)*h**3-12*(q*q-4*q-16)*h*h+288*h+144
B=lambda q:-(q**3-8*q-8)*h**4+24*(q+2)*h**3+12*(q*q+4*q+8)*h*h+72*(q+2)*h+144
count=0

def verify(claim):
    global count
    assert claim
    count+=1

common=D(2*h)*D(n*h)*D((n+2)*h)
verify(S.factor(g(2*h)+(n-1)*(g((n+2)*h)-g(n*h))-2*n*h*A(n)/common)==0)
verify(S.factor(g(n*h)+g((n+2)*h)-g(2*h)-2*n*h*B(n)/common)==0)
P=h**3*(n+2)*(n*n+2*n+4)+12*h*h*(n+2)**2+72*h*(n+2)+144
verify(S.factor(g(2*h)+g(n*h)-g((n+2)*h)-2*h*h*n*P/common)==0)
verify(S.factor(A(n).subs(h,8/n)+16*(39*n**4-592*n**3-1536*n**2-1536*n-2048)/n**4)==0)
for q in range(2,18):
    roots=S.Poly(A(q),h).count_roots(0,S.oo)
    verify(roots==0)
    if 7<=q<=17:
        st=S.sturm(A(q),h)
        def pattern(vals):
            return ''.join('+' if v>0 else '-' if v<0 else '0' for v in vals)
        left=pattern([v.subs(h,0) for v in st])
        right=pattern([S.LC(S.Poly(v,h)) for v in st])
        verify(left=='++---')
        verify(right==('+++--' if q<=14 else '++++-'))
for q in range(18,35):
    verify(S.Poly(A(q),h).count_roots(0,S.oo)==2)
    verify(S.Poly(B(q),h).count_roots(0,S.oo)==1)
    verify(A(q).subs(h,S.Rational(8,q))<0)
    step=S.sqrt(S.Rational(12,q))
    verify(S.simplify(A(q).subs(h,step))>0)
    verify(S.simplify(B(q).subs(h,step))>0)
for q in range(2,18):
    verify(S.Poly(B(q),h).count_roots(0,S.oo)==(0 if q<=3 else 1))

# Full-matrix checks at exact rational timesteps; compare direct Pade inverse to orbit formulas.
for q in range(2,7):
    e=S.ones(q,1)
    Lq=q*S.eye(q)-e*e.T
    L2=S.Matrix([[1,-1],[-1,1]])
    L=S.kronecker_product(L2,S.eye(q))+S.kronecker_product(S.eye(2),Lq)
    for step in [S.Rational(1,5),S.Rational(2,5),S.Rational(4,5),S.Rational(7,5)]:
        N=12*S.eye(2*q)-6*step*L+step*step*L*L
        M=12*S.eye(2*q)+6*step*L+step*step*L*L
        T=N*M.inv()
        a=12*step*A(q).subs(h,step)/(D(2*step)*D(q*step)*D((q+2)*step))
        b=12*step*B(q).subs(h,step)/(D(2*step)*D(q*step)*D((q+2)*step))
        c=S.Rational(6,q)*(g(2*step)+g(q*step)-g((q+2)*step))
        verify(all(sum(T.row(j))==1 for j in range(2*q)))
        verify(S.simplify(T[0,q]-a)==0)
        verify(S.simplify(T[0,1]-b)==0)
        verify(S.simplify(T[0,q+1]-c)==0)
        verify(all(T[j,j]>0 for j in range(2*q)))
# Exact sign witness in the 36-vertex case: positive, negative, positive, negative.
for step,expected in [(S.Rational(1,3),True),(S.Rational(2,5),False),
                      (S.Rational(4,5),True),(S.Rational(6,5),False)]:
    ap=A(18).subs(h,step);bp=B(18).subs(h,step)
    verify((ap>=0 and bp>=0)==expected)
    verify((ap<0)==(step==S.Rational(2,5)))
    verify((bp<0)==(step==S.Rational(6,5)))
print('VERIFY_OK exact checks:',count)
