from decimal import Decimal, getcontext

getcontext().prec = 60
D = Decimal

def dpow(a, x):
    a = D(a)
    x = D(x)
    return (x * a.ln()).exp()

def T_bounds(s_text, N=5000):
    s = D(s_text)
    total = D(0)
    for n in range(2, N + 1):
        nn = D(n)
        total += D(1) / (D(n - 1) * dpow(nn + 1, D(2) * s))
    # For n>N, with m=n-1>=N:
    # 1/((n-1)(n+1)^(2s)) <= m^(-(2s+1)).
    # Since x^(-(2s+1)) decreases,
    # sum_{m=N}^\infty m^(-(2s+1))
    # <= integral_{N-1}^\infty x^(-(2s+1)) dx.
    tail_upper = dpow(D(N - 1), -D(2) * s) / (D(2) * s)
    return total, total + tail_upper

def R_bounds(s_text, N=5000):
    s = D(s_text)
    lo, hi = T_bounds(s_text, N)
    b = dpow(2, D(1) - s)
    return b + lo.sqrt(), b + hi.sqrt()

for s in ("1.4135", "1.4135195", "1.41352", "1.414"):
    lo, hi = R_bounds(s)
    print(s, "R_lower-1 =", lo-D(1), "R_upper-1 =", hi-D(1))
