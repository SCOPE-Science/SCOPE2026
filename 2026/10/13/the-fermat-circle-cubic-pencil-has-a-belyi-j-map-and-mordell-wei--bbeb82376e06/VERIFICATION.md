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

# Reproducibility and verification

The accompanying `verify.py` requires Python 3 and SymPy. From the directory containing this file, run `python3 verify.py`. The expected concluding line is:

```
VERIFY_OK: quartic invariants, Belyi j, ramification, singular members, nine base blowups, I4 bridges, MW rank 3
```

The checks are exact symbolic equalities over \(\mathbb Q\), not floating-point samples: quartic invariants and discriminant, the identities for \(j\) and \(j-1728\), derivative-factor ramification, squarefreeness/coprimality, affine singular-point reduction, both line–conic factorizations, intersection directions, and the first/second base-point blow-up expansion. The final integer identity is a cross-check on the Shioda–Tate rank calculation.

The substantive infinite claims rely on the mathematical proof in `RESULT.md`: the classification of all complex fibers, Kodaira type of the exceptional four-cycle, relative minimality, and Picard rank. No assertion of independent mathematical audit, externally certified theorem proving, or arithmetic Mordell–Weil computation is made.
