# Homotopy classification of bidirected double-star multipath complexes

## Finding
For integers \(a,b\geq1\), take the double-star tree with adjacent centres \(u,v\), with \(a\) pendant neighbours at \(u\) and \(b\) pendant neighbours at \(v\). Replace each tree edge by both possible directed arcs, obtaining \(D_{a,b}\). Let \(X_{a,b}=X(D_{a,b})\) be the multipath complex: its vertices are the arcs and its faces are precisely the arc sets whose directed subgraph is a disjoint union of directed, vertex-simple paths (isolated vertices allowed).

Put \(m=\min(a,b)\), \(M=\max(a,b)\), and \(r_t=t^2-3t+1\) for \(t\geq3\). Then the full integral homotopy type is
\[
|X_{a,b}|\simeq
\begin{cases}
S^1,&m=1,\ M\leq2,\\
\bigvee^{M^2-3M+1} S^2,&m=1,\ M\geq3,\\
\bigvee^{M^2-M-1} S^2,&m=2,\\
\bigvee^{2(a-1)(b-1)}S^2\ \vee\
\bigvee^{(a^2-3a+1)(b^2-3b+1)}S^3,&m\geq3.
\end{cases}
\]
All asserted wedges have positive multiplicity where they appear. In particular, these complexes have torsion-free integral homology. Their reduced homology occurs in two adjacent dimensions exactly when \(a,b\geq3\). The smallest such case is \(|X_{3,3}|\simeq\bigvee^8S^2\vee S^3\).

## Assumptions and scope
The graph is finite and has no loops or multiple arcs with the same ordered endpoints. Each undirected edge of the underlying double star contributes two opposite arcs. A multipath cannot contain an oriented cycle, including a directed two-cycle; every vertex has at most one incoming and one outgoing chosen arc. Joins and wedges are taken in the usual (unbased or based as appropriate) topological sense, and the displayed homotopy equivalences are for geometric realizations. All integer parameters \(a,b\) are at least one. This statement does not concern arbitrary bidirected trees, arbitrary orientations, or non-multipath path homology.

## Proof
**1. The two pendant-star complexes.** Let \(C_t\) be the multipath complex of the bidirected star with \(t\) leaves. At its centre, a multipath can use at most one incoming arc and one outgoing arc. It can use both precisely when they meet different leaves: choosing opposite arcs along the same leaf-edge would form a directed two-cycle. Thus \(C_t\) is exactly the one-dimensional crown graph \(K_{t,t}\) with the \(t\) diagonal matching edges removed. Its \(2t\) vertices and \(t(t-1)\) edges yield
\[
C_1\simeq S^0,\qquad C_2\simeq S^0,\qquad
C_t\simeq\bigvee^{t^2-3t+1}S^1\quad(t\geq3).
\]
Indeed, \(C_1\) comprises two isolated vertices, \(C_2\) comprises two disjoint edges, and \(C_t\) is connected for \(t\geq3\), with the indicated graph-cycle rank.

**2. Removing the central arrows.** Denote the two opposite arcs joining the centres by \(e_+\) and \(e_-\), and let \(Z\) be the subcomplex comprising faces using neither arrow. Since the remaining arcs lie in two independent bidirected stars, \(Z=C_a*C_b\), the simplicial join. Neither multipath can include both central arrows, since they make a directed two-cycle. Therefore \(X_{a,b}\) is obtained from \(Z\) by adjoining two cones \(e_+*L_+\) and \(e_-*L_-\), where \(L_\pm\) are their respective links inside \(Z\). Each link is the full join of the \(a\) inward-pointing leaf arcs at one centre and the \(b\) outward-pointing leaf arcs at the other (the choices reverse for the opposite central arrow). Hence both links are the graph \(K_{a,b}\), with
\[
L_+\simeq L_-\simeq\bigvee^{(a-1)(b-1)}S^1,
\]
interpreted as a contractible graph when \(m=1\). The two links use disjoint arc vertices and have no shared simplices other than the empty face. The sequential cone attachments are therefore genuine homotopy cofibres of their inclusion maps into \(Z\).

**3. The case \(m=1\).** Both central-arrow links are nonempty contractible graphs. A cone attached along a contractible subcomplex is homotopy neutral. Thus \(X_{a,b}\simeq Z\). If \(M\leq2\), the join is \(S^0*S^0\simeq S^1\). Otherwise it is \(S^0*(\bigvee^{r_M}S^1)\simeq\bigvee^{r_M}S^2\).

**4. The case \(m=2\), \(M\geq3\).** The join \(Z\) is homotopy equivalent to a wedge of \(r_M\) two-spheres, hence simply connected. Every map from the connected graph \(L_\pm\) to \(Z\) is null-homotopic. Attaching the two cones therefore wedges on their suspensions. Each link has first Betti number \(M-1\). Consequently
\[
X_{a,b}\simeq\bigvee^{r_M+2(M-1)}S^2
=\bigvee^{M^2-M-1}S^2.
\]

**5. The exceptional \(a=b=2\) case.** Now \(Z=C_2*C_2\simeq S^1\), so simply connectedness is unavailable. Nevertheless, \(L_+\to Z\) is a homotopy equivalence: it is the join of an inclusion of one representative leaf-arrow from each of the two contractible components of the first \(C_2\) and the analogous inclusion for the other \(C_2\). Each factor map is a homotopy equivalence \(S^0\to C_2\), and joins preserve homotopy equivalences. Hence \(Z\cup_{L_+}\operatorname{Cone}(L_+)\) is contractible. The second link is \(L_-\cong K_{2,2}\simeq S^1\). Attaching its cone to this contractible space yields its unreduced suspension, homotopy equivalent to \(S^2\). Thus the same formula for \(m=2\) holds with \(M=2\), giving precisely one two-sphere.

**6. The case \(m\geq3\).** By the join formula, \(Z\simeq\bigvee^{r_a r_b}S^3\). It is simply connected, so both inclusions of the connected graphs \(L_\pm\) are null-homotopic. The two cone attachments add \((a-1)(b-1)\) two-spheres each, with the base three-spheres unaffected. This proves the last formula. In all cases, the asserted integral homology and torsion-free conclusions follow from the wedge decompositions. \(\square\)

## Verification
The standalone `verify.py` independently enumerates all directed-arc subsets of sizes zero through four and tests the in/out-degree and acyclicity conditions. For every \(1\leq a\leq b\leq6\), it constructs integral simplicial incidence signs and evaluates the boundary ranks over \(\mathbb F_2\), \(\mathbb F_3\), and \(\mathbb F_5\). All 21 parameter pairs agree with the predicted reduced Betti ranks. The program also checks the two central-arrow links, including all compatible pairs of link vertices. Run `python3 verify.py` from the directory containing this document and the program. Successful output concludes with `VERIFY_OK 21 parameter pairs, three fields, and both central-edge links`. Finite-field computations alone cannot establish the homotopy theorem, integral torsion-freeness for unbounded parameters, or universal novelty; those claims depend on the preceding homotopy proof.

## Relationship to prior work
Caputi, Collari, and Smith (2026) define the multipath complex and compute homotopy types of **bidirected paths**, together with homology of **bidirected polygons** and suspension operations. These results motivate the question of what changes when the underlying bidirected tree has two branching centres. The present classification treats a different natural family: double stars with arbitrary positive branching parameters, including the first mixed-dimensional sphere wedges. Caputi, Collari, Di Trani, and Smith (2023/2024) study multipath homotopy types for several classes of digraphs; their directed-tree and orientation examples do not give the double-star classification here. Caputi, Collari, and Ramos (2024) compare multipath and matching constructions for digraphs without directed cycles; the opposite arcs on every edge of \(D_{a,b}\) create directed two-cycles, so that acyclic comparison does not directly specialize to this result. No claim of independent mathematical certification or exhaustive global literature coverage is made.

## Limitations
The classification is confined to bidirected double stars with \(a,b\geq1\). It neither treats trees with three or more branching vertices nor determines equivariant representations of their automorphism groups. The finite computational comparison extends only to \(a,b\leq6\) over the three indicated fields, although the proof is symbolic and integral for every positive \(a,b\). Equivalent results in inaccessible, unpublished, or unindexed literature cannot be excluded. Independent validation has not been performed.

## References
1. L. Caputi, C. Collari, and J. P. Smith, *Multipath complexes of bidirectional polygonal digraphs*, arXiv:2601.05670v1, publicly posted 2026-01-09, https://arxiv.org/abs/2601.05670.
2. L. Caputi, C. Collari, S. Di Trani, and J. P. Smith, *On the homotopy type of multipath complexes*, Mathematika 70 (2024), e12235, preprint arXiv:2208.04656, https://arxiv.org/abs/2208.04656.
3. L. Caputi, C. Collari, and E. Ramos, *The weak categorical quiver minor theorem and its applications: matchings, multipaths, and magnitude cohomology*, preprint (2024), https://arxiv.org/abs/2401.01248.
