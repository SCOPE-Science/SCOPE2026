# Exact smallest-attractor transition for Thue–Morse words

## Finding
Let \(t_0=0\) and \(t_{m+1}=t_m\overline{t_m}\), where the bar complements every bit. If \(\mathcal A(t_m)\) denotes the family of minimum-cardinality string attractors, then
\[
|\mathcal A(t_4)|=87,\qquad |\mathcal A(t_5)|=40,\qquad |\mathcal A(t_6)|=32.
\]
All minimum attractors of \(t_6\) are classified exactly: choose one position from each of \(\{16,17\}\), \(\{32,33\}\), and \(\{48,49\}\), and choose the fourth position from exactly one of the two pairs \(\{24,25\}\) or \(\{40,41\}\). Every such choice is a minimum attractor, and there are exactly \(32\) choices.

## Assumptions and scope
A string attractor of a finite word \(w\) is a set of positions meeting at least one occurrence of every distinct factor of \(w\). Positions here are one-based. The claim concerns only the three finite Thue–Morse words \(t_4,t_5,t_6\), of lengths \(16,32,64\), and does not assert stabilization beyond \(t_6\).

The cutoff is intrinsic to the known size theorem. Kutsukake et al. prove that the minimum attractor size is \(4\) for every \(t_m\) with \(m\ge4\); their lower-bound argument handles \(m\ge6\) uniformly, while \(t_4\) and \(t_5\) are the two exceptional base cases checked exhaustively. Thus \(t_4,t_5,t_6\) isolate the transition from the exceptional base cases to the first word in the uniform regime.

## Proof
For a factor \(u\) of a finite word \(w\), let \(C_w(u)\) be the set of positions covered by at least one occurrence of \(u\). A position set \(S\) is a string attractor exactly when \(S\cap C_w(u)\ne\varnothing\) for every distinct factor \(u\). Hence minimum string attractors are minimum hitting sets of the finite hypergraph \(\{C_w(u):u\text{ is a factor of }w\}\).

For each of \(t_4,t_5,t_6\), the verifier constructs every distinct factor directly from the word and forms its exact coverage set. Duplicate coverage sets are removed, and then every inclusion-nonminimal edge is removed. The verifier checks that every original coverage edge contains one retained minimal edge, so hitting the reduced hypergraph is equivalent to hitting the full factor hypergraph.

It then enumerates every position subset of cardinality at most \(4\). No subset of cardinality at most \(3\) hits every retained edge. At cardinality \(4\), the exact solution counts are respectively \(87\), \(40\), and \(32\). Each positive solution is independently rechecked against all factor occurrences, rather than only against the reduced hypergraph.

For \(t_6\), the resulting \(32\) solution sets are compared with the explicit family
\[
\{a,b,c,d\},
\]
where \(a\in\{16,17\}\), \(c\in\{32,33\}\), \(d\in\{48,49\}\), and \(b\) belongs to exactly one selected pair among \(\{24,25\}\) and \(\{40,41\}\). The two families agree element-for-element. This supplies both the count and the classification.

## Verification
The supplied verifier reconstructs the Thue–Morse words, factor-coverage hypergraphs, inclusion-minimal edge sets, and all candidate subsets from scratch. Across the three lengths it checks \(723084\) subsets. It also compares the recomputed minimum attractors with `ATTRACTORS.tsv` and directly checks every recorded attractor against every distinct factor occurrence. Successful replay ends with `VERIFY_OK transition_counts=87,40,32 t6_classification=32 total_subsets_checked=723084`.

## Relationship to prior work
Kutsukake et al. determine the minimum attractor size of Thue–Morse words, proving \(\gamma(t_m)=4\) for \(m\ge4\), but do not enumerate all minimizers. Schaeffer and Shallit revisit Thue–Morse attractors in an automatic-sequence framework, record minimum-size information and witnesses, and report that a direct automatic characterization analogous to the period-doubling case did not complete. Banbara et al. later classify and count all smallest attractors for Fibonacci and period-doubling words and explicitly motivate the number of smallest attractors as a finer repetitiveness statistic; their Thue–Morse discussion cites the known size result rather than a complete minimizer enumeration.

The present finite classification therefore supplies the exact smallest-attractor multiplicity at the two exceptional Thue–Morse base cases and the first uniform-regime case, together with a closed description at length \(64\).

## Limitations
The proof is exhaustive and exact only for \(t_4,t_5,t_6\). The observed value \(32\) is not claimed to persist for longer Thue–Morse words. Literature searches cannot rule out an unindexed table, thesis appendix, private computation, or differently phrased prior enumeration; this is the main residual originality risk.

## References
1. K. Kutsukake et al., “On repetitiveness measures of Thue–Morse words,” arXiv:2005.09524, first public version 2020-05-19.
2. L. Schaeffer and J. Shallit, “String Attractors for Automatic Sequences,” arXiv:2012.06840, first public version 2020-12-12.
3. M. Banbara et al., “The Smallest String Attractors of Fibonacci and Period-Doubling Words,” CPM 2026, DOI 10.4230/LIPIcs.CPM.2026.33.
