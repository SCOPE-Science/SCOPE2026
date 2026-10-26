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

# Verification record

The included `verify.py` uses only Python's standard library, and builds each partial bijection directly. For sizes \(n=1,2,3\), all ordered pairs are checked using two explicit empty-composition tests, independent of the domain-image kernel expression. The compressed kernel inertia is computed using exact rational symmetric congruence eliminations. For sizes \(n=1,2,3,4\), its determinant is checked modulo the primes \(101\) and \(1009\).

The resulting full matrix orders are \(2,7,34,209\) and the predicted inertias are, respectively, \((1,1,0)\), \((4,2,1)\), \((10,10,14)\), and \((38,32,139)\). The concluding program marker is `VERIFY_OK_ROOK_MUTUAL_ANNIHILATION_INERTIA`.

This provides finite corroboration, not exhaustive verification for all sizes. The universal proof is contained in `RESULT.md`, whose critical steps are the exact incidence compression and nonsingular rank-antitriangular homotopy. Real spectral signs and the retention of loops are essential scope restrictions. No independent mathematical audit has been performed.
