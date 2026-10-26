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

# Reproduction of the dodecahedral spectral classification

The standalone file `verify_dodecahedron.py` uses Python 3 and its standard library only. Run `python3 verify_dodecahedron.py` from this directory.

The actual execution printed the following independent checkpoint labels (these are checks, not a substitute for the proof in `RESULT.md`):

```
EXACT_GEOMETRIC_SCHEME_IDENTITIES_PASS
EXACT_LEGENDRE_COEFFICIENT_SIGN_TESTS_PASS 186 degrees
RANK_EXCEPTIONS [(0, 1), (1, 3), (2, 5), (3, 7), (4, 9), (5, 6), (8, 9), (14, 9)]
LOWEST_NONZERO_EIGENVALUE_OVER_0_TO_185 0.0019406356177512336 at degree 13
ANALYTIC_TAIL_CERTIFICATE_PASS ell>=186
ALL_CHECKS_PASS
```

All algebraic tests use exact rational arithmetic in \(\mathbb Q(\sqrt5)\). Geometric identities are recalculated from the twenty vertex coordinates and checked entry by entry. The strict inequality used for the infinite tail is established symbolically in `RESULT.md`, not by a finite matrix experiment. The numeric least-eigenvalue approximation is descriptive only. No outside independent review or validation has been performed.
