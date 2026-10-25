---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

Plane-filling degree-4 forms over F2 constitute 8-dimensional evaluation kernel (256 quartics); F_A=det(AX,X,X^[2]) has kernel precisely scalar matrices. Geometric smoothness is equivalently rank 66 for the degree-10 Macaulay map (H,Hx,Hy,Hz) and corresponds to irreducible characteristic cubic of A. Exact enumeration yields 48 irreducible matrices modulo scalar pair=24 distinct smooth forms; over F2 three nonzero members of W are F,G,F+G, giving eight pencils, a single GL3(F2)=168 orbit, stabilizer 21. An independent matrix-bitmask calculation reproduced 168/24/8 and checked the displayed representative triplet; inspected standalone Macaulay-rank and conjugacy programs independently encode the full checks. Common stabilizer C7 is a Singer group, transitive on seven rational points with three algebraic eigenpoints over F8. Base rational intersections are transverse since F,G,F+G have nonzero distinct gradients at F2-points. Bezout length 16; any remaining non-eigenpoint has a 7-element orbit, too large for 16-7-3=6 remainder; three conjugate eigenpoints each contribute multiplicity (16-7)/3=3. This is a finite exact classification coupled to a geometric proof.

## originality

PASS

Homma–Kim classify individual smooth minimal plane-filling quartics and their automorphisms; Asgarli–Ghioca study existence of smooth pencils for larger fields and higher-degree plane-fillers. The examined primary statements do not cover exact eight binary smooth quartic pencils plus scheme-theoretic eigenpoint triple intersections. Homma–Kim full text remained unavailable, so priority risk is preserved.

## value

PASS

Classifies natural simultaneous plane-filling and smoothness compatibility over the minimal field, resolving a finite exact pencil census and producing an informative nonreduced Singer base-intersection geometry; not merely recounting known 24 individual smooth quartics.

The dated certificate retains the supplied scientific assessment, sources and limitations.
