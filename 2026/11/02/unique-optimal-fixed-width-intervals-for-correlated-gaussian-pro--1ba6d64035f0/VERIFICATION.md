---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

For -1<rho<1 and h>0, the exact correlated normal-product density is exp(rho*z/d)K0(|z|/d)/(pi sqrt d). K1>K0>0 makes its tails strictly monotone. On -h<c<h the log endpoint-density ratio has strictly negative derivative, goes from +infinity to -infinity, and equals 2 rho h/d at c=0, giving one interior maximum with correct sign; outside that interval mass is monotone. K0(t)=-log(t/2)-gamma+O(t^2|log t|) and K1(t)=1/t+O(t|log t|) yield c=(rho/d)h^2[log(2d/h)-gamma]+o(h^2) and gain rho^2 h^3[log(2d/h)-gamma]^2/(pi*d^(5/2)). Independent scipy root checks with rho=0.4,h=.2; rho=-.7,h=.1; rho=.5,h=.003 confirmed sign and small-width scale (the original source checker.py and exact Git blobs were inspected). Finite tests are not proof. rho=0 yields c=0 and zero gain; near rho=+/-1 uniformity is not asserted.

## originality

PASS

PASS best-of-knowledge: the exact density and mode are classical; the all-width maximizing interval, unique center and small-width logarithmic displacement/gain are distinct objects not found in inspected 2022 product-distribution survey. Recent 2026 VG CDF paper was abstract-access only, leaving explicit risk.

## value

PASS

The concentration function for a highly skewed singular density is a natural small-ball statistic; its maximizing interval differs strictly from the mode and admits sharp nonanalytic displacement and gain constants, a motivated exact parametric classification rather than a mechanical density restatement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
