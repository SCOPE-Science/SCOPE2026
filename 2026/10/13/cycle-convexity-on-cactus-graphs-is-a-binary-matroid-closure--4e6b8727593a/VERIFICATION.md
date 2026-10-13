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
Run `python3 verify.py` from a directory containing the two embedded files `verify.py` and `verification_output.txt`. This uses only Python's standard library, enumerates all subsets on 15 explicit cactus profiles, compares iterative cycle closure with binary-vector closure, and directly calculates maximum sizes of convex-independent, Helly-independent and Radon-independent sets. It prints `PASS profiles=15 tested_subsets=3576` and the full per-profile record in `verification_output.txt`.

The checker is logically separate from the proof's pruning argument: it computes hulls by repeated infection, while the linear closure uses binary rank. The tests are exhaustive for their declared finite profiles, not for all graphs or for the infinite cactus family. The incidence-forest pruning proof in `RESULT.md` is the universal certificate; the computational checks do not establish any claims about non-cactus graphs or external verification.
