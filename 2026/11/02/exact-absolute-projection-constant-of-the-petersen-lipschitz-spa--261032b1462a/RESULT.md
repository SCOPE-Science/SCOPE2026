# Exact absolute projection constant of the Petersen Lipschitz space

## Finding

Let \(P=KG(5,2)\) be the Petersen graph: its ten vertices are the two-element subsets of \(\{1,2,3,4,5\}\), and two vertices are adjacent exactly when disjoint. Give \(P\) unit edge lengths and the shortest-path metric. Fix any base vertex. For the **real**, nine-dimensional Banach space \(X=\operatorname{Lip}_0(P)\), equipped with its usual Lipschitz norm, the absolute linear projection constant is exactly

\[
\boxed{\lambda(X)=\frac{11}{5}.}
\]

In its canonical isometric realization as the edge-gradient space \(C\subset\ell_\infty^{15}\), the Euclidean orthogonal projection onto \(C\) attains this minimum. Moreover, this is the **unique** projection onto \(C\) commuting with the natural signed \(S_5\) edge action. Uniqueness is asserted only among equivariant projections: there may be nonsymmetric minimizers.

## Assumptions and scope

For a real finite-dimensional Banach space \(X\), write \(\lambda(X)=\sup_{X\hookrightarrow Y}\inf\{\|Q\|:Q:Y\to X\text{ is a bounded linear projection}\}\), where the supremum runs through isometric embeddings into Banach spaces. Take each oriented Petersen edge once and let \(B\) be the \(15\times10\) vertex-to-edge incidence matrix, \((Bf)_{(u,v)}=f(v)-f(u)\). Set \(C=\operatorname{im}B\). Because graph distances are shortest-path distances, \(\|f\|_{\operatorname{Lip}}=\max_{uv\in E(P)}|f(v)-f(u)|\), so \(X\) is isometric to \(C\), independently of the chosen base vertex and orientation. Connectedness gives \(\operatorname{rank} B=9\).

This theorem is about the absolute projection constant of \(\operatorname{Lip}_0(P)\), **not** about the Euclidean distortion of the metric, nor the projection constant of the dual Lipschitz-free space. All scalars are real.

## Proof

**1. Reduction to the edge cube.** Let \(\lambda(C,\ell_\infty^{15})\) be the least norm of an idempotent from \(\ell_\infty^{15}\) onto \(C\). The absolute projection constant equals this number. Indeed, the edge embedding is isometric. Conversely, for any isometric copy of \(X\) in any Banach space \(Y\), the identity from that copy to \(C\subset\ell_\infty^{15}\) extends to a norm-one map \(T:Y\to\ell_\infty^{15}\), because real \(\ell_\infty^{15}\) is injective (extend each coordinate functional by Hahn–Banach). If \(Q\) is any projection from \(\ell_\infty^{15}\) onto \(C\), then \(Q T\), followed by the inverse edge embedding, is a projection from \(Y\) onto its copy of \(X\), with norm at most \(\|Q\|\). Taking the supremum yields the assertion.

**2. Symmetry reduction.** Permutations of \(\{1,2,3,4,5\}\) act as automorphisms of \(P\) and as signed coordinate permutations \(U_g\) on the oriented edge space. They preserve \(C\) and have \(\ell_\infty\)-operator norm one. For any projection \(Q\) onto \(C\), the average \(\overline Q=\frac1{120}\sum_{g\in S_5}U_g Q U_g^{-1}\) also projects onto \(C\), commutes with all \(U_g\), and satisfies \(\|\overline Q\|\le\|Q\|\). Hence it suffices to determine equivariant projections.

**3. Signed-stabilizer row lemma.** Fix an edge \(e=uv\). Its subgroup of setwise stabilizers in \(S_5\) has order eight. If \(q\) is row \(e\) of an equivariant operator, then for every stabilizer element \(g\), \(qU_g=\varepsilon_gq\), where \(\varepsilon_g\in\{-1,1\}\) is the sign of the oriented image of \(e\). Directly classify the fifteen edges under the stabilizer. There is one base edge, four edges sharing an endpoint with it, eight further edges bearing nonzero alternating coefficients, and two edges whose coefficients must vanish: a stabilizer permutation fixes each of the last two edges while reversing its orientation relative to \(e\). On each of the other three orbits the sign condition permits precisely one scalar degree of freedom. Thus every such row is of the form

\[
q=a w_0+b w_1+c w_2,
\]

where \(w_0\) is the signed base-edge indicator; \(w_1\) equals \(\pm1\) on the four incident edges and zero elsewhere; and \(w_2\) equals \(\pm1\) on the eight remaining nonzero positions, with signs chosen as the gradients specified below. In particular, their supports are disjoint, so \(\|q\|_1=|a|+4|b|+8|c|\). For full explicit signs, orient edges lexicographically by endpoint two-subsets and choose \(w_j\) to be the sign of the corresponding coordinate in the vector \(B h\), where

\[
h=\tfrac1{10}(4I+A)(\delta_v-\delta_u),
\]

and \(A\) is the Petersen vertex-adjacency matrix. The nonzero values of \(B h\) on these three supports are respectively \(3/5,\pm1/5,\pm1/10\). This makes the sign conventions entirely explicit and independent of a picture. The finite orbit/sign computation can be reconstructed with the accompanying exact-rational verifier, which checks the signed-stabilizer constraint matrix has rank twelve, leaving precisely three free coordinates.

Apply the incidence matrix to the row and let \(N(u),N(v)\) denote vertex-neighborhoods. A direct incidence count gives

\[
(w_0B)=\delta_v-\delta_u,\qquad
(w_1B)=2(\delta_v-\delta_u)+T,\qquad
(w_2B)=-2T,
\]

where \(T=\sum_{z\in N(v)\setminus\{u\}}\delta_z-\sum_{z\in N(u)\setminus\{v\}}\delta_z\). The two vectors \(\delta_v-\delta_u\) and \(T\) are independent. Consequently the necessary and sufficient constraint \(qB=B_e\), for an equivariant retraction, is

\[
a+2b=1,\qquad b=2c.
\]

Every projection onto \(C\) has trace equal to \(\dim C=9\). By edge transitivity and equivariance, all fifteen diagonal entries are equal; the diagonal is \(a\). Hence \(15a=9\). Solving gives \(a=3/5\), \(b=1/5\), \(c=1/10\). The equivariant projection is therefore unique, and every such projection has

\[
\|Q\|_{\ell_\infty^{15}\to\ell_\infty^{15}}=\|q\|_1
=\frac35+4\frac15+8\frac1{10}=\frac{11}{5}.
\]

**4. Attainment.** The Petersen adjacency matrix satisfies \(A^2=2I-A+J\), with \(J\) the all-ones matrix. Its Laplacian is \(L=B^{\mathsf T}B=3I-A\). On the zero-sum vertex subspace, \((3I-A)(4I+A)=10I\). Thus for any oriented edge \(e=uv\), its potential \(h_e=(4I+A)(\delta_v-\delta_u)/10\) solves \(Lh_e=\delta_v-\delta_u\). The Euclidean orthogonal edge-gradient projection \(P_0=B L^\dagger B^{\mathsf T}\) has row \(e\) equal to \((Bh_e)^{\mathsf T}\). The potential takes values \(-3/10\) at \(u\), \(+3/10\) at \(v\), \(-1/10\) at each of the two other neighbors of \(u\), \(+1/10\) at each of the two other neighbors of \(v\), and zero at all remaining vertices. Its edge gradients therefore have absolute-value multiplicities \(1,4,8,2\) for \(3/5,1/5,1/10,0\), proving \(\|P_0\|_{\infty\to\infty}=11/5\). Symmetry reduction proves that no other projection can have smaller norm, completing the proof.

## Verification

Run the accompanying standalone Python 3 script with `python verify_petersen_projection.py`. It uses only the standard library and exact rational arithmetic, constructs the ten two-subset vertices and fifteen disjointness edges, checks the adjacency identity, verifies the fifteen-by-fifteen Hodge projection is a symmetric idempotent fixing all gradients, enumerates all \(120\) signed edge automorphisms, and calculates that the stabilizer constraint matrix has rank \(12\). It also checks all row-support multiplicities and the three scalar equations above. A successful run prints `CHECK_OK automorphisms=120 signed_stabilizer_rank=12 hodge_rows=15 rational_projector_identities=yes`.

These finite exact calculations verify the critical finite graph identities; the argument for arbitrary Banach superspaces is the analytical Hahn–Banach/injectivity step, not a finite enumeration.

## Relationship to prior work

The general theory of absolute projection constants, injective ambient spaces and symmetry averaging is classical and is developed in Defant–Galicer–Mansilla–Mastyło–Muro (2022). Dilworth–Kutzarova–Ostrovskii (2018) develop edge/cycle realizations and symmetry methods for Lipschitz-free spaces of finite graphs, focusing in particular on diamond and Laakso families. Basso (2021) gives a general linear-program method for relative projection constants in finite-dimensional polyhedral spaces. None of these inspected statements supplies the numerical projection constant of the Petersen graph's real Lipschitz-function space. This claim concerns the dual gradient subspace, not the metric \(\ell_1\)-distortion of the Petersen graph, the Euclidean inradius of its symmetric edge polytope, or the constants of different graph families. An earlier computation under different projection terminology cannot be excluded from the available search.

## Limitations

The assertion concerns one canonical nine-dimensional Banach space and real scalar projections. The argument does not establish the minimum projection constant of the Lipschitz-free dual, nor constants for all Kneser graphs, other edge weights, or complex scalars. The uniqueness statement is restricted to automorphism-equivariant projections. General historical-priority searches cannot prove worldwide uniqueness; independent mathematical audit has not been performed.

## References

1. A. Defant, D. Galicer, M. Mansilla, M. Mastyło and S. Muro, *Projection constants for spaces of multivariate polynomials*, arXiv:2208.06467v1 (first posted 2022-08-12), especially Introduction and Chapter 2, https://arxiv.org/pdf/2208.06467.
2. S. J. Dilworth, D. Kutzarova and M. I. Ostrovskii, *Lipschitz free spaces on finite metric spaces*, arXiv:1807.03814v1 (2018), especially Sections 1, 4–6, https://arxiv.org/pdf/1807.03814.
3. G. Basso, *Absolute Lipschitz extendability and linear projection constants*, arXiv:2104.14238 (2021), especially Section 5.2, https://arxiv.org/pdf/2104.14238.
