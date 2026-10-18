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

# Verification notes

The standalone `verify.py` constructs the finite hole process's directed tree weights independently and compares their exact symbolic current against the theorem. It checks the zero-bias linear coefficient, second-order coefficient, and full parity defect using SymPy's exact rational simplification. It then solves the separate four-state stationary generator for six positive rate quadruples and eight biases, with six bias-reversal classifications and nine three-site consistency checks. All checks executed successfully.

The proof in `RESULT.md` is an exact finite-dimensional argument; the script is a reproducibility and arithmetic check, not a substitute for the proof. No finite computation purports to establish any infinite-system claim. The theorem is restricted to four sites, one hole and strictly positive hopping rates with \(|\varepsilon|<1\). No independent audit has been performed.
