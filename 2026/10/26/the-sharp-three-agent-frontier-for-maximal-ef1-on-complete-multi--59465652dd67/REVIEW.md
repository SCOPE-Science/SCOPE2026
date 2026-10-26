# Review of the complete-multipartite maximal-EF1 theorem

## Correctness

PASS. The proof treats every complete multipartite graph, including the empty case, by the exhaustive alternatives: a part of at least three goods, a doubleton with all parts of size at most two, and all singleton parts. In the large-part case, the last-received-item inequality proves EF1 for an arbitrary common monotone set function and tie-breaking guarantees three nonempty bundles; leaving other parts unassigned is therefore maximal. In the doubleton case, the maximum of the lower singleton values ensures the two singleton recipients can both remove one item from the third agent's bundle to eliminate envy. All omitted parts conflict with all occupied parts. The known four-agent counterexample is fully reproved with an exact separation into three cases. The standalone verifier independently checks the constructed allocations and contrast on 187,375 exhaustive small additive instances, 4,885 nonadditive-monotone instances and 6,000 further additive instances; these experiments do not replace the general proof.

## Originality

PASS, subject to publication-priority limitations. The closest papers are Igarashi–Manurangsi–Yoneda (arXiv:2506.14149v1), Equbal et al. (arXiv:2605.09930v1), and Hummel–Hetland (DOI 10.1007/s10458-021-09537-3). Their results respectively concern two agents on arbitrary graphs and three-agent general-graph failures, additional path/tree and hardness regimes, and four-agent complete-allocation counterexamples. None of the inspected relevant passages states or implies the new universal three-agent complete-multipartite positive result under arbitrary identical monotone set valuations. Comparisons were made at the level of implications: the negative \(K_{3,3}\) case and two-agent theorem do not imply the new positive statement. Published-result and related-literature searches produced no decisive covering theorem. Residual risk is equivalent folklore or an unindexed specialized result; no independent priority audit is claimed.

## Value

PASS. This supplies a full, efficiently constructive structural subclass of the explicitly unsettled three-agent additive regime, and in fact handles the strictly broader class of identical monotone valuations. The three-to-four agent boundary is sharp even inside complete bipartite graphs. The result is not merely a fixed numerical census: it works for arbitrary part sizes, any number of parts, and nonlinear common valuations, while explaining exactly how discarding entire conflicting parts permits maximality without completeness. The known failure at four agents makes the positive threshold mathematically meaningful.

## Limitations

No claim is made for general conflict graphs, heterogeneous agents, nonmonotone values, complete allocations, EFX, or independent review. The four-agent construction and its first discovery belong to prior work. Searches cannot establish absolute publication priority.

Self-review: passed. Independent audit: not yet performed.
