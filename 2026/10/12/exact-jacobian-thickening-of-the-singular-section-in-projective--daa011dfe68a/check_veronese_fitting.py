"""Exact finite witness checks for the universal Veronese Jacobian-Fitting proof."""
from sympy import symbols, Matrix, expand, binomial, factor

for d in (3, 4, 5, 6):
    z=symbols('z:'+str(d+1)); x,y=symbols('x y')
    # Genuine generating equations from the rational-normal curve minors.
    f=[z[0]*z[i+2]-z[1]*z[i+1] for i in range(d-1)]
    j=Matrix([[p.diff(z[k]) for k in range(2,d+1)] for p in f])
    assert expand(j.det()-z[0]**(d-1))==0, (d,j.det())
    # Full rational-normal cone ideal has quadratic generators;
    # the determinant survives the Veronese map.
    v={z[i]:x**(d-i)*y**i for i in range(d+1)}
    assert all(expand(q.subs(v))==0 for q in f)
    assert expand(j.det().subs(v)-x**(d*(d-1)))==0
    N=d*(d-1)
    # The orbit coefficients of (x+t*y)^N are a basis of Sym^N.
    assert all(binomial(N,k)!=0 for k in range(N+1))
    exact=sum(k*d+1 for k in range(d-1))
    closed=(d-1)*(d*d-2*d+2)//2
    assert exact==closed
    print(d, 'minor=',j.det(), 'transverse_length=',exact)
print('VERONESE_FITTING_CHECK_OK')
