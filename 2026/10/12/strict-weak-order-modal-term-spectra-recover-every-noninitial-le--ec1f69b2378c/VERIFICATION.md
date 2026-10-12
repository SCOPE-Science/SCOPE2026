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

# Reproducibility

The package contains complete source code `artifacts/verify.py`. From the extracted package root run:

```sh
python3 artifacts/verify.py
```

The Python standard library is sufficient. Latest observed output:

```text
VERIFY_OK vectors 56 type_tests 168 pointed_valuation_samples 738094 inverse_polynomials 56 direct_clone_tests 22 direct_term_operations_total 16860 root_invariance_families 5
```

The verifier exhaustively enumerates \\(56\\) positive level vectors of total width at most \\(6\\) and height at most \\(4\\), checking each at \\(q=1,2,4\\) by two different pointed-type representations. It tests exact rational reconstruction from the arity polynomial, directly constructs small nullary and unary term-operation clones by Boolean and modal closure (\\(22\\) comparisons), and checks invariance under changing the initial level width in five families. These finite checks do not certify the theorem in all sizes; the unrestricted proof is in RESULT.md.

An independent audit has not been performed. The code makes no claim of exhaustive literature priority verification.
