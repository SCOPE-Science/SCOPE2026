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

# Reproducible checks and limits

Run the included self-contained Python 3 script with `python3 verify.py`. It uses only the standard library. The script enumerates positive cyclic run-gap compositions for each size, independently constructs the induced-component profile of every proper vertex subset, computes the predicted rank enumerator, and directly checks all partial bijections for order preservation and reflection on crowns of four, six and eight vertices. The script also verifies the first three high-rank coefficient formulas (including the four-vertex exception) and the numerical sequence of total monoid cardinalities through sixteen vertices. Each line `CROWN_OK` records the successful checks at that size; the final `VERIFY_OK` is emitted only when all assertions pass.

These computations are exhaustive only in the finite ranges indicated. The proof for all finite crowns is the component classification and the cyclic rooting argument in `RESULT.md`, not an extrapolation from these outputs. No independent mathematical audit has been conducted.
