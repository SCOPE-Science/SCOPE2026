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

# Verification of the two-patch extinction-time comparison

The proof is an exact symbolic calculation from a three-state transient generator; this report records companion reproducibility checks, not an independent audit.

Run `python3 verify_two_patch.py` with Python 3.10 or newer. The checker uses `fractions.Fraction`, enumerates 3,125 exact first-step identity cases, 729 matched-total polynomial coefficient identities, and five exact values around the unique crossover, and prints:

```
VERIFY_OK first_step_exact=3125 comparison_polynomials=729 sharp_example=5
```

The unrestricted denominator-positivity check follows because the local rates are positive and the denominator polynomial has strictly positive coefficients. The factorization and strict monotonicity of the critical comparison polynomial constitute the analytical proof of the infinite parameter-domain classification. The finite computation is supplementary and cannot independently establish those universal statements.

No simulation, field-data fit, asymptotic approximation, or independent scientific validation was performed. The historical-literature access limitations are recorded in REVIEW.md and AUDIT.json.
