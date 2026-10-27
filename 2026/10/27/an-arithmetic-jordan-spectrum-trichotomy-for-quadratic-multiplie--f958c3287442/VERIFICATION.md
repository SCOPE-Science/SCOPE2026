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

The executable `verify.py` uses pure Python 3. Its test data are generated from the six quadratic coefficients and do not use precomputed historical certificates. It constructs the multiplication operator directly on all sixteen squarefree monomials and checks the predicted first-power and second-power ranks in \(729\) exhaustive \(\mathbb F_3\) cases, \(360\) \(\mathbb F_5\) cases, \(360\) \(\mathbb F_7\) cases, and \(343\) deterministic cases over \(\mathbb F_9\). Independently it exhaustively counts all six-dimensional coefficient configurations over \(\mathbb F_3\), \(\mathbb F_5\), and \(\mathbb F_7\); the counts match each of the seven polynomial formulas. It also enumerates every product triple over \(\mathbb F_9\) and verifies the characteristic-three intersection count.

Run `python3 verify.py`; a successful run prints `VERIFY_OK_DEGREE_TWO_SQUAREFREE_JORDAN`. These are finite checks, not a proof in arbitrary field size. The uniform proof is the determinant/hafnian rank-stratification argument in `RESULT.md`. No independent audit has been performed.
