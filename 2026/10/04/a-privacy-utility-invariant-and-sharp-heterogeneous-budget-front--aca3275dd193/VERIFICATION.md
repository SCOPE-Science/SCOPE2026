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
# Verification

The packaged script `verify_heterogeneous_gdp.py` checks the finite-dimensional algebra of the claim using deterministic examples and a fixed pseudorandom seed. It verifies:

- \(\mathbb E[e^{-\xi_k}]=1\) for the canonical Gaussian mean/variance pair;
- \(\mu_{\mathrm{prod}}=\Delta_{\max}/\sqrt V\) and \(2L\mu_{\mathrm{prod}}^2=\Delta_{\max}^2\);
- the \(V_0\ge T\) frontier branch by saturating all local caps;
- the \(V_0<T\) branch by tightening one local parameter exactly enough to make \(V=T\);
- randomized positive parameter instances for numerical consistency.

The script does not certify the Gaussian-DP theory itself. The privacy step is analytic: neighboring output laws are equal-variance Gaussians and their mean shift is bounded sharply by the product log sensitivity. The originality assessment is literature-based and is not established by the checker.
