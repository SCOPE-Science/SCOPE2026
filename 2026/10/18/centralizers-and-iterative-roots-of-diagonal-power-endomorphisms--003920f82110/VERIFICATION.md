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

# Reproduction of the mathematical checks

Use Python 3 without external packages: `python3 verify.py`.

The program checks the following scientific assertions directly, without calling any external data service:

- Every nonerasing morphism on two letters with image length at most four is tested, \(900\) assignments total; for each of \(16\) power profiles with exponents from one to four, the number of solutions to \(\Psi^{\circ k}=\Phi\) for \(k=2,3\) agrees with the permutation-cycle enumeration and with an independently implemented labeled-cycle coefficient recurrence.
- Every nonerasing morphism on three letters with image length at most three is tested, \(59{,}319\) assignments total; every one of \(27\) power profiles with exponents from one to three is checked for \(k=2,3\).
- The centralizer normal form is compared to direct word substitution for all \(196\) two-letter morphisms with image length at most three and six specified profiles, and for all \(1{,}728\) three-letter morphisms with image length at most two and five specified profiles.
- The cycle coefficient recurrence also gives \(R_2(2,2)=2\), \(R_2(4,4,4)=10\), \(R_2(6,6,6,6)=48\) and \(R_3(8,8,8)=21\).

These profiles are exhaustively tested **at the stated length cutoffs**. For the root tests this also exhausts roots of each listed target profile, since applying a nonerasing endomorphism never shortens a word. Outside the enumerated profiles, finite computation is neither a proof of the universal classification nor a claim of exhaustive numerical validation. The proof in `RESULT.md` supplies the all-parameter argument. The checker outputs `VERIFY_OK` only when all direct and formula-based comparisons pass.

Mathematical checking status: self-reviewed; independent auditing has not occurred.
