# Two-distance visibility in three-factor Hamming graphs: the sharp Zarankiewicz transition

## Finding

Let \(a,b,c\ge2\), and let \(H_{a,b,c}=K_a\square K_b\square K_c\) be the Cartesian product of three complete graphs, on labeled coordinate sets. Define \(\mu_2(H)\) as the largest cardinality of a vertex set \(S\) such that every two of its vertices are joined by a shortest path of length at most two whose internal vertices avoid \(S\). Write \(Z(r,s)\) for the maximum number of ones in an \(r\times s\) zero-one matrix with no all-one \(2\times2\) submatrix (equivalently, the largest number of edges in a \(C_4\)-free bipartite graph with part sizes \(r,s\)).

**Structural and extremal theorem.** Every two-distance mutual-visibility set in \(H_{a,b,c}\) is contained in at least one of the following: (i) a coordinate plane, within which the selected cells form a \(C_4\)-free zero-one matrix; (ii) a closed radius-one Hamming ball; (iii) a four-vertex parity tetrahedron on two symbols of each coordinate. Conversely, every subset of one of these three types, subject to the \(C_4\)-free requirement in (i), is two-distance mutually visible. Consequently,

\[
\boxed{\mu_2(H_{a,b,c})=\max\{a+b+c-2,\ Z(a,b),\ Z(a,c),\ Z(b,c)\}.}
\]

Let \(N_{r,s}(m)\) count labeled \(r\times s\) zero-one matrices with exactly \(m\) ones and no all-one \(2\times2\) submatrix, taking \(N_{r,s}(m)=0\) for \(m>Z(r,s)\). Put \(M=\mu_2(H_{a,b,c})\) and \(L=a+b+c-2\). The **number of maximum two-distance mutual-visibility sets** is exactly

\[
\boxed{abc\,\mathbf1_{\{M=L\}}+cN_{a,b}(M)+bN_{a,c}(M)+aN_{b,c}(M)+2\mathbf1_{\{a=b=c=2\}}.}
\]

In the equal-factor family \(H_q=K_q\square K_q\square K_q\), this gives the sharp transition

\[
\boxed{\mu_2(H_q)=\begin{cases}3q-2,&2\le q\le6,\\ Z(q,q),&q\ge7.\end{cases}}
\]

For \(3\le q\le5\) all maxima are the \(q^3\) complete radius-one balls. At \(q=6\), both radius-one balls and optimal coordinate-plane configurations attain the maximum \(16\); there are \(216+18N_{6,6}(16)\) maxima. For every \(q\ge7\), all maxima belong to coordinate planes, and there are \(3qN_{q,q}(Z(q,q))\) maxima. At \(q=2\), there are exactly ten maxima: eight radius-one balls and two parity tetrahedra. The values of \(Z(q,q)\) for unrestricted large \(q\) remain a separate open extremal problem; no closed formula for them is claimed here.

## Assumptions and scope

All graph factors are simple complete graphs with labeled vertex sets and orders at least two. Graph distances are Hamming distances of three-coordinate words. A coordinate plane fixes exactly one coordinate; a radius-one ball centered at \(u\) contains \(u\) and all vertices differing from \(u\) in exactly one coordinate, hence has \(a+b+c-2\) vertices. A parity tetrahedron is the four-element subset of a coordinate \(2\times2\times2\) box of one fixed parity of its three binary choices. The word *maximum* means maximum cardinality, not inclusion-maximality. The counting formula counts vertex sets rather than ordered listings; distinct coordinate-label assignments are distinct sets.

## Proof

**1. Diameter-two anticode lemma.** Suppose every pair of words in \(S\subseteq A\times B\times C\) differs in at most two coordinates. If \(S\) is contained in a coordinate plane there is nothing to prove. Otherwise there are two words at distance exactly two: if every pair had distance at most one, all of \(S\) would lie on one coordinate line. Rename coordinates and symbols to take these two words as \(u=(0,0,0)\) and \(v=(1,1,0)\). Since \(S\) is not contained in the third-coordinate plane, some word has third coordinate \(t\ne0\). Such an off-plane word must have its first two coordinates equal either to \((0,1)\) or to \((1,0)\): distance at most two from both \(u\) and \(v\) forces it to match one of their first-two coordinates in each comparison.

If all off-plane words have the same type \((0,1,t)\), then each in-plane word \((x,y,0)\) must satisfy \(x=0\) or \(y=1\), else it would differ from that off-plane word in all three coordinates. Thus every word is at distance at most one from \((0,1,0)\), and \(S\) lies in a closed radius-one ball. The symmetric argument applies if all off-plane words have type \((1,0,t)\).

If both off-plane types occur, say \((0,1,t)\) and \((1,0,t')\), their distance bound forces \(t=t'\). Every other off-plane word must have this same third symbol. An in-plane word must satisfy both \((x=0\text{ or }y=1)\) and \((x=1\text{ or }y=0)\), leaving only \((0,0,0)\) and \((1,1,0)\). Hence \(S\) is contained in the four vertices \((0,0,0),(1,1,0),(0,1,t),(1,0,t)\): a parity tetrahedron. This completes the anticode classification without assuming that \(S\) is maximal.

**2. Visibility within the three carriers.** In a coordinate plane, distinct cells in different rows and columns have exactly two shortest two-edge paths, whose internal vertices are the other two corners of their \(2\times2\) rectangle. Such a pair fails visibility precisely when all four corners are selected. Pairs sharing a coordinate are adjacent. Thus visibility in a plane is equivalent to \(C_4\)-freeness of the selected matrix. In a radius-one ball, any distance-two pair lies on different coordinate axes through the center; its two common neighbors are the center and the opposite corner, the latter lying outside the ball. Hence one shortest path avoids all selected internal vertices, regardless of whether the center itself is selected. Finally, the two internal vertices of a geodesic joining any pair in a parity tetrahedron have the opposite parity and lie outside the tetrahedron. Subsets inherit these properties. Every visible set necessarily satisfies the diameter-two condition, so the preceding anticode lemma gives a complete if-and-only-if classification.

**3. Extremal value and multiplicity.** A coordinate plane supports at most the appropriate \(Z(r,s)\) vertices, and every extremal \(C_4\)-free matrix is feasible. A radius-one ball supports \(L=a+b+c-2\) vertices, and a tetrahedron supports four. Since \(L\ge4\), the maximum is the displayed four-term maximum. Moreover \(L>\max\{a,b,c\}\), so a maximum set cannot belong to two different coordinate planes: their intersection is a coordinate line. The full radius-one balls cannot lie in any coordinate plane and have distinct centers. A maximum set carried by a ball is the entire ball, and there are exactly \(abc\) centers. Any tetrahedron can be maximum only if \(L=4\), equivalent to \(a=b=c=2\), where there are exactly two parity tetrahedra. These disjoint categories prove the counting formula.

**4. Equal factors and the exact cutoff.** Let \(z_q=Z(q,q)\). For \(q=2,3,4,5,6\), one has respectively

\[
(z_2,z_3,z_4,z_5,z_6)=(3,6,9,12,16).
\]

The upper bounds follow by counting unordered pairs of rows appearing together in a column. If column \(j\) has \(d_j\) ones, then a \(C_4\)-free matrix satisfies \(\sum_j\binom{d_j}{2}\le\binom q2\). For a fixed total of \(m\) ones, convexity makes the left side smallest when the column degrees differ by at most one. Applying this lower bound to \(m=4,7,10,13,17\), respectively, gives \(2,5,8,11,16\), strictly exceeding \(\binom q2=1,3,6,10,15\). Hence \(z_q\le3,6,9,12,16\). Each bound is attained by the explicit matrices in `check_zarankiewicz.py`; their \(C_4\)-freeness can also be checked by inspecting each pair of rows.

For every \(q\ge7\), take an \(q\times q\) circulant matrix whose row \(i\) has ones in columns \(i,i+1,i+3\) modulo \(q\). It has \(3q\) ones. The six ordered nonzero differences of \(\{0,1,3\}\) are \(\pm1,\pm2,\pm3\), pairwise distinct modulo every \(q\ge7\); thus any two rows share at most one occupied column, proving \(z_q\ge3q>3q-2\). For \(q\le5\), \(z_q<3q-2\), and for \(q=6\), \(z_q=3q-2=16\). This proves the sharp transition and the stated extremal-set census, using the disjoint-category multiplicity formula from step 3.

## Verification

The two supplied standalone Python 3 scripts use only the standard library. `check_visibility.py` enumerates every diameter-at-most-two subset by maximal-clique search (and then all submasks), independently evaluates each pair's actual geodesic visibility, and compares that direct predicate against the structural classification. For factor sizes \((2,2,2),(2,2,3),(2,3,3),(3,3,3),(2,3,4),(3,3,4)\), the pairs **(maximum size, number of maxima)** are respectively \((4,10),(5,12),(6,30),(7,27),(7,168),(8,36)\). The direct and classified predicates agree for every enumerated diameter-two subset; the largest checked instance has \(30{,}992\) candidate subsets. `check_zarankiewicz.py` verifies all six explicit small-order and circulant-bound ingredients described in the proof (square orders \(2\) through \(6\), and circulant orders \(7\) through \(30\)). The scripts are finite cross-checks; the general theorem follows from the written proof.

## Relationship to prior work

Cera López, García-Vázquez, Valenzuela-Tripodoro, and Yero introduced \(k\)-distance mutual visibility and established general bounds and several exact graph-class results (arXiv:2408.03976, first publicly posted 2024-08-07). Their isometric-subgraph lower bound does not imply the new upper bound for three-factor Hamming graphs. Cicerone, Di Stefano, and Klavžar proved that ordinary mutual visibility on \(K_r\square K_s\) equals the Zarankiewicz number \(Z(r,s)\) (arXiv:2112.13024, first publicly posted 2021-12-24). The present result uses that connection for coordinate planes but proves that every two-distance configuration outside those planes is trapped in a ball or tetrahedron; hence it also identifies exactly when the two-factor obstruction governs the three-factor optimum. Bujtás, Klavžar, and Tian studied **total** mutual visibility on three-factor Hamming graphs (arXiv:2307.05168), a distinct requirement involving all ambient vertex pairs rather than only selected pairs. The binary-cube instance \(q=2\) has also been characterized elsewhere and is included here solely for completeness. The claims of novelty are the nonbinary three-factor structural reduction, rectangular optimum/multiplicity formula, and equal-factor transition; prior two-factor and binary results are not claimed anew.

## Limitations

The formula for \(q\ge7\) deliberately retains the open Zarankiewicz extremal number and its optimal-matrix multiplicity; it is an exact reduction, not a closed numerical solution of that classical problem. The result applies only to exactly three complete-graph factors of orders at least two and to distance bound two. The finite scripts check explicit instances, not all parameter values. Literature searches and inspection of the most relevant accessible primary works did not reveal a covering nonbinary three-factor theorem, but unindexed or later publications remain a possible priority risk.

## References

1. M. Cera López, P. García-Vázquez, J. C. Valenzuela-Tripodoro, and I. G. Yero, *The \(k\)-distance mutual-visibility problem in graphs*, arXiv:2408.03976 (first version 2024-08-07), https://arxiv.org/abs/2408.03976.
2. S. Cicerone, G. Di Stefano, and S. Klavžar, *On the mutual visibility in Cartesian products and triangle-free graphs*, arXiv:2112.13024 (first version 2021-12-24), https://arxiv.org/abs/2112.13024.
3. C. Bujtás, S. Klavžar, and J. Tian, *Total mutual-visibility in Hamming graphs*, arXiv:2307.05168 (first version 2023-07-11), https://arxiv.org/abs/2307.05168.
