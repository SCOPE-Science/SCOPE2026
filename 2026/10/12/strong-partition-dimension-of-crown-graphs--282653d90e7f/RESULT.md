# Strong partition dimension of crown graphs
## Finding
For every integer \(n\ge3\), let \(\operatorname{Cr}_n\) be the crown graph with bipartition
\[
A=\{a_1,\ldots,a_n\},\qquad B=\{b_1,\ldots,b_n\},
\]
and with \(a_i\) adjacent to \(b_j\) exactly when \(i\ne j\). Then
\[
\operatorname{pd}_s(\operatorname{Cr}_n)=n.
\]
A stronger counting statement drives the lower bound: if a strong resolving partition has \(q\) parts meeting \(A\), then it has at least \(n-q\) additional singleton parts of the form \(\{b_i\}\).

## Assumptions and scope
For a nonempty vertex set \(W\), write \(d(x,W)=\min_{w\in W}d(x,w)\). A set \(W\) strongly resolves two vertices \(x,y\notin W\) when either
\[
d(x,W)=d(x,y)+d(y,W)
\]
or the same equality holds with \(x\) and \(y\) exchanged. A vertex partition is strong resolving when every two vertices in the same part are strongly resolved by another part. Its minimum number of parts is \(\operatorname{pd}_s\).

Only finite simple crown graphs with \(n\ge3\) are considered. The proof does not use computation.

## Proof
The crown distances from \(a_i\) are
\[
d(a_i,b_i)=3,\qquad d(a_i,b_j)=1\ (j\ne i),\qquad d(a_i,a_j)=2\ (j\ne i).
\]
In particular, \(b_i\) is the unique vertex at distance \(3\) from \(a_i\).

Let \(\Pi\) be any strong resolving partition. Consider one part \(U\in\Pi\) containing \(r\ge2\) vertices \(a_i\), with index set \(I\). For distinct \(i,j\in I\), the pair \(a_i,a_j\) has distance \(2\). Any part \(W\ne U\) that strongly resolves this pair must therefore have set-distances \(1\) and \(3\): distances \(0\) cannot occur because \(W\) is disjoint from \(U\), and no larger difference is available in the crown graph. Since \(b_i\) is the unique vertex at distance \(3\) from \(a_i\), the equality \(d(a_i,W)=3\) forces \(W=\{b_i\}\); symmetrically, \(d(a_j,W)=3\) forces \(W=\{b_j\}\). Hence for every pair \(i,j\in I\), at least one of \(\{b_i\}\) or \(\{b_j\}\) is a singleton part of \(\Pi\). Equivalently, among the indices in \(I\), at most one can have its matched \(b\)-vertex in a nonsingleton part. Thus \(U\) forces at least \(r-1\) distinct singleton \(B\)-parts.

Let \(q\) be the number of parts of \(\Pi\) meeting \(A\), and let their \(A\)-occupancies be \(r_1,\ldots,r_q\). The index sets are disjoint and \(r_1+\cdots+r_q=n\). The preceding paragraph yields at least
\[
\sum_{t=1}^q(r_t-1)=n-q
\]
distinct singleton parts from \(B\). None of them meets \(A\), so \(|\Pi|\ge q+(n-q)=n\).

For the matching upper bound, take
\[
U_0=\{a_1,\ldots,a_{n-1},b_n\},\qquad U_1=\{a_n,b_1\},
\]
and singleton parts \(\{b_i\}\) for \(2\le i\le n-1\). There are exactly \(n\) parts. If \(a_i,a_j\in U_0\), one of \(i,j\) lies in \(\{2,\ldots,n-1\}\), and its singleton matched vertex has distances \(3\) and \(1\) to the pair. If \(a_i,b_n\in U_0\) with \(i\ge2\), the singleton \(\{b_i\}\) has distances \(3\) and \(2\), while for \(i=1\) the singleton \(\{b_2\}\) has distances \(1\) and \(2\). Finally, \(\{b_2\}\) has distances \(1\) and \(2\) to the pair \(a_n,b_1\in U_1\). Each displayed difference is exactly the distance of the paired vertices, so every nonsingleton part is strongly resolved. Therefore \(\operatorname{pd}_s(\operatorname{Cr}_n)\le n\), completing the proof.

## Verification
The accompanying checker independently builds crown-graph distance matrices, verifies the displayed \(n\)-part construction for \(3\le n\le12\), and exhaustively enumerates all set partitions with fewer than \(n\) parts for \(n=3,4,5\). It also finds a valid \(n\)-part partition in each of those exhaustive cases. The replay output is:

`VERIFY_OK construction_n=3..12 exhaustive_n=3..5 partitions_tested=45148 construction_checks=10`

These computations are stress tests only; the theorem for all \(n\ge3\) follows from the proof above.

## Relationship to prior work
Strong partition dimension was introduced by González Yero. The foundational paper gives the general bounds
\[
\omega(G_{SR})\le \operatorname{pd}_s(G)\le \alpha(G_{SR})+1
\]
and notes that a \(2\)-antipodal graph has strong resolving graph equal to a disjoint union of edges. A crown graph is \(2\)-antipodal, so these results give only
\[
2\le \operatorname{pd}_s(\operatorname{Cr}_n)\le n+1.
\]
The exact value \(n\) therefore does not follow from those bounds. The later product-graph paper studies strong and Cartesian graph products and reuses the same general strong-resolving-graph bounds; it does not supply a matching-deleted complete-bipartite calculation.

Targeted searches under the aliases “crown graph”, “complete bipartite minus perfect matching”, “matching-deleted complete bipartite”, and “strong resolving partition” did not locate a prior statement of the theorem above.

## Limitations
The result concerns the scalar strong partition dimension only. It does not classify or enumerate all minimum strong resolving partitions; exhaustive checks show that many nonisomorphic-looking minimum partitions already occur for small \(n\). Search failure is not a proof of novelty, and an unindexed or differently named source could still exist.

## References
1. I. González Yero, *On the strong partition dimension of graphs*, arXiv:1312.1987, first public version 6 December 2013; later published in *The Electronic Journal of Combinatorics* 21(3), P3.14 (2014), DOI: 10.37236/3474.
2. I. G. Yero, D. Kuziak, J. A. Rodríguez-Velázquez, *Strong resolving partitions for strong product graphs and Cartesian product graphs*, *Discrete Applied Mathematics* 202 (2016), 70–78, DOI: 10.1016/j.dam.2015.08.026.
