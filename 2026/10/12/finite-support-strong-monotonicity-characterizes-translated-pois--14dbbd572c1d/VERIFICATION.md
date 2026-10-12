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
# Reproducibility and mathematical limits

The complete proof uses only (i) the finite polynomial identity for exponentially tilted characteristic functions, (ii) a nonzero polynomial's inability to vanish on a circular arc, (iii) normalized factorization into independent Bernoulli probability-generating functions, and (iv) the explicit Fourier modulus of a tilted Bernoulli variable. These steps prove the claim for every finite support, with no numerical extrapolation.

Run `python3 verify.py` with Python 3 and no external packages. The saved checker produced:

```
PASS: four Bernoulli factors yield nonnegative normalized PGF with expected negative roots
PASS: 10648 exact integer coefficient triples; 608 ordinary-but-not-strong cases
PASS: rational witness has tilted Fourier zero at angle 2.065012371258, but endpoint modulus 0.356537679935
LIMIT: numerical point check not an infinite proof; full equivalence is established algebraically in RESULT.md
```

All reported integer coefficient tests and the Bernoulli-factor identities use exact rational/integer arithmetic. The displayed angle and modulus use ordinary floating-point arithmetic only to illustrate the rational-algebraic witness. The complete infinite-degree-uniform theorem is a direct mathematical proof, not a purported computer certificate or independent verification.
