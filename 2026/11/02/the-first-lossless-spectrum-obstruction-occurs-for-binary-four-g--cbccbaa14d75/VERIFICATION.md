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

# Complete computational verification

Execute `python3 verify_kgram.py` with Python 3 standard library. The output `verify_kgram_output.txt` records `ALL_CHECKS_PASSED`.

The program constructs the finite de Bruijn state graph and enumerates all reachable (vertex, observed-edge-mask) states with repeated edges allowed. In a second closure it forbids repeated edges. A third, independent strongly connected component criterion checks each of the 255 nonempty three-gram masks and 65,535 nonempty four-gram masks. Complete mask-set equality is asserted, not just numerical equality. It independently enumerates all binary words through length ten as a further three-gram check.

The finite proof is exhaustive because repeated-edge walks are represented by a finite state and the reachability closure proceeds until no new states remain. Reported evidence does not establish any result for longer windows or larger alphabets. Independent mathematical validation has not been performed.
