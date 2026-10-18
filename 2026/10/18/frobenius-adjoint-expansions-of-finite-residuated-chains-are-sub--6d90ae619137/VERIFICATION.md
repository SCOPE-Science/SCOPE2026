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

# Verification and limitations

The proof in `RESULT.md` establishes the theorem for all finite bounded integral commutative residuated chains. The package also includes a self-contained Python 3 program, `verify.py`, requiring only the standard library. Execute `python3 verify.py` to reproduce the finite corroboration.

The checker independently enumerates all increasing contractive right adjoints and reconstructs their left adjoints, then checks F1–F5 directly. A second enumeration takes all endpoint-containing subsets, tests closure under fusion and residual, constructs lower/upper roundings, and compares the full sets of surviving operator pairs. The two algorithms agree for standard Łukasiewicz and Gödel chains through size ten and for nilpotent-minimum and drastic-product chains through size nine. Additional closed-subalgebra enumeration through size thirteen verifies the two closed formulas; order correspondence is checked through size eight.

Observed output:

```
MV_COUNTS_n2_TO_n10 [1, 2, 2, 3, 2, 4, 2, 4, 3]
GODEL_COUNTS_n2_TO_n10 [1, 2, 4, 8, 16, 32, 64, 128, 256]
FINITE_CHAIN_FROBENIUS_VERIFY_OK
```

Only the finite instances listed above were computationally tested. They do not prove the arbitrary finite-chain statement; that is supplied by the constructive algebraic proof. No independent audit has been performed.
