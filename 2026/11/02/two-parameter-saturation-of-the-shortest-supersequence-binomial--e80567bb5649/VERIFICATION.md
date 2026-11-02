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

The proof is a four-stage argument: a Parikh-vector length obstruction; exact terminal-letter and boundary characterization; a forced-step compression and expansion bijection; and binomial counting. The finite verifier exercises a separately implemented shortest-supersequence recurrence, direct subsequence tests, and the actual compression/expansion procedures.

Reproduce with `python3 verify.py`; compare with `verification_output.txt`. The standalone code requires no third-party dependencies and performs 84 DP cases, 14,706 bridge tests, and 5,960 brute-force word checks.

These computations are finite corroboration only. The infinite-parameter result rests on the written inverse proof, including the termination and terminal-letter arguments. The result says nothing about deletion-minimal supersequences of larger-than-shortest length; that question is unproved here. Independent mathematical audit: not performed.
