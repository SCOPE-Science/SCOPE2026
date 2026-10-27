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

# Reproducibility and limits
Execute `python check.py` in an environment with NumPy and SciPy. The script computes induced two-norms by singular values, optimizes over the physically allowed interval, checks analytically predicted endpoint and interior classifications for representative weight vectors, and verifies the same-weight-multiset rearrangement. An equality endpoint is resolved by the mathematical proof rather than numerical endpoint tolerance.

The finite numerical checks cannot certify the assertion for every dimension or real/complex weighting. The proof uses a phase-removing diagonal unitary, a strongly convex envelope, and a first-order Hermitian perturbation restricted to the maximal-singular-value eigenspace. The largest path component of maximal edges yields the exact cosine threshold. The numerical radius of the absolute-weighted tridiagonal symmetrization supplies the second boundary. No independent audit or exhaustive prior-art certification has been performed.
