"""Brute-force verification for lane-360 corner-recurrence claims (stdlib only).

Checks on cyclic models X=Z/PZ, S=T=cyclic shift, A={0..q-1}:
 (V1) explicit control inequality  |blockavg - d^3| <= a*b + d^{3/2}(a+b)
      for anchored AND shifted MxM blocks (shift-uniformity via unitarity).
 (V2) periodic obstruction: for P=2q, every (m,n) with 7q/8 < m,n <= q
      satisfies c(m,n) < d^3/2 = 1/16  => empty square of side q-floor(7q/8).
 (V3) density conversion: blockavg >= 3d^3/4  =>  E-density >= d^3/4.
Writes artifacts/verify_log.json and prints VERIFY_OK.
"""
import json
import math
import os

HERE = os.path.dirname(os.path.abspath(__file__))


def make_model(P, q):
    A = set(range(q))
    d = q / P

    def f(x):
        return 1.0 if (x % P) in A else 0.0

    def c(m, n):
        s = 0
        for x in range(P):
            if f(x) * f(x + m) * f(x + n):
                s += 1
        return s / P

    def avg_fns(N, M=0, L=0):
        # u(x)=N^{-1} sum_{m=M+1}^{M+N} f(x+m), v likewise with L
        # a=||u-d||_2, b=||v-d||_2, blockavg=N^{-2} sum c(m,n) over block
        u = [sum(f(x + m) for m in range(M + 1, M + N + 1)) / N for x in range(P)]
        v = [sum(f(x + n) for n in range(L + 1, L + N + 1)) / N for x in range(P)]
        a = math.sqrt(sum((t - d) ** 2 for t in u) / P)
        b = math.sqrt(sum((t - d) ** 2 for t in v) / P)
        blk = sum(c(m, n) for m in range(M + 1, M + N + 1)
                  for n in range(L + 1, L + N + 1)) / (N * N)
        return blk, a, b

    return d, f, c, avg_fns


def check_V1():
    rows = []
    for (P, q, N, M, L) in [(16, 8, 5, 0, 0), (16, 8, 5, 3, -2),
                            (32, 12, 7, -5, 4), (200, 100, 60, 37, -11)]:
        d, f, c, avg_fns = make_model(P, q)
        blk, a, b = avg_fns(N, M, L)
        lhs = abs(blk - d ** 3)
        rhs = a * b + (d ** 1.5) * (a + b)
        ok = lhs <= rhs + 1e-12
        rows.append({"P": P, "q": q, "N": N, "M": M, "L": L,
                     "lhs": lhs, "rhs": rhs, "ok": ok})
        assert ok, ("V1 failed", rows[-1])
    return rows


def check_V2():
    rows = []
    for q in [8, 16, 40, 80, 400]:
        P = 2 * q
        d, f, c, _ = make_model(P, q)
        tau = d ** 3 / 2  # 1/16
        m0 = int(math.floor(7 * q / 8)) + 1
        side = q - int(math.floor(7 * q / 8))
        worst = 0.0
        for m in range(m0, q + 1):
            for n in range(m0, q + 1):
                v = c(m, n)
                worst = max(worst, v)
                assert v < tau, ("V2 failed", q, m, n, v)
        rows.append({"q": q, "P": P, "m0": m0, "side": side,
                     "tau": tau, "max_c_on_square": worst, "ok": True})
        assert side >= q / 8 - 1
    return rows


def check_V3():
    P, q, N = 200, 100, 60
    d, f, c, avg_fns = make_model(P, q)
    blk, a, b = avg_fns(N, 0, 0)
    tau = d ** 3 / 2
    E = sum(1 for m in range(1, N + 1) for n in range(1, N + 1)
            if c(m, n) >= tau)
    dens = E / (N * N)
    # implication under test: blk >= 3d^3/4  =>  dens >= d^3/4
    premise = blk >= 0.75 * d ** 3 - 1e-12
    bound = (blk - tau) / (1 - tau)  # avg <= dens*1 + (1-dens)*tau
    row = {"P": P, "q": q, "N": N, "blockavg": blk, "density": dens,
           "required_avg": 0.75 * d ** 3, "required_density": d ** 3 / 4,
           "premise_holds": premise, "linear_bound": bound}
    assert premise, row
    assert dens + 1e-12 >= bound and dens + 1e-12 >= d ** 3 / 4, row
    return row


def main():
    log = {"V1_control_inequality": check_V1(),
           "V2_empty_square_obstruction": check_V2(),
           "V3_density_conversion": check_V3(),
           "status": "VERIFY_OK"}
    with open(os.path.join(HERE, "verify_log.json"), "w") as fh:
        json.dump(log, fh, indent=2)
    print("VERIFY_OK")
    print(json.dumps({"V2_sides": [r["side"] for r in log["V2_empty_square_obstruction"]],
                      "V3": log["V3_density_conversion"]}, indent=2))


if __name__ == "__main__":
    main()
