---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-12.md",
      "INDEPENDENT_AUDIT_2026-10-12.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

From normal variation delta H=-Delta f-n csc^2(R) f and E_j(c,...,c)=c^j, reconstruct delta F=delta H/n independent of index k. Independently differentiate phi=N/D at stationary F=c and cancel equal area-variation terms, obtaining delta phi=2c average(delta F)=-2c csc^2(R) average f. Therefore delta(phi/F-F)=(2/n)Delta f+2 csc^2(R)(f-average f). Constants and degree-one harmonics neutral; degree-lambda for degree ell is 2 csc^2(R)(1-ell(ell+n-1)/n), with sharp shape gap 2(n+2)/(n sin^2 R) at ell=2. Independently checked binomial-derivative cancellation through n<=15 and all k; proof analytic for every n>=2, k=0..n-1 and 0<R<pi/2; no nonlinear convergence rate claimed.

## originality

PASS

For the precisely defined nonlocal Luo--Wei--Zhou curvature flow, the full mean-projection operator is mathematically more specific than the stated nonlinear convergence framework. Best-of-knowledge O remains subject to an unusually strong full-text access limitation on the focal primary paper.

## value

PASS

The primary flow has global nonlocal normalization and a full derivative distinct from its local spatial operator. Isolating the rank-one average projection, k-independence, neutral moduli and degree-two sharp linearized gap gives a directly applicable local stability benchmark, without claiming an unproved nonlinear rate.

The dated certificate retains the supplied scientific assessment, sources and limitations.
