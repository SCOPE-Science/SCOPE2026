"""Independent algebraic replay of the first sketched FOM and GMRES coefficients.

Standard-library Python 3; no external packages needed.
"""
import math
import random

r = random.Random(350084)
# SPD A=diag(1,4), b=(1,1) (not an eigenvector).
a = 2.5
d = 1.5
m = a*a+d*d
q = 4
# v=(1,1)/sqrt(2), w=(-1,1)/sqrt(2); Av=a*v+d*w.
for ell in (2,3,4,8,32,100):
    for _ in range(200):
        # Gaussian sketches of v and its perpendicular w.
        U=[r.gauss(0,1) for j in range(ell)]
        W=[r.gauss(0,1) for j in range(ell)]
        uu=sum(u*u for u in U)
        uw=sum(u*w for u,w in zip(U,W))
        ww=sum(w*w for w in W)
        # The sketch of Av is a U + d W.
        av=[a*u+d*w for u,w in zip(U,W)]
        p=sum(u*t for u,t in zip(U,av))
        vnorm=sum(t*t for t in av)
        if abs(p)<1e-13: continue
        cf=uu/p
        cg=p/vnorm
        # Direct least-squares and Galerkin equations.
        assert abs((uu-cf*p)) < 5e-10*(1+uu)
        assert abs((p-cg*vnorm)) < 5e-10*(1+p*p)
        # Independent orthogonal Gaussian representations, pointwise.
        f_ratio=1/(a+d*uw/uu)
        assert abs(cf-f_ratio) < 3e-11*(1+abs(cf))
        # qperp=(d*v-a*w)/sqrt(m), orthogonal to q=Av/sqrt(m).
        Q=[(a*u+d*w)/math.sqrt(m) for u,w in zip(U,W)]
        P=[(d*u-a*w)/math.sqrt(m) for u,w in zip(U,W)]
        qq=sum(t*t for t in Q)
        qp=sum(t*z for t,z in zip(Q,P))
        g_ratio=a/m+(d/m)*qp/qq
        assert abs(cg-g_ratio) < 3e-11*(1+abs(cg))
        # Exact unsketched Euclidean residual from b=(1,1).
        res_direct=(1-cg)**2+(1-4*cg)**2
        res_expanded=2*(1-2*a*cg+m*cg*cg)
        assert abs(res_direct-res_expanded) < 5e-11*(1+abs(res_direct))
        # True energy of x*=A^-1 b=(1,1/4).
        energy_direct=(1-cf)**2+4*(.25-cf)**2
        energy_split=(1-1/a)**2+4*(.25-1/a)**2 +2*a*(cf-1/a)**2
        assert abs(energy_direct-energy_split) < 5e-10*(1+abs(energy_direct))

# Check formula for density at Y=0 by independently normalized Student density.
for ell in (2,3,4,10,50):
    t0=-a*math.sqrt(ell)/d
    std_t_density=(math.gamma((ell+1)/2)/
        (math.sqrt(ell*math.pi)*math.gamma(ell/2)) *
        (1+t0*t0/ell)**(-(ell+1)/2))
    density_from_student=std_t_density*math.sqrt(ell)/d
    density_formula=(math.gamma((ell+1)/2)/
        (math.sqrt(math.pi)*d*math.gamma(ell/2)) *
        (1+a*a/(d*d))**(-(ell+1)/2))
    assert abs(density_from_student-density_formula) < 1e-12*(1+density_formula)

for ell in (3,4,7,15):
    var_cg = d*d/(m*m*(ell-2))
    residual=2*(1 -2*a*(a/m)+m*((a/m)**2+var_cg))
    expected=2*(d*d/m)*(ell-1)/(ell-2)
    assert abs(residual-expected) < 1e-12*(1+expected)

# Eigenvector case A diagonal, b=e1: no sketch randomness in either coefficient.
for ell in (2,3,9):
    U=[r.gauss(0,1) for _ in range(ell)]
    a0=7.0
    cf=sum(u*u for u in U)/sum(u*a0*u for u in U)
    cg=sum(u*a0*u for u in U)/sum((a0*u)**2 for u in U)
    assert abs(cf-1/a0)<1e-12
    assert abs(cg-1/a0)<1e-12
print('verification passed')
