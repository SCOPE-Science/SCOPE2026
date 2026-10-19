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

The proof requires no untrusted computational inference. It is based on the exact Gaussian-arcsine mixture, a pointwise uniform exponential comparison, an endpoint Laplace expansion with nondegenerate derivatives uniformly bounded on \(q\in[0,1/4]\), the classical Bessel asymptotic, and Gaussian tail integration.

Run `python mix_crossover_checker.py` with NumPy and SciPy (versions specified as lower bounds in `requirements.txt`). It checks 149 deterministic assertions involving exact-integral quadrature, a global logarithmic envelope, a near-classical Bessel comparison, the second rare-displacement crossover, and fixed-parameter endpoint Gaussian tails. The actual embedded script was extracted and rerun successfully, reporting 149 passing checks. These are numerical illustrations and consistency tests, not finite certification of an infinite inequality.

The \(q\downarrow0\) statements describe the densities of the *already-computed, fixed-\(q\) infinite-time weak limits*. No interchange with the original walk time variable is demonstrated. Independent audit: not performed.
