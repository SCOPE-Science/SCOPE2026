# Exact static and adaptive shattering of six-leaf rooted triplet systems

## Finding
For the Boolean class \(\mathcal T_6\) obtained by asking whether a rooted, non-plane binary phylogenetic tree on six labeled leaves displays a prescribed resolved triplet, the exact dimensions are
\[
\operatorname{VCdim}(\mathcal T_6)=4,\qquad
\operatorname{Ldim}(\mathcal T_6)=9.
\]
Consequently its adaptive-minus-static shattering gap is five. The adaptive dimension attains the information-theoretic upper bound, because the class has precisely \(945\) different trees and \(\lfloor\log_2 945\rfloor=9\). For three through six leaves, the (number of trees, VC dimension, Littlestone dimension) triples are respectively \((3,1,1)\), \((15,2,3)\), \((105,3,5)\), and \((945,4,9)\).

## Assumptions and scope
A tree is a rooted, unordered, full binary tree, with each leaf carrying a different label in \(X=\{0,1,2,3,4,5\}\); every non-leaf has precisely two children. A resolved-triplet query \(ab\mid c\), for distinct \(a,b,c\in X\), returns one exactly when the least common ancestor of \(a,b\) is a proper descendant of the least common ancestor of \(a,c\). The pair \(ab\) is unordered. There are \(3\binom63=60\) queries. A query with answer zero allows either of the *other two* resolved topologies on its three labels. This last convention is essential: the result concerns a **Boolean one-vs-rest** class, not multiclass prediction with one specified competing topology per branch.

VC dimension is the maximum number of distinct fixed queries for which all zero-one patterns occur among the concepts. Littlestone dimension is the maximum depth of a complete binary tree whose internal nodes are labeled by queries and for which every complete answer path is realized by at least one concept. No hypothesis is imposed about tree shape beyond rooted binary branching, and no statement is made about larger leaf sets.

## Proof
**Enumeration lemma.** The number of rooted unordered full binary trees on \(n\ge2\) distinct leaves is \((2n-3)!!\): inserting a new labeled leaf as the sibling of a subtree, including the entire root subtree, gives exactly \(2n-3\) possible insertion positions and is reversible. In particular there are \(945\) trees for six leaves. Every tree is represented uniquely by its set of proper non-singleton descendant-leaf clusters. A resolved triplet \(ab\mid c\) is displayed exactly when some descendant cluster contains \(a,b\) but not \(c\). The standalone checker constructs the full cluster set in two independent ways: recursive root bipartition and repeated leaf insertion, and verifies that the two resulting sets agree.

**VC lower bound.** The four queries \(12\mid0\), \(14\mid5\), \(24\mid5\), and \(34\mid5\) produce all \(16\) Boolean patterns across the \(945\) trees. This claim is checked directly by the embedded script using the displayed-cluster criterion; it does not rely on a probabilistic sample.

**VC upper bound.** The leaf-relabeling group acts transitively on the \(60\) queries. If any support of five distinct queries were shattered, a relabeling would make its first query \(q_0=12\mid0\). Thus it suffices to enumerate shattered query supports containing \(q_0\). Starting with the partition of all \(945\) concepts according to their response at \(q_0\), append further queries in strictly increasing query-index order. A query extends a shattered support exactly when it splits *every* current nonempty response-pattern cell into two nonempty cells. If any cell is not split, no superset can be shattered, so discarding that branch is exhaustive. Across all \(59\) possible additional queries, this exact search finds respectively \(1,57,1458,18144\) shattered supports of sizes \(1,2,3,4\) that contain \(q_0\), and **none of size five**. Every possible five-query support is excluded by transitivity and prefix heredity. Therefore VC dimension is four.

**Littlestone lower bound.** The file `depth9_certificate.json` specifies a complete depth-nine adaptive query tree as nested `query`, `zero`, `one`, and `leaf` records. Its \(511\) internal nodes use query indices in the precisely defined lexicographic query list. Its \(512\) leaves name distinct complete phylogenetic trees among the \(945\) generated concepts. For each node the verifier filters surviving trees by the indicated response; every leaf's named tree survives all nine successive filters. Hence every response path is feasible and the Littlestone dimension is at least nine.

**Littlestone upper bound.** A complete depth-ten shattered query tree requires at least \(2^{10}=1024\) pairwise distinct hypotheses: one concept cannot realize two different paths because the paths first diverge at a query given two different responses. There are only \(945\) available trees. Thus the Littlestone dimension is at most nine.

For the three-, four-, and five-leaf entries in the first section, the same concept construction and fixed-query search are used, while the exact residual-concept recursion \(L(S)=\max_q(1+\min\{L(S_{q=0}),L(S_{q=1})\})\) over queries splitting \(S\), initialized at \(L(S)=0\) for singletons, establishes their adaptive dimensions. Every recursive call decreases the number of surviving concepts. The checker uses exact integer bitsets and memoization; an information-theoretic branch-size test only excludes branches too small to improve the current lower bound.

## Verification
From a directory containing the supplied artifacts, run:

```sh
python verify_rooted_triples.py depth9_certificate.json
```

The verifier uses only Python's standard library and validates the complete cluster enumeration by two methods, one-of-three rooted-triplet consistency, all fixed-support prefixes containing a representative query, explicit four-query lower witness, every path and witness of the nine-level adaptive certificate, and the exact smaller cases. It emits `ROOTED_TRIPLET_ALL_CHECKS_PASS` on success; its complete recorded output is in `verification_output.txt`. A separate optional script, `make_certificate.py`, reconstructs the adaptive certificate deterministically. The checker is an exhaustive finite proof implementation, not a substitute for unperformed independent audit.

## Relationship to prior work
Avdiukhin, Yaroslavtsev, Vainstein, Fischer, Das, and Mirza (2023, arXiv:2302.04492, Theorems 1.4 and 1.5 and Appendix C) establish Natarajan dimension \(n-2\) and multiclass Littlestone dimension of order \(n\log n\) for phylogenetic triplet labels. Their static shattering requires two *specified, distinct* triplet labels at each query, and their adaptive branches each specify a triplet orientation. The present Boolean interpretation permits either alternative triplet when the answer is zero. Neither their asymptotic result nor their exact Natarajan formula supplies the exact six-leaf Boolean VC and Littlestone dimensions here; the numerical conclusion is verified separately.

Semple and Toft (2020) emphasize that rooted triples uniquely encode binary phylogenetic trees, an injectivity fact compatible with the direct concept enumeration but insufficient to establish shattering dimensions. Harvey, Jansson, Marciniak, and Murakami (2024) classify complexity of required/forbidden resolved and fan triplet consistency; that decision-problem classification does not calculate Boolean shattering ranks. Arvanitakis and collaborators (2026) establish asymptotic Natarajan bounds for multiclass quartet queries, an adjacent but distinct learning problem. The present result claims neither a new tree-encoding theorem nor any new asymptotic learning rate.

## Limitations
The dimensions are established exactly only for at most six leaves. The claim does not resolve the static or adaptive dimensions for larger leaf sets, nonbinary trees, or multiclass labeling of a triple. The VC upper bound is computer-assisted exhaustive enumeration of finite supports; the Littlestone lower bound is a finite certificate, rather than a compact explicit closed-form construction. Accessible searches and primary comparisons do not establish universal historical priority, and independent scientific validation has not been performed.

## References
1. D. Avdiukhin, G. Yaroslavtsev, D. Vainstein, O. Fischer, S. Das and F. Mirza, *Tree Learning: Optimal Sample Complexity and Algorithms*, arXiv:2302.04492, first public version 2023-02-09, especially Theorems 1.4–1.5 and Appendix C. https://arxiv.org/abs/2302.04492
2. C. Semple and G. Toft, *Trinets encode orchard phylogenetic networks*, arXiv:2012.02231, first public version 2020-12-03. https://arxiv.org/abs/2012.02231
3. D. J. Harvey, J. Jansson, M. Marciniak and Y. Murakami, *Resolving Unresolved Resolved and Unresolved Triplets Consistency Problems*, IWOCA 2024. https://www.df.lth.se/~jj/Publications/ternary_triplets_consistency4_IWOCA_2024.pdf
4. D. Arvanitakis and collaborators, *Optimal Phylogenetic Reconstruction from Sampled Quartets*, arXiv:2604.17461, 2026; related multiclass quartet results. https://arxiv.org/abs/2604.17461
