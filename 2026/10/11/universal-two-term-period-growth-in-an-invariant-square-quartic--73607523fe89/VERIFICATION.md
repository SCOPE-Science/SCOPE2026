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

# Verification of the period expansion

The standalone `verify_period.py` uses SymPy to reconstruct the algebraic identities \(\dot H=0\), \((r^{-1}-1)\,dU/dr=((1+r)(1+z r))^{-1}\), and the exact derivative and endpoint values of the proposed elementary antiderivative. It was run against the extracted package version and returned `CHECK_OK`.

The decisive infinite-energy step is analytic, not experimental: the nonnegative defect functions are decreasing and integrable on \((0,\infty)\), so their convolution at \(E\) tends to zero by a two-half-interval estimate. The proof also verifies that the normalized energy levels are closed and regular, and that no time reparametrization is used.

For the checkable \(p=q=0\) case, the exact elliptic formula gives the observed values \(T(2)-8\approx5.589308028589\), \(T(4)-16\approx5.546649149481\), and \(T(7)-28\approx5.545183586400\). Their target \(8\log2\approx5.545177444480\) is consistent, but the numerical values alone prove no infinite limit.

No examination or certification by an independent auditor is asserted. The literature comparison leaves an explicit residual access risk concerning Villadelprat and Zhang (2019/2020), whose abstract describes general boundary-period behavior.
