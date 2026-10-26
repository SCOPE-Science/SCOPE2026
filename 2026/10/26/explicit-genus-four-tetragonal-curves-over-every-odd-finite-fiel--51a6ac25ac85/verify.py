"""Exact finite cross-checks for explicit genus-four curves over odd fields.

Requires Python 3 and SymPy; no network or external data files.
Universal smoothness follows from the branch-locus argument in RESULT.md,
not from sampling finite fields.
"""
from itertools import combinations, product
from sympy import symbols, diff, expand, groebner, Integer


def nonresidue(p):
    return next(c for c in range(2, p) if pow(c, (p-1)//2, p) == p-1)


def parameter(p):
    t = 2 if p == 7 else 3 if p == 13 else 1
    k = (t**3 + t)**2 % p
    assert k and ((27*k)**2-16) % p, (p,t,k)
    return t, k


def verify_prime(p):
    c=nonresidue(p)
    t,k=parameter(p)
    x,y,z,w = symbols('x y z w')
    vs=(x,y,z,w)
    Q=x*y-z*z+c*w*w
    F=y**3+x*x*y+2*y*(z*z+c*w*w)-k*x**3
    # The six minors of the two-row Jacobian: singular iff all vanish.
    minors=[expand(diff(Q,vs[i])*diff(F,vs[j])-diff(Q,vs[j])*diff(F,vs[i]))
            for i,j in combinations(range(4),2)]
    for pivot in range(4):
        others=[var for i,var in enumerate(vs) if i!=pivot]
        subs={vs[pivot]: Integer(1)}
        basis=groebner([Q.subs(subs),F.subs(subs)]+[h.subs(subs) for h in minors],
                       *others, modulus=p, order='grevlex')
        assert list(basis)==[Integer(1)], (p,pivot,basis)
    P=(1,t*t,t,0)
    assert (P[0]*P[1]-P[2]**2+c*P[3]**2)%p==0
    assert (P[1]**3+P[0]**2*P[1]+2*P[1]*(P[2]**2+c*P[3]**2)-k*P[0]**3)%p==0
    N=0
    for pivot in range(4):
        for tail in product(range(p),repeat=3-pivot):
            x0,y0,z0,w0=([0]*pivot+[1]+list(tail))
            if (x0*y0-z0*z0+c*w0*w0)%p==0 and (y0**3+x0*x0*y0+2*y0*(z0*z0+c*w0*w0)-k*x0**3)%p==0:
                N+=1
    return c,k,N


def verify_segre_identity():
    a,b,e,d=symbols('a b e d')
    # x=a*e, y=b*d, u=a*d, v=b*e;
    # u^2+v^2=2(z^2+c*w^2) over a splitting field.
    x,y,u,v=a*e,b*d,a*d,b*e
    k=symbols('k')
    lhs= y**3+x*x*y+y*(u*u+v*v)-k*x**3
    rhs=(b**3+b*a*a)*(d**3+d*e*e)-k*a**3*e**3
    assert expand(lhs-rhs)==0


def main():
    assert (27*4)**2-16==2**7*7*13
    verify_segre_identity()
    for p in [3,5,7,13,17]:
        c,k,n=verify_prime(p)
        print('p=%d c=%d kappa=%d N(F_p)=%d chart_groebner=OK'%(p,c,k,n))
    print('VERIFY_OK')

if __name__ == '__main__':
    main()
