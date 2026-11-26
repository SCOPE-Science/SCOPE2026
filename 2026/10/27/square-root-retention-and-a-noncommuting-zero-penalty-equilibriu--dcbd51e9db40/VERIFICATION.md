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

With t=1−ε and retentions (a,b,c), the first circuit from origin 1 gives utility ta+2t²(1−a)b and returns with weight t³(1−a)(1−b)(1−c). Geometric summation therefore gives the asserted utility everywhere except the void origin at ε=0, which is treated separately. Quotient differentiation cancels the acting retention from the derivative's sign; at zero penalty it is c(1−b)−b. The zero profile has a profitable full-retention deviation. With only a positive, player 2 can increase retention; with a,b positive but c=0, player 1 can decrease a strictly locally without crossing the singular origin. All such supports are cyclic relabelings. With all three positive, the three necessary derivative signs give b<c<a<b. At a symmetric positive-penalty candidate, the sign polynomial F_t(q)=1−t³(1−q)²−2tq has F_t′<0, F_t(0)>0, and F_t(1)=1−2t. Own-action indifference at the unique interior root is sufficient for Nash; t≤1/2 selects q=1, including the indifferent boundary t=1/2. Expansion of the quadratic root gives √(3ε)+O(ε). Summing incoming mass at each symmetric node gives the real weight tq/(ε+tq), and total void weight 3ε/(ε+tq); these tend to 1 per agent and 0 void while direct zero-penalty evaluation at the limiting profile gives all three votes void. The two limits concern the weight map, not convergence to some existing unpenalized equilibrium. Independent stable evaluation of the quadratic root reproduces the sample retentions 0.0171233652176 and 0.1558277369823; replay with node /workspace/review-evidence/bounded-checks.js. Numeric diagnostics and the frozen finite grid do not establish the continuum theorem.

## originality

PASS

The geometric-penalty model, positive-penalty existence and generic zero-penalty nonexistence are known and expressly not claimed as new. The checked antecedents do not cover the simultaneous nonnegative continuous-cycle obstruction, exact symmetric retention branch with threshold 1/2, square-root rate and resulting weight discontinuity. This passes for that specific quantitative and continuous-strategy result, not for the generic claim that cycles can obstruct delegation equilibria.

## value

PASS

This example tests a substantive interpretation of positive-penalty existence: along the exact symmetric equilibria the rule recovers essentially every vote as damping disappears, while the limiting strategy profile invalidates every vote under the zero-penalty rule. The square-root rate and explicit threshold make that singular behavior quantitative, and continuous nonnegative payoffs rule out attributing it solely to binary actions or negative utilities.

The dated certificate retains the supplied scientific assessment, sources and limitations.
