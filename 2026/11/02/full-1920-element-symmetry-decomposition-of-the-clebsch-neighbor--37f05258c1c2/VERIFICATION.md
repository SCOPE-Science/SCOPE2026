---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Finite verification

Run `python verify.py` using Python 3.8 or newer and the standard library. The program generates the Clebsch graph as even-weight vectors of five bits with Hamming-four adjacency and computes all simplicial faces.

The actual checks give \(16\) vertices, \(352\) nonempty faces and face vector \((16,80,160,80,16)\). All signed consecutive boundary compositions vanish. Elimination modulo \(2\), \(3\), \(5\) and \(101\) gives boundary ranks \((15,65,64,16)\), with the rational ranks forced to the same numbers by rank saturation. The complete generated group has \(1920\) distinct graph automorphisms and exhausts the theoretical upper bound. Signed cellular Lefschetz traces are checked on every group element; their sum is zero and the sum of squares is \(5760\). The Fourier projections are compared for each permutation in the stabilizers of the zero-, one-, and two-element dual subsets. Dimensions of the three resulting rational irreducibles are \(6,15,10\), with no invariant line.

The success marker is `CLEBSCH_NEIGHBORHOOD_FULL1920_THREE_IRREDUCIBLES_VERIFIED`.

The verification is a fully finite exact computation; it establishes neither a unique bibliographic origin nor an integral/equivariant homotopy classification. Independent audit has not been performed.
