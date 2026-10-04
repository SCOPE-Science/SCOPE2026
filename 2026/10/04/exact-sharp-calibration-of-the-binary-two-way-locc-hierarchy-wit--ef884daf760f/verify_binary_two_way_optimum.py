#!/usr/bin/env python3
from decimal import Decimal, getcontext
from fractions import Fraction

getcontext().prec = 80
D = Decimal

def dec(fr):
    return D(fr.numerator) / D(fr.denominator)

def E_decimal(p):
    return (D(6) - (D(4)-D(3)*p).sqrt() - (D(4)+D(5)*p).sqrt()) / D(16)

def Fprime_decimal(p):
    return -D(3)/(D(2)*(D(4)-D(3)*p).sqrt()) + D(5)/(D(2)*(D(4)+D(5)*p).sqrt())

def main():
    p = Fraction(8, 15)

    # Exact reversible stationary equation.
    assert 25*(Fraction(4)-3*p) == 9*(Fraction(4)+5*p)
    assert Fraction(4)-3*p > 0
    assert Fraction(4)+5*p > 0

    # Exact endpoint derivative signs after elementary evaluation.
    # F'(0) = 1/2 and F'(1) = -2/3.
    assert Fraction(1,2) > 0
    assert Fraction(-2,3) < 0

    pd = dec(p)
    root15 = D(15).sqrt()
    exact_min = D(3)/D(8) - root15/D(15)
    one_way = D(1)/D(8)
    advantage = (D(4)*root15-D(15))/D(60)
    sep = (D(3)-D(5).sqrt())/D(8)
    sep_gap = D(5).sqrt()/D(8)-root15/D(15)

    assert abs(E_decimal(pd)-exact_min) < D("1e-70")
    assert abs((one_way-exact_min)-advantage) < D("1e-70")
    assert abs((exact_min-sep)-sep_gap) < D("1e-70")
    assert advantage > 0
    assert sep_gap > 0
    assert abs(Fprime_decimal(pd)) < D("1e-70")
    assert Fprime_decimal(D(0)) > 0
    assert Fprime_decimal(D(1)) < 0

    # Supplementary finite stress test.
    n = 200000
    best_p = D(0)
    best_e = E_decimal(best_p)
    for k in range(1, n+1):
        q = D(k)/D(n)
        val = E_decimal(q)
        if val < best_e:
            best_e = val
            best_p = q
    step = D(1)/D(n)
    assert abs(best_p-pd) <= step
    assert best_e >= exact_min-D("1e-70")
    assert best_e-exact_min < D("1e-10")

    print("VERIFY_OK")
    print("p_star =", pd)
    print("E_star =", exact_min)
    print("one_way_error =", one_way)
    print("exact_advantage =", advantage)
    print("separable_error =", sep)
    print("separable_gap =", sep_gap)
    print("grid_points =", n+1)
    print("grid_best_p =", best_p)
    print("grid_best_error =", best_e)

if __name__ == "__main__":
    main()
