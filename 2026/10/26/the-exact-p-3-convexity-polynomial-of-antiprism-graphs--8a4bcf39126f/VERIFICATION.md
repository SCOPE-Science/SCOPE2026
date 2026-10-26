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

# Reproduction and limits

Run `python3 verify_antiprism.py` with Python 3 standard library beside `RESULT.md`. The code enumerates every vertex subset of the graph \(A_n\) for \(3\le n\le10\) using the defining outside-neighbour test, separately enumerates sets avoiding all graph distances one and two, verifies the rational generating coefficients by an explicit recurrence, and counts cyclic ternary words through \(n=12\). The run terminates with `VERIFY_OK`. These finite checks are consistency checks only. The all-order statement rests on the connected triangle propagation, gap description, and the log-determinant identity in the proof. Independent external auditing has not been performed.
