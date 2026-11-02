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

The analytic proof is in `RESULT.md`. Its critical block is a \(2\)-by-\(2\) matrix, and its global-block determinant is simplified using the critical equation. The included `verify.py` independently builds the graph, reconstructs every distance by breadth-first search, checks the distance categories, calculates the full centered powered-distance spectra at five exponents, and compares the global quadratic forms directly. It also checks the standard-block critical determinant.

Run `python verify.py` with Python 3 and NumPy installed. The recorded replay output was:

`PASS: critical exponent p=0.706863663237331; 136 independent structural and spectral checks across 16 graphs`

The tested parameters were \(r\in\{2,3,4,5\}\) and \(t=m-2r\in\{0,1,2,4\}\). This is supplemental finite evidence, not an exhaustive verification of the theorem. The all-parameter argument is a symbolic zero-sum-space decomposition together with a separate strict-positivity calculation for the possible competing modes. No independent audit has been conducted.
