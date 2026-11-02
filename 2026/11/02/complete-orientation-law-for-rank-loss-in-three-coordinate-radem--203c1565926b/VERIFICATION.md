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

# Reproducible checks
Run `python3 verify.py` from this package's directory. The program uses only the Python 3 standard library and computes exact rational probabilities, with no Monte Carlo estimation or network access.

The program exhaustively enumerates all \(8^L\) possible sign-column configurations for \(L=2,3,4\), for all 124 nonzero integer normals in \(\{-2,-1,0,1,2\}^3\): 372 exact rank-deficiency, rank-zero, and mean-square-loss comparisons. The program computes the projected rank solely from integer cross products. Analytically, this equals the rank of the projected columns for any full-row-rank matrix with the stated kernel.

Only finite examples are computed. The proof's classification of all real kernel orientations and every integer \(L\ge2\) is deductive, not a claim of exhaustive numerical testing of uncountably many normal vectors. The Gaussian comparison follows from absolute continuity, not simulation.
