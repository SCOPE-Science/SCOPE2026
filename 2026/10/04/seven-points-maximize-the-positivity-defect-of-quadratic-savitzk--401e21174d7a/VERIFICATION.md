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
The checker uses exact rational arithmetic for every finite identity it tests. It verifies the closed center-weight formula, polynomial reproduction through degree two, symmetry, normalization, the published five- and seven-point coefficient patterns, the sign cutoff, and the exact negative-mass formula.

For \(1\le m\le27\), it computes the defect exactly and confirms that \(m=3\) is the unique maximizer with value \(4/21\). For the analytic tail argument it verifies the rational constants at \(m=28\) and the exact squared inequality that bounds the remaining radical. It also checks the strictly positive seven-point witness, whose center output is exactly \(-2/21\) after normalizing \(M=1\).

The all-\(m\) result is not inferred from finite enumeration. The monotone integral bound and asymptotic argument are given explicitly in RESULT.md.
