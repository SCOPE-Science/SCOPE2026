# Optimal census-depth recovery of tree-shaped ecological interaction networks

## Finding

Let \(T\) be a simple undirected tree on \(n\) unlabeled taxa, interpreted as an idealized ecological interaction network. For each \(k\in\{0,\ldots,n\}\), draw a subset \(S\) of exactly \(k\) distinct taxa uniformly without replacement. Let \(X_{T,k}\) count the interaction edges with **both** endpoints in \(S\). A census at depth \(k\) means knowing the complete probability distribution of \(X_{T,k}\), not merely observing one random count. The total number \(n\) of taxa is known, but identities of the taxa and of the edges are not observed.

**Theorem (complete minimum-depth classification through nine taxa).** For each \(4\le n\le8\), the following is the exact set of depths \(k\) for which the law of \(X_{T,k}\) identifies every unlabeled \(n\)-vertex tree \(T\) among such trees:

| Taxa \(n\) | All individually sufficient depths \(k\) |
|---|---|
| 4 | \(3\) |
| 5 | \(3,4\) |
| 6 | \(4\) |
| 7 | \(4,5\) |
| 8 | \(5\) |

For \(n=9\), no single depth is sufficient. Exactly five unordered pairs of sampling depths suffice, and they are
\[
\{4,6\},\quad\{5,6\},\quad\{5,7\},\quad\{6,7\},\quad\{6,8\}.
\]
Thus the minimum number of distinct sampling depths jumps from one to two at nine taxa. For \(n=10\), no collection of depths identifies every tree: two nonisomorphic ten-vertex trees have identical laws at **all** depths. That full-information obstruction was previously known as an equality of subgraph component polynomials [2]; the new classification concerns the much smaller, optimally selected collection of fixed-cardinality laws.

For \(n\le3\), the unlabeled tree topology is unique without any census. Moreover, for all \(n\ge2\) and all depths, the mean
\[
\mathbb E[X_{T,k}]=\frac{k(k-1)}{n}
\]
is independent of topology; the identification here comes from the full distribution, not the mean.

## Assumptions and scope

The contact graph is a connected, acyclic, unweighted, simple and undirected graph. Sampling is uniform over the \(\binom nk\) subsets of size \(k\). Every edge is counted if and only if its two endpoints are in the sample; there is no sampling error, detection error or uncertainty about \(n\). Trees are compared up to graph isomorphism; labeling is irrelevant. The result is a finite exact classification for \(n\le10\). It does not assert identification for arbitrary graphs or for larger trees.

Write
\[
H_{T,k}(j)=\#\{S\subseteq V(T):|S|=k,\ |E(T[S])|=j\},
\qquad
\Pr(X_{T,k}=j)=\frac{H_{T,k}(j)}{\binom nk}.
\]
The law is therefore equivalent to the integer histogram \(H_{T,k}\). For trees, each induced graph is a forest and has \(k-j\) connected components when it contains \(j\) edges. Consequently the complete family of such histograms is a reindexing of the subgraph component polynomial in [2].

## Proof

**Step 1 — Normalization and information content.** Each of the \(n-1\) tree edges lies entirely in a uniform \(k\)-subset with probability \(k(k-1)/(n(n-1))\), which proves the claimed mean. The positive denominator \(\binom nk\) establishes that equality of entire laws is equivalent to equality of integer histograms for the same \(n,k\). The histograms for \(k=0,1,n\) are constant over all \(n\)-vertex trees, so only depths \(2\le k\le n-1\) need consideration.

**Step 2 — Exhaustive enumeration without a precomputed tree table.** The attached standard-library program `verify.py` generates all unlabeled trees of order at most ten inductively, starting from the one-vertex tree. Given all representatives with \(r\) vertices, it adjoins a new degree-one vertex separately to every vertex of every representative and retains one representative of each resulting isomorphism type. Every tree with \(r+1\ge2\) vertices has a leaf; removing that leaf gives an \(r\)-vertex tree. By induction, adding the leaf back at the corresponding vertex produces a generated isomorphic copy. Therefore no isomorphism class is missed.

Duplicate removal uses canonical rooted-tree encodings. A tree's center is either a single vertex or a pair of adjacent vertices, identifiable by simultaneous repeated removal of leaves. Root at the unique center, or encode the two centered rooted halves in sorted order, and recursively encode each rooted branch by a sorted sequence of its children's encodings in parentheses. Induction on rooted-tree size shows equality of encodings is equivalent to rooted isomorphism. The tree center is preserved by isomorphisms, so equality of the resulting whole-tree code is equivalent to unrooted isomorphism. Hence the construction contains exactly one tree of every unlabeled type. As a cross-check, the enumerated type counts by order from one to ten are
\[
1,1,1,2,3,6,11,23,47,106.
\]

**Step 3 — Exact distribution computation and identification.** For each generated tree the program visits every one of the \(2^n\) vertex subsets, calculates both its cardinality and the number of edges induced by it using exact bit operations, and increments \(H_{T,k}(j)\). It verifies \(\sum_j H_{T,k}(j)=\binom nk\) for every \(k\), then compares complete integer vectors for all pairs of distinct tree types.

The complete list of individual identifying depths for orders four through eight is precisely the first table in the Finding. For order nine, the following table gives the **number of unordered nonisomorphic tree pairs with equal complete sampling distributions** at each one depth:

| Depth \(k\) | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---:|---:|---:|---:|---:|---:|---:|
| Indistinguishable pairs | 1081 | 117 | 10 | 1 | 1 | 7 | 96 |

Every entry is positive, and the previously excluded depths are topology-blind. Thus one depth cannot identify every nine-vertex tree. Comparing the ordered pair of histograms at every two-depth combination reveals exactly the five pairs stated in the theorem, with **zero** indistinguishable tree pairs for each of those five and at least one indistinguishable pair for every other two-depth combination. This both proves sufficiency and exhaustively classifies all minimum two-depth designs.

**Step 4 — Full-information boundary.** The generator finds two ten-vertex trees, displayed here as sets of edges using vertices numbered 0 through 9, with different canonical forms but identical \(H_{T,k}(j)\) for **every** \(k,j\):

```text
A: (0,1) (0,2) (0,3) (1,4) (1,5) (2,6) (3,7) (6,8) (8,9)
B: (0,1) (0,2) (0,3) (1,4) (1,5) (2,6) (4,7) (6,8) (7,9)
```

The program verifies both nonisomorphism and exact agreement. This phenomenon, including the ten-vertex threshold for full subgraph-component data, is already established in Proposition 3 of [2]; it is cited here to delineate the limit of the new optimal-design classification, not offered as a new counterexample.

## Verification

Run `python3 verify.py` with Python 3.10 or newer; no external packages or downloaded data are required. The script checks all tree-shape counts, exact histogram normalizations, complete one-depth classifications for orders four to eight, all seven one-depth collision counts for order nine, all twenty-one two-depth choices for order nine, and the full-data ten-vertex collision. Its ending marker is `VERIFY_OK`. Independently, a separate enumeration using graph-library nonisomorphic trees and direct subset combinations agreed on the minimum-depth result for orders up to nine; that additional check is corroborative only. The complete exhaustive verification is supplied in the program itself and its coverage is justified in Step 2.

## Relationship to prior work

Martinez et al. [1] document the ecological importance of sampling effort when inferring food-web structure; their empirical setting does not define the idealized exhaustive probability-law experiment used here. Tittmann, Averbouch and Makowsky [2] define the induced-subgraph component polynomial, prove that it distinguishes nonisomorphic trees through order nine, and exhibit the first full-polynomial tree collision at order ten. Those prior facts are necessary context, not claims of novelty. The logical fact that a full collection of sampling depths distinguishes trees through nine does **not** imply that a single depth works for eight or that precisely two suffice for nine; the complete optimal depth choices and exact collision counts here require new comparisons of the individual cardinality slices. Liao and Hou [3] establish other structural recovery theorems from the full polynomial and distinguish different graph families; the relevant examined statements do not supply this complete minimum-depth classification.

## Limitations

The result assumes that the entire theoretical sampling law is known exactly at each selected depth; it does not bound the number of replicate observations required to estimate it reliably. No claim is made about noisy data, directed or weighted networks, non-tree interactions, unknown network size, or any order beyond ten. The enumeration is a rigorous finite proof because its generation and isomorphism reduction are complete; it is not a proof about all infinite orders. The ten-vertex loss of identifiability is prior literature, while the one-depth/two-depth design distinction is the delimited contribution. Unindexed equivalent enumerations of cardinality-specific graph-polynomial coefficients remain a literature risk.

## References

[1] N. D. Martinez, B. A. Hawkins, H. A. Dawah, and B. P. Feifarek, "Effects of sampling effort on characterization of food-web structure," *Ecology* **80** (1999), 1044–1055. First published 1999-04-01. DOI: 10.1890/0012-9658(1999)080[1044:EOSEOC]2.0.CO;2.

[2] P. Tittmann, I. Averbouch, and J. A. Makowsky, "The enumeration of vertex induced subgraphs with respect to the number of components," arXiv:0812.4147, initial public version 2008-12-22; *European Journal of Combinatorics* **32** (2011), 954–974. https://arxiv.org/abs/0812.4147.

[3] Y. Liao and Y. Hou, "Note on the subgraph component polynomial," arXiv:1311.6856, initial public version 2013-11-27; *Electronic Journal of Combinatorics* **21** (2014), #P3.27. DOI: 10.37236/3953.
