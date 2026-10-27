"""Reproducible exact checks for the two-gap symmetric Fourier-atom zero theorem.

Requires Python 3 and sympy. Finite checks corroborate an independent
all-degree analytic proof; they are not a substitute for it.
"""
import sympy as s

x=s.Symbol('x')
P=s.Symbol('p')
num=0
for n in range(3,16):
    c=s.Rational(n-2,2*n-2) if n%2 else s.Rational(1,2)
    Q=s.Poly(s.expand(P*s.chebyshevt(n,x)+(1-P)*s.chebyshevt(n-2,x)), x)
    samples=[('below',c/2,n-2),('critical',c,n-2 if n%2 else n-1),('above',(c+1)/2,n)]
    if n%2:
        samples.insert(-1,('above_below_half',(c+s.Rational(1,2))/2,n))
    for label,p,real_count in samples:
        q=s.Poly(Q.as_expr().subs(P,p),x)
        assert q.degree()==n
        assert q.count_roots(-1,1)==real_count,(n,label,p,q.count_roots(-1,1),real_count)
        assert q.eval(1)==1
        assert q.eval(-1)==(-1)**n
        if label=='critical':
            multiplicity=3 if n%2 else 2
            assert all(s.diff(q.as_expr(),x,j).subs(x,0)==0 for j in range(multiplicity))
            assert s.diff(q.as_expr(),x,multiplicity).subs(x,0)!=0
        if label=='below':
            # Negative roots in t^2 are precisely the imaginary pair.
            vals=[complex(z) for z in s.nroots(q.as_expr(), maxsteps=250)]
            assert sum(abs(z.imag)>1e-6 for z in vals)==2
            assert all(abs(z.real)<1e-6 for z in vals if abs(z.imag)>1e-6)
        num+=1
print(f'PASS: {num} exact Sturm root counts and all critical multiplicity checks (degrees 3--15).')
for n in (3,4,5,6,7,9,10,15):
    c=s.Rational(n-2,2*n-2) if n%2 else s.Rational(1,2)
    for pp in (c/2,c,(c+1)/2):
        Q=(pp*s.chebyshevt(n,x)+(1-pp)*s.chebyshevt(n-2,x))
        for xx in (s.Rational(1,3),s.Rational(-2,5)):
            val=complex(Q.subs(x,xx).evalf(35))
            import cmath
            z=cmath.acos(float(xx))
            other=float(pp)*cmath.cos(n*z)+(1-float(pp))*cmath.cos((n-2)*z)
            assert abs(val-other)<1e-12
print('PASS: 48 independent Chebyshev/Fourier polynomial evaluations.')
for n in range(3,18):
    q=s.Poly(P*s.chebyshevt(n,x)+(1-P)*s.chebyshevt(n-2,x),x)
    if n%2:
        crit=s.Rational(n-2,2*n-2)
        assert s.diff(q.as_expr(),x).subs(x,0).factor()==(-1)**((n-1)//2)*(2*n-2)*(P-crit)
    else:
        assert q.as_expr().subs(x,0)==(-1)**(n//2)*(2*P-1)
print('PASS: 15 exact threshold-coefficient identities.')
print('All finite checks passed; infinite degree and uniqueness follow from the analytic argument.')
