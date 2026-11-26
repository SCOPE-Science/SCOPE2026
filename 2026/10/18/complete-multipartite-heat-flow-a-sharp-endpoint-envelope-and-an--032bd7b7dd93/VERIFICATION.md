---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Frozen RESULT.md line 21 is false where it says intermediate sizes may be skipped. The replacement RESULT.md proves the opposite. The projector calculation gives a positive diagonal, nonpositive other entries and zero row sum, so the symmetric kernel has both endpoint norms equal to twice the maximum diagonal. Maximizing the two weighted exponentials separately gives the sharp bound; different rates make it strict for every nonsingleton row, and finiteness and endpoint decay make it strict for the supremum if no singleton exists. The logarithmic time derivatives of the rescaled rows h_m are in [m−1,m) and zero for m=1, giving the unique directional crossings. For fixed t>0, write h_m=(n−m)e^(mt)(1−g_t(m)), where g_t(m)=∫₀ᵗe^(−mu)du lies in (0,1) and g_t″>0 for real 1≤m<n. This makes log h_m strictly concave in size; at the outer crossing for a<b<c the middle row beats both, so t_ab<t_ac<t_bc. Consequently all adjacent crossings are global, exactly two adjacent sizes tie at each, and every size is uniquely active on an open interval. The last active row recovers n from the larger exponential rate, or the sole rate for an all-singleton graph; distinct positive rates are uniquely extracted from the exact tail. At fixed n, analytic agreement on any single-size interval forces equal zero-time limits 2(n−m), identifying each size. The two graphs have equal n and size sets but unequal multiplicity of eigenvalue 18. The original numerical checker was inspected and not executed, and its pairwise tests cannot adjudicate the frozen skip assertion; the replacement proof establishes the conclusions without it.

## originality

PASS

For the repaired theorem, the established heat-equation and blow-up spectrum results supply the framework and spectral ingredients. The inspected related claims do not prove the exact ordinary endpoint derivative norm with sharp singleton equality, the complete no-skip transition pattern, or the resulting inverse equivalence. No priority certification is inferred from this bounded comparison.

## value

PASS

This is a sharp time-resolved norm for a natural graph family, with an exact universal-vertex equality criterion. Showing that every size occurs as the worst row class answers a concrete structural question left by pairwise monotonicity. The recovery theorem exactly identifies what the endpoint profile can determine and what spectral information it can lose, rather than merely reproducing a numerical norm at a chosen time.

The dated certificate retains the supplied scientific assessment, sources and limitations.
