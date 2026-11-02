# Translation representations and a rational quotient transition for affine-plane Rips complexes

## Finding

For every prime power \(q\ge3\), let \(G_q\) be the point--line incidence graph of \(\mathrm{AG}(2,q)\), with unit-edge shortest-path metric, and put \(K_q=\operatorname{VR}_{\le2}(G_q)\). The additive group \(T=(\mathbb F_q^2,+)\) acts on this simplicial complex by translations. Let \(\mathrm{Aug}_T\) denote the augmentation representation \(\ker(\mathbb Q[T]\to\mathbb Q)\).

There are *integral*, natural \(T\)-equivariant isomorphisms
\[
H_2(K_q;\mathbb Z)\cong H_1(G_q;\mathbb Z),\qquad
H_q(K_q;\mathbb Z)\cong
\bigotimes_{d\in\mathbb P^1(\mathbb F_q)}\widetilde H_0(D_d;\mathbb Z),
\]
where \(D_d\) is the discrete \(q\)-point set of affine lines in direction \(d\). In particular, these are free integral lattices and the action on the top homology is a tensor of permutation-augmentation lattices.

Set
\[
\tau_q=(-1)^q(q-1),\qquad
 a_q=\frac{(q-1)^{q+1}-\tau_q}{q^2},\qquad
 b_q=\frac{(q-1)^{q+1}+(q^2-1)\tau_q}{q^2}.
\]
Then \(a_q,b_q\) are nonnegative integers, and the **complete rational translation modules** are
\[
H_2(K_q;\mathbb Q)\cong(q-1)\mathrm{Aug}_T,
\qquad
H_q(K_q;\mathbb Q)\cong b_q\mathbf1\oplus a_q\mathrm{Aug}_T.
\]
All other positive-degree reduced rational homology groups vanish. Since rational homology of a quotient by a finite group equals its invariant homology, the quotient \(K_q/T\) has no positive rational homology except \(H_q(K_q/T;\mathbb Q)\cong\mathbb Q^{b_q}\). The exceptional order-three case satisfies
\[
H_2(K_3;\mathbb Q)\cong H_3(K_3;\mathbb Q)
\cong 2\mathrm{Aug}_{\mathbb F_3^2},\qquad
\widetilde H_*(K_3/T;\mathbb Q)=0,
\]
whereas \(b_4=18\) and \(b_5=160\). For every prime power \(q\ge4\), \(b_q>0\). In the quotient filtration, its \(b_q\) degree-\(q\) classes are born at threshold \(2\) and die at threshold \(3\); for \(q=3\) there is no positive-dimensional rational bar.

## Assumptions and scope

The result concerns *Desarguesian* affine planes of prime-power order, not arbitrary non-Desarguesian affine planes. Points are \(\mathbb F_q^2\); lines are the sets \(y=mx+b\), for \(m,b\in\mathbb F_q\), and \(x=b\) for vertical lines. Translation by \((u,v)\) acts on points by addition and on nonvertical line parameters by \((m,b)\mapsto(m,b+v-mu)\), on vertical lines by \((\infty,b)\mapsto(\infty,b+u)\). Thus no translation changes the parallel direction. Graph distances are measured between vertices of the bipartite incidence graph, and the inclusive scale-two Rips complex includes each set of vertices with all pairwise distances at most \(2\). Ordinary, unreduced homology is used in positive degrees; in degree zero the complexes are connected.

The previously published nonequivariant classification
\(K_q\simeq\bigvee^{(q-1)^2(q+1)}S^2\vee\bigvee^{(q-1)^{q+1}}S^q\)
is treated as background, not as a new finding. The present contribution is the integral translation action, its complete rational module structure, and its quotient transition.

## Proof

**The equivariant Mayer--Vietoris decomposition.** Let \(P\) and \(L\) be the point and line sets. Let \(P_\ell\) be the points on line \(\ell\) and \(L_p\) the lines through point \(p\). At graph distance \(2\), all distinct points are adjacent, and two distinct lines are adjacent if and only if they have different parallel directions. Point--line pairs are adjacent exactly when incident. Since two distinct points have only one common line, no mixed clique contains two points and two lines. Put
\[
U=\Delta(P)\cup\bigcup_{\ell\in L}\bigl(\{\ell\}*\Delta(P_\ell)\bigr),\qquad
V=B\cup\bigcup_{p\in P}\bigl(\{p\}*\Delta(L_p)\bigr),
\]
where \(B\) is the clique complex on the line vertices, and \(*\) means simplicial join. The clique description gives \(K_q=U\cup V\), while \(U\cap V\) is *exactly* the original incidence graph \(G_q\). Each cone added to \(\Delta(P)\) has its own line apex, so \(U\) is contractible; similarly, each distinct point apex can be collapsed from \(V\) to obtain \(B\). The inclusions and their homology maps are \(T\)-equivariant. Thus the integral Mayer--Vietoris sequence is an exact sequence of \(\mathbb Z[T]\)-modules.

**The two homology degrees.** The line complex is the join
\[
B=\bigast_{d\in\mathbb P^1(\mathbb F_q)}D_d,
\]
where every \(D_d\) is a discrete \(q\)-point space. Its only positive reduced homology is the free group in degree \(q\), canonically the tensor product of the reduced zero-dimensional homologies of its \(q+1\) factors. Translations fix each direction, so there is no factor-permutation Koszul sign. For \(q\ge3\), \(H_1(B)=H_2(B)=0\), except that \(H_2(B)=0\) also follows directly from \(q\ge3\). The graph \(G_q\) has homology only in degrees \(0\) and \(1\). The positive-degree segments of the integral Mayer--Vietoris sequence therefore give natural \(T\)-module isomorphisms \(H_2(K_q;\mathbb Z)\cong H_1(G_q;\mathbb Z)\) and \(H_q(K_q;\mathbb Z)\cong H_q(B;\mathbb Z)\). For \(q=3\) these are distinct degrees \(2\) and \(3\). The same sequence proves vanishing in all other positive degrees.

**The cycle-space character.** The incidence graph has \(q^2\) points, \(q(q+1)\) lines and \(q^2(q+1)\) edges, hence
\[
\dim H_1(G_q;\mathbb Q)=q^2(q+1)-q^2-q(q+1)+1
=(q-1)^2(q+1).
\]
Orient each graph edge from point to line. A nonidentity translation fixes no point or incidence edge, but fixes exactly the \(q\) line vertices parallel to its displacement vector. Consequently its traces on the graph cellular chains are \(\operatorname{tr}(C_1)=0\) and \(\operatorname{tr}(C_0)=q\). The exact chain relation \([H_1]-[H_0]=[C_1]-[C_0]\) and \(H_0\cong\mathbf1\) give
\[
\operatorname{tr}\bigl(t\mid H_2(K_q;\mathbb Q)\bigr)=1-q
\quad\text{for every }t\ne0.
\]
At identity its trace is \((q-1)^2(q+1)=(q-1)(q^2-1)\). These are exactly the character values of \((q-1)\mathrm{Aug}_T\), proving the first rational-module formula by semisimplicity in characteristic zero.

**The top-homology character.** For a permutation of a finite set \(D\), its trace on \(\widetilde H_0(D;\mathbb Q)\) equals the number of fixed elements minus \(1\). A nonzero displacement vector lies in exactly one of the \(q+1\) one-dimensional \(\mathbb F_q\)-directions. It fixes all \(q\) affine lines in that direction and no line in any other direction. Thus the \(q+1\) augmentation factors have traces \(q-1,-1,\ldots,-1\), and the tensor-product trace is \(\tau_q=(-1)^q(q-1)\). At identity it is \(d_q=(q-1)^{q+1}\). For each nontrivial complex character \(\chi\) of the abelian group \(T\), its multiplicity is
\[
\frac1{q^2}\left(d_q+\tau_q\sum_{t\ne0}\overline{\chi(t)}\right)
=\frac{d_q-\tau_q}{q^2}=a_q,
\]
whereas the trivial-character multiplicity is \(b_q=(d_q+(q^2-1)\tau_q)/q^2\). This proves integrality, nonnegativity, and the asserted rational decomposition, including over \(\mathbb Q\) because the character of \(\mathrm{Aug}_T\) is rational and \(\mathbb Q[T]\) is semisimple. Substituting \(q=3,4,5\) gives \((a_q,b_q)=(2,0),(15,18),(164,160)\). The positive value of \(b_q\) for all \(q\ge4\) follows from the displayed formula, using \((q-1)^q>q^2-1\) for odd \(q\ge5\); the even case has \(\tau_q>0\).

**Passage to translation quotients.** For a finite group acting simplicially on a finite complex, rational averaging (or transfer) identifies \(H_*(K_q/T;\mathbb Q)\) with the invariant part of \(H_*(K_q;\mathbb Q)\), even when simplex stabilizers are nontrivial. Indeed, barycentric subdivision makes the action admissible, and invariants of rational simplicial chains calculate the quotient chains. The preceding character decomposition gives zero invariants in degree \(2\) and exactly \(b_q\) in degree \(q\). The same argument at scale \(1\) uses \(H_1(G_q;\mathbb Q)^T=0\). At threshold \(3\), every point vertex is adjacent in the distance-three graph to every vertex (a nonincident point--line pair has distance \(3\)), so the Rips complex is a cone; larger scales remain contractible. This proves the rational quotient barcode claim.

## Verification

The included standard-library Python checker builds incidence graphs over \(\mathbb F_3\), \(\mathbb F_4\) and \(\mathbb F_5\), with \(\mathbb F_4\) represented by the irreducible polynomial \(t^2+t+1\). It produces integral fundamental-cycle bases, transports every cycle under **every** translation, reconstructs the transported cycles exactly from their chord coefficients, checks the resulting integer traces against the character formula, and separately constructs each parallel-class augmentation action. It verifies the tensor-product traces and invariant multiplicities for all \(9\), \(16\) and \(25\) group elements, respectively. For \(q=3\), it additionally enumerates the entire scale-two complex (face vector \((21,126,282,255,135,84,36,9,1)\)) and checks exact mod-\(101\) boundary ranks, obtaining Betti vector \((1,0,16,16,0,0,0,0,0)\). The terminal marker is `AFFINE_TRANSLATION_INTEGRAL_CYCLES_AND_ALL_ACTIONS_OK`.

These are reproducibility and small-field regression tests. The universal statement for arbitrary prime powers is proved by the preceding exact Mayer--Vietoris and representation calculations, not inferred from the finite tests.

## Relationship to prior work

Adams and Coskunuzer (first public version 2021-03-11) identify graph-power filtrations with the Rips filtrations of graph shortest-path metrics and study geometric bounds for persistence; they do not determine affine-plane symmetry modules. Feng and Nukala (first public version 2023-02-28) give homotopy types of scale-two Rips complexes for subset layers in Hamming metrics, not affine incidence graphs or their translation representations. A published *Affine-plane incidence Rips complexes have two sphere dimensions* result proves the nonequivariant sphere-wedge decomposition of \(K_q\) for arbitrary finite affine planes. Its inspected full result and proof give the structural subcomplexes used here but do not state or calculate either integral symmetry action, its regular/augmentation decomposition, or rational translation-quotient Betti numbers. That nonequivariant theorem alone cannot distinguish different actions on the same wedge of spheres. Galetto, Montaño and Wellner (2026) develop equivariant Rips homology for hypercubes under their hyperoctahedral groups, not for affine incidence graphs under translations. A published projective-plane incidence-graph Rips theorem treats a different geometry in which all pairs of lines intersect, and so has no affine parallel-class tensor factor.

## Limitations

The symmetry action here is the *translation subgroup*, not the full affine collineation group. The stronger integral statement concerns actual homology lattices, not an asserted integral splitting of rational augmentation representations, and does not determine torsion in the homology of the quotient. Rational acyclicity at order three does not imply contractibility of the quotient. The source comparison cannot rule out every unindexed equivalent result. The verifier checks three finite fields, while correctness for all prime powers rests on the mathematical proof.

## References

- H. Adams and B. Coskunuzer, *Geometric Approaches on Persistent Homology*, arXiv:2103.06408 (v1 2021-03-11), https://arxiv.org/abs/2103.06408.
- Z. Feng and N. C. P. Nukala, *On Vietoris-Rips complexes of Finite Metric Spaces with Scale 2*, arXiv:2302.14664 (v1 2023-02-28), https://arxiv.org/abs/2302.14664.
- *Affine-plane incidence Rips complexes have two sphere dimensions*, published mathematical result, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-affine-plane-incidence-rips-complexes-have-two-sphere-dimensions--3087baeea0a4 (full RESULT.md inspected).
- F. Galetto, J. Montaño and Z. Wellner, *Homology of Vietoris-Rips complexes of hypercube graphs via group actions*, arXiv:2606.20784 (v1 2026-06-18), https://arxiv.org/abs/2606.20784.
- *Scale-two Vietoris–Rips complexes of finite projective-plane incidence graphs*, published mathematical result, https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-scale-two-vietoris-rips-complexes-of-finite-projective-plane-inc--c3740b96b3c3 (full RESULT.md inspected).
