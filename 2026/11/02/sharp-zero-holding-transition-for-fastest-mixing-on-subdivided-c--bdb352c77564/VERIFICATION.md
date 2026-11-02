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

# Verification and limitations

Run `python verify.py` in this directory with Python 3 and NumPy available. The verifier builds the exact graph adjacency and transition matrix, constructs independent invariant spectral blocks, checks multiplicities and eigenvalues against a full symmetric eigensolver, and uses rational arithmetic to test the polynomial support threshold across integer parameters. Random feasible orbit-invariant and non-invariant allocations provide additional finite sanity checks, and explicit small perturbations test the exceptional pairs. It prints an assertion count on completion.

Proof responsibility lies with the exact matrix decomposition and Laplacian Rayleigh quotient in RESULT.md; finite sampling alone establishes neither all-parameter optimality nor historical originality. Numerical tolerance is used only for floating-point eigenvalue checks. No independent audit or external certification has been performed.
