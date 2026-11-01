# An exact multiplicity formula for the sphere rank of partition-graph clique complexes

## Finding

Let \(G_n\) have as vertices the integer partitions of \(n\geq1\), with two partitions adjacent precisely when one is obtained from the other by transferring a single Ferrers cell from a removable corner to a distinct addable corner, followed by reordering. Let \(K_n=\operatorname{Cl}(G_n)\) be its flag (clique) complex. For a partition \(\lambda\), write the distinct part sizes in increasing order as \(d_1<\cdots<d_s\), with respective positive multiplicities \(m_1,\ldots,m_s\). Define

\[
 r(\lambda)=\begin{cases}
 0,&s\leq2,\\
 \binom{s-2}{2}+\#\{i:2\leq i\leq s-1,\ m_i\geq2\},&s\geq3.
 \end{cases}
\]

Then, for **every** positive integer \(n\),

\[
 \chi(K_n)=1+\sum_{\lambda\vdash n}r(\lambda),\qquad
 \widetilde H_2(K_n;\mathbb Z)\cong\mathbb Z^{\sum_{\lambda\vdash n}r(\lambda)},\qquad
 |K_n|\simeq\bigvee^{\sum_{\lambda\vdash n}r(\lambda)}S^2.
\]

All reduced integral homology in other degrees vanishes. The **new assertion is the all-parameter nonnegative formula for the multiplicity**. The fact that these complexes are wedges of two-spheres and that their multiplicity is \(\chi(K_n)-1\) was previously proved in [1]. In particular, the formula gives \(\sum_{\lambda\vdash26}r(\lambda)=4480\).

## Assumptions and scope

A partition is a finite nonincreasing list of positive integers totaling \(n\). A removable (respectively, addable) corner is a Ferrers cell whose removal (respectively addition) leaves a partition Ferrers diagram; the two corner positions used in a transfer are different. In this theorem \(G_n\) is **exactly** the unit-cell transfer graph from [1,2], not the binary-word graph on partitions. The statement holds for all \(n\geq1\), including the contractible cases \(n\leq7\). The topological sphere-wedge conclusion invokes the established theorem [1]; the explicit Euler-characteristic identity is proved directly below.

## Proof

**1. A strict orientation and a unique minimum for each clique.** For a partition \(\lambda\) write \(h_j=\#\{i:\lambda_i\ge j\}\) for the height of its \(j\)-th Ferrers column, and put \(Q(\lambda)=\sum_{j\ge1}j h_j\). Equivalently, \(Q(\lambda)=\sum_i\lambda_i(\lambda_i+1)/2\). An elementary transfer from a removable corner in column \(a\) to an addable corner in column \(b\) changes the column-height vector by \(-e_a+e_b\) and changes \(Q\) by \(b-a\). Distinct partitions cannot result when \(a=b\); consequently an edge changes \(Q\) strictly. Every clique has pairwise distinct heights and hence a unique vertex at which \(Q\) is minimal. We count all nonempty simplices by their unique minimum.

**2. Increasing transfers at a fixed partition.** Let \(\lambda\) have \(s\) distinct row lengths \(d_1<\cdots<d_s\) with multiplicities \(m_i\). The removable corners are in columns \(d_i\), while the addable corners are in columns \(1,d_j+1\), for \(1\leq j\leq s\). A transfer increases \(Q\) exactly when its recipient column is larger than its source column. Thus its source and target have the form \((d_i,d_j+1)\) with either \(i<j\), or \(i=j\) and \(m_i\geq2\). The off-diagonal transfers are always admissible: they move a cell from a strictly shorter row-length block to a strictly longer one. A same-block transfer is admissible precisely when that block contains at least two rows: it then changes two equal rows into lengths one greater and one smaller. If the block contains a single row, moving its own cell to its own next column does not represent a legitimate distinct-row transfer. A recipient in column \(1\) never increases \(Q\).

Introduce a bipartite graph \(B_\lambda\) whose left vertices are \(R_1,\ldots,R_s\), right vertices are \(A_1,\ldots,A_s\), and whose edges are \(R_iA_j\) for \(i<j\), together with \(R_iA_i\) when \(m_i\geq2\). Edges of \(B_\lambda\) are therefore in canonical bijection with the neighbors of \(\lambda\) having larger height; duplicate partitions cannot arise because a transferred column-height difference uniquely determines both columns.

**3. The upper link is a line-graph clique complex.** Two distinct such increasing transfers yield adjacent neighbor partitions if and only if they share their removed column or share their added column. Indeed, their difference has the form \((-e_a+e_b)-(-e_c+e_d)\). When \(a=c\) or \(b=d\) it is a single unit transfer; the endpoints are partitions, hence this is an edge of \(G_n\). In all other cases it has four distinct nonzero terms, or a coefficient of magnitude two if a source equals the other's target; because all transfers strictly increase height, opposing transfers cannot cancel to another one-unit move. Hence the graph induced by the higher neighbors is exactly the line graph \(L(B_\lambda)\). Denote its flag complex by \(U_\lambda\), the *upper link* of \(\lambda\).

A clique of the line graph of a simple bipartite graph consists of edges sharing a common endpoint. (Three pairwise intersecting edges without a common endpoint would form a triangle in the bipartite graph.) Cover \(U_\lambda\) by simplices indexed by the nonisolated vertices of \(B_\lambda\): the simplex at a vertex consists of all incident edges of \(B_\lambda\). Nonempty intersections of any such simplices are simplices; two distinct members meet in a single vertex of \(U_\lambda\) precisely when the two indexing vertices form an edge of \(B_\lambda\), and there are no triple intersections. By the simplicial nerve lemma, \(U_\lambda\simeq B_\lambda^{\mathrm{core}}\), where the right-hand side deletes isolated vertices from \(B_\lambda\). This remains valid if \(B_\lambda\) consists of a single edge; if it has no edges then \(U_\lambda\) is empty.

**4. Euler contributions of the upper links.** For \(s\geq2\), the off-diagonal edges connect all \(R_i\) for \(1\leq i\leq s-1\) via \(A_s\), and all \(A_j\) for \(2\leq j\leq s\) via \(R_1\). Any diagonal edges attach the remaining possible vertices \(A_1,R_s\) to this connected core, so \(B_\lambda^{\mathrm{core}}\) is connected. With \(t=\#\{i:m_i\geq2\}\) it has

\[
 E=\binom{s}{2}+t,\qquad V=2(s-1)+\mathbf1_{m_1\geq2}+\mathbf1_{m_s\geq2}.
\]

Its cycle rank is consequently

\[
 E-V+1=\binom{s-2}{2}+\sum_{i=2}^{s-1}\mathbf1_{m_i\geq2}=r(\lambda),
\]

using the identity \(\binom{s}{2}-2(s-1)+1=\binom{s-2}{2}\). For \(s=2\), this yields zero. For \(s=1\), the upper link is either empty (\(m_1=1\)) or a point (\(m_1\geq2\)); this exceptional empty case is exactly \(\lambda=(n)\).

**5. Count simplices by their minima.** Given a nonempty simplex \(\sigma\), let \(\lambda\) be its unique lowest-height vertex and let \(\tau=\sigma\setminus\{\lambda\}\). Then \(\tau\) ranges over all faces (including the empty face) of \(U_\lambda\). The contribution of all simplices having minimum \(\lambda\) to the ordinary Euler characteristic is

\[
 \sum_{\tau\in U_\lambda\,\mathrm{including}\,\varnothing}(-1)^{|\tau|}
 =1-\chi(U_\lambda).
\]

For \(s\geq2\), \(\chi(U_\lambda)=1-r(\lambda)\); for \(s=1,m_1\geq2\), it equals one; and for the unique partition \(\lambda=(n)\) it equals zero. Thus the total over all \(\lambda\vdash n\) is exactly \(1+\sum_{\lambda\vdash n}r(\lambda)\). This establishes the Euler characteristic formula without any finite-range assumption or reference to experimental data. The integral homology and homotopy classifications then follow by substituting into the independently established all-\(n\) wedge-of-two-spheres theorem [1]. \(\square\)

## Verification

The standalone `verify.py` implements the partition sum without generating any cliques. It separately generates the full partition transfer graph, counts its complete clique face-vector to obtain Euler characteristic for \(1\leq n\leq15\), and checks equality with the formula. It additionally checks the formula against every one of the 25 published multiplicity values from [1, Table 1] and confirms the exact prediction for \(n=26\). Finite checks do not replace Steps 1–5. Execute `python verify.py` from the extracted package using Python 3 and NetworkX.

## Relationship to prior work

Lyudogovskiy [1] proves the unrestricted sphere-wedge type but leaves its multiplicity as \(\chi(K_n)-1\), and lists only finite initial values. Lyudogovskiy [2] tabulates the first 25 Euler characteristics, gives clique- and nerve-enumeration formulas and explicitly poses exact all-parameter formulas for \(\chi(K_n)\) as an open problem (Problem 6.1). The present multiplicity-local formula is not a restatement of the alternating full-clique count: it depends only on the number and multiplicities of distinct parts of each partition, obtained through the oriented-link and bipartite-cycle-rank argument. The earlier *Local Morphology of the Partition Graph* [4] proves that an entire neighborhood of a partition is a line graph of an admissibility graph, a closely related and stronger **local** statement. It does not compute the Euler characteristic or rising-link cycle-rank sum across all partitions; the oriented global cancellation and the explicit numerical formula are the new steps.

## Limitations

The proof presupposes the graph's precise Ferrers-corner transfer adjacency and the published topological wedge theorem for the homotopy conclusion. No formula for individual clique numbers, asymptotic growth, higher equivariant invariants, or other partition graph models is claimed. A later conceptual synthesis of the same graph [3] was located but its full text was not retrieved; its available description addresses structural/topological mechanisms rather than this all-parameter counting formula. Equivalent or stronger work outside the inspected sources remains possible; independent validation has not been performed.

## References

[1] F. B. Lyudogovskiy, *The homotopy type of the clique complex of the partition graph*, arXiv:2603.14370 (first public 2026-03-15), https://arxiv.org/html/2603.14370v1.

[2] F. B. Lyudogovskiy, *Numerical topology of the clique complex of the partition graph: Euler characteristic, clique counts, and sequence data*, arXiv:2603.26656 (first public 2026-03-27), https://arxiv.org/html/2603.26656v1.

[3] F. B. Lyudogovskiy, *Local Complexity, Overlap Control, and Global Simplicity in Partition Graphs*, arXiv:2606.20773 (2026-06-18), https://arxiv.org/abs/2606.20773.

[4] F. B. Lyudogovskiy, *Local Morphology of the Partition Graph*, arXiv:2603.18696 (first public 2026-03-19), https://arxiv.org/html/2603.18696v1.
