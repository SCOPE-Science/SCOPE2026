---
{
  "schema_version": 1,
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "status": "unknown",
    "evidence": null
  },
  "expert_attestation": {
    "status": "unknown",
    "evidence": null
  }
}
---

# Independent mathematical audit

## correctness

PASS

The two removed regions are disjoint 4-simplices of volume s^4/24. The polar is the hull of the cross-polytope and the tips ±(1,1,1,1)/(4−s); for s>0 each tip sees only its corresponding facet, giving two disjoint pyramids of volume s/[24(4−s)] each, with the formula also valid at s=0. The product gives D(s)=s/3+O(s²) and the recorded lower bound 2631s/8064; exact rational arithmetic confirms the three C=2 violations. For arbitrary fixed C>0 this lower bound beats the cubic as s tends to zero; C≤0 is immediate. The cube inclusions give 0≤δ≤−log(1−s/4)≤9s/32<D. Further, any Banach–Mazur sandwich B⊂TK_s⊂λB implies P(K_s)≤λ^4 P(B) by primal/polar inclusions and affine invariance. For x=D/P(B), δ≥x/[4(1+x)], and 0<x≤s/28≤1/56. Combining this with the lower bound on D gives δ≥(877/116736)s>s/140 throughout the interval, in particular at the checked nodes. Thus the quotient D/δ² is defined for s>0 and diverges. The side fallback is indeed false: the functional polar of exp(−|x|) is the indicator of [−1,1], so J=4 and variance 2 give a right side of 9/2. Inspected RESULT.md and artifacts/verify_target.py and verify_fallback_counterexample.py; independent simplex geometry and exact Fraction node evaluations, not reliance on archived statuses.

## originality

PASS

Credit the exact path-specific product, derivative and consequent obstruction reversal, not discovery of linear-scale local minimality of the cube. The exact September index match is this same record. Two later general profiles cover the formula retrospectively; the October generalization expressly credits the September special case. The distinct same-day unconditional deformation is of a different body and does not imply this result. NPRZ gives a general linear lower bound in a normalized inclusion defect, not the exact path coefficient or product. The broad contextual assertion about unknown sharp rates should not be read as denying the known NPRZ linear bound.

## value

PASS

This natural primal truncation/polar stacking path was proposed as a concrete flat-rate obstruction. The exact product and nonzero coefficient resolve that proposed test in the opposite direction: the polar volume increases to first order while the primal loss is fourth order, decisively excluding every fixed cubic envelope. The claim is about this path, not the already-known general linear lower estimate or a general stability theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
