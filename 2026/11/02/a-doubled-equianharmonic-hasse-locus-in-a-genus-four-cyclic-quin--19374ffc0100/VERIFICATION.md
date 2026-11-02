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

# Reproducible coefficient checks

Run `python3 verify_cyclic5_11.py` in a Python 3 environment with `sympy>=1.11`, and `python3 verify_binomial_11.py` with Python 3's standard library. Both supplied standalone scripts were run against the same polynomial identities, using separate expansion implementations. Actual successful outputs:

```
VERIFY_OK: genus 4 basis valuations, 4 block coefficients, 2x2 determinant, all polynomial identities
STRATA_OK: p=11, rank 4 for Q !=0 and rank 2 for Q=0, a-numbers 0 and 2, stable ranks equal ranks
DIVISOR_OK: det(B)=4*t^6*(t-1)^6*(t^2-t+1)^2; two F121 points, each multiplicity two
MODULI_OK: exceptional branch configurations form one equianharmonic S3 orbit, j_br=0
BINOMIAL_OK: eleven independent F11[t] coefficients match all four Cartier block identities
BINOMIAL_DETERMINANT_OK: block det=2*t^4*(t-1)^4 and total Hasse determinant=4*t^6*(t-1)^6*Q^2
```

The programs check exact polynomial coefficients in \(\mathbb F_{11}[\lambda]\), not an interpolation on finitely many field elements. The proof additionally uses elementary tame ramification, semilinear Cartier stability, and the discriminant criterion for the quadratic. This verification is not independent external certification. It does not establish uniqueness of the scientific result in historical literature.
