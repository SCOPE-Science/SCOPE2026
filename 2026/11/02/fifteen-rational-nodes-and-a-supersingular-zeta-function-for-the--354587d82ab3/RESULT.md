# Fifteen rational nodes and a supersingular zeta function for the characteristic-three Clebsch Hessian

## Finding
Let \(k=\mathbb F_3\) and let \(e_j\) denote the degree-\(j\) elementary symmetric polynomial in five variables \(X_0,\ldots,X_4\). Inside the hyperplane \(e_1=0\cong\mathbb P^3_k\), consider the smooth cubic \(S:e_3=0\) and its quartic Hessian \(H:e_4=0\). The characteristic-three Hessian determinant of the dehomogenized four-variable cubic is exactly \(e_4\), not merely proportional to it.

**Theorem.** The geometric singular locus of \(H\) consists of precisely fifteen ordinary double points, all rational over \(k\): the ten permutations of \([1:-1:0:0:0]\) and the five permutations of \([1:-1:-1:-1:-1]\). The minimal resolution \(\pi:\widetilde H\to H\) is a K3 surface. For every integer \(m\ge1\),
\[
\#\widetilde H(\mathbb F_{3^m})=3^{2m}+1+3^m\bigl(21+(-1)^m\bigr).
\]
Consequently,
\[
Z(\widetilde H/\mathbb F_3,T)=\frac{1}{(1-T)(1-9T)(1-3T)^{21}(1+3T)}.
\]
The surface is supersingular (all degree-two Frobenius slopes are one). By the Tate theorem for K3 surfaces in odd characteristic, its geometric Picard rank is \(22\), its Picard rank over \(\mathbb F_3\) is \(21\), and all geometric divisor classes descend over \(\mathbb F_9\) up to finite index.

## Assumptions and scope
All geometric statements are over an algebraic closure of \(\mathbb F_3\); all arithmetic point counts and zeta factors concern the specified \(\mathbb F_3\)-model. The cubic uses the **elementary-symmetric integral model** \(e_3=0\). In characteristic three the naive reduction of the classical power-sum equation \(\sum X_i^3=0\), subject to \(e_1=0\), is identically satisfied and does **not** define the smooth cubic used here. Over characteristic zero, \(\sum X_i^3=3e_3\) on \(e_1=0\), which explains the relation with the Clebsch cubic.

For the Hessian take \(X_4=-X_0-X_1-X_2-X_3\) and the determinant of the ordinary \(4\times4\) second-derivative matrix of \(e_3\). The extension field \(\mathbb F_9\) in the point count is represented by \(\mathbb F_3[\theta]/(\theta^2+1)\).

## Proof
**1. Smooth cubic and Hessian identity.** On the hyperplane \(e_1=0\),
\[
\frac{\partial e_3}{\partial X_i}=e_2+X_i^2.
\]
If the cubic were singular, all five squares \(X_i^2\) would agree. Since \(\sum X_i=0\), a nonzero vector with that property has one sign different from the other four, up to simultaneous scalar and permutation; for either sign choice, \(e_3\ne0\). Therefore \(S\) is smooth. Direct expansion in the four independent coordinates gives the polynomial identity
\[
\det\left(\frac{\partial^2 e_3}{\partial X_i\partial X_j}\right)_{0\le i,j\le3}=e_4\quad\text{in }\mathbb F_3[X_0,X_1,X_2,X_3],
\]
where the elementary symmetric functions are evaluated at the five coordinates with \(X_4\) eliminated. This identity is checked coefficient by coefficient in the accompanying verifier.

**2. Complete geometric singular locus.** The gradient components of \(e_4\) on \(e_1=0\) are
\[
\frac{\partial e_4}{\partial X_i}=e_3-e_2X_i-X_i^3.
\]
Thus the Jacobian criterion for the hyperplane section says that every coordinate of a singular point satisfies one common cubic equation \(X_i^3+e_2X_i=c\). On \(e_1=0\), Newton's identity gives \(e_2=\sum X_i^2\). If \(e_2=0\), the cubic equation forces all coordinates equal; their sum then forces all to vanish, an impossibility. Otherwise choose \(u\) in the algebraic closure with \(u^2=-e_2\) and set \(Y_i=X_i/u\). Then each \(Y_i^3-Y_i\) is the same constant. Since the roots of \(Y^3-Y=d\) form a translate of \(\mathbb F_3\), write \(Y_i=r+\epsilon_i\) with \(\epsilon_i\in\mathbb F_3\). The relation \(\sum Y_i=0\) forces \(r=\sum\epsilon_i\in\mathbb F_3\). Therefore all \(Y_i\in\mathbb F_3\), with \(\sum Y_i=0\) and \(\sum Y_i^2=-1\). Exactly two or five coordinates are nonzero, because the number of nonzero \(Y_i\) is congruent to two modulo three. The sum-zero condition leaves exactly the ten sign-pairs and the five one-versus-four sign patterns stated in the theorem. Direct substitution shows that each lies on \(e_4=0\) and has equal ambient gradient components. Hence there are no other geometric singularities.

**3. Local singularity type and K3 resolution.** In the affine chart \(X_0=1\), write \(X_1=a,X_2=b,X_3=c,X_4=-1-a-b-c\). The \(3\times3\) Hessian of the local equation \(e_4\) has determinant \(1\in\mathbb F_3\) at both orbit representatives \((a,b,c)=(-1,0,0)\) and \((-1,-1,-1)\). In characteristic three a nondegenerate quadratic tangent cone gives an ordinary \(A_1\) point. Thus all fifteen points are nodes. As the hypersurface has only isolated singularities, it is geometrically integral: two positive-degree components of a quartic surface in \(\mathbb P^3\) would meet in a curve, necessarily a positive-dimensional singular locus. Its minimal resolution has trivial canonical class and vanishing first cohomology, hence is a K3 surface. Each node is rational and has a split exceptional conic \(\mathbb P^1\) over every finite extension of \(\mathbb F_3\).

**4. Exact point counts.** Enumerate the canonical representatives of projective \(3\)-space over \(\mathbb F_q\): the vectors whose first nonzero coordinate equals one. For each such vector \((X_0,\ldots,X_3)\), set \(X_4=-\sum_{i=0}^3X_i\), compute \(e_4\), and retain its zeros. Exact arithmetic gives
\[
\#H(\mathbb F_3)=25,\qquad \#H(\mathbb F_9)=145.
\]
Replacing each rational node by an exceptional \(\mathbb P^1\) contributes \(q\) additional points. Thus
\[
\#\widetilde H(\mathbb F_3)=70,\qquad \#\widetilde H(\mathbb F_9)=280.
\]
The complete finite enumeration and its field arithmetic are provided in `verify_hessian3.py`; the verified transcript is `verify_hessian3.out`.

**5. Frobenius eigenvalues, zeta, and supersingularity.** A K3 surface has \(22\) second-cohomology Frobenius eigenvalues \(\alpha_i\), each of complex absolute value \(3\). The two point counts give
\[
\sum_{i=1}^{22}\alpha_i=70-1-9=60,\qquad
\sum_{i=1}^{22}\alpha_i^2=280-1-81=198.
\]
Put \(\zeta_i=\alpha_i/3\), so \(|\zeta_i|=1\). Since \(\sum\zeta_i^2=22\), equality in the triangle inequality forces every \(\zeta_i^2=1\). Since \(\sum\zeta_i=20\), precisely \(21\) of the \(\zeta_i\)'s equal \(+1\) and one equals \(-1\). This proves the complete zeta function and the formula for all \(m\). As every normalized eigenvalue is a root of unity and each eigenvalue has \(3\)-adic valuation one, the K3 has all Newton slopes one. The cited Tate theorem identifies the Frobenius-invariant eigenvalue multiplicities with the rational Picard ranks, giving \(21\) over \(\mathbb F_3\) and \(22\) geometrically. The cohomological reasoning, rather than extrapolation of finite counts, establishes all-extension conclusions.

## Verification
Run `python verify_hessian3.py` with `sympy==1.14.0` and the Python standard library. The script checks the Hessian polynomial identity modulo three, both singular orbit representatives' local quadratic Hessians, membership and Jacobian equations for the fifteen explicit nodes, exhaustive \(\mathbb F_3\) and \(\mathbb F_9\) projective point counts, and the resulting Frobenius trace arithmetic. It concludes with `VERIFY_OK`. The completeness of geometric singularities, the K3 property, and the full zeta deduction are proved above; they do not rest on finite-field enumeration alone.

## Relationship to prior work
Dardanelli and van Geemen [1, Sections 1.4–1.6 and 2.4–2.5] give the classical Sylvester pentahedral Hessian \(e_4=0\), its ten nodes in the characteristic-zero smooth-cubic setting, and the complex Clebsch Hessian K3 lattice of discriminant \(15\). Their pairs of lines use primitive cube roots of unity, which coalesce in characteristic three, so their characteristic-zero node statement does not establish the positive-characteristic result here. The new assertion is the characteristic-three extra five nodes, all rational, and the exact Frobenius/zeta calculation for the resolved arithmetic special fiber. The general Tate theorem used for Picard ranks is [2], not a new assertion. The standard theory of nodal K3 resolutions and the Weil bounds are also background results.

## Limitations
The characteristic-three model is specified by \(e_3\), not by the degenerate mod-three reduction of a power-sum cubic. The point counts are exhaustive only for \(\mathbb F_3\) and \(\mathbb F_9\); the all-extension formula follows rigorously from K3 cohomology and the equality case in the Weil bound. This result does not determine an Artin invariant, an integral Picard basis, or a minimal equation for the simultaneous resolution in mixed characteristic. The novelty comparison is limited to the inspected literature, catalogs and exact indexed search results; it is not a proof of historical priority. No independent scientific audit is asserted.

## References
[1] Elisa Dardanelli and Bert van Geemen, *Hessians and the moduli space of cubic surfaces*, arXiv:math/0409322v1 (first publicly posted 2004-09-18), Sections 1.4–1.6 and 2.4–2.5, https://arxiv.org/abs/math/0409322.

[2] Keerthi Madapusi Pera, *The Tate conjecture for K3 surfaces in odd characteristic*, arXiv:1301.6326v1 (2013-01-27), https://arxiv.org/abs/1301.6326.
