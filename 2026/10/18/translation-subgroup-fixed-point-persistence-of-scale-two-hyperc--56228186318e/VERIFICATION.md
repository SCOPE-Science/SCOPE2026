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

The barycentric-coordinate fixed-orbit lemma identifies |K|^H with the complex of H-orbits whose unions are faces. For the cube this is precisely the coset Hamming diameter criterion. Weight-one H has cosets with graph adjacency Q_{n-1} at r=2 and isolated cosets at r=1. Weight-two H has A_y,B_y bipartite Cayley generators (1,0),(1,e_j) forming an F2 basis, yielding Q_{n-1}. Every rank-two subspace of nonzero weights <=2 is either a coordinate square or a 3-coordinate even-parity plane; distinct orbits cannot combine, giving 2^(n-2) isolated barycenters. Such planes admit no admissible rank-three extension. Vertex/edge counts give cube cycle rank 1+(n-3)2^(n-2), and constant integer-threshold filtration gives the asserted persistence. Independent direct coset/compatibility enumeration for every rank<=3 H at n=3,4,5 found rank-one graph loci 6,10,15; rank-two point loci 4,10,20; no exceptions. No extrapolation from finite checks.

## originality

PASS

No exact equivalent fixed-locus theorem was found in the bounded searches; the nearby scale-two Čech representation concerns the closed-neighborhood nerve, whereas Rips(Q_n;2) is the Hamming-distance clique complex and has different homology degree.

## value

PASS

Complete integral geometric-fixed-space diagrams under every nontrivial translation subgroup, including rank-two parity planes and actual scale-one-to-two maps, are natural equivariant refinements not recoverable from the known nonequivariant VR wedge or rational representation. Explicit orbit-complex isomorphisms make this a reusable small-scale subgroup-isotropy boundary, not a relabeling of the parent homology.

The dated certificate retains the supplied scientific assessment, sources and limitations.
