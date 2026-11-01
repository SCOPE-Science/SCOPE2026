# Neighborhood homology distinguishes all four strongly regular \((28,12,6,4)\) graphs

## Finding
Let \(G\) be a finite simple graph with \(28\) vertices, regular degree \(12\), and exactly \(6\) (respectively \(4\)) common neighbors for each adjacent (respectively nonadjacent) pair. There are precisely four isomorphism classes: the triangular graph \(T_8=L(K_8)\) and three Chang graphs. For the Lovász open-neighborhood complex \(\mathcal N(G)\), the complete reduced homology over \(\mathbb F_2\) is as follows; every degree not displayed has zero reduced homology.

| Graph | Nonzero reduced mod-two homology |
| --- | --- |
| \(T_8\) | \(\widetilde H_3\cong\mathbb F_2^{553}\), \(\widetilde H_5\cong\mathbb F_2^8\) |
| Four-matching-switched Chang graph | \(\widetilde H_3\cong\mathbb F_2^{253}\), \(\widetilde H_4\cong\mathbb F_2^{12}\) |
| Eight-cycle-switched Chang graph | \(\widetilde H_2\cong\mathbb F_2\), \(\widetilde H_3\cong\mathbb F_2^{166}\), \(\widetilde H_4\cong\mathbb F_2^4\) |
| Disjoint triangle-and-pentagon-switched Chang graph | \(\widetilde H_2\cong\mathbb F_2^2\), \(\widetilde H_3\cong\mathbb F_2^{175}\), \(\widetilde H_4\cong\mathbb F_2^{24}\) |

The four reduced homology signatures differ pairwise, although these four graphs have identical strongly regular parameters and adjacency spectra. In particular, their neighborhood complexes are pairwise not homotopy equivalent. This statement does **not** determine integral homology or individual homotopy types.

## Assumptions and scope
Set \(V=\binom{\{0,1,\ldots,7\}}{2}\). The graph \(T_8\) has vertex set \(V\), and vertices \(a,b\) are adjacent exactly when \(|a\cap b|=1\). For a subset \(S\subseteq V\), its Seidel switch replaces adjacency by nonadjacency precisely for pairs with exactly one member in \(S\). Retain adjacency within \(S\) and within \(V\setminus S\).

The three switching sets are explicitly:

1. Four disjoint edges of \(K_8\): \(\{01,23,45,67\}\).
2. The eight edges of the Hamiltonian cycle \(01,12,23,34,45,56,67,70\).
3. The three edges \(01,12,02\) together with five edges \(34,45,56,67,73\).

Here \(ab\) abbreviates the graph vertex \(\{a,b\}\); only these displayed combinatorial labels use shorthand. Under the standard classification of strongly regular graphs, these switches give precisely the three Chang classes, and together with \(T_8\) exhaust the parameter class.

For a simple graph \(G=(V,E)\), define \(\mathcal N(G)=\{\sigma\subseteq V:\exists v\in V\ \forall u\in\sigma,\;uv\in E\}\). The empty simplex is included, and a nonempty simplex has some common adjacent vertex. In this paper, all chain groups and Betti ranks refer to reduced simplicial homology with coefficients in \(\mathbb F_2\). Graph isomorphism invariance and the stated graph-family classification justify extending the four explicit computations to **every** graph of these parameters.

## Proof
The bundled `verify.py` enumerates all \(28\) two-subset vertices in lexicographic order and applies each switch exactly as defined. It directly checks, for every vertex and unordered pair, all degree and common-neighbor identities \((28,12,6,4)\). The four graphs have different pairs of clique counts \((c_4,c_6)=(280,56),(248,8),(240,0),(240,3)\), an independent check of pairwise nonisomorphism. The classical Chang classification ensures there are no missing isomorphism classes.

For any one of these graphs, each open neighborhood contains precisely \(12\) graph vertices. Thus every simplex belongs to some one of the \(28\) full simplices on open neighborhoods, and an exact face enumeration is obtained by taking the union of **all** subsets of each neighborhood. Two independent generators perform this construction: binary submask enumeration and literal combinations of every subset cardinality. They agree on every face, not merely on cardinalities. The resulting nonempty face totals are respectively \(105896,105896,105832,105868\). The full face counts by dimension appear in `verification_output.txt`; these totals include every dimension from zero through eleven, while the empty simplex is stored separately.

For dimension \(k\ge1\), the verifier constructs the full mod-two boundary matrix column-by-column: each \(k\)-simplex contributes its \(k+1\) codimension-one faces, without signs in characteristic two. Exact binary Gaussian elimination determines the rank of every matrix. Writing \(f_k\) for the number of \(k\)-simplices and \(r_k\) for the rank of the boundary from dimension \(k\) to \(k-1\), the Betti formula is \(\beta_k=f_k-r_k-r_{k+1}\) for positive degrees; in dimension zero, subtract one for reduced homology. For example, for \(T_8\), the full calculation gives \(\beta_3=11410-2449-8408=553\) and \(\beta_5=25704-12760-12936=8\). For the eight-cycle switch it gives \(\beta_2=2968-351-2616=1\), \(\beta_3=11178-2616-8396=166\), and \(\beta_4=21168-8396-12768=4\). All other entries follow from the complete vectors and ranks in the bundled reproducibility record; each is an exact integer subtraction, not a numerical fit.

As a structurally separate check, the verifier performs an explicit sequence of valid elementary simplicial collapses, always removing a face having a **unique codimension-one coface** together with that coface. A higher coface would imply a second codimension-one coface, so the chosen lower face is genuinely free. The \(49150,50538,51041,50161\) collapse pairs reduce the four complexes to \(7596,4820,3750,5546\) nonempty simplices. The remaining faces form simplicial complexes; independent binary elimination using the *opposite pivot convention* yields exactly the same reduced Betti groups as the full boundary calculation. The exact Euler–Poincaré identity holds before and after all collapses. These checks determine the entire homology over \(\mathbb F_2\), because every boundary group and kernel dimension in all dimensions is accounted for.

Distinct reduced homology signatures imply pairwise non-homotopy-equivalence. The graph classification then proves the claim for every \((28,12,6,4)\) strongly regular graph.

## Verification
Run `python3 verify.py` with Python 3.10 or newer; no external packages or downloaded datasets are required. The program prints the complete face vectors, full and collapsed boundary ranks, collapse counts, four- and six-clique counts, and mod-two Betti signatures for all four graphs. The embedded `verification_output.txt` is the recorded standard output from the same source. The final line must be `VERIFY_FOUR_28_VERTEX_NEIGHBORHOOD_COMPLEXES_EXACT_MOD2_PASS`.

A full independent-from-input check reconstructs all four graphs and their faces from formulas, and compares two face-generation implementations exactly. The separate collapsed-complex elimination is a second complete chain calculation. No sampling, floating-point rank, timeout-based inference, or extrapolation to other graph families is used.

## Relationship to prior work
Matsushita and Wakatsuki (first publicly available December 5, 2023) establish Alexander duality between dominance and neighborhood complexes and applications to selected graph families. Their theorem motivates exact neighborhood-topology computations but does not calculate these four strongly regular examples. The published classification of Chang graphs and the SageMath graph descriptions establish the four graph representatives, **not** their neighborhood-complex homology.

An accessible prior computation entitled *Mixed-dimensional mod-two neighborhood homology first appears at \(T_7\)* determines the triangular-graph neighborhood-complex mod-two Betti ranks through \(T_7\), explicitly without claiming anything for \(n\ge8\). Its \(T_7\) rank pair \((246,7)\) is not a special case or a stronger result implying the new \(T_8\) profile or the three switched graphs. Fröberg's 2026 investigation analyzes Stanley–Reisner rings and linear resolutions for other graph classes, not the four topological homology profiles here. Related clique-complex calculations for line graphs concern a different simplicial construction. Searches for the four graph aliases, Hom-complex formulations and exact homology signatures located no covering calculation; lack of a search hit is not itself a proof of novelty.

## Limitations
This is a complete finite theorem **only for the four parameter-class graphs** and **only over \(\mathbb F_2\)**. It does not establish torsion-freeness, integral homology groups, homotopy decompositions, or corresponding classifications for other strongly regular parameters. The comparison with indexed and accessible literature cannot exclude equivalent calculations under less searchable terminology; in particular, an unindexed computation of \(\operatorname{Hom}(K_2,G)\) may encode the same invariant. Exact computational certificates prove the stated finite facts but are not a claim of independent validation.

## References
1. T. Matsushita and S. Wakatsuki, *Dominance complexes, neighborhood complexes and combinatorial Alexander duals*, arXiv:2312.02639v1 (2023-12-05), https://arxiv.org/abs/2312.02639.
2. E. W. Weisstein, *Chang Graphs*, MathWorld, https://mathworld.wolfram.com/ChangGraphs.html; SageMath documentation, *ChangGraphs*, https://doc.sagemath.org/html/en/reference/graphs/sage/graphs/generators/families.html.
3. *Mixed-dimensional mod-two neighborhood homology first appears at \(T_7\)*, published scientific record, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-mixed-dimensional-mod-two-neighborhood-homology-first-appears-at--5026f3f1e8ec.
4. R. Fröberg, *Stanley–Reisner rings of neighborhood complexes and linear resolutions*, Journal of Algebraic Combinatorics 63, article 56 (2026), https://doi.org/10.1007/s10801-026-01530-x.
