---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

For u with ordered absolute coordinates a≥b≥c, solving plane x1=-(bx2+cx3)/a gives Jacobian 1/a and forbidden corners of total projected area (b+c-a)_+²/(bc), hence A=4/a-(b+c-a)_+²/(abc). Near six axis normals this is 4/a and spherical cap probability exactly 3(1-4/(4+ε)). Near twelve face diagonal normals tangent deficit is 4sqrt(2)|t|+2(|s|-sqrt(2)|t|)_+²/|s| plus o(radius). Integrating the degree-one sublevel yields quadrant J=(4+π)/(64sqrt2), coefficient 12*4J/(4π)=3(4+π)/(16πsqrt2). Independently evaluated tangent ratios near 1 (.99967,.99992,.999985) and constant .30139183075. Global extrema used from prior cube section theory; no claim of full CDF.

## originality

PASS

Best-of-knowledge PASS. Global extrema and exact area as a function of a fixed normal are known (Ambrus and Marichal–Mossinghoff), as are separate random face-vector laws. No inspected result supplies Haar probability germ at axis minima together with explicit ε² upper-tail coefficient at face-diagonal cusps. Existing published Resultary random cube hexagon face count concerns a discrete face-count statistic, not the metric area tails. Incomplete exhaustive literature coverage remains a residual risk.

## value

PASS

The probability density of central slicing area near both sharp geometric endpoints is a natural stereological invariant; different exponents 1 and 2 and an explicit unusual π coefficient quantify concentration beyond deterministic extrema, with potential use in sampling rare extreme planar sections.

The dated certificate retains the supplied scientific assessment, sources and limitations.
