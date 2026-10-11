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

# Reproducibility and limits

Run `python3 verify.py` with the Python standard library. The deterministic exact-arithmetic checker constructs all Johnson adjacency matrices and the degree-cutoff projectors via Lagrange spectral interpolation for \(4\le n\le8\), \(2\le k\le\lfloor n/2\rfloor\), and \(0\le L<k\). It checks idempotence of every projector, annihilation of the claimed spectral values, and the first four traces of powers of the compressed face operator.

Observed output:

```
VERIFY_OK parameter_sets=23 exact_coordinate_rows=773 moments=1..4 spectral_annihilator=true projection_idempotence=true
```

All matrices, projectors, and moments use exact rational arithmetic, so there is no tolerance parameter. These checks are finite corroboration only. The proof for all admissible integers is supplied in `RESULT.md`, using harmonic-lift norm identities, the two-coordinate degree filtration, and a rank-one hypergeometric compression. Independent audit has not been performed.
