# Three-independent rook-graph polynomials and bipartite two-factor extremizers

## Finding

For nonnegative integers \(m,n\), let \(R_{m,n}=K_m\square K_n\) be the rook graph with vertex set \([m]\times[n]\). Define the three-independence polynomial
\[
I_{m,n}(z)=\sum_{U\subseteq V(R_{m,n}):\,\Delta(R_{m,n}[U])\le 2}z^{|U|}.
\]
Here a subgraph on the empty vertex set has maximum degree zero, and \(I_{m,0}(z)=I_{0,n}(z)=1\). Put \(w=xyz^2\). The complete labelled two-parameter generating function is the identity of formal power series
\[
\boxed{\sum_{m,n\ge0}\frac{I_{m,n}(z)}{m!n!}x^my^n=\frac{\exp\!\left(x+y+\frac{xyz+\tfrac12xy(x+y)z^2}{1-xyz^2}+\frac{xy^3+x^3y}{6}z^3-\frac12xyz^2\right)}{\sqrt{1-xyz^2}}.}
\]
The square root is its formal branch with constant coefficient one. The polynomial determines the number of all three-independent sets of each size in every rook graph.

For every integer \(q\ge2\), the maximum size of a three-independent set of \(R_{q,q}\) is precisely \(2q\). Such maximum sets are exactly the edge sets of the spanning two-regular bipartite subgraphs (two-factors) of \(K_{q,q}\). In particular, there are exactly
\[
\boxed{N_q=(q!)^2[t^q]\frac{e^{-t/2}}{\sqrt{1-t}}}
\]
maximum sets. For \(q=2,3,4,5,6,7,8\), these numbers are \(1,6,90,2040,67950,3110940,187530840\), respectively.

For \(m,n\ge2\) and \(\max\{m,n\}\ge5\), every three-independent subset \(U\) has a totally dominating complement \(V(R_{m,n})\setminus U\). Thus the full cardinality polynomial for total outer three-independent dominating sets is \(z^{mn}I_{m,n}(z^{-1})\), interpreted as a polynomial. In particular, for \(q\ge5\), the minimum total outer three-independent domination number is \(q^2-2q\), and the number of its minimum sets is \(N_q\).

## Assumptions and scope

All graphs are finite, undirected and simple. The Cartesian product \(K_m\square K_n\) joins two distinct cells exactly when they share one coordinate. A three-independent set is a vertex set whose induced subgraph has maximum degree at most two; in the alternative \(k\)-independence convention, it is a two-independent set. A totally dominating set \(D\) requires every vertex, including those in \(D\), to have a neighbor in \(D\). A total outer three-independent dominating set \(D\) is totally dominating and has \(\Delta(R_{m,n}[V\setminus D])\le2\). The generating-function identity holds for all \(m,n\ge0\), the square extremal statements for all \(q\ge2\), and the total-domination complement statement only in its stated size range.

## Proof

**1. Translation to a bipartite edge constraint.** Identify each cell \((i,j)\) of the rook graph with the edge joining left vertex \(i\) to right vertex \(j\) in \(K_{m,n}\). A cell set \(U\) determines a simple bipartite graph \(H\) with \(E(H)=U\). The number of neighbors of the edge \(ij\) in the line graph \(L(H)=R_{m,n}[U]\) is exactly
\[
d_H(i)+d_H(j)-2.
\]
Consequently, \(U\) is three-independent if and only if \(d_H(i)+d_H(j)\le4\) for every selected edge \(ij\).

**2. Exact connected-component classification.** A non-isolated vertex of \(H\) has degree at most three. If a vertex has degree three, then every one of its neighbors has degree at most one; thus its whole connected component is the three-star \(K_{1,3}\). If no vertex has degree three, the component has maximum degree at most two and is a path or a cycle. As \(H\) is simple and bipartite, every cyclic component is an even cycle of length at least four. Conversely, every disjoint union of isolated vertices, paths, simple even cycles of length at least four, and three-stars satisfies the degree-sum constraint. This is a necessary-and-sufficient classification.

**3. Component exponential generating functions.** Use \(x\) to mark left-side labels, \(y\) right-side labels and \(z\) edges. Isolated vertices contribute \(x+y\). An odd-edge alternating path of length \(2k+1\) has \(k+1\) vertices of each color and contributes \(x^{k+1}y^{k+1}z^{2k+1}\); an even-edge path of length \(2k\) with \(k\ge1\) contributes \(\tfrac12(x^{k+1}y^k+x^ky^{k+1})z^{2k}\). Both claims follow by listing the two oriented color sequences and dividing by path reversal. Summing over \(k\) gives
\[
P(x,y,z)=\frac{xyz+\tfrac12xy(x+y)z^2}{1-xyz^2}.
\]
A simple alternating cycle on \(k\) left and \(k\) right labeled vertices has \((k!)^2/(2k)\) realizations for \(k\ge2\), so its exponential contribution is \((xyz^2)^k/(2k)\). Thus all cycles contribute
\[
C(x,y,z)=\sum_{k\ge2}\frac{(xyz^2)^k}{2k}=-\frac12\log(1-xyz^2)-\frac12xyz^2.
\]
The two orientations of a three-star contribute \((xy^3+x^3y)z^3/6\). The labelled two-sort exponential formula applies because the components form a unique unordered decomposition; exponentiating the sum of these four component series gives exactly the stated generating function. Every component was characterized and counted exactly once, so this proves all coefficients, not merely an asymptotic statement.

**4. Square maxima and their multiplicities.** Each permitted component containing \(v\) vertices has at most \(v\) edges; equality holds only for a cycle. The bipartite graph \(H\) has at most \(2q\) vertices when \(m=n=q\), so \(|U|=|E(H)|\le2q\). For every \(q\ge2\), the complete bipartite graph contains a spanning even cycle, so this bound is attained. Equality forces all \(2q\) vertices to belong to cyclic components and every vertex to have degree two, i.e. \(H\) must be a spanning bipartite two-factor. The labelled exponential series for such cycles on balanced shores is
\[
\exp\!\left(\sum_{k\ge2}\frac{t^k}{2k}\right)=\frac{e^{-t/2}}{\sqrt{1-t}}.
\]
Multiplying its coefficient of \(t^q\) by \((q!)^2\) gives \(N_q\) exactly.

**5. Total outer domination consequence.** Let \(m,n\ge2\) with \(\max\{m,n\}\ge5\), and let \(U\) be any three-independent set. For each \(u\in U\), its degree in \(R_{m,n}\) is \(m+n-2\ge5\), and at most two of its neighbors lie in \(U\); therefore it has a neighbor outside \(U\). Now suppose \(v\notin U\) has no neighbor outside \(U\). Every neighbor of \(v\) then lies in \(U\). Choose a row or column clique through \(v\) of order at least five. It contains at least four vertices of \(U\), and each of these has at least three neighbors inside \(U\), contradicting the three-independence condition. Thus every vertex has a neighbor outside \(U\), so the complement is totally dominating. The polynomial reversal and square minimum follow by complementation and the proved maximum-set classification.

## Verification

The accompanying `verify.py` uses only the Python standard library. It constructs rook graphs and checks each selected cell subset for its exact induced degree and, separately, the total-domination condition. It compares these counts with an independent distinguished-component recursion, also expands the component exponential series with rational arithmetic, and checks the bipartite two-factor formula through order eight. Executing `python3 verify.py` reports `VERIFY_OK` with 13 exhaustive graph instances and 108398 directly tested cell subsets. These calculations corroborate but are not substitutes for the preceding all-parameter proof.

## Relationship to prior work

Mao, Cheng, Wang and Guo (2017 online; journal 2018) established bounds for the \(k\)-independence number of Cartesian products of complete graphs, but not the complete size enumeration or the sharp square result given here. Cabrera-Martínez and collaborators (2020) studied total outer \(k\)-independent domination and its general inequalities. Mortosa (2022) considered \(k\)-independence in graph products and revisited the rook-product bounds. A related full-size enumeration of induced forests in rook graphs covers only bipartite path-forest components; the present invariant is different, since its bipartite witnesses can additionally contain even cycles and three-stars. A 2024 study of complexity of \(k\)-independence in products was accessible for abstract-level comparison only, and priority risks remain. These references motivate the invariant; none of the accessible stated earlier bounds or enumerations directly supplies the displayed three-independence EGF or the square two-factor classification.

## Limitations

The main polynomial concerns induced maximum degree two, not arbitrary induced maximum degree; in particular it is not the forest polynomial, since induced cycles are admitted. The total-domination equivalence has only been proved for \(m,n\ge2\) and \(\max\{m,n\}\ge5\); no claim is made for smaller boards. Source comparisons are not an independent guarantee of publication priority. The coefficient-extraction identity is exact, but it is not simplified to a single elementary finite sum for every coefficient.

## References

1. L. Mao, E. Cheng, H. Wang, C. Guo, *The k-independence number of graph products*, publicly available online June 27, 2017; DOI: 10.26493/2590-9770.1216.6d2.
2. M. Cabrera-Martínez et al., *On the Total Outer k-Independent Domination Number of Graphs*, *Mathematics* 8 (2020), 194; DOI: 10.3390/math8020194.
3. R. Mortosa, *Conjuntos k-independentes em alguns produtos de grafos*, 2022, Universidade Federal de Goiás thesis.
4. J. Cappelle, E. Coelho, R. Mortosa, D. Nascimento, *Complexity results on k-independence in some graph products*, 2024; DOI: 10.1051/ro/2024098 (abstract accessible; full text was not inspected).
