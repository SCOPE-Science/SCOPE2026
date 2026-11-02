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

# Reproduction and checks

Run `python CHECKER.py` with NumPy and SciPy installed. It constructs the killed finite-volume continuous-time Markov chain for two independently flipping velocity signs, solves \((-Q)m=\mathbf1\) and \((-Q)M=2m\), and averages over all interior separation bins and four orientation states. Four scales and three mesh sizes are checked, including the expected reduction in discrepancy on mesh refinement. This independently corroborates the continuum formulas without assuming their derived conditional polynomials.

The exact symbolic proof is in `RESULT.md`. Its strongest checks are substitution into both second-moment backward equations and both incoming absorbing conditions, polynomial integration for the global second moment, and sign/uniqueness analysis of the two quartic derivatives. Grid convergence is not itself a proof for arbitrary real rates.

At zero reversal rate, half the initial direction pairs never meet, so the finite-moment formulas are stated only for strictly positive rates. Relative second moments at very small rates are large; no finite-time cutoffs are claimed.
