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

Counting ordered pairs means choosing x and then y=s−x. For s=0 every unit x gives z=0. For v_p(s)=a with 1≤a<k, z=s/(xy) has valuation a and the equation reduces after dividing by p^a to x(s−x)=s₀/z₀ modulo p^(k−a). Its mod-p roots are unit square roots of −s₀/z₀; simple lifting gives two roots for exactly half the unit z₀, and each root has p^a lifts. For unit s, the discriminant s²−4s/z ranges bijectively over residues outside one nonzero mod-p class, and every root gives a unit pair since the product s/z is a unit. A nonzero discriminant of even valuation 2j with square unit part has 2p^j roots: after dividing the root by p^j there are two simple roots mod p^(k−2j), each with p^j free lifts. The zero discriminant has p^floor(k/2) roots, and the omitted class subtracts p^(k−1) unit-square discriminants. This also covers p=3, where the unit-square stratum is empty. Squaring and counting gives m² at s=0, 2m² per nonunit valuation layer, and p^(k−1)[(k+1)(p−1)−3] per unit s (use the two parities of k). Adding these gives the stated E(H). Two-coordinate character orthogonality supplies exactly N²; division by m⁴ gives the displayed normalized expression under counting measure.

## originality

PASS

Pass is for the complete valuation-stratified ordered representation census at the frozen publication date, not for the aggregate fourth moment or the root-counting machinery. The total fourth moment is mechanically recoverable from an earlier one-coefficient moment theorem by a conductor decomposition. Two distinct later catalogue records give exact coverage of the census, one directly and one after sum/difference conversion; this is evidence of overlap, not a claim about first discovery or dependence.

## value

PASS

The full representation spectrum records how collision multiplicities change between unit sums, each nonunit valuation and the zero sum. It contains information lost by summing squared counts, including the singular zero-discriminant fiber and the absence of ordinary unit-square fibers at p=3. This gives exact benchmarks for additive questions on a standard modular curve. The value is the census, not re-evaluating a covered aggregate or asserting a general restriction norm.

The dated certificate retains the supplied scientific assessment, sources and limitations.
