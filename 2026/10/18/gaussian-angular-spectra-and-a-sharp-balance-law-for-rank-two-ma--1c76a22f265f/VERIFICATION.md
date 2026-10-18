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

Run `python3 check.py` using a Python standard-library interpreter. No numerical packages, network access, or random seeds are needed. The checker independently enumerates every permutation of the labeled ground set for all 58 rank-two parallel-class size partitions totaling at most eight elements. It compares the relative frequency of the unique greedy-exposed basis against the theorem's exact rational probability for every vertex.

It also verifies the normalization of the probabilities, recomputes the second-collision formula via two independent rational expressions, checks 3065 exact discrete strict-majorization transfers on integer partitions through total size fifteen, and checks all claimed rational quantities for the two eighteen-element examples, including the vertex and edge counts.

The complete mathematical argument is contained in `RESULT.md`; it proves the statements for all admissible dimensions independently of enumeration. Finite exhaustion through eight elements and transfer tests through fifteen elements are not asserted to prove the infinite quantifiers. No independent external audit or separate certification is claimed.
