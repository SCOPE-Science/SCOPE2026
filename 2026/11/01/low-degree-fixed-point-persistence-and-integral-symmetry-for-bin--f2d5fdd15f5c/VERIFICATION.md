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

The geometric fixed set is the orbit-centroid subcomplex: its vertices are invariant orbit simplices and joins require all cross-orbit vertex distances <= r. For a weight-one generator the cross-max is 1+d(y,z); for either two-dimensional allowable subgroup it is 2+d(y,z). For a two-bit flip, same-color cross-max is 2+d and different-color is 1+d. The r=2 orbit graph has 2^(n-1) vertices and is a standard cube graph; its integral cycle rank is 1+2^(n-2)(n-3). At r=3 all newly added edges reduce through triangles to the cube graph, whose elementary squares bound cones, so pi_1 vanishes. The argument extends to all later scales by shortening new edges. Exact shift models give the stated low-degree barcodes, with no torsion. Signed edge/vertex permutation traces in 0 -> L -> C1 -> C0 -> Z ->0 yield tr(0,h)=1-f+2e and tr(1,h)=1-q. Independently enumerated every coset and cross-distance for 89 (n,type,scale) cases n=2..7; all agreed. These bounded cases support, but do not replace, the stated all-n proof.

## originality

PASS

The radius-two fixed-locus result is explicitly treated as prior, and ambient hypercube Rips homology/representations do not directly compute geometric fixed-point loci. No identified prior statement implies the all-scale fixed filtrations together with the integral residual cycle representation; pass is best-of-knowledge, with a real risk of overlooked equivariant literature.

## value

PASS

The passage from a previously identified radius-two fixed graph to its full low-degree persistence gives a natural sharp death threshold and nontrivial integral equivariant information: a signed cycle-lattice module for the residual centralizer. Geometric fixed loci are a standard but distinct invariant from invariant ambient homology, so the complete low-degree barcode and action can be independently used in equivariant topological-data questions. The claim goes well beyond renaming a rank or a routine normalization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
