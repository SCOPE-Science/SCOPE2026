---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

Any affine h(x)=cx+d minorizing a x^2/2 satisfies d<=-c^2/(2a); for fixed c the tangent envelope maximizes distance to the target sublevel, reducing the supremum to tangents h_y. For 0<Delta<G and u>0 the relevant slopes are y>0, with target distance d_y=u-y/2-y_*^2/(2y) and exact loss d_{y_*}-d_y=(y-y_*)^2/(2y), proving the unique optimizer y_*=u sqrt(1-r). At Delta=G, y->0+ approaches but never attains the supremum; at Delta>G, h=0 has empty target and infinite slowness under the source convention. Substitution into the W inequality gives the stated necessary-and-sufficient trial-modulus frontier. Symmetry restores |u|.

## originality

PASS

The 2026 primary paper introduces descent-slowness and the affine W-certificate and proves how a certificate controls the gap, but its inspected certificate section and quadratic experiments do not optimize slowness over all affine minorants of a scalar quadratic or state the modulus-inflation/nonattainment frontier. The earlier W-stationarity paper uses a different radius/W-gap construction, and Lan's bundle-level paper predates this certificate. Three targeted Resultary searches returned no equivalent published SCOPE result.

## value

PASS

The trial growth modulus is a central adaptive quantity of the new W-certificate framework, and the scalar strongly convex quadratic is its canonical exact-growth benchmark. A complete necessary-and-sufficient inflation frontier, including the sharp nonattainment at the true gap/modulus, gives a motivated boundary fact about what the certificate can geometrically achieve; it is more than a numerical example or routine verification of a single parameter choice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
