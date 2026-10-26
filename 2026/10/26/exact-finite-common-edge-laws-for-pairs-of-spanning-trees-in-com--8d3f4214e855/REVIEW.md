# Review of exact common-edge laws for complete bipartite spanning trees

## Correctness — PASS

The two main assertions use a unique degree-core decomposition. A tree of \(K_{a,b}\) has exactly \(a-1\) excess degree units on the \(b\)-side, so at most \(a-1\) nonleaf vertices there. Conditioned on a fixed skeleton, the other vertices choose neighbours independently and uniformly. For a pair of skeletons, at most \(2(a-1)\) vertices require special treatment; all remaining common-edge indicators give independent Bernoulli \(1/a\) trials. Nonnegative probability-polynomial factorization establishes an **exact** convolution rather than a limiting approximation, and the maximum common-edge count bounds the correction degree. In the three-vertex-side case, exhaustive classification into the two possible skeleton forms gives the displayed rational polynomial, normalization, moments, and the exact number of disjoint tree pairs. The eight listed skeleton-pair cases distinguish all overlap patterns without double counting. Reproducibility checks from `verify.py` independently enumerate all \(186{,}624\) tree pairs of \(K_{3,4}\) and \(4{,}100{,}625\) pairs of \(K_{3,5}\), and verify the exact rational expressions through \(n=40\). The infinite claims are justified by the core and counting proofs, not finite tests.

## Originality — PASS, with priority qualifications

The closest direct paper, Bóna–Burghart–Wagner, arXiv:2501.18570v4, §5, observes an **approximately** binomial law when one bipartition class stays fixed and proves asymptotic results under other growth regimes. Its full inspected text does not determine an independent exact finite binomial component, the six-degree correction polynomial for \(K_{3,n}\), or the number of pairs with zero common edges. The forest-extension count of Dong–Ge, arXiv:2103.05294, and the multipartite version of Wang–Ge, arXiv:2602.03602, give counts for trees containing a fixed forest rather than the complete pair-overlap distribution. A two-row overlap formula applies only to \(K_{2,b}\); the three-row formulas and all-\(a\) convolution do not follow from that specialization alone. Related tree-packing existence theorems do not count the ordered pairs. No equivalent finite law was identified in the available comparisons. Historical priority under alternative names and the possibility of a derivation from more general unpublished identities remain residual risks; independent historical verification is not complete.

## Mathematical value — PASS

The precise fixed-small-side distribution is directly motivated by the non-Poisson regime identified in the recent random-spanning-tree literature. Determining its exact binomial factor for every small-side size, and the entire nontrivial bounded correction for the first three-vertex case, is substantially more informative than knowing the asymptotic normal regime or a first moment. The explicit zero-overlap term counts ordered edge-disjoint tree pairs for an infinite graph family, connecting probabilistic overlap laws with classical tree-packing enumeration. Both the law and the count are natural invariants of labelled complete bipartite graphs, not arbitrary parameter slices.

## Limits and comparison risks

The general factorization currently supplies the support bound rather than a closed expression for its correction polynomial; the full correction is established here for \(a=3\), \(b\ge4\). The result does not enumerate unlabeled tree decompositions or apply to arbitrary bipartite graphs. While the key related papers were inspected and multiple synonyms compared, broad literature coverage cannot establish absolute priority. The proof has had no independent mathematical audit.

Self-review: passed. Independent audit: not yet performed.
