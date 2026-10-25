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

The body |x_i|<=2 and |x_1|+|x_2|+|x_3|<=3 has the 24 distinct signed permutations of (0,1,2) as vertices. Its 36 Euclidean length-sqrt(2) edges have endpoint squared norms five and inner products four. A central plane with normal u crosses exactly those edges whose endpoint scalar products have opposite signs, and a generic section vertex corresponds to exactly one crossing. In the sorted positive-normal wedge x>y>z>0, only signs of x−2y, x−2z, y−2z change; the five feasible chambers have section N=8,10,6,8,6 at stated rational representatives. Ten-sided region x>2y, y<2z is a spherical triangle spanned by (1,0,0),(4,2,1),(2,1,1), giving solid angle 2 atan(1/D), D=11+3sqrt(14)+4sqrt(6)+2sqrt(21), and P10=24 atan(1/D)/pi. Every edge has antipodal projection sign-split probability alpha/pi with alpha=acos(4/5); hence E N=36alpha/pi. Solving normalization and mean with N in {6,8,10} yields P6=4−18alpha/pi+P10 and P8=18alpha/pi−3−2P10. I separately enumerated 24 vertices, 36 edges, all five signed-chamber counts using integer arithmetic and the spherical-angle probabilities to 12 decimals; the packaged checker was inspected but not rerun. This finite chamber partition PLUS analytic solid-angle/mean integrals proves the continuous law; Monte Carlo is not needed for the proof.

## originality

PASS

Best-of-knowledge novelty is the specific fully quantified invariant, not the underlying classical method or any known special-case total count. Same-object aliases and combinatorial slicing signatures were searched. The edge-cut formulation provides a derivation, not an earlier evaluation of Haar chamber solid angles in the checked literature. Known isoperimetric or section-existence conclusions have different quantifiers from a random-Haar metric distribution; they neither imply nor contradict this exact calculation.

## value

PASS

The BCC Voronoi cell/regular truncated octahedron is a canonical space-filling polyhedron. Its entire orientation-dependent central-section polygon side law is a natural exact stereological benchmark; the derivation distinguishes five normal chambers and a nontrivial decagonal solid-angle contribution. Exact probabilities and mean for three possible section types are not recoverable from the mere existence of 6-,8-,10-gons, so this is a meaningful complete invariant of a natural solid.

The dated certificate retains the supplied scientific assessment, sources and limitations.
