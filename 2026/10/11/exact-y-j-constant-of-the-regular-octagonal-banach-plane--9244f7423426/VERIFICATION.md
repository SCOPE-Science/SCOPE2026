---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

Corrected orientation N(x)=N(y)=N(x+y)=1 and objective N(x-y) verified against full RESULT and code. New checker enumerates 8^3 active facet triples and all 24 fourth facets, solves every nonsingular system in Q(sqrt2), tests 24 support inequalities and compares all eight objective forms exactly: 96 feasible systems, 48 vertices, maximum 2sqrt2-1. Explicit x=(1,1-sqrt2), y=(2-2sqrt2,sqrt2-2) satisfies all THREE unit constraints and attains the bound; the original witness had the y sign wrong and its original checker reversed the objective. New full RESULT and verifier are supplied, not merely suggested. Finite certificate is exhaustive by compact active-facet LP reduction, not by sampling.

## originality

PASS

The corrected centered-triple extremum is not mechanically supplied by the published classical James or Schäffer octagon constants. The 2021 paper gives an exact alias via delta_X(1), so that alias was searched; no consulted theorem implies the specific octagonal radical. This is best-of-knowledge originality, not an assertion that inaccessible texts contain no such value.

## value

PASS

The Fu--Liu--Li centered equilateral-triple constant for a canonical non-Hilbert octagonal norm is a concrete unknown unit-separation convexity invariant. Its exact radical identifies a nontrivial facet extremizer and provides a usable calibration for comparisons of Y_J, J1 and δ_X(1); the numerical coincidence with an unrelated rectangular constant does not make it a textbook substitution. No general polygon classification is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
