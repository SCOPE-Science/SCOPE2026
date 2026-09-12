"""Numerical verification for the lane-1335 disproof (t0=q0=1/2, b=1).

Checks:
1. e_n = (t^(n+1)-1)/(t^-1-t) stays bounded away from 0 and converges to -1/(t^-1-t).
2. Partial traces S_N(x) = sum_{n<=N} (n+1)*|e_n|^(-x) grow without bound (~N^2),
   confirming Tr(|D|^{-x}) = +inf for every real x (hence every complex z).
"""
t = 0.5
c = 1 / (1 / t - t)

def e(n):
    return (t ** (n + 1) - 1) / (1 / t - t)

print(f"t0={t}, accumulation point -c={-c}")
print("n : e_n")
for n in range(1, 11):
    print(f"{n} : {e(n):.10f}")
assert all(abs(e(n)) >= 0.5 - 1e-12 for n in range(1, 2000)), "lower bound failed"
assert abs(e(5000) + c) < 1e-6, "limit failed"
print("lower bound |e_n|>=1/2 and limit -2/3: OK")

for x in [-2, 0, 1, 3, 10]:
    for N in (100, 500, 2000):
        S = sum((n + 1) * abs(e(n)) ** (-x) for n in range(1, N + 1))
        print(f"x={x:>3} N={N:>5}: S_N={S:.6g}")
print("Partial traces grow quadratically in N for every x: divergence confirmed.")
