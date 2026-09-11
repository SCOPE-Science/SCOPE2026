"""Hensel 1-dim Q3-family inside D: fix x1=x2=1, x3=1+3*t0, solve 2*x0^4+7+8-17*x3^4=0
for x0 = 1 mod 3. dF/dx0 at P0 = 8 = 2 mod 3 != 0, so Hensel lifts uniquely.
Log solutions mod 27 for t0 in 0..8 (i.e. x3 mod 27 in 1+3t0). Exact integer arithmetic."""
def lift(x3, k):
    # solve 2*x^4 = 17*x3^4 - 15  (mod 3^k), x=1 mod 3, by Hensel from x=1
    mod = 3**k
    rhs = (17*pow(x3,4,mod) - 15) % mod
    x = 1
    # Newton on f(x)=2x^4-rhs; f'(x)=8x^3, unit mod 3. Lift digit by digit base 3.
    for j in range(1, k):
        m = 3**(j+1)
        fx = (2*pow(x,4,m) - rhs) % m
        fp = (8*pow(x,3,m)) % m
        # fp invertible mod 3; inverse mod m via pow
        inv = pow(fp, -1, m)
        x = (x - fx*inv) % m
    assert (2*pow(x,4,mod) - rhs) % mod == 0
    assert x % 3 == 1
    return x
for t0 in range(9):
    x3 = 1 + 3*t0
    x0 = lift(x3, 3)
    assert (2*x0**4 + 7 + 8 - 17*x3**4) % 27 == 0
    print(f"x3={x3:3d} (mod27) -> x0={x0:3d} (mod27), check 2x0^4+15-17x3^4 = 0 mod27 OK")
print("HENSEL_FAMILY_OK: 9 distinct Q3-points of D logged (1-dim subdisc, x0=1 mod3, smooth: dF/dx0=2 mod3)")
