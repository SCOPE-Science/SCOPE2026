# Exact limited domination and low-capacity rigidity for rectangular rook graphs

## Finding
Let \(m,n\ge2\) be integers, and let \(R_{m,n}=K_m\square K_n\) be the rook graph on the squares of an \(m\)-by-\(n\) board: distinct squares are adjacent precisely when they share a row or column. For an integer \(k\) with \(0\le k\le m+n-2\), a subset \(D\) of vertices is **\(k\)-limited dominating** when every vertex outside \(D\) is adjacent to a vertex in \(D\), and every vertex of \(D\) has at most \(k\) neighbors outside \(D\). Let \(\gamma_k^{\mathrm L}\) denote the smallest size of such a set.

**Exact value (all parameters):**
\[
\gamma_k^{\mathrm L}(R_{m,n})
=\min\bigl\{m\max(1,n-k),\;n\max(1,m-k)\bigr\}.
\]
In particular, the standard Cartesian-product upper bound for \(k\)-limited domination is attained for every pair of complete-graph factors, not just for the previously treated square subfamily.

**Rigidity of all minimizers (low-capacity range):** If \(1\le k<\min(m,n)\), then every minimum \(k\)-limited dominating set consists of a union of whole parallel rows or a union of whole parallel columns. More precisely:

- When \(m<n\), the minimum sets are precisely the \((m-k)\)-row slabs, with \(\binom{m}{k}\) distinct choices.
- When \(m>n\), the minimum sets are precisely the \((n-k)\)-column slabs, with \(\binom{n}{k}\) distinct choices.
- When \(m=n\), the minimum sets are precisely the \((m-k)\)-row slabs and the \((n-k)\)-column slabs, with \(2\binom{m}{k}\) distinct choices.

At \(k=0\), the entire vertex set is the unique admissible set. The claim does not classify all minimum sets once \(k\ge\min(m,n)\).

## Assumptions and scope
Graphs are finite, simple, and undirected. Both factors have at least two vertices; rows are indexed by \([m]\), columns by \([n]\). The nontrivial capacity interval is \(1\le k<m+n-2\), but the statement also includes the exact endpoints \(k=0\) and \(k=m+n-2\). Capacity counts all neighbors *outside* the selected set, without assigning individual demand vertices to individual guards. These quantifiers and the adjacency convention match the cited definition of \(k\)-limited domination.

## Proof
Write \(\rho_i=|D\cap(\{i\}\times[n])|\) for the occupancy of row \(i\), and \(\kappa_j=|D\cap([m]\times\{j\})|\) for the occupancy of column \(j\). A selected square \((i,j)\in D\) has exactly
\[
(n-\rho_i)+(m-\kappa_j)
\]
neighbors outside \(D\); the row and column contributions are disjoint. Thus the \(k\)-limited condition is equivalent to
\[
\rho_i+\kappa_j\ge m+n-k\qquad\text{for every }(i,j)\in D. \tag{1}
\]

A dominating set must occupy **every row or every column**. Indeed, if a row \(i\) and a column \(j\) were both empty, the unselected square \((i,j)\) would have no selected neighbor. Conversely, any set occupying every row (or every column) dominates all unselected squares.

Suppose first that all rows are occupied. Choose any \((i,j)\in D\) in each row \(i\). As \(\kappa_j\le m\), inequality (1) implies \(\rho_i\ge n-k\). Since \(\rho_i\ge1\), summing over \(i\) gives
\[
|D|\ge m\max(1,n-k). \tag{2}
\]
Similarly, if all columns are occupied, each occupied column has \(\kappa_j\ge\max(1,m-k)\), giving
\[
|D|\ge n\max(1,m-k). \tag{3}
\]
Every dominating set falls into at least one of these cases; hence its cardinality is at least the minimum of the right-hand sides of (2) and (3).

For the reverse inequality, put \(b=\max(1,n-k)\) and select **all** squares in any fixed set of \(b\) columns. This set has cardinality \(mb\), dominates by occupying every row, and each selected square has exactly \(n-b\le k\) outside neighbors. Symmetrically, select all squares in \(a=\max(1,m-k)\) rows; it has cardinality \(na\), dominates every unselected square, and each selected square has exactly \(m-a\le k\) outside neighbors. The smaller construction attains the lower bound. This proves the formula for all stated \(m,n,k\).

For the rigidity statement assume \(1\le k<\min(m,n)\), so \(n-k\) and \(m-k\) are positive. If a minimum set meeting all rows attains the row-covering lower bound \(m(n-k)\), equality in (2) forces \(\rho_i=n-k\) in every row. Equation (1) then forces \(\kappa_j\ge m\) for every \((i,j)\in D\), so every used column is completely filled: \(D\) consists of exactly \(n-k\) whole columns. Similarly, equality in (3) implies that every used row is completely filled and there are exactly \(m-k\) such rows.

The difference between the two possible lower bounds is
\[
m(n-k)-n(m-k)=k(n-m).
\]
For \(m<n\) the row-covering bound is strictly larger, so only the whole-row minimizers can occur; for \(m>n\) the symmetric statement holds. When \(m=n\) both slab orientations attain the same value; they are distinct for the stated positive \(k\). Choosing the omitted rows or columns yields the listed binomial counts. When \(k=0\), any selected vertex cannot have an outside neighbor, and connectivity forces \(D\) to be the entire graph.

## Verification
The standalone C++17 program `verify_rook.cpp` constructs the adjacency list as neighborhood bit masks, enumerates **every nonempty subset** of each tested rook graph, and independently checks both the domination requirement and the outside-neighbor capacity at every selected square. It computes all minima, and also counts all minimizing sets for \(k<\min(m,n)\). It compares these independent exhaustive counts with the theorem.

Run `c++ -std=c++17 -O2 verify_rook.cpp -o verify_rook` and then `./verify_rook`. The recorded output is `verify_rook.out`. The program covers 14 rectangular boards with \(2\le m\le n\le9\) and at most 20 squares, 93 capacity triples, and 1,763,138 nonempty tested subsets. It reports zero discrepancies, including equality-case counts. The infinite statements follow from the preceding proof, **not** from finite enumeration.

## Relationship to prior work
Božović, Radić, Kovijanić-Vukićević and Tepeh introduced the \(k\)-limited domination parameter and determined it on complete graphs and several other basic families (arXiv:2606.22422, June 21, 2026). Tepeh subsequently established a general Cartesian-product upper bound and proved its sharpness in the specific rook-graph case \(K_{k+2}\square K_{k+2}\) (arXiv:2606.22428, June 21, 2026, Theorem 7 and Proposition 8 in the available full first version). The present result establishes equality for **all** pairs of complete-graph factors, all capacities, and rigidly classifies every minimum set in the low-capacity interval. An upper bound alone does not imply equality; the missing global lower bound is furnished by the row-or-column coverage dichotomy and occupancy inequality (1). The first-version square result is a special case, not a substitute for that argument.

The same parameter can be expressed as \((1,t)\)-domination on regular graphs, with \(t=m+n-2-k\). This equivalence is credited to the originating paper and is not claimed here as new.

## Limitations
No assertion is made for Cartesian products with three or more factors or arbitrary graph products. Although the exact minimum is known for all capacities, the classification of *all* optimal sets is restricted to \(k<\min(m,n)\). The complete revised October 2026 version of arXiv:2606.22428 was not accessible at the time of comparison; the first-version full text and later abstract were accessible. An unindexed equivalent statement under \((1,t)\)-domination or in that revision remains an originality risk. Computational checks use finite boards only and cannot replace the universal proof.

## References
1. D. Božović, G. Radić, Ž. Kovijanić-Vukićević, A. Tepeh, *On k-limited domination in graphs*, arXiv:2606.22422 (first posted June 21, 2026), https://arxiv.org/html/2606.22422.
2. A. Tepeh, *On k-limited domination: complexity and Cartesian products*, arXiv:2606.22428 (first posted June 21, 2026), accessible first-version full-text rendition https://www.researchgate.net/publication/407508234_On_k-limited_domination_complexity_and_Cartesian_products ; revised version listing https://www.arxiv.symmetricfunctions.com/paper/2606.22428v2.
