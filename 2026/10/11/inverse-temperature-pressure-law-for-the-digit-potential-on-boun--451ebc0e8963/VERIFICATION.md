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
# Verification evidence

Run `python3 verify.py` from a directory containing this document and the included standalone script. The script uses only the Python standard library. Its run printed the following finite checks:

```
t= 20; t*(P-t*alpha) approximation=0.827685251; tail absolute upper bound=0.00e+00
t= 60; t*(P-t*alpha) approximation=0.828394028; tail absolute upper bound=9.00e-149
t=200; t*(P-t*alpha) approximation=0.828498417; tail absolute upper bound=2.54e-43
t=500; t*(P-t*alpha) approximation=0.828504690; tail absolute upper bound=6.16e-16
VERIFY_OK: direct lexicographic and renewal-polynomial counts agree for every word length 0..13 (16383 tested binary words).
```

The script verifies the first \(13\) symbols of the chosen irrational slope via an exact rational enclosure; checks all \(16{,}383\) test words using two distinct combinatorial constructions and integer-polynomial coefficients; and evaluates finite positive renewal sums with a geometric omitted-tail **absolute upper bound** at the displayed numerical roots. Floating-point rounding is not rigorously enclosed by these bounds. They are diagnostic examples, not a computational proof of the irrational-slope theorem. All infinite conclusions follow from the explicit graph identity, Diophantine spacing and covering lemmas, unique-ergodicity argument, and convexity proof in RESULT.md. No independent audit has been performed.
