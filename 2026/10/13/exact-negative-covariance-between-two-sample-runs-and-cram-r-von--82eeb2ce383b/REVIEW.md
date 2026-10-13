# Review

## Correctness
PASS. The pooled-label reduction is exact under the continuous common-distribution null. The identity \(T=(mnN^2)^{-1}\sum_{j=1}^{N-1}B_j^2\) follows directly from the pooled empirical-distribution jumps. Hypergeometric second moments give \(\mathbb ES=mnN(N+1)/6\). Conditioning one edge to be a change leaves a uniform residual word with \(m-1\) and \(n-1\) labels; the resulting conditional means and variances sum to the stated aggregate identity, which yields \(\operatorname{Cov}(R,T)=-(2mn-N)/(3N^2)\). The exceptional small totals \(N=2,3\) are handled directly. Exact-rational replay checks the finite formulas on thousands of words but is not used as an infinite proof.

## Originality
PASS. The closest inspected runs source gives the marginal null law, mean and variance of the same one-dimensional run statistic, while the Cramér–von Mises source treats the global two-sample discrepancy separately. Targeted statement, alias, bridge-energy and implication searches did not locate the mixed covariance or a stronger theorem that yields it. Existing exact results connecting runs to a centered Mann–Whitney square and connecting that square to Cramér–von Mises do not imply the missing runs–Cramér–von Mises covariance. Residual risk remains that older rank-test or empirical-process literature contains the same mixed moment under another normalization.

## Value
PASS. Runs and Cramér–von Mises are canonical but structurally different two-sample diagnostics: one is local in adjacent pooled labels and the other is a global quadratic empirical-bridge energy. The theorem gives a simple exact finite-sample coupling, proves its sign for every nontrivial size configuration, and identifies a nonzero proportional-sample covariance limit. This is a motivated structural relation rather than a renaming or arbitrary parameter slice.

## Closest literature and limitations
The inspected runs paper is M. Biswas, M. Mukhopadhyay and A. K. Ghosh, DOI 10.1093/biomet/asu045. The inspected Cramér–von Mises context is W.-X. Zhou, C. Zheng and Z. Zhang, arXiv:1509.03459. P. Marsh, DOI 10.1080/10485250903486078, supplies an explicit primary 62G10 classification for the two-sample nonparametric-testing setting. The theorem assumes a continuous common null and the displayed Cramér–von Mises normalization.

Self-review: passed. Independent audit: not yet performed.
