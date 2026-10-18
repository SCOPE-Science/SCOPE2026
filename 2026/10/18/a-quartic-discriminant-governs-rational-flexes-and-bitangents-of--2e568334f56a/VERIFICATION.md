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
# Verification and reproducibility

Run `python3 verify_tangent_quartic.py` using Python 3 and SymPy. The program separately enumerates every rational point and rational line for prime fields \(3,5,7,11,13,17,19\), calculates the unique tangent line from the gradient, and matches tangent fiber counts against the quartic equation and the restriction quadratic. It checks the quartic adjugate identity by exact symbolic expansion. The reported \((q,k,F,B,E)\) values are \((3,2,5,4,4)\), \((5,4,5,13,13)\), \((7,1,11,23,23)\), \((11,1,9,62,62)\), \((13,1,15,84,84)\), \((17,4,15,146,146)\), and \((19,1,21,180,180)\). It also computes that each of the seven companion quartics has no geometric singularities, by proving the relevant polynomial ideals contain one on each affine chart.

Each prime-field computation is finite and exhaustive for that field, but does not establish the all-prime-power theorem; the uniform symbolic argument is in `RESULT.md`. The program uses SymPy for the quartic smoothness checks; if SymPy is absent it explicitly skips those checks. The result makes no assertion about geometric smoothness of the original plane-filling curves away from rational points and no assertion about smoothness of every companion quartic.
