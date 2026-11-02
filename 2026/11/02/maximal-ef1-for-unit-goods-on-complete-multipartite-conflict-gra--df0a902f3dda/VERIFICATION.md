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

# Verification and limits

The mathematical proof in `RESULT.md` is the primary basis for the claim. Run `python3 verify_multipartite.py` with Python 3 and no third-party dependencies. This checker constructs allocations deterministically and verifies the original graph-edge constraints and maximality against each unassigned good for each color class; it independently tests class-size EF1 and the case-three assigned-item bound.

The checker passed 7,517 finite graph/agent instances; 5,118 had unassigned goods. Exhaustion is over documented bounded families of complete multipartite part sizes, with additional seeded samples. No finite test establishes the universally quantified theorem, and the code does not claim external certification. Limitations and publication-priority risks are recorded in the mathematical result and review.
