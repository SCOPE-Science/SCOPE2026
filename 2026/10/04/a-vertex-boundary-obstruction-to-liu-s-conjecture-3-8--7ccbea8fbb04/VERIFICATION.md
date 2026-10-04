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

The proof is analytic. The critical steps checked are the internal angle-bisector formula, the limits as the interior point approaches \(C\), the exact simplification
\[
b^2-\frac{ab((a+b)^2-c^2)}{(a+b)^2}=\frac{b(ac^2-(a-b)(a+b)^2)}{(a+b)^2},
\]
and the strict-sign transfer by continuity.

For the \(3\)-\(4\)-\(5\) triangle, exact rational arithmetic gives \(w_c^2=160/9\) and boundary defect \(-16/9\). The bundled checker also evaluates the original defect at several interior points on \(P_\varepsilon=(\varepsilon,4-2\varepsilon)\); these finite evaluations are consistency checks only and are not used to prove the neighborhood statement.

The literature comparison included the exact 2012 source statement, a 2016 open-access follow-up using the same distance and angle-bisector objects, and a 2018 full-text follow-up. Exact-formula and alias searches found no covering prior statement. The remaining risk is unindexed or differently worded prior work.
