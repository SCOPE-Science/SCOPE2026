# Power domination polynomials of spider trees and extremal arm balances
## Finding
Let \(T=S(\ell_1,\ldots,\ell_k)\) be a spider tree with center \(c\), \(k\ge3\) arms, positive arm lengths \(\ell_i\), and \(L=\sum_i\ell_i\). A set \(S\subseteq V(T)\) is power dominating if and only if either \(c\in S\) or \(S\) meets at least \(k-1\) arms. Consequently, writing \(A_i(x)=(1+x)^{\ell_i}-1\), the power domination polynomial is \[\mathcal P(T;x)=x(1+x)^L+\prod_{i=1}^k A_i(x)+\sum_{i=1}^k\prod_{j\ne i}A_j(x).\] For fixed \(L\) and \(k\), and for every real \(x>0\), this polynomial is uniquely maximized, up to arm permutation, when the arm lengths differ by at most one, and uniquely minimized when the arm-length multiset is \(\{{1,\ldots,1,L-k+1\}}\). In particular the same unique extremizers hold for the total number of power dominating sets, obtained at \(x=1\).

## Assumptions and scope
A spider tree is a finite tree with a center vertex \(c\) of degree \(k\ge3\) such that deleting \(c\) leaves \(k\) paths. The center-to-leaf paths are the arms, and arm \(i\) has \(\ell_i\ge1\) edges. A power domination process starts from a chosen set \(S\), first observes the closed neighborhood \(N[S]\), and then repeatedly applies the zero-forcing rule: an observed vertex with exactly one unobserved neighbor observes that neighbor. A set is power dominating when eventually every vertex is observed.

The result concerns arbitrary positive arm lengths. The extremal statement fixes both the number of arms \(k\) and total arm length \(L\).

## Proof
First classify all power dominating sets.

If \(c\in S\), then the domination step observes the first vertex of every arm. Each arm is a path extending away from the center, so the forcing rule propagates independently along every arm until all vertices are observed.

Now suppose \(c\notin S\). If \(S\) meets at least \(k-1\) arms, every met arm propagates toward the center and outward along its path. Thus the center becomes observed. At that stage there is at most one completely untouched arm, so the center has at most one unobserved neighbor and, if necessary, forces into that last arm; propagation then finishes the graph.

Conversely, suppose \(c\notin S\) and \(S\) meets at most \(k-2\) arms. Then at least two arms contain no selected vertex. No vertex in either untouched arm can be observed before the center is observed. When the center first becomes observed, it has at least two unobserved neighbors, namely the first vertices of those untouched arms, so it cannot force into either one. No other observed vertex is adjacent to them. The process therefore stalls. This proves the characterization.

For counting, let
\[
A_i(x)=(1+x)^{\ell_i}-1,
\]
so \(A_i(x)\) is the generating polynomial for a nonempty choice from arm \(i\). Center-containing sets contribute \(x(1+x)^L\). Center-free power dominating sets either meet all arms, contributing \(\prod_i A_i(x)\), or omit exactly one arm, contributing \(\sum_i\prod_{j\ne i}A_j(x)\). This gives the displayed formula. At \(x=1\), the total number is
\[
2^L+\prod_i(2^{\ell_i}-1)+\sum_i\prod_{j\ne i}(2^{\ell_j}-1).
\]

It remains to prove the extremal statement. Fix \(x>0\), put \(t=1+x>1\), and define \(u_m=t^m-1\). The center-containing term \(xt^L\) is fixed when \(L\) is fixed. Hold all arm lengths except two, say \(a,b\), fixed. Let
\[
C=\prod_{h\ne a,b}u_{\ell_h}>0,
\qquad
R=\sum_{h\ne a,b}\frac1{u_{\ell_h}}>0.
\]
The part of the center-free contribution depending on \(a,b\) is
\[
C\big((1+R)u_a u_b+u_a+u_b\big).
\]
For fixed \(s=a+b\), set \(X=t^a+t^b\). Since \(u_a u_b=t^s-X+1\) and \(u_a+u_b=X-2\), this expression becomes
\[
C\big((1+R)(t^s+1)-2-RX\big),
\]
which is strictly decreasing in \(X\).

If \(a\ge b+2\), balancing to \(a-1,b+1\) strictly decreases \(X\), because
\[
(t^a+t^b)-(t^{a-1}+t^{b+1})=(t-1)(t^{a-1}-t^b)>0.
\]
Hence every nontrivial balancing step strictly increases \(\mathcal P(T;x)\). Repeating reaches exactly the arm-length multisets whose entries differ by at most one, proving the unique maximum up to arm permutation.

If \(a\ge b\ge2\), concentrating to \(a+1,b-1\) strictly increases \(X\), since
\[
(t^{a+1}+t^{b-1})-(t^a+t^b)=(t-1)(t^a-t^{b-1})>0.
\]
Thus every concentration step strictly decreases the polynomial. Repeating until all but one parts equal one yields the unique minimum \(\{1,\ldots,1,L-k+1\}\).

## Verification
The included checker builds each spider as an ordinary graph and runs the power domination process directly from the definition. It exhaustively tests every vertex subset for 432 spider types with three to five arms, arm lengths from one through four, and at most ten arm edges. This checks 483,024 vertex subsets against both the structural characterization and the coefficient formula.

A separate exact-rational check enumerates 1,392 arm-size partitions for total arm length through twenty and three to six arms, and confirms the unique balanced maximum and concentrated minimum at \(x\in\{1/2,1,2\}\). These finite checks are corroborative; the theorem for all positive real \(x\) follows from the strict transfer argument above.

## Relationship to prior work
Brimkov, Patel, Suriyanarayana, and Teich introduced the power domination polynomial and developed decomposition tools together with explicit formulas for standard families including paths, cycles, wheels, stars, complete graphs, and selected coronas. Their path-attachment decomposition explicitly excludes attaching a path at an endpoint, so it does not directly cover a spider formed by identifying path endpoints at a common center. Their star formula is recovered here as the special case \(\ell_1=\cdots=\ell_k=1\).

Varghese, Varghese, and Vijayakumar study power domination for spiders in the setting of Mycielskian graphs and note the minimum power domination behavior of spiders, but do not enumerate all power dominating sets of arbitrary spiders. A later paper on domination- and power-domination-polynomial entropy develops additional named graph families; the inspected text contains no spider family. Targeted searches for “power domination polynomial” together with “spider,” “starlike tree,” “subdivided star,” and equivalent counting phrases did not locate the all-set formula or the arm-balance extremal theorem above.

## Limitations
The extremal comparison fixes both \(L\) and \(k\), and it is specific to spider trees. The theorem does not claim an extremal ordering among arbitrary trees. The exhaustive computations cover bounded instances only and do not replace the symbolic proof. Literature searches cannot exclude differently phrased or non-indexed prior work.

## References
1. B. Brimkov, R. Patel, V. Suriyanarayana, A. Teich, “Power domination polynomials of graphs,” arXiv:1805.10984v1 (2018).
2. S. Varghese, S. Varghese, A. Vijayakumar, “Power domination in Mycielskian of spiders,” AKCE International Journal of Graphs and Combinatorics (2022), DOI 10.1080/09728600.2022.2082900.
3. K. Geethu, A. Parthiban, “On Graph Entropy Measures Based on the Number of Dominating and Power Dominating Sets,” Malaysian Journal of Mathematical Sciences 19 (2025), DOI 10.47836/mjms.19.1.14.
