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

The endpoint proof uses the exact derivative jump \(4bf'(b)\) at \(t=1/2\), the central limit theorem for \(\mathrm{Bin}(n,1/2)\), and the Gaussian negative-part expectation. The repair constructs a nonnegative \(C^1\) derivative on the continuation interval with prescribed value and derivative at the join, then integrates it to obtain a nondecreasing \(C^2\) extension constant near \(1\). The Bernstein derivative formula proves monotonicity, and Taylor's theorem gives the explicit error bound.

A numerical sanity check for \(b=1\), \(f(x)=x\) gives scaled endpoint errors \(-0.70934\), \(-0.76757\), and \(-0.78802\) for \(n=100,1000,10000\), approaching \(-\sqrt{2/\pi}\). This check is not used as proof. Independent audit and external validation have not been performed.
