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

# Verification scope

Run `python verify.py` in the same directory after installing dependencies from `requirements.txt`. Exact rational checks include the spectral endpoint identities, feasible row sums, all three edge-support regimes, and permissible intervals on 561 integer pairs. Dense numerical diagonalization compares full graph transition spectra against the four analytic eigenspaces for 77 parameter pairs. A separate linear program solves the reduced SLEM minimax problem in 209 cases; 420 feasible non-invariant perturbations are also compared to the proved value. The actual output is preserved in `verification_output.txt`.

These checks neither enumerate all graph orders nor certify an infinite theorem. The global proof uses group averaging, the four-mode exact spectrum and a two-variable minimax inequality. In particular, the assertion about every unrestricted optimizer's core-edge weights follows by averaging nonnegative entries, not by testing finitely many matrices.

The publication-first-date evidence for the mathematical starting point is arXiv:0709.0955v1, first posted on 2007-09-06. Literature searches have the limitations stated in REVIEW.md. No independent audit has been performed.
