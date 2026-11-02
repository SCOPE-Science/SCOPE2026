# Geodesic hull-set polynomials of categorical products of complete graphs

## Finding
For all integers \(m,n\ge3\), let \(G_{m,n}=K_m\times K_n\) denote the **categorical (direct, tensor) graph product**: its vertices are \((i,j)\) with \(1\le i\le m\), \(1\le j\le n\), and distinct vertices are adjacent precisely when both coordinates differ. Let \(\operatorname{Hull}(S)\) be the smallest *geodesically convex* vertex set containing \(S\), obtained by iterating all shortest-path intervals. The hull-set polynomial is
\[
H_{m,n}(z)=\sum_{S\subseteq V(G_{m,n}):\,\operatorname{Hull}(S)=V(G_{m,n})}z^{|S|}.
\]
If \(\max\{m,n\}\ge4\), then
\[
\boxed{H_{m,n}(z)=(1+z)^{mn}-\sum_{k=0}^{\min\{m,n\}}\binom mk\binom nk k!\,z^k.}
\]
Equivalently, a set is **not** a hull set if and only if it contains at most one vertex from every row and every column. In particular every proper geodesically convex set is a clique (a partial permutation matrix).

The unique exceptional parameter pair is \((m,n)=(3,3)\). For this pair, the six maximal proper convex sets are the complements of the six permutation matrices of order three, and
\[
\boxed{H_{3,3}(z)=6z^3+45z^4+90z^5+78z^6+36z^7+9z^8+z^9.}
\]
Consequently the geodesic hull number is \(3\) on \(K_3\times K_3\) and \(2\) for every other pair in the stated range. There are exactly six minimum hull sets in the exceptional case (the three complete rows and three complete columns), while for \(\max\{m,n\}\ge4\) there are precisely \(m\binom n2+n\binom m2\) minimum hull sets.

## Assumptions and scope
All graphs are finite, simple and undirected. In particular \(\times\) denotes the *categorical product*, **not** the Cartesian product \(\square\). A set \(X\) is geodesically convex when every vertex on every shortest path between two vertices of \(X\) lies in \(X\). An arbitrary set's hull is the intersection of all geodesically convex sets containing it. Because these products have diameter \(2\), this convexity is also the induced-three-vertex-path \(P_3^*\) convexity, not the ordinary \(P_3\) two-neighbor bootstrap convexity. A *partial permutation matrix* is a subset of grid positions using each row and each column at most once. All vertex subsets are distinguished and are not identified under symmetry.

## Proof
**1. Intervals and diameter.** Two distinct grid cells are adjacent if their row and column indices both differ. If two distinct cells are nonadjacent, they share one row or one column. When the row agrees and the columns are \(j\ne k\), their common neighbors are *exactly*
\[
\{(a,\ell):a\ne i,\ \ell\notin\{j,k\}\}.
\]
The transposed formula holds for a same-column pair. Since both dimensions are at least three, this set is nonempty, so the graph has diameter two and its shortest-path closure simply inserts all common neighbors of nonadjacent selected pairs.

**2. A same-row pair generates the whole grid outside the exceptional case.** By symmetry suppose an initial set contains \((i,j)\) and \((i,k)\), with \(j\ne k\). Their interval adds all cells \((a,\ell)\) where \(a\ne i\) and \(\ell\notin\{j,k\}\).

If \(n\ge4\), choose two distinct columns \(\ell_1,\ell_2\) outside \(\{j,k\}\). Given any row \(b\ne i\), choose a row \(a\) different from both \(i\) and \(b\), possible since \(m\ge3\). The already inserted pair \((a,\ell_1),(a,\ell_2)\) adds \((b,j),(b,k)\). Thus every cell of every row other than \(i\) is now present. Selecting two distinct such rows in column \(j\) adds the remaining cells of row \(i\). The hull is the entire grid.

If instead \(n=3\) and \(m\ge4\), denote the unique third column by \(\ell\). The first interval selects column \(\ell\) at every row except \(i\). For any row \(b\), two of these selected rows may be chosen different from \(b\), because \(m-2\ge2\). The corresponding same-column pair adds \((b,j),(b,k)\). Hence both original columns become full. Two selected cells in column \(j\) at rows different from \(i\) now add \((i,\ell)\), completing the grid. The same argument with row and column transposed applies to every same-column pair. Every set containing a nonadjacent pair is therefore a hull set.

Conversely any subset with no same-row and no same-column pair is a clique: every two of its vertices are adjacent. A clique is geodesically convex, and so cannot be a hull set unless it is the entire graph (which it cannot be here). Thus for \(\max\{m,n\}\ge4\) the non-hull sets are exactly the partial permutation matrices. There are \(\binom mk\binom nk k!\) of cardinality \(k\); subtraction from the full-subset polynomial \((1+z)^{mn}\) proves the first formula.

**3. The exceptional \(3\)-by-\(3\) grid.** A full row or column is a hull set: its three pairs generate the other two rows (or columns), and hence the entire grid. Suppose \(X\) is proper and convex and contains a same-row pair \((i,j),(i,k)\). With \(a,b\) the other rows and \(\ell\) the remaining column, closure forces the four-cell cross
\[
B=\{(i,j),(i,k),(a,\ell),(b,\ell)\}\subseteq X.
\]
It cannot contain \((i,\ell)\), since that would give a complete row. Its remaining possible cells form the four corners \((a,j),(a,k),(b,j),(b,k)\). Adding any one corner forces its diagonally opposite corner; for example, \((a,j)\) together with \((a,\ell)\) forces \((b,k)\). A corner from the other diagonal would complete some row or column, and thus produce the full hull. Accordingly \(X\) is either exactly the four-cell cross, or exactly that cross plus one diagonal, a six-cell set equal to the complement of a permutation matrix.

Each of the six complements of permutation matrices is indeed convex. It has exactly two cells in every row and column; for any two in the same row, the two common neighbors are exactly the selected cells of the omitted column, and the transposed assertion holds. These six convex sets are maximal proper convex sets. Finally, if \(X\) contains no same-row or same-column pair, it is a partial permutation matrix; it lies in the complement of some full permutation matrix, because any partial matching of a \(3\)-by-\(3\) bipartite grid extends to a full permutation and one can select a full permutation disjoint from its selected cells. Thus **every** proper convex set lies in one of those six maximal sets, and every set contained in one of the six has a proper hull.

For \(\pi\in S_3\), put \(M_\pi=\{(i,\pi(i)):i=1,2,3\}\) and \(X_\pi=V\setminus M_\pi\). The polynomial of non-hull subsets is the inclusion-exclusion union of the Boolean lattices of the six \(X_\pi\):
\[
\sum_{\varnothing\ne F\subseteq S_3}(-1)^{|F|+1}(1+z)^{|\bigcap_{\pi\in F}X_\pi|}.
\]
Evaluating these \(63\) finite intersection terms and subtracting from \((1+z)^9\) gives exactly the displayed \(H_{3,3}(z)\). This calculation is replayed independently in the accompanying verifier.

**4. Minima.** The polynomial for the generic case first has a nonzero term at degree \(2\); the two-element hull sets are exactly pairs sharing a row or sharing a column, giving \(m\binom n2+n\binom m2\) sets. In the exceptional case the polynomial begins with \(6z^3\), and the six full rows or columns are precisely its degree-three hull sets.

## Verification
The accompanying standalone \(\texttt{verify.py}\) constructs the graph from the adjacency definition and computes all vertex distances by breadth-first search, then the geodesic hull by repeated shortest-path interval closure. It exhausts **all** \(107008\) subsets across five parameter pairs: \((3,3),(3,4),(4,3),(3,5),(4,4)\), comparing the entire coefficient vectors with the theorem. It separately checks that the six maximal exceptional proper convex sets are the six complements of permutation matrices and verifies the exceptional \(63\)-term inclusion-exclusion calculation. Its final status is \(\texttt{VERIFY\_OK}\). These finite checks are corroboration; the infinite result is proved by Steps 1–4.

## Relationship to prior work
Dourado, Penso and Rautenbach's \(2019\) work introduces a source for the \(P_3^*\) hull framework and investigates complexity on chordal graphs and an algorithm for unit interval graphs [1]. Its later full-text-indexed journal version likewise presents those two principal results [2]. Their stated results do not establish a hull-set polynomial or classification for categorical products of complete graphs. The \(2016\) thesis of Nascimento examines \(P_3\) hull numbers for Cartesian, strong, and lexicographic products and geodesic hulls for complementary prisms [3]; its examined thesis chapters do not cover this categorical-product family or the induced-path convexity used here. The formal distinctions between \(P_3\), \(P_3^*\), and geodesic convexity matter; here \(P_3^*\) and geodesic convexity coincide **because of diameter two**, not by a general transfer theorem. No claim of exhaustive publication-priority certification is made.

## Limitations
The theorem assumes both factors have at least three vertices. It does not classify the factor-size-two cases, general categorical products, the ordinary \(P_3\)-convex hull, or one-step geodetic sets. A strongly relevant conference chapter [1] was accessible only by bibliographic information, abstract, and references rather than its full text; unexamined results in less-visible literature remain a publication-priority risk. The accompanying finite computations do not constitute a proof for unbounded dimensions. No independent mathematical audit has been performed.

## References
[1] M. C. Dourado, L. D. Penso and D. Rautenbach, *The Hull Number in the Convexity of Induced Paths of Order 3*, IWOCA 2019, LNCS 11638, 214–228, first online 10 July 2019. DOI: 10.1007/978-3-030-25005-8_18.

[2] M. C. Dourado, L. D. Penso and D. Rautenbach, *The hull number in the convexity of induced paths of order 3*, Theoretical Computer Science **906** (2022), 52–63. DOI: 10.1016/j.tcs.2022.01.004.

[3] J. R. Nascimento, *O Número Envoltório P3 e o Número Envoltório Geodético em Produtos de Grafos*, M.Sc. thesis, Universidade Federal de Goiás (2016). https://repositorio.bc.ufg.br/tede/handle/tede/6583.
