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

`verify_centralizers6.py` constructs all exterior basis products in dimension six and performs modular Gaussian elimination on 32-by-32 odd-to-even wedge-multiplication matrices. Over fields of 3, 5 and 7 elements it checks 6 prescribed representatives and 70 pseudorandom odd elements per field, 228 cases in total, plus the exact cardinality-sum identity for the six proposed strata. Recorded result: `VERIFY_OK_EXTERIOR6_CENTRALIZER_DISTRIBUTION 228_ODD_MULTIPLICATION_CASES`.

`verify_trivector6.py` independently tests every homogeneous exterior-degree map for 1,016 zero, decomposable, divisible rank-four, generic and randomly sampled trivectors in four prime fields, recording `VERIFY_OK_TRIVECTOR_SIX_GENERATOR_JORDAN 1016 matrix_cases`. The strong all-field statement rests on the symbolic proof, not finite testing. A symbolic calculation confirms that weighting centralizer size by stratum multiplicity recovers the independently established commuting-pair polynomial; this agreement is a consistency check, not originality evidence.

Exact run commands: `python3 verify_centralizers6.py` and `python3 verify_trivector6.py`. Both scripts are included here in full. No independent external validation has been performed.
