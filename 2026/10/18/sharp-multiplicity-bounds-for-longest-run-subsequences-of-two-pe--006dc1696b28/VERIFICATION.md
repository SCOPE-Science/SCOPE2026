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

The complete proof is in `RESULT.md`. Execute `python3 check.py` with Python 3.9 or later. The program uses only the standard library and constructs every possible subsequence by independent position-mask enumeration for all second permutations on at most five labels. It requires each such optimum to have length \(m+1\) and agrees exactly with the record formula for the number of distinct optimum words.

A second exhaustive census iterates over all \(m!\) second permutations for each \(1\le m\le9\), checks the lower and upper count inequalities and checks the claimed equality families against independently constructed adjacent-block tilings and designated leading-value forms. The largest test covers all \(362{,}880\) permutations on nine labels. The expected terminal message is `ALL_RUN_MULTIPLICITY_TESTS_PASSED`; it was observed when executing this file from the package staging directory.

The program does not prove the theorem for all alphabet sizes, perform literature verification, or provide independent certification. Infinite validity is justified by the argument in `RESULT.md`; the finite experiments corroborate it and expose boundary errors if present.
