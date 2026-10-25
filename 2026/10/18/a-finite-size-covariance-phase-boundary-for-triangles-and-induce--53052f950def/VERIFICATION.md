---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

Counting cycle edge sets with c_ell=(ell-1)!/2 and forbidden chords ell(ell-3)/2, only overlaps of 2 or 3 triangle vertices with the induced cycle can contribute. For 2 vertices a shared edge is a required cycle edge with fraction 2/(ell-1), otherwise a prohibited chord; averaging yields p^(ell+2)(1-p)^q[2/(ell-1)-p]. For 3 vertices the triangle is impossible inside induced C_ell, giving -p^(ell+3)(1-p)^q. Their multiplicities per triangle are 3*C(n-3,ell-2) and C(n-3,ell-3), respectively. The exact affine bracket has a single positive root for n>ell, no positive root for n=ell. Algebraic differentiation of the rational root yields the n-upward and ell-downward monotonicity and fixed-ell limiting shift. Independently enumerated full 2^(n choose 2) labeled graph probability spaces for five rational configurations through n=6; agreement includes exact zero at (n,ell,p)=(5,4,2/5), with sign grids through n=23. Finite enumerations are cross-checks only.

## originality

PASS

Classical overlap/flag expansions are standard, but Ellis–Ferry study variance of a single ordinary noninduced motif, and Sah–Sawhney study single-motif local limit/exceptional density theory. Neither inspected treatment states this exact evaluated triangle-versus-induced-hole covariance and finite-size phase boundary. Janson 1990 addresses joint or induced subgraph counts and is a serious possible source of general formulas; full text could not be obtained and authorized institutional route reported VPN disconnected. No definitive statement of noncoverage is made for Janson.

## value

PASS

The joint sign of two fundamental network motifs, triangles measuring local transitivity and chordless holes measuring chordality obstructions, is not determined by separate moments. The result gives a complete finite-order and all-hole-length covariance phase diagram, threshold ordering and exact finite-size correction, including the sharp n=ell negative boundary. This is a natural multi-parameter mixed-statistic question rather than an arbitrary isolated graph calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
