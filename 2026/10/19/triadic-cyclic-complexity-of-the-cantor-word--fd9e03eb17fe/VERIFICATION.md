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

The mathematical proof in `RESULT.md` covers all integer scales \(k\ge0\). An accompanying standalone Python program (`verify_cantor.py`) provides finite, independent checks of its constructions.

Run `python3 verify_cantor.py` with Python 3. It uses a morphism generator and an independent base-three digit generator and confirms equality of the resulting prefixes. It computes distinct factors, minimal cyclic rotations, exact class counts, and the coincidence of prefix and reversed-prefix necklaces at all scales \(k=0,1,\ldots,7\). It checks that these coincidences occur precisely at power-of-two weights and that no additional cyclic classes exist.

Executed output ended in `VERIFY_OK`. At the largest tested length, \(N=2187\), it verified \(4373\) distinct factors and \(249\) conjugacy classes. Finite checks do not constitute a proof of the assertion for all \(k\); the proof depends on block separation and the unique odd circular gap.

Independent audit has not been performed.
