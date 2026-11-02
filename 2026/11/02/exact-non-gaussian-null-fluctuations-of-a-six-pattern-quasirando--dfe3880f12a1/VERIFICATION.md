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

# Reproducible algebraic checks

Run `python verify_null_limit.py` with SymPy. The program symbolically constructs the conditional one-point and two-point pattern kernels, confirms exact first-order cancellation and reversal invariance, and integrates the squared canonical second projection on one ordering chamber. It checks \(\int K^2=121/3600\) and the consequent leading variance coefficient \(121/1800\) using rational arithmetic. An independent finite enumeration inside the same program confirms means and variances of all uniform permutations at sizes four through seven.

The checker uses no stochastic approximation. The infinite-sample spectral limit itself follows from the analytic canonical U-statistic theorem, not a finite computation. The implementation assumes correct established U-statistic theory; its assertions are finite algebraic checks, not an independent proof of that theory or independent mathematical validation. The limit's spectral eigenvalues are not individually enumerated.
