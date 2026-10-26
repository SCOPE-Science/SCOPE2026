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

Run `python elliptic_12_cover_check.py` using Python 3. It verifies the six certificate rows, including group sums, tangent multiplicities, and the fact that each row covers every one of the twelve elements. It also checks smoothness, the exact point counts over the finite field of eleven elements and the rational 2-torsion for the two sample cubics. The universal lower bound and rational-flex equivalence are supplied by the mathematical proof, not by the finite checker. Independent audit has not been performed.
