---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

PASS: Frozen RESULT.md 4060c2f defines 120 normalized 600-cell vertices partitioned into T(24-cell) and Y(96-point snub). On S^3 with probability surface normalization, degree-l addition kernel is (l+1)U_l(x.y), harmonic dimension (l+1)^2. Independently constructed all 120 vertices in exact Z[phi] pairs, checked U_l 600-cell matrices satisfy U_l^2=(120/(l+1))U_l for l=0..5, and restricted first 24 rows to the integer 24-cell. Numerical diagonalization of that exact 24x24 integer matrix plus the proven kernel positivity yields spectra for Y by E_Y*E_Y=120I-E_T*E_T: l=0 96(1), l=1 96(4), l=2 96(9), l=3 72(8)+120(8), l=4 0(2)+80(9)+120(14), l=5 48(12)+120(24). Separate frozen CHECK.py verifies the stronger exact polynomial annihilators for T including K(K-8)(K-24)=0 in degree 4 and traces. Thus degree-four kernel dimension two and degree-five full rank with cond sqrt(5/2). Restriction is exact degree, not cumulative bandwidth.

## originality

PASS

PASS, best-of-knowledge for the precise six harmonic Gram spectra and degree-4-to-degree-5 injectivity recovery on the 96 snub vertices. Koca et al. provide the 600=24+96 vertex geometry and subgroup orbits. Bannai et al. provide harmonic-index design framework and 600-cell harmonic index 58 observation, which is not this multi-degree 96-point sampling spectral table. Group-representation and association scheme approaches could in principle yield these values but no inspected primary text stated them.

## value

PASS

PASS: The snub 24-cell is a canonical highly symmetric chiral configuration and degree-specific harmonic sampling rank is a natural interpolation invariant. Exact nonmonotone 2-dimensional nullspace at degree 4 followed by full degree-5 recovery and an explicit condition number is a meaningful structural erasure phenomenon; verified exact algebra prevents a floating-point artifact.

The dated certificate retains the supplied scientific assessment, sources and limitations.
