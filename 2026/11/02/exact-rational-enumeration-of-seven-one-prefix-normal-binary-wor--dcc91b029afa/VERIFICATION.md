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

# Reproducibility and bounds

Run `python3 verify.py` in the extracted package directory. Only the Python standard library is needed. The program prints `VERIFY_OK` after these independent exact checks:

- Enumeration of all rank-four active-facet intersections in a five-dimensional cone via integer determinants, producing the displayed thirteen primitive rays and sum of degrees 39.
- Exhaustive counting of **all** cone lattice points up to weighted degree 39, providing every coefficient needed by the proven numerator degree bound; verifying the exact numerator polynomial identity, and checking degrees 40 through 70 additionally.
- Direct complete enumeration of all binary words with exactly seven ones at lengths from 7 through 18. Agreement with the proposed rational generating function is supplemental testing, not the basis of the all-length result.
- Polynomial identities for denominator cancellation and primitive-fourth / primitive-sixth cyclotomic noncancellation; numerator palindromicity and evaluation at one.

Observed output:

```
VERIFY_OK rays=13 degrees_sum=39 coeffs=71 word_lengths=7..18
density7_counts_n7_to18 1,4,13,31,71,134,249,417,688,1062,1628,2367
numerator_H 1,3,9,17,35,48,76,85,108,103,108,85,76,48,35,17,9,3,1
```

The finite computational certificate is exhaustive for the explicitly proved degree bound, not an attempted proof by extrapolation. The rational-cone triangulation and its degree bound, as well as the reduction of prefix normality to gap inequalities, are proved mathematically in `RESULT.md`. No external certification or independent audit is implied.
