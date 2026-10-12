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

# Verification record

The standalone `verification.py` needs Python 3 with only standard-library modules. It can be run without network access using `python3 verification.py`. Its `cycle_count` implementation uses independent traversal labels, while `exact_covariance` enumerates each \(n^n\) uniform mapping, directly counts incoming images and accumulates \(C_nD_{n,r}\) for every in-degree \(0\le r\le n\). The separate `formula` routine computes the finite-cycle-Palm covariance coefficient with exact rational arithmetic.

Actual replay checked every mapping for \(n=2,3,4,5,6,7\), totaling 873611 self-maps, and matched the exact formula at each one of 33 degree coordinates. It also verified the deterministic zero-sum and first-degree-weighted zero-sum covariance constraints for six values of \(n\), totaling 12 identities. Its high-precision exact-rational finite checks are independent of the asymptotic limiting argument. Representative output terminates with `VERIFY_OK all_degrees 33 independent_mappings 873611 conservation_identities 12`.

Floating-point diagnostics for \(n=100,500,2000\) illustrate convergence of the first five degree-class covariances toward their predicted values. These are diagnostics only; even an infinite number of numerical tests would not establish compact-uniform convergence or fixed-degree sign classification, which instead follow from the Gaussian domination and uniform analytic expansion in RESULT.md.

**Limits:** No evaluation of random mapping laws other than the uniform independent-image model; no claim of universal finite-size covariance signs; no independent scientific audit has been performed.
