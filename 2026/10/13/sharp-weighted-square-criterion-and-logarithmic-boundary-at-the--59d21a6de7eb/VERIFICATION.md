---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification

The proof is analytic. For finite tails \(T_j=\sum_{i=j}^N\varepsilon_i\), direct telescoping verifies
\[
S_N=\sum_{j=1}^N j\varepsilon_j(T_j+T_{j+1}),
\]
with \(T_{N+1}=0\). Cauchy--Schwarz then gives \(S_N\le4W_N\). The source Proposition 1 gives \(W_N\le S_N\) for positive decreasing perturbations.

For the sharpness family \(\varepsilon_n=n^{-3/2}\), the proof uses only the integral estimate
\[
\sum_{i=j}^Ni^{-3/2}\ge2\left(j^{-1/2}-(N+1)^{-1/2}\right),
\]
which yields \(4H_N-16\le S_N\le4H_N\). Thus the constant \(4\) is optimal without relying on numerical convergence.

The logarithmic conclusions reduce to the classical convergence tests for \(\sum 1/[n(\log n)^{2p}]\) and, on the boundary, \(\sum 1/[n\log n(\log\log n)^{2q}]\).

`verify.py` replays the finite identity and inequalities on exact rational data and computes the sharpness ratios by a linear-time tail recursion. Those computations are checks only; the infinite conclusions and optimality are proved above.
