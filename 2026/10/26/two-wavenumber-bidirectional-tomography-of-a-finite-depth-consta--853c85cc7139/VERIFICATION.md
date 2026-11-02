---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

Under known density, known surface advection reference, two distinct known wavenumbers 0<k1<k2, and strictly positive h,S,g,sigma, the classic constant-vorticity dispersion gives delta_i=u_i-d_i=S tanh(k_i h)/k_i and p_i=u_i*d_i=(g/k_i+sigma*k_i/rho)tanh(k_i h). R=k1delta1/(k2delta2)=tanh(k1h)/tanh(k2h) is strictly increasing from k1/k2 to 1 because k/sinh(2kh) strictly decreases. Hence h and then S are unique. Y_i=k_i p_i/tanh(k_i h)=g+(sigma/rho)k_i² is an invertible 2×2 linear system, and strict positive gravity/surface tension are exactly Y1<Y2<(k2²/k1²)Y1. Conversely positive difference/product uniquely recover each measured speed pair, proving sharp sufficiency. At one k, h and g can vary freely, yielding a two-parameter nonidentifiability family. The derivative of R has a linear shallow-depth zero and exponentially small deep-depth tail, establishing the inverse-condition laws. Independently implemented forward/inverse reconstruction for 12 positive parameter configurations and checked the identities; finite tests corroborate, not prove, global injectivity.

## originality

PASS

Ellingsen–Brevik give the *forward* finite-depth constant-vorticity gravity-capillary dispersion, which is openly credited. The four-parameter inverse identifiability classification, minimal two-wavenumber measurement count, exact open feasible-data inequalities, and sharp boundary conditioning were not found as theorems of the inspected full source. Nonlinear gravity-capillary bifurcation papers concern different inverse problems. Residual historical inverse-dispersion literature could contain the same elementary but useful transformation.

## value

PASS

Depth, shear, restoring acceleration and capillarity are natural physical coefficients, and four directional speeds at two wavelengths are a minimal dimensional measurement set. Proving global uniqueness together with a sharp realizability test and endpoint conditioning is a complete, self-contained inverse problem classification, not just plugging numbers into the dispersion law. Physical measurement accuracy/viscosity are expressly outside scope.

The dated certificate retains the supplied scientific assessment, sources and limitations.
