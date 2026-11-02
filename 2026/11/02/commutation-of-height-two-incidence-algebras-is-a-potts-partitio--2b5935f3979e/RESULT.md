# Commutation of height-two incidence algebras is a Potts partition function with a two-forest exponent

## Finding

Let \(P\) be a finite nonempty poset with no strict chain of three distinct elements, let \(G=(V,E)\) be its undirected strict-comparability graph, and let \(A=I(P,\mathbb F_q)\) for any prime power \(q\). Write \(v=|V|\), \(m=|E|\), and, for \(F\subseteq E\), let \(k(F)\) be the number of connected components of \((V,F)\), including isolated vertices, and \(r(F)=v-k(F)\). For two independent uniform elements of \(A\), their commuting probability is exactly

\[
\mathcal P_G(q)=q^{-m}\sum_{F\subseteq E}(q-1)^{|F|}q^{-2r(F)}.
\]

Equivalently, the exact number of ordered commuting pairs is

\[
\mathcal C_G(q)=q^m\sum_{F\subseteq E}(q-1)^{|F|}q^{2k(F)}.
\]

The first formula is the Fortuin--Kasteleyn expansion of the \(q^2\)-state Potts partition function with edge weight \(q-1\), normalized by \(q^{m+2v}\); it is a specialization of the Tutte polynomial. In particular, the probability depends only on the graphic matroid of \(G\), not on the orientation of its comparabilities or on isolated vertices.

Put \(p_q=(q-1)/q^2\) and \(\rho_q=(q-1)/(q^2+q-1)\). If \(F_{\rho_q}\) retains edges independently with probability \(\rho_q\), and \(\beta(F)=|F|-r(F)\) is the cycle rank, then

\[
\mathcal P_G(q)=q^{-m}(1+p_q)^m\,\mathbb E\bigl[q^{2\beta(F_{\rho_q})}\bigr].
\]

Thus \(\mathcal P_G(q)\ge q^{-m}(1+p_q)^m\) for every \(q\ge2\), with equality **if and only if** \(G\) is a forest. For a connected height-two poset, this is also the toricity criterion for its incidence monoid under the two-sided maximal-torus action, by the known theorem of Bilen Can.

For a **fixed** finite graph \(G\), define \(s_2(G)\) to be the maximum number of its edges that can be partitioned into two forests (empty forests allowed). Then, as \(q\to\infty\) through prime powers,

\[
\mathcal P_G(q)=\nu_G q^{-s_2(G)}\bigl(1+O_G(q^{-1})\bigr),
\]

where the positive integer \(\nu_G\) is precisely the number of subsets \(F\subseteq E\) maximizing \(|F|-2r(F)\). The large-field decay exponent is consequently the rank of the union of two copies of the graphic matroid. It equals \(m\) exactly when the edges of \(G\) can be partitioned into two forests. At the density boundary, the leading constant need not be one: for \(K_{3,4}\), it is two and the exponent is twelve, while for \(K_{4,4}\) the leading constant is one and the exponent is fourteen although the graph has sixteen edges.

## Assumptions and scope

The poset may be disconnected, may have isolated vertices, and need not be graded; the only structural assumption is the absence of three distinct elements \(x<y<z\). The strict-comparability graph is simple and bipartite. The field may have any prime-power order, including characteristic two. Commutation means \(ab=ba\) in the **full** incidence algebra; no restriction to units, radicals, or idempotents is made. The asymptotic holds for a fixed poset, not uniformly over growing graph families. The toric comparison is asserted only for connected posets in the setting of the cited established theorem.

## Proof

Choose a linear extension of \(P\). Every element \(a\in A\) has independent diagonal entries \(d_u\in\mathbb F_q\) for \(u\in V\) and off-diagonal entries \(x_e\in\mathbb F_q\) for \(e=(u,v)\in E\) with \(u<v\). Since no three distinct elements form a chain, there are no products of two strictly off-diagonal basis elements. For a second element \(b=(h_u,y_e)\), the condition \(ab=ba\) is therefore the collection, one per edge \(e=(u,v)\), of equations

\[
(d_u-d_v)y_e-(h_u-h_v)x_e=0.
\]

For fixed diagonal values, let \(\xi_u=(d_u,h_u)\in\mathbb F_q^2\). An edge with \(\xi_u=\xi_v\) imposes no restriction on \((x_e,y_e)\), giving \(q^2\) possibilities. An edge with \(\xi_u\ne\xi_v\) imposes exactly one nonzero linear equation in two variables, giving \(q\) possibilities. The edge variables are disjoint, so their choices multiply. As the \(\xi_u\) are independent and uniform among \(q^2\) colors, this gives

\[
\mathcal P_G(q)=q^{-m-2v}\sum_{\xi:V\to\mathbb F_q^2}\prod_{uv\in E}\left(1+(q-1)\mathbf{1}_{\xi_u=\xi_v}\right).
\]

Expanding the product over all edge subsets \(F\), colorings constant on each component of \((V,F)\) number \(q^{2k(F)}\). This proves the probability formula, and multiplication by \(|A|^2=q^{2(v+m)}\) gives the ordered-pair formula. Using the standard Fortuin--Kasteleyn--Tutte identity, one may also write

\[
\mathcal P_G(q)=q^{-m-2r(E)}(q-1)^{r(E)}
 T_G\!\left(1+\frac{q^2}{q-1},q\right).
\]

The expression in terms of \(r(F)\) shows that \(\mathcal P_G(q)\) is invariant under graphic-matroid isomorphisms. Setting \(p_q=(q-1)/q^2\), the summand equals \(p_q^{|F|}q^{2\beta(F)}\). Normalize the weights \(p_q^{|F|}\) into independent Bernoulli-edge probabilities with parameter \(\rho_q=p_q/(1+p_q)\) to obtain the percolation expectation. The cycle rank is nonnegative and is zero for every edge subset exactly when \(G\) is a forest; if \(G\) has a cycle, its edge set occurs with positive probability and makes the expectation strictly larger than one. The cited toric characterization concerns precisely connected height-two incidence monoids with forest Hasse graph; for such posets the Hasse and strict-comparability graphs coincide.

For the large-field claim, rewrite each summand as

\[
(q-1)^{|F|}q^{-2r(F)}=q^{|F|-2r(F)}(1-q^{-1})^{|F|}.
\]

Let \(\Delta_G=\max_{F\subseteq E}(|F|-2r(F))\). The empty set gives \(\Delta_G\ge0\). Because the sum has finitely many terms with positive leading coefficients, the leading power of \(q\) is \(\Delta_G\), and its coefficient is exactly \(\nu_G\). Hence

\[
\mathcal P_G(q)=q^{-(m-\Delta_G)}(\nu_G+O_G(q^{-1})).
\]

The rank formula for the union of two graphic matroids (Edmonds' matroid-union theorem) states

\[
s_2(G)=\min_{F\subseteq E}\bigl(|E\setminus F|+2r(F)\bigr)=m-\Delta_G.
\]

This identifies the exponent. In particular, \(s_2(G)=m\) if and only if the entire edge set is a union of two forests, completing the proof. For \(K_{3,4}\) and \(K_{4,4}\), an explicit enumeration of the \(2^{12}\) and \(2^{16}\) edge subsets respectively gives \((s_2,\nu)=(12,2)\) and \((14,1)\); the included verifier reproduces these finite examples. Neither finite enumeration is used to prove the all-graph theorem.

## Verification

The attached standalone `verify.py` checks the equation \(ab=ba\) through direct incidence-algebra multiplication in nine small prime-field instances, independently matches the Potts coloring sum against the random-cluster edge-subset expansion in sixteen instances, and checks the two-forest rank via a separate exhaustive two-color forest partition algorithm in ten graphs. It includes both sparse and cyclic bipartite graphs and the dense \(K_{3,4}\), \(K_{4,4}\) examples. Run `python3 verify.py` with the Python standard library; the successful output ends with `VERIFY_OK 9 direct algebra cases, 16 independent color sums, 10 two-forest rank checks`.

The proof, not these finite tests, supplies the all-poset and all-prime-power conclusions. The finite checker enumerates prime fields only, and the matroid-union identification uses a classical theorem rather than a new proof of that theorem.

## Relationship to prior work

Bilen Can's 2021 study of incidence monoids establishes their algebraic-semigroup and toric complexity structure, including the forest characterization of toric height-two cases, but does not enumerate ordered commuting pairs over finite fields. Fornaroli, Khrypchenko, and Santulo's 2022 study characterizes bijective commutativity preservers of incidence algebras, including centralizer lemmas, but does not give the present complete commuting-pair count or Tutte specialization. The published graphical-group enumeration of Rossmann addresses conjugacy classes and centralizers of a different graph-associated group rather than the associative incidence algebra considered here.

The Fortuin--Kasteleyn expansion, Tutte polynomial, Edmonds' matroid-union rank formula, and Nash--Williams' forest-covering criterion are established results and are not claimed as new. A published single-arrow Kronecker path-algebra commuting probability matches the one-edge specialization; likewise, an earlier complete-bipartite incidence-algebra centralizer study concerns a special graph family. Neither accessible statement supplies the general graph-matroid formula or the two-forest exponent for all height-two incidence algebras. The new contribution asserted here is the algebra-to-Potts identification and its structural consequences, not the pre-existing combinatorial identities separately.

## Limitations

The height-two hypothesis is essential for the edge equations to decouple; the formulas are not claimed for arbitrary longer posets or for multiple arrows. The large-field asymptotic is for fixed \(G\). Equivalence under the graphic matroid does not imply that the numerical probability determines that matroid. An unlocated broader theorem about commuting probabilities of square-zero extensions may implicitly subsume the exact formula; publication priority remains provisional. No independent mathematical audit has been performed.

## References

- M. Bilen Can, *Incidence Monoids: Automorphisms and Complexity*, first posted May 20, 2021, arXiv:2105.09826, especially Theorem 1.3.
- É. Z. Fornaroli, M. Khrypchenko, and E. A. Santulo Jr., *Commutativity preservers of incidence algebras*, first posted July 21, 2022, arXiv:2207.10713, especially Section 1.3 and Theorem 3.35.
- T. Rossmann, *Enumerating conjugacy classes of graphical groups over finite fields*, *Bulletin of the London Mathematical Society* 54 (2022), DOI:10.1112/blms.12665.
- C. M. Fortuin and P. W. Kasteleyn, *On the random-cluster model. I. Introduction and relation to other models*, *Physica* 57 (1972), DOI:10.1016/0031-8914(72)90045-6 (classical graph partition-function identity).
- J. Edmonds, *Matroid partition*, in *Mathematics of the Decision Sciences*, 1968 (classical matroid-union and partition results).
