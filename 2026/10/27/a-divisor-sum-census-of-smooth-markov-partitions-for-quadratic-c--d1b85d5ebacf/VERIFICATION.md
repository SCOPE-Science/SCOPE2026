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

For the reciprocal polynomial, the disk inequalities are |1/d|<1 and 1+1/d>|t/d| (for real roots the latter gives positivity of both products at ±1, excluding roots beyond those endpoints given the product bound; for nonreal conjugates the product bound suffices). Summing 2d+1 at positive d and 2|d|−3 at negative d verifies E(H). HDJ Theorem 1.2 supplies the diagonalizable integral-power test. A double root gives a nontrivial Jordan block, with nonzero nilpotent term in every positive power on the expanding locus. For irreducible roots equal integral powers imply a root-of-unity ratio; the trace squared divided by d minus 2 is that ratio plus its inverse, a rational algebraic integer in [−2,2]. The real case has t=0 and the nonreal possibilities and converse powers in the record are exact. For the count of integer roots, |a+b|≤|ab| for |a|,|b|≥2, so there is no additional trace cap; taking absolute magnitudes yields D(H)−2H+1 ordered pairs, then sign choice, removal of 2(floor(sqrt(H))−1) equal pairs and division by two give the claimed integer-root class. The t=0 overlap is precisely d=−a² with |a|≥2; its subtraction and the diagonal subtraction cancel the separate t²=d contribution. The nonreal t²=2d and 3d families have t=±2j and ±3j respectively and determinants 2j² and 3j², with the trace cap automatic. This proves both exact formulas for all H≥2, and inserting the hyperbola estimate and dividing by 2H²−2 gives the stated errors including O(H^(−3/2)) for the proportion. The finite H=2..65 diagnostic and its code were inspected, not rerun; the analytic proof is independent of that diagnostic.

## originality

PASS

The claimed novelty is an exact census in a specified trace–determinant height box and the derived density, not the geometry or integral-power criterion. The HDJ criterion, its finite-exponent result and representative spectral types, and the divisor-summatory asymptotic are prior inputs. Neither the identified HDJ results nor the other checked evidence supply the exact box enumeration or its leading and secondary terms. Priority is bounded by the comparisons below.

## value

PASS

The simultaneous trace–determinant bound is a natural conjugacy-invariant height on this companion family. Counting at that height quantifies how exceptional the geometrically regular partitions are: the shrinking proportion and exact small-height corrections are useful and do not follow merely from knowing a finite test for each matrix. No claim about typicality among all integral matrices or other dimensions is warranted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
