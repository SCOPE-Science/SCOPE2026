# Complete distance-two and distance-three mutual-visibility polynomials of rectangular grids

## Finding
Let \(G_{m,n}=P_m\square P_n\) be the rectangular grid with \(m,n\ge2\). A \(k\)-distance mutual-visibility set \(S\) is a subset of vertices such that each two distinct vertices are joined by some shortest path of length at most \(k\) with no other vertex of \(S\) on the path. Define the **full cardinality polynomial**
\[
F^{(k)}_{m,n}(z)=\sum_{S:\,S\text{ is }k\text{-distance mutually visible}}z^{|S|},
\]
including the empty set. For any positive integers \(h,w\), set
\[
B_{h,w}=\max\{m-h+1,0\}\max\{n-w+1,0\},\quad D_h=B_{h,h},\quad E_{h,w}=B_{h,w}+B_{w,h}\quad(h<w).
\]
Then **every coefficient** of both \(F^{(2)}_{m,n}\) and \(F^{(3)}_{m,n}\) is determined for every pair \(m,n\ge2\) by the following explicit formulas:
\[
\boxed{F^{(2)}_{m,n}(z)=1+mnz+(E_{1,2}+E_{1,3}+2D_2)z^2
 +(4D_2+2E_{2,3})z^3+D_3z^4.}
\]
\[
\boxed{\begin{aligned}
F^{(3)}_{m,n}(z)={}&1+mnz
 +(E_{1,2}+E_{1,3}+E_{1,4}+2D_2+2E_{2,3})z^2\\
&+(4D_2+10E_{2,3}+4E_{2,4}+8D_3)z^3\\
&+(E_{2,3}+2E_{2,4}+25D_3+4E_{3,4})z^4\\
&+(4D_3+4E_{3,4})z^5+E_{3,4}z^6.
\end{aligned}}
\]
This enumerates **all** feasible subsets at every cardinality, not merely the largest sets. Its leading coefficients recover, but do not claim to newly establish, the previously known optimal \(3\)-distance grid configurations. It also gives the complete \(2\)-distance polynomial and all smaller-cardinality \(3\)-distance counts.

## Assumptions and scope
The grid's labeled vertex set is \(\{0,\ldots,m-1\}\times\{0,\ldots,n-1\}\), and edges join Manhattan-neighboring vertices. The shortest-path condition is existential, and a path of length greater than \(k\) never qualifies. No quotient by graph automorphisms is taken. The formulas hold at small dimensions where \(k\) may exceed the graph diameter, using the same literal shortest-path definition. No assertion is made about distances above three, higher-dimensional grids, unrestricted visibility polynomials, or variants that exempt distant pairs.

## Proof
**Locality lemma.** For a valid \(k\)-distance mutual-visibility set, all selected pairs have Manhattan distance at most \(k\). Consequently, the occupied row span and column span are each at most \(k\). For \(k\in\{2,3\}\), after subtracting the least occupied coordinate in each direction, every nonempty valid set is a subset of a box of at most \(4\times4\) vertices. A shortest grid path is exactly a path whose successive moves each decrease the Manhattan distance to its destination by one. It cannot leave the axis-parallel bounding rectangle of its endpoints; hence neither translating a selected set nor restricting the ambient grid to its exact bounding rectangle affects any of the required path-existence decisions.

**Anchored counting lemma.** An *anchored* subset of an \(h\times w\) box has exact occupied row and column spans \(h-1\) and \(w-1\): in particular it touches the two extreme rows and two extreme columns. Let \(p^{(k)}_{h,w}(z)\) count all such anchored \(k\)-distance mutual-visibility subsets by size. The following gives every nonzero polynomial for \(k=2,3\) with \(h\le w\); the polynomials are symmetric in the two dimensions and all unlisted shapes are zero:

| Exact box \((h,w)\) | \(p^{(2)}_{h,w}(z)\) | \(p^{(3)}_{h,w}(z)\) |
|:--|:--|:--|
| \((1,1)\) | \(z\) | \(z\) |
| \((1,2)\) | \(z^2\) | \(z^2\) |
| \((1,3)\) | \(z^2\) | \(z^2\) |
| \((1,4)\) | \(0\) | \(z^2\) |
| \((2,2)\) | \(2z^2+4z^3\) | \(2z^2+4z^3\) |
| \((2,3)\) | \(2z^3\) | \(2z^2+10z^3+z^4\) |
| \((2,4)\) | \(0\) | \(4z^3+2z^4\) |
| \((3,3)\) | \(z^4\) | \(8z^3+25z^4+4z^5\) |
| \((3,4)\) | \(0\) | \(4z^4+4z^5+z^6\) |

**Exhaustive finite proof of the lemma.** The accompanying `verify_grid.py` iterates over each \(h,w\in\{1,2,3,4\}\) and each of the \(2^{hw}-1\) nonempty vertex masks, retaining precisely those whose occupied bounding box is all \(h\times w\). For each selected unordered pair, it first requires Manhattan distance at most \(k\), then performs a finite reachability search in which every move decreases distance to the destination by one, rejecting internal vertices of the selected set. Such paths are *exactly* the shortest paths; the predicate therefore checks the definition without relaxation or approximation. Summing the accepted masks by set size establishes the entire table, not just its largest entries. A second self-contained implementation, `verify_paths.py`, explicitly generates *all* shortest paths between each pair and encodes their internal vertices as bitmasks before independently counting valid subsets. Both exact enumerations were run against the files and agree for all 16 exact boxes and both distances. Each loop is finite, covers its asserted universe completely, and does not infer an infinite fact from partial data. The infinite claim comes from the proved locality lemma.

**Global polynomial.** Each nonempty set has a *unique* exact occupied bounding box and a unique translation moving that box to coordinates starting at zero. A fixed anchored pattern on an \(h\times w\) box has exactly \(B_{h,w}\) translations into \(G_{m,n}\). There is no collision between different anchored patterns or translations because the occupied coordinate minima and exact spans can be recovered from the resulting set. Therefore, for \(k=2,3\),
\[
F^{(k)}_{m,n}(z)=1+\sum_{h=1}^{4}\sum_{w=1}^{4} B_{h,w}\,p^{(k)}_{h,w}(z).
\]
Substituting every entry of the exhaustive anchored table, grouping transposed boxes through \(E_{h,w}\), and gathering coefficients yields exactly the two boxed polynomials. This completes the proof for all \(m,n\ge2\).

## Verification
Executing `python3 verify_grid.py` and `python3 verify_paths.py` from the package directory reproduces and compares every anchored coefficient in the table. They require only the Python standard library and terminate by exhaustive finite loops. The closed formulas give, for \(G_{3,3}\),
\[
F^{(2)}_{3,3}(z)=1+9z+26z^2+24z^3+z^4,
\]
\[
F^{(3)}_{3,3}(z)=1+9z+34z^2+64z^3+29z^4+4z^5,
\]
and for \(G_{4,4}\),
\[
F^{(3)}_{4,4}(z)=1+16z+90z^2+212z^3+140z^4+32z^5+4z^6.
\]
The first checker asserts these exact coefficients after reconstructing all local tables; the second uses a distinct shortest-path enumeration to confirm the tables. These computations are exhaustive certificates for the finite reduction, not merely spot checks of arbitrary grid sizes.

## Relationship to prior work
Cera López, García-Vázquez, Valenzuela-Tripodoro and Yero introduced \(k\)-distance mutual visibility in arXiv:2408.03976 (first public 2024-08-07). Their full open-access text obtains general bounds and results for other graph classes and explicitly proposes studying grids \(P_r\square P_t\). It does not enumerate all grid configurations by cardinality. Korže and Vesel (arXiv:2309.15201) analyze unrestricted mutual visibility, notably Cartesian products involving cycles, and record Manhattan intervals of grid geodesics; they do not give the present bounded-distance all-set polynomials. A pre-existing grid-specific result already determines the **largest** \(3\)-distance mutual-visibility sets and their counts; those top-degree consequences are not asserted to be new. The new statement is strictly stronger enumerative information at every smaller cardinality, notably all coefficients \(z^2\) through \(z^5\) for \(k=3\), as well as the full \(k=2\) polynomial. Distance mutual-visibility *coloring* (arXiv:2510.10284) counts partitions into feasible color classes, not individual feasible sets. Fault-tolerant mutual visibility (DOI:10.1002/net.70074) requires multiple internally disjoint geodesics and is a distinct parameter.

## Limitations
The full coefficient classification is restricted to fixed distances \(k=2,3\) on two-dimensional rectangular grids, not all \(k\) or all Cartesian products. The anchored polynomials are certified by a complete bounded exhaustive computation with explicit, reproducible code and an independently implemented route test; a symbolic, case-free derivation of each small anchored coefficient is not supplied. Earlier work covers the top-degree \(k=3\) consequences. No independent human audit, comprehensive priority certification, or claim about unindexed literature is provided.

## References
1. M. Cera López, P. García-Vázquez, J. C. Valenzuela-Tripodoro, I. G. Yero, *The k-Distance Mutual-Visibility Problem in Graphs*, arXiv:2408.03976, initial public date 2024-08-07; DOI:10.1007/s40840-024-01811-3; full article https://link.springer.com/article/10.1007/s40840-024-01811-3.
2. D. Korže, A. Vesel, *Mutual-Visibility Sets in Cartesian Products of Paths and Cycles*, arXiv:2309.15201; DOI:10.1007/s00025-024-02139-x; full article https://link.springer.com/article/10.1007/s00025-024-02139-x.
3. S. Babu, B. Brešar, A. Lakshmanan S, B. Samadi, *Distance mutual-visibility coloring: relations with (total) domination, exact distance graphs and graph products*, arXiv:2510.10284.
4. S. Cicerone, G. Di Stefano, S. Klavžar, G. Zhang, *Fault-Tolerant Mutual-Visibility: Complexity and Solutions for Grid-Like Networks*, DOI:10.1002/net.70074 (2026); full article https://onlinelibrary.wiley.com/doi/10.1002/net.70074.
