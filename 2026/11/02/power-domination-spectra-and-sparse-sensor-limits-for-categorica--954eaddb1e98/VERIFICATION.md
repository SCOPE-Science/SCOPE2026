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

# Verification record

The standalone `verify_power_product.py` checks the exact graph-adjacency definition, simulates the closed-neighborhood and all simultaneous forcing rounds, and compares the outcomes to the claimed structural classification. It then checks every coefficient of the proposed power-domination polynomial directly against independent graph-level counts.

All nonempty subsets were examined for dimensions \((3,3)\), \((3,4)\), \((3,5)\), \((4,4)\), \((4,5)\), and \((5,3)\): a total of \(1,184,250\) examined vertex sets. Every subset of sizes \(1\) through \(4\) was also checked for \((5,5)\), and sizes \(1\) through \(3\) for \((5,6)\) and \((6,6)\). Checks verify the maximum-one-forcing-round assertion and immediate-stalling of all failed sets. The executable prints `VERIFY_OK` on completion.

The program is independent of the symbolic counting argument but not an exhaustive proof for all graph orders. Proof for arbitrary \(m,n\ge3\) is supplied in `RESULT.md`, including all boundary cases and both Bernoulli limits. The independent audit status is not performed.
