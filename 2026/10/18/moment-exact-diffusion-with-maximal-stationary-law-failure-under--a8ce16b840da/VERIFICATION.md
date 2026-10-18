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

Execute the provided standard-library script with `python3 check.py` from the package directory. The observed output was:

```
PASS: 21140 exact rational assertions in affine common-reset systems
```

The program uses `fractions.Fraction` and deterministic seeded test cases. It checks stationary moment identities against both jump and diffusion generators, the Cauchy determinant, the exact nonzero cubic generator difference, and the explicit exponential-age moments when marks vanish. Parameters include dimensions \(2,3,4,5\), independent heterogeneous rational relaxation rates, and two families of reset marks.

Checks performed outside the program: the Markov generators were compared symbolically on \(1,x_i,x_ix_j,x_i^3\); the unique invariant states were justified by pathwise or mean-square contractivity; the Cauchy determinant was reconstructed using the standard Cauchy identity and a Gram representation; the complete-reset age representation was derived from exponential memorylessness; the exponential-Brownian stationary integral was checked in \(L^2\); and its Malliavin derivative and nonsingular Gram matrix were verified analytically by linear independence of exponentials. The Bouleau–Hirsch criterion is used only after these hypotheses are checked.

**What this does not establish.** Finite rational checks cannot prove an infinite-dimensional or arbitrary-parameter theorem; the proof supplies that generality. Neither the program nor the analytical proof establishes total-variation separation for nonzero partial-reset multipliers, an explicit smooth density, convergence rates, or results for repeated damping parameters. Independent scientific audit has not been performed.
