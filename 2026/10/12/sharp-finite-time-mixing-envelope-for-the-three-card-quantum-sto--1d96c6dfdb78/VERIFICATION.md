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

# Verification and scope

From the package directory run `python3 verify.py` using Python 3.9+; there are no third-party dependencies. Expected exact output: `VERIFY_OK 18205 six_state_checks, sharp_envelope and asymptotic_ratio`. The program independently builds all six permutations, the 6-by-6 central Hamiltonian, and the rank-one/rank-four spectral projectors. It compares a matrix-derived Lindblad probability distribution against the group-character formula over representative rates and phases; checks total variation, the analytic optimal cosine and a dense comparison grid; and includes rational-arithmetic consistency tests. Its 18,205 checks are finite sanity tests, not an exhaustive certificate over a continuous domain.

The proof of the continuum global optimum uses piecewise derivative signs. The long-time coefficient follows by an analytic expansion at zero exponential damping parameter. Exact nonuniformity follows from strict positivity of the sign-character mode at every finite time.

Source comparison and priority limitations: the general quantum stochastic Fourier propagator already appears in He et al. (2026) and corresponding author thesis chapter 3.6. The original complete arXiv v1 HTML manuscript and the closely corresponding author thesis chapter were materially read. The direct PDF fetch failed; this did not prevent primary full-text inspection. Neither search coverage nor this self-review replaces independent auditing.
