---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

In the tensor embedding, a homogeneous quadratic tensor commuting with a nonzero v (chosen as first basis vector) can only be a multiple of vv. The alternating degree-two commutator space contains no such nonzero tensor, in characteristic two as well. Thus [v,−] on degree two is injective. For independent degree-one projections v,v′ the five vectors x,y,[x,y],[x,[x,y]],[y,[x,y]] are independent by degree: the degree-two bracket is nonzero, and the two degree-three leading terms have different multidegrees in a basis beginning with v,v′, each with a word coefficient ±1. They also span by class three, giving the free rank-two type. For rank-one projection, subtract a multiple of the generator with nonzero projection; if the resulting degree-two part is nonzero there is a nonzero central bracket, independent of the two generators by degree, giving Heisenberg. Otherwise they commute, as do pairs with both projections zero. Independence of projections gives P5=(A−1)(A−q)(BC)^2. At rank one there are (A−1)(q+1) projected pairs and B²−B noncommuting degree-two lift choices per pair, by the injectivity above, with C² central choices. The commuting total is BC²[B+(q+1)(A−1)]; removal of the zero pair and the (q+1)(ABC−1) rank-one pairs gives P2. The ordered generating lifts of an abelianization basis have cardinality 1, q², q^6 for the two-dimensional abelian, Heisenberg and rank-two free types respectively; generation follows from nilpotence. Multiplying those fiber sizes by |GL₂(q)| and dividing the corresponding P_d verifies S₂,S₃,S₅. Comparing degree-one and degree-two bracket constraints gives centralizers W₂⊕W₃ or kx⊕W₃ for the two noncentral cases; the center is W₃. At n=2 both noncentral sizes have dimension 3, as allowed by the statement. The supplied verifier was read, not replayed. Its small exhaustive checks and larger seeded checks are not used to extend the field-independent proof.

## originality

PASS

Pass for the joint uniform rank-n spectrum and all distinct-type counts, not for the familiar structural observations in isolation or the already covered rank-two odd-characteristic abelian census. The strongest exact overlaps found are with the rank-two breadth algebra and the later two-Engel census for the same free algebra; neither gives the remaining full rank-uniform census. Boral's thesis presents a real unresolved comparison for the structural classification and possibly more.

## value

PASS

The spectrum supplies a uniform finite-field probability law and distinguishes the actual generated isomorphism types, including the intermediate Heisenberg outcome. The distinct-subalgebra counts give a separate census useful when all generating pairs would overcount, and the formulas distinguish which abelian or nonabelian strata survive in small characteristic. This is a natural full class-three count, beyond a single low-rank example or an isolated centralizer calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
