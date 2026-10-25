---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

Full cube matching complex face vector (12,42,44,9), signed boundary ranks (11,31,9) and previously known wedge4 S2 are consistent. Independent exhaustive enumeration of all 4096 induced vertex sets gives mod2 H2-supported counts by size 8:6,9:24,10:42,11:12,12:1, none <=7. The six 8-vertex sets complement precisely six nonparallel cube perfect matchings. The displayed 4 free-face collapses leave an 8-vertex 18-edge 12-triangle closed connected surface with vertex-cycle links and Euler characteristic 2, so S2; full cube symmetries permute all six. The submitted Smith-unit matrix certificate (9 ∂3 columns plus 4 carrier cycles, rank13 all unit factors) ensures integral generation of H2=Z4, stronger than rational or mod2 spanning. Independent full 48-element automorphism Lefschetz computation confirms S4 class traces (4,0,0,1,2) and antipodal-composed (2,−2,−2,−1,0), giving even Specht(2,1,1) and odd trivial one-dimensional piece. SNF part inspected in source algorithm, not independently rerun.

## originality

PASS

Exact same ordinary cube matching complex homotopy wedge4 S2 is established in published 2026 Resultary full text and explicitly credited; that theorem does not study induced support minimality, six sphere carriers, integer primitive spanning or Aut(Q3) action. Braun–Hough treat planar two-row grids rather than a 3-direction cube. Related Morse complex of Q3 has different vertices (acyclic graph-edge matchings), so its homology cannot be conflated with ordinary matching complex.

## value

PASS

Shortest induced supports for ambient H2 are a natural geometric/sparse-realization invariant of a canonical graph complex. The complete six-carrier classification, primitive integral generators and antipodal parity decomposition add independent structural information to an already-known homotopy type; valuable without claiming a higher-dimensional Qn theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
