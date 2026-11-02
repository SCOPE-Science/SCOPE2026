---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

The finite field F4 with t²+t+1=0 defines 16 points and 20 affine lines. Both affine line listing and determinant condition identify the same 80 forbidden collinear triples, so the cap complex has exactly 1792 nonempty faces with f=(16,120,480,840,288,48). An independent implementation rebuilt the deterministic 16-stage lower/upper face matching from the definition, obtaining exactly 783 pairs; its freshly serialized CSV matched the actual Git MATCHING.csv blob byte for byte (8243 bytes). Every one of the 6768 Hasse cover incidences was oriented downward unless matched, and a complete topological sort reached all 1792 faces, proving acyclicity. Exactly one critical vertex and 225 critical 3-simplices remain, with no cells of any other positive dimension. By discrete Morse theory the resulting CW complex has one 0-cell and 225 3-cells attaching to a point; it is therefore a genuine wedge of 225 S³ over Z, not merely a homology computation. Verification exhausts the finite complex rather than sampling it.

## originality

PASS

Alan Lew’s primary MSc thesis Section 6.2 and Figure 6.4 compute precisely the same AG(2,4) cap complex face vector and integral homology Z^225 in degree 3; both are explicitly credited and NOT novel. Lew does not give its homotopy decomposition or the 783-pair complete acyclic matching. Since a nonpure 5-dimensional simplicial complex with concentrated integral H3 is not automatically a sphere wedge, the submitted exact CW collapse is a stronger homotopy assertion. Resultary general matching/independence-complex records treat different complexes. No earlier equal homotopy statement found in materially inspected sources; residual historical priority risk remains.

## value

PASS

This is a naturally defined nonpure cap complex of a canonical finite affine plane, with maximal faces of cardinalities four and six. Its previously known torsion-free homology cannot by itself settle homotopy type. The fully explicit acyclic Morse matching resolves the precise integral wedge decomposition and annihilates possible higher-dimensional attaching behavior. A complete finite classification of this motivated complex has standalone value without a general q theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
