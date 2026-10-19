# Self-review

## Correctness — PASS

The dimensionless process, Poisson flip rates, wall waiting law, admissible boundary \(a+g>0\), and symmetric initial orientation are fixed explicitly. Direct backward-generator equations for \(n=1,2\) and their two wall boundary conditions produce the exact mean and variance. Differentiating the rational variance yields the quartic \(P_g\); Descartes' one-sign-change argument supplies global uniqueness and sign, including the degenerate boundary \(g=g_{\rm var}\). Substitution of the previously published mean optimizer into the exact variance derivative proves strict separation. An independent transfer-matrix Laplace differentiation checks the first two moments. The finite checks supplement, not replace, the proof. Large-\(a\) divergence and \(a=0,g>0\) endpoint are addressed.

## Originality — PASS, with explicit priority risk

Angelani (2023, DOI 10.1088/1751-8121/ad009e, full text, equation 45) already provides the entire first-passage transform for general wall rates: **all moments are implicitly computable**, so neither this model nor a second-moment algorithm is original. Angelani (2024, arXiv:2311.11873, section 2, equations 7–11) expressly gives the mean-minimizing critical wall enhancement \((\sqrt7-1)/3\). Neither inspected source states a variance-optimization threshold, a unique global variance-minimizing tumbling rate, or the strict ordering of the two optima. The nontrivial exact extra classification requires deriving the quartic, proving its positive-root phase boundary for a continuum of enhancements, and comparing the two optimum curves. Jeon et al. (arXiv:2310.04016) study variance of search with a different partially absorbing internal target and a speed rather than enhanced-wall tumbling optimum. General first-passage transforms pose *residual implicit-priority risk*; this is not a claim of proven global novelty and needs independent examination.

## Scientific value — PASS

The same physical device can favor different settings according to whether average clearance time or its variability is optimized. The strict interval \(g_{\rm mean}\le g<g_{\rm var}\) demonstrates that eliminating bulk tumbles is optimal for the mean yet suboptimal for reliability measured by exit-time variance. This is a qualitative regime conflict in a published active-escape model, not a small coefficient improvement or an arbitrary parameter sample. Closed global thresholds and optimizer ordering help distinguish mean-time versus fluctuation-sensitive operating criteria. The theorem does not control entire tail distributions or general geometries.

## Closest literature and limits

L. Angelani, *One-dimensional run-and-tumble motions with generic boundary conditions*, J. Phys. A **56** (2023), 455003, DOI 10.1088/1751-8121/ad009e; L. Angelani, *Optimal escapes in active matter*, Eur. Phys. J. E **47** (2024), 9, arXiv:2311.11873; E. Jeon, B. G. Go, Y. W. Kim, *Searching for a partially absorbing target by a run-and-tumble particle in a confined space*, Phys. Rev. E **109** (2024), 014103, arXiv:2310.04016. The exact whole-transform coverage is acknowledged. General extensions and independent priority review have not been established.

Self-review: passed. Independent audit: not yet performed.
