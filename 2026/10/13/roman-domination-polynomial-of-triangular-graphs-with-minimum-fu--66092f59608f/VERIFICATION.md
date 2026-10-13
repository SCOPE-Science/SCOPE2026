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

Run `python3 verify.py` with Python 3.10 or later, using only the standard library. The standalone script constructs the Roman weight polynomial by the stated inclusion-exclusion formula and checks it against a direct enumeration of every ternary labeling of triangular graphs through \(n=5\). It also independently enumerates every subset of label-two edges through \(n=6\), accounting for all free choices of label-one vertices by binomial coefficients. Finally it checks the minimum exponent and number of minimizing functions against the matching census for \(3\le n\le18\).

The captured output in `verification_output.txt` records 49,660 exhaustive ternary-label function checks through \(n=5\), agreement of the independent support-subset expansion through \(n=6\), and the full coefficient and minimum-profile comparisons. The direct support-subset calculation includes all \(2^{15}\) possible label-two subsets for \(n=6\). A successful script execution produces the same final three `OK` statements as the captured output.

These finite tests check implementations, boundary cases and explicit coefficient identities, but cannot prove the infinite statement or completeness of the external literature search. Universal correctness rests on the support bijection, inclusion-exclusion count and matching extremality proved in `RESULT.md`; equivalence with existing differently named results is a separate literature question.
