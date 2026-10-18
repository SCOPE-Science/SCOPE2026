# Scientific review

## Correctness — PASS
Conditioning on the first closed chord at position \(t\) partitions the matching into \(t-1\) early chords and \(n-t+1\) fully late chords. All early/early crossings occur with conditional probability one half, all eligible open-early/late crossings with one third, and all late/late crossings with one third. These give the exact regression for every admissible \(n,t\). Unconditional crossing mean and classical variance, the exact first-closure tail and Rayleigh moment convergence prove the sharp covariance and correlation equivalents. The standalone finite verifier checks every matching through seven chords.

## Originality — PASS, with residual risk
Acan–Hitczenko's arXiv:1411.5751v1 (examined throughout the introductory model, Theorem 4, and its proof) describes the first closure and its marginal Rayleigh limit, not the exact conditional crossing regression. Acan's arXiv:1501.01489v1 (examined through the introduction, statement of results, and crossing discussion) studies chord intersection graphs but does not give the first-closure conditional expectation. Flajolet–Noy (2000) give unconditional crossing moments, which do not determine a conditional mean given the earliest closure. An earlier joint-enumeration relation remains possible; that possibility has not been ruled out conclusively. 

## Mathematical value — PASS
Two separately studied natural statistics—earliest repeated pair and intersection-graph edge count—obey a complete exact monotone regression and a sharp finite-size crossing-excess phase boundary. The result distinguishes a systematic finite-sample positive association from asymptotically vanishing correlation, with an explicit coefficient. These quantities are mathematically motivated by the standard memory-game and random chord-intersection models.

## Limitations
The conditional crossing law is a mean identity only. Velleman–Warrington's original full paper was not inspected; an implicit equivalent statement may exist. A full independent priority and correctness audit is outstanding.

Self-review: passed. Independent audit: not yet performed.
