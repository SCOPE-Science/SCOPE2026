# Three exact homotopy types for neighborhoods of maximal squared-cycle packings

## Finding
Let \(W_n=C_n^2\) be the graph on \(\mathbb Z/n\mathbb Z\) in which two distinct vertices are adjacent when their cyclic distance is at most two. Let \(H_k(W_n)\) have as vertices the independent \(k\)-sets of \(W_n\), two such vertices being adjacent precisely when the underlying sets are disjoint. Write \(\mathcal N(H)\) for the **open** Lovász neighborhood complex: a finite set of vertices is a face if it has a common graph neighbor.

For exactly the three parameters \(k\in\{2,3,4\}\) and \(n=3k+2\), the complete integral homotopy classifications are

\[
\mathcal N(H_2(W_8))\simeq S^2\vee S^2\vee S^3,\qquad
\mathcal N(H_3(W_{11}))\simeq S^3,\qquad
\mathcal N(H_4(W_{14}))\simeq S^3.
\]

These are homotopy equivalences, not merely equalities of Betti numbers. In particular the first case has reduced integral homology \(\mathbb Z^2\) in degree two and \(\mathbb Z\) in degree three; the other two have a single \(\mathbb Z\) in degree three. All remaining reduced integral homology groups vanish.

There is an immediate structural consequence. The canonical cover of each neighborhood complex whose nerve is the total \(k\)-cut complex of \(W_{3k+2}\) cannot be a good cover: the published total-cut homotopy types are \(S^4\) for \(k=2\) and \(S^5\) for \(k=3,4\), different from the three neighborhood homotopy types displayed above.

## Assumptions and scope
All graphs are finite, simple and without loops. For each tested \(k\), a \(k\)-set is independent in \(W_{3k+2}\) exactly when the cyclic gaps between consecutive selected points are all at least three. Such sets are *maximum* independent sets, because any independent set consumes three cyclic positions per selected point. The values \(k=2,3,4\), corresponding to \(n=8,11,14\), are the entire asserted range; no statement for larger \(k\) is claimed. There are \(12,22,35\) vertices in the respective disjointness graphs.

## Proof
The proof is finite and algorithmically exhaustive. A complete Python implementation is provided in `verify.py`; the argument below specifies the finite objects and checks that constitute the certificate.

**(1) Exact faces.** For each \(k\), enumerate every \(k\)-subset of \(\mathbb Z/(3k+2)\mathbb Z\) and test all pairwise cyclic distances to construct the independent sets. A second enumeration by cyclic gaps independently produces the same sets. Make the disjointness graph \(H_k\). Every nonempty simplex of \(\mathcal N(H_k)\) is a subset of the open neighborhood \(N_{H_k}(v)\) of at least one vertex \(v\). Enumerating every subset of each such neighborhood therefore exhausts all simplices, with no untested cases. The numbers of simplices **including the empty face** are \(911,16391,272861\), respectively. The respective ordinary face vectors, ordered by dimension starting at zero, are

\[
\begin{aligned}
k=2:&\ (12,66,204,304,228,84,12);\\
k=3:&\ (22,231,1133,2871,4301,4092,2519,979,220,22);\\
k=4:&\ (35,567,3920,14427,33502,53585,61684,52136,32459,14707,4704,1001,126,7).
\end{aligned}
\]

**(2) An explicitly reproducible matching.** Starting with all faces, including the empty face, choose the as-yet-unselected vertex with the largest number of available pairs \((\sigma,\sigma\cup\{v\})\); break ties using the specified fixed pseudorandom seed. Remove all these pairs and repeat, stopping when fewer than thirty faces remain. This yields, in the three cases, \(447,8182,136419\) matched pairs. The remaining critical-cell inventories, omitting the implicit basepoint added when the empty face was paired, are

\[
\begin{array}{c|l}
k&\text{critical cells by dimension}\ \\ \hline
2&9\text{ in degree }2,\ 8\text{ in degree }3\\
3&8\text{ in degree }2,\ 13\text{ in degree }3,\ 5\text{ in degree }4,\ 1\text{ in degree }5\\
4&1\text{ in degree }1,\ 11\text{ in degree }2,\ 11\text{ in degree }3.
\end{array}
\]

For each codimension-one incidence \(\sigma\subset\tau\), orient the Hasse edge \(\tau\to\sigma\), reversing it exactly when \((\sigma,\tau)\) is matched. A full topological sort processes every face: the three checks inspect \(3700,89089,1913226\) incidences, respectively. Thus the matching is acyclic, so the complex is homotopy equivalent to its Morse CW complex.

**(3) Exact integral attaching-degree matrices.** Fix the ascending-vertex orientation of each simplex. The boundary of an oriented simplex is the alternating sum of codimension-one faces. The differential between unmatched cells is calculated by signed gradient-path reduction: if a lower cell \(a\) is matched with an upper cell \(b\) with incidence \(\epsilon\in\{\pm1\}\), replace \(a\) by \(-\epsilon\) times the sum of the other facets of \(b\), and continue until only critical cells remain. This recursion is well-founded by acyclicity. Cells matched as upper partners vanish in the projection. The complete implementation constructs each resulting integer matrix and verifies that consecutive differentials compose to zero.

The nonzero Smith diagonals, with the degree of the differential indicated, are

\[
\begin{array}{c|l}
k&\text{nonzero diagonal entries}\ \\ \hline
2&\partial_3:\ 1\text{ repeated }7\text{ times}\\
3&\partial_3:\ 1\text{ repeated }8\text{ times};\ \partial_4:\ 1\text{ repeated }4\text{ times};\ \partial_5:\ 1\\
4&\partial_2:\ 1;\ \partial_3:\ 1\text{ repeated }10\text{ times}.
\end{array}
\]

All other matrix entries can be eliminated integrally without producing any nonunit invariant factor.

**(4) From integer differentials to homotopy.** For \(k=2\), the Morse CW complex starts with a point, nine two-cells and eight three-cells. Since \(\pi_2(\bigvee^9 S^2)\cong\mathbb Z^9\), the seven primitive degree vectors permit seven cellular homotopy cancellations. The final three-cell has zero attaching degree in the remaining two two-cells and hence attaches trivially. The result is \(S^2\vee S^2\vee S^3\).

For \(k=3\), there are no one-cells. Eight primitive three-cell attachments first cancel the eight two-cells, leaving five three-cells, five four-cells and one five-cell. Four primitive four-cell attachments then cancel four three-cells. The remaining four/five-cell pair has unit degree; any additional component of its attaching map in the surviving three-sphere can be removed by a triangular self-equivalence of \(S^3\vee S^4\). The result is one \(S^3\).

For \(k=4\), there is initially exactly one one-cell, and the primitive two-cell boundary has degree one around that circle, so these two cells cancel. The remaining ten two-cells and eleven three-cells have ten primitive independent degree vectors, yielding ten further homotopy cancellations and leaving one three-cell, hence \(S^3\). The cancellations in each case are justified by the exact unit Smith factors and the homotopy groups of the indicated sphere bouquets, not solely by equality of homology ranks.

## Verification
Run `python verify.py` in a directory containing `verify.py` and an installed version of SymPy compatible with `requirements.txt`. It reconstructs all vertices, neighborhoods, faces, matched pairs, codimension-one incidences and acyclicity checks, followed by signed integer Morse differentials and exact Smith normal forms. It independently compares direct cyclic-distance and gap enumerations; checks the full face vectors, critical cells and reduced homology ranks; and verifies consecutive Morse differentials compose to zero. The verified final line is `ALL_VERIFY_OK exact complete enumeration, Hasse acyclicity and integer Smith invariants`.

## Relationship to prior work
Shen, Song, Yu, Zhou and Zhuang, *Neighborhood Complexes of induced k-independent graphs* (arXiv:2512.09674, first posted 2025-12-10), define exactly the disjointness construction used here. Their Theorem 4.8 computes the neighborhood complex for \(W_{3k+1}\), while their Proposition 4.10 exhibits the total-cut complex as the nerve of a cover that need not be good. The present calculations address the first three instances of the adjacent previously untreated residue \(3k+2\).

The same authors' *Homotopy Type of Total Cut Complexes of Squared Cycle Graphs* (arXiv:2510.22574, first posted 2025-10-26), Theorem 1.6, establishes \(\Delta^t_k(W_{3k+2})\simeq S^5\) for \(k\ge3\); its subject is the total-cut complex, not the neighborhood complex of the disjointness graph on maximum independent sets. In the latter paper the known \(k=2\) total-cut type is \(S^{n-4}\) for \(n\ge7\). Thus neither theorem implies the new homotopy classifications; indeed the homotopy discrepancies prove the corresponding cover cannot be good in these three cases.

## Limitations
The result is a complete finite classification only for \(k=2,3,4\). It establishes no recurrence, does not determine all \(k\), and does not compute equivariant or persistent homology. A semantically equivalent computation in unindexed literature remains possible. No independent mathematical audit is asserted.

## References
1. Y. Shen, Z. Song, F. Yu, L. W. Zhou and J. Zhuang, *Neighborhood Complexes of induced k-independent graphs*, arXiv:2512.09674, initially posted 2025-12-10. https://arxiv.org/abs/2512.09674
2. Y. Shen, Z. Song, F. Yu, L. W. Zhou and J. Zhuang, *Homotopy Type of Total Cut Complexes of Squared Cycle Graphs*, arXiv:2510.22574, initially posted 2025-10-26. https://arxiv.org/abs/2510.22574
3. R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145.
