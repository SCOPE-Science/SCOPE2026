# Independent mathematical audit

## correctness

PASS

Let \(G=K_{n_1,\ldots,n_r}\) and let \(m_i\) be the number of selected vertices in part \(i\). Global domination is equivalent to meeting every part: domination in the complement, which is the disjoint union of the part cliques, forces and is forced by \(m_i\ge1\) for every \(i\). In a complete multipartite graph every induced path has length at most two. Consequently a selected set is monophonic exactly when either at least two parts contribute at least two selected vertices, or exactly one part does so and that part is selected in full, with the all-singleton case reducing to the whole vertex set. Combining the two predicates gives the submitted all-set classification. Minimizing the resulting profiles gives \(N\) when at most one part has size at least two, \(r+1\) when at least two such parts exist and some part has size two, and \(r+2\) otherwise; the submitted minimum-set counts follow by choosing the exceptional parts and singleton selections. The inspected exact-commit verifier implements exhaustive definition-level checks of the predicate and minimum formulas on all 87 multipartite types through order nine and 22,932 subsets; the universal conclusion rests on the symbolic proof above, not on those finite checks.

## originality

PASS

The 2021 defining paper gives the complete-bipartite specialization, not an arbitrary complete-multipartite all-set classification. The complete 13-page 2026 follow-up was read in this round after open routes did not yield full text; it develops general bounds, extremal characterizations, realization results and corona products, but contains no complete-multipartite theorem. Resultary searches for the exact arbitrary-multipartite conjunction returned nearby domination polynomials but no equivalent monophonic-global result. Thus the submitted structural classification, generating polynomial and exact minimum-set counts survive statement-level comparison.

## value

PASS

Complete multipartite graphs are a canonical extension of the published complete-bipartite case. The result gives every admissible set, a closed enumerator, the exact minimum and exact minimum-set counts, so it is a complete natural family classification rather than an isolated computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
