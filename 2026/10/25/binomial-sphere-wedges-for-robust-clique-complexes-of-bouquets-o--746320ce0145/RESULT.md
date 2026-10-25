# Binomial sphere wedges for robust clique complexes of bouquets of four-cycles

## Finding
For \(m\ge1\), form the bouquet graph \(B_m\) from \(m\) cycles of length four by identifying exactly one vertex of each cycle, and otherwise identifying no vertices. For all integers \(k\ge4\), its robust clique complex satisfies the **integral homotopy equivalence**
\[
\mathsf{Cliq}_k(B_m)\simeq\bigvee^{\binom m{k-1}}S^{2k-3}.
\]
A zero sphere count means a contractible complex. In particular, for \(k=4\) the number of five-sphere summands is \(\binom m3\); thus the values at \(m=3,4,5\) are \(1,4,10\).

## Assumptions and scope
All graphs and simplicial complexes are finite; homotopy equivalences are of geometric realizations, with integral coefficients. For a vertex subset \(S\), \(\alpha(G[S])\) means the maximum number of pairwise nonadjacent vertices in its induced subgraph. Define
\[\mathsf{Cliq}_k(G)=\{S\subseteq V(G):\alpha(G[S])\le k-1\}.\]
Write the bouquet vertices as a center \(c\) and triples \(a_i,b_i,d_i\) indexed by \(1\le i\le m\). The four edges of the \(i\)-th square are \(ca_i,cb_i,a_id_i,b_id_i\). Distinct squares have no edges between their noncentral vertices. There are no further assumptions on \(m\) and \(k\), except \(m\ge1\) and \(k\ge4\).

## Proof
**Step 1 (a cofiber).** Let \(K=\mathsf{Cliq}_k(B_m)\), \(X=K\setminus\{c\}\), and \(L=\operatorname{lk}_K(c)\). Then \(K=X\cup(c*L)\), so \(|K|\simeq |X|/|L|\) because a simplicial subcomplex inclusion is a cofibration. The graph obtained by deleting \(c\) is the disjoint union of the paths \(a_i-d_i-b_i\). For every face \(S\in X\), the maximum independent-set size of \(S\cup\{c\}\) is
\[\alpha(B_m[S\cup\{c\}])=\max\{\alpha(B_m[S]),\,1+|\{i:d_i\in S\}|\}.\]
Indeed, an independent set either avoids \(c\) or contains \(c\); in the latter case it can contain precisely the available \(d_i\) and no \(a_i,b_i\). Hence
\[L=\{S\in X:|\{i:d_i\in S\}|\le k-2\}.\]
If \(m<k-1\), this is all of \(X\), so \(K=c*X\) is a cone; the stated binomial count vanishes.

**Step 2 (all non-link faces).** Assume \(m\ge k-1\). Every face of \(X\setminus L\) contains at least \(k-1\) of the \(d_i\). Since distinct distal vertices \(d_i\) are independent and faces of \(X\) have independence number at most \(k-1\), it contains exactly \(k-1\) of them. Call their index set \(I\). No vertex from a branch outside \(I\) can belong to this face, since it would add one independent vertex. Within a represented branch \(i\in I\), at most one of \(a_i,b_i\) can be selected, since these two leaves are nonadjacent. Conversely any such choice gives a face with independence number exactly \(k-1\): each represented branch contains its middle vertex and at most one leaf, so each contributes one to the independent-set size.

**Step 3 (closed balls and their boundaries).** For each \((k-1)\)-element subset \(I\subseteq[m]\), let \(D_I=\{d_i:i\in I\}\) and let \(Z_I=\operatorname{st}_X(D_I)\), the closed simplicial star consisting of faces extendable by \(D_I\) in \(X\). The characterization in Step 2 gives the exact simplicial join
\[
Z_I=\Delta(D_I)*\mathop{\star}_{i\in I}\{\varnothing,\{a_i\},\{b_i\}\}
\cong\Delta^{k-2}*(S^0)^{*(k-1)}.
\]
The iterated join of \(k-1\) zero-spheres is a sphere of dimension \(k-2\). Consequently \(|Z_I|\) is a closed ball of dimension \((k-2)+(k-2)+1=2k-3\). Moreover, exactly those faces missing at least one vertex of \(D_I\) lie in \(L\); therefore
\[
Z_I\cap L=\partial\Delta(D_I)*(S^0)^{*(k-1)}=\partial Z_I\cong S^{2k-4}.
\]
Distinct stars meet only inside \(L\), because a face lying in the non-link portion of both would contain at least \(k\) distinct distal vertices and would be forbidden. Finally \(X=L\cup\bigcup_{|I|=k-1} Z_I\), since Step 2 exhausts \(X\setminus L\).

**Step 4 (quotient and integral homotopy type).** Collapsing \(|L|\) to the basepoint, all \(|Z_I|\) become mutually disjoint away from that point and each becomes \(|Z_I|/|\partial Z_I|\cong S^{2k-3}\). Their quotient therefore is the one-point union of precisely \(\binom m{k-1}\) such spheres. Since \(|K|\simeq |X|/|L|\), the theorem follows. This argument is a homotopy-level proof and imposes no field or characteristic restrictions.

## Verification
The standalone standard-library program `verify.py` independently reconstructs each bouquet graph, calculates exact independence numbers for every subset by vertex-deletion dynamic programming, and checks the vertex link, star boundaries, non-link coverage, and disjointness of the open star interiors. It checks all \(1\le m\le5\) and \(k\in\{4,5\}\). For \(k=4\), it also calculates all reduced mod-two Betti numbers from the complete simplicial boundary matrices and finds only the predicted \((2k-3)\)-dimensional rank. The recorded reproducible output is in `verification_output.txt`. These finite calculations are corroboration, not a substitute for the universal proof above.

## Relationship to prior work
The definition of a robust clique complex is the same as that of the bounded-independence complex of Kim and Lew. Their 2019 preprint / 2022 paper addresses collapsibility and Leray bounds, not the asserted homotopy classification of bouquets. Filakovský's February 11, 2026 paper proves sphere-wedge results for square-sequence graphs, where each new square is attached along an existing edge or a path of two edges, and conjectures more general high-threshold behavior within that class. The graph \(B_m\) for \(m\ge2\) is **outside that square-sequence hypothesis**: its square blocks meet only at a single vertex. Thus the new theorem extends the natural scope of the high-threshold question but does not prove any unaddressed case of the square-sequence conjecture. An indexed 2026 result treats the three-robust clique complex of all connected bipartite graphs; its threshold \(k=3\) does not imply the present \(k\ge4\) statement. Prior indexed comparisons were made for alternative terminology, explicit parameter families, and dominating general statements.

## Limitations
The theorem applies only to the cactus family with all four-cycle blocks meeting at one common vertex; it does not claim the same multiplicity for arbitrary cactus graphs, other gluing patterns, or all graphs containing squares. The empty-wedge convention is essential when \(m<k-1\). Bibliographic indexing may be incomplete, so the absence of a known dominating homotopy statement is not proof of global priority. Independent review has not occurred.

## References
1. M. Filakovský, *The Topology of \(k\)-Robust Clique Complexes in Grid-like Graphs*, arXiv:2602.11365, first public 2026-02-11, https://arxiv.org/abs/2602.11365. Relevant: Theorem 1.2, Corollary 1.3, Conjecture 1.5, Definition 2.3.
2. M. Kim and A. Lew, *Complexes of graphs with bounded independence number*, arXiv:1912.12605 (2019); Israel J. Math. 249 (2022), 83–120, https://arxiv.org/abs/1912.12605. Relevant: definition, Theorems 1.5–1.9 and Section 7.
