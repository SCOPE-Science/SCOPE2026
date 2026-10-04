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
The published Jacobian at the liver-free fixed point is diagonal with entries \(1+h(1-g)\) and \(1+h(1-\zeta)\). For \(0<g<1\), \(0<\zeta<1\), and \(h>0\), both entries are strictly greater than one, which proves the source classification directly.

The bundled `verify.py` checks an exact rational witness from the stated domain. It confirms \(g=1/2\), \(\zeta=1/3\), and \(h=1\) give multipliers \(3/2\) and \(5/3\), while the two thresholds printed in the source are \(-4\) and \(-3\). Hence the printed sink inequality holds even though the fixed point is a source.

The checker is supporting arithmetic only. The universal conclusion follows from the exact sign inequalities and does not rely on a finite numerical search. No global-dynamics or partial-infection-bifurcation claim is verified here.
