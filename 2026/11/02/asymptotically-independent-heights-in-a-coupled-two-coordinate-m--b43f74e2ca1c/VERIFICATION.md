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

Run `python moran_height_checker.py` with Python 3. The self-contained code checks overlapping pair-marker probabilities against exact rational enumeration for three q values and thresholds 2–5, excludes incompatible same-coordinate markers, exhaustively checks the height/marker pathwise equivalence through eight updates, and checks finite-state recursion against the limiting profile. There were 156987 passed assertions.

The infinite-size theorem is proved analytically through the precise marker geometry, the strict inequality \(2q-1<q^2\), a geometric-series summation, and the published local-dependence point-process Poisson bound. No finite enumeration certifies the asymptotic estimates, and no independent audit has yet occurred.
