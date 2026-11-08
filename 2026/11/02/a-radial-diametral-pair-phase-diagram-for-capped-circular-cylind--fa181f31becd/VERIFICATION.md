---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

For top/bottom disk points, every surface path must cross rims; optimize chord+unrolled lateral geodesic+chord. The all-angle minimum of chord costs is obtained from the first point where a focal ellipse touches the rim, not from a symmetric-contact guess; it yields the exact piecewise G_R,r(t). Competing against known D=h+2R defines the infimum critical radius. The function 2R cos(t/2)+sqrt(h²+R²t²) has no interior minimum, giving h0=(pi²-4)R/4, and its near-zero expansion gives the second threshold 2R. Strict shortcuts exclude non-opposite-cap candidates above h0. Independently tested focal angular minimization on dense grids and one-dimensional profiles; these numerical tests are not used as proof.

## originality

PASS

Qualified best-of-knowledge: exact cylinder diameter and part of the antipodal geometry are prior work. The new claim gives full equal-radius opposite-cap diametral criterion, sharp two thresholds and complete locus of all diametral pairs above the first threshold.

## value

PASS

Equality cases of a known intrinsic diameter are mathematically natural. A complete sharp opposite-cap radial phase diagram, with two nontrivial thresholds and uniqueness for tall cylinders, is useful geometry rather than merely recomputation of diameter; its intermediate regime has genuinely changing maximizing loci.

The dated certificate retains the supplied scientific assessment, sources and limitations.
