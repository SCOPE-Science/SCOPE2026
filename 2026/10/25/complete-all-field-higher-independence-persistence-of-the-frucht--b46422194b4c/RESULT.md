# Complete all-field higher-independence persistence of the Frucht graph

## Finding
Let \(F\) be the labeled twelve-vertex Frucht graph defined below. For an integer \(r\ge 1\), let \(K_r=\operatorname{Ind}_r(F)\), with simplices the vertex sets whose induced graph components have at most \(r\) vertices. Then the nested filtration \(K_1\subseteq\cdots\subseteq K_{12}\) has the following **complete positive-degree persistent-homology barcode over every field**. Each displayed interval is half-open, and the indicated multiplicity is exact.

| Homological degree | Interval | Multiplicity |
| --- | --- | ---: |
| \(2\) | \([1,2)\) | 3 |
| \(3\) | \([2,3)\) | 1 |
| \(4\) | \([5,6)\) | 1 |
| \(5\) | \([3,4)\) | 16 |
| \(5\) | \([3,7)\) | 1 |
| \(5\) | \([6,7)\) | 32 |
| \(6\) | \([7,8)\) | 128 |
| \(7\) | \([8,9)\) | 135 |
| \(8\) | \([9,10)\) | 55 |
| \(9\) | \([10,11)\) | 11 |
| \(10\) | \([11,12)\) | 1 |

The ordinary degree-zero barcode consists of one essential interval \([1,\infty)\). The displayed bars are all positive-degree bars; there are no further positive-degree essential intervals. Notably, one degree-five class persists from \(r=3\) through \(r=6\), whereas the other sixteen classes born at \(r=3\) die upon entering \(r=4\).

Every integral homology group of every stage is torsion-free. Their only nonzero **reduced** integral homology groups are:

| \(r\) | Reduced integral homology |
| --- | --- |
| \(1\) | \(\widetilde H_2\cong\mathbb Z^3\) (previously known) |
| \(2\) | \(\widetilde H_3\cong\mathbb Z\) |
| \(3\) | \(\widetilde H_5\cong\mathbb Z^{17}\) |
| \(4\) | \(\widetilde H_5\cong\mathbb Z\) |
| \(5\) | \(\widetilde H_4\cong\mathbb Z\) and \(\widetilde H_5\cong\mathbb Z\) |
| \(6\) | \(\widetilde H_5\cong\mathbb Z^{33}\) |
| \(7\) | \(\widetilde H_6\cong\mathbb Z^{128}\) |
| \(8\) | \(\widetilde H_7\cong\mathbb Z^{135}\) |
| \(9\) | \(\widetilde H_8\cong\mathbb Z^{55}\) |
| \(10\) | \(\widetilde H_9\cong\mathbb Z^{11}\) |
| \(11\) | \(\widetilde H_{10}\cong\mathbb Z\) |
| \(r\ge 12\) | Zero |

For \(r=1,2,3,4,6,7,8,9,10,11\), the corresponding **integral homotopy types** are wedges of spheres in exactly the indicated homology degrees and multiplicities; \(K_r\) is contractible for \(r\ge12\). In particular, the new threshold-two case is \(K_2\simeq S^3\). At \(r=5\), only the integral homology and persistence assertions are made: a wedge-of-spheres homotopy type is **not** claimed.

## Assumptions and scope
The graph has vertices \(\{0,1,\ldots,11\}\) and exactly these undirected edges, stated here to remove all graph-labeling ambiguity:

```python
EDGES = ((0,1),(0,6),(0,7),(1,2),(1,7),(2,3),(2,8),(3,4),(3,9),
         (4,5),(4,9),(5,6),(5,10),(6,10),(7,11),(8,9),(8,11),(10,11))
```

This is the standard Frucht graph, a cubic graph with trivial automorphism group; its twelve-vertex, eighteen-edge identity and LCF representation are documented by MathWorld. The filtration parameter is an **integer** counting the maximum size of a connected component of the induced subgraph on a selected vertex set. At \(r=1\), the ordinary independence complex is obtained. At \(r\ge12\), the full eleven-simplex is obtained. The homology statement uses singular or simplicial homology, with no coefficient restrictions for the interval statement beyond the assumption that coefficients form a field.

## Proof
**Exhaustive face criterion.** For each of the \(2^{12}=4096\) vertex masks \(U\), compute the largest cardinality \(c(U)\) of a component of \(F[U]\), with \(c(\varnothing)=0\). Then \(U\in K_r\) if and only if \(c(U)\le r\). Each tested subset is represented by a distinct integer mask, and the verifier explicitly checks the downward-closed property. For \(r=1,\ldots,12\), the numbers of faces **including** the empty face are respectively
\[
169,\ 825,\ 1593,\ 2281,\ 2798,\ 3211,\ 3540,\ 3827,\ 4017,\ 4083,\ 4095,\ 4096.
\]

**Acyclic Morse model.** Work on the full face poset including the empty face. For vertices \(v=0,1,\ldots,11\) in order, match each still-unmatched face \(\sigma\) not containing \(v\) to \(\sigma\cup\{v\}\), whenever that latter face is still unmatched. After every vertex, remove all just-matched pairs. For every \(r\), the supplied verifier reverses every matched Hasse edge, constructs every remaining oriented codimension-one incidence, and topologically sorts the **entire** graph. All incidences are accounted for and the directed graph is acyclic. This certifies an acyclic discrete-Morse matching, not merely a favorable homology calculation. The empty face is always paired; consequently the reduced Morse complex may be read with an added basepoint. Here is the complete critical-cell and adjacent integer Morse-boundary rank census:

| \(r\) | Critical cells by dimension | Nonzero adjacent boundary ranks |
| --- | --- | --- |
| 1 | \(4\) in degree \(2\), \(1\) in degree \(3\) | \(\operatorname{rank}\partial_3=1\) |
| 2 | \(2\) in degree \(3\), \(1\) in degree \(4\) | \(\operatorname{rank}\partial_4=1\) |
| 3 | \(2\) in degree \(4\), \(19\) in degree \(5\) | \(\operatorname{rank}\partial_5=2\) |
| 4 | \(1\) in degree \(4\), \(6\) in degree \(5\), \(4\) in degree \(6\) | \(\operatorname{rank}\partial_5=1\), \(\operatorname{rank}\partial_6=4\) |
| 5 | \(1\) in degree \(4\), \(3\) in degree \(5\), \(3\) in degree \(6\), \(1\) in degree \(7\) | \(\operatorname{rank}\partial_6=2\), \(\operatorname{rank}\partial_7=1\) |
| 6 | \(36\) in degree \(5\), \(3\) in degree \(6\) | \(\operatorname{rank}\partial_6=3\) |
| 7–11 | Respectively \(128,135,55,11,1\) in degrees \(6,7,8,9,10\) | All zero |
| 12 | None | All zero |

For a face \(\rho\) in a fixed dimension, the integral Morse projection \(R(\rho)\) is defined recursively as follows. A critical \(\rho\) maps to its own basis vector; a face paired **downward** maps to zero; a face \(\rho\) paired **upward** with \(\tau\) maps to
\[
R(\rho)=-\frac{1}{[\tau:\rho]}
\sum_{\substack{\eta\prec\tau\\\eta\ne\rho}}
 [\tau:\eta]R(\eta),
\]
where the signed simplicial incidence \([\tau:\eta]\) is \(+1\) or \(-1\). Acyclicity makes this recursion well founded. Apply \(R\) to the ordinary signed boundary of each critical cell. All integer Morse differentials are computed with the displayed expression, and adjacent products are verified to vanish. For every resulting matrix, exact integral row-and-column operations find the indicated number of **unit** pivots and leave an all-zero residual matrix. Thus every nonzero Smith invariant factor is \(1\); the integral homology table follows. At \(r=2\), the critical cell masks are \(834\) and \(1100\) in degree three and \(740\) in degree four, with the latter's Morse boundary coefficients \(0\) and \(1\). This yields \(K_2\simeq S^3\), not just its third Betti number.

**Other homotopy types.** At \(r=1,2,3,6\), the Morse CW complex has cells in only two consecutive positive dimensions, with all nonzero boundary pivots units. The lower-dimensional skeleton is a wedge of spheres of dimension at least \(2\); its corresponding homotopy group in the attaching dimension is a free abelian group described by the degree vectors. Primitive integer row/column changes and cancellation of those unit-degree pairs leave exactly the displayed number of equal-dimensional sphere summands. At \(r=4\), first cancel the unit \(4\)-to-\(5\) pair, then cancel the four unit \(5\)-to-\(6\) pairs; the remaining CW complex has just one five-cell and a basepoint. At \(r=7,\ldots,11\), only one positive critical dimension occurs, giving the stated sphere wedges immediately. At \(r=12\), all nonempty cells are paired apart from the basepoint, giving a contractible complex. For \(r=5\), the ranks and Smith factors prove the homology statement but do not rule out unstable higher attaching maps; no unwarranted homotopy splitting is inferred.

**Persistence maps.** Independently of the Morse reduction, order **all 4096 simplices** by \((c(U),|U|,U)\) and reduce their **signed integer** boundary columns against the highest previously retained pivot. The complete algorithm and every tie-break are in `verify_frucht_higher.py`. Exactly 2048 pivot pairs arise, and **each pivot coefficient is \(+1\) or \(-1\)**; hence the column reductions work without division over \(\mathbb Z\) and remain valid over every field. Discard bars whose endpoints occur at the same parameter and the augmented empty-face bar \([0,1)\). The resulting nonzero-length positive-degree pair counts are precisely the eleven barcode rows given above. A separate mod-two bitset reduction produces the same 2048 pairings, including tie-breaking. This proves the persistence statement over arbitrary fields, rather than inferring intervals only from stagewise Betti numbers.

## Verification
Run `python3 verify_frucht_higher.py` with Python 3; no third-party libraries or external data are required. The program enumerates all \(4096\) vertex subsets, independently computes their induced-component sizes, forms each filtered face poset, verifies **every** oriented Hasse incidence for the discrete-Morse matching, computes complete signed Morse differentials, verifies all chain identities and unit Smith pivots, and carries out two direct full-filtration persistence reductions (integer and mod two). The final successful output is `COMPLETE_VERIFY_OK`. These finite checks are **exhaustive for this fixed twelve-vertex graph**, not extrapolations to other graphs or arbitrary graph sizes.

## Relationship to prior work
Deshpande and Singh introduced a systematic discrete-Morse study of higher-independence complexes, determining graph families including complete multipartite, fully whiskered, path, cycle and perfect rooted-tree classes; none of those general results specializes to this nonchordal, asymmetric cubic graph. Sawant's May 24, 2026 preprint proves vertex decomposability for all tree higher-independence complexes, making extension beyond trees natural; it does not compute the filtration of the Frucht graph. The previously published ordinary Frucht graph independence complex satisfies \(K_1\simeq\bigvee^3S^2\), including a vertex-deletion classification. That known first stage is **not claimed as new**. The present full all-field barcode, the new threshold-two sphere, and the remaining higher-stage homology and specified homotopy types are logically additional: the ordinary first-stage result and tree theorem do not determine the inclusion-induced maps through thresholds \(2,\ldots,12\).

## Limitations
The result is an exhaustive **finite case** for the graph named above, not a theorem for all cubic, asymmetric, or nonchordal graphs. It determines homology and field-valued persistence at every integer threshold, and homotopy at every stage **except \(r=5\)**. In that exceptional stage, vanishing torsion in homology does not by itself eliminate unstable attaching-map phenomena. The persistence assertion is about homology with coefficients in a field and makes no unproved blanket interval-decomposition claim for arbitrary integral persistence modules. Exact computation is a proof only because every vertex subset, incidence, Morse matching, and needed integer reduction is exhaustively checked; no partial enumeration is treated as complete. As with any literature comparison, priority cannot be ruled out absolutely for inaccessible or unindexed work; no independent scientific audit is claimed.

## References
1. R. Sawant, *On the Vertex Decomposability of r-Independence Complexes of Trees*, arXiv:2605.25150, first public version May 24, 2026, https://arxiv.org/abs/2605.25150.
2. P. Deshpande and A. Singh, *Higher Independence Complexes of graphs and their homotopy types*, arXiv:2001.05448, first submitted January 15, 2020, https://arxiv.org/abs/2001.05448.
3. E. W. Weisstein, *Frucht Graph*, MathWorld, https://mathworld.wolfram.com/FruchtGraph.html.
4. *The Frucht graph independence complex and its complete vertex-deletion classification*, public record and proof, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-the-frucht-graph-independence-complex-and-its-complete-vertex-de--8b7d9b2243c2.
5. R. Forman, *Morse Theory for Cell Complexes*, Advances in Mathematics 134 (1998), 90–145.
