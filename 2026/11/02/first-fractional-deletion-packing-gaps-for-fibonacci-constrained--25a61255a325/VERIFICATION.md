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

# Verification protocol

From the directory containing `RESULT.md` and the `artifacts` directory, execute:

```
python3 artifacts/verify.py artifacts/certificates.json
python3 artifacts/census.py
```

The first program uses only Python's standard library, exact integers, and rational arithmetic. It reconstructs all binary source words with no adjacent `11`, their distinct length-one-deletion shadows, and the complete output universe. For each of the seven lengths it checks the explicit integer code. At lengths one to five it checks the output transversals; at lengths six and seven it checks the nonnegative rational primal and dual fractional certificates, every clique's pairwise-confusability condition, the integer quarter-units, total clique weights, and the coverage inequalities that give strict integral upper bounds. The second program computes all seven maximum independent-set cardinalities by a separate branch enumeration without using the certificate file.

The terminal markers from verified current-package runs are `VERIFY_OK` and `CENSUS_OK` respectively. The finite certificates imply the exact theorem; floating-point optimization outputs and previously saved log messages are not required. This is not independent scientific validation or historical-priority certification.
