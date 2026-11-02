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

# Reproducible verification

Run `python3 verify.py` with Python 3 and its standard library. The output should be:

```
VERIFY_OK Catalan_recursions=602 fuss_ratio_cases=900 binomial_ratio_cases=2304 affine_screen_cases=49341 exact_integer_and_rational=yes
```

The checker verifies exact Catalan and central-binomial recurrence identities, 900 exact Fuss–Catalan ratio/drift cases, 2304 exact fixed-slope binomial cases, and searches 49,341 candidate affine maps against finite prefixes of three integer sequences. These finite checks cannot establish the infinite claims. The unrestricted theorem rests on the documented proof that every positive slope is an integer, every putative affine self-map induces an eventual fixed index shift, and every nonzero shift contradicts the divergence of a weighted sum of one-step drifts. The Stirling expansion supplies the required hypothesis for the hypergeometric examples. No external mathematical validation was performed.
