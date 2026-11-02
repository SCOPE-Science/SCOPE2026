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

# Verification record

The identity \(T_n(b,c)=[X^n](X^2+bX+c)^n\) is used with nonzero integer coefficients. The exact symbolic proof of the valuation phases is in `RESULT.md`: it normalizes the finite multinomial sum and applies Legendre's factorial valuation formula to every term. The critical-line construction is exact for every depth parameter and does not rely on computation. The binary histogram is an exhaustive combinatorial consequence for every dyadic depth.

Execute `python3 verify.py` using Python 3. The verifier computes coefficients by an independent integer recurrence derived from the generating function and crosschecks selected terms by the multinomial sum. It tests both valuation regimes, the normalized-unit congruence modulo four, critical-line examples, and primitive-coefficient dyadic histograms. The reported output was:

```
VERIFY_OK coefficient_pairs= 1944 valuation_indices= 157464 unit_mod4_checks= 59292 direct_multinomial_checks= 3920 critical_witnesses= 72 dyadic_histograms= 60
```

This computational evidence is finite, not a proof of an infinite statement. Generality rests on the identities in `RESULT.md`. The theorem excludes zero coefficients and does not classify the full critical-line behavior. Historical originality and mathematical correctness have not been independently audited.
