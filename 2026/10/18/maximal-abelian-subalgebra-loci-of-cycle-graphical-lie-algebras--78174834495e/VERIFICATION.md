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

Checked RESULT.md lines 5–51. Adding the central edge space preserves commutation, so any largest abelian subalgebra is its inverse image from a commuting vertex plane. Adjacent nonzero coordinate restrictions on that plane are proportional because independent edge labels test the corresponding exterior products, also in characteristic two. Dimension ≥2 rules out full support, and the nonzero runs each contribute at most one dual direction. Thus the dimension is at most floor(n/2), achieved by an independent vertex set. Equality gives independent directions, one per run. All run and gap lengths are one if n is even; if n is odd exactly one of them is two. The single doubled supported run has the indicated projective parameter with nonzero coordinates, whose two limits are the coordinate planes with a doubled omitted gap. Every such gap has exactly two endpoints in the family, obtained by thickening across either of its two omitted vertices; the neighboring line indices are i±2. No third line meets there. Each family is literally a Plücker line because the other a−1 vectors are fixed; the reduced union is the whole geometric locus by the support classification. Over any k, this union of k-defined lines (or points) has radical ideal after algebraic closure, and equality of the geometric zero sets identifies the reduced k-locus by contraction. Near an intersection the two lines can be made coordinate axes in their Plücker projective span, giving local equation uv=0 and hence an ordinary node in any characteristic. Step two generates the odd cyclic index group, so the normalization exact sequence gives χ(O)=n−n=0 and arithmetic genus one. Counting rational nodes once gives n(q+1)−n=nq, with two rational points in the even case. A separately written enumeration of commuting generating lines and their spans (python3 /workspace/review_checks.py 1) checked exact point sets and pairwise incidence on eight cases, including n=5 over F4 (20 points), and n=7 over F2 (14 points). These checks corroborate the field-independent proof; they do not certify unreduced scheme structure, and the frozen verifier was inspected, not run.

## originality

PASS

The supported distinct contribution is the global reduced equality-locus geometry: the explicit Plücker lines, their closed incidence and split ordinary nodes, and the resulting genus-one polygon for odd cycles. Dimension, finite-field support classification and the numerical count are not independently original: 640289cbe228 gives the latter by specialization, with substantial overlap in the proof's coordinate-support method. The strongest geometric comparator 0a1963133942 supplies local-in-stratum affine support arrangements, not the closure incidences among strata. Getting the global claim requires determining those closures and which limits coincide, not just evaluating the general censuses. No inspected source states or supplies that completed global gluing, and the date of 640289cbe228 does not establish priority relative to this record.

## value

PASS

The global equality locus refines a familiar maximal-dimension bound by describing all maximizers and their degenerations. The shift from two isolated choices to a connected rational-component curve of arithmetic genus one is a substantive structural invariant of the graphical construction. It is information not carried by the numerical census or by separate affine strata, and gives a useful test case for how maximal abelian loci on more general graphs are assembled.

The dated certificate retains the supplied scientific assessment, sources and limitations.
