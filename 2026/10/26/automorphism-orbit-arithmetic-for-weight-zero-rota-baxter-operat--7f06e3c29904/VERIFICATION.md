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

Run `python3 verify.py` using a standard Python 3 installation. The executable code works over prime fields using integer residues and does not require any external packages or networks. It constructs all predicted weight-zero Rota–Baxter operators, checks their defining identities on all basis pairs, evaluates the explicit automorphism action and its orbits, and compares them with the divisor-sum formula. For dimensions at most four in the listed runs, it independently checks the coefficient-level conjugation expression by multiplying the actual linear maps. In dimension three over the three-element field it separately tests all \(3^9\) possible linear maps and verifies that all solutions lie in the predicted family.

Successful explicit checks before packaging:

| Dimension \(n\) | Field size \(q\) | Operators | Conjugacy classes |
| ---: | ---: | ---: | ---: |
| 3 | 3 | 51 | 22 |
| 3 | 5 | 245 | 36 |
| 4 | 3 | 159 | 62 |
| 4 | 5 | 1245 | 176 |
| 5 | 3 | 483 | 190 |
| 5 | 5 | 6245 | 880 |
| 4 | 7 | 4795 | 376 |
| 5 | 7 | 33607 | 2054 |

The checker prints `VERIFY_OK` for its configured cases and `EXHAUSTIVE_ALL_LINEAR_MAPS_N3_Q3_VERIFY_OK` for the separate exhaustive case. Finite-field experiments are not proofs for arbitrary dimensions or extensions of prime fields. The mathematical proof is in `RESULT.md` and establishes the full odd-prime-power statement by algebraic normal forms and Burnside counting.
