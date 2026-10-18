---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

Eq. (25) defines ν(U^n)=-(U^n-U^(n-1))/(k U^n) at n>=1, with special ν(U^0)=0 only. For localized central E,I source and initially empty remote E,I,Q,R, the explicit four-neighbor old-time stencil in Eq. (26) leaves all four compartments zero at a point beyond graph distance one after the first step. Hence the second-step correction must evaluate 0/0. Algebraically 1+kν=U^(n-1)/U^n has no path-independent limit at (0,0): approaching along U^(n-1)=U^n gives 1, along U^(n-1)=2U^n gives 2. Independent exact-rational stencil and ratio checks reproduced these facts. This is a failure of the PRINTED discrete map for the specified nonnegative initialization, not a claim that simulations used no hidden convention or that the continuous PDE is ill-posed.

## originality

PASS

Best-of-knowledge original narrow result after comparing actual mathematical implications with primary source and adjacent literature: The original consistency amendment concerns accuracy, while the new claim concerns definability on nonnegative localized data; general NSFD positivity results do not specify the paper's ν(0,0) continuation.

## value

PASS

A specific missing state-space rule prevents the published corrected, positivity-motivated epidemiological numerical recurrence from being defined on its own stated localized zero compartments. This affects reproducibility of long-time trajectories, gives an explicit support-propagation witness and identifies the minimal mathematical issue (nonremovable zero denominator). It is more substantive than generic division-by-zero checking because the zero case is forced by the reported data and stencil.

The dated certificate retains the supplied scientific assessment, sources and limitations.
