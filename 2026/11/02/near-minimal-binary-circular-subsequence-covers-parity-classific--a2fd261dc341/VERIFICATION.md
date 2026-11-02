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

The accompanying `verify.py` checks the cyclic equal-edge parity condition against an independently programmed greedy-arch circular-universality test for every binary word of lengths \(3,5,7,9,11,13,15,17\). It checks the direct set of scattered subsequences of every rotation for lengths through \(9\), and independently enumerates rotation and reversal orbits. It also checks the fixed-reflection count and that every admitted word has no nontrivial period. Run with `python verify.py` using Python's standard library; the success marker is `VERIFY_OK`.

The finite test covers \(174{,}760\) binary words for greedy comparison and \(680\) for direct scattered-subsequence comparison. It verifies the first eight \(k\)-instances, not the general infinite theorem; the latter is supported by the explicit combinatorial matching and parity proof in RESULT.md. No independent audit is claimed.
