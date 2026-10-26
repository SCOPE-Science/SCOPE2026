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

Run `python check.py` with Python 3 and `mpmath` (see `requirements.txt`). All computations in `check_results.txt` were performed from the provided standalone checker. The checker verifies 90 exact rational finite-ring equalities between independently enumerated permitted cyclic words and matrix powers; evaluates the normalized correction at multiple segment lengths and system sizes with 95-decimal-place arithmetic; checks the leading eigenvalue expansion; and makes 40,000 independent kinetic deposition trials in each of three finite examples. The output records 136 completed assertions.

These calculations do not establish the uniform asymptotic for infinitely many system sizes; that result follows from the exact transfer identity, analytic eigenvalue branch, nonprincipal spectral bound and exponential expansion in `RESULT.md`. Monte Carlo comparisons do not establish exact equality.

The rigorous domain is fixed integer \(\ell\ge2\), periodic rings of \(n\ge\ell+1\) sites, independent rate-one Poisson clocks at every anchor, and accepting segments only when they add previously uncovered sites. The asymptotic error is uniform only on compact intervals of the centered time variable. No independent audit has been performed.
