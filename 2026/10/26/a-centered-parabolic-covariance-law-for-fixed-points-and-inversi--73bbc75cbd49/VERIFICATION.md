---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

For Ewens-θ on S_n, θ>0 and n≥3, marked singleton deletion gives P(B_i)=θ/(θ+n-1) and conditional Ewens(n-1). Its two cross-inversion contributions total 2(i-1)(n-i)/(θ+n-2), by the exact one-coordinate marginal. Subtract the known M_n(θ) and complete the square around (n+1)/2. The resulting radius squared equals (1-θ)(n-1)[(n-3)(2n-1)+3(n-1)θ]/[12(θ+n-3)(θ+n-1)] and covariance = 2θ(R²-(i-(n+1)/2)²)/[(θ+n-1)(θ+n-2)]. Denominators positive for n≥3; θ>1 all negative, θ=1 central zero only if n odd, 0<θ<1 central window, endpoints negative; R²/n→(1-θ)/6 gives mesoscopic limit. Independently enumerated every n! permutation for n=3..7 for θ=1/2,1,2 and all i using exact rational cycle weights and inversions; identities agreed. Finite check corroborates, not proves arbitrary n.

## originality

PASS

Pinsky–Schickentanz Theorem 1(b) establishes unconditional Ewens inversion mean; its Proposition 10 conditions on the total number of fixed points, which does not imply this position-indexed signed covariance without a new marked-point regression calculation. Prior published results on uniform fixed-point/descent dependence and inversion/cycle-count dependence involve different indicators. The exact parabolic covariance and sqrt(n) central sign window remain a narrowly original derived classification on inspected evidence.

## value

PASS

The exact location-resolved effect and θ-dependent sign reversal reveal where individual fixed points preferentially align with inversions, a meaningful refinement of known global means; mesoscopic scaling is independently useful.

The dated certificate retains the supplied scientific assessment, sources and limitations.
