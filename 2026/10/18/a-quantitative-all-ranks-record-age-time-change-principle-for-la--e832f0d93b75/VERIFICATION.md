---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

For each strict active record index r, its first physical success time T_r is the unique corresponding strict lazy record time. At T_r, A_{T_r}=r and |A_t-qt|≤D, so each completed active gap and its physical gap obey |qL−ℓ|≤2D; the same applies to the final censored pair with t=n. Re-normalizing physical lengths by n and active lengths by m contributes at most D/(qn) to the 2D/(qn) discrepancy. Sorting matched nonnegative lengths is nonexpansive in sup norm. When the active horizon changes from m to h, all old completed intervals persist; the first new completed interval extends the old censored interval by at most |m−h|, and further new intervals have length at most |m−h|. Sorting and normalization give ||Q_m−Q_h||∞≤2|m−h|/h. Since |m−h|≤D+1, the claimed pathwise bound follows, including m=1 and zero-length censored intervals. For Bernoulli clock increments, the maximal two-sided Hoeffding–Ville inequality P(D>x)≤2 exp(−2x²/n) integrates to E D≤√(πn/2). On m=0 use the trivial distance bound 1 with probability (1−q)^n; all parameters and expectation constants check. Szabó–Vető Theorem 4 exactly covers censored ages of the active symmetric continuous walk, so coordinatewise PD convergence follows by vanishing coupled discrepancy. The independent exact-rational checker passes 118014 finite checks; those do not prove the all-n claim, whose proof is deterministic plus a standard concentration theorem.

## originality

PASS

The novel candidate is the explicit, pathwise, simultaneous all-ranks inequality for the censored renewal composition after independent Bernoulli pauses, with a deterministic effective-horizon finite-sample O_q(n^{-1/2}) Wasserstein comparison. The non-lazy PD(1/2,0) theorem itself is Szabó–Vető (2016), not original. Majumdar–Mounaix–Schehr (2021) directly studies the lazy random-walk record model and explicitly poses record ages as further work; its count/correlation formulas do not entail this pathwise estimate. Régnier–Dolgushev–Bénichou (2024) treats general multitime record-count/epoch renewal transforms, not this coupled ranked-age metric in inspected sections. Published record-related database hits concerned different statistics. Best-of-knowledge originality survives, with the possibility of an unindexed general time-change coupling under a different name.

## value

PASS

Record ages under nonzero staying probability were explicitly left for future study in the 2021 lazy-walk paper. Simultaneous normalized ranked ages are a natural infinite-dimensional observable of the renewal record process, and a deterministic finite-horizon comparison is useful when transferring non-lazy record-age laws and evaluating finite lazy-record samples. The estimate cleanly separates a quantitative clock perturbation from the already-known non-lazy PD limit, and it holds for arbitrary active paths, not only the random-walk corollary. Although the bounding lemmas are elementary and not claimed optimal, their precise coupled full-ranking conclusion addresses a motivated gap rather than a merely renamed computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
