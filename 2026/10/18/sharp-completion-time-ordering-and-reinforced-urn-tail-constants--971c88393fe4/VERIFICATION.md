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

For finite-population balancing, couple via the sampled indices and condition on inclusion of the recolored ball and on the other categories. When the pair supplies t≥2r draws, recoloring shifts the allowed hypergeometric interval by one. The gained endpoint t−r and lost endpoint r−1 have nonnegative mass difference since the larger unmarked population is A−1≥B and C(x,v)/C(x,u) grows in x for v>u (if a relevant lower binomial factor vanishes, checking the support endpoints gives the same sign). For t<2r there is no pair success. Smoothing the finite population thus maximizes success at the balanced counts. Mixing iid-colored populations of size qa recovers k iid draws at distinct indices; the homogeneous population has zero success and positive mixture mass, so the comparison is strict for qr≤k≤qa. Above qa completion without replacement is certain while iid completion is not. For iid pair balancing, differentiating the truncated binomial sum telescopes to the two boundary masses and gives the displayed sign change about u=1/2. For an interior unequal vector, the conditioning event with all other quotas met and at least 2r pair draws has positive mass at every k≥qr; boundary vectors cannot succeed. Thus the uniform vector is the unique maximizer, and a symmetric Dirichlet draw is almost surely interior and nonuniform. All three probabilities vanish before qr. For the fixed-j beta-binomial mass the factorial and gamma ratios leave exponent −a and the stated coefficient; doing the same for two fixed counts under aggregation gives exponent −2a for q≥3, and for q=2 both deficient is impossible once k>2r−2. The first two Bonferroni bounds therefore preserve the leading q-fold coefficient. For q=3,a=2 the one-colour masses at j=0 and j=1 are 20/[(k+4)(k+5)] and 40k/[(k+3)(k+4)(k+5)], independently giving C=180 at r=2. Discrete tail summation with increments (k+1)^s−k^s gives the moment criterion including divergence at s=a. Replay: RESULT.md lines 25–80 and the above single-colour specialization. The supplied verify.py was inspected, not executed, and its finite comparisons are not a certificate of the universal ordering or the limit. There is no pathwise coupling claim, growing-parameter tail uniformity, or ordering for arbitrary unbalanced urns.

## originality

PASS

The three multicolor stopping laws, the repeated-copy iid marginal, one-appearance iid balancing, first-hit Pólya marginal tails, and the full simultaneous Pólya tail and moment criterion at r=1 have identifiable coverage. In particular the linked Resultary 5623e019d5e4 gives the exact r=1 coefficient even for unequal masses; this is not merely an exponent match. The distinct content is the strict all-horizon comparison across the three mechanisms and the sharp simultaneous coefficient for repeated quotas r>1, with pair-deficiency control. The checked comparators do not state or mechanically give that package. This pass credits only the distinction beyond the covered cases, not priority for the completion laws or first-appearance tails.

## value

PASS

The balanced quota target gives a common nontrivial experiment with finite stock, independent repeats and persistent reinforcement. The ordering distinguishes all three at every feasible finite horizon; the tail coefficient identifies which rare events govern repeated-copy completion, yielding quantitative tails and an exact integrability boundary for the reinforced law. These conclusions extend beyond the already available one-hit or single-colour formulas.

The dated certificate retains the supplied scientific assessment, sources and limitations.
