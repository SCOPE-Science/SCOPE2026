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

Finite-field Brauer vanishing gives Pic(S)=L^w. Every actual line-orbit sum is an arithmetic effective divisor, and averaging a geometric nonnegative line decomposition gives every invariant effective class as a nonnegative combination of such sums. The pairing is nondegenerate on the invariant subspace, and its polar yields the arithmetic nef cone. For independent reproduction, /workspace/branches/independent-5.py run with the frozen RESULT.md path matched all 18 rows and the displayed 16-index certificate; output is in /workspace/branches/independent-5.log. The check labels the conic class by the empty even mask, H−E_i−E_j by {i,j}, and E_i by the complement of {i}. Exceptional swaps permute bits and the Cremona reflection on the first three points is the last-two swap followed by XOR on those two bits, so this is the same order-1920 Weyl action. Signed cycles classify the classes: conjugating in the full signed group normalizes signs on each cycle, and an odd cycle supplies an odd-sign centralizer element, preventing class splitting in the even subgroup. The primitive fixed kernel means ambient orbit-column Smith factors are the same trace quotient factors, after checking equal ranks. The signed discriminant comes from the Gram determinant of an independent trace sublattice divided by the square of its saturation index. The cone computation independently cuts a simplicial polar by the remaining exact inequalities, adding rays at crossings of adjacent rays and counting its facets by active-ray rank. This checked all listed ray counts, including the split 16/26 case. The certificate basis is saturated and the actual four orbit sums give Smith factors (1,4,4). This is conditional on each surface's actual Frobenius class, not a realization claim over each field.

## originality

PASS

The 18-class structure, the index-only table including the unique index-16 class, and real cone generation by orbit sums have demonstrable overlap. The supported distinct result is the full integral quotient and Picard-discriminant data together with exact effective and nef extremal-ray counts, including the (Z/4)² group structure rather than its order alone. No examined match gives that classification.

## value

PASS

The trace quotient measures precisely which arithmetic lattice classes are missed integrally by line orbit sums even though those sums span over the reals; its invariant factors distinguish missing generators from a mere index. The discriminants and the arithmetic effective/nef ray counts complement this with exact pairing and cone data. The rank-four cases show why rank or the number of effective rays alone does not give the dual count. The finite range is the full Weyl class space for the degree, not an arbitrary cutoff.

The dated certificate retains the supplied scientific assessment, sources and limitations.
