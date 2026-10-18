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

# Reproducibility and mathematical scope

The standalone file `verify_heawood_duality.py` regenerates both simplicial complexes from the binary-dot-product definition of the Fano incidence graph. Run `python3 verify_heawood_duality.py`. No external libraries or datasets are required. A successful run ends with `VERIFY_OK`; `verify_output.txt` is the output of one actual successful execution.

The program exhausts all incidence-compatible bijections and independently computes their number using a subset permanent, enumerates all faces of both complexes, constructs complete mod-two boundary matrices, and derives rational ranks from exact chain inequalities. It enumerates every group automorphism as a Fano linear map or a bipartition-swapping duality, calculates its action on graph edges, and evaluates the reduced homology character both from direct fixed oriented faces and from unions of permutation cycles. It proves equality of the two character computations and the sign-twist relation for all \(336\) elements. It also enumerates the eight Sylow-seven subgroups and checks exact inner-product orthogonality of the resulting rational constituents and invariant dimensions.

This is an exhaustive finite certificate for the specified Heawood graph, not an infinite-family argument. Character comparison over \(\mathbb Q\) gives an abstract rational representation isomorphism, not an explicit chain map, integral lattice splitting, or equivariant homotopy equivalence. A software run log alone does not substitute for inspecting the code and the proof. Existing nonequivariant homotopy and the ordinary-complex equivariant module are used as prior context, not presented as novel claims. The provided mathematical arguments and replay are self-reviewed; no independent scientific audit has been performed.
