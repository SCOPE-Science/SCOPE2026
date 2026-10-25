# Review

## Correctness (C): PASS

For the specified mixed attachment process, the probabilities of increasing and decreasing the fixed vertex's leaf-neighbour count are enumerated exactly. Their difference is

\[
\frac{(1-2p)(L-1)+(1-p)(1-L/D+S)}n,
\]

with \(L\le D\) and \(S\ge0\). The positive-part transform yields the multiplicative expectation inequality, and a two-direct-attachment event supplies a strictly positive starting value. The gamma product and its asymptotic give the claimed constant. The statement is limited to expectations and makes no almost-sure or upper-bound claim.

## Originality (O): PASS, best-knowledge comparison

The full text of *Random friend trees* (arXiv:2403.20185v1) was inspected for the model variant and its results. It states qualitative degree divergence for the direct-versus-neighbour mixture but does not state the fixed-vertex expected leaf-neighbour lower bound. The full text of Cannings–Jordan, *Random walk attachment graphs* (arXiv:1303.1052v2), was also inspected; its mixed zero-step/one-step result concerns the global leaf proportion, not this local statistic. published-finding corpus searches using model names, the direct-attachment parameter, leaf-neighbour count, and the proposed exponent returned no matching result; nearby random-recursive-tree claims concern different models and observables. This is not a claim that literature search is exhaustive.

## Value (V): PASS

Leaf-neighbour counts are the local reinforcement statistic driving the friend-tree attachment probability. The mixed direct/one-step model is explicitly proposed as a natural variation of the friend-tree model, while the available result is qualitative. The bound supplies a quantitative, parameter-dependent lower-growth benchmark for each fixed vertex in the regime \(0<p<1/2\), with an explicit positive constant. It does not overstate this as an exact exponent or phase transition.

## Closest literature and limitations

- Addario-Berry et al., *Random friend trees*, arXiv:2403.20185v1 (2024): introduces the model and discusses the mixture; the inspected result is qualitative for the mixture.
- Cannings and Jordan, *Random walk attachment graphs*, arXiv:1303.1052v2 (2013): proves bounds for the global proportion of leaves under a zero-step/one-step mixture, which do not imply this fixed-vertex expectation bound.
- Residual risk: unindexed work may study local leaf-neighbour statistics in the same mixture. The claim is an expectation lower bound only; an independent audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
