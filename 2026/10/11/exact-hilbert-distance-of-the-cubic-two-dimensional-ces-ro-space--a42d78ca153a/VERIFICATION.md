---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

Let a=9^{2/3}; H²=(a u²+v²)/4. Homogeneity reduces sharp H≤N to a polynomial whose nonconstant coefficients are positive for t≥0 and equality only at axes. Ratio R(t)=[8+(1+t)³]^{2/3}/(a+t²) rises then falls, since φ(t)=t(1+8/(1+t)²) is strictly increasing; its unique τ gives Rmax≈1.299582043601. Arbitrary tilted quadratic forms cannot beat it: using x=(1,0),y=(0,τ), N(x+y)=N(x−y) and the Euclidean parallelogram equality yield distortion²≥Rmax; H attains. Independent symbolic polynomial check and high-precision numerical stationarity τ≈2.766739880... verify constants; finite grid not the universal proof.

## originality

PASS

PASS best knowledge: pre-existing Cesàro norm James/B-convexity and Ptolemy/von-Neumann–Jordan constants provide a matching lower-bound scalar but do not in inspected materials establish a globally sharp ellipsoid or no-tilted-ellipse proof for p=3. Related published exact Hilbert distance for p=4 has a different norm/exponent; no dominating all-p theorem found. Saejung 2010 full text inaccessible is recorded as risk.

## value

PASS

PASS: an exact optimal Hilbertian comparison for a canonical asymmetric Cesàro plane, with explicit extremal ellipse and rigorous global optimality, is a natural metric invariant. It proves an otherwise nonautomatic equality of lower geometric constant with true Banach–Mazur distance and could be used as a precise benchmark.

The dated certificate retains the supplied scientific assessment, sources and limitations.
