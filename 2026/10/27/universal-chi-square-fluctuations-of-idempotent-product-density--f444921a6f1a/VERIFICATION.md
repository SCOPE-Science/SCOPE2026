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

For the canonical idempotents (i,p_{λi}^{-1},λ), the product is idempotent exactly when p_{λi}p_{μi}^{-1}=p_{λj}p_{μj}^{-1}; the order of factors is unchanged in deriving this condition. Equal rows always succeed and reversing the row order inverts both ratios. Thus the ordered count is rn²+2Σ_{λ<μ,g}N_{λμ}(g)². Completing the square and dividing by (rn)² proves the exact scaled identity and the equality condition. For one pair let C count collisions of unordered columns. Its indicators have success probability 1/h and are pairwise independent even when they share a column (condition on its ratio); Q=h−n+2hC/n then has mean h−1 and variance 2(h−1)(n−1)/n. Distinct row pairs have pairwise independent entire ratio sequences, by conditioning within each column on the common row entry if necessary. They need not be jointly independent: at n=2, agreement of ratios for pairs (1,2) and (2,3) forces agreement for (1,3). The Gaussian limits are independent because the bounded iid column vectors have block-diagonal covariance; after scaling each occupancy by √(h/n), its block is the projection onto the (h−1)-dimensional zero-sum space. Taking squared norms yields the claimed d=(h−1)binom(r,2) and prefactor 2/(r²h). The exact moments give a summable O(n^-2) second moment around θ, so first Borel–Cantelli yields the any-coupling assertion without across-size independence. At n=1 it correctly gives T=1 and zero variance. The scope is fixed r and finite G, labeled independent uniform nonzero entries, not random isomorphism classes or sparse matrices. Frozen verify.py and VERIFICATION.md document finite exhaustive count/moment cases including S3; inspected, not executed here, and not used as proof of the limit.

## originality

PASS

The distinctive contribution is the Rees-semigroup reduction of an intrinsic ordered-product statistic to all row-pair occupancies, including the cross-pair orthogonality that gives universal finite moments and a single scaled chi-square law for every finite group of the same order. The general probability tools (Pearson, the multivariate CLT, or the degenerate U-statistic limit) and the Rees representation are not new. The strongest inspected same-event statements concern other algebraic objects; the strongest same-Rees statements concern generation, commutation, or a particular deterministic sandwich rather than the iid universal law. The comparison is bounded, not a claim of first discovery.

## value

PASS

An invariant proportion of successful products is a quantitative alternative to the all-or-nothing condition that idempotents form a subsemigroup. The deterministic identity characterizes the configurations minimizing the proportion when balanced row-pair occupancies are possible. The finite bias and variance are both resolved, and the χ² limit shows that ordinary first-order Gaussian scaling would miss the fluctuations. Group-order universality, despite dependencies among three or more row pairs, is a structural conclusion of the product count rather than an arbitrary numerical slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
