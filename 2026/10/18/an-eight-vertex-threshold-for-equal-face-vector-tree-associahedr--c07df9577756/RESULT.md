# An eight-vertex threshold for equal-face-vector tree associahedra with unequal Gaussian angular collisions

## Finding

Let \(G_A\) and \(G_B\) be the following two trees on \(\{0,1,\ldots,7\}\):

\[
\begin{aligned}
E(G_A)&=\{01,02,14,23,45,46,47\},\\
E(G_B)&=\{01,02,14,17,23,45,46\}.
\end{aligned}
\]

Here \(ij\) denotes the undirected edge \(\{i,j\}\). Their degree multisets are respectively \(\{4,2,2,2,1,1,1,1\}\) and \(\{3,3,2,2,1,1,1,1\}\), so the trees are not isomorphic.

Define their canonical graph associahedra as the coordinate-simplex sums

\[
P_G=\sum_{\substack{\varnothing\ne S\subseteq V(G)\\G[S]\text{ connected}}}\operatorname{conv}\{e_i:i\in S\}\subset\mathbb R^8.
\]

Each is a seven-dimensional polytope. They have **the identical complete face vector**, listed in increasing face dimension (including the whole polytope):

\[
(f_0,f_1,\ldots,f_7)=(2952,10332,14336,10010,3680,676,52,1).
\]

For independent isotropic Gaussian objective vectors \(Z,Z'\), let \(C(G)\) denote the probability that the vertices of \(P_G\) uniquely exposed by \(Z\) and by \(Z'\) coincide. Their exact collision probabilities differ:

\[
C(G_A)=\frac{14239}{4838400},\qquad
C(G_B)=\frac{76393}{33868800},\qquad
C(G_A)-C(G_B)=\boxed{\frac{97}{141120}}>0.
\]

**Sharp finite-order threshold.** Among canonical graph associahedra of nonisomorphic trees having at most seven vertices, equal complete face vectors never occur. Among the 23 nonisomorphic trees on eight vertices, \(G_A,G_B\) form the only pair with an equal vertex count, hence the only equal-face-vector pair. Thus **eight** is the least possible number of graph vertices for an equal-face-vector pair of tree associahedra whose Gaussian angular collision probabilities differ.

## Assumptions and scope

All graphs are finite, undirected, simple trees. An induced subgraph \(G[S]\) is connected when every pair of its vertices is joined inside \(S\). A tube is a nonempty proper connected vertex subset. Two tubes are compatible if nested, or disjoint with no graph edge joining them. The graph associahedron is the unit-weight coordinate-simplex Minkowski sum displayed above, in its intrinsic coordinate-sum affine hyperplane with the ambient Euclidean metric. Adding common singleton translations does not change its normal fan or angular probabilities.

The two Gaussian vectors have independent \(N(0,1)\) coordinates, and each has a unique exposed vertex almost surely. The probability \(C(G)\) is their same-vertex collision probability; it is also the sum of the squared spherical measures of all vertex normal cones. No claim is made about nonisomorphic trees with more than eight vertices or about arbitrary non-tree graphs.

## Proof

**First, face numbers.** The standard tubing-face correspondence states that a compatible family of \(k\) distinct proper tubes indexes exactly one face of dimension \(7-k\) of a graph associahedron on eight graph vertices. This follows from the nested-set model of graph associahedra and is recalled in Cardinal--Langerman--Pérez-Lantero (2018, Section 2.2).

The exhaustive exact enumeration in `verify.py` loops over every nonempty proper subset of eight vertices, retains precisely those inducing a connected subgraph, and forms every compatible tube family by recursive clique enumeration on the compatibility graph. For each of \(G_A,G_B\), the numbers of families of sizes \(k=0,1,\ldots,7\) are precisely

\[
(1,52,676,3680,10010,14336,10332,2952).
\]

Reversing this list gives the asserted face vector. This enumerates all potential tube families, without sampling or extrapolation.

**Second, angular probabilities.** Every strict coordinate ordering has probability \(1/8!\) under the isotropic Gaussian law. Let \(\pi\) be a permutation listed from highest to lowest objective coordinate. Its unique maximizing vertex for the simplex sum is the explicit integer vector

\[
x_G(\pi)=\sum_{\substack{\varnothing\ne S\subseteq V(G)\\G[S]\text{ connected}}}
e_{\operatorname{first}_{\pi}(S)},
\]

where \(\operatorname{first}_{\pi}(S)\) is the first vertex of \(S\) in order \(\pi\). This equality holds because the support function of a Minkowski sum is the sum of the support functions of its summands; each summand has a uniquely maximizing coordinate for a generic direction.

For each exposed vertex \(x\), set \(N_G(x)=|\{\pi\in S_8:x_G(\pi)=x\}|\). Consequently

\[
C(G)=\frac{1}{(8!)^2}\sum_x N_G(x)^2.
\]

The independently written direct-permutation part of `verify.py` enumerates all \(40320\) orders separately for each graph, evaluates the full coordinate vector \(x_G(\pi)\) from all connected subsets, and counts equal vectors by exact integer arithmetic. It finds precisely \(2952\) distinct exposed points for each graph and obtains, as reduced rational numbers, \(14239/4838400\) and \(76393/33868800\). Subtraction gives \(97/141120\), and no equality of distinct exposed points is assumed rather than checked.

**Third, minimality and uniqueness.** Every labeled tree on \(n\ge2\) vertices occurs exactly once among the \(n^{n-2}\) Prüfer sequences of length \(n-2\). The checker enumerates all such sequences for \(1\le n\le8\), groups the resulting trees by their center-rooted canonical unordered-tree encodings, and obtains respectively

\[
1,1,1,2,3,6,11,23
\]

unlabeled trees for these successive orders. For each representative, it computes the number \(V(G)\) of elimination trees through the exact rooted recursion

\[
V(\varnothing)=1,\qquad
V(G)=\sum_{v\in V(G)}\prod_{K\in\operatorname{Comp}(G-v)}V(K),
\]

with the single-vertex case normalized to \(V=1\). Elimination trees correspond bijectively to graph-associahedron vertices (Cardinal--Merino--Mütze, 2021). For every order \(n\le7\), these vertex numbers are pairwise distinct among nonisomorphic trees. At \(n=8\), the only repeated number is \(2952\), occurring on exactly the two displayed tree isomorphism classes. Any equal face vector would in particular require equal vertex numbers; therefore no pair exists below eight and the displayed pair is the unique eight-vertex candidate. The tube and angle calculations finish the proof.

As an additional independent consistency check, `verify.py` also computes Gaussian collision probabilities by the elimination-root recursion

\[
C(G)=\frac{1}{|V(G)|^2}\sum_{v\in V(G)}
\prod_{K\in\operatorname{Comp}(G-v)}C(K),\qquad C(\varnothing)=1,
\]

which follows by conditioning two independent uniform coordinate rankings on their common first vertex. The recursion agrees exactly with the direct \(8!\)-permutation calculation for both graphs.

## Verification

Run `python3 verify.py` with a recent Python 3 interpreter. The checker has no third-party dependencies and uses exact integers and `fractions.Fraction`; its declared graphs and expected rational assertions are visible in the source. It checks the complete face vectors by all compatible tubings, the collision fractions by all coordinate rankings, a second independent elimination recursion, all unlabeled-tree isomorphism classes through eight vertices by Prüfer codes and canonical tree encodings, and the exact uniqueness/minimality assertions. Its terminating output is `ALL EXACT CHECKS PASSED`.

The computation is finite and exhaustive over precisely the stated domains; no claim of an infinite-tree classification follows from it. The mathematical reductions to tubings, support functions, and Prüfer codes are explicitly stated above so the certificate is more than an unexplained computation log.

## Relationship to prior work

Graph associahedra, their tubing-face correspondence, and the description of vertices as elimination/search trees are established mathematics, used here as inputs and not claimed as discoveries. Cardinal--Langerman--Pérez-Lantero (2018) study rotation diameter for trees and explicitly explain tube compatibility; Cardinal--Merino--Mütze (2021) provide comprehensive elimination-tree generation theory. The path-graph special case of collision counting is the classical random binary-search-tree equality problem studied by Chern and collaborators; this work does not claim that general principle as new.

The present concrete contribution is the **least-order face-vector-twin counterexample distinguished by Gaussian normal-cone collisions**, with the exact values, complete face vectors, and an exhaustive minimality certificate. Existing standard tubing and elimination recurrences are used to make these claims checkable; their existence alone does not determine the two explicit angular moments or this finite threshold.

## Limitations

The threshold is only among tree graph associahedra and only for equality of full face vectors with difference in the specified Gaussian collision probability. Equal face vectors do not imply that the polytopes are combinatorially isomorphic; no such stronger equivalence is asserted. This is a finite exact result, not an asymptotic theorem. Other constructions or earlier computations under alternate terminology may already contain related examples; the literature comparison does not constitute proof of global priority. Independent external mathematical validation has not been performed.

## References

1. J. Cardinal, S. Langerman, P. Pérez-Lantero, *On the Diameter of Tree Associahedra*, arXiv:1803.11427v1, March 30, 2018, especially Section 2.2, https://arxiv.org/abs/1803.11427.
2. J. Cardinal, A. Merino, T. Mütze, *Combinatorial generation via permutation languages. IV. Elimination trees*, arXiv:2106.16204v1, June 30, 2021, especially Sections 1–3 and 7, https://arxiv.org/abs/2106.16204.
3. J. Cardinal, L. Pournin, M. Valencia-Pabon, *Diameter Estimates for Graph Associahedra*, arXiv:2106.16130v1, June 30, 2021, https://arxiv.org/abs/2106.16130.
4. H.-H. Chern, M.-I. Fernández-Camacho, H.-K. Hwang, C. Martínez, *Psi-series method for equality of random trees and quadratic convolution recurrences*, Random Structures & Algorithms 44 (2014), 67–108, https://doi.org/10.1002/rsa.20428. (Path/BST equality precedent; not the pair of tree graph associahedra.)
