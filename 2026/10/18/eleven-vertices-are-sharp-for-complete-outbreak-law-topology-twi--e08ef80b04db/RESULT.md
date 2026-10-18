# Eleven vertices are sharp for complete outbreak-law topology twins on trees

## Finding

**Theorem (complete-distribution indistinguishability, sharp minimum).** Let \(T\) be a finite, simple, unweighted tree with \(n\) vertices. Independently retain each edge with probability \(p\in(0,1)\), choose a vertex uniformly at random and independently, and let \(X_T(p)\) be the size of its open-edge connected component. For all \(n\le 10\), equality of the complete laws of \(X_T(p)\) and \(X_U(p)\), for all \(p\in(0,1)\), forces two \(n\)-vertex trees \(T,U\) to be isomorphic. At \(n=11\), there is exactly one unordered pair of nonisomorphic trees whose complete laws agree for every \(p\). Both have the same degree multiset \((1,1,1,1,1,1,2,2,3,3,4)\).

One explicit pair, with vertices labeled from \(0\) to \(10\), is:

```text
A: (0,1) (0,2) (0,3) (0,4) (1,5) (1,6) (2,7) (5,8) (8,9) (8,10)
B: (0,1) (0,2) (0,3) (0,4) (1,5) (1,6) (2,7) (7,8) (7,9) (8,10)
```

Their common uniform-source mean outbreak polynomial is

\[
\mathbb E X(p)=1+\frac{20p+28p^2+26p^3+18p^4+14p^5+4p^6}{11}.
\]

Their **entire**, not just mean, outbreak distributions coincide. For example, when \(p=1/2\), the eleven probabilities at outbreak sizes \(1,\ldots,11\) have the common exact numerator sequence

\[
(3904,1888,1680,1272,975,636,413,272,153,60,11)/11264.
\]

## Assumptions and scope

An *open cluster* is a connected component of the graph retaining each edge independently with common probability \(p\). The source is uniform on the vertices **before** edge states are sampled. Trees are unrooted and unlabelled for the isomorphism claim; the displayed labels merely encode an explicit witness. The theorem asserts uniqueness only **among eleven-vertex trees** and no statement about larger orders or arbitrary cyclic networks. In an epidemic interpretation, the transmission experiment is *independent undirected bond transmission*, not a general stochastic SIR process with dependent outgoing transmissions.

For a vertex set \(S\) inducing a connected subgraph, let \(k=|S|\), and let \(b_T(S)\) count edges of \(T\) with exactly one endpoint in \(S\). Write \(B_T(k,b)\) for the number of connected vertex sets with \(k\) vertices and boundary size \(b\).

## Proof

**1. Exact complete-law encoding.** Because \(T\) is a tree, a particular connected set \(S\) of \(k\) vertices is an open component precisely when its \(k-1\) internal edges are open and its \(b_T(S)\) boundary edges are closed. Edge states outside it are immaterial. Choosing a uniform root contributes a factor \(k/n\). Hence for all \(1\le k\le n\),

\[
\Pr\{X_T(p)=k\}=\frac{k}{n}p^{k-1}\sum_b B_T(k,b)(1-p)^b. \tag{1}
\]

For two trees of the same order, their complete distributions agree for every \(p\in(0,1)\) if and only if all integer coefficients \(B_T(k,b)\) agree: the monomials in \(1-p\) are linearly independent. Therefore the exact mathematical problem is the injectivity of the *connected-subset size–edge-boundary histogram* on unrooted trees.

**2. Exhaustive classification with proved coverage.** Starting from the one-vertex tree, generate each next order by attaching a leaf to each vertex of every preceding tree. Every nontrivial tree has a leaf, so deleting one from an arbitrary tree proves that this generation scheme reaches *every* isomorphism class. A center-rooted canonical string is formed by recursively sorting child strings, taking the lexicographically smallest encoding over the one or two centers. Center stripping and recursive encoding are isomorphism-invariant and complete: equality of rooted encodings gives a root-preserving tree isomorphism, and every unrooted isomorphism carries centers to centers. Deduplication by these strings leaves each isomorphism class exactly once.

For each generated tree, iterate through all nonempty vertex subsets; a graph-search on the induced subset decides connectivity, and if connected, its boundary count is the sum of degrees in the subset minus twice \(k-1\). This enumerates all coefficients in (1) using exact integers. The complete class counts at orders \(1,\ldots,11\) are

\[
1,1,1,2,3,6,11,23,47,106,235,
\]

matching the standard enumeration of unlabelled trees (OEIS A000055). Across all those classes, no two distinct trees of the same order have identical \(B\)-histograms at orders \(1\) through \(10\); at order \(11\), exactly one group consists of two trees and every other histogram is unique. The fully executable standard-library integer census and its exact output are in `verify_tree_outbreak.py` and `certificate.json`. The preceding coverage and canonicalization arguments turn this bounded computation into an exhaustive finite proof, not a sample search.

**3. Witness equality and nonisomorphism.** The two displayed trees share the following complete histogram; each entry lists boundary size followed by its count, with all omitted counts zero:

| \(k\) | \(b:\,B(k,b)\) |
|---:|---|
| 1 | 1:6, 2:2, 3:2, 4:1 |
| 2 | 1:1, 2:3, 3:4, 4:1, 5:1 |
| 3 | 1:1, 2:4, 3:3, 4:4, 5:2 |
| 4 | 1:1, 2:3, 3:6, 4:7, 5:1, 6:1 |
| 5 | 1:1, 2:4, 3:9, 4:4, 5:5, 6:1 |
| 6 | 1:1, 2:5, 3:6, 4:10, 5:6 |
| 7 | 1:1, 2:4, 3:10, 4:15 |
| 8 | 1:1, 2:5, 3:20 |
| 9 | 1:1, 2:15 |
| 10 | 1:6 |
| 11 | 0:1 |

Thus (1) yields equality of every outbreak probability for *all* \(p\), rather than equality at a grid of probabilities. The graphs are not isomorphic: vertex \(0\) is their unique degree-four vertex, but its distances to the two degree-three vertices form \(\{1,3\}\) in \(A\) and \(\{1,2\}\) in \(B\). This invariant rules out any graph isomorphism.

**4. Independent exact coefficient validation.** Enumerating all \(2^{10}=1024\) open-edge states, let \(A_T(k,j)\) be the number of *vertex–state pairs* with open cluster size \(k\) and precisely \(j\) open edges. Then

\[
\Pr\{X_T(p)=k\}=\frac1n\sum_{j=0}^{n-1}A_T(k,j)p^j(1-p)^{n-1-j}.
\]

For every tree, the two enumerations are connected by the exact identity

\[
 A_T(k,j)=k\sum_b B_T(k,b)\binom{n-k-b}{j-k+1}, \tag{2}
\]

with out-of-range binomial coefficients zero. Indeed, a fixed open component of size \(k\) forces its \(k-1\) internal edges open and \(b\) boundary edges closed, while the remaining \(n-k-b\) edges may be freely chosen. The verifier constructs \(A\) *directly* from all edge subsets, constructs the right side of (2) independently from connected vertex subsets, and checks equality for both eleven-vertex witnesses, together with equality of their complete coefficient tables. The common distribution at \(p=1/2\) above follows by summation.

## Verification

Run `python3 verify_tree_outbreak.py` with the Python standard library only and compare its exact, sorted JSON output with `certificate.json`. The program generates every tree class through order eleven, checks counts \(1,1,1,2,3,6,11,23,47,106,235\), checks no duplicate profiles through ten and exactly one double profile at eleven, gives both witness edge lists, verifies the boundary-to-edge-state coefficient identity, and returns the complete exact common polynomial coefficients. An additional independent enumeration using `networkx.nonisomorphic_trees` at orders two through eleven produced the same class counts and profile collision counts; that optional corroboration does not enter the standalone proof. No floating-point comparison occurs.

## Relationship to prior work

Newman's percolation framework motivates the finite independent-transmission outbreak-size proxy. Kenah and Robins establish why general stochastic SIR with nondegenerate infectious periods cannot automatically be replaced by independent undirected bonds; the present claim deliberately stays on the valid independent-bond side of that boundary. Lanchier and La Salle analyze the first two moments of finite regular-graph percolation cluster sizes rather than topology identification among trees. Hosoya polynomial research studies a coarser pair-distance profile, which determines the first-moment curve on trees but not necessarily the full distribution. Earlier tree polynomials, including the polynomial of Chaudhary and Gordon, are related through subtrees and structural invariants but do not by their accessible claims establish the stated sharp eleven-vertex complete-distribution collision classification. The ordinary count of unlabelled trees in OEIS A000055 is used solely to corroborate census coverage; it contains no claimed collision table for this percolation invariant.

## Limitations

The equality is for a *uniformly selected, unobserved source* and *homogeneous independent edge transmission*. Recording the source identity, heterogeneous edge probabilities, directional transmissions, timings, or additional spatial observations can distinguish the trees. The numerical cutoff is established only through eleven vertices, not an all-orders classification of collision families. The result is not a claim of a new graph-isomorphism algorithm and not an inference guarantee under finite or noisy observed outbreaks. Related graph-polynomial results may encode this phenomenon under another name; bibliographic equivalence is not independently certified.

## References

1. M. E. J. Newman, “The spread of epidemic disease on networks,” first public preprint 2002-04-30, arXiv:cond-mat/0205009; *Physical Review E* 66, 016128 (2002). https://arxiv.org/abs/cond-mat/0205009
2. E. Kenah and J. M. Robins, “Second look at the spread of epidemics on networks,” arXiv:q-bio/0610057 (2006); *Physical Review E* 76, 036113 (2007). https://arxiv.org/abs/q-bio/0610057
3. N. Lanchier and A. La Salle, “First and second moments of the size distribution of bond percolation clusters on regular graphs,” arXiv:2111.01982 (2021). https://arxiv.org/abs/2111.01982
4. E. Deutsch and S. Klavžar, “Computing Hosoya polynomials of graphs from primary subgraphs,” arXiv:1212.3179 (2012). https://arxiv.org/abs/1212.3179
5. S. Chaudhary and G. Gordon, “Tutte polynomials for trees,” *Journal of Graph Theory* 15 (1991), 317–331. https://doi.org/10.1002/jgt.3190150308
6. OEIS Foundation, A000055, “Number of trees with \(n\) unlabeled nodes.” https://oeis.org/A000055
