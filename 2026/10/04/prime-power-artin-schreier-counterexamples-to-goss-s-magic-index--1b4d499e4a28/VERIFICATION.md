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

The proof is uniform in \(q=p^s\); the finite computation below is only an independent check of a non-prime base field.

Run `python3 verify.py`. The script implements exact arithmetic in
\[
\mathbb F_{25}=\mathbb F_5[u]/(u^2-3)
\]
and then in
\[
K=\mathbb F_{25}[\theta]/(\theta^5-\theta-3).
\]
It verifies the five-step Frobenius orbit \(\theta^{25}=\theta+1\), checks the finite-field reciprocal-sum identity exactly at \(z=\theta\), and exhaustively verifies that the normalized finite-difference map \(h\mapsto\Delta_1(Yh)/m\) is a bijection on every monic degree-\(m-1\) polynomial for \(1\le m\le4\). The verified bijections force the Pascal recurrence, whose \(n=3\) coefficient vector is exactly \((1,2,3,4,0)\), the coefficient vector of \((1-X)^3\) in characteristic \(5\).

Expected terminal line:

`VERIFY_OK q=25 p=5 n=3 frobenius_orbit=5 reciprocal_sum=exact phi_sizes=1,25,625,15625 coefficients=1,2,3,4,0`

These finite checks corroborate every algebraic ingredient of the non-prime example. The infinite statement is proved by the symbolic Frobenius-orbit argument, the reciprocal-sum identity over \(\mathbb F_q\), and the finite-difference bijection for every \(1\le m<p\).
