# Scientific review

## Correctness

**PASS.** All quantifiers and boundary regimes are explicit: fixed integer \(m\ge4\), fixed \(\delta\in(0,1)\), and \(\beta\downarrow\delta/\Lambda\) from above within \((0,1)\). The graph construction gives exactly three connected induced blocks of cardinality \(m\). Its isolated spectra are elementary, and a Rayleigh quotient yields \((m+1)/2\le\Lambda-(m-1)\le m\). Monotone fixed-point iteration, strict radial subhomogeneity and a critical Perron-weighted union bound establish existence, uniqueness, and the normalized Perron limit. The block eigenvector identities yield the \(m^2/8\) bound. Ten numerical fixed points reproduced in `checker.py` support, but are not needed for, the infinite-family proof. The claim is about the deterministic product recurrence, not an absorbing stochastic epidemic.

## Originality

**PASS, with explicit priority risk.** Dung and Phuc (arXiv:2607.14048, read through Sections 2–4) rank local isolated thresholds and simulate aggregate community infection but do not establish any quantitative ordering theorem between those measures. Prasse and Van Mieghem (DOI:10.1007/s00285-020-01542-6, read Theorem 1 and nearby text) prove Perron-direction endemic asymptotics for continuous-time NIMFA, an antecedent method acknowledged in the result. Bonaccorsi et al. (arXiv:1412.6157, read the source's quotient-spectrum and reduced-SIS sections) give spectral tools for equitably partitioned continuous-time epidemic networks rather than the explicit non-equitable three-block product-map family. Li et al. (DOI:10.1016/j.jpdc.2018.04.009) analyze heterogeneity and SIR epidemic size; the available scientific text does not identify this endemic SIS comparison. The quantitative equal-size, quadratic reversal is not a restatement of those inspected claims. Possible unindexed constructions and transferable prior eigenspace arguments remain an acknowledged risk.

## Value

**PASS.** The motivating literature advocates induced-subgraph threshold sets as community-level vulnerability indicators and juxtaposes them with per-community infection sums. The theorem shows a mathematically substantive limitation of interpreting one as a monotone ranking of the other: all blocks can be isolated-subcritical, yet the seemingly more resistant path block has arbitrarily quadratically larger equilibrium burden than the clique block, even after controlling exactly for population size. The arbitrary-size bound and full equilibrium proof go beyond a small arbitrary graph example. The deliberately dense external mixing is essential contextual scope, not a claim about empirical weakly coupled communities.

Self-review: passed. Independent audit: not yet performed.
