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

Run `python3 verify_grassmann.py` with Python 3. The checker computes exterior products by bit masks, uses its own finite-field row elimination, and independently enumerates all \(3^{10}=59049\) elements of \(\bigwedge^3\mathbb F_3^5\). It finds exactly one zero element, \(2420\) rank-two forms, and \(56628\) rank-four forms. It also checks 180 wedge-multiplication cases and 80 random-seeded direct commutation comparisons in the unit group over \(\mathbb F_3\). It verifies integer class-equation identities for \(q=3,5,7,9\). The reference output ends in `ALL_EXACT_CHECKS_PASSED`.

The direct algebra checks use only the prime field \(\mathbb F_3\); the \(q=9\) check concerns symbolic-integer counts, not implemented field arithmetic. The proof in RESULT.md establishes all odd prime powers and is independent of the finite verification. No exhaustive enumeration of the full \(q^{31}\)-element group was attempted, and no independent mathematical audit has been performed.
