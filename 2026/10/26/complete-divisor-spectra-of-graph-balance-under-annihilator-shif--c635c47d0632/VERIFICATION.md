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

The exact algebraic proof in `RESULT.md` covers every field and every integer \(m\ge2\). Finite computation is a separate cross-check, not an infinite certification.

Run `python3 verify.py` with Python 3. The checker uses only the Python standard library. It represents the algebra structure over prime fields, exhaustively enumerates invertible ordered bases in the indicated small examples, filters bases satisfying pairwise-zero multiplication, constructs their support graphs and computes their integer signed-walk balance using height potentials.

Observed checks: \((m,q)=(2,2)\) has \(24\) natural ordered bases and attained balances \(\{1,2\}\), with both balances on connected graphs; \((2,3)\) has \(432\) bases with balances \(\{1,2\}\); \((3,2)\) has \(192\) bases with balances \(\{1,3\}\). All connected-only spectra agree. For each \(m\) from \(2\) through \(12\) and each \(q\in\{2,3,5,7\}\), the explicitly constructed natural basis for every divisor was checked against the predicted gcd and the structure multiplication. The checker prints `VERIFY_OK` if all assertions pass.

The brute-force enumeration is exhaustive **only for the three listed finite cases**. No finite-field experiment proves the all-fields theorem; that conclusion rests on the complete normal-form argument and signed-walk lattice proof.
