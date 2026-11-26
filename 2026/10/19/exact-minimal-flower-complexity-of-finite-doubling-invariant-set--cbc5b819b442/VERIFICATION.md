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

For finite nonempty E-invariant K, E restricts to a permutation, so each ordered output has exactly one required inverse. A selector with j jumps has j petals: the closed lifts of its continuity intervals are disjoint, since the only possible shared outputs under E would be interval endpoints, and the two lifts at any jump differ. A jump-free selector is impossible by degree. If K is contained only in the closure, each required inverse at a prescribed point is still a lateral limit; moving a jump at that point slightly onto the side carrying the other sheet preserves the number of jumps and includes the required inverse in the interior. In each ordinary gap the two bits force one jump iff they differ, and in the wraparound gap the covering interchanges sheets, so it forces one iff the bits agree. Independent lifts on the gaps attain these lower bounds, including when 0 is prescribed and for the singleton. Their sum is odd. On the grid of denominator D=2^n−1, if the inverse has numerator a and the output numerator j, then 2a=j+bD, so b is the parity of j and the wrap term contributes one. On a primitive nonconstant cycle the predecessor bits are the last column of the sorted rotations. The least rotation has a preceding 1 (otherwise shifting backward lengthens its initial zero run), and the greatest has a preceding 0, so the seam adds zero and the cost is the linear run count minus one. The finite supplied verifier was inspected, not executed; its discrete minimization and rational instances do not substitute for the proof.

## originality

PASS

The supported distinct claim is the finite-set optimum with both the exact fixed-point-grid extremum and the equality to the BWT run count on a primitive cycle. Neither the established jump/component relation nor the established BWT run classifications are credited as new.

## value

PASS

For the natural covering problem on finite invariant unions, the result replaces a search over continuous jump locations by a sharp, constructive count from predecessor order. It supplies an exact exponentially growing obstruction for full fixed-point sets and lets a researcher obtain the sharp geometric cost of one cycle from an ordinary BWT run count. It makes no claim about arbitrary infinite supports, higher degrees, or the full invariant set inside an optimizing flower.

The dated certificate retains the supplied scientific assessment, sources and limitations.
