# Lower mutual-visibility number of odd three-row tori

## Finding

**Theorem.** For every integer \(k\ge 2\), the lower mutual-visibility number of the Cartesian torus \(C_3\square C_{2k+1}\) is exactly
\[
\mu^{-}(C_3\square C_{2k+1})=5.
\]
Moreover, an explicit five-vertex inclusion-maximal mutual-visibility set is
\[
S_k=\{(0,0),(0,1),(1,0),(2,k+1),(2,k+2)\}.
\]
Here the first coordinates are taken modulo \(3\), and the second coordinates modulo \(2k+1\). This solves the odd-length, three-row subfamily of the toroidal-grid lower-mutual-visibility problem, without asserting a value for arbitrary even circumferences or wider tori.

## Assumptions and scope

All graphs are finite, simple, connected and undirected. For a vertex set \(X\subseteq V(G)\), two vertices \(u,v\in X\) are *\(X\)-visible* if some shortest \(u,v\)-path has no internal vertex in \(X\). A *mutual-visibility set* has this property for every pair of its members. Such a set is *inclusion-maximal* when adding any single outside vertex destroys the property. The *lower mutual-visibility number* \(\mu^{-}(G)\) is the minimum cardinality of any inclusion-maximal mutual-visibility set. (These are not the ordinary maximum mutual-visibility number or its total/outer/dual variants.)

Write \(n=2k+1\) with \(k\ge2\) and take the torus vertices to be \((r,j)\) for \(r\in\{0,1,2\}\) and \(j\in\mathbb Z/n\mathbb Z\). Vertices are adjacent if either the rows differ and columns agree, or the rows agree and columns are cyclically consecutive. Since \(C_3=K_3\), a geodesic between different rows changes row *exactly once*, and its column steps form a shortest arc in \(C_n\); a same-row geodesic never changes row. Between distinct columns in an odd cycle, the shortest arc is unique and has length at most \(k\).

## Proof

**Lower bound.** Let \(X\) be an inclusion-maximal mutual-visibility set. It must occupy all three rows. Indeed, if row \(r\) were empty, add any \((r,j)\). Every previously visible pair admits a geodesic using only its two endpoint rows, so their visibility remains. From the new vertex to an old vertex \((s,t)\), walk along row \(r\) from column \(j\) to \(t\) along a shortest cycle arc, and then make the single row change to \((s,t)\). All internal vertices lie in the initially empty row; hence the enlarged set is mutually visible. This contradicts maximality.

A set of size at most four occupying three rows has row occupancies \((1,1,1)\) or \((2,1,1)\), up to permutation. In the first case any second vertex can be added to one row: cross-row pairs stay visible by switching at the starting column into the row of the endpoint, whose only selected vertex is that endpoint. In the second case let the two selected columns in the busy row be \(u,v\). They can be extended to a three-vertex mutual-visibility set *within the odd cycle*: by a rotation and reflection write \(u=0\), \(v=d\), \(1\le d\le k\), and add column \(k+1\). The three consecutive cyclic gaps are \(d\), \(k+1-d\), and \(k\), all at most \(k\). Each gap is the unique geodesic between its endpoints and avoids the third selected vertex. Cross-row pairs remain visible because each of the other two rows has just one selected vertex; immediately switch into the singleton endpoint's row and then travel to that endpoint. Thus the enlarged set is still mutually visible. No maximal set has fewer than five vertices.

**Five-vertex upper bound.** Put
\[
a=(0,0),\quad b=(0,1),\quad c=(1,0),\quad d=(2,k+1),\quad e=(2,k+2).
\]
The ten pairs are mutually visible. The pairs \((a,b)\), \((a,c)\), and \((d,e)\) are adjacent. For the pairs \((a,d)\) and \((a,e)\), follow the backward shortest cycle arc entirely in row \(0\), then switch at the terminal column to row \(2\). For \((b,d)\), take the forward shortest arc in row \(0\), then switch at \(d\). For \((b,c)\), switch from row \(0\) to row \(1\) at column \(1\), then move to column \(0\). For \((b,e)\), switch at column \(1\) immediately into row \(2\), then follow the backward shortest arc to column \(k+2\). This arc avoids \(d\). Finally, for \((c,d)\) and \((c,e)\), follow the backward shortest arc entirely in row \(1\) and switch to row \(2\) only at the destination. Every displayed path is a geodesic and has no other vertex of \(S_k\) in its interior.

It remains to prove inclusion-maximality. Every vertex not in \(S_k\) belongs to exactly one of the following six cases. In each, adding the vertex destroys visibility of the specified pair; an endpoint involving the newly added vertex is explicitly indicated when needed.

| New vertex | Range of \(j\) | Witness pair that becomes nonvisible | Why every geodesic is blocked |
| --- | --- | --- | --- |
| \((0,j)\) | \(2\le j\le k\) | \(a,(0,j)\) | Their unique same-row shortest arc contains \(b\). |
| \((0,j)\) | \(k+1\le j\le2k\) | \(a,d\) | Their backward column arc is unique. A row change before its endpoint would traverse \(e\) in row \(2\), so a clear geodesic must stay in row \(0\) through \((0,j)\). |
| \((1,j)\) | \(1\le j\le k\) | \(a,(1,j)\) | The unique forward arc requires switching at column \(0\), through \(c\), or later, through \(b\). |
| \((1,j)\) | \(k+1\le j\le2k\) | \(c,d\) | A row change before column \(k+1\) meets \(e\); switching only at the endpoint forces the entire backward arc in row \(1\) through \((1,j)\). |
| \((2,j)\) | \(j\in\{0,1\}\cup\{k+3,\ldots,2k\}\) | \(b,e\) | Their unique backward column arc must switch into row \(2\) at column \(1\), or else pass \(a\) in row \(0\); thereafter it traverses \((2,j)\). |
| \((2,j)\) | \(2\le j\le k\) | \(e,(2,j)\) | Their unique shortest same-row arc passes through \(d\). |

The ranges also cover the cases where the displayed interval is empty (for \(k=2\)). Therefore every possible addition fails, and \(S_k\) is inclusion-maximal of size five. Combining the two bounds proves the theorem. \(\square\)

## Verification

The included standalone `verify.py` independently constructs the torus adjacency and all-pairs graph distances. For every selected set \(X\), it checks visibility using a shortest-path search with \(X\setminus\{u,v\}\) forbidden for each selected pair; it does not assume the cyclic-geodesic case analysis in the proof. It verifies that the explicit \(S_k\) is inclusion-maximal at odd circumferences \(n\in\{5,7,9,11,13,15,17,19,21,31,41,51\}\). It also exhaustively enumerates all subsets of sizes one through four at \(n\in\{5,7,9\}\) and confirms that none is inclusion-maximal. Run `python3 verify.py`; successful output ends in `VERIFY_OK`.

Finite verification is only corroboration. The lower bound and six-case maximality proof establish the infinite statement.

## Relationship to prior work

Brešar and Yero introduced \(\mu^{-}\) and showed \(\mu^{-}(P_m\square P_n)=3\) for rectangular path grids and \(\mu^{-}(K_m\square K_n)=m+n-1\) for products of two complete graphs. Their concluding Problem 1 expressly asks for lower mutual-visibility numbers of cylindrical and toroidal grids. The present family is toroidal because \(K_3=C_3\), but its second factor \(C_{2k+1}\) is not complete for \(k\ge2\); hence neither cited product formula specializes to it.

Cicerone, Di Stefano, Drozek, Hedzet, Klavžar and Yero study the *maximum* mutual, outer, dual and total visibility numbers of tori, not the minimum size of an inclusion-maximal ordinary mutual-visibility set. Earlier work of Cicerone, Di Stefano and Klavžar addresses maximum/independent mutual visibility in Cartesian products. These do not imply the new lower-inclusion-maximal value. No claim about all tori, even-length circumferences, or every maximal set is made.

## Limitations

The result is confined to odd \(n\ge5\) with first factor \(C_3\). It does not classify all inclusion-maximal sets or all possible cardinalities, nor does it determine even-width or larger-first-factor toroidal cases. Computational checks reach only the stated finite orders and are not used as a proof of the infinite case. A previously unindexed equivalent result is a residual literature-priority risk; no independent validation is asserted.

## References

1. B. Brešar and I. G. Yero, *Lower (total) mutual-visibility number in graphs*, arXiv:2307.02951 (first public version 2023-07-06); see Corollaries 4 and 7 and concluding Problem 1. https://arxiv.org/abs/2307.02951
2. S. Cicerone, G. Di Stefano, L. Drozek, J. Hedzet, S. Klavžar, and I. G. Yero, *Variety of mutual-visibility problems in graphs*, arXiv:2304.00864 (2023), Section 4. https://arxiv.org/abs/2304.00864
3. S. Cicerone, G. Di Stefano, and S. Klavžar, *On the mutual visibility in Cartesian products and triangle-free graphs*, arXiv:2112.13024 (2021), Section 3. https://arxiv.org/abs/2112.13024
