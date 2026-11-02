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

# Verification report

The theorem is proved analytically in `RESULT.md` from four spectral projectors and three exact primal/dual Wasserstein computations. It is checked computationally by `verify_crown.py`, a standalone Python 3 standard-library script using `fractions.Fraction`.

Actual local execution yielded:

```
CHECK_OK exact_rational_pair_and_transport_checks= 6195 orders=5..14 bases=2,3,5
```

For each indicated graph and sampling time \(t=\log b\), it constructs the Markov heat rows using exact rational spectral multipliers, verifies probability normalization and nonnegativity, checks every unordered pair's signed marginals, validates nonnegative transport plans whose balances match those marginals, verifies distance-weighted costs, and verifies either an exact admissible 1-Lipschitz dual potential or the universal unit-distance lower bound. It checks the claimed maximal coefficient for every pair.

No floating-point tolerance is used in the standalone certificate. Finite tests do **not** prove the formula for every real \(t\ge0\) or every unbounded integer \(n\), prove priority, or provide independent validation. Those infinite claims depend on the proof in `RESULT.md`.
