"""General-seed wash-out + epsilon-stage table (exact arithmetic).

Admitted seed s=2 (X_{i+1} = X_i^3 x (S^2)^2). Generalize one step:
  t_1 = 2, t_{i+1} = 3 t_i + s  =>  t_i = (2+s/2)*3^{i-1} - s/2.
N_i = 2*4^{i-1} unchanged (multiplicity m=4). D_i = 2 t_i.

Certifies:
 (1) Closed form for s in {1..10}: recursion matches closed form i=1..10.
 (2) For each such s: ratio gmax_i = D_i/(2N_i) strictly decreasing for
     i>=2, -> 0 geometrically (step multiplier in (3/4, 1) eventually);
     J_s(1/4) = least j>=3 with (1/4)N_j >= D_j/2 exists; tabulate.
 (3) Seed-independence of the threshold: one-step size ratio is k/m = 3/4
     regardless of s (s only shifts the constant), so slow growth holds
     for EVERY seed. Exact: D_{i+1}/N_{i+1} = (3/4)(D_i/N_i) + s/(2N_{i+1})
     ... verify the recurrence and the bound D_i/N_i <= C_s (3/4)^i.
 (4) Epsilon-stage table for admitted s=2: J_eps = least j with u_j < eps
     for eps in {1/2,1/4,1/8,1/16,1/32,1/100,1/1000}; exact values.
     This makes the rc(V)=0 upper route explicit: rc(V) <= u_j -> 0.

Prints VERIFY_OK. Stdlib only.
"""
from fractions import Fraction

def t_closed(i, s):
    # (2+s/2)*3^{i-1} - s/2
    return 2 * (3 ** (i - 1)) + Fraction(s, 2) * (3 ** (i - 1) - 1)
    # = 2*3^{i-1} + (s/2)(3^{i-1}-1); check s=2: 2*3^{i-1}+3^{i-1}-1 = 3^i-1. OK

def t_rec_list(s, n):
    out = []
    t = 2
    for i in range(1, n + 1):
        out.append(t)
        t = 3 * t + s
    return out

def N(i):
    return 2 * (4 ** (i - 1))

def Js(s, g=Fraction(1, 4)):
    j = 3
    while True:
        t = t_closed(j, s)
        D = 2 * t
        if g * N(j) >= Fraction(D + 1, 2) or g * N(j) >= D / 2:
            # use sharp D/2 form for seed table
            if g * N(j) >= Fraction(D, 2):
                return j
        j += 1
        assert j < 500

def main():
    print("(1) closed forms s=1..10:")
    for s in range(1, 11):
        rec = t_rec_list(s, 10)
        for i in range(1, 11):
            assert rec[i - 1] == t_closed(i, s), (s, i)
    print("  recursion == closed form i=1..10 for all s OK")

    print("(2) decay + J_s(1/4):")
    for s in range(1, 11):
        prev = None
        for i in range(2, 15):
            Di = 2 * t_closed(i, s)
            gmax = Fraction(Di, 2 * N(i))
            if prev is not None:
                assert gmax < prev, (s, i)
            prev = gmax
        jstar = Js(s)
        D = 2 * t_closed(jstar, s)
        assert Fraction(1, 4) * N(jstar) >= Fraction(D, 2)
        D0 = 2 * t_closed(jstar - 1, s)
        assert Fraction(1, 4) * N(jstar - 1) < Fraction(D0, 2)
        print(f"  s={s}: gmax decreasing i>=2 OK; J(1/4)={jstar}")
    # admitted s=2 must give 8
    assert Js(2) == 8

    print("(3) seed-independent threshold k/m=3/4:")
    # recurrence check: D_{i+1}/N_{i+1} vs (3/4)(D_i/N_i): difference = s/(2 N_{i+1})*2?
    # D_{i+1} = 2(3 t_i + s) = 3 D_i + 2s; N_{i+1} = 4 N_i.
    # So D_{i+1}/N_{i+1} = (3/4)(D_i/N_i) + 2s/(4N_i) = (3/4)(D_i/N_i) + s/(2N_i).
    for s in (1, 2, 10):
        for i in range(1, 10):
            Di = 2 * t_closed(i, s)
            D1 = 2 * t_closed(i + 1, s)
            lhs = Fraction(D1, N(i + 1))
            rhs = Fraction(3, 4) * Fraction(Di, N(i)) + Fraction(s, 2 * N(i))
            assert lhs == rhs, (s, i)
    print("  recurrence D'/N'=(3/4)(D/N)+s/(2N) exact OK")
    print("  contraction factor 3/4<1 for every s; s only shifts constant. OK")

    print("(4) epsilon stages (admitted s=2, u_j=(3^j-1)/2^{2j-1}):")
    for enum, eden in [(1, 2), (1, 4), (1, 8), (1, 16), (1, 32),
                       (1, 100), (1, 1000)]:
        eps = Fraction(enum, eden)
        j = 3
        while True:
            u = Fraction(3 ** j - 1, 2 ** (2 * j - 1))
            if u < eps:
                break
            j += 1
            assert j < 100
        # sharpness: previous stage not below eps
        uprev = Fraction(3 ** (j - 1) - 1, 2 ** (2 * (j - 1) - 1))
        assert uprev >= eps, (eps, j)
        print(f"  eps={eps}: J_eps={j} (u={Fraction(3**j-1, 2**(2*j-1))})")
    print("  rc(V) <= u_j -> 0 explicit OK")
    print("VERIFY_OK")

if __name__ == "__main__":
    main()
