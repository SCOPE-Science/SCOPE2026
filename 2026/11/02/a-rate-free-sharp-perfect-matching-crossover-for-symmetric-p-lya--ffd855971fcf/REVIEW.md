# Mathematical review

## Correctness

PASS (self-review). The precise graph model is the loopless projection of the sequential Pólya threshold graph. Reilly–Scheinerman's suffix matching test is reconstructed using Hall's condition, and the classical reflection count is combined with the exact exchangeable urn word weights. The endpoint representation and symmetry give an explicit first-order approximation by \(\mathbb E|K|/n\), with a deterministic error of order \(n^{-1}+\kappa_n^{-1}\). A joint Beta-normal/binomial-normal limit, a subsequence argument that does not assume a ratio limit, and uniform integrability prove the sharp constant. Reproduced finite exact and numerical tests: 8620 assertions. The finite tests do not prove the asymptotic.

## Originality

PASS relative to the inspected sources, with historical-priority risks. Reilly and Scheinerman (2009) already give the matching criterion and the independent fair-bit probability, so neither is counted as a new result. Yu, Alajaji and Gharesifard (2026) define the dependent graph process, the exact exchangeable word law and other graph properties, not the matching crossover. Antal, Ben-Naim and Krapivsky (2010) give Pólya first-passage/equality results, rather than this finite-horizon symmetric initial-mass/graph-size triangular-array law. Schulte-Geers and Stadje (2014) treat all-time maxima and fixed initial masses, including the known \(1-\log2\) limit. Actual searches of the accessible literature and mathematical claim records did not reveal the rate-free \(\sqrt{n^{-1}+\kappa_n^{-1}}\) matching law. A general unpublished or unindexed exchangeable-ballot theorem might imply it; no claim of unique priority is made.

## Value

PASS. Existence of a perfect matching is a basic structural connectivity condition for a random graph. Correlated vertex types change its chance in a way not visible from the same one-vertex marginal: the sharp coefficient and effective size show the exact boundary between sampling fluctuations and reinforcement heterogeneity. Unlike the already-known independent and fixed-concentration endpoint cases, the theorem works through every intermediate scaling, including oscillating concentration-to-size ratios. No broader classification or paper-sized consequence is asserted.

## Scope and checks

- The finite-word matching test and beta mixture are independent implementations; all logged finite assertions passed.
- The nonstandard joint central-limit step is proved with conditional characteristic functions and a subsequence argument.
- The graph is loopless for matching, initially colour-symmetric, and of even order.
- Limit regime requires both order and initial-to-reinforcement concentration to diverge.
- Related all-time and fixed-parameter urn formulas are credited, not presented as new.
- Risks: possible general boundary-crossing theorems outside the inspected corpus; no independent mathematical audit.

Self-review: passed. Independent audit: not yet performed.
