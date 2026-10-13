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

Run `python3 verify.py` with Python 3.9 or later. It requires only the standard library and uses `fractions.Fraction` throughout; no simulation or external dataset is needed.

The executable performs exact checks of all specified level covariances and the integrated \(5/18\) identity for \(5\le n\le74\), independently recurses the Kingman merger chain for \(3\le n\le15\), and fully enumerates all labeled merger histories for \(2\le n\le7\). The latter total is 59,602 histories. A successful run prints `VERIFIED: 5715 exact identities; 59602 complete labeled coalescent merger histories (n=2..7)`.

These finite verifications cannot prove the all-\(n\) result. Its proof relies on uniform-composition counting, conditional cherry regression, and elementary rational summation in `RESULT.md`. The clock rate and the terminal branch convention must match the assumptions there.
