# Power-domination polynomial and factor rigidity of tensor products of complete graphs

## Finding

For integers \(m,n\ge 4\), write \(G_{m,n}=K_m\times K_n\), where \(\times\) denotes the **direct (tensor/categorical)** graph product, not the Cartesian product. Every power-dominating subset \(S\subseteq V(G_{m,n})\) is characterized exactly by one of these mutually compatible tests: the selected vertices meet at least two rows and at least two columns; or \(S\) lies in one row and \(|S|\ge n-2\); or \(S\) lies in one column and \(|S|\ge m-2\). The latter two cases include no singleton when \(m,n\ge4\).

Consequently, with \(\mathcal P(G;z)=\sum_{S\text{ power dominating}}z^{|S|}\),

\[
\boxed{\mathcal P(G_{m,n};z)=(1+z)^{mn}-1-mnz
 -m\sum_{k=2}^{n-3}\binom nk z^k
 -n\sum_{k=2}^{m-3}\binom mk z^k.}
\]

Empty sums are zero. In particular,

\[
\gamma_P(G_{m,n})=2,\qquad
p(G_{m,n};2)=2\binom m2\binom n2
+\mathbf 1_{\{n=4\}}m\binom n2
+\mathbf 1_{\{m=4\}}n\binom m2.
\]

The entire polynomial also determines the unordered pair \(\{m,n\}\) **within this family**. Indeed let \(N\) be its degree and define
\[
L=\max\Big\{k\in\{0,\ldots,N\}: [z^k]\mathcal P(G_{m,n};z)<\binom Nk\Big\}.
\]
Then \(N=mn\) and \(L=\max(m,n)-3\). Thus the larger factor equals \(L+3\), and the smaller is \(N/(L+3)\). No polynomial uniqueness among arbitrary graphs is asserted.

## Assumptions and scope

The vertex set is \([m]\times[n]\). Distinct vertices \((i,j)\), \((i',j')\) are adjacent if and only if \(i\ne i'\) and \(j\ne j'\). A row fixes \(i\); a column fixes \(j\). A set \(S\) power dominates if, after initially observing all vertices in the closed neighborhood \(N[S]\), repeatedly observing the unique unobserved neighbor of any observed vertex eventually observes every vertex. Propagation may be performed simultaneously or one vertex at a time; the terminal closure is the same. Throughout, both \(m\) and \(n\) are integers at least four. For coefficients \([z^k]\), all vertices are distinguishable and no quotient by automorphisms is taken.

## Proof

**Step 1 (a diagonal pair suffices).** Suppose \(S\) contains \((r,c)\) and \((s,d)\) with \(r\ne s\), \(c\ne d\). The closed neighborhoods of these two vertices initially observe all but at most \((r,d)\) and \((s,c)\): a vertex that fails adjacency to the first belongs to its row or column, and to fail adjacency to the second simultaneously it must be one of these two cross-corners (the initially selected endpoints themselves are observed). Choose \(u\notin\{r,s\}\). The vertices \((u,c)\) and \((u,d)\) are already observed. Of the two possibly missing corners, \((u,c)\) is adjacent only to \((r,d)\), while \((u,d)\) is adjacent only to \((s,c)\). Thus each has at most one unobserved neighbor and forces its missing corner, if any. Hence every set containing a diagonal pair power dominates.

A subset meets at least two rows and at least two columns if and only if it contains a diagonal pair. Indeed, otherwise, after taking two vertices in different rows, all vertices would be forced into their common column; this contradicts meeting two columns. The converse is immediate.

**Step 2 (one-row sets).** Let \(S\) contain \(k\ge2\) vertices in a single row \(r\), with distinct selected columns. Every vertex outside row \(r\) is initially observed, since it is adjacent to a selected vertex in a different column. The only unobserved vertices are the \(u=n-k\) unselected vertices of row \(r\). Every observed vertex outside row \(r\) has either \(u\) or \(u-1\) unobserved neighbors, according as its column is selected or unselected among the \(u\) omitted columns. Every observed vertex in row \(r\) has none. If \(u\ge3\), no forcing move exists, so \(S\) fails. If \(u\le1\), the process already finishes or an observed vertex outside row \(r\) has exactly one unobserved neighbor. If \(u=2\), a vertex outside row \(r\) in one of the two omitted columns forces the other omitted row vertex; thereafter the last is forced. Therefore a one-row set with \(k\ge2\) power dominates exactly when \(k\ge n-2\). Interchanging the coordinates gives the one-column condition \(k\ge m-2\).

**Step 3 (singletons and empty sets).** Starting at one vertex \((r,c)\), the \(n-1\) other vertices in row \(r\) and the \(m-1\) other vertices in column \(c\) remain unobserved after the initial domination step. An observed vertex outside that row and column has \((n-2)+(m-2)\ge4\) unobserved neighbors; the initial vertex has none. Consequently no force is possible. The empty set fails as well.

Together these steps prove the stated necessary-and-sufficient classification.

**Step 4 (enumeration).** There are \(2^{mn}\) vertex subsets altogether. The failed ones are the empty set, all \(mn\) singletons, each size-\(k\) subset of a single row for \(2\le k\le n-3\), and each size-\(k\) subset of a single column for \(2\le k\le m-3\). For \(k\ge2\), no failed row subset can equal a failed column subset and no two distinct fibers share such a subset. These disjoint categories yield the polynomial by subtraction. Every two-vertex set meeting two rows and columns dominates, so \(\gamma_P=2\). There are exactly two diagonal pairs in each chosen \(2\times2\) rectangle. In addition, a two-vertex one-row set succeeds exactly when \(n=4\), and a one-column pair succeeds exactly when \(m=4\). This gives the minimum-set count.

**Step 5 (factor reconstruction).** The coefficient deficit \(\binom{mn}{k}-[z^k]\mathcal P(G_{m,n};z)\) equals the number of failed size-\(k\) subsets. Its largest nonzero index is \(L=\max(n-3,m-3,1)=\max(m,n)-3\), since both factors are at least four. The polynomial degree is \(mn\) because the entire vertex set power dominates. The two factors are recovered as asserted, including the equal-factor case.

## Verification

Run `python3 verification/verify_power_direct_product.py` from the package root. The standalone checker constructs the tensor-product adjacency relation directly, performs the initial domination and iterative unique-neighbor closure, and compares this independently with the structural characterization. It exhaustively tests all \(2^{16}+2\cdot2^{20}=2{,}162{,}688\) subsets on \((m,n)=(4,4),(4,5),(5,4)\), and further tests \(34{,}503\) sampled or two-vertex candidates over nine larger parameter pairs. It independently compares the resulting exact cardinality histograms with the polynomial for the three exhaustive boards and verifies the degree and minimum-set formulas on the additional boards. The recorded deterministic output is in `verification/output.txt`. Finite enumeration checks boundary cases but does not replace the proof for unbounded \(m,n\).

## Relationship to prior work

The standard power-domination polynomial and its coefficient definition were developed by Brimkov, Patel, Suriyanarayana and Teich (first publicly posted 28 May 2018). Their decomposition theorems and the families handled in the explicit-polynomial section do not give this direct-product family. In particular, the join formula is inapplicable: \(G_{m,n}\) is not a nontrivial join, since its complement, the connected rook graph \(K_m\square K_n\), is connected.

Dorbec, Mollard, Klavžar and Špacapan studied power domination of graph products, treating the numerical parameters of direct products of paths, strong products of paths and lexicographic products. Their direct-product operation is the same operation as here, but their direct-product factor family consists of paths, not complete graphs, and their study does not establish this complete cardinality enumerator. The ordinary domination bounds for direct products of Brešar, Klavžar and Rall are for a distinct invariant. Some literature denotes the **Cartesian** product of complete graphs with the same cross symbol; its adjacency condition is the opposite of the direct-product adjacency used here and such results do not imply this theorem. The residual possibility of an undiscovered identical enumerator is acknowledged.

## Limitations

The result is restricted to the direct products of two complete graphs with both factor orders at least four. Smaller factors, directed or looped graph conventions, and other graph products are not covered. It does not assert global characterization among all graphs by the power-domination polynomial. Computational tests are finite. Originality is assessed against the accessible sources described here and may require independent bibliographic review.

## References

1. B. Brimkov, R. Patel, V. Suriyanarayana and A. Teich, *Power domination polynomials of graphs*, arXiv:1805.10984, 28 May 2018. https://arxiv.org/abs/1805.10984
2. P. Dorbec, M. Mollard, S. Klavžar and S. Špacapan, *Power Domination in Product Graphs*, SIAM Journal on Discrete Mathematics 22 (2008), 554–567. https://doi.org/10.1137/060661879
3. C. Benson, D. Ferrero, M. Flagg, M. Furst, L. Hogben, V. Vasilevska and B. Wissman, *Power domination and zero forcing*, arXiv:1510.02421 (2015). https://arxiv.org/abs/1510.02421
4. B. Brešar, S. Klavžar and D. F. Rall, *Dominating direct products of graphs*, Discrete Mathematics 307 (2007), 1636–1642. https://doi.org/10.1016/j.disc.2006.09.013
