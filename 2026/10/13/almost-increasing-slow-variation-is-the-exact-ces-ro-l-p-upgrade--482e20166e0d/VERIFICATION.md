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

For \(G(x)=xL(x)\) and the de Bruijn normalization \(b_n^p=n\widetilde L(n)\), the proof uses
\[
G(b_n^p)\sim n,
\qquad n/b_n^2\to0.
\]
For \(H(x)=x^pL(x^p)\) and any \(\eta\in(0,2-p)\), Potter's inequality ensures a constant \(C\) with
\[
\frac{x^2}{b_n^2}\le C\frac{H(x)}{H(b_n)}
\quad (A\le x\le b_n)
\]
for sufficiently large fixed \(A\) and large \(n\). This bounds the quadratic contribution of centered truncated sums by the weighted Cesàro tail. Almost increase controls the complementary \(p\)-moment of the tails. Doob, von Bahr--Esseen, and elementary maximal estimates yield the full conclusion.

When almost increase fails, the rare-spike rows have \(q_m=1/[m v_m L(v_m)]\), \(n_m\sim u_mL(u_m)\), and
\[
E\left[(M_{n_m}/b_{n_m})^p\right]
\ge(1+o(1))\frac{L(u_m)}{mL(v_m)}\ge(1+o(1))m^2.
\]
The spike occurrence probability is at most \(n_mq_m=O(1/m)\), and the weighted Cesàro expectation per active row is exactly \(1/m\).

The standalone `verify.py` uses only the Python standard library. It checks a representative decreasing slowly varying weight \(L(x)=1/\log(e+x)\), solving its exact inverse scale \(G(x)=n\) by bisection, and evaluates the lower-bound ratio for four exact two-scale choices. It also tests the analytic peak/trough formulas for a slowly varying weight that remains above one but violates almost increase. The exact inverse norming used for the check is asymptotically equivalent to the de Bruijn norming in the theorem.

Expected successful line:
`VERIFY_OK ratios=4.000,9.000,16.000,25.000 oscillation=unbounded`.

The finite calculations illustrate only consequences of the analytic proof and do not establish the infinite implications.
