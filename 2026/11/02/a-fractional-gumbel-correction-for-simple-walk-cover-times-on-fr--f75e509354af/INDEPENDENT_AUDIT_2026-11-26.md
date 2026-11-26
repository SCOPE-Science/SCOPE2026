# Independent mathematical audit

## correctness

PASS

The frozen CDF and mean are both mathematically supported. Each excursion selects a uniform petal and a fair initial leaf; a specified leaf is visited with probability 3/(4n). Marking one or both leaves per petal gives (3) by inclusion–exclusion (a zeroth power is 1 at m=0). The mean excursion count is finite by a leaf union bound; Wald and the expected residual two steps from the last leaf give (4). Poisson splitting gives the product CDF. In the mean integral, on u≤n/3 the paired-term change is bounded by n^(−1/3)u^(4/3)e^(−u/2), and the independent-binomial difference by O(u² e^(−2u)/n); outside that range the tail is exponentially small by Φ_n≤e^(−u). Thus dominated convergence gives Γ(4/3)/2^(4/3) before the final walk-time factor. The repaired RESULT.md focuses on the discrete-step CDF. For correctness of its sharpened error, K=ceil(8n log n) controls M_n by the leaf union bound. Both exponential interarrival sums and excursion length sums, centered separately, have quadratic log-MGF near zero. A union bound through K gives deviation at most A sqrt(n) log n except with O(n^(−3)) probability for A large; this works even though excursion paths and M_n are dependent. The inequalities S_(M_n−1)<T_n≤S_(M_n) then give a two-clock CDF sandwich with compact-uniform x shift O(log n/sqrt n). The Poissonized Taylor error O(n^(−2/3)) is smaller. Thus the corrected walk-time claim includes the stated quantitative remainder without using the recorded checker as a proof; supplied scripts were inspected, not run.

## originality

PASS

For the repaired finding only: the actual discrete-time CDF correction with a compact-uniform error that is smaller than n^(−1/3) was not found or established as a direct corollary in the inspected sources. The frozen presentation is narrowed: its Poissonized law, Poissonized expansion and mean correction are covered mathematically by the paired-star record, and the exact inclusion–exclusion framework is established work. The overlap verdict does not infer earlier priority from catalogue dates.

## value

PASS

The repaired result quantifies the effect of genuinely correlated discoveries on a natural graph walk. It distinguishes, at the first nontrivial order, the actual walk from an independent coupon prediction and shows that the two random clocks cannot account for the anomalous correction. Compact-uniform smaller-order error makes that distinction quantitative; no significance is assigned to merely recomputing the covered expectation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
