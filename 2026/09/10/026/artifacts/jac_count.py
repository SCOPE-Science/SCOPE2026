"""Direct Jacobian counts by reduced-Mumford-divisor enumeration over F_p.
Run: python3 jac_count.py
For each p in {5,7,11}: enumerates monic u of degree <= 2 and v with
v^2 = f mod u (exact GF(p) arithmetic), plus identity; asserts totals
71, 120, 136 matching counts.py's (N1^2+N2)/2-p formula values.
Prints JAC_COUNT_OK.
"""
import sys

def make(p):
    def pnorm(a):
        a = [c % p for c in a]
        while len(a) > 1 and a[-1] == 0:
            a.pop()
        return a
    def pmul(a, b):
        r = [0]*(len(a)+len(b)-1)
        for i, ca in enumerate(a):
            for j, cb in enumerate(b):
                r[i+j] = (r[i+j]+ca*cb) % p
        return pnorm(r)
    def pdivmod(a, b):
        a = pnorm(a)
        b = pnorm(b)
        db = len(b)-1
        inv = pow(b[db], -1, p)
        q = [0]*max(1, len(a)-db)
        while len(a)-1 >= db and not (len(a) == 1 and a[0] == 0):
            c = a[-1]*inv % p
            d = len(a)-1-db
            q[d] = (q[d]+c) % p
            for i in range(db+1):
                a[d+i] = (a[d+i]-c*b[i]) % p
            a = pnorm(a)
        return pnorm(q), a
    def peval(a, t):
        return sum(c*pow(t, i, p) for i, c in enumerate(a)) % p
    return pnorm, pmul, pdivmod, peval

def count_J(p, f):
    pnorm, pmul, pdivmod, peval = make(p)
    n = 1  # identity
    # deg 1: u = x - a
    for a in range(p):
        fa = peval(f, a)
        n += sum(1 for y in range(p) if (y*y) % p == fa)
    # deg 2: monic x^2 + b x + c, v = d x + e
    for b in range(p):
        for c in range(p):
            u = [c, b, 1]
            for d in range(p):
                for e in range(p):
                    v = [e, d]
                    vv = pmul(v, v)
                    N = max(len(vv), len(f))
                    num = pnorm([(vv[k] if k < len(vv) else 0)
                                 - (f[k] if k < len(f) else 0)
                                 for k in range(N)])
                    _, r = pdivmod(num, u)
                    if len(r) == 1 and r[0] == 0:
                        n += 1
    return n

def main():
    expect = {3: 27, 5: 71, 7: 120, 11: 136}
    for p, want in expect.items():
        f = [c % p for c in [1, 4, 0, -5, 0, 1]]
        n = count_J(p, f)
        print(f"#J(F{p}) by Mumford enumeration: {n} (want {want})")
        assert n == want, (p, n, want)
    print("JAC_COUNT_OK")

if __name__ == "__main__":
    main()
