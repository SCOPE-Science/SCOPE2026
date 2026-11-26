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

Write multiplication as cyclic shift P of the coordinatewise product. Squaring a vector with a nonzero coordinate shows that the support of the span of coordinatewise products equals that of U. Closure makes that support shift-invariant, so a nonzero U has full support. Choose d independent coordinate restrictions, d=dim U; their diagonal bilinear tensors are independent, so the product span has dimension at least d and by closure no more. Every other coordinate restriction therefore has its tensor square in their diagonal span. Off-diagonal tensor coefficients force it to be proportional to exactly one chosen restriction, including in characteristic two. Equality of the shifted product span and U makes that partition translation-invariant; its zero block is a subgroup, so blocks are residues modulo d with d|n. Normalize the least coordinate in each block to 1. The weights then propagate by squaring across blocks and the successive block-zero weights satisfy b_0=1 and b_{k+1}=c*b_k^(2^d), with b_{n/d}=1 precisely when c^M_d=1. These equations also prove closure and uniqueness (if d<n, c is the normalized weight at coordinate d; otherwise only c=1). Inclusion forces refinement modulo e and hence d|e; the ratio of weights at e and 0 gives h=c^((2^e−1)/(2^d−1)) when e<n, and the general exponent-difference identity proves sufficiency. For e=n the same equation holds by wraparound. Nonzero cycle constants show perfection and allow an ideal element's nonzero coefficient to be isolated by multiplication and propagated to all basis vectors. The result is a weighted cycle as exhibited in the proof, not necessarily isomorphic over K to the unweighted E_d(K). Over F_q cyclicity of the unit group gives the gcd counts. Independent bounded checks exhaust all subsets of F_2^4 for the subspace/closure test (counts 1,1,1,1 in dimensions 0,1,2,4), and check all constructed F_8, n=6 nodes for closure and their pairwise inclusions by rank (1,7,7,1,1 in dimensions 0,1,2,3,6). The latter does not enumerate all F_8 subspaces; exhaustiveness there and in arbitrary fields is from the proof.

## originality

PASS

The supported distinct result is the all-dimensional embedded classification and explicit incidence condition over arbitrary fields, with its full finite-field count. General disjoint-support bases and the dimension-one count are known and not counted as new. The strongest homomorphism overlap reaches only the images of maps from unweighted cycles; it need not reach every subalgebra even over finite fields.

## value

PASS

This gives the entire incidence structure for a natural simple family, rather than just counts of idempotents or abstract isomorphism types. Containment is a concrete power map over the ground field, and the result includes subalgebras that need not be embedded copies of the smaller unweighted cycle. It provides an exact reusable finite-field polynomial and an arbitrary-field classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
