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

The prime-power formula gives the stated exponent transition, preserving the support; on nonunits L₂(n)<n and the iterates stay odd so the terminal value is 1. For b>0, the second exponent stays at b for c steps, then drains in b steps, while the first exponent after these steps is max(a,1). For b=0<c, the first transition produces second exponent 1 and first exponent (a−1)₊; the second coordinate is positive at times 1 through c and then vanishes. The remaining first exponent is max(a−1,1), giving c+max(a,2) total steps. For b=c=0 there are exactly a steps. At a fixed k≥2, in the region a,b≥1 the ratio to 15·7^(k−2) is (3/7)^(a−1)(5/7)^(b−1); for a=0,b≥1 it is (5/7)^(b−1)/3. In the b=0 regions the ratio is at most 3/5, including pure powers of 3. Only (a,b,c)=(1,1,k−2) attains one. The five counting terms for k≥3 are 1, 2(k−1), (k−1)(k−2)/2, 3, k−3; the first two levels respectively contain {3} and {5,9,15}. Summation and coefficient extraction give the advertised generating function. Since the logarithm has base 7>1, the level extremum is equivalent to the claimed lower bound and its equality family. The unit is outside the frozen domain; 3 is a genuine failure of the numeric inequality. The frozen verify.py is a replay path using prime-factor iterations on [0,9]^3 and complete fibers up to 16 in [0,17]^3 (every exponent is bounded by its height). It was inspected, not run; these computations are finite corroboration only.

## originality

PASS

Credit the prior stopping-time formula and maxima on the trajectory-restricted domain without 7, and the earlier exact all-odd maxima for the first ten levels. The surviving distinct result is the uniform height classification with the 7-transition present, including an all-level restricted extremizer and exact histogram. The previous finite census and the 7-free theorem do not imply that infinite claim, and Defant stated the unrestricted inequality as a conjecture, not a theorem.

## value

PASS

This is the smallest prime support containing 7 closed under the odd-prime L₂ transitions, and it contains the conjectured extremal progression. It is not an arbitrary exponent cutoff. The formula resolves every level within that natural family, separating the transient filling of a missing lower prime from subsequent depletion. The sharp unique maximizer settles an infinite test case of the lower bound, and the histogram gives a complete exact benchmark for work on inverse stopping-time strata. The usefulness is in the all-level structure with 7, not in tabulating the earlier initial levels again.

The dated certificate retains the supplied scientific assessment, sources and limitations.
