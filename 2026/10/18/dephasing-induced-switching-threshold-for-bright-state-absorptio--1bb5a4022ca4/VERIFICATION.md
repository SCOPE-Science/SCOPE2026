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

# Verification protocol and limitations

The complete mathematical proof is in `RESULT.md`. To reproduce numerical consistency checks, run `python verification.py` with NumPy installed. The checker builds the full complex superoperator on all \((m+n)^2\) density-matrix coordinates, not merely the five-variable subsystem, and solves the finite-dimensional Poisson equation for integrated survival. A deterministic pseudorandom generator yields complex positive-semidefinite initial density matrices. The code also solves the exactly coherent two-level subsystem at zero dephasing and tests the global-dephasing phase boundary on both sides and at equality.

The executed checker reported: `PASS: 124 finite direct-matrix/phase-boundary tests; max absolute mean-time error 2.49e-14`. Conditions tested include \(m\in\{2,3,4\}\), \(n\in\{1,2,3,4\}\), positive sampled couplings and rates, plus further integral-mean and switching-boundary checks. The numerical matrices are small and the comparisons do not prove any arbitrary-dimensional assertion; the derivation of the five-variable closure, Hilbert--Schmidt decay inequality, and exact quadratic phase test do that work.

Only ideal site-independent hopping and identical loss across an entire absorbing part are proved. The code neither establishes originality nor constitutes independent scientific validation.
