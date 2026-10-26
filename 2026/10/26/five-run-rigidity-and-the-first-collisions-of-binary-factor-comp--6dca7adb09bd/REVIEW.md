# Scientific review

## Correctness — PASS
The run-count discriminator first recovers the labeled symbol totals and monochromatic maxima, then distinguishes two, three, four, and five runs using full-total rows of the Parikh support. For four runs the minimum-zero count at all ones gives the interior zero run and the first maximum-zero threshold determines the first one run. For five runs the maximum-zero counts at the larger and smaller one-run lengths determine both unordered outer-run and inner-run pairs and their pairing modulo reversal. These arguments cover all positive run lengths, including equalities. The explicit six-run family is proved by complete four-row factor-composition enumeration. Direct exhaustive enumeration and a constructive inverse program agree on the tested finite domains; computations are checks, not substitutes for proof.

## Originality — PASS
The closest work is Burcsi et al., arXiv:1611.09017, Theorem 4, which gives the general equivalence of identical factor-Parikh supports and pairs of prefix-normal forms, but not the sharp run-bounded injectivity, inverse run-length formulas, or explicit six-run collision spectrum. Cunha et al., DOI:10.4230/LIPIcs.CPM.2017.19, studies algorithms for the same run-length encoded setting but does not state inverse injectivity. Afshar et al., arXiv:2007.08787, Lemma 9, provides the reversal obstruction, not a converse for any run-bounded class. Fleischmann et al., arXiv:1905.11847, treats the weaker equality of a single prefix-normal form. Searches for the same combinatorial claim, equivalent prefix-normal conditions, and stronger coverage did not reveal an implication subsuming this exact classification. Residual risk: an equivalent run-count corollary could exist in unindexed literature.

## Mathematical value — PASS
The full Parikh-factor support is the exact information available to a binary jumbled-pattern index. Determining when this data has a unique source up to its unavoidable reversal symmetry is a motivated inverse problem. A sharp five-to-six-run transition provides a natural structural boundary, an explicit reconstruction procedure, the shortest collision length, and an infinite collision family; it is not a parameter substitution or isolated table entry.

## Limits
All claims are for contiguous factors over the labeled binary alphabet. The six-run pairs prove loss of injectivity, not a classification of all higher-run ambiguity classes. Finite verification is confined to the stated ranges; originality comparisons are literature-based and cannot exclude unindexed equivalent presentations.

Self-review: passed. Independent audit: not yet performed.
