# Interior full-fiber saturation and two-point rigidity for finite Blaschke Schwarz–Pick matrices

## Finding

Let \(B:\mathbb D\to\mathbb D\) be any finite Blaschke product of degree \(d\ge1\), and let \(w\in\mathbb D\) be a regular value of \(B\). List the \(d\) distinct points of the full fiber as \(Z=(z_1,\ldots,z_d)\), so \(B(z_j)=w\). Define the positive definite Bergman Gram matrix and its derivative counterpart by
\[
G=\left[\frac{1}{(1-z_i\overline{z_j})^2}\right]_{i,j=1}^d,\qquad
H=\left[\frac{B'(z_i)\overline{B'(z_j)}}{(1-B(z_i)\overline{B(z_j)})^2}\right]_{i,j=1}^d.
\]
Then, with \(v=(B'(z_1),\ldots,B'(z_d))^{\mathsf T}\),
\[
\boxed{v^*G^{-1}v=d(1-|w|^2)^2.}
\]
Consequently the generalized eigenvalue matrix \(G^{-1/2}HG^{-1/2}\) has spectrum \(\{d,0,\ldots,0\}\), counting multiplicity. The sharp degree-\(d\) finite-point Schwarz–Pick bound \(H\preceq dG\) is **attained at every interior regular full fiber** of every finite Blaschke product. Its maximizing coefficient vector is unique up to nonzero scalar and is \(c=G^{-1}v\).

There is a complete two-point rigidity result at the first nontrivial degree. If \(d=2\) and \(z_1\ne z_2\) are arbitrary interior points, then
\[
\boxed{\det(2G_Z-H_{B,Z})=0\quad\Longleftrightarrow\quad B(z_1)=B(z_2).}
\]
Equivalently, equality \(c^*H_{B,Z}c=2c^*G_Zc\) holds for some nonzero vector \(c\) **if and only if** the two distinct points form a regular full fiber. Otherwise \(2G_Z-H_{B,Z}\) is positive definite.

## Assumptions and scope

Here \(\mathbb D=\{z\in\mathbb C:|z|<1\}\), and \(A^2(\mathbb D)\) is the analytic Bergman space with normalized area measure \(dA=\pi^{-1}\,dx\,dy\). Its reproducing kernel at \(a\) is \(k_a(z)=(1-\overline a z)^{-2}\). A regular value means \(B'(z)\ne0\) at all points satisfying \(B(z)=w\); finite properness supplies exactly \(d\) such points. The order of a fiber does not matter. The sharp matrix inequality \(H_{B,Z}\preceq\min\{d,n\}G_Z\) for arbitrary \(n\)-tuples is an input from Tian (2026), not claimed here as new. The new assertions concern *exact interior saturation* and the *degree-two equality locus*.

## Proof

**1. Exact full-fiber identity.** Fix a regular value \(w\), and form the disk automorphism \(\phi_w(\zeta)=(\zeta-w)/(1-\overline w\zeta)\) and \(C=\phi_w\circ B\). Then \(C\) is a degree-\(d\) finite Blaschke product with simple zeros precisely at \(z_1,\ldots,z_d\). Its derivative at each zero is
\[
C'(z_j)=\frac{B'(z_j)}{1-|w|^2}.
\]
We show that \(C'\) lies in \(E=\operatorname{span}\{k_{z_1},\ldots,k_{z_d}\}\). Indeed, up to a unimodular factor,
\[
C(z)=\prod_{j=1}^d\frac{z-z_j}{1-\overline{z_j}z}.
\]
If no \(z_j\) is zero, the numerator and denominator have equal degree. Their rational partial-fraction decomposition is a constant plus terms \(A_j/(1-\overline{z_j}z)\), and differentiation gives a linear combination of \((1-\overline{z_j}z)^{-2}\). If one \(z_j=0\), the degree difference is one, the polynomial part is at most linear, and its derivative is a constant, namely a multiple of \(k_0\). Distinctness of the zeros ensures no repeated pole. Thus \(C'\in E\) in both cases.

The vectors \(k_{z_j}\) are linearly independent because their Bergman Gram matrix is strictly positive definite at distinct points. The norm of the unique interpolant \(f\in E\) with values \(f(z_j)=u_j\) is \(\|f\|_{A^2}^2=u^*G^{-1}u\). Apply this with \(f=C'\) and \(u=v/(1-|w|^2)\). The holomorphic change-of-area formula for a proper degree-\(d\) map now gives
\[
\|C'\|_{A^2}^2=\int_{\mathbb D}|C'(z)|^2\,dA(z)
=\int_{\mathbb D}\#C^{-1}(\zeta)\,dA(\zeta)=d.
\]
Consequently \(v^*G^{-1}v=d(1-|w|^2)^2\). On a full fiber, \(H=vv^*/(1-|w|^2)^2\), so \(G^{-1/2}HG^{-1/2}\) is rank one, with its sole nonzero eigenvalue equal to \(d\). Cauchy–Schwarz in the \(G\)-inner product gives the unique maximizing direction \(G^{-1}v\).

**2. Isometric pullback and the equality criterion.** For a finite Blaschke product of degree \(d\), the derivative-weighted composition operator
\[
(U_Bf)(z)=\frac{B'(z)}{\sqrt d}\,f(B(z))
\]
is an isometry on \(A^2(\mathbb D)\), again by the area formula. Its adjoint sends \(k_z\) to \(\overline{B'(z)}k_{B(z)}/\sqrt d\). Hence, on the span \(E_Z=\operatorname{span}\{k_{z_1},k_{z_2}\}\), the inequality \(H_{B,Z}\preceq dG_Z\) is the contractivity of the adjoint of this isometry. Equality for a nonzero coefficient vector is equivalent to a nonzero element of \(E_Z\) lying in the closed range of \(U_B\).

**3. Degree-two normal form.** Every degree-two finite Blaschke product has exactly one critical point in \(\mathbb D\), counted with multiplicity. Compose with a source automorphism sending it to zero and a target automorphism sending its image to zero. The resulting degree-two finite Blaschke product has a double zero at zero and is therefore \(e^{i\theta}z^2\). A final target rotation makes it \(z^2\). Automorphisms preserve Bergman Gram inequalities and their equality loci: the reproducing-kernel covariance
\[
\frac{\alpha'(z)\overline{\alpha'(\zeta)}}{(1-\alpha(z)\overline{\alpha(\zeta)})^2}
=\frac1{(1-z\overline\zeta)^2}
\]
produces invertible diagonal congruences under changes of source coordinates, while target automorphisms leave the derivative Gram form invariant. Thus it suffices to study \(B(z)=z^2\).

For \(B(z)=z^2\), \(U_Bf(z)=\sqrt2 z f(z^2)\), and its closed range is exactly the odd subspace of \(A^2\). For distinct \(z_1,z_2\), a vector \(ak_{z_1}+bk_{z_2}\) can be odd only if its constant coefficient vanishes, so \(a+b=0\). The coefficient of \(z^2\) then vanishes only if \(a(\overline{z_1}^{\,2}-\overline{z_2}^{\,2})=0\). A nonzero vector forces \(z_2=-z_1\); conversely \(k_{z_1}-k_{-z_1}\) is a nonzero odd Bergman function for any nonzero \(z_1\). This is exactly the condition \(B(z_1)=B(z_2)\). Undoing the automorphisms yields the asserted classification for every degree-two Blaschke product. The known semidefinite bound then implies strict positive definiteness off the equality locus, completing the proof.

## Verification

The accompanying standalone `verify.py` checks the inverse-Gram identity by exact rational elimination on five distinct full fibers of degrees one through five; a regular nonzero fiber of the degree-two power map; and the vanishing/nonvanishing of the degree-two defect determinant on four pairs. Run `python3 verify.py` with a standard Python installation. The expected output is `EXACT_FIBER_CHECK_OK zero_fibers=5 nonzero_fibers=1 quadratic_pairs=4`.

These are finite checks and are **not** used as an infinite proof. The general argument uses rational partial fractions, Bergman interpolation, the degree-counted holomorphic area formula, and the range of an isometric weighted composition operator. The normalized area convention gives \(\|z^n\|_{A^2}^2=1/(n+1)\), which fixes all constants.

## Relationship to prior work

Tian (2026), *A finite-Point Schwarz-Pick Inequality*, proves \(H_{f,Z}\preceq nG_Z\) for arbitrary self-maps and \(H_{B,Z}\preceq\min\{n,d\}G_Z\) for degree-\(d\) finite Blaschke products. Its sharpness argument uses \(B(z)=z^d\) and sampling points in one fiber approaching the boundary. Its full proof does not provide the all-regular-fiber inverse-Gram identity for arbitrary finite Blaschke products or characterize all equality pairs for degree two. The sharp *uniform constant* is therefore known; the assertions here classify interior attainment rather than improve that constant.

A published related result, *Sharp range–valence constant for finite-point Schwarz–Pick matrices* (2026), extends the uniform constant to finite-valent maps with a target-radius restriction. Its power-map example achieves the degree bound at every regular power-map fiber. This special case is subsumed here, so it is **not** the novelty claim. What is added is the exact arbitrary finite-Blaschke-fiber identity and the necessary-and-sufficient quadratic equality classification.

Badea and Renard (2024) study operator versions of multipoint Schwarz–Pick estimates formulated through hyperbolic divided differences and model operators, not the stated Bergman derivative-Gram equality locus.

## Limitations

Full-fiber saturation assumes a *regular* interior value. Critical fibers have confluent evaluation phenomena and are not classified here. The off-fiber rigidity theorem is for degree two and two distinct sample points; no general equality classification for higher degrees or arbitrary point counts is claimed. The result uses the already published sharp finite-point inequality rather than reproving its generality. Older unindexed operator-theoretic treatments of composition-isometry equality cases could conceivably contain an equivalent characterization, so originality still merits independent literature verification.

## References

1. James Tian, *A finite-Point Schwarz-Pick Inequality*, arXiv:2608.10443v1, publicly released 11 August 2026, especially Theorem 2.1 and the proof/sharpness discussion. https://arxiv.org/abs/2608.10443
2. *Sharp range–valence constant for finite-point Schwarz–Pick matrices*, 2026, published research record; theorem, proof and comparison: https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-sharp-range-valence-constant-for-finite-point-schwarz-pick-matri--9c5e4b893dca
3. Cătălin Badea and Axel Renard, *Schwarz-Pick type inequalities from an operator theoretical point of view*, Journal of Mathematical Analysis and Applications 540 (2024), 128578, arXiv:2405.01357v2. https://arxiv.org/abs/2405.01357
