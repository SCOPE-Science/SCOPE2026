---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

PASS. For a stationary two-state CTMC with availability fraction pi in (0,1), transition total rate gamma>0, conditional detection d in (0,1], and fixed first/last visits 0,T, the exact non-detection probability is v D P(x) D P(y) D P(z) D 1. Independent symbolic expansion matched alpha^4+c alpha^2 y+c alpha(alpha+beta y)(x+z)+c(c+beta^2 y)xz where x*y*z=R=e^{-gamma T}. Coefficient of x+z strictly positive; AM-GM at fixed y forces x=z=u, and u in [sqrt(R),1]. Differentiate the one-variable expression to Fprime=2c H(u)/u^3, H=c u^4+alpha^2 u^3-alpha beta R u-alpha^2 R. H"" is positive, H(sqrt R)<0 for 0<R<1, H(1) changes sign exactly at Tc=gamma^{-1} log[alpha(alpha+beta)/(alpha^2+c)]. Hence the endpoint doublets are unique for 0<T<=Tc (d<1), and otherwise there is a unique interior symmetric schedule 0,a,T-a,T. At uniform u0=R^(1/3), H(u0)=-(1-d)R^(4/3), proving strict outer gaps shorter than middle for d<1. For d=1, H factors and gives unique equal spacing at all T. Independent exact-rational matrix/product and derivative checks corroborate the analytical global proof.

## originality

PASS

Best-of-knowledge, theorem/implication-based comparison of relevant primary literature; a failed search by itself does not prove historical priority. Closest known published results address different parameters/objects or only more general frameworks.

## value

PASS

PASS. A sharp optimal-design transition between replicated instantaneous endpoint observations and four separated surveys gives a substantive, nontrivial scheduling result for a natural two-state ecological availability model. The quantitative criterion and uniqueness offer guidance for mathematical study-design analysis, while physical assumptions and lack of field validation are explicit.

The dated certificate retains the supplied scientific assessment, sources and limitations.
