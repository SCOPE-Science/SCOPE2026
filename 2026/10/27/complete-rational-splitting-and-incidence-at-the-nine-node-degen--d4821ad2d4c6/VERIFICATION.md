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

Specializing Veniani’s equation at ι with ι²=−1 gives the frozen polynomial. An independent exact census exhausted the six reduced row-echelon charts of sizes 6561,729,81,81,9,1. Substituting a general linear combination of the two rows and requiring all five binary quartic coefficients to vanish found 23,9,4,2,1,1 lines in the charts; the resulting 40 matrices match the certificate. All 820 normalized projective points were scanned for simultaneous vanishing of the polynomial and gradient. Nine passed and each restricted affine Hessian was nonsingular, giving nodes in characteristic three. Veniani's geometric totals of 40 lines and nine A₁ singularities then rule out further geometric objects; the rational census alone would not do this. Two intersecting rational lines meet at a rational point by linear algebra. The point scan on the 40 lines reproduces multiplicities 1^36, 2^153, 4^1, 6^9; the sixfold points are exactly the nodes and the fourfold point is smooth. Each pair is counted only once, so the edge counts are 153+6=159 smooth and 9·15=135 singular. The graph has degrees 12^4,14^18,16^18, and the line-node counts for 0,1,2 nodes are 4,18,18. Galois conjugation transfers the counts to −ι. The reduced finite line scheme consists of 40 points with residue field F₉, giving (1−T)^−40, without any claim about nilpotents.

## originality

PASS

This is a bounded pass on arithmetic splitting and the exact marked rational incidences of this particular singular fiber. Veniani already gives the family, exceptional parameter, geometric totals, line types and some valencies; neither those totals nor their consequences for abstract valencies are being credited as new. The nearest inspected primary and catalogue passages did not give this fiber’s full rational descent and incidence census.

## value

PASS

The parameter is the geometrically distinguished nine-node boundary of a specific studied quartic family. Exact Frobenius splitting and the distribution of line intersections at versus away from nodes give arithmetic configuration data not supplied by a total geometric line count. A future calculation on that boundary can reuse the exact line coordinates and marked incidences; the computation proves a natural finite invariant and detects the unique smooth four-line point, rather than sampling arbitrary fibers.

The dated certificate retains the supplied scientific assessment, sources and limitations.
