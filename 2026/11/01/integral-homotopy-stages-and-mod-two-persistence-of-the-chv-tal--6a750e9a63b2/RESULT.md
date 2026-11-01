# Integral homotopy stages and mod-two persistence of the Chvátal higher-independence filtration

## Finding

Let \(G\) be the standard twelve-vertex Chvátal graph specified by its complete edge list below. For each integer \(r\geq 1\), let \(K_r=\operatorname{Ind}_r(G)\) consist of the vertex subsets \(U\) such that **every connected component** of the induced graph \(G[U]\) has at most \(r\) vertices. These are nested simplicial complexes \(K_1\subseteq K_2\subseteq\cdots\subseteq K_{12}\). All homotopy statements use ordinary, integral homotopy equivalence.

**Theorem.** The complete filtration has the following homotopy types:

| Cutoff \(r\) | Integral homotopy type of \(K_r\) |
| --- | --- |
| 1 | \(S^2\) (previously known) |
| 2 | \(S^3\) |
| 3 | \(S^3\) |
| 4 | \(\bigvee^{64}S^3\) |
| 5 | \(\bigvee^{252}S^4\) |
| 6 | \(\bigvee^{382}S^5\) |
| 7 | \(\bigvee^{318}S^6\) |
| 8 | \(\bigvee^{165}S^7\) |
| 9 | \(\bigvee^{55}S^8\) |
| 10 | \(\bigvee^{11}S^9\) |
| 11 | \(S^{10}\) |
| 12 or greater | A point |

Each noncontractible stage is a torsion-free wedge of spheres in one dimension. The classification is complete for **this graph** and all possible integer cutoffs, not a claim about arbitrary four-chromatic graphs.

There is additional information not implied by these stagewise types. The complete positive-dimensional **persistent homology over \(\mathbb F_2\)** of the inclusions \(K_r\hookrightarrow K_{r+1}\), with intervals \([b,d)\) born at cutoff \(b\) and dying at cutoff \(d\), is:

| Homological dimension | Interval | Multiplicity |
| --- | --- | ---: |
| 2 | \([1,2)\) | 1 |
| 3 | \([2,5)\) | 1 |
| 3 | \([4,5)\) | 63 |
| 4 | \([5,6)\) | 252 |
| 5 | \([6,7)\) | 382 |
| 6 | \([7,8)\) | 318 |
| 7 | \([8,9)\) | 165 |
| 8 | \([9,10)\) | 55 |
| 9 | \([10,11)\) | 11 |
| 10 | \([11,12)\) | 1 |

There is also the single ordinary, essential degree-zero interval \([1,\infty)\). Thus one degree-three class persists through the three stages \(r=2,3,4\), while 63 additional degree-three classes appear only at \(r=4\). The barcode is **mod-two**, not an assertion about integral persistence maps.

## Assumptions and scope

Use vertices labeled `0` through `11`, with the following 24 unordered edges, and no other edges:

```text
(0,1) (0,4) (0,6) (0,9) (1,2) (1,5) (1,7) (2,3)
(2,6) (2,8) (3,4) (3,7) (3,9) (4,5) (4,8) (5,10)
(5,11) (6,10) (6,11) (7,8) (7,11) (8,10) (9,10) (9,11)
```

This is a four-regular, triangle-free, four-chromatic graph. The checker confirms the chromatic number by a complete three-coloring search and an explicit four-coloring. The graph, including its labeling, is thereby fixed; no graph-isomorphism recognition is required to replay the proof.

The empty vertex subset is included as the empty simplicial face. Its induced graph has no connected components, so it belongs to every \(K_r\). For a nonempty subset \(U\), define \(c(U)\) as the size of the largest component of \(G[U]\); define \(c(\varnothing)=0\). Then its filtration cutoff is \(\lambda(U)=\max(1,c(U))\), and \(U\in K_r\) precisely when \(\lambda(U)\le r\). Since the graph is connected on twelve vertices, \(K_{12}\) is the full eleven-dimensional simplex, while \(K_{11}\) is its boundary.

The notation \(\bigvee^a S^d\) means the one-point wedge of \(a\) copies of the standard \(d\)-sphere. Reduced integral homology follows from the homotopy table; all barcode assertions are over \(\mathbb F_2\).

## Proof

**1. Exhaustive finite face sets and acyclic matchings.** Encode a vertex subset \(U\) by the integer bit mask \(\sum_{v\in U}2^v\). For each of the 4096 masks, determine \(c(U)\) by breadth-first search in the induced graph and compute \(\lambda(U)\). This generates **every** face of each \(K_r\), not merely facets or a random sample.

For each \(r\), let \(L\) initially be the collection of all masks at filtration cutoff at most \(r\). Process pivots \(v=0,1,\ldots,11\) in order. For each pivot, scan the currently unmatched masks \(a\) in increasing numerical order and pair \(a\) with \(a\cup\{v\}\) whenever \(v\notin a\) and both masks remain unmatched. Remove both masks from \(L\) after pairing. This produces disjoint face-coface pairs of adjacent dimensions. Every matching includes the empty face paired with the singleton `0`; for the usual, nonaugmented face poset remove this one pair and retain the singleton as a critical base vertex. The verifier topologically sorts the *complete* directed face-poset Hasse diagram both before and after this removal, reversing exactly matched incidences. Consequently the matchings are acyclic, and Forman's discrete-Morse theorem gives one zero-cell together with the other critical cells listed below.

| \(r\) | Faces including empty | Matched pairs including empty pair | Other critical cells |
| ---: | ---: | ---: | --- |
| 1 | 127 | 63 | 1 in dimension 2 |
| 2 | 425 | 209 | 3 in dimension 2, 4 in dimension 3 |
| 3 | 729 | 360 | 3 in dimension 2, 5 in dimension 3, 1 in dimension 4 |
| 4 | 1176 | 548 | 72 in dimension 3, 8 in dimension 4 |
| 5 | 1804 | 771 | 257 in dimension 4, 5 in dimension 5 |
| 6 | 2590 | 1104 | 382 in dimension 5 |
| 7 | 3314 | 1498 | 318 in dimension 6 |
| 8 | 3797 | 1816 | 165 in dimension 7 |
| 9 | 4017 | 1981 | 55 in dimension 8 |
| 10 | 4083 | 2036 | 11 in dimension 9 |
| 11 | 4095 | 2047 | 1 in dimension 10 |
| 12 | 4096 | 2048 | None |

These are full counts: each line obeys \(2\cdot\text{pairs}+\text{other critical cells}=\text{faces}\). The complete directed Hasse graphs across all twelve stages contain 167,180 incidences; each is independently checked to be acyclic. In particular, no nontrivial critical one-cells remain.

**2. Exact integral attaching-degree computations.** Orient every simplex by increasing vertex labels. Its simplicial boundary has alternating signs. For a matched lower face \(a\) with matched upper face \(b\), use the unit coefficient \(\epsilon=\langle\partial b,a\rangle\in\{\pm1\}\) to project its chain recursively onto critical lower cells:

\[
P(a)=-\epsilon\sum_{\substack{t\subset b\\|t|=|a|,\ t\ne a}}
\langle\partial b,t\rangle P(t).
\]

For critical lower faces, \(P(a)=a\); for an upper member of a pair, \(P(a)=0\). Because the matching is acyclic, this recursive elimination is well founded. Projecting the boundary of each critical upper cell yields the exact integral Morse differential, not just ranks over a finite field. `VERIFY.py` reconstructs all differential entries and hashes each nonempty matrix; the hashes are also recorded in `MORSE_CERTIFICATES.json`.

Every nonempty Morse differential occurs in one of five cases:

| Stage and differential | Integer matrix shape | Explicit square minor | Determinant |
| --- | --- | --- | ---: |
| \(r=2\), \(\partial_3\) | \(3\times4\) | rows 0,1,2; columns 0,1,2 | \(-1\) |
| \(r=3\), \(\partial_3\) | \(3\times5\) | rows 0,1,2; columns 0,1,2 | \(-1\) |
| \(r=3\), \(\partial_4\) | \(5\times1\) | row 0; column 0 | \(-1\) |
| \(r=4\), \(\partial_4\) | \(72\times8\) | rows 1,8,10,12,14,16,18,26; all columns | \(-1\) |
| \(r=5\), \(\partial_5\) | \(257\times5\) | rows 3,14,31,43,121; all columns | \(-1\) |

Here row and column indices begin at zero, ordered by the integer masks of critical faces. The exact determinant algorithm uses fraction-free Gaussian elimination with integer division checks. The checker also verifies \(\partial_3\partial_4=0\) at \(r=3\).

For concreteness, at \(r=3\), the two successive integral Morse matrices are

\[
\partial_3=
\begin{pmatrix}
0&0&-1&-1&-1\\
1&0&1&0&0\\
-1&1&0&0&0
\end{pmatrix},
\qquad
\partial_4=
\begin{pmatrix}-1\\-1\\1\\-1\\0\end{pmatrix}.
\]

The chain relation holds, and both maps are primitive in the appropriate free abelian groups. No Morse boundary not appearing in the preceding table is nonzero.

**3. From these integral matrices to homotopy types.** Forman's theorem provides a CW complex with one base vertex and the displayed positive-dimensional critical cells. If all positive cells are of one dimension \(d\ge2\), every attaching map to the base vertex is constant and the CW complex is the stated wedge of \(d\)-spheres; this proves the entries \(r=1\) and \(6\le r\le11\). At \(r=12\) no positive cells remain.

For \(r=2,4,5\), there are cells only in consecutive dimensions \(d\) and \(d+1\), with \(d\ge2\). The \(d\)-skeleton is a wedge of \(d\)-spheres. By the Hurewicz isomorphism \(\pi_d(\bigvee S^d)\cong H_d(\bigvee S^d;\mathbb Z)\), attaching maps of the \((d+1)\)-cells are classified by their exact integral degree vectors. The displayed full-column-rank unimodular minor makes their images a primitive direct summand. Integral changes of basis of the free homotopy group and elementary cell cancellations yield the residual wedges of \(4-3=1\), \(72-8=64\), and \(257-5=252\) spheres, respectively.

At \(r=3\), the three two-cells and five three-cells have surjective primitive \(\partial_3\), so the three-skeleton is simply connected with \(\pi_2=0\), and has integral \(H_3\cong\mathbb Z^2\). It is therefore homotopy equivalent to a wedge of two three-spheres. The unique four-cell has primitive nonzero attaching-degree vector in \(\ker\partial_3\): the displayed \(\partial_4\) has a coefficient of \(-1\), and \(\partial_3\partial_4=0\). Since \(\ker\partial_3\) is a direct summand, this class is also primitive in the rank-two third homology. Attaching the four-cell eliminates one three-sphere, leaving precisely \(S^3\). This completes the stagewise **integral homotopy** proof.

There is also a direct structural explanation for the near-maximal entries. The graph is four-vertex-connected: exhaustive checks show that deleting at most three vertices leaves it connected, while deleting vertices `0,2,5,7` disconnects it. Consequently, for \(8\le r\le11\), every vertex set of size greater than \(r\) is connected and hence forbidden, while every set of size at most \(r\) is automatically allowed. Thus \(K_r\) is the full \((r-1)\)-skeleton of the eleven-simplex, a known wedge of \(\binom{11}{r}\) spheres of dimension \(r-1\). These near-maximal terms are included to make the filtration complete, not presented as independently surprising discoveries. The genuinely nontrivial Morse reductions occur at cutoffs two through seven.

**4. Inclusion maps and mod-two persistence.** Stagewise homotopy equivalences alone do not identify the maps between stages. The verification therefore separately orders every **nonempty** simplex by the triple `(cutoff, simplex dimension, integer mask)`, computes its complete ordinary boundary over \(\mathbb F_2\), and performs the standard column-reduction algorithm. Every filtration simplex is included, including those at the maximal cutoff; no bounded-dimensional truncation is used. Nonzero intervals produced by the pairing of column pivots are exactly those in the Finding table. All final unpaired births are the single ordinary degree-zero class. This proves the full mod-two barcode without inferring it from the wedge counts.

## Verification

The executable `VERIFY.py` requires only Python 3 and its standard library. Run `python3 VERIFY.py` from the directory containing the file; it prints `CHVATAL_HIGHER_INDEPENDENCE_FILTRATION_VERIFIED`, followed by exact face counts, matching counts, Hasse incidences, Morse-matrix SHA-256 hashes, unit-minor witnesses and the complete barcode. `CHECK_OUTPUT.txt` records output from a successful actual execution. `MORSE_CERTIFICATES.json` holds the numerical certificate summary; it is not a substitute for the executable exact construction.

Independent computational mechanisms are used for the integral Morse reduction and the ordinary mod-two persistence reduction. The former constructs all integer gradient-path differentials and verifies explicit determinant-one minors; the latter constructs the raw simplicial boundary columns without using the Morse matrices. The latter also checks the degree-by-degree Betti numbers implied by the homotopy table. A separate exact coloring backtrack confirms the graph's four-chromatic property. All 4096 subsets, all twelve cutoffs and every face-poset incidence are included.

## Relationship to prior work

Deshpande and Singh (arXiv:2001.05448, first public January 15, 2020) define higher-independence complexes and compute homotopy types for complete multipartite graphs, fully whiskered graphs, paths, cycles and perfect arity trees. Their definitions and homotopy question motivate this calculation, but the Chvátal graph is not one of their classified families. Abdelmalek and collaborators (arXiv:2106.10863) study higher-independence complexes primarily for chordal and tree-related classes; the nonchordal, triangle-free Chvátal graph is outside those hypotheses.

Ghosh and Selvaraja (arXiv:2505.06614) prove a general chordality theorem for the near-maximal cutoffs \(r\geq |V(G)|-2\), which may imply qualitative shellability at cutoffs ten and eleven. It does not give the exact homotopy counts for this graph at those cutoffs, any classification at cutoffs two through nine, or the persistence barcode. This existing stronger qualitative coverage at the two high cutoffs is explicitly acknowledged.

The **ordinary** independence complex of this exact Chvátal graph was already shown to be \(S^2\), together with a vertex-deletion dichotomy. Separately, an equivariant simplicial collapse connects that ordinary independence complex with the Lovász open-neighborhood complex. Those earlier results establish the \(r=1\) stage and are explicitly not claimed as new. The new core is the higher-cutoff integral homotopy classification **for \(2\le r\le7\)** together with the complete inter-stage persistent mod-two barcode. Classical high-cutoff simplex-skeleton entries and the known cutoff-one sphere are retained solely to give a self-contained complete filtration. Neither the known ordinary independence homotopy result nor its neighborhood-complex collapse implies that table or the nontrivial persistent interval \([2,5)\).

Relevant published results were checked by their objects and mathematical implications, not simply by searching for the graph name. In particular, an independence complex (induced components of size one) is only the initial stage of the present filtration. Known general chordal-graph wedge results do not apply to this nonchordal graph. Searches for higher independence, dissociation complexes, all cutoffs, the Chvátal graph and persistent homology located no equivalent classification in the inspected sources. This is a best-knowledge originality assessment, not a claim of exhaustive global priority.

## Limitations

The complete proof is an exhaustive finite calculation for a single canonically motivated graph and all of its twelve possible cutoffs. It is **not** a theorem for arbitrary triangle-free or four-chromatic graphs. The barcode coefficients are \(\mathbb F_2\), and the result does not determine integral persistence maps or equivariant homotopy types. Finite computations here are exhaustive for the stated finite object, not extrapolations to infinite families. The entire graph and all checker algorithms are specified so that the enumerations and critical integral minors can be reproduced.

A bibliographic residual risk is that equivalent higher-cutoff computations exist in unindexed literature or are implicit in a more general theorem not captured by the inspected primary sources. The homotopy types and persistence intervals have not received independent expert audit.

## References

1. P. Deshpande and A. Singh, *Higher Independence Complexes of graphs and their homotopy types*, arXiv:2001.05448 (first posted 2020-01-15), https://arxiv.org/abs/2001.05448.
2. F. M. Abdelmalek, P. Deshpande, S. Goyal, A. Roy and A. Singh, *Chordal graphs, higher independence and vertex decomposable complexes*, arXiv:2106.10863 (first posted 2021-06-21), https://arxiv.org/abs/2106.10863.
3. A. Ghosh and S. Selvaraja, *Chordality and Shellability of Higher Independence Complexes*, arXiv:2505.06614 (first posted 2025-05-10), https://arxiv.org/abs/2505.06614.
4. V. Chvátal, *The smallest triangle-free 4-chromatic 4-regular graph*, J. Combin. Theory **9** (1970), 93–94, DOI:10.1016/S0021-9800(70)80057-6.
5. R. Forman, *Morse theory for cell complexes*, Advances in Mathematics **134** (1998), 90–145, DOI:10.1006/aima.1997.1650.
6. *The Chvátal graph independence complex and its vertex-deletion dichotomy*, publicly indexed finite calculation, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-the-chv-tal-graph-independence-complex-and-its-vertex-deletion-d--676b14391238.
7. *An equivariant collapse connecting the Chvátal independence and neighborhood complexes*, publicly indexed finite calculation, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-an-equivariant-collapse-connecting-the-chv-tal-independence-and--3077dabdf181.
