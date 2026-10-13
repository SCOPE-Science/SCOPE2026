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

The proof uses two exact ingredients. First, unitary conjugation preserves trace, so an automorphism can be implemented in the stated representation only if it preserves the permutation character. Second, the affine basis permutation
\[
P_{a,c}|i\rangle=|ai+c\rangle
\]
satisfies
\[
P_{a,c}V(r)P_{a,c}^{\dagger}=V(r^a),\qquad
P_{a,c}V(f)P_{a,c}^{\dagger}=V(r^{2c}f).
\]
For even \(n\), the congruence \(2c\equiv b\pmod n\) is solvable exactly when \(b\) is even; for odd \(n\), it is solvable for every \(b\).

The included checker uses exact integer arithmetic. It enumerates \(3\le n<25\), all units \(a\), all residues \(b\), and all group elements needed for the natural permutation character. It confirms that character preservation is equivalent to the stated parity criterion, verifies the exact count of implementable automorphisms, and checks both conjugation identities on every basis vector. A separate sharp test confirms that, for \(n=4\), \(f\) has two fixed vertices whereas \(rf\) has none.

The checker output is `VERIFY_OK`. These finite computations are consistency checks only; the proof in `RESULT.md` establishes the all-\(n\) statement.
