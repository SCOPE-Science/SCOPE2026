# Doubly resolving bases of crown graphs

## Finding
For every integer \(n\ge 3\), let \(\operatorname{Cr}_n\) be the crown graph with bipartition
\[
A=\{a_1,\ldots,a_n\},\qquad B=\{b_1,\ldots,b_n\},
\]
and edges \(a_i b_j\) exactly when \(i\ne j\). Write \(P_i=\{a_i,b_i\}\) for the deleted matched pair. Then
\[
\psi(\operatorname{Cr}_n)=
\begin{cases}
n,&3\le n\le6,\\
n-1,&n\ge7.
\end{cases}
\]
Here \(\psi(G)\) is the minimum cardinality of a doubly resolving set: a set \(S\subseteq V(G)\) such that, for every distinct \(u,v\), the values \(d(u,s)-d(v,s)\) are not constant as \(s\) ranges over \(S\).

The minimum sets can be classified completely. If \(n\ge7\), every basis omits exactly one pair \(P_r\), contains exactly one vertex from every other \(P_i\), and has at least three selected vertices in each of \(A\) and \(B\). Hence the number of bases is
\[
n\left(2^{n-1}-2\left(1+(n-1)+\binom{n-1}{2}\right)\right).
\]
If \(3\le n\le6\), every basis has size \(n\) and is of exactly one of the following two types:

1. one pair \(P_r\) is omitted, a distinct pair \(P_s\) is doubled, and every remaining pair contributes exactly one vertex;
2. every pair contributes exactly one vertex, and the number of selected vertices in \(B\) is neither \(2\) nor \(n-2\).

Therefore the number of bases for \(3\le n\le6\) is
\[
n(n-1)2^{n-2}+2^n-\binom n2\left(2-\mathbf 1_{\{n=4\}}\right).
\]
For \(n=3,4,5,6\), these counts are respectively \(14,58,172,514\).

## Assumptions and scope
Graphs are finite, simple, undirected, and connected. The theorem is for crown graphs \(\operatorname{Cr}_n\) with \(n\ge3\); thus the graph has \(2n\) vertices. The term “basis” means a doubly resolving set of minimum cardinality, not an inclusion-minimal set of arbitrary size.

The distance structure used below is
\[
d(a_i,a_j)=d(b_i,b_j)=2\quad(i\ne j),
\]
\[
d(a_i,b_i)=3,
\qquad
d(a_i,b_j)=1\quad(i\ne j).
\]

## Proof
For distinct vertices \(u,v\), define
\[
\delta_{u,v}(s)=d(u,s)-d(v,s).
\]
A set \(S\) doubly resolves \(u,v\) exactly when \(\delta_{u,v}\) is nonconstant on \(S\).

First consider \(a_i,a_j\) with \(i\ne j\). Directly from the distance table,
\[
\delta_{a_i,a_j}(s)=
\begin{cases}
-2,&s\in\{a_i,b_j\},\\
 2,&s\in\{a_j,b_i\},\\
 0,&\text{otherwise}.
\end{cases}
\]
If both \(P_i\) and \(P_j\) are omitted from \(S\), this difference is identically zero on \(S\), so \(S\) is not doubly resolving. Consequently every doubly resolving set omits at most one matched pair. In particular,
\[
|S|\ge n-1.
\]
For all candidate sets occurring below, \(|S|\ge3\); with at most one omitted pair, the displayed three-valued formula also shows that every same-side pair is doubly resolved.

Next consider the matched nonedge \(a_i,b_i\). Its difference profile is
\[
\delta_{a_i,b_i}(s)=
\begin{cases}
-3,&s=a_i,\\
 3,&s=b_i,\\
 1,&s=a_k\text{ with }k\ne i,\\
-1,&s=b_k\text{ with }k\ne i.
\end{cases}
\]
Thus, if \(P_i\) is omitted, the pair \(a_i,b_i\) is doubly resolved exactly when \(S\) meets both bipartition sides. If \(P_i\) is represented, then any other selected vertex supplies a different difference value, so this pair causes no further obstruction in the candidate sizes considered here.

Finally take an adjacent cross pair \(a_i,b_j\) with \(i\ne j\). Then \(\delta_{a_i,b_j}\) takes only the values \(-1\) and \(1\):
\[
L^-(i,j)=\{a_i,a_j\}\cup\{b_k:k\notin\{i,j\}\}
\]
is exactly its \(-1\) level set, while
\[
L^+(i,j)=\{b_i,b_j\}\cup\{a_k:k\notin\{i,j\}\}
\]
is exactly its \(1\) level set. Each of \(L^-(i,j)\) and \(L^+(i,j)\) is a transversal of the matched pairs \(P_1,\ldots,P_n\). Therefore \(a_i,b_j\) fails to be doubly resolved by \(S\) exactly when \(S\subseteq L^-(i,j)\) or \(S\subseteq L^+(i,j)\).

Suppose now that \(|S|=n-1\). The lower-bound argument forces exactly one omitted pair, say \(P_r\), and exactly one selected vertex from every other pair. Let \(p\) and \(q\) be the numbers selected from \(A\) and \(B\), so \(p+q=n-1\). The omitted matched pair requires \(p,q\ge1\). If \(\min\{p,q\}=1\), choose the adjacent cross pair whose indices are the omitted index and the unique index represented on the minority side; then \(S\) lies in one of the two level transversals above. If \(\min\{p,q\}=2\), choose the adjacent cross pair indexed by those two minority-side indices; again \(S\) lies in a level transversal. Conversely, if \(p,q\ge3\), neither level transversal can contain \(S\): after deletion of one pair, any such level transversal has a minority side of size at most two. Hence
\[
|S|=n-1\text{ is doubly resolving}\quad\Longleftrightarrow\quad p\ge3\text{ and }q\ge3.
\]
This is possible exactly when \(n-1\ge6\), that is, \(n\ge7\). The lower bound is therefore attained precisely for \(n\ge7\), proving \(\psi(\operatorname{Cr}_n)=n-1\) in that range. Choosing the omitted pair and then a binary orientation on the remaining \(n-1\) pairs, excluding orientations with at most two vertices on either side, gives
\[
n\left(2^{n-1}-2\left(1+(n-1)+\binom{n-1}{2}\right)\right)
\]
bases.

For \(3\le n\le6\), no size-\(n-1\) set can have three selected vertices on both sides, so \(\psi(\operatorname{Cr}_n)\ge n\). We classify the size-\(n\) doubly resolving sets. Since at most one matched pair can be omitted, either exactly one pair is omitted, in which case exactly one distinct pair is doubled and all others are singletons, or no pair is omitted, in which case the set is a transversal.

In the first case the doubled pair contributes vertices from both sides, so the omitted matched pair is resolved; moreover, a set containing both vertices of one pair cannot lie inside either cross-pair level transversal, because every such level transversal contains exactly one vertex from each matched pair. Hence every set of the first type is doubly resolving.

In the second case, a transversal equals some \(L^+(i,j)\) exactly when its selected \(B\)-indices are \(\{i,j\}\), and it equals some \(L^-(i,j)\) exactly when its selected \(B\)-indices are the complement of \(\{i,j\}\). Thus a transversal is doubly resolving exactly when its number of selected \(B\)-vertices is neither \(2\) nor \(n-2\). This proves the classification. There are \(n(n-1)2^{n-2}\) first-type bases. The number of valid transversals is
\[
2^n-\binom n2\left(2-\mathbf 1_{\{n=4\}}\right),
\]
because the two excluded Hamming-weight layers coincide only when \(n=4\). Adding the two terms proves the stated count.

## Verification
A standalone checker in `verify.py` constructs \(\operatorname{Cr}_n\), computes all-pairs distances by breadth-first search, tests the defining difference condition for every vertex pair, and compares the resulting minimum sets with the theorem’s structural classifier. It exhausts every subset smaller than the claimed optimum and every subset at the claimed optimum for \(3\le n\le9\). Its expected terminal line is:

`VERIFY_OK n_range=3..9 subset_checks=142833 basis_checks=59467 bases=3096 max_order=18`

This finite computation is corroborative. The infinite statement for all \(n\ge3\) is established by the proof above, not by extrapolation from the computation.

## Relationship to prior work
Cáceres, Hernando, Mora, Pelayo, Puertas, Seara, and Wood introduced doubly resolving sets in their study of Cartesian-product metric dimension and denoted the minimum size by \(\psi(G)\). Their paper develops the parameter for complete graphs, Hamming graphs, paths and grids, cycles, and trees; the inspected full text does not treat crown graphs, complete bipartite graphs, or matching-deleted graphs.

Liu, Zafari, and Zarei determine minimum doubly resolving sets for cocktail-party graphs. A cocktail-party graph is a complete graph with a perfect matching deleted, whereas \(\operatorname{Cr}_n\) is a complete bipartite graph with a perfect matching deleted. The former has diameter two and the latter has diameter three, so their theorem does not imply the crown classification.

Nizami studies the ordinary metric dimension of crown graphs and their subdivisions. Ordinary resolving sets are weaker than doubly resolving sets, so that result does not imply the theorem here. A later paper on strong and doubly metric dimensions of Johnson and Kneser graphs treats ordinary Kneser graphs rather than the bipartite Kneser realization of crown graphs, and likewise does not cover this statement.

## Limitations
The theorem concerns the exact minimum size, complete basis structure, and basis counts for \(\operatorname{Cr}_n\); it does not enumerate all nonminimum doubly resolving sets. The computational checker is exhaustive only through \(n=9\) and is not a certificate for larger \(n\). The literature comparison cannot exclude an unindexed source using an uncommon synonym for doubly resolving sets or crown graphs; focused searches under “crown graph,” “complete bipartite graph minus a perfect matching,” “bipartite Kneser graph,” “doubly resolving,” “double metric dimension,” and closely related formulations did not reveal a covering result.

## References
1. J. Cáceres, C. Hernando, M. Mora, I. M. Pelayo, M. L. Puertas, C. Seara, and D. R. Wood, *On the Metric Dimension of Cartesian Products of Graphs*, arXiv:math/0507527, first public version 26 July 2005; SIAM Journal on Discrete Mathematics 21(2), 423–441 (2007), DOI 10.1137/050641867.
2. J.-B. Liu, A. Zafari, and H. Zarei, *Metric Dimension, Minimal Doubly Resolving Sets, and the Strong Metric Dimension for Jellyfish Graph and Cocktail Party Graph*, Complexity (2020), Article 9407456, DOI 10.1155/2020/9407456.
3. A. R. Nizami, *Invariance of metric dimension of subdivision of the crown graph*, Journal of Prime Research in Mathematics 14(1), 18–23 (2018).
4. J. Kratica et al., *The strong and doubly metric dimensions of Johnson and Kneser graphs*, arXiv:2605.06837 (2026).
