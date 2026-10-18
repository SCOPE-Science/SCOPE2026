---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

For n>=2 the retained body K_n^- obeys -1<=t<=0 and t+sqrt(n²-1)||y||<=n. The uniqueness of maximal inscribed ellipsoids and O(n-1) transverse invariance force axial semiaxis a, radial semiaxis b and center -s, with 0<s<1. Exact support-function containment is a<=min(s,1-s), b²<=((n+s)²-a²)/(n²-1). The logarithmic volume derivative in a is positive over the feasible domain, forcing a=min(s,1-s); along s<=1/2 the remaining volume strictly increases, and along s>=1/2 it strictly decreases, by the derivatives printed in RESULT.md. Unique optimizer s=a=1/2,b=sqrt(n/(n-1)). The volume ratio to the unit ball equals 1/2 (n/(n-1))^((n-1)/2), conditional on the original primary theorem J(K_n)=B_2^n. I rechecked the algebra and all boundary cases n=2 and s=1/2; no finite numerical maximization is used.

## originality

PASS

The recent Zhou–Zou–Liu paper displays exactly E_n and its volume ratio as a feasible half-cone witness, so neither object nor ratio itself is new. The narrow claim adds global maximality/uniqueness among ALL inscribed ellipsoids of the retained half-cone. This property is not established by the primary material actually accessible here, and the original package quotes a Section 4 statement that maximality is not needed; this cannot replace inspecting the full source. Best-of-knowledge PASS is restricted to maximality, with a significant unresolved historical/2026 full-text comparison risk.

## value

PASS

Maximizing inside the particular half-cone is an exact intrinsic John-ellipsoid computation relevant to the canonical sharpness family for the central-cut conjecture. It clarifies whether the exhibited witness is optimal for that very body in every finite dimension, without claiming the still-open global finite-dimensional central-cut constant. Natural optimization target, not an arbitrary parameter slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
