---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

All vertices of I_{n,k} are 0–1 vectors with at most k ones; the Gaussian support selects at most k largest positive coordinates, so the lost cube width is exactly the sum of the (B−k)_+ smallest positives plus the (n−B−k)_+ smallest absolute negatives, divided by ||G||. Width equality requires n−k≤B≤k (Gaussian sign count), giving the exact finite binomial identity even when the range is empty. For each sign group b~n/2, transform half-normal order statistics using uniforms and exponential spacings; maximal-inequality and F^−1(u)=u/a+O(u²) show Σ_{j≤m}X_(j)=m²/(2ba)+o_P(1) uniformly for m≤Ksqrt(n). Binomial CLT for B and Gaussian radius normalization give Q_c(Z). The ordinary cube width expands by the delta method to Y of variance 1−3/π, and signs are exactly independent of absolute magnitudes, yielding asymptotic independence. At c=0, Q=χ_1²/(4a); c>0 atom mass 2Φ(2c)−1, c≤0 none. Independently enumerated 525 small-n vertex-support tests (n=2..8) confirm the finite identity; no finite test purports to prove CLT.

## originality

PASS

Best-of-knowledge, not absolute priority: For uniform-matroid independence polytope I_{n,k}=[0,1]^n∩{Σx_i≤k} with (k−n/2)/sqrt(n)→c, the Gaussian cube-width fluctuation and finer sqrt(n)-scaled cap deficit jointly converge to independent Y~N(0,1−3/π) and Q_c(Z)=[(Z/2−c)_+²+(−Z/2−c)_+²]/sqrt(2/π); the exact width-equality probability is a binomial tail, with chi-square balanced limit and an atom for c>0. The inspected primary sources contribute prerequisite constructions or related weaker/different statements, without identifying a prior theorem that logically entails the distinctive final statement. Inaccessible/unindexed historical overlap remains an explicit risk.

## value

PASS

The capped cube/uniform-matroid independence polytope is a canonical rank-constrained polytope. The geometric question when a central cap changes a random projection is naturally quantified by width equality and defect. The exact sign-tail law and joint Gaussian/chi-square two-scale phase transition at half rank go beyond a known cube-width marginal, without claiming general matroids or all rank regimes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
