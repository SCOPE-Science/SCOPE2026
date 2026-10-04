#!/usr/bin/env python3
from decimal import Decimal, getcontext

getcontext().prec = 70
D = Decimal
r = D(3).sqrt()
two = D(2)

def P0(p):
    return (D(1)-p)/D(3)

def P1(p):
    return (two+r)*(two+p)/D(12)

def P2(p):
    return (two-r)*(two+p)/D(12)

def overlap(p):
    return (D(1)-p)/(two*(two+p))

def Q(p):
    return P0(p)+P1(p)

def S(p):
    return Q(p)*Q(p)-D(4)*P0(p)*P1(p)*overlap(p)

def E(p):
    return D(1)-(Q(p)+S(p).sqrt())/two

def Sprime(p):
    # Derivative of [20+8r+(4+8r)p-(3+4r)p^2]/48.
    return ((D(4)+D(8)*r)-two*(D(3)+D(4)*r)*p)/D(48)

def Qprime():
    return (r-two)/D(12)

def Hprime(p):
    return Qprime()+Sprime(p)/(two*S(p).sqrt())

def main():
    pstar = (D(45)-D(8)*r)/D(39)
    estar = (D(63)-D(32)*r)/D(117)
    eone = D(1)/D(2)-r/D(4)
    gap = (D(11)*r-D(18))/D(468)

    assert D(0) < pstar < D(1)
    assert abs(E(pstar)-estar) < D("1e-60")
    assert abs(E(D(1))-eone) < D("1e-60")
    assert abs((eone-estar)-gap) < D("1e-60")
    assert gap > 0

    # Posterior normalization for representative branch.
    for p in (D(0), pstar, D(1)):
        assert abs(P0(p)+P1(p)+P2(p)-D(1)) < D("1e-60")
        assert D(0) <= overlap(p) <= D(1)

    # Exact stationary relation in numerical high precision.
    assert abs(Hprime(pstar)) < D("1e-58")
    assert Hprime(D(0)) > 0
    assert Hprime(D(1)) < 0

    # Verify the factored squared-stationary identity at sample points.
    for k in range(21):
        p = D(k)/D(20)
        lhs = Sprime(p)*Sprime(p)-D(4)*Qprime()*Qprime()*S(p)
        rhs = ((p-D(1))*((D(18)+D(11)*r)*p-(D(14)+D(9)*r)))/D(216)
        assert abs(lhs-rhs) < D("1e-58")

    # Supplementary dense-grid stress test.
    n = 200000
    best_p = D(0)
    best_e = E(best_p)
    for k in range(1,n+1):
        p = D(k)/D(n)
        ep = E(p)
        if ep < best_e:
            best_e = ep
            best_p = p
    step = D(1)/D(n)
    assert abs(best_p-pstar) <= step
    assert best_e >= estar-D("1e-55")
    assert best_e-estar < D("1e-10")

    print("VERIFY_OK")
    print("p_star =", pstar)
    print("E_star =", estar)
    print("E_one_way =", eone)
    print("exact_gap =", gap)
    print("grid_points =", n+1)
    print("grid_best_p =", best_p)
    print("grid_best_E =", best_e)

if __name__ == "__main__":
    main()
