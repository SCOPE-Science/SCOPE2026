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
# Verification and boundaries

The proof reduces the operator to the polynomial \(s(X)-d_tu(X)\), verifies the polar-sign reflection \(UXU=(2-X)E\) on \(E=1_{\{u(X)>0\}}\), and uses invariance of a finite tracial functional under this symmetry. The paired trace formula and the exact identity \(2s(x)-Lu(x)=((\sqrt a+\sqrt b)x-2\sqrt b)^2\) are the decisive infinite-dimensional steps. The two distinct \(M_2(\mathbb C)\) witnesses give equality for \(d_t\le L/2\) and \(d_t>L/2\) respectively.

The included `verify_trace.py` is executable using the Python standard library. It checks an exact rational witness with trace deficit \(40\), squared Frobenius distance \(6480\), and sharp ratio \(1/162\), plus a commuting sharpness check and 15,000 deterministic scalar principal-angle comparisons. These computations are supplementary, not a proof of universal validity.

No experiment addresses general positive operators outside the common two-point-spectrum family or infinite traces. External independent validation has not been performed.
