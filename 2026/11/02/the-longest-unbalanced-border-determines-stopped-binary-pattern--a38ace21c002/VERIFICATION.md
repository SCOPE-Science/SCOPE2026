---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The all-length argument is sound. Independently, let F and A be the first-hit and avoidance generating functions with letter weights x/2 and xy/2. Decomposing any string gives 1=A(1-x(1+y)/2)+F. Appending the target to an avoiding string gives a first-hit string followed by the residual suffix corresponding to a unique nonempty self-overlap; dividing by the target weight gives A=F times the sum of reciprocal border-prefix weights. This establishes the stated bivariate function, including the full-word term. Integrating the y derivative divided by x weights each contribution by 1/tau; subtracting half the integrated x derivative uses almost-sure hitting and tau>=1. The result is the stated strictly positive kernel times the signed border polynomial at T=2/x. If the last nonzero coefficient d_b is positive, unit prefix increments imply d_j>=1-(b-j), so all earlier negative terms together are bounded by T^b sum_{h>=2}(h-1)/T^h=T^b/(T-1)^2<T^b for T>2. Negation handles the other sign, and all zero coefficients give exact equality. The geometric hitting tail and integrable endpoints justify the operations; this is not inferred from finite testing.

## originality

PASS

The distinct contribution is necessity for the stopped q statistic and the strict sign classification, not the published sufficiency, generating function, or a result for limiting avoidance frequency. The strongest distinct catalog match is a finite-alphabet extension: it demonstrably covers the binary statement by specialization, but its own prior-work section describes the binary classification as earlier, and the materials inspected do not establish it as prior coverage of this finding.

## value

PASS

This resolves a precise published open direction for a natural stopping-time statistic, and gives a strict sign criterion even for globally balanced words and mixed border imbalances. The one-step bound supplies a uniform explanation of why cancellation cannot occur. No resolution of the avoidance-frequency conjecture is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
