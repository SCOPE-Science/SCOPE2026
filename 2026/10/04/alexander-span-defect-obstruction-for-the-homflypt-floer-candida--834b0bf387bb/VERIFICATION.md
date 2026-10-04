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

The proof was checked at each nontrivial interface.

The recent source fixes the HOMFLY–PT normalization so that \(P_K(1,z)=\nabla_K(z)\). Therefore specialization cannot create a \(z\)-degree larger than the original polynomial, and
\[
\operatorname{sp}\Delta_t(K)=\deg \nabla_K(z)\le\deg P_z(K).
\]

The standard concordance bounds give
\[
2|\tau(K)|\le2g_4(K)\le2g(K)
\]
and
\[
|s(K)|\le2g_4(K)\le2g(K).
\]
Thus failure of either target candidate forces the displayed strict Alexander-span inequality. The Alexander span is even for a knot because the Alexander polynomial is symmetric up to a monomial unit, so the defect below \(2g\) is at least \(2\).

The classical fibered-knot theorem was checked against Friedl–Vidussi's Annals record, whose abstract explicitly recalls that a fibered knot has Alexander polynomial of degree twice its genus.

The bundled arithmetic regression script prints:

`VERIFY_OK tuples=85305 tau_failure_tuples=10560 s_failure_tuples=10560`

This finite script checks only the logical arithmetic consequences of the premises. It is not used as evidence for the general knot-theoretic inequalities.

The independent-audit channel has not been performed.
