# Chromatic thresholds for commutator products in finite quiver-algebra unit groups

## Finding

Let \(Q\) be a finite quiver with a nonempty vertex set \(V\), with loops and parallel arrows permitted. For any prime power \(q\), let \(k=\mathbb F_q\), let \(J\) be the arrow ideal, and let
\[
 A=kQ/J^2,\qquad G=A^\times.
\]
For every unordered pair \(e=\{i,j\}\) of **distinct** vertices, let \(\mu_e\) be the total number of arrows in either direction between \(i\) and \(j\). Let \(H\) be the simple graph with edge set \(E(H)=\{e:\mu_e>0\}\). Write \(J_{\mathrm{off}}\) for the span of all nonloop arrows. For \(y\in J_{\mathrm{off}}\), its support graph \(H_y\) has precisely those edges \(e\) on which at least one of the \(\mu_e\) arrow coordinates of \(y\) is nonzero. Isolated vertices are retained in support graphs. An edgeless graph on \(V\) has chromatic number \(1\).

**Theorem.** If \(q=2\), then \(G\) is abelian. If \(q>2\), then
\[
 G' = 1+J_{\mathrm{off}}.
\]
For every integer \(r\ge1\) and every \(y\in J_{\mathrm{off}}\), the following conditions are equivalent:

1. \(1+y\) is a product of \(r\) ordinary group commutators in \(G\) (allowing identity factors);
2. \(\chi(H_y)\le(q-1)^{2r}\).

No unit outside \(1+J_{\mathrm{off}}\) is a product of commutators. Consequently, for nonzero \(y\in J_{\mathrm{off}}\), its minimum commutator length is the least positive integer \(r\) such that \(\chi(H_y)\le(q-1)^{2r}\); the identity has length zero. If \(H\) has at least one edge, the commutator width of \(G\) is
\[
 \boxed{\operatorname{cw}(G)=\left\lceil\log_{(q-1)^2}\chi(H)\right\rceil.}
\]
The width is zero when \(H\) is edgeless. For every integer \(r\ge1\), the number of **distinct outputs** of products of \(r\) commutators is exactly
\[
 \boxed{\left|[G,G]_{\mathrm{word}}^{\,r}\right|=
 \sum_{\substack{F\subseteq E(H)\\ \chi((V,F))\le(q-1)^{2r}}}
 \prod_{e\in F}(q^{\mu_e}-1).}
\]
The product over the empty set is \(1\). This is an image-size formula, not a formula for the number of representing tuples. All assertions are insensitive to arrow orientations; multiplicities influence image sizes, but not commutator width.

For instance, if \(q=3\) and \(H=K_5\) with exactly one arrow on each undirected edge, then \(G'\) has \(3^{10}=59049\) elements, the image of one commutator has \(59049-2^{10}=58025\) elements, and \(\operatorname{cw}(G)=2\). For fixed \(q>2\), the algebras with underlying graphs \(K_{(q-1)^{2r}+1}\) have commutator width \(r+1\). Thus commutator width is unbounded within this class of finite metabelian groups when the field is fixed.

## Assumptions and scope

The quotient \(J^2=0\) is essential. A group commutator is \([g,h]=ghg^{-1}h^{-1}\), and its length means the minimum number of such commutators whose product is the target. Reversing the convention does not affect the word image or length because inverses of commutators are commutators. Every quiver vertex is present, even an isolated vertex. The base field may have arbitrary prime-power order; the logarithmic expression is used only for \(q>2\).

For the image-size formula, distinct arrows with the same unordered endpoints are separate coordinates but a single graph edge. A vertex loop is a coordinate in \(J\), not an edge of \(H\). The counting formula includes the identity as its empty-support term. The zero-fold product has just the identity, and is not included in the displayed formula for \(r\ge1\).

## Proof

**1. A square-zero semidirect product.** The vertex idempotents give a split semisimple subalgebra \(S=\bigoplus_{i\in V}ke_i\cong k^V\). Every unit is uniquely \((1+x)t\), with \(x\in J\) and \(t=\sum_i t_ie_i\in S^\times\), where every \(t_i\in k^\times\). Since \(J^2=0\), the subgroup \(1+J\) is its additive group and
\[
 G=(1+J)\rtimes T,\qquad T=(k^\times)^V.
\]
For an arrow \(a:i\to j\), conjugation by \(t\in T\) multiplies its coordinate by \(\lambda_a(t)=t_i/t_j\). On loops this character equals \(1\). In coordinates \((x,t)=(1+x)t\), the group law is \((x,t)(z,s)=(x+t\cdot z,ts)\). A direct multiplication, including both inverses, gives the commutator identity
\[
 [(x,t),(z,s)]=\big((1-s)\cdot x+(t-1)\cdot z,1\big).
\]
In the arrow coordinate \(a:i\to j\), its coefficient is
\[
 (1-\lambda_a(s))x_a+(\lambda_a(t)-1)z_a.\tag{1}
\]
This is independently verifiable by multiplication in \(A\).

**2. Derived subgroup and the small-field boundary.** Formula (1) vanishes on every loop. Hence \(G'\subseteq1+J_{\mathrm{off}}\). If \(q>2\), for each arrow between distinct vertices choose \(t\in T\) with \(t_i\ne t_j\). With \(x=0\) and only the corresponding coordinate of \(z\) nonzero, equation (1) yields any desired scalar multiple of that arrow. Such single-coordinate commutators generate \(1+J_{\mathrm{off}}\), proving equality. If \(q=2\), then \(T\) is trivial and \(G=1+J\) is abelian.

**3. Necessity of graph coloring.** Suppose \(1+y\) is a product of \(r\) commutators. For the \(h\)-th factor, write its two torus components as \(t^{(h)},s^{(h)}\in T\). Every arrow coordinate of this factor is zero if the endpoints have equal torus labels for both components. This follows directly from (1), independently of its unipotent inputs. Since products of commutators simply add arrow coordinates, each graph edge \(\{i,j\}\) in \(H_y\) must be separated by at least one of the \(2r\) torus components. Thus the vertex map
\[
 i\longmapsto\big(t_i^{(1)},s_i^{(1)},\ldots,t_i^{(r)},s_i^{(r)}\big)
 \in(k^\times)^{2r}
\]
is a proper coloring of \(H_y\) using at most \((q-1)^{2r}\) colors.

**4. Sufficiency and an explicit realization.** Conversely let \(c:V\to(k^\times)^{2r}\) be a proper coloring of \(H_y\). Its \(2r\) components specify \(t^{(h)},s^{(h)}\in T\). At every arrow \(a:i\to j\) with \(y_a\ne0\), some coordinate distinguishes \(c(i)\) and \(c(j)\). For at least one \(h\), either \(1-\lambda_a(s^{(h)})\ne0\) or \(\lambda_a(t^{(h)})-1\ne0\). Assign \(y_a\) to that commutator alone, by setting the corresponding \(x_a\) or \(z_a\) equal to \(y_a\) divided by that nonzero coefficient; set all other contributions on that arrow to zero. Do this independently for every arrow, including parallel arrows and both orientations. Set loop coordinates to zero. Formula (1) then shows that the product of these \(r\) commutators is precisely \(1+y\).

**5. Width and image size.** The minimum-length assertion is the combination of steps 3 and 4. Every support graph is a spanning subgraph of \(H\), hence has chromatic number at most \(\chi(H)\). Selecting one nonzero arrow coordinate on every edge produces a support graph equal to \(H\), giving the matching lower bound for group width. For a fixed edge support \(F\), all \(\mu_e\) coordinates associated with an edge \(e\in F\) may be chosen arbitrarily except that they cannot all be zero; there are exactly \(q^{\mu_e}-1\) choices. Different supports are disjoint, and steps 3 and 4 decide their membership in the word image. Summing these independent counts gives the image-size formula.

For \(K_5\) at \(q=3\), four available colors cannot color the whole graph, but every proper edge-subgraph of \(K_5\) is four-colorable (delete an edge and merge its endpoints, then delete further edges). Exactly \(2^{10}\) radical vectors have every arrow coordinate nonzero. Therefore one commutator reaches the remaining \(3^{10}-2^{10}\) elements, and two commutators reach all of \(G'\). The general complete-graph family follows similarly from \(\chi(K_N)=N\).

## Verification

The attached standalone file `verify.py` constructs units using the original quotient-algebra product \((t,a)(s,b)=(ts,(t_i b_a+a_a s_j)_a)\), forms commutators with group inverses, and enumerates the entire one-commutator image in seven small cases. It tests characteristic two, fields of orders three and four (with explicit extension-field arithmetic), a loop, opposite arrows and a directed triangle. In each case the exact image equals the independently computed graph-colorability prediction. It separately verifies that no commutator on the five-vertex complete graph over \(\mathbb F_3\) has full arrow support, then explicitly constructs two commutators whose product has all ten coordinates equal to \(1\). The execution terminates with `ALL_EXACT_COMMUTATOR_CHECKS_PASSED`.

The proof, not the finite enumeration, establishes the theorem for all quivers, all admissible fields and all positive word lengths. Neither this checker nor the proof counts representation fibers for nonzero targets.

## Relationship to prior work

Iovanov and Sistko (2017) develop a classification of maximal subalgebras of finite-dimensional algebras, including quiver algebras and radical filtrations. That work supplies context for the algebra family but does not in its inspected sections classify products of unit-group commutators. Nikolov and Segal (2011/2012) give general factorization bounds for finite-group commutators as functions of generating parameters, not the support-sensitive exact criterion here. Bartholdi, Groth and Lysenok (2017/2022) investigate commutator width of the first Grigorchuk group, which is not the present finite metabelian family.

Previously recorded results for units of radical-square-zero quiver algebras calculate class numbers, commuting probabilities and torsion order distributions using graph polynomials; those totals do not determine the possible nonzero supports of an individual commutator or the minimal length of each target. A separate published calculation of additive commutator fibers in generalized Kronecker path algebras counts commutators of ring elements, rather than ordinary *group* commutators in arbitrary quiver-algebra unit groups. The present theorem is a word-image and commutator-width classification; it makes no new claim about those earlier totals or about general graph-coloring theory.

## Limitations

This is a theorem for unit groups of square-zero-arrow quiver algebras, not for arbitrary finite-dimensional algebra unit groups or for untruncated path algebras. The theorem determines which targets occur and the number of distinct outputs, not their individual representation-fiber multiplicities. It uses ordinary vertex chromatic number; efficient evaluation on arbitrary graphs is not asserted. It does not recover orientation or multiplicities from widths alone. No claim of historical uniqueness is made: an equivalent result under semidirect-product representation or graph-coloring terminology may exist outside the inspected sources.

## References

1. M. C. Iovanov and A. Sistko, *Maximal Subalgebras of Finite-Dimensional Algebras*, arXiv:1705.00762v1 (first posted 2017-05-02); Sections 2 and 4, especially Theorem 4.1 and Proposition 4.2. https://arxiv.org/abs/1705.00762
2. N. Nikolov and D. Segal, *Generators and commutators in finite groups; abstract quotients of compact groups*, arXiv:1102.3037, *Invent. Math.* 190 (2012), 513–602; introduction and Theorems 1.2–1.3. https://arxiv.org/abs/1102.3037
3. L. Bartholdi, T. Groth and I. Lysenok, *Commutator width in the first Grigorchuk group*, arXiv:1710.05706v1 (2017), *Groups Geom. Dyn.* 16 (2022), 493–522; introduction. https://arxiv.org/abs/1710.05706
4. *Commutator fibers and commuting probabilities of finite Kronecker path algebras*, publicly available research record (2026), concerning additive commutators of ring elements rather than unit-group word images.
