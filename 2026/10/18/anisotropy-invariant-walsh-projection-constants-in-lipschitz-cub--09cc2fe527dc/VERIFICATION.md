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

The analytic proof derives an upper estimate from directional Walsh kernels and an attaining sign-gradient at a least-weight coordinate. Translation averaging proves that the Fourier projection has the minimum norm among all projections onto the specified subspace. Coordinate transitivity makes the directional kernel norms coincide, independently of the positive weights.

For reproducibility, run `python CHECKER.py`. The script uses Python's standard library only and performs exact rational evaluations of weighted edge Lipschitz norms and integer Walsh transforms. It tests all homogeneous degrees in dimensions \(2\) through \(6\), selected unions of spectral levels, and a proper-transitive example; it compares kernel and binomial values through dimension \(7\) and checks the quadratic identity through dimension \(11\). The tests do not enumerate all dimensions, all support families, or all real weights. Universal validity depends on the written analytic argument rather than empirical checks.

No external or independent audit has been performed.
