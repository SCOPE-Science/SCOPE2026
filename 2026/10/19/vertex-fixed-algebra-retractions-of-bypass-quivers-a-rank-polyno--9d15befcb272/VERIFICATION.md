---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

For the specified relation-free three-vertex path algebra, fixing the vertices forces the arrow images into their endpoint corners. The maps on the two consecutive arrow spaces are S and T, the map on direct arrows is (D,B), and the map on length-two paths is P=S⊗T. There are no unstated multiplicativity conditions. Idempotence requires S,T,D to be projections and BD+PB=B. Splitting by image and kernel gives exactly B(im D)⊆ker P and B(ker D)⊆im P, in every characteristic. This gives the stated power of q, independently of the Gaussian-binomial counts of image/kernel decompositions. The corner image projects onto im D and meets the path space in im P, so its rank is d+ab. All triples occur, and lowering a or b from the maximal pair costs at least two ranks, proving the codimension-one coefficient and both unique extremes. The small example was recomputed from I_2(2,k)=(1,6,1): the coefficients in ascending attainable-rank order are (1,28,194,104,288,48,48,16,1), totaling 728; neither 7 nor 8 occurs as a product (a+1)(b+1), hence rank 10 cannot occur for t=1. This finite arithmetic supplements the general proof, not the converse.

## originality

PASS

The strongest inspected overlaps establish the bypass shear, general path-algebra morphisms, and related rank enumerations, but do not give or subsume the exact anchored, composition-idempotent rank count on these corners. Credit is limited to the full weighted rank distribution and rank gaps, not to the shear or Gaussian-binomial projection counts.

## value

PASS

The smallest acyclic bypass geometry in which direct-arrow and path images share a corner gives a natural test of split algebra images. The formula counts labeled splitting maps including the path-valued shear multiplicities, and gives a field-independent forbidden codimension-two rank in the exhibited example despite the adjacent ranks occurring. This supplies useful exact data not recoverable from counting linear projections alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
