---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-19.md",
      "INDEPENDENT_AUDIT_2026-10-19.json"
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

The primary article Proposition 3.25 and Corollary 3.26 explicitly establish the generating function for S_n^(d): (1-2z-sum_(k=1)^(d-1) C_k z^(k+1))^-1. Set b1=1/2, bj=C_(j-1)/4^j for j>=2; sum bj=3/4, bj~(4sqrt(pi)j^3/2)^-1. Normalized vertex count is total weight of ordered compositions of n with all parts <=floor(alpha*n); one-block contribution vanishes. Exactly two O(n) parts produce I(alpha)/(16pi) for each ordered choice and the remaining fixed-size parts contribute (3/4)^(m-2). At alpha<=1/2 the two-large interval collapses and n^2 scaling vanishes. Cases with >=3 large parts vanish after K->infinity. Uniform bound n^2 T_(n,m) <= C_alpha m^5 (3/4)^(m-2) justifies sum over m; geometric identity sum_m binom(m,2)p^(m-2)=(1-p)^-3=64 yields 4 I(alpha)/pi, with I=4(2alpha-1)/sqrt(alpha(1-alpha)). Independent normalized recurrence n=1800 for alpha=0.4,0.5,0.6,0.75,0.9 gives qualitative threshold and slow convergence from above for >1/2; these finite values are only corroboration.

## originality

PASS

Bossinger–Gürdoğan full accessible 2026 preprint Section 3.4, Proposition 3.25 and Corollary 3.26 supply the exact fixed-depth generating function, fully credited. The source treats fixed depth, Catalan endpoint, finite n and formal extension; its inspected section does not give the joint n->infinity linear-depth alpha limit or the 1/2 two-large-block transition constant. General fewest-big-jumps literature concerns heavy-tail sums with different random block count and does not itself supply this geometric vertex asymptotic. Resultary returned no exact diagonal pellytope theorem.

## value

PASS

The first explicit sharp phase transition for the natural linear-depth interpolation between Pell-type and Catalan polytope vertex growth, with a quantitative discontinuity of scaling and exact continuum parameter constant; motivated asymptotic invariant and independently useful classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
