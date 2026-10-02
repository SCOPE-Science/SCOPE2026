---
{
  "schema_version": 1,
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-01.md",
      "INDEPENDENT_AUDIT_2026-10-01.json"
    ]
  },
  "lean_verification": {
    "status": "unknown",
    "evidence": null
  },
  "expert_attestation": {
    "status": "unknown",
    "evidence": null
  }
}
---

# Independent mathematical audit

## correctness

PASS

Large-x Stirling asymptotics force a=b-1/2 and c>=log sqrt(2pi). With that a, the next digamma term gives f'=(b^2-b+1/6)/(2x^2)+O(x^-3), so complete monotonicity forces b^2-b+1/6<=0; the x->0 derivative excludes b>1/2. Thus b is at least 1/2-sqrt(3)/6. For that remaining interval, the Laplace kernel K_b(t)=1/t+1/2-b-e^{-bt}/(1-e^{-t}) is positive: writing r=1-2b and t=2y reduces it to (1+ry)sinh y>y e^{ry}; the logarithmic comparison decreases in r, and the submitted two-range derivative estimates prove the worst case r=1/sqrt3. Hence -f' is a positive Laplace transform and f is completely monotone, strictly so after integrating K_b/t and using the nonnegative limiting constant.

## originality

PASS

Guo 2015 proves only the coarse necessary interval 0<b<=1/2 in general and proves iff sufficiency on the subinterval [1/2-sqrt3/6,1/2]. The submitted second-order large-x obstruction excludes the entire missing interval 0<b<1/2-sqrt3/6, completing the iff classification. The inspected 2019 review and targeted searches did not state this global closure.

## value

PASS

The result closes an explicit missing parameter interval in a natural complete-monotonicity classification and supplies a direct positive-kernel proof at the exact boundary. A complete iff threshold for a standard gamma remainder is a motivated structural fact, not an arbitrary numerical slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
