# A sharp one-circle-to-sphere-wedge transition for clique-fiber cyclic Rips complexes

## Finding
For integers \(m\ge2\), \(r\ge2\), and \(n\ge3r\), form the Cartesian graph product \(G_{m,n}=K_m\square C_n\). Give its vertices the shortest-path metric, and use the **inclusive** Vietoris--Rips convention: a finite vertex set is a face if every pair has distance at most \(r\). Then
\[
\operatorname{VR}(G_{m,n};r)\simeq
\begin{cases}
\displaystyle\bigvee^{mr-1}S^2,&n=3r,\\
S^1,&n>3r.
\end{cases}
\]
In particular, all its integral homology groups are torsion-free, and the transition at \(n=3r\) changes the fundamental group from trivial to infinite cyclic. The family \(m=3\) consists of thin toroidal grids \(C_3\square C_n\). For example, the complexes at \((m,r,n)=(3,2,6)\) and \((3,3,9)\) are wedges of five and eight \(2\)-spheres, respectively.

## Assumptions and scope
Write vertices as \((i,a)\), where \(i\in\mathbb Z/n\mathbb Z\) is a column and \(a\in\{1,\ldots,m\}\) is a row. For any two vertices,
\[
d((i,a),(j,b))=d_{C_n}(i,j)+\mathbf1_{a\ne b}.
\]
Indices are interpreted cyclically, and \(n\ge3r\) ensures each cyclic pair of columns at distance exactly \(r\) has a unique clockwise short orientation. No assertion is made when \(r=1\) or \(n<3r\).

## Proof
**1. The lower-scale core.** Let \(B\) be the subcomplex of faces whose columns are pairwise at cyclic distance at most \(r-1\). Because every pair in any selected columns at distance at most \(r-1\) is adjacent at scale \(r\), \(B\) is obtained from \(\operatorname{VR}(C_n;r-1)\) by replacing each column vertex with a full \((m-1)\)-simplex. Removing every row other than a chosen row by dominated-vertex collapses identifies \(B\simeq\operatorname{VR}(C_n;r-1)\). The standard finite-cycle Rips classification [2] gives \(B\simeq S^1\), since \(n\ge3r>3(r-1)\). The chosen-row cyclic edge loop generates \(\pi_1(B)\): its inclusion is degree one under the standard circle model (equivalently map each short column window to its corresponding short arc of the circle).

**2. The distance-\(r\) simplices.** For each clockwise pair of columns \((i,i+r)\) and row \(a\), denote the long edge by \(e_{i,a}=\{(i,a),(i+r,a)\}\). Let \(I_i\) be the set of **all** vertices in the intervening columns \(i+1,\ldots,i+r-1\), and put \(F_{i,a}=\Delta(e_{i,a}\cup I_i)\), a full simplex. It is a Rips simplex because the endpoints have the same row and all other column distances are at most \(r-1\).

We verify that these are all noncore faces except the triangles described below. Any face outside \(B\) contains a pair of columns at cyclic distance exactly \(r\); their two vertices must have the same row, say \(a\). Translate the columns so that the pair is \((0,r)\). A third column \(j\) at distance at most \(r\) from both endpoints lies between \(0\) and \(r\) clockwise, unless \(n=3r\) and \(j=2r\). Indeed, an outside column would have to obey simultaneously \(j\ge n-r\) and \(j\le2r\); this is possible precisely when \(n=3r\), and then only at \(j=2r\). In the ordinary intervening columns the other vertices may have any row and belong to \(I_i\). At the exceptional column \(2r\), the row must equal \(a\); furthermore no intervening vertex is adjacent to that exceptional vertex, because every such cyclic distance is greater than \(r\). Thus the only faces outside the union of \(B\) and the \(F_{i,a}\) are the **full triangles**
\[
T_{j,a}=\{(j,a),(j+r,a),(j+2r,a)\},\qquad0\le j<r,\quad1\le a\le m,
\]
which occur if and only if \(n=3r\). No larger simplex contains such a triangle. There are exactly \(mr\) of them.

**3. Collapse away the ordinary distance-\(r\) edges.** Put \(U=B\cup\bigcup_{i,a}F_{i,a}\). Each \(F_{i,a}\) meets \(B\) in \(\partial\Delta(e_{i,a})*\Delta(I_i)\), and two distinct \(F_{i,a}\) meet only inside \(B\): a face with two distinct distance-\(r\) column pairs would necessarily be one of the exceptional triangles, not a face of an \(F_{i,a}\). Pick any vertex \(p_i\in I_i\), possible because \(r\ge2\). For each \(S\subseteq I_i\setminus\{p_i\}\), pair \(e_{i,a}\cup S\) with \(e_{i,a}\cup S\cup\{p_i\}\), processing the pairs in descending order of \(|S|\). Every pair is an elementary free-face collapse: all larger cofaces containing its lower face have previously been removed, except the displayed upper face. Since these are precisely the non-\(B\) faces of \(F_{i,a}\), this gives \(U\searrow B\). Hence \(U\simeq S^1\).

**4. Attach the exceptional triangles.** If \(n>3r\), the full Rips complex equals \(U\), finishing this case. If \(n=3r\), attach the \(mr\) maximal triangles \(T_{j,a}\) along their boundary loops in \(U\). Within \(F_{i,a}\), each long edge \(e_{i,a}\) is homotopic relative endpoints to the clockwise path of \(r\) ordinary edges in row \(a\): both paths bound a triangulated disk in that full simplex. Consequently the three successive long edges around each \(T_{j,a}\) form a loop homologous and homotopic to exactly one clockwise full turn along row \(a\). By Step 1, each attaching loop represents a generator \(\pm1\) of \(\pi_1(U)\cong\mathbb Z\).

The first attached disk kills that generator and yields a contractible complex up to homotopy; attaching any remaining disk along a nullhomotopic loop adds a wedge summand \(S^2\). With \(mr\) such disks this gives precisely \(\bigvee^{mr-1}S^2\). This homotopy construction is integral; it does not infer infinite claims from finite field ranks.

## Verification
The standalone standard-library program `verify.py` independently builds every clique from the graph-metric adjacency relation. For 16 explicit triples \((m,r,n)\), it checks that the proposed core, interval simplices, and exceptional triangles give a complete face covering; all purported carrier simplices satisfy the distance bound; the classification of repeated distance-\(r\) pairs; and the predicted reduced homology by exact binary boundary-matrix reduction. Run `python3 verify.py` to reproduce `VERIFY_OK 16 exhaustive clique-cover and homology checks`. These finite checks are corroborative; Steps 1--4 establish the statement for all parameters.

## Relationship to prior work
Adams, Adetowubo, Barriga-Acosta, Feng and Sterling [1] study shortest-path Rips complexes of **square** toroidal grids and prove, among other results, a wedge of \(6r^2-1\) two-spheres for the square grid at side length \(3r\) and scale \(r\). The present graphs have a complete-graph factor \(K_m\), which is not generally a square cycle of length \(3r\); their square-grid classification does not imply either branch of this theorem. Adamaszek and Adams [2] classify Rips complexes of a single finite circle and supply the one-dimensional input in Step 1. The metric-gluing work [3] and infinite-lattice work [4] concern different geometric constructions. Searches for equivalences, cyclic blow-up presentations and larger-parameter covering theorems found no prior statement implying this exact family; this is a bounded literature comparison, not a claim to exhaustive novelty.

## Limitations
The classification excludes \(r=1\) and \(n<3r\), and does not address equivariant homotopy or persistence across the entire filtration. It applies to the shortest-path (graph \(\ell^1\)-type) metric, not Euclidean, strong-product or maximum-product metrics. The computer checks sample finitely many instances and do not constitute a general proof. Equivalent unindexed or unpublished work could exist. No independent validation has been performed.

## References
[1] H. Adams, A. Y. Adetowubo, H. Barriga-Acosta, Z. Feng, J. Sterling, *Vietoris--Rips complexes of torus grids*, arXiv:2502.07134, originally submitted 2025-02-10, https://arxiv.org/html/2502.07134v2 (Introduction, Sections 5--7).

[2] M. Adamaszek and H. Adams, *The Vietoris--Rips complexes of a circle*, arXiv:1503.03669, https://arxiv.org/html/1503.03669v2 (finite cyclic-graph circle regime).

[3] M. Adamaszek et al., *On Homotopy Types of Vietoris--Rips Complexes of Metric Gluings*, arXiv:1712.06224, https://arxiv.org/html/1712.06224v5 (metric-gluing results).

[4] A. Gupta, S. Sarkar, S. Shukla, *On the Vietoris--Rips Complexes of Integer Lattices*, arXiv:2511.04238, https://arxiv.org/html/2511.04238v1 (infinite lattices).
