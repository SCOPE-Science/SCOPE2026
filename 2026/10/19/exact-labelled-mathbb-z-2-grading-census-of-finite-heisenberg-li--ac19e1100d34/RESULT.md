# Exact labelled \(\mathbb Z/2\)-grading census of finite Heisenberg Lie algebras

## Finding
Let \(q\) be any prime power and \(n\geq1\). Put \(H=H_n(q)=V\oplus\mathbb F_q z\), where \(\dim V=2n\) and \([u+az,v+bz]=\omega(u,v)z\) for a fixed nondegenerate alternating form \(\omega\). A **labelled \(\mathbb Z/2\)-grading** is an ordered decomposition \(H=H_0\oplus H_1\) such that \([H_i,H_j]\subseteq H_{i+j\bmod 2}\). The zero odd component is allowed. Distinct embedded component subspaces count as distinct gradings; this is not counting only equivalence classes.

Write
\[
 s_j(q)=q^{j^2}\prod_{h=1}^j(q^{2h}-1),\qquad s_0(q)=1.
\]
The complete count, separated by the degree of the one-dimensional center, is as follows.

**Even center.** For every \(r\in\{0,\ldots,n\}\), exactly
\[
 E_{n,r}(q)=q^{2(n-r)}\frac{s_n(q)}{s_r(q)s_{n-r}(q)}
\]
gradings have \(z\in H_0\), \(\dim H_0=2r+1\), and \(\dim H_1=2(n-r)\).

**Odd center.** Exactly
\[
 O_n(q)=q^{n(n+3)/2}\prod_{h=1}^n(q^h+1)
\]
gradings have \(z\in H_1\); every one has \((\dim H_0,\dim H_1)=(n,n+1)\).

Thus the total number of labelled gradings is
\[
 G_n(q)=O_n(q)+\sum_{r=0}^nE_{n,r}(q).
\]
Under the full Lie-algebra automorphism group there are exactly \(n+2\) orbits: one for each even-center \(r\) and one odd-center orbit, with the displayed orbit sizes. For fixed \(n\), as \(q\to\infty\) through prime powers,
\[
 \frac{O_n(q)}{G_n(q)}=1-q^{-n}+\mathcal{O}_n(q^{-n-1}).
\]
In characteristic two, all nontrivial gradings in this census are *not* obtained from eigenspaces of an inner adjoint idempotent \(\operatorname{ad}(h)^2=\operatorname{ad}(h)\): any such inner adjoint on \(H\) is zero. This is a boundary of that particular construction, not a statement about constructions involving arbitrary derivations or about simple Lie algebras.

## Assumptions and scope
The field is the full \(\mathbb F_q\), including extensions and characteristic two. The bracket is alternating, \([x,x]=0\), even in characteristic two. A grading is an **embedded ordered pair** of \(\mathbb F_q\)-linear subspaces with fixed group labels \(0,1\); only the final orbit statement identifies pairs under automorphisms. The center \(\mathbb F_q z\) is fixed as a subspace, not pointwise. The formula includes the trivial grading \((H,0)\) exactly once (\(r=n\)); it excludes a zero-even/whole-odd decomposition, which is not a grading because \([H,H]\ne0\).

## Proof
**1. The central degree.** The commutator ideal is \([H,H]=\mathbb F_q z\). For any group grading the commutator ideal is graded: each bracket of homogeneous vectors is homogeneous. Therefore the one-dimensional center is contained entirely in exactly one of \(H_0,H_1\). Projection \(\pi:H\to V=H/\mathbb F_qz\) yields an ordered direct sum \(V=U\oplus W\) with \(U=\pi(H_0)\) and \(W=\pi(H_1)\). The directness uses the fact that the center itself belongs to a single component.

**2. Even center.** Suppose \(z\in H_0\). Then \(H_0=\pi^{-1}(U)\) and \(H_1\) is a graph of a unique linear functional \(W\to\mathbb F_q z\). The only nonautomatic bracket condition is \([H_0,H_1]\subseteq H_1\). Because every bracket is central and \(H_1\cap\mathbb F_qz=0\), this is equivalent to \(\omega(U,W)=0\). Since \(V=U\oplus W\) and \(\omega\) is nondegenerate, \(U\) and \(W\) are mutually orthogonal nondegenerate symplectic subspaces. Hence \(\dim U=2r\), \(\dim W=2(n-r)\). The symplectic group acts transitively on nondegenerate \(2r\)-subspaces, with stabilizer \(\mathrm{Sp}_{2r}(q)\times\mathrm{Sp}_{2(n-r)}(q)\), so the number of choices of \(U\) is \(s_n(q)/(s_r(q)s_{n-r}(q))\). Its orthogonal complement is the unique \(W\). There are \(q^{2(n-r)}\) linear functionals on \(W\), which yields \(E_{n,r}(q)\), with no duplication.

**3. Odd center.** Suppose \(z\in H_1\). Now \(H_1=\pi^{-1}(W)\), and \(H_0\) is the graph of a linear functional \(U\to\mathbb F_q z\). The conditions \([H_0,H_0]\subseteq H_0\) and \([H_1,H_1]\subseteq H_0\) force \(\omega(U,U)=\omega(W,W)=0\), because \(H_0\) has zero intersection with the center. There is no restriction on \(\omega(U,W)\). Complementary totally isotropic subspaces of a \(2n\)-dimensional symplectic space are both Lagrangian and have dimension \(n\). The number of Lagrangians is \(\prod_{h=1}^n(q^h+1)\), by the transitive symplectic action and the standard parabolic stabilizer, or by recursive isotropic-line incidence. Fix one \(U\) and one Lagrangian complement \(W_0\). Every complementary Lagrangian \(W\) is the graph over \(W_0\) of a linear map into \(U\). The isotropy condition says that the corresponding \(n\times n\) matrix is symmetric, including in characteristic two. Thus exactly \(q^{n(n+1)/2}\) complements occur. Finally \(H_0\) has \(q^n\) choices of its graph functional. Their product gives \(O_n(q)\) without duplication.

**4. Automorphism orbits.** Every symplectic transformation of \(V\) lifts to an automorphism of \(H\) fixing \(z\). Symplectic transformations act transitively on nondegenerate symplectic decompositions of fixed \(2r\), and on ordered complementary Lagrangian pairs. A central shear \(v+az\mapsto v+(a+f(v))z\), for arbitrary \(f\in V^*\), removes or inserts any graph functional. The grading strata above therefore each form one full automorphism orbit. Different even-center \(r\) have different \(\dim H_0\), while center parity distinguishes the odd-center orbit even if component dimensions coincide. There are exactly \(n+2\) orbits.

**5. Asymptotic and characteristic-two boundary.** For fixed \(n\), \(s_n(q)=q^{2n^2+n}(1+\mathcal{O}_n(q^{-1}))\), so the highest degree of \(E_{n,r}(q)\) is \(4r(n-r)+2(n-r)\). Its unique maximum over integral \(0\le r\le n\) is \(n^2+n\), with leading coefficient one. Meanwhile \(O_n(q)=q^{n^2+2n}(1+\mathcal{O}_n(q^{-1}))\), giving the claimed proportion. In a class-two Lie algebra every \(\operatorname{ad}(h)\) has square zero. Consequently \(\operatorname{ad}(h)^2=\operatorname{ad}(h)\) forces \(\operatorname{ad}(h)=0\), so its eigenspace decomposition yields only the trivial grading, even though \(G_n(q)>1\) for every stated \(q,n\).

## Verification
The accompanying standalone script `check_gradings.py` generates every subspace by unique reduced-row-echelon bases, loops over complementary ordered pairs, and directly tests all three bracket inclusions. It does not classify candidates by isotropic subspaces before checking. The exhaustive cases \((n,q)=(1,2),(1,3),(1,4),(1,5),(2,2)\) give respectively \(G_n(q)=17,46,97,176,577\), with even-center and odd-center strata matching the formulas exactly. The \(q=4\) case implements \(\mathbb F_4\) as \(\mathbb F_2[t]/(t^2+t+1)\). Run `python3 check_gradings.py`; the required final message is `ALL_GRADING_COUNTS_PASSED 5`. These finite checks are not substitutes for the proof for all \(q,n\).

## Relationship to prior work
Calderón, Draper, Martín, and Sánchez (arXiv:1405.4093, 2014), Section 3 and Theorem 1, establish that group gradings of Heisenberg Lie algebras have homogeneous symplectic bases, and compute the automorphism group and the Weyl group of a fine grading. Those broad structural facts are **prior art** and are not claimed here. The current contribution counts all *embedded, fixed-label* \(\mathbb Z/2\)-component decompositions over each finite field by central degree, supplies their exact orbit cardinalities and large-field concentration, and distinguishes inner-adjoint constructions in characteristic two. The existence and structural classification of Heisenberg gradings alone is not new.

Eick and Moede (arXiv:2205.03155, initially available 2022-05-06), Sections 1, 2.1, and 4.1, develop the inner-adjoint-idempotent method for constructing characteristic-two gradings in **simple** finite Lie algebras. The present nilpotent examples do not contest its conclusions; they exhibit a different, explicitly enumerable part of the grading landscape. Hakavuori, Kivioja, Moisala, and Tripaldi, *Gradings for nilpotent Lie algebras* (2022 preprint), address classification up to equivalence over characteristic zero and torsion-free/maximal gradings, rather than the finite-field labelled \(\mathbb Z/2\) cardinalities here.

## Limitations
The contribution is an explicit finite-field enumerative refinement of an established qualitative Heisenberg-grading framework, **not** a new existence or general classification theorem for all group gradings. The published homogeneous-basis classification together with standard finite symplectic group formulas makes related derivations possible; no claim is made that none has been written elsewhere. This work does not classify graded isomorphisms beyond the stated automorphism orbits, nor graded Lie superalgebra enhancements in characteristic two. Exhaustive examples have small \(n,q\), whereas the general statements rely on the proof above. No independent review has been performed.

## References
1. A. Calderón, C. Draper, C. Martín and T. Sánchez, *Gradings and Symmetries on Heisenberg type algebras*, arXiv:1405.4093 (first submitted 2014-05-16), Section 3, Theorem 1. https://arxiv.org/abs/1405.4093
2. B. Eick and T. Moede, *Computing subalgebras and \(\mathbb Z_2\)-gradings of simple Lie algebras over finite fields*, arXiv:2205.03155 (first submitted 2022-05-06), Sections 1, 2.1 and 4.1; *Communications in Mathematics* 30 (2022), 37–50. https://arxiv.org/abs/2205.03155
3. E. Hakavuori, V. Kivioja, T. Moisala and F. Tripaldi, *Gradings for nilpotent Lie algebras*, 2022 preprint, Sections 2.1 and 3.1. https://hakavuori.fi/publication/gradings-2022-01-11.pdf
