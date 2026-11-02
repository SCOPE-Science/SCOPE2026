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

# Verification details

Execute `python3 verify.py` with the Python standard library; it checks the exact companion-matrix thirteenth power, the integral negative-index roots, exact recurrence terms through \(n=4000\), another 200,000 values modulo \(3^{19}\), 26 far-index lifting cases, and **all indices within the complete periods** for valuation levels \(0\) through \(8\). Expected output:

```
VERIFY_OK matrix_power=13 negative_roots=2 exact_terms=4001 modular_terms=200000 far_lifts=26 complete_period_levels=9 sharp_global=29/13
```

The verification program does not use unbounded sampling to certify the theorem. The complete-index argument comes from the explicit matrix identity and the binomial valuation lemma, while the all-level sharp discrepancy follows from the four explicit residue positions for any \(t\ge2\). Finite tests are independent checks of exact premises, residue formulas, and selected instances; complete small-period checks are exhaustive **only at those finite levels**. No independent audit is represented by these calculations.
