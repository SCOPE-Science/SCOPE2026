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

Run `python3 verify.py` with the standard Python 3 library. The program reconstructs all signed-permutation vertices in the two parameter chambers; enumerates every \(\binom{24}{4}\) candidate quadruple; computes determinant polynomials with exact integers; independently cross-checks all determinants with exact rational \(4\times4\) Leibniz determinants at two parameter values; and verifies all candidate parameter inequalities by exact rational Bernstein-basis coefficient positivity on the **complete** intervals.

The checker also computes vertex-supported maximizer counts at interior parameter values and each geometric endpoint, and verifies an exact polynomial certificate for the sharp overall occupancy lower bound. Both the 24-vertex chamber formula and the Bernstein interval certificate, rather than floating-point parameter sampling, establish the infinite-parameter statement.

No external audit or certification was performed. The result does not classify possible nonvertex equal-volume tetrahedra. Historical originality is assessed against inspected published literature, not independently certified.
