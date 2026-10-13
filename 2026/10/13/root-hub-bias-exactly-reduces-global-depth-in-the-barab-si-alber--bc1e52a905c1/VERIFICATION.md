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

The proof in `RESULT.md` is analytic. The accompanying checker independently enumerates all preferential-attachment parent histories through
\[
n=9.
\]

Each parent history is assigned its exact rational probability under degree-proportional attachment. The replay constructs degrees and root depths directly and verifies
\[
\mathbb E R_n
=
\frac{2\Gamma(n-\tfrac12)}
{\sqrt{\pi}\,\Gamma(n-1)},
\]
using an equivalent rational product in the code,
\[
\mathbb E P_n
=
\frac{n-1}{2}(H_{n-1}+1),
\]
and
\[
\operatorname{Cov}(R_n,P_n)
=
-\mathbb E R_n\,B_n.
\]

The checker also verifies through \(n=300\), using exact rational arithmetic, that the covariance recurrence, normalized recurrence, positive-sum representation, and harmonic closed form are mutually consistent.

The asymptotic constant is checked numerically only as a diagnostic. Its proof uses the gamma-ratio asymptotic and
\[
H_{n-2}-H_{2n-3}\to-\log2.
\]

Finite enumeration and numerical asymptotics are not used as proofs for arbitrary \(n\).

Independent audit has not been performed.

Exact replay result: `VERIFY_OK sizes=8 weighted_histories=46233 history_checks=8 finite_formula_checks=30 recurrence_checks=894 asymptotic_checks=3`.
