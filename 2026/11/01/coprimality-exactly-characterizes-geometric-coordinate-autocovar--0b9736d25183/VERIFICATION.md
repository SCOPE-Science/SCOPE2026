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

# Verification details

Run `python3 checker.py` with the Python standard library. The checker builds all affine itinerary branches and exact rational starting-point intervals, independently of the Fourier proof. It verifies 82 exact covariance identities, including coprime all-lag cases through time four and noncoprime exact second-lag cases. The implementation reports the total number of integrated affine pieces. These finite evaluations do not establish the theorem for all integers or all times; the written Fourier argument does. No external independent audit or formal proof check has been performed.
