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

# Verification of the proportional-beta mean-tail theorem

The complete analytic argument appears in RESULT.md. It uses exact differentiation of the binary relative entropy, a strictly increasing ratio of two branch derivatives, integration of a positive weight, and an exact log-odds Jacobian. The critical polynomial assertion is
\[
AB-2A(1-r)w+Brw^2>0\quad\text{for }\frac{1-p}{p}\le r\le1,\quad 0<w<p,
\]
under \(1/2<p<1\) and the branch-domain restriction. This follows from monotonicity in \(r\) and the displayed strictly positive value at its lower endpoint. The binomial consequence is an exact beta–binomial CDF identity.

Execute `python3 check_beta_binomial.py` without additional dependencies. Observed output:

```
PASS: 600 exact binomial tail values; 576 exact consecutive comparisons; 3469 exact rational derivative checks
```

The verifier constructs binomial probabilities using integer numerators and rational denominators. The universal strict monotonicity, the beta endpoint limits, and the quantifiers over all real concentration parameters are analytic, **not** consequences of exhaustive finite computation. No third-party verification is asserted.
