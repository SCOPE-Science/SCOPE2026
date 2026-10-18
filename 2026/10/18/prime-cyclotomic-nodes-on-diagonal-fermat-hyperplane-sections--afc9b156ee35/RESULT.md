# Prime-cyclotomic nodes on diagonal Fermat hyperplane sections

## Finding
Let \(p\ge3\) be an odd prime and \(N\ge5\) an integer. Over \(\mathbb Q\) put
\[
X_{p,N}=V\!\left(\sum_{i=1}^{N}x_i,\ \sum_{i=1}^{N}x_i^{p+1}\right)\subset\mathbb P^{N-1}_{\mathbb Q}.
\]
Viewed inside the first hyperplane, this is a hypersurface of dimension \(N-3\). It is geometrically integral and normal. If \(p\nmid N\), it is smooth. If \(N=pm\), with \(m\ge1\) and \(N\ge5\), it has exactly
\[
A_{p,m}=\frac{(pm)!}{p(m!)^p}
\]
geometric singular points, and every one is an ordinary double point. There are no other singularities. Its *scheme-theoretic* singular locus \(S_{p,m}\) over \(\mathbb Q\) is finite étale, with
\[
S_{p,m}\cong\coprod_{j=1}^{B_{p,m}}\operatorname{Spec}\mathbb Q(\zeta_p),
\qquad B_{p,m}=\frac{(pm)!}{p(p-1)(m!)^p}.
\]
In particular, no closed singular point is rational over \(\mathbb Q\); every closed singular point has degree \(p-1\). The set of geometric nodes, with its natural \(\mathfrak S_{pm}\)-action, is the transitive set
\[
\mathfrak S_{pm}\big/\bigl((\mathfrak S_m)^p\rtimes C_p\bigr),
\]
where \(C_p\) cyclically permutes the \(p\) blocks. The Galois-orbit set of closed singular points is
\[
\mathfrak S_{pm}\big/\bigl((\mathfrak S_m)^p\rtimes\operatorname{AGL}_1(\mathbb F_p)\bigr).
\]
As an arithmetic corollary, the canonical finite étale spread-out of \(S_{p,m}\) over \(\mathbb Z[1/p]\), obtained from the cyclotomic rings of integers, has \(A_{p,m}\) points over \(\mathbb F_{\ell^r}\) if \(\operatorname{ord}_p(\ell)\mid r\), and zero otherwise, for any prime \(\ell\ne p\). This is a statement about the spread-out of the characteristic-zero singular scheme, **not** a claim that it exhausts the singularities of the hypersurface after every characteristic-\(\ell\) reduction.

## Assumptions and scope
All geometry and singular schemes in the theorem are over \(\mathbb Q\) or its algebraic closure, hence characteristic zero. The integer \(N\ge5\) excludes the exceptional zero-dimensional situation at \(N=p=3\). A geometric ordinary double point means a hypersurface singularity whose quadratic tangent cone is nondegenerate. The finite étale spread-out is the disjoint union of copies of \(\operatorname{Spec}\mathbb Z[\zeta_p,1/p]\); it is not asserted to equal the entire relative singular scheme of the integral hypersurface model.

## Proof
**1. Exhaustive singular-point equation.** Let \(H\) denote \(\sum_i x_i=0\) and let \(F=\sum_i x_i^{p+1}\). Since \(p+1\ne0\) in characteristic zero, the Jacobian rank drops at a projective point precisely when
\[
x_1^p=x_2^p=\cdots=x_N^p=\lambda.
\]
If \(\lambda=0\), all coordinates vanish, impossible in projective space. After scaling, every coordinate is a \(p\)-th root of unity. Conversely, any such tuple satisfying \(\sum_i x_i=0\) is on \(F=0\), because \(x_i^{p+1}=x_i\), and satisfies the Jacobian equations. Thus this gives *all* singular points.

**2. Cyclotomic balance.** Fix a primitive \(p\)-th root \(\zeta_p\). Let \(n_j\) count occurrences of \(\zeta_p^j\), for \(0\le j<p\). The relation \(\sum_j n_j\zeta_p^j=0\) says the integral polynomial \(\sum_jn_jT^j\), of degree at most \(p-1\), is divisible over \(\mathbb Q\) by the minimal polynomial \(\Phi_p(T)=1+T+\cdots+T^{p-1}\). It follows that all \(n_j\) are equal to some \(m\), so \(N=pm\). Conversely, all balanced tuples satisfy the relation. There are \((pm)!/(m!)^p\) ordered balanced tuples. Multiplication by the common \(p\)-th root acts freely and gives projective equivalence, so the geometric node count is \(A_{p,m}\).

**3. Nondegenerate quadratic tangent cone.** At any singular point choose the affine chart \(x_N=1\). Eliminate \(x_{N-1}=w=-1-\sum_{i=1}^{N-2}y_i\) and set \(y_i=x_i\). The affine defining equation is \(f=1+\sum_{i=1}^{N-2}y_i^{p+1}+w^{p+1}\). Write \(c=p(p+1)\). At the node, each \(y_i,w\) is a \(p\)-th root of unity, and its Hessian is
\[
\left(\frac{\partial^2 f}{\partial y_i\partial y_j}\right)
=c\bigl(\operatorname{diag}(y_1^{-1},\ldots,y_{N-2}^{-1})+w^{-1}{\bf1}{\bf1}^{\mathsf T}\bigr).
\]
By the matrix determinant lemma and \(\sum_{i=1}^{N-2}y_i=-1-w\), its determinant equals
\[
-c^{N-2}\,w^{-1}\prod_{i=1}^{N-2}y_i^{-1}\ne0.
\]
So every singularity is an ordinary double point. In particular, the local Jacobian ideal is the maximal ideal (Jacobian linearization invertible), and the entire finite singular scheme is geometrically reduced.

**4. Geometric integrality and normality.** The polynomial \(F|_H\) is not identically zero: at \((1,-1,0,\ldots,0)\) it has value \(2\), since \(p+1\) is even. Its singular locus is finite by steps 1–3. If the hypersurface were reducible over an algebraic closure, distinct positive-degree factors would meet in dimension at least \(N-4\ge1\) inside \(H\cong\mathbb P^{N-2}\), giving a positive-dimensional singular locus. A repeated factor similarly forces positive-dimensional singular support. Thus the hypersurface is geometrically integral. Being a hypersurface, it satisfies \(S_2\); its isolated singularities in dimension \(N-3\ge2\) give \(R_1\). Serre's criterion proves normality. The argument also covers the smooth case.

**5. Exact residue fields and orbit spaces.** Every balanced configuration uses all \(p\) roots. Ratios of its nonzero homogeneous coordinates therefore generate \(\mathbb Q(\zeta_p)\), and the point is defined over that same field. Hence its residue field is exactly \(\mathbb Q(\zeta_p)\) of degree \(p-1\). The finite reduced singular scheme is therefore a disjoint union of \(B_{p,m}=A_{p,m}/(p-1)\) copies of \(\operatorname{Spec}\mathbb Q(\zeta_p)\). Labeling the \(p\) equal-sized coordinate blocks by \(\mathbb F_p\) gives all geometric tuples. Common multiplication by \(\zeta_p\) translates the labels; Galois automorphisms \(\zeta_p\mapsto\zeta_p^a\) multiply labels by \(a\in\mathbb F_p^\times\). Permuting coordinates is transitive. The two stabilizers are therefore the stated block-permutation semidirect products with \(C_p\) and \(\operatorname{AGL}_1(\mathbb F_p)\).

**6. Frobenius splitting of the finite étale model.** For \(\ell\ne p\), the residue degree of \(\ell\) in \(\mathbb Q(\zeta_p)\) is \(f=\operatorname{ord}_p(\ell)\). Each cyclotomic factor gives \((p-1)/f\) factors of degree \(f\) over \(\mathbb F_\ell\). Each contributes \(f\) maps to \(\mathbb F_{\ell^r}\) when \(f\mid r\), and none otherwise. Multiplying by \(B_{p,m}\) gives the claimed count.

## Verification
The standalone standard-library-plus-SymPy script `check_nodes.py` independently enumerates balanced root words and their translation/Galois orbits for \((p,m)=(3,2)\) and \((5,1)\), and verifies the affine Hessian determinant identity by exact reduction modulo \(\Phi_p\). It yields respectively \((30,15)\) and \((24,6)\) for (geometric nodes, closed points), and prints `VERIFY_OK`. The symbolic proof, rather than these finite computations, establishes the general theorem. Formula-only examples include \((p,m)=(5,2)\), with \(22680\) geometric nodes and \(5670\) closed points, and \((7,1)\), with \(720\) and \(120\).

## Relationship to prior work
Lam and Leung's characteristic-zero cyclotomic relation theorem supplies the underlying classification of vanishing sums of prime-order roots of unity (the prime case follows already from the minimal polynomial). The present geometric statement does not re-claim that root-sum result: it identifies the singular scheme of a concrete projective hypersurface, proves nodality, computes all residue fields, and gives its symmetric- and Galois-equivariant structure. Cafure, Matera and Privitelli investigate different symmetric hypersurface families over finite fields using elementary symmetric functions; their main singular-locus bounds do not directly assert these formulas. Catanese and Tonoli classify even sets of nodes on sextic surfaces, which is relevant to the first surface case \((p,N)=(5,5)\), but their inspected results neither specify this diagonal hypersurface's cyclotomic Galois scheme nor an all-prime theorem.

## Limitations
The theorem does not calculate the topology or Picard groups of the resulting hypersurfaces. The finite étale spread-out is not identified with the singular scheme of every positive-characteristic fiber; extra or non-ordinary singularities may appear upon reduction. The uniqueness of this exact geometric-and-arithmetic formulation in all literature has not been independently established; prior root-of-unity and symmetric-hypersurface frameworks substantially overlap in ingredients.

## References
- T. Y. Lam and K. H. Leung, *On vanishing sums for roots of unity*, arXiv:math/9511209v1 (13 November 1995), especially Section 2, Theorem 2.2, and the introduction. https://arxiv.org/abs/math/9511209
- A. Cafure, G. Matera and M. Privitelli, *Singularities of symmetric hypersurfaces and an application to Reed-Solomon codes*, arXiv:1109.2265v1 (10 September 2011), Sections 1–2. https://arxiv.org/abs/1109.2265
- F. Catanese and F. Tonoli, *Even sets of nodes on sextic surfaces*, J. Eur. Math. Soc. 9 (2007), 705–737, Sections 1–2. https://doi.org/10.4171/JEMS/94
