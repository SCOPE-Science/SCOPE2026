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

# Reproducibility and verification

The theorem's analytic content is in `RESULT.md`. This file records only self-review; no independent audit has been performed.

Run `python verify.py` from the directory containing `verify.py`, with Python 3, NumPy and SymPy installed. The check constructs each weighted wheel adjacency matrix directly, groups its eigenvectors by common eigenvalue into full orthogonal projectors, and forms \(\sum E_\lambda\circ E_\lambda\). This construction is separate from the closed Fourier formula. The script also enumerates Fourier eigenvalues, verifies stochastic row sums, tests explicit nullvectors, and checks three exact algebraic-resonance examples.

Observed replay:

`VERIFY_OK numerical_cases=442 exact_symbolic_cases=3 exact_matrix_identities=3 resonances=105 worst_matrix_error=2.23e-14 worst_spectrum_error=1.65e-14 worst_kernel_residual=1.17e-13 n6_k3_rank=5/7 n8_k3_rank=7/9`

The symbolic tests independently check projector idempotence, resolution of the identity, fused-projector Schur-square formula and rank at \((n,k)=(6,3),(6,2),(8,4)\). Other tests cover integer rim sizes 3 through 28, sampled spoke weights, each admissible exact resonance and both sides of each resonance. The algebraic proof, not finite samples or floating-point thresholds, establishes equations (1)–(2) for all permitted inputs.

Scientific limitations: finite computation does not establish the infinite theorem, and near-degenerate eigenspace grouping is sensitive to numeric tolerances; resonant couplings are constructed and labeled analytically before numerical testing. Comparisons to Kimmerling's prior unweighted wheel formula are not independent novelty certification. No expert or external validation is asserted.
