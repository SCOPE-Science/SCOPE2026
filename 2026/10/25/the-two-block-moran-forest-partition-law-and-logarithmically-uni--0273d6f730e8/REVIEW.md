# Review: Two-block Moran-forest partition sizes

## Correctness (C): PASS

Starting from the published independent-parent representation, every two-component labeling is counted by within-block increasing attachments and root choices; averaging the initial run yields the displayed finite mass. Combining with the independently proved Poisson-binomial root law normalizes the result. Exact arithmetic exhausts all parent assignments through n=7 and verifies normalization to n=100. Uniform weight asymptotics and harmonic normalization prove the unrestricted log-scale limit; finite checks are not relied on for the limit.

Critical points: the earliest birth in each block selects a later parent; every other birth selects an earlier same-block parent. The first-run length has expectation \(a/(b+1)+b/(a+1)\). Every equal-size bipartition is counted with a factor \(1/2\). The exact mass normalization follows independently from the existing Bernoulli root law. The log-uniform limit follows from \(w_n(s)=1/(s+1)+O(1/n)\), uniformly for \(1\le s\le n/2\), and \(Z_n=\log n+O(1)\). The verification script uses finite exhaustive checks but is not the justification of these identities for unbounded order.

## Originality (O): PASS, subject to residual historical-priority uncertainty

The founding author-open preprint, arXiv:1906.08806, expressly identifies the full exchangeable partition probability function as lacking a closed expression; only the root-count and unconditioned selected-tree laws are supplied. Later arXiv:2509.19678 studies edit-chain spectra, not partition sizes. Specific searches for the Moran two-block sector and the log-uniform conditioned law returned no coincident or stronger result. Residual risk of unindexed equivalent work is acknowledged, not treated as proof of historical priority.

The closest primary source is Bienvenu, Duchamps and Foutel-Rodier, *The Moran forest* (arXiv:1906.08806). Its Section 2.2 specifically notes the lack of a closed EPPF. Its root-count generating function is weaker than partition-size information. Chung and Robertson (arXiv:2509.19678) provides a spectral generalization of editing processes, not a complete or two-component EPPF. Uniform set-partition frequency-count identities concern a different probability measure. An inaccessible or unindexed prior equivalence remains a priority risk, not proof of nonexistence.

## Mathematical value (V): PASS

The EPPF is the natural, expressly identified unresolved descriptor of the stationary Moran forest. Its exact complete two-component sector is nontrivial at every finite order and yields a qualitative rare-event phenomenon: conditioned on exactly two components, the smaller component has no single deterministic power scale, with a uniform logarithmic exponent. This is not the ordinary typical-tree size law, and can serve as a baseline for later multiblock EPPF investigations.

## Scope and limitations

The result is limited to exactly two components in a labeled stationary Moran forest and does not produce the general all-component partition law. The logarithmic limit is under rare-event conditioning. Exact finite tests validate concrete instances, not arbitrary sample size. Independent mathematical assessment remains to be done.

Self-review: passed. Independent audit: not yet performed.
