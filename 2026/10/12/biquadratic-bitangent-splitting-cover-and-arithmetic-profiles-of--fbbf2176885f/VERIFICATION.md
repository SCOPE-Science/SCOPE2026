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

Run `python verify_bitangents.py` with Python 3 and SymPy. On the packaged source, it completed exact symbolic checks and returned:

```
VERIFY_OK distinct_bitangents=28 classes=A12+B4+C12 generic_Galois=V4 orbits=1^4+2^6+4^3 rational_lambda_t2=-34/25
VERIFY_OK quadratic_subfields=A=-lambda-1,B=lambda+2 branch=-2,-1,infinity real_counts=16,28,4
```

The first message certifies the verifier's assertions for the three polynomial square identities, 28 distinct rational-function-field bitangent coefficients, the action of \(s\mapsto-s\) and \(s\mapsto1/s\), the orbit decomposition, and one rational example. The second certifies the exact radical relations, quadratic subfields, derivative and branch representatives, and multiple rational parameter substitutions. The real count follows by explicit signs of the two radicands, as proved in RESULT.md; the script's message is a label for these mathematical deductions, not a numerical sampling proof. The algebraic independence and minimality steps are established by valuations and coefficient recovery in RESULT.md. A finite script cannot establish the general characteristic-zero 28-bitangent theorem; that independent classical fact is explicitly used in the proof. Reproducibility is not independent validation.
