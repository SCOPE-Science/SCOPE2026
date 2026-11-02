# A diameter-three jump \(\gamma\)-graph for rectangular rook complements

## Finding

Let \(m,n\ge4\) be integers and let \(G_{m,n}=K_m\times K_n\) be the **categorical graph product**: its vertices are cells \((i,j)\in[m]\times[n]\), and two distinct cells are adjacent precisely when they lie in different rows **and** different columns. This is the complement of the \(m\)-by-\(n\) rook graph, not its Cartesian product.

Let \(J_{m,n}\) be the *jump minimum-domination reconfiguration graph*. Its vertices are the minimum dominating subsets of \(G_{m,n}\); two are adjacent precisely when one selected cell can be removed and one other cell inserted, preserving minimum domination. Then \(\gamma(G_{m,n})=3\), and the following conclusions hold for every \(m,n\ge4\):

1. \(J_{m,n}\) is connected and \(\operatorname{diam}(J_{m,n})=3\).
2. It has exactly \(L=mn(m-1)(n-1)\) vertices of *corner type*, each of degree \(d_L=mn-1\), and exactly \(T=6\binom{m}{3}\binom{n}{3}\) vertices of *matching type*, each of degree \(d_T=3((m-2)(n-2)+1)\).
3. Therefore
   \[|V(J_{m,n})|=L+T,\qquad |E(J_{m,n})|=\frac{L(mn-1)+3T((m-2)(n-2)+1)}2.\]
4. The jump graph is regular if and only if \(m=n=4\); in that case it has \(240\) vertices, degree \(15\), and \(1800\) edges.

The classification of minimum dominating triples used here is **previously known**; the new result is the diameter and degree structure of their reconfiguration graph, not their cardinality count.

## Assumptions and scope

All graphs are finite, simple and undirected. The two factors have orders \(m,n\ge4\). Domination is *closed-neighborhood domination*: a vertex in a dominating set dominates itself. A minimum dominating set has cardinality \(\gamma(G)\), not merely inclusion-minimality. A jump permits arbitrary replacement; no adjacency is required between the removed and inserted cells. Thus the assertion does **not** concern the slide \(\gamma\)-graph.

A *corner triple* has rows with occupancy pattern \((2,1)\) and columns with the same pattern, so it has the form \(\{(r,c),(r,d),(s,c)\}\) for distinct \(r,s\) and \(c,d\). A *matching triple* consists of three cells with pairwise distinct rows and pairwise distinct columns. These two families are disjoint.

## Proof

**1. Minimum dominating triples.** A set of at most two cells cannot dominate. For two in a common row (or column), an unselected cell in that row (or column) is not adjacent to either (here \(m,n\ge4\)); for two in distinct rows and columns, their two crossed cells are undominated. A corner triple dominates: if a cell is not adjacent to the two row-arm vertices, it is in their common row, where it is adjacent to the column-arm vertex unless selected; other cases follow symmetrically. A matching triple dominates because any unselected cell shares a row with at most one selected cell and a column with at most one, leaving at least one of the three selected cells adjacent to it. Hence \(\gamma(G_{m,n})=3\).

Conversely, a dominating triple cannot be contained in one row or column, since each has an unselected cell when \(m,n\ge4\). Suppose exactly two selected cells share row \(r\), at columns \(c\ne d\), and the third lies at \((s,e)\) with \(s\ne r\). Unless \(e\in\{c,d\}\), cell \((r,e)\) is unselected and undominated; hence the triple is a corner. The column-dual argument applies. If no row repeats and no column repeats, it is a matching triple. If no row repeats but a column repeats, the column-dual argument again forces a repeated row. Thus these are all minimum triples. This classification agrees with the previously recorded rook-complement counts [1,2]; it is included here to fix the precise domain of the jump graph.

The \(L\) corner triples have unique pivots \((r,c)\), with \(m-1\) possible second rows and \(n-1\) possible second columns. A matching triple chooses three rows, three columns, and a bijection, giving \(T\).

**2. Exact jump degrees.** Two distinct minimum triples are adjacent exactly when they share two cells. A matching triple has three pairs of retained cells. Each retained pair lies in distinct rows and columns; it can be completed to a matching triple in \((m-2)(n-2)\) ways or to a corner in two cross-completions. One completion is the old triple, so each pair gives \((m-2)(n-2)+1\) distinct neighbors. The three families of moves are disjoint; hence \(d_T=3((m-2)(n-2)+1)\).

For a corner \(\{(r,c),(r,d),(s,c)\}\), retaining its same-row pair yields \(2(m-1)-1=2m-3\) new corner completions; retaining its same-column pair yields \(2(n-1)-1=2n-3\). Retaining the pair of arms that share neither coordinate yields \((m-2)(n-2)+1\) new completions, as in the matching case. The three types of moves are disjoint. Their sum is \(mn-1\). Double-counting degrees gives the edge formula. Finally,
\[d_L-d_T=mn-1-3((m-2)(n-2)+1)=-2((m-3)(n-3)-1).\]
Both types occur for \(m,n\ge4\), so equality holds exactly when \((m-3)(n-3)=1\), namely \(m=n=4\).

**3. A bounded-support lemma establishes the universal diameter upper bound.** Given any two triples \(S,T\), their union uses at most six distinct row labels and six distinct column labels. Relabel these used rows and columns to an auxiliary \(p\)-by-\(q\) rectangle, with \(2\le p,q\le6\). The triples become two corner/matching triples in that rectangle. The finite-kernel lemma below guarantees a path of at most three one-cell exchanges between them in the auxiliary rectangle. Every intermediate triple is again a corner or a matching, which remains a minimum dominating triple when embedded back into the original \(m\)-by-\(n\) board by the characterization in step 1. Hence \(\operatorname{diam}(J_{m,n})\le3\) for every \(m,n\ge4\).

**Finite-kernel lemma.** For each of the \(25\) integer pairs \((p,q)\) with \(2\le p,q\le6\), the exchange graph on the corner/matching three-cell sets in \([p]\times[q]\) has diameter at most three. Here, for \(p<4\) or \(q<4\), the vertex family is **defined by these occupancy patterns**, not by the original graph's domination number. This finite statement is proved by the complete deterministic enumeration in `proof_checker.py`: the program lists all \(\binom{pq}{3}\) possible triples, filters the two defining patterns, constructs every exchange edge by exact shared-pair indexing, and verifies for **each vertex** that its closed three-step neighborhood is the entire vertex set. It checks all \(25\) pairs, with the largest auxiliary graph having \(3300\) vertices. The complete source is embedded, has no nonstandard dependencies, and may be run with `python3 proof_checker.py`. This is an exact finite proof of a bounded-support lemma, not extrapolation from small board sizes.

**4. Sharpness.** For \(m,n\ge4\), the two valid corner triples \(\{(1,1),(1,2),(2,1)\}\) and \(\{(3,3),(3,4),(4,3)\}\) are disjoint. Since one jump changes just one cell, at least three jumps are needed between them. Combining with step 3 gives diameter exactly three.

## Verification

Run `python3 proof_checker.py` using Python 3's standard library. The program prints `ALL_ASSERTIONS_PASSED` only after every finite-kernel pair has passed the three-step reachability test. It also independently checks the triple-shape criterion against **direct closed-neighborhood domination in the actual categorical products** for all triples in the \(4\times4\), \(4\times5\), \(4\times6\), \(5\times5\), \(5\times6\), and \(6\times6\) boards. This comprises \(17{,}224\) direct predicate comparisons, plus exact degree and count comparisons. A saved stdout transcript is included as `checker_output.txt`.

The reason finite verification suffices for the infinite diameter statement is the explicit **at-most-six-active-rows-and-columns reduction** in step 3. The program does not attempt an impossible exhaustive check of infinitely many graphs; the nonstandard finite-kernel lemma is the only computational lemma needed for the upper bound.

## Relationship to prior work

The established count and classification of minimum dominating sets in square rook complements appears in OEIS A292074 (2017) [1], and the complete minimal-dominating-set census for rectangular rook complements appears in OEIS A384123 (2025) [2]. Both cover the basic shape classification used in step 1, so no originality is claimed for it. They do not state or imply the exchange graph's diameter, the two degree formulas, or the regularity transition.

Mynhardt and Nasserasr [3] give the precise definition of the jump \(\gamma\)-graph and survey results on trees, paths, cycles, Harary graphs and other classes. In particular, general induced-subgraph containment in a Johnson graph does **not** imply preservation of Johnson-graph distances. Rall [4] classifies well-dominated direct products, including the exceptional \(K_3\times K_3\) case, but gives no diameter or degree characterization for the jump graph of the products considered here.

## Limitations

The claim concerns **jump**, not slide, reconfiguration, and requires both factor orders to be at least four. It does not assert that the jump graph is Hamiltonian, vertex-transitive, or distance-regular, or that its full distance distribution is known. The diameter proof relies on a reproducible exact finite enumeration of the \(25\) bounded-support cases. Priority searches cannot exclude every unindexed or differently worded publication; no independent mathematical audit has been performed.

## References

[1] OEIS A292074, *Number of minimum dominating sets in the \(n\times n\) rook complement graph*, first dated 2017-09-12; 2017-09-13 comment gives the two triple shapes. https://oeis.org/A292074

[2] OEIS A384123, *Number of minimal dominating sets in the \(n\times m\) rook complement graph*, dated 2025-05-20. https://oeis.org/A384123

[3] C. M. Mynhardt and S. Nasserasr, *Reconfiguration of Colourings and Dominating Sets in Graphs: a Survey* (2020), arXiv:2003.05956v1, especially Sections 1 and 4.3–4.4. https://arxiv.org/pdf/2003.05956

[4] D. F. Rall, *On well-dominated direct, Cartesian and strong product graphs* (2021), arXiv:2105.09797v1. https://arxiv.org/pdf/2105.09797
