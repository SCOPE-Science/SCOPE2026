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
# Verification of the visibility spectrum

The standalone `verify.py` runs using the Python standard library. Its five integer coefficient vectors are rational witnesses for all values \(D=0,1,2,3,4\). For each witness, it constructs five ambient vectors, confirms their unique rational linear relation, checks all ten pair thresholds, solves the full affine barycentric system for each of the \(32\) signed configurations, and compares the observed visibility histogram with the theoretical \((2,10,20-2D,2D)\).

Execution from the embedded package: `python verify.py`. The expected final line is `ALL_EXACT_VISIBILITY_CHECKS_PASSED`. This verifies the finite algebraic certificates. The proof that these witnesses extend to admissible smooth-patch boundary distributions is given analytically in `RESULT.md` and is not inferred from the computation. The proof applies in ambient dimension four only. No independent mathematical audit was performed.
