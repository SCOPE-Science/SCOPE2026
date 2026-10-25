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

The proof correctly distinguishes Crofton planes from uniformly oriented conditioned planes: for normal n the allowed offsets have length 2A, A=max(a|n1|,b|n2|,c|n3|), and exactly |t|<B, the median vertex-height magnitude, produces a hexagon. Thus true probability is EA(B)/EA(A) with both expectations under original uniform normal; the width is properly accounted for. The exact median identity B=sum pairwise maxima−2A and pairwise spherical integrals Emax(a|n_i|,b|n_j|)=sqrt(a²+b²)/2 give EB=S/2−2EA. For an octahedron each of the 3 edge-length classes has 4 edges, exterior dihedral angles 2 arctan(ab/(c sqrt(a²+b²))); the Steiner mean-width formula yields EA=T/π, hence πS/(2T)−2. Axial derivative T′=S′φ and (T/S)′=√2 S′(φ−ψ)/S² changes sign only at λ=1; both exact degenerations follow from arctan limits. Independent direct arithmetic evaluated the probability at λ=.01,.1,.5,1,2,10,100 with valid 0..1 values and unique sampled peak at 1; finite values alone do not prove uniqueness. The edge-crossing checker code and limits are inspected, but Monte Carlo is not used as universal proof.

## originality

PASS

Two closest published octahedron laws on Resultary are exact triaxial and axial 2D ORTHOGONAL PROJECTION/shadow probabilities; their full RESULT.md texts were inspected. Their regular octahedron hexagon-shadow value is ≈0.350959, in contrast to the Crofton affine-section regular value ≈0.552149656, directly proving these probabilities are different observables. The source on polytope slicing addresses combinatorial reconstruction from slices, not width-weighted affine-plane probabilities. The regular affine-section benchmark and mean-width identity are acknowledged prior/standard; new statement is full positive triaxial Crofton law plus strict axial ratio classification. Historical Crofton formula may be unindexed.

## value

PASS

A complete triaxial probability law for randomly intersecting affine planes and a sharp single-axis rigidity theorem are natural stochastic integral geometry invariants. It cleanly demonstrates how random offsets and width bias change section-face probabilities versus shadows; the exact degenerations explain the boundary geometry.

The dated certificate retains the supplied scientific assessment, sources and limitations.
