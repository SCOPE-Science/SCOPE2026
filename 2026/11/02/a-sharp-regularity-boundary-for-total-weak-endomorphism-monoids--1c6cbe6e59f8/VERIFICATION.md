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

# Finite verification

Execute `python verify.py` using Python 3 with only its standard library. The script enumerates every total weak self-map and checks an explicit inner-inverse section condition for bipartite graphs of part sizes (1,1), (1,2), (1,3), (1,4), (2,2), (2,3), (2,4), and (3,3), plus every possible inner inverse on complete multipartite graphs with part sizes (1,1,1), (1,1,2), and (1,2,2). It directly constructs and tests a witness for (2,2,2). Expected final line: `VERIFY_OK`. The finite computations are corroborative; universal correctness follows from the mathematical argument in RESULT.md.

No independent mathematical audit has been performed.
