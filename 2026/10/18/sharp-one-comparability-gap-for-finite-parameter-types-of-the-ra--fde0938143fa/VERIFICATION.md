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

Run `python3 verify.py` under Python 3.10 or later without third-party dependencies. The script generates every labeled strict partial order through five vertices, counts one-point order-extension profiles directly, independently reconstructs the allowed profiles using transitive closure through four vertices, and checks the one-point doubling fiber structure in 4,200 labeled five-vertex induced extensions with comparable bases. It checks two sharp families through nine vertices. Expected labeled-poset counts for orders one through five are 1, 3, 19, 219, 4,231; the maximum non-antichain counts are bounded by the exact formula \(3\cdot2^{n-1}\).

The computational checks are finite only. They cannot establish the asserted inequalities for all sizes; the complete proof is the symbolic restriction-fiber argument in `RESULT.md`. The source-priority comparison is a literature review, not a novelty certificate. Independent audit has not been performed.
