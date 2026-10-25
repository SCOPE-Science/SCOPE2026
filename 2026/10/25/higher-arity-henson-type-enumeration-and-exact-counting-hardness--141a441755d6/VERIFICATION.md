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

# Verification and reproducibility

Run `python3 verify.py` with Python 3.9 or later. The code uses only the standard library, makes no external requests, and uses exact integer arithmetic. Expected successful output is reproduced verbatim in `verification_output.txt`.

The checker constructs finite triangle-free graph extensions directly from all ordered new-to-parameter adjacency bits; independently, it counts independent sets in the Cartesian product for the same parameters. It verifies equality across 263 small cases, the explicit independent-parameter formulas across 14 cases, and the one-query padding-recovery identity across 443 bipartite cases for arities 2, 3, and 4. The direct checker only tests finite examples and does not exhaust all graph orders or tuple arities. The infinite-family argument is given in `RESULT.md` and depends on the previously established homogeneous extension property, the exact graph-product bijection, and the uniform padding error bound.

No independent audit or external mathematical certification has been performed.
