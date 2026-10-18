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

# Computational checks

Run `python3 verify_matched_apex.py` using Python 3's standard library. It implements the proof's legal moves on a specified hub and fixed perfect matching and enumerates every weak composition of \(4r\) for \(r=1,2,3,4\): respectively 15, 495, 18,564, and 735,471 configurations. For every one, the procedure terminates with a positive number of pebbles at the hub and none elsewhere. A separate recursive reachability search verifies one nonstackable configuration of size \(4r-1\) for each of these orders: \((1,1,1)\) for \(r=1\), and a configuration with zero at the hub, \(2r+1\) on one leaf, zero on its mate and one on every other leaf for \(r=2,3,4\).

These are complete **finite** checks for the stated small cases, not a proof of general lower sharpness. The all-order upper bound follows from the parity/gathering argument in `RESULT.md`. No independent audit has been performed.
