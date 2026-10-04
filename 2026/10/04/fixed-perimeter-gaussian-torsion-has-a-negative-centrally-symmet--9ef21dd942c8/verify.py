#!/usr/bin/env python3
import math


def hyp1f1(a, b, z, tol=1e-16, max_terms=10000):
    term = 1.0
    total = 1.0
    for n in range(max_terms):
        term *= (a + n) / (b + n) * z / (n + 1.0)
        total2 = total + term
        if abs(term) <= tol * abs(total2):
            return total2
        total = total2
    raise RuntimeError("Kummer series did not converge")


def lambda_k(k):
    m0 = hyp1f1(k/2.0, k+1.0, 0.5)
    m1 = hyp1f1(k/2.0+1.0, k+2.0, 0.5)
    return k + (k/(2.0*(k+1.0))) * (m1/m0)


def radial_from_support(theta, eps, k=2):
    # h=1+eps cos(k phi). Solve theta=phi+atan(h'/h) by Newton,
    # then return sqrt(h^2+h'^2).
    phi = theta
    for _ in range(20):
        h = 1.0 + eps*math.cos(k*phi)
        hp = -eps*k*math.sin(k*phi)
        hpp = -eps*k*k*math.cos(k*phi)
        q = hp/h
        F = phi + math.atan(q) - theta
        qp = (hpp*h-hp*hp)/(h*h)
        dF = 1.0 + qp/(1.0+q*q)
        phi -= F/dF
    h = 1.0 + eps*math.cos(k*phi)
    hp = -eps*k*math.sin(k*phi)
    return math.hypot(h,hp)


def main():
    A = math.sqrt(math.e)-1.0
    s = math.sqrt(math.e)
    assert 2.0 - 8.0*A < 0.0

    rows=[]
    for k in range(2,22,2):
        lam=lambda_k(k)
        coeff=A/(2.0*s)*(2.0-A*(k*k+2.0*lam))
        assert lam > k
        assert coeff < 0.0
        rows.append((k,lam,coeff))

    # Support-to-radial expansion rho=1+eps f-eps^2 f'^2/2+O(eps^3)
    # for f=cos(2 theta), tested by halving epsilon and observing cubic scaling.
    theta=0.37
    errs=[]
    for eps in (1e-3,5e-4,2.5e-4):
        exact=radial_from_support(theta,eps,2)
        f=math.cos(2*theta)
        fp=-2*math.sin(2*theta)
        approx=1.0+eps*f-0.5*eps*eps*fp*fp
        errs.append(abs(exact-approx))
    assert errs[1] < errs[0]/6.0
    assert errs[2] < errs[1]/6.0

    # Zero-mode normalization check against the exact ball radial derivative.
    # T'(R)=R F(Z), Z=R^2/2, F(Z)=(cosh Z-1)/Z.
    z=0.5
    F=(math.cosh(z)-1.0)/z
    Fp=(z*math.sinh(z)-(math.cosh(z)-1.0))/(z*z)
    Tpp=F+Fp  # R=1, so R^2=1
    G=1.0-math.exp(-0.5)
    a=-(math.sqrt(math.e)-1.0)
    b=-1.0
    w=math.exp(-0.5)
    expansion_Tpp=-G*b-a*w
    assert abs(Tpp-expansion_Tpp) < 2e-14

    for k,lam,coeff in rows:
        print(f"k={k:2d} lambda={lam:.15f} HessianCoeff={coeff:.15f}")
    print(f"all_mode_margin={2.0-8.0*A:.15f}")
    print("VERIFY_OK")

if __name__ == '__main__':
    main()
