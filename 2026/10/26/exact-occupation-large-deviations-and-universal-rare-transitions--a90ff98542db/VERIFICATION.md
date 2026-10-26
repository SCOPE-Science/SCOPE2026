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

The standalone `verify.py` (Python standard library) checks positive stochastic kernels, detailed balance, symmetric flow margins, the exact pair-contribution formula, non-negativity to roundoff, an exact uniform benchmark, and higher KL cost for nonzero loop circulation over seeded interior cases. These are finite algebraic and numerical checks, not an independent mathematical audit. The LDP proof relies on the classical finite-state Markov method of types; the unique entropy contraction is proved directly in `RESULT.md`. Boundary costs are checked analytically there.

**Scientific limits:** Exact finite-time probabilities, prefactors, boundary-conditioned Markov transition concentration, and population-wide branching fluctuations are not claimed. Potential historical overlap with W. S. Hsia (1976) remains because only its accessible abstract could be examined.
