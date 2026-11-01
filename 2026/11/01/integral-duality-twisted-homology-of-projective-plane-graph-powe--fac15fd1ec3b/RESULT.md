# Integral duality-twisted homology of projective-plane graph-power complexes

## Finding
Let \(\Pi\) be any finite projective plane of order \(q\ge2\). Its point--line incidence graph \(G\) has graph-path metric \(d\), and \(K=\operatorname{VR}_{\le2}(V(G),d)\) denotes the simplicial complex of all nonempty vertex sets having pairwise distance at most two. Write \(\Gamma=\operatorname{Aut}(G)\). Bipartite connectedness supplies a character \(\varepsilon:\Gamma\to\{\pm1\}\), equal to \(+1\) when points and lines are separately preserved, and to \(-1\) when they are interchanged.

**Theorem (integral equivariant structure).** There is an integral \(\Gamma\)-module isomorphism
\[
\widetilde H_2(K;\mathbb Z)\cong H_1(G;\mathbb Z)\otimes_{\mathbb Z}\mathbb Z_{\varepsilon},
\qquad\operatorname{rank}\widetilde H_2(K;\mathbb Z)=q^3.
\]
Every other reduced integral homology group of \(K\) is zero. The isomorphism is equivariant for the entire automorphism group, including polarities and correlations interchanging points with lines.

Choose the orientation of every incidence edge from its point to its line. For a class-preserving automorphism \(g\), let \(f_E(g)\) be the number of point--line flags fixed endpointwise and let \(f_V(g)\) be the number of fixed graph vertices. For a class-exchanging automorphism let \(a_E(g)\) be the number of flags whose two endpoints are interchanged by \(g\). Then the entire degree-two rational homology character is
\[
\chi_2(g)=\operatorname{tr}\bigl(g\mid\widetilde H_2(K;\mathbb Q)\bigr)=
\begin{cases}
f_E(g)-f_V(g)+1,&\varepsilon(g)=+1,\\
a_E(g)-1,&\varepsilon(g)=-1.
\end{cases}
\]
This is a formula for each individual automorphism of every finite projective plane, whether or not Desarguesian or self-dual.

**Fano-plane specialization.** For \(\Pi=\operatorname{PG}(2,2)\), the complete incidence-graph automorphism group has order \(336\). On its \(168\)-element collineation subgroup the degree-two traces have distribution \(8:1\), \(1:48\), \(0:63\), \(-1:56\); on the \(168\) dualities the distribution is \(2:28\), \(0:84\), \(-1:56\). The resulting eight-dimensional rational representation is absolutely irreducible and has no nonzero invariants. For the orthogonality polarity \(\tau\) exchanging a nonzero binary point vector with the line having that same equation, there is also the integral \(\mathbb Z[C_2]\)-lattice classification
\[
\left.\widetilde H_2(K;\mathbb Z)\right|_{\langle\tau\rangle}
\cong\mathbb Z^{2}\oplus\mathbb Z[C_2]^{3},
\]
with the two displayed copies of \(\mathbb Z\) trivial and each regular summand carrying the interchange involution. This integral statement is stronger than the rational eigenspace dimensions \(5\) and \(3\).

## Assumptions and scope
A finite projective plane of order \(q\) has \(N=q^2+q+1\) points and \(N\) lines, with exactly \(q+1\) lines through each point and \(q+1\) points per line. Any two distinct points lie on exactly one common line, and dually for lines. All graph edges have length one; the Rips distance threshold is inclusive. There is no assertion that planes exist for all orders. The module statement concerns ordinary **integral simplicial homology** with its natural graph-automorphism action, not Borel equivariant homology.

## Proof
**1. A two-piece decomposition.** Every pair of distinct points has graph distance two, as does every pair of distinct lines. Incident point--line pairs have distance one and nonincident pairs have distance three. Thus \(K\) has a full simplex \(\Delta(P)\) on all points and another \(\Delta(L)\) on all lines. A mixed clique cannot contain two different points and two different lines: the two points would then lie on two common lines.

Let \(U\) be \(\Delta(P)\) together with, for each line \(\ell\), the simplex on \(\{\ell\}\cup P(\ell)\). Let \(V\) be the dual construction on \(\Delta(L)\), adding for each point \(p\) the simplex on \(\{p\}\cup L(p)\). Every clique lies in at least one of these two complexes, hence \(K=U\cup V\). Each extra line vertex in \(U\) belongs to a unique maximal simplex; its cone can be collapsed relative to the point-face already in \(\Delta(P)\). Consequently \(U\) collapses onto the full point simplex and is contractible. Dually, \(V\) is contractible. Their intersection \(U\cap V\) consists of precisely all vertices and incidence edges, so it is \(G\).

**2. Integral Mayer--Vietoris and the duality sign.** These simplicial inclusions are cofibrations. As \(U\), \(V\), and the connected graph \(G\) have known integral homology, the Mayer--Vietoris connecting map \(\partial_{MV}\) gives an isomorphism \(H_2(K;\mathbb Z)\xrightarrow{\sim}H_1(G;\mathbb Z)\) and vanishing of other reduced homology. The isomorphism is canonical after choosing the ordering \((U,V)\). On chains the intersection enters through \(c\mapsto(c,-c)\) in \(C_*(U)\oplus C_*(V)\). If an automorphism preserves point and line classes, it preserves the ordering and commutes with \(\partial_{MV}\). If it exchanges the classes, it swaps the two summands and changes this inclusion by a minus sign. Thus
\[
\partial_{MV}\circ g_* =\varepsilon(g)\,g_*\circ\partial_{MV},
\]
where the \(g_*\) on the right is the ordinary action on \(H_1(G;\mathbb Z)\). This proves the asserted twist over \(\mathbb Z\), not merely over a field. Its rank is the cycle rank of \(G\), namely
\[
|E(G)|-|V(G)|+1=(q+1)N-2N+1=q^3.
\]

**3. Each automorphism trace.** The oriented integral graph chain complex has the equivariant short exact sequence
\[
0\to H_1(G;\mathbb Q)\to C_1(G;\mathbb Q)\to C_0(G;\mathbb Q)\to\mathbb Q\to0.
\]
The last copy of \(\mathbb Q\) is trivial because the graph is connected. Hence the trace on \(H_1(G;\mathbb Q)\) is \(1+\operatorname{tr}(C_1)-\operatorname{tr}(C_0)\). For class-preserving \(g\), every setwise fixed incidence edge is orientation preserving, giving \(\operatorname{tr}(C_1)=f_E\), and \(\operatorname{tr}(C_0)=f_V\). For class-exchanging \(g\), the vertex trace is zero, and every setwise fixed edge is oriented backwards, giving \(\operatorname{tr}(C_1)=-a_E\). Multiplying by \(\varepsilon(g)\) proves both character formulas.

**4. Full Fano character and integral polarity module.** Represent its seven points and seven lines by the seven nonzero vectors of \(\mathbb F_2^3\), with incidence \(p\cdot\ell=0\). Every class-preserving automorphism arises from \(A\in\mathrm{GL}_3(\mathbb F_2)\), acting by \(p\mapsto Ap\) on points and \(\ell\mapsto(A^{-1})^\mathsf{T}\ell\) on lines. There are \((8-1)(8-2)(8-4)=168\) such matrices. The orthogonality polarity \(\tau\) identifies the two vector classes, and its coset gives all \(336\) incidence-graph automorphisms. The explicit finite enumeration in the verification program checks the complete class-preserving group independently among the \(7!\) permutations of the seven point labels, and checks the fixed-flag formula against signed simplicial Lefschetz traces for all \(336\) automorphisms. It yields the two displayed distributions.

The character inner product with itself for the full group is
\[
\frac{64+56+48+56+4\cdot28}{336}=1.
\]
Consequently the eight-dimensional rational representation stays irreducible after extending scalars to \(\mathbb C\), and since it is nontrivial it has no invariant vectors. The orthogonality polarity fixes three graph edges setwise, all by swapping their endpoints, because \(p\cdot p=0\) exactly for the three nonzero binary vectors of weight two. Its trace on \(H_2\) is therefore \(3-1=2\).

To retain integral information, identify \(H_1(G;\mathbb Z)\) with the integral flow lattice of graph edges. Choose a spanning tree, orient every edge from point to line and use the eight remaining chord edges for an integral basis of fundamental cycles. The verification program builds this lattice and computes the polarity's signed action on it, including the class-exchange twist. Its exact integer \(8\)-by-\(8\) involution matrix \(T\) satisfies \(T^2=I\), \(\operatorname{tr}T=2\), and \(\operatorname{rank}_{\mathbb F_2}(T-I)=3\).

For completeness, any involution on a finite-rank free abelian group is integrally conjugate to a direct sum of \(+1\)-blocks, \(-1\)-blocks, and two-by-two interchange blocks. One way to establish this is to take the primitive positive and negative eigensublattices: their direct sum has elementary \(2\)-group quotient in the ambient lattice, and the half-integral gluing projects injectively to the mod-two reductions of both eigensublattices. Choosing bases adapted to these paired gluing subspaces yields one interchange block per glued pair and leftover \(+1\)/\(-1\) blocks. The number of interchange blocks is precisely \(\operatorname{rank}_{\mathbb F_2}(T-I)\). Here there are three; the trace and total rank give \(a-b=2\) and \(a+b+6=8\), hence two trivial blocks and no sign blocks. This proves the integral polarity-module formula.

## Verification
The accompanying `verify_incidence_equiv.py` uses only Python's standard library. It constructs the Fano incidence graph directly, verifies its incidence axioms and all pairwise shortest-path distances, independently enumerates every scale-two Rips face by distance tests, checks the complete set of \(168\) point-preserving automorphisms among all \(7!\) point permutations, and enumerates all \(336\) point-line automorphisms. It compares a direct signed simplicial Lefschetz calculation with the fixed-flag character formula element by element. It also constructs an integral fundamental-cycle basis and checks the polarity's twisted integer matrix and its exact rank modulo two. The output is embedded separately as `verification_output.txt` and ends in `VERIFY_OK`.

The finite verification corroborates the Fano specialization. The theorem for *every* finite projective plane follows from the axioms, two-piece decomposition and natural integral Mayer--Vietoris sequence, not from extrapolating the finite enumeration.

## Relationship to prior work
Adamaszek's *Clique complexes and graph powers* (arXiv:1104.0433, submitted 2011-04-03) studies graph powers and their clique complexes; its Sections 2, 3, 5 and 6 contain homotopy criteria and explicit cycle-power results but no point-line incidence Rips representation or bipartition-exchanging action. Chambers, de Silva, Erickson and Ghrist's *Vietoris--Rips complexes of planar point sets* concerns Euclidean Rips shadows, not finite projective incidence graph automorphisms.

The particularly close published result *Scale-two Vietoris--Rips complexes of finite projective-plane incidence graphs* establishes the ordinary homotopy type \(\bigvee^{q^3}S^2\), the persistence multiplicities, and a nonequivariant two-contractible-piece argument. Those conclusions do not determine an automorphism action on the homology; an abstract equivalence to a suspension is not equivariant without specifying how point-line exchange acts on the two cones. The present theorem retains the canonical order of the two pieces, resolves the sign in the connecting homomorphism, determines the **integral** representation for all automorphisms, and provides the full Fano automorphism character plus its polarity-lattice structure. Its ordinary homology rank is acknowledged as previously covered, not claimed as new.

## Limitations
The general isomorphism depends on the axioms of a finite projective plane and the unweighted inclusive scale-two graph metric. It does not automatically extend to arbitrary partially linear incidence systems. The first Betti number and sphere-wedge homotopy type were known before this representation calculation; originality is asserted only for the integral equivariant refinement and its stated consequences. The character calculation is over characteristic zero; modulo-characteristic divisibility questions require the integral module, which the theorem supplies but does not classify for every automorphism subgroup. Unindexed equivalent accounts or a hidden equivariant deduction in another source remain possible. Independent mathematical audit has not been performed.

## References
1. M. Adamaszek, *Clique complexes and graph powers*, arXiv:1104.0433, first submitted 2011-04-03; Israel Journal of Mathematics 196 (2013), 295–319. https://arxiv.org/abs/1104.0433.
2. E. W. Chambers, V. de Silva, J. Erickson, R. Ghrist, *Vietoris–Rips complexes of planar point sets*, original author-hosted complete text: https://jeffe.cs.illinois.edu/pubs/pdf/rips.pdf.
3. *Scale-two Vietoris–Rips complexes of finite projective-plane incidence graphs*, publicly available research record (2026-10-04): https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-scale-two-vietoris-rips-complexes-of-finite-projective-plane-inc--c3740b96b3c3. Its nonequivariant homotopy/persistence calculation is prior coverage and is explicitly excluded from the claimed novelty.
