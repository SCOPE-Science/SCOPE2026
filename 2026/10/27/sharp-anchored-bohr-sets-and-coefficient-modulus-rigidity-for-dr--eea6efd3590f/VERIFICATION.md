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

# Verification and limits

The proof checks the sharp Bohr ball for both finite dimensions \(d\ge2\) and countably many coordinates, treating pointwise majorants through the multinomial identity and a convergent geometric series. The contractivity of the exhibited multiplier follows from \(\|M_\ell\|\le1\) and one-variable rational contraction functional calculus. Each asserted boundary equality is an exact algebraic identity, not an asymptotic or numerical estimate.

`CHECKER.py` was executed with Python's `fractions.Fraction`. It checks the degreewise multinomial profile for rational boundary squared-coordinate pairs through degree twelve, confirms profile normalization for finite truncations, and checks the precise finite-tail correction to the deficit identity for multiple rational coefficients. These finite diagnostics do not establish the full theorem.

The inspected 2026 source covers unrestricted Bohr sets; the 2019 fixed-zero-coefficient paper covers a different single-variable setting. The older 2002 multivariable paper could not be inspected in full, so historical priority remains open to independent verification. No independent audit has been performed.
