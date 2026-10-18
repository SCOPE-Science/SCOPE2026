# Modular polar collapse and Hessian-rank strata of the generic symmetric determinant

## Finding

Fix an integer \(n\geq3\), an algebraically closed field \(k\) of arbitrary characteristic, and the generic symmetric matrix \(S=(x_{ij})_{1\leq i,j\leq n}\), with independent coordinates \(x_{ij}=x_{ji}\) for \(i\leq j\). Write \(F=\det S\), \(N=n(n+1)/2\), \(m=n(n-1)/2\), \(E=(n+1)(n-2)/2\), and \(H(F)\) for the ordinary \(N\)-by-\(N\) Hessian in these coordinates. The following is a single characteristic-dependent description of the polar map, its base support, and the ranks of its differential.

1. **Integral Hessian identity.** The polynomial identity
   \[
   \det H(F)=(-1)^{n-1+m}(n-1)2^m F^E
   \]
   holds already over \(\mathbb Z\). Thus its Hessian determinant is nonzero precisely if \(\operatorname{char} k\ne2\) and \(\operatorname{char} k\nmid(n-1)\) (with the latter automatic in characteristic zero).

2. **The polar map changes type in characteristic two.** Define \(\Phi_F:\mathbb P^{N-1}\dashrightarrow\mathbb P^{N-1}\) by all ordinary first partial derivatives \(\partial F/\partial x_{ij}\). In characteristic different from two it is, after a linear change in the target coordinates, the classical adjugate Cremona involution. In characteristic two all off-diagonal derivatives vanish identically, while the projective image is the coordinate \(\mathbb P^{n-1}\) indexed by diagonal derivatives. Its reduced base support is
   \[
   \operatorname{Bs}(\Phi_F)_{\mathrm{red}}=
   \begin{cases}
   \{[S]:\operatorname{rank}S\leq n-2\},&n\text{ odd},\\
   \{[S]:\operatorname{rank}S\leq n-2\}\ \cup\ \mathbb P(\operatorname{Alt}_n),&n\text{ even},
   \end{cases}
   \]
   where \(\operatorname{Alt}_n\subseteq\operatorname{Sym}_n(k)\) is the vector space of zero-diagonal symmetric matrices in characteristic two. When \(n\) is even, \(\mathbb P(\operatorname{Alt}_n)\) is an additional irreducible linear component; its open subset of invertible alternating matrices lies **outside** the hypersurface \(F=0\). This extra component does not occur in odd size.

3. **Complete Hessian-rank classification at geometric points.** Put \(r=\operatorname{rank}S\). In odd characteristic, or characteristic zero, the Hessian ranks for \(r=n,n-1,n-2,r\leq n-3\) are respectively
   \[
   \begin{cases}N,&r=n,\ \operatorname{char}k\nmid(n-1),\\
   N-1,&r=n,\ \operatorname{char}k\mid(n-1),\\
   n+1,&r=n-1,\\
   3,&r=n-2,\\
   0,&r\leq n-3.
   \end{cases}
   \]
   In characteristic two, the corresponding ranks are
   \[
   \begin{cases}n,&r=n,\ n\text{ even},\\
   n-1,&r=n,\ n\text{ odd},\\
   0,&r=n-1\text{ and the induced nondegenerate form on }k^n/\ker S\text{ is alternating},\\
   2,&r=n-1\text{ and that form is nonalternating},\\
   2,&r=n-2,\\
   0,&r\leq n-3.
   \end{cases}
   \]
   The exceptional alternating corank-one case can only arise when \(n\) is odd. In odd positive characteristic dividing \(n-1\), the Hessian determinant vanishes identically although the polar map remains a birational Cremona transformation. All ranks refer to the **ordinary** Hessian, not divided-power or Hasse derivatives.

## Assumptions and scope

We work with **independent upper-triangular entries**, not with \(n^2\) independent generic-matrix variables. In characteristic two, \(\operatorname{Alt}_n\) means the symmetric matrices whose diagonal entries are zero, equivalently the alternating bilinear forms. The base locus assertion concerns the **reduced support** of the homogeneous gradient ideal; its embedded and nilpotent structure is not asserted. The rank classification concerns each geometric matrix over the algebraically closed field; the same polynomial identities hold after arbitrary base change. In statements of divisibility, \(\operatorname{char}k=0\) never divides a positive integer.

## Proof

**Step 1 (Hessian identity over the integers).** Let \(T_g:\operatorname{Sym}_n\to\operatorname{Sym}_n\) be the linear congruence action \(A\mapsto g^TAg\). Its determinant on the \(N\)-dimensional coefficient space is \((\det g)^{n+1}\), as follows for diagonal \(g\) by multiplying the weights \(g_ig_j\) with \(i\leq j\), and then for arbitrary \(g\) by polynomial density. The determinant satisfies \(F(T_g A)=(\det g)^2F(A)\). By differentiating twice, and taking determinants,
\[
\det H(F)(T_g A)=(\det g)^{2N-2(n+1)}\det H(F)(A)
=(\det g)^{(n+1)(n-2)}\det H(F)(A).
\]
Over a characteristic-zero algebraically closed field every invertible symmetric matrix is congruent to \(I_n\). Since \(2E=(n+1)(n-2)\), the quotient \(\det H(F)/F^E\) is constant on the dense open set of invertible symmetric matrices, hence the polynomial identity holds. At \(I_n\), the diagonal-coordinate Hessian block is \(J_n-I_n\); the off-diagonal-coordinate block is \(-2I_m\), with mixed entries zero. Its determinant is \((-1)^{n-1}(n-1)(-2)^m\). This proves the claimed coefficient over \(\mathbb Q\), and equality of the two integer-coefficient polynomials over \(\mathbb Q\) proves equality over \(\mathbb Z\), with no division by \(2\) required upon subsequent reduction.

**Step 2 (polar map and base support).** Differentiation with respect to a diagonal entry yields \(\operatorname{adj}(S)_{ii}\); with respect to an off-diagonal independent entry it yields \(2\operatorname{adj}(S)_{ij}\). If \(2\) is invertible, the gradient vector is a linear coordinate transform of the symmetric adjugate. The identity \(\operatorname{adj}(\operatorname{adj}S)=F^{n-2}S\) proves that projective adjugation is birational and involutive on its domain. In characteristic two the off-diagonal gradients vanish; the nonzero diagonal gradients are principal \((n-1)\)-minors. Restricting to diagonal invertible matrices gives
\[
(a_1,\ldots,a_n)\longmapsto\bigl(\prod_{j\ne1}a_j,\ldots,\prod_{j\ne n}a_j\bigr),
\]
which projectively is the coordinatewise inverse on a dense torus. Hence the image closure equals the entire coordinate target \(\mathbb P^{n-1}\).

If \(\operatorname{rank}S\leq n-2\), every \((n-1)\)-minor vanishes, so every diagonal gradient vanishes. If \(\operatorname{rank}S=n-1\), the adjugate is a nonzero rank-one symmetric matrix, necessarily \(c vv^T\) for a nonzero vector \(v\). Some \(v_i\ne0\), hence some diagonal entry \(cv_i^2\ne0\), and this rank stratum is never a base point. If \(S\) is invertible, its diagonal gradients all vanish precisely when the diagonal entries of \(S^{-1}\) vanish, i.e. when \(S^{-1}\) is alternating. For an invertible symmetric matrix in characteristic two, the inverse is alternating exactly when the original form is alternating: one direction follows since the inverse of an alternating nondegenerate form is alternating, and conversely apply this to the inverse. A nondegenerate alternating form exists only in even dimension. For even \(n\), the invertible alternating matrices form a dense open subset of the linear space \(\operatorname{Alt}_n\) (for example a direct sum of \(2\)-by-\(2\) hyperbolic blocks). Its projective closure is an extra irreducible component not contained in the rank-at-most-\(n-2\) locus. This gives the base support exactly.

**Step 3 (Hessian ranks on the smooth full-rank orbit).** A congruence transformation acts on the Hessian by an invertible congruence up to a nonzero scalar, so rank is constant on each isometry class. In characteristic different from two all nonsingular symmetric bilinear forms over the algebraic closure are congruent to \(I_n\), where the Hessian blocks computed in Step 1 give rank \(N\) unless the field characteristic divides \(n-1\), when the rank drops by one. In characteristic two every nondegenerate nonalternating symmetric form is congruent to \(I_n\), while the other possibility, available only in even dimension, is the alternating direct sum of \(n/2\) hyperbolic blocks \(\begin{pmatrix}0&1\\1&0\end{pmatrix}\). To see the nonalternating classification directly, split off a nonisotropic one-dimensional summand (rescale its norm to one, possible over an algebraically closed field) and repeat; if the nonsingular perpendicular remainder is alternating, decompose it into hyperbolic planes. Each form \(\langle1\rangle\oplus H\) is isometric to \(\langle1,1,1\rangle\): for a norm-one vector \(e\) and a hyperbolic pair \(a,b\) with \(B(a,b)=1\), the three vectors \(e+a,e+b,e+a+b\) form an orthonormal basis in characteristic two. This converts each remaining hyperbolic plane into diagonal norm-one directions. All off-diagonal-variable first derivatives vanish identically in characteristic two, so the Hessian is supported on the \(n\) diagonal-coordinate directions. At \(I_n\) its diagonal block is \(J_n-I_n\), of rank \(n\) for even \(n\) and \(n-1\) for odd \(n\). At the alternating block diagonal matrix, the determinant after diagonal perturbation is \(\prod_{j=1}^{n/2}(1+t_{2j-1}t_{2j})\); its diagonal-coordinate Hessian is an invertible direct sum of \(2\)-by-\(2\) exchange blocks, rank \(n\). Thus the formula covers both full-rank types.

**Step 4 (singular-rank strata).** Given a symmetric \(S\) of rank \(r=n-c\), choose a basis in which \(S=\operatorname{diag}(B,0_c)\) with \(B\) nonsingular and symmetric. Its determinant has vanishing order exactly \(c\) in the matrix-entry coordinates transverse to the rank stratum. For \(c\ge3\), all second derivatives vanish. If \(c=2\), its degree-two Taylor term is \((\det B)(uv-w^2)\) in the three entries of the lower-right symmetric \(2\)-by-\(2\) block; the quadratic Hessian has rank \(3\) if \(2\) is invertible and rank \(2\) if characteristic two. For \(c=1\), write the perturbed matrix by blocks as \(\begin{pmatrix}B+U&b\\b^T&z\end{pmatrix}\). The determinant has second-order Taylor terms
\[
 z\bigl(\det B+\operatorname{tr}(\operatorname{adj}(B)U)\bigr)-b^T\operatorname{adj}(B)b.
\]
There is an invertible \((n-1)\)-by-\((n-1)\) Hessian block \(-2\operatorname{adj}(B)\) in the \(b\)-directions when \(2\) is invertible, plus a rank-two \(z\)-versus-\(U\) block because the determinant differential at \(B\) is nonzero. Therefore the rank is \(n+1\). In characteristic two the \(b\)-Hessian vanishes and only the rank-two \(z\)-versus-\(U\) block can remain. It is nonzero exactly when the diagonal-cofactor vector of \(B\) is nonzero, i.e. when \(B^{-1}\) is nonalternating. If \(B\) is alternating, all second derivatives vanish; otherwise the rank is \(2\). This proves every case.

## Verification

With SymPy 1.14.0 as declared in `verification/requirements.txt`, the bundled `verification/check_hessian.py` constructs the full generic symmetric determinant and ordinary Hessian over the integers for \(n=3,4\) using exact symbolic arithmetic. It verifies the entire polynomial Hessian identity at \(n=3\), evaluates the identity at independent integer matrices for \(n=4\), computes predicted Hessian ranks at selected symmetric forms modulo primes \(2,3,5,7\), verifies characteristic-two vanishing of off-diagonal gradient polynomials, and checks the characteristic-two invertible alternating base point and corank-one alternating Hessian degeneration. Run `python3 verification/check_hessian.py` and `cd verification && python3 random_checks.py`. The second script checks every symmetric \(3\)-by-\(3\) binary matrix and 150 reproducibly sampled symmetric \(4\)-by-\(4\) binary matrices for the claimed base and Hessian rank classification. Their expected end markers are `VERIFY_OK` and `FINITE_SPOTS_OK`. These are **finite diagnostics** and do not replace the all-size proofs of Steps 1–4.

## Relationship to prior work

The classical adjugate Cremona transformation and nonmodular symmetric-determinant Hessian phenomenon are existing results, not claimed here as new. Ciliberto–Russo–Simis study polar maps and vanishing Hessians in characteristic zero; their hypotheses do not establish modular rank strata. Grenet–Monteil–Thomassé identify the characteristic-two involution expansion of symmetric determinants (a starting point for the off-diagonal derivative vanishing), but do not give the polar base-support decomposition or global Hessian-rank stratification. Cunha–Ramos–Simis study characteristic-zero symmetry-preserving degenerations of the generic symmetric matrix; the present modular exceptional components are not covered by their assumptions. Xie's 2026 work on symmetric-determinant apolarity in odd positive characteristic concerns differential annihilator ideals and Lefschetz properties rather than the polar base geometry or pointwise Hessian ranks. The contribution is the **combined all-rank, all-characteristic classification**, including the unexpected full-rank alternating base component in even characteristic-two size and the odd-characteristic Hessian-collapse-versus-Cremona dichotomy. An equivalent formulation in other literature remains a residual originality risk.

## Limitations

The polar base locus is determined **only as a reduced support**, not as a nonreduced or primary-decomposed scheme. The field is assumed algebraically closed in the pointwise rank statements and orbit-normal-form proof; the integral polynomial identity and gradient expressions make sense over any field. The result does not claim novelty for the characteristic-zero Hessian factor alone, the classical adjugate involution, or the characteristic-two involution expansion. The bundled examples do not certify arbitrarily large matrix sizes. Literature comparison cannot establish absolute uniqueness.

## References

- C. Ciliberto, F. Russo and A. Simis, *Homaloidal hypersurfaces and hypersurfaces with vanishing Hessian*, arXiv:math/0701596, first posted 2007-01-21, https://arxiv.org/abs/math/0701596.
- B. Grenet, T. Monteil and S. Thomassé, *Symmetric Determinantal Representations in characteristic 2*, arXiv:1210.5879, first posted 2012-10-22, https://arxiv.org/html/1210.5879v2.
- R. Cunha, Z. Ramos and A. Simis, *Symmetry preserving degenerations of the generic symmetric matrix*, arXiv:1802.08067, first posted 2018-02-20, https://arxiv.org/abs/1802.08067.
- Y. Xie, *Symmetric-determinant apolarity in odd characteristic*, arXiv:2609.38212, first posted 2026-09-25, https://arxiv.org/abs/2609.38212.
