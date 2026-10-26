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

The boundary-value problem is equivalent to \(\int_0^1u=-1\) and \(\int_0^1tu=0\). For a nondecreasing BV control, the distributional derivative \(\mu=Du\) is nonnegative and the moment identity \(\int_0^1s(1-s)\,d\mu(s)=1\) follows by eliminating \(u(0+)\). The inequalities \(\int(1-s)^2d\mu\ge m^2/T\) and \(s(1-s)\le1/4\) yield the two lower bounds. The candidate step controls satisfy the two moments exactly; the capped branch identities simplify to \(-U\tau+b(1-\tau)=-1\), \(-U\tau^2/2+b(1-\tau^2)/2=0\), and \(-U+(U-1)^2/(U-2)=b\), where \(\tau=1/(U-1)\) and \(b=1/(U-2)\).

The global feasibility cutoff uses the maximum first moment among box-bounded controls with fixed mean; the maximizer is certified by the sign of \( (t-\tau)(u-u^*)\) on either side of its switch. The exact TV minimization claim is restricted to nondecreasing controls; no claim is made about the global minimum over all bounded BV controls. No numerical experiment is used as a substitute for proof.
