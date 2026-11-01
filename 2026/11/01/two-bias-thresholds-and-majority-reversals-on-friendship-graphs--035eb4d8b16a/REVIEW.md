# Scientific review: two bias thresholds on friendship graphs

## Correctness — PASS

The integer-pair reduction is exact: every mixed triangle rim edge becomes the center's initial color in one update, while an initially monochrome edge is frozen. Center first-step flip is equivalent to \(b>a\); second-step final flip is equivalent to \(b>n/2\), or a tie with \(b>a\). These comparisons prove fixed-point entry by two, the majority-reversal identity, the complete fixed census and the sharp \(n\ge3\) threshold. Central-coefficient extraction gives the unbiased initial flip law; a binomial threshold minus a specified even-size exception gives the final flip law. Stirling's formula, geometric binomial-tail ratios, the law of large numbers and two triangular-array CLTs prove the limits. The independent adjacency-based verifier enumerates \(174{,}760\) initial states and \(42\) weighted cases. The theorem is strictly about the specified synchronous loopless tie-retention rule.

## Originality — PASS (qualified)

The closest conceptual antecedent is Mossel–Neeman–Tamuz, arXiv:1207.0893, Section 3.1, which exhibits biased-information loss through multiple cliques and a small core but employs a different graph with self-loops. Tamuz–Tessler, arXiv:1307.4035, proves general information-retention results; Benjamini et al., arXiv:1405.2486, cites Goles–Olivos' period-two theorem. Neither covers this explicit friendship-graph all-state cutoff, exact reversal census, two distinct critical bias values or their Gaussian windows. The literature and mathematical-record comparisons considered other names for the graph and equivalent signed-pair voting rules. Unindexed equivalents remain a residual risk; lack of a hit alone is not treated as a novelty proof.

## Value — PASS

The same network exhibits a transient global majority that is followed by a different stable global majority after two synchronous rounds. Under uniform inputs this happens asymptotically half the time even as the original center almost never changes permanently. Under biased inputs, the strict interval \(1/2<p<1/\sqrt2\) produces the temporary-reversal regime with probability tending to one, and the two sharp \(n^{-1/2}\) critical windows quantify its finite-size transitions. These are natural information-retention and attraction-basin statistics for a standard graph family, not a selected small-instance enumeration.

## Limitations

No independent validation is claimed. A complete historical literature census is unavailable; the equivalence risk in unindexed papers remains. The theorem does not generalize to other tie rules, asynchronous dynamics, or a fully i.i.d. center without mixing the two conditional laws.

Self-review: passed. Independent audit: not yet performed.
