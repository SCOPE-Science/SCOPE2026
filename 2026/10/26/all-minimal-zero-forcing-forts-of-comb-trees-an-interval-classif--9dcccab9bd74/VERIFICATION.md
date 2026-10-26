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

Execute `python3 verify.py` using a standard Python 3 interpreter. No libraries beyond the Python standard library and no external downloads are required. The script constructs each comb from its edges and examines every vertex subset, tests the fort condition directly at every outside vertex, and computes subfort existence dynamically for all smaller masks. These algorithms are independent of the auxiliary-graph proof. The exact family and size-distribution formulas are compared with the resulting exhaustive sets for all \(1\leq n\leq9\). The recorded 9 cases comprise \(349524\) subsets, \(2055\) forts, and \(95\) minimal forts. The recorded last line is `VERIFICATION_OK cases=9 subsets=349524 forts=2055 minimal=95`.

Checks establish finite premises and guard against small-boundary errors. Infinite validity follows only from the complete mathematical proof in `RESULT.md`. The supplied output was generated from the supplied script in the same package; no independent assessment has been performed.
