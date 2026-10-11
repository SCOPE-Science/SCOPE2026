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
# Verification notes

The argument uses exact substitution identities, group actions and elementary integer arithmetic, not numerical extrapolation. The two substituted return words are determined inductively from the initial return-word pair. Their integral determinant and the greatest common divisor of their entries establish Smith diagonal entries \(1\) and \(2^{n-1}\). A separate clopen-component argument identifies the limiting return subgroup with the fibre stabilizer.

The included `check_components.py` was executed from its package path with Python 3 and printed `Finite return lengths and Smith-index tests passed for n=2..9, k=2..17.` It checks literal consecutive return words for the substitution fixed point, determinant magnitude and subgroup cardinality for the stated finite ranges. This is a finite sanity check only: it does not certify the infinite induction, group-extension theorem, or bibliographic originality. No external independent validation or audit has been performed.
