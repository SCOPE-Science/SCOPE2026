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

# Verification protocol

Execute from the extracted directory, with Python 3 and optionally SymPy available:

```sh
python classify.py > recreated_classification.json
python secondary_scan.py
python verify.py
```

`classify.py` uses only the standard library. It enumerates all 32767 nonzero coefficient masks; calculates seven rational line restrictions; checks binary-quartic squarefreeness using polynomial Euclidean GCD, including the infinity point; applies all seven rational Jacobian conditions; then enumerates all 168 projective matrices and both orbits. The expected file `classification.json` contains all 25 masks. Compare the JSON contents of the recreated output with `classification.json` without relying on field key order.

`secondary_scan.py` uses a separate binomial-coefficient substitution implementation and a direct first-derivative test on all coefficient masks; it must reproduce the same exact 25-element set. `verify.py` uses SymPy's polynomial arithmetic for independently constructed restrictions, then computes the unit ideal for the homogeneous polynomial and its partial derivatives on each affine chart of each candidate curve. This is a geometric check over the algebraic closure, not a finite extension-point enumeration. Its reference output is `verification_output.txt`; the scan reference output is `secondary_output.txt`.

The certificate establishes the **finite classification in the specified coefficient space**. It does not prove historical publication priority, all-field generalization, abstract curve isomorphism classes, or independent validation.
