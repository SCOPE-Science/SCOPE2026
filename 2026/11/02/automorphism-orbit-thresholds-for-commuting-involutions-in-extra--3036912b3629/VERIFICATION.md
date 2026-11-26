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

For a labeled map E -> G its projected image is totally singular, since squares and commutators are trivial. The induced quotient action is all of O(V,q): lifts of a transformed basis give the same presentation, with the center fixed, and the relations give at most 2^(2m+1) normal forms. The kernel acts by V*; for a difference character vanishing on K the restriction from V* to the image U is surjective (also realized by inner twists by nondegeneracy). Witt extension of the isometry of the totally singular projected images, followed by such a twist, makes the maps coincide exactly, not just their images. Conversely K and χ are preserved and any pair occurs by choosing a complement of K and basis lifts. The Gaussian count and type-difference term then follow with r=0 giving one. For raw counts the number of nonzero singular vectors in the j-step quotient is (2^(m-j)-1)(2^(m-j-1)+1) for plus and (2^(m-j-1)-1)(2^(m-j)+1) for minus; multiplying lift counts 2^j and dividing by the ordered basis count gives exactly T_±. Every surjection onto U lifts in 2^r ways; at r=1 the raw difference including identity is 2^(m+1).

## originality

PASS

The supported distinct contribution is the full-postcomposition orbit classification of labeled elementary-abelian maps, and the first rank at which its count detects type. Raw counts and the quadratic model, Witt extension, and singular-space counts are not credited as original. Inspected inner-conjugacy, raw-count, and subgroup-geometry results do not provide the labeled fusion and kernel-character conclusion in this setting.

## value

PASS

The profile measures equivalence of ordered commuting involutions rather than just existence, subgroup counts, or quotient geometry. It isolates exactly the central data surviving all automorphisms and proves a sharp delayed type-detection threshold despite immediate separation by raw counts. That distinction and complete orbit profile are useful for labeled-map enumeration; verifying classical T_± is not itself the contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
