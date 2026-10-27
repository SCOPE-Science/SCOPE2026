# Scientific review: four-agent pairwise-distance facility selection

## Correctness — PASS

The exact expected-cost formula independently enumerates all six unordered sampled pairs. The unrestricted optimum follows from contiguous clustering and the median property for absolute distances. Reflection reduces the universal inequality to five explicit positive polynomial certificates for \(2\mathrm{OPT}\,Z-N\); the limit family verifies sharpness. The standalone `verify.py` passed 32,015 exact-rational assertions and is supplementary, not a substitute for the proof.

## Originality — PASS, with residual priority risk

Ma and Peng (arXiv:2608.09061), Chan, Lin, and Wang (arXiv:2608.22484), and Jia (arXiv:2608.19633) establish the same rule's population-uniform ratio \(4\), but a population-uniform sharp factor does not imply the fixed-four-agent factor \(2\). The exact four-agent statement and nonattainment are not present in the materially inspected two main texts. The Jia full text was not accessible for complete comparison, so an equivalent statement in that manuscript remains a residual risk. Targeted bibliographic and mathematical-results searches found no equivalent stated frontier; unsuccessful searches are not proof of priority. Earlier three-agent inverse-power mechanisms and one-omission Product-Gap analyses have different probabilities or cardinality regimes. The deterministic Two-Extremes factor \(2\) concerns a different mechanism and does not subsume this result.

## Value — PASS

The first four-agent two-facility case permits two agents to be unserved simultaneously, making its exact efficiency loss a natural benchmark. The factor \(2\), strictly half the established population-uniform factor, is sharp; the diverging-outlier family identifies a distinctive rare-but-costly event that keeps the limiting expected loss nonzero. This is a finite-electorate mathematical characterization, not a claim about large-population optimality or new incentive compatibility.

## Limitations and remaining risk

Only exactly four distinct, equally weighted reports on the real line are covered; no claim is made for co-location, more agents, metric spaces other than the line, or other rules. A plausible inaccessible primary manuscript and unindexed work present publication-priority risks. No external audit, independent reproduction, or certification has been conducted.

Self-review: passed. Independent audit: not yet performed.
