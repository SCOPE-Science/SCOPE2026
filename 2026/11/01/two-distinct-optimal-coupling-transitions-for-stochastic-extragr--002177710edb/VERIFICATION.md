---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

All couplings are uniquely q=Pr(U=V), with masses q/2 and (1-q)/2. Since J^2=-I the update is M_uv=(1-xuv)I-eta v J and satisfies M_uv^T M_uv=g_uv(x)I, g=(1-xuv)^2+xv^2>0. Hence squared norms multiply independently and E||z_n||^2=R(q,x)^n||z0||^2 at every horizon. Independent symbolic gain calculations give R_shared-R_complement=x(9x-2)/2, R_shared-1=x(17x-5)/2, R_complement-1=x(8x-3)/2. For the almost-sure limit SLLN applies to bounded finite-support log gains and the product difference is -x(8x^2-13x+2), establishing the distinct transition and tie cases throughout 0<x<3/8. The proof handles every nonzero initial state, n>=1, all positive x in mean square; zero-stability boundaries are noncontractive. Exact symbolic checks corroborate each identity.

## originality

PASS

Best-of-knowledge originality of the complete final claim after explicit statement/implication comparison; qualified by documented priority risks. The exact two thresholds follow from original gain calculations specific to this finite-sum game and are not stated or established as an implication of available prior theoretical bounds.

## value

PASS

Sampling correlation between prediction and correction calls is a natural fixed-oracle-budget algorithm-design variable; this minimal benchmark exhibits different optimal couplings under arithmetic mean square and geometric typical-path risk. It also gives a sharp stability interval and a concrete regime where common sampling wins finite-horizon expectation but complementary wins almost-sure exponent. The claim deliberately does not generalize to arbitrary games or adaptive sampling.

The dated certificate retains the supplied scientific assessment, sources and limitations.
