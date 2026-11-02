---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

Accept Ostrovski’s published polygon existence, rotation number, and foliation for his special parameter family, not any generic angle. Quarter-orbit closure after K corner steps and N bottom shears gives r_N(1+N delta)=1. Because det B=1, each corner or shear increment has raw determinant -t delta r_N^2. The fourfold shoelace identity, including its center-translation telescope, yields enclosed polygon area 1-4t r_N+2t(1-K delta)r_N^2, hence outer area 4t r_N-2t(1-K delta)r_N^2. At N=0 this equals 2t(1+K delta). Published continuous monotone foliation identifies the exact exterior-polygon area with the slow-rotation sublevel distribution at rho_N=1/[4(K+N)]. Since neighboring thresholds differ by O(N^-2), monotone sandwiching upgrades the discrete expansion to all eps: area=(16t/delta)eps+O_K(eps^2); normalize by the annulus area to obtain the reciprocal-rotation 1/R tail and divergent expectation. The reciprocal rotation number is not mistakenly interpreted as an orbital return period.

## originality

PASS

The exact all-level Lebesgue area law and the small-rotation measure tail are not contained in the inspected source theorem, which constructs/foliates the polygons and states their rotation numbers. They are additional geometric computations, although determined by published geometry.

## value

PASS

The nontrivial quantitative invariant is the area distribution of invariant-circle rotation speeds in a known integrable island. The rational all-N formula, sharp small-winding coefficient, and heavy-tail exponent quantify a dynamical observable that cannot be read from qualitative foliation alone. An exact measure law of a natural invariant annulus is independently useful despite being derived from published orbit geometry.

The dated certificate retains the supplied scientific assessment, sources and limitations.
