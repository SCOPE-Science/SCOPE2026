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

At the cube roots, the cyclic moments are H0=|a|²+|b|²+|c|², H1=b conj(a)+c conj(b)+a conj(c), K0=|b|²+4|c|², K1=2c conj(b). Nonzero K1 forces b,c nonzero for every competitor, including those initially allowed to have lower degree. After fixing c>0, the roots of 4s²−K0 s+|K1|²/4 are c² and |b|²/4. In each branch K1 fixes b, so H1 fixes a by a real-linear equation of determinant c_branch²−|b_branch|². The excluded ratios 1,2,4 account exactly for vanishing determinants or a repeated root here. The other branch has (c',b')=(|b|/2,2cb/|b|), so the changed a is homogeneous real-linear in a, and its energy gap at a=0 is 3(4c²−|b|²)/4, nonzero on the stated locus. The zero set of that nonzero polynomial in the two real coordinates of a is null for every allowed (b,c); Fubini lifts this to coefficient space, including the phase coordinate. For M=1,2, maximal Jacobian rank of the polynomial measurement map on the five-real-dimensional gauge chart is at most four and is locally constant off a proper algebraic set; its local fibers there have positive dimension. This is a pointwise obstruction to almost-everywhere recovery, not just dimension counting. For the integer ambiguity witness the moments are (89,68,52,24), giving the claimed intensity triples; the coefficient triples are not proportional.

## originality

PASS

The closest primary source poses the actual structured almost-everywhere sampling question rather than answering the quadratic case at three points. The closest different published records use more and/or materially different measurements and do not imply this fixed-design threshold. No covering result was found in the comparison below.

## value

PASS

A sharp answer in the first genuinely quadratic case of a published sampling question, with a deterministic two-branch inverse and an exact counterexample separating almost-everywhere recovery from all-signal recovery. Generic frames or ordinary dimension counting do not supply the constructive structured sufficiency.

The dated certificate retains the supplied scientific assessment, sources and limitations.
