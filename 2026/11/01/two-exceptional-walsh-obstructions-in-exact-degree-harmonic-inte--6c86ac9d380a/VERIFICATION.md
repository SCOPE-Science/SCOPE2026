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

# Verification of the hypercube interpolation rank theorem

The standalone `cube_harmonic_rank_checker.py` uses exact rational arithmetic for the Gegenbauer recurrence and Krawtchouk/Walsh eigenvalue sums. It was executed successfully from the associated artifact files: all 741 sectors for dimensions 3 through 8, degrees 0 through 18, and weights 0 through the dimension matched the formula, including both exceptional zeros and nonnegativity elsewhere.

Separately, symbolic Taylor expansion checks were carried out for the two exceptional-weight derivative formulas at odd indices \(m=1,3,5,7\); both vanish at the excluded index \(m=1\) and are nonzero thereafter. These are sanity checks, not certificates for infinitely many degrees.

The infinite proof uses the Fischer orthogonal decomposition, an irreducible complex null quadric, and explicit generating functions. The full argument is given in `RESULT.md`. Independent mathematical audit has not been performed.
