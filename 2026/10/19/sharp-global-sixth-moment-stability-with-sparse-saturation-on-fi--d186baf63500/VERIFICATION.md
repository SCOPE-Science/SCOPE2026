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

The standalone script `verify_sharp_triple_stability.py` was run using only the Python 3 standard library. It returned:

```
VERIFY_OK exact_prob_cases= 228 independent_fourier_cases= 8
```

It uses exact rational arithmetic for probability-polynomial identities on 228 vectors, including an exhaustive denominator-six grid in dimension five. Eight complex Fourier sums at prime fields five and seven independently verify the orthogonality normalization and triple-collision expression. The script explicitly tests simplex vertices, uniform points, support-two and support-three inputs, and nontrivial unequal profiles. General validity over prime-power fields is supplied by the written proof, not by the finite enumerations. No independent audit has been performed.
