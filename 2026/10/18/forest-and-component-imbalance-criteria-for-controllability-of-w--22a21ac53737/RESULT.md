# Forest and component-imbalance criteria for controllability of weighted rook networks

## Finding
For integers \(p,q\ge2\) and real \(a,b>0\), let \(L=aL(K_p)\otimes I_q+bI_p\otimes L(K_q)\) be the direction-weighted Laplacian of the rectangular rook graph on cells \((i,j)\). For a set \(S\) of cells, let \(B_S\) have exactly one unit-coordinate input column per cell in \(S\), and consider \(\dot z=-Lz+B_Su\). Make two bipartite graphs on the **same** vertex set of \(p\) row-vertices and \(q\) column-vertices: \(H_S\) contains precisely the **unselected** cells as row–column edges; \(F_S\) contains the **selected** cells.

**Exact criterion.** If \(ap\ne bq\), the pair is controllable if and only if \(H_S\) is a forest. If \(ap=bq\), it is controllable if and only if \(H_S\) is a forest and the following component condition holds. Let \(C_1,\ldots,C_t\) be *all* connected components of \(F_S\), including isolated row/column vertices; let \(r_c\) and \(s_c\) be the counts of row and column vertices in \(C_c\). Then either \(t=1\), or \(t=2\) and \(r_1s_2\ne r_2s_1\). In particular, \(t\ge3\) is never admissible at resonance.

**Minimum actuator number.** With one independent scalar input at each selected vertex, the exact minimum is
\[
\gamma(p,q;a,b)=\begin{cases}
(p-1)(q-1),&ap\ne bq,\\
(p-1)(q-1),&ap=bq\text{ and }p,q\ge3,\\
\max\{p,q\},&ap=bq\text{ and }\min\{p,q\}=2.
\end{cases}
\]
At nonresonance, **every** minimum placement is the complement of a spanning tree of \(K_{p,q}\); thus there are exactly \(p^{q-1}q^{p-1}\) labeled minimum placements. At resonance, a rectangular \((p-1)\)-by-\((q-1)\) patch fails, but for \(p,q\ge3\) a different placement of the same cardinality attains the bound.

## Assumptions and scope
The graphs are finite and simple, with \(p,q\ge2\). Each of the \(p\) row indices is completely connected along its column direction with edge weight \(a\), and each of the \(q\) column indices along its row direction with edge weight \(b\), according to the displayed Kronecker-sum normalization. The signs in \(\dot z=-Lz+B_Su\) have no influence on controllability. The inputs are *independent terminal inputs*, not one shared input across all selected vertices and not arbitrary dense control vectors. Graph components always include isolated vertices. The theorem is for exact fixed weights; no generic-weight or strong-structural controllability claim is made.

## Proof
**1. Eigenspaces.** Write \(\mathbf1_p\) and \(\mathbf1_q\) for constant vectors and \(U_p=\{f\in\mathbb R^p:\sum_i f_i=0\}\), with \(U_q\) analogously. Since \(L(K_p)=pI_p-J_p\), the four mutually orthogonal eigenspaces are
\[
\mathbf1_p\otimes\mathbf1_q:\ 0,\qquad
U_p\otimes\mathbf1_q:\ ap,\qquad
\mathbf1_p\otimes U_q:\ bq,\qquad
U_p\otimes U_q:\ ap+bq.
\]
The last space consists exactly of real \(p\)-by-\(q\) arrays \(X\) with every row sum and every column sum zero; it has dimension \((p-1)(q-1)\). The middle spaces merge when, and only when, \(ap=bq\). For a real symmetric state matrix, the PBH test says that no nonzero vector in any **whole** eigenspace may vanish on all selected coordinates.

**2. Forest test for the interaction eigenspace.** An array \(X\) in \(U_p\otimes U_q\) vanishes on \(S\) precisely when its support lies among the edges of \(H_S\), with signed edge values having zero sum at every row and column vertex. Such an array is a circulation after consistently orienting all edges from rows to columns. A cycle supports a nonzero alternating \(+1,-1\) circulation. Conversely, on a forest any zero-divergence edge assignment is zero: remove a leaf, whose incident edge must have coefficient zero, and iterate. Thus restriction to \(S\) is injective on the interaction eigenspace exactly when \(H_S\) is acyclic.

**3. Nonresonant remaining eigenspaces.** If a mean-zero row vector \(f\) vanishes through all selected cells, every row index supporting a nonzero \(f_i\) must be entirely unselected. Two entirely unselected rows would put the four edges of \(K_{2,2}\) in \(H_S\), contradicting acyclicity (since \(q\ge2\)). Hence at most one row can be entirely unselected. A mean-zero vector supported on at most one row must vanish. The same argument, interchanging rows and columns, applies to \(U_q\). The zero eigenspace is detected whenever \(S\) is nonempty; a forest \(H_S\) cannot equal all of \(K_{p,q}\), since \(p,q\ge2\). This proves the nonresonant equivalence.

**4. Resonant component condition.** At \(ap=bq\), each vector in the merged middle eigenspace is the array \(Y_{ij}=f_i+g_j\), where \(\sum_i f_i=\sum_j g_j=0\); this representation is unique. The equations \(Y_{ij}=0\) on selected edges imply that on each connected component \(C_c\) of \(F_S\), all present row-values equal one parameter \(t_c\), and all present column-values equal \(-t_c\). This includes components consisting of a single isolated vertex. The two centering equations reduce **exactly** to
\[
\sum_{c=1}^t r_ct_c=0,\qquad \sum_{c=1}^t s_ct_c=0.
\]
There is no nonzero solution if and only if the \(2\)-by-\(t\) component-count matrix has full column rank. Since each component contains at least one vertex, this occurs for \(t=1\), or for \(t=2\) with nonzero determinant \(r_1s_2-r_2s_1\); it is impossible when \(t\ge3\). Combining this with Step 2 proves the exact resonant test.

**5. Sharp minimum and placement constructions.** If \(H_S\) is a forest, it has at most \(p+q-1\) edges, so \(|S|\ge pq-(p+q-1)=(p-1)(q-1)\). Off resonance, select the block \(S=\{0,\ldots,p-2\}\times\{0,\ldots,q-2\}\). Its complement is the bipartite double-star consisting of all edges incident to the last row or last column; this is a spanning tree, proving equality. Moreover, a placement attaining the lower bound has an unselected forest with exactly \(p+q-1\) edges and hence a spanning tree. The standard matrix-tree calculation for \(K_{p,q}\) gives \(p^{q-1}q^{p-1}\) such trees and therefore this many optimal sets.

At resonance, the merged eigenspace has dimension \(p+q-2\), so also \(|S|\ge p+q-2\). If \(p,q\ge3\), the interaction bound is at least as large, because \((p-1)(q-1)\ge p+q-2\). Construct an unselected tree \(H_S\) by joining the last row to **all** columns, and joining each preceding row to exactly one column, choosing column \(0\) for the first preceding row, column \(1\) for the second, and column \(0\) for any others. Its \(p+q-1\) edges form a spanning tree. The selected graph \(F_S\) has one connected component on the first \(p-1\) rows and **all** \(q\) columns: each of the first two rows meets at least one common column because \(q\ge3\), and their distinct excluded columns ensure no column is isolated; all remaining preceding rows join this component. The final row is isolated. Thus the component-count pairs are \((p-1,q)\) and \((1,0)\), of determinant \(-q\ne0\). The resonant criterion proves optimality.

If \(p=2\), resonance requires at least \(p+q-2=q\) selected cells. Selecting the entire first row gives an unselected star (a forest), and component pairs \((1,q)\), \((1,0)\), with determinant \(-q\ne0\). The symmetric argument applies when \(q=2\). This completes all cases, including \(p=q=2\).

## Verification
The standalone `verify_rook.py` uses only Python's standard library and tests exact Laplacian eigen-equations, exact-rank restrictions, and the two graph criteria. It exhaustively checks **every** selection on boards \((p,q)=(2,2),(2,3),(2,4),(3,3),(3,4)\) both on and off resonance; it also checks explicit constructions and deterministic additional selections on larger boards. The test run completed 11,378 assertions. Integer matrices are reduced modulo the prime \(2^{61}-1\); for the tested matrix dimensions the determinant Hadamard bound is below that prime, so nonzero minors cannot vanish solely on reduction. No finite test is used as a proof for unbounded \(p,q\).

## Relationship to prior work
Notarstefano and Parlangeli (2012, arXiv:1203.0129) establish PBH-based observability/controllability criteria for Cartesian **products of paths**. Yuan and collaborators (2013, arXiv:1310.5806) emphasize maximum eigenspace multiplicity as a general driver-count baseline; such a bound alone does not determine **which** terminal vertex sets are controllable. Monshizadeh, Zhang, and Camlibel (2014, arXiv:1403.4868) study a zero-forcing framework for strong structural controllability, a different quantifier over state matrices. Anđelić, Brunetti, and Stanić (2020, DOI 10.1007/s00373-020-02212-6) treat graph products with a **single binary input vector** and give a spectral-product criterion; their single-input conclusions do not establish this many-independent-terminal-input forest/component classification. Dai (2022, DOI 10.1049/cth2.12385) develops minimum leader-set tools and solves particular bipartite self-similar networks; its treated families differ from weighted rectangular rook graphs.

The separate ingredient that row-/column-zero-sum arrays correspond to circulations is standard linear algebra on bipartite incidence matrices, not independently claimed as new. The contribution assessed here is the full if-and-only-if classification **across all selected vertex sets and both resonance regimes**, its component-imbalance restriction, its constructive sharpness, and its exact optimal-placement enumeration away from resonance. Known generic maximum-multiplicity bounds are explicitly not claimed as new. Searches did not locate a paper stating the combined classification, but a differently presented or unindexed equivalent remains possible.

## Limitations
The theorem treats only two-factor products of **complete** graphs with two direction-constant positive weights. It does not extend as stated to arbitrary row-specific/edge-specific weights, higher Cartesian dimension, time-varying inputs, a common scalar control on all selected vertices, actuator failures, control energy, or robust controllability under coefficient perturbations. The resonance locus is an exact equality, not a numerical tolerance rule. Results are mathematical self-reviewed; no independent audit or experimental network validation has been performed.

## References
1. G. Notarstefano and G. Parlangeli, *Controllability and observability of grid graphs via reduction and symmetries*, arXiv:1203.0129v1, first public 2012-03-01. https://arxiv.org/html/1203.0129v1
2. Z. Yuan, C. Zhao, Z. Di, W.-X. Wang, and Y.-C. Lai, *Exact Controllability of Complex Networks*, arXiv:1310.5806v1, first public 2013-10-22. https://arxiv.org/html/1310.5806v1
3. N. Monshizadeh, S. Zhang, and M. K. Camlibel, *Zero forcing sets and controllability of dynamical systems defined on graphs*, arXiv:1403.4868v1, first public 2014-03-19. https://arxiv.org/abs/1403.4868
4. M. Anđelić, M. Brunetti, and Z. Stanić, *Laplacian controllability for graphs obtained by some standard products*, Graphs and Combinatorics 36 (2020), 1593–1602. https://doi.org/10.1007/s00373-020-02212-6 ; accessible manuscript: https://www.iris.unina.it/retrieve/e268a731-dc2d-4c8f-e053-1705fe0a812c/gc2.pdf
5. L. Dai, *Minimum leader selection for controllability of undirected graphs with leader–follower framework*, IET Control Theory & Applications 17 (2023), 505–515, initially public 2022-10-29. https://doi.org/10.1049/cth2.12385
