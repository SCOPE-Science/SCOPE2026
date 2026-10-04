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

The proof is symbolic and valid for every \(n\ge3\) and \(1\le k<n\). The critical checks are:

1. Directly derive the inverse actions of \(b\) and \(c\) and confirm that a deleting inverse \(c\)-step occurs exactly when states \(1\) and \(2\) have occupancy pattern occupied/empty.
2. Normalize a shortest inverse avoidance path by replacing any nondeleting inverse \(c\)-step with the inverse \(b\)-step that gives the same set or a subset.
3. Convert each deleting step to an occupied-to-empty cyclic boundary \(p\), with exact cost \(p\) for \(p\ne0\) and \(n\) for \(p=0\), and exact update \((P\setminus\{p\})-p\).
4. Check that \(B_{n,k}\) alone has its only boundary at \(0\), after which the tail targets force boundary \(n-1\) repeatedly.
5. Replay \(w_{n,k}=(cb^{n-2})^{k-1}cb^{n-1}\) and verify its length and avoidance property.

`artifacts/verify_wielandt_avoiding.py` independently builds exact image-subset distances. The recorded run checks all target subsets for every \(3\le n\le11\), including uniqueness of the maximizer, and replays the explicit witness for every parameter pair through \(n=40\). The output file ends in `VERIFY_OK`.

The finite computation does not certify cases beyond its enumerated range; those cases are covered by the proof, not by extrapolation.
