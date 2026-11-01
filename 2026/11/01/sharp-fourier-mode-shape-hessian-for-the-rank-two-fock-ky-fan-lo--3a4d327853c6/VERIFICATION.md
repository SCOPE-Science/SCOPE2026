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

# Verification of the sharp shape-Hessian formula

The exact proof in `RESULT.md` reconstructs the operator normalization, smooth trace-norm shape differentiation, the isolated rank-two Ky Fan cluster, and its Fourier-mode expansion. The independent finite-dimensional consistency program `experiments/check_hessian.py` reads no external file and requires only NumPy and SciPy. It uses incomplete Gamma integrals to construct truncated Toeplitz matrices for deformed radial graphs and evaluates a centered second difference for the top-two eigenvalue sum. It passes 15 comparisons over three radii and five Fourier modes, and six checks of the closed-form coefficient and strict ordering, for 21 checks overall. Reproduce with `python experiments/check_hessian.py`.

The numerical tests are floating-point and finite-matrix only. They do not prove analyticity, infinite-dimensional spectral perturbation, strict monotonicity at all Fourier orders, or complete originality. Those scientific requirements are evaluated by the mathematical proof and documented literature comparisons. The source arXiv:2607.28376 already proves qualitative global disk optimality, and this verification deliberately does not reassert that statement as new.
