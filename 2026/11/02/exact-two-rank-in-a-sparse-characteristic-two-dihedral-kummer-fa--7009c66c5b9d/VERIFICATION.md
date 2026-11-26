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

The odd-degree Kummer presentation w=xty has degree 3M (the commuting cyclic actions act faithfully on w), with ramification gcds 1,M,1. The gcds at zero and infinity use gcd(M,3)=1 and M=2 mod 3, and tame Riemann–Hurwitz gives M. Local valuations make a differential holomorphic exactly when the two fractional parts sum to more than one. Counting by the CRT for (i mod 3,i mod M) gives M pairwise distinct characters. For 2j=i mod 3M the remaining factors after extracting a square are t and t+1 to exponents 0 or 1. When i is in the basis, if j is not in it, a nonzero such digit would force the doubled fractional-parts sum to be at most one. The Cartier rules thus give precisely the asserted partial inverse-doubling permutation; its stable image is the span of complete surviving cycles, which gives the two-rank, not merely the rank of one Cartier application. The residue-one two-step condition is u in (1/6,1/3) or (2/3,5/6). For branch choices a,b, the inverse map from J_b to J_a is x -> (x+2a+1-b)/4. Composing along a word and adjoining the reflected terminal symbol gives one fixed point of the reflected contraction; its denominator divides 4^h+1, so it cannot hit a boundary with denominator three or six. This proves existence and uniqueness of each itinerary, and 4^h=-1 mod M makes those tests sufficient for the entire orbit. Doubling exchanges the two nonzero residue classes, giving 2^(h+1). Bounded independent replay: python3 /workspace/reproductions/frozen_checks.py rank constructs and checks the base-four digit witnesses for h=1..10. It is not a proof of the rank theorem or a reproduction of the frozen finite-field zeta computation. Frozen verification code and notes were inspected, not executed.

## originality

PASS

Credit the known family, genus and group, quotient and upper bound, and the general three-point-cover slope method. The distinct finding is the uniform exact 2-rank evaluation for M=4^h+1. Applying general slope formulas to a fixed M could compute a particular case, but the dependence on h does not follow without a nontrivial all-h orbit count. The reflected binary itinerary is such a count.

## value

PASS

The precise rank of an existing geometric family is a motivated invariant. The sparse sequence realizes unbounded positive rank with rank/genus tending to zero, invisible to the prior upper bound. The reflection and itinerary argument is a substantive exact evaluation rather than finite tabulation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
