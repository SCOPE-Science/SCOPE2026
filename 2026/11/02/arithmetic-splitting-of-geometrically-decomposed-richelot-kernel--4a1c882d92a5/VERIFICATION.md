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

Independently checked exhaustiveness without relying on the supplied norm calculations. The fifteen matchings have either three cross pairs (six) or one cross pair (nine) between the L and R triples. For three cross pairs the permutation is j↦b±j. With the minus sign, all quadratic constant terms are ω^b and the determinant vanishes. With the plus sign, the three quadratic rows are proportional by column factors to the invertible cube-root Vandermonde; the sole possible zero comes from the common linear-coefficient factor A+A⁻¹ω^b. This occurs exactly when t=A²=−ω^b, one additional matching when s=0. For a one-cross-pair matching with cross roots X=Aω^i,Y=A⁻¹ω^l, the other two quadratic rows are (1,X,X²) and (1,Y,Y²). The determinant against (1,−X−Y,XY) is (Y−X)(X²+4XY+Y²). Smoothness gives X≠Y, so the sole zero condition is z²+4z+1=0 for z=X/Y=tω^{i−l}. The relation z³+z⁻³=−52 is equivalent to s²=−50, since the degree-six polynomial factors as the stated quadratic times quartic; for any such s one can choose t to be a quadratic root and choose the sign of A. Two different differences i−l cannot qualify simultaneously: the distinct quadratic roots would be reciprocal and differ by a cube root of unity, forcing t⁶=1 and s²∈{0,4}, impossible in p≥7. Thus exactly three extra matchings occur in that stratum. Frobenius adds opposite k shifts to L and R labels, possibly swaps the triples, and sends each base index b to εb. For the normalized exceptional fibers k=0: A^q=A^{±1}, using A²=−1 or the reciprocal quadratic and the invariance of nonzero A³+A⁻³ in the latter case. On the s=0 addition the component swap and label negation both preserve the matching. On the three s²=−50 additions, the component swap fixes every matching, and label negation transposes the two nonzero diagonal-cross indices. This yields all six cycle types, not just fixed-point counts. Since −50=(5²)(−2) and the excluded ±2 and 0 are disjoint from this locus, the character frequencies follow; zeta factors depend on the orbit lengths. The determinant criterion is for a geometrically decomposed polarized quotient and does not require either elliptic factor to be defined over the base field.

## originality

PASS

Credit attaches to the complete arithmetic cycle classification of the geometrically decomposed subset in this pencil, especially the exceptional fibers, not to the known geometric counts, generic involutions, or the character and zeta formalities once cycles are known. The prior automorphism and all-kernel arithmetic results give substantial partial coverage and methods, but no checked prior statement determines the full selected-subset table.

## value

PASS

This is a natural automorphism-rich pencil with two geometrically distinguished exceptional strata. The orbit classification determines exactly which outgoing decomposed Richelot kernels are available over the base or quadratic extension, an invariant needed for arithmetic isogeny calculations that geometric totals or counts of all rational kernels cannot supply. The all-prime-power statement, including the exceptional fibers and distinction from descent of factors, provides a usable classification rather than a finite enumeration or a renaming of the geometric counts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
