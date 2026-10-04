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

The proof is analytic. The accompanying checker uses exact rational arithmetic.

For random positive rational triples \(a,b,c\) and rational \(t\in(0,1)\), it independently differentiates
\[
\kappa(t)=\frac{M_4(t)}{V(t)^2}
\]
through the central moments and verifies the exact identity
\[
\kappa'(t)
=
\frac{4abc\,t(1-t)}{V(t)^3}
\left[(3b-1)t+(3c-1)\right].
\]

It checks the two exact boundary formulas
\[
\kappa(0)=h(c),
\qquad
\kappa(1)=h(a),
\]
the uniform identity
\[
\kappa(t)=\frac32,
\]
and, whenever the stationary point is interior, the identities
\[
t_*=\frac{1-3c}{3b-1}
\]
and
\[
\kappa(t_*)=
\frac{1-3(ab+bc+ca)}
{ab+bc+ca-9abc}.
\]

The script also verifies the derivative sign reversal in the minimum and maximum regimes and monotonicity samples in the remaining regime.

Finite replay checks the algebra; it is not used to infer the universal theorem.

Independent audit has not been performed.

Exact-rational replay result: `VERIFY_OK derivative_checks=30000 boundary_checks=60000 uniform_checks=55 stationary_checks=23630 phase_checks=9701 monotone_checks=20286`.
