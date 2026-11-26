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

Conditional binomial counting has thresholds k-r when the expert is right and k+1 when wrong, and beta integration gives the displayed tail. For the marginal from r to r+1, in the gain case the removed voter is wrong and the other novices have k-r-1 successes, while in the loss case the removed voter is right and the others have k successes. The binomial coefficients agree by complementation. Integration yields the two beta functions, and their ratio is the shifted gamma product from j=k-r-1 through k. Adding a factor (a+j)/(b+j)>1 at each step makes the bracket strictly decreasing, so at most two adjacent maximizers occur on [0,k]; r>=k is exactly the dictator plateau. If r/k tends to t<1, the log product is (a-b)log(1/(1-t))+o(1), by expansion at O(1/k) and summing reciprocal indices. At ratios just below and above rho the limiting brackets have opposite strict signs, so monotonicity traps every maximizer; eventually r<k and the plateau cannot be optimal. This gives rho/2 of the whole electorate and conditional pairwise correlation Var(Theta)/[E(Theta)(1-E(Theta))]=1/(a+b+1). The (3,2) product telescopes to (k+3)/(k-r+1), sign 4k-7r-2. For k>=2 its zero lies strictly before the last increment, so the ceiling optimizer, ties at k=4 mod 7 and absence of a dictator optimum follow. At k=1 the unique relevant increment in each model is positive. For fixed p=3/5 the marginal bracket q-(1-q)(3/2)^(r+2) is positive for r=0 and negative for r>=1. A separate finite exact-rational replay performed 136 tail-difference and example maximizing-set checks, the latter through k=29; these checks do not prove the universal limit. The frozen script was not executed.

## originality

PASS

The finite beta-integrated marginal product and proportional restricted optimizer are distinct from established expert-vote weighting, beta-binomial vote counts and common-signal models. The strongest indexed result shares the one-expert architecture and conditional pivotal formula, but its unimodality and bounded optimizer require all conditional novice accuracies above one half. A beta mixture with positive density below one half is not a specialization of that theorem. The independent-vote benchmark and small correlated-vote precedents are credited explicitly.

## value

PASS

Keeping positive marginal competence and expert precision fixed while changing the dependence model turns a bounded optimal delegation count into a genuinely macroscopic one. The exact pivotal product explains the switch and gives a useful finite selection rule, not merely a limiting heuristic or a restatement that correlation can matter. The explicitly calibrated rational comparison holds the marginal precisions fixed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
