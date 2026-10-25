# Scientific review

## Correctness (C): PASS

The four-tuple alphabet is partitioned exactly into GC-probability bins with multiplicities \(b_i=(i+1)(k-i+1)\), and the pair success probability has an explicit rational formula. Counting legal paths gives the transfer matrix and its Perron growth rate. For tolerance less than \(1/2\), every legal pair has opposite GC sides and both failure probabilities lie within the extreme tails. This yields the upper spectral estimate. A complete bipartite tail subgraph yields the matching-order lower bound; the constants \(1/24\) and \(2\) are checked algebraically. For the first threshold the four-bin graph and its path eigenvalue are computed explicitly; the \(k=2\) exception is excluded. The verifier checks finite instances by direct composite-symbol enumeration and tests the closed-form onset eigenvalues. Finite verification is not substituted for the all-resolution proof.

## Originality (O): PASS, subject to residual risk

The 2026 Bodur–Walter–Wachter-Zeh paper establishes the probabilistic composite-DNA local constraint model and fixed-parameter transfer-matrix capacity method, which is expressly **prior** and not claimed here. Its inspected local-capacity argument and examples do not state uniform growing-resolution estimates, the \(\varepsilon\asymp1/k\) threshold law, the continuous scaling exponent, or the exact first onset formula. The 2025 Nguyen–Wang–Cai–Zhang–Yakhini paper imposes deterministic satisfaction by all synthesis realizations rather than a probability threshold for each two-position window. Checked indexed mathematical records on DNA window profiles, code recovery depth, and sliding-frameproof capacity have incompatible objects and do not imply the quantitative claim. An unindexed equivalent parameter-scaling derivation remains possible. Literature comparisons address the mathematical implications, not only titles.

## Value (V): PASS

The model's resolution controls its available composite alphabet of cardinality \(\binom{k+3}{3}\), while the biochemical tolerance controls whether higher-GC mixtures can occur in locally balanced data. The theorem identifies the previously unspecified uniform tradeoff between these two design parameters, including sharp limiting information-exponent transitions and an exact first mixed-symbol capacity jump. This is a natural structural boundary across all synthesis resolutions, rather than a computation at isolated parameter values. It does not claim a full protocol or a solution for longer windows.

## Closest literature and limitations

Bodur, Walter, and Wachter-Zeh, *Probabilistic GC-Constraints for Composite DNA*, arXiv:2610.09998v1, is the nearest prior framework and already covers general spectral counting. Nguyen et al., *Constrained Coding for Composite DNA*, arXiv:2501.10645v1, treats different deterministic constraints. The quantitative results are restricted to adjacent pairs, strict exact balancing and \(0\leq\varepsilon<1/2\); no independence from other future mathematical derivations is established.

Self-review: passed. Independent audit: not yet performed.
