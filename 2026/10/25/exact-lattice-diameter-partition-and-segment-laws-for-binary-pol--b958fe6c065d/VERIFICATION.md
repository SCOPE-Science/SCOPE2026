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

A diameter segment has integer-point distance equal to the gcd of its endpoint coordinate differences. Every pair of scaled binary vertices attains gcd=n, while [0,n]^d bounds the gcd above by n. If x,y attain diameter then some coordinate equals 0 and n, so choosing any vertex of each point’s minimal P-face gives different labels, proving a proper f0(P) coloring matching the scaled-vertex clique. Each unoriented primitive ternary direction u has a unique zero-coordinate common part z in the rational polytope R_u; the resulting disjoint Ehrhart sums prove quasipolynomiality from n=1, including lower-dimensional pieces. The hypersimplex signed-support count, unique s=1 degree-leading term and Eulerian normalized volume follow, as does the parity tetrahedron support casework. Independent exact gcd enumeration confirmed 45 hypersimplex parameter triples (d<=6,n<=3) and 11 tetrahedral dilations.

## originality

PASS

Best-of-knowledge PASS with precise overlap: Averkov–Brose–De Loera–Lopez-Campos–Torres (arXiv:2508.20009v2, Theorem 4.6) proves eventual Ehrhart-type quasipolynomiality for any integral P and Theorem 5.4 universal bound 2^d on lattice Borsuk, but not the exact f0(P) equality for every binary P and n, from-the-first-dilation decomposition, hypersimplex formula/Eulerian leading term or exact period-two tetrahedron. Their Lemma 5.2 clique characterization underlies the framework, not the binary vertex-face injection. Euclidean/Hamming Borsuk results on matroids concern another diameter metric.

## value

PASS

PASS: natural full-class sharpening of a current lattice-diameter program. Exact face-based coloring replaces a uniform 2^d bound with an intrinsic vertex invariant. Rational Ehrhart slices give the entire segment sequence, hypersimplices supply an explicit rank-sensitive closed formula, and a small parity tetrahedron proves true quasiperiodicity cannot universally be strengthened to polynomiality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
