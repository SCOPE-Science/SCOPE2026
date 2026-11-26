---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

With the frozen angular-frequency convention, integrating the 3-ball slices gives the positive prefactor 8πα⁻³s⁻³ multiplying F. The convolution of cos(ux) with sin(sx), evaluated at 1, is s(cos u−cos s)/(s²−u²); applying 1−s∂s gives F=s²N/(s²−u²)². Taylor expansion in u at u=±s gives the removable value (sin s−s cos s)/4; the axial slice s=0 reduces to the positive cubic-weight cosine integral by |sin(u/2)|<|u/2|. For 0<s<π, N/(2s) is the strict tangent deficit of cos√t at t=s², using strict convexity up to π² and that the tangent is below −1 thereafter. At s=π, N=2π(1+cos u), with ±π removed from the alleged zeros by the positive resonance value. For a closest zero the comparison with (3π,π) gives |u|≤3π and π≤s≤π√(1+9/α²). The lower bound is strict because u=0,s=π is not a zero. At (3π,π), N_s=−8π², N_u=0, N_uu=2π, so the true local curve has s=π+(u−3π)²/(8π)+O((u−3π)³); moving slightly left strictly improves the upper bound at each finite α. Compact localization forces any positive-u minimizer onto that curve as α grows. The second derivative of s(u)² at the limit is 1/2; analytic stationarity for s(u)²+α⁻²u² then gives the stated shifts and the −36π²/α² term in κ². Finally, volume 2π/(3α³) gives the claimed J₂-root threshold by comparing to the ball; the strict lower bound even suffices at equality of the stated threshold.

## originality

PASS

Verified prior work supplies the same scaled profile framework, existence of a positive zero-free strip, and the large-elongation ball comparison, including an explicit weaker sufficient threshold. The supported distinct claim is the sharp four-dimensional transverse bound π, the exact boundary zero set, and the ensuing nearest-zero expansion and improved sufficient threshold; the compared earlier bounds and infimum formulation do not give these conclusions.

## value

PASS

The exact transverse endpoint is the quantitative obstruction in a pre-existing Fourier-zero isoperimetric counterexample, not an arbitrary parameter sample. It supplies the first possible zeros, determines the previously unspecified asymptotic slope, and distinguishes the nearest zero from the boundary point through an explicit curvature correction. The smaller sufficient counterexample threshold is a concrete consequence, not the sole advance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
