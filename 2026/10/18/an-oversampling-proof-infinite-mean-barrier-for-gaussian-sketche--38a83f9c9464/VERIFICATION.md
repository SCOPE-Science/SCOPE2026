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
# Verification of the mathematical claim

The exact Lanczos reduction is checked algebraically using randomly generated rational sketch matrices on two- and three-step SPD tridiagonal systems. Independently, the first-step sketched Galerkin condition and sketched least-squares normal equations were checked with exact rational arithmetic, and Student-CDF numerical integrations were compared with analytical tail constants.

The script `check.py` passed 2,396 rational one-step equations, 208 rational multistep Lanczos reductions, and 15 numerical tail-constant checks. Separate numerical integration checked the Gaussian–chi integral for the one-step exact tail constant at sketch sizes 1, 2, 3, and 5, with agreement to displayed precision; those checks are not required by the script.

Run `python check.py` with `scipy` installed as specified by `requirements.txt`. The mathematical proof, not sampling, establishes the infinite-\(T\) law and sharp moment thresholds. Finite test cases neither exhaust the parameter domain nor provide an independent audit. The theorem excludes terminated Lanczos spaces, structured sketches and guarded implementations.
