# The singular rational normal curve and transverse \(A\)-type of odd binary-form quadratic hulls

## Finding
For every odd integer \(r\ge 7\), put \(p=(r-3)/2\), let \(V=\operatorname{Sym}^{r}\mathbb C^2\), and let \(C_r=\{[\ell^r]:0\ne\ell\in\mathbb C^2\}\subset\mathbb P V\) be its rational normal curve. Let \(X_r\subset\mathbb P V\) be the *scheme* cut out by the three coefficients of the transvectant \((f,f)_{r-1}\). Equivalently, \(X_r\) is the quadratic hull of the \(p\)-osculating variety of \(C_r\).

Then \(X_r\) is an integral complete intersection of three quadrics, and its **reduced singular locus** is exactly \(C_r\). At *every* point of \(C_r\), the completed local analytic germ is a smooth one-dimensional factor times a suspended simple singularity of type \(A_{(r-1)/2}\). Explicitly, there are completed local coordinates in which
\[
\widehat{\mathcal O}_{X_r,[\ell^r]}\cong
\mathbb C[[s,t,z_1,\ldots,z_{r-4}]]/
\left(z_1^2+\cdots+z_{r-4}^2+t^{(r+1)/2}\right).
\]
The transverse Milnor and Tjurina numbers are both \((r-1)/2\). This states a local analytic classification, not an assertion about the nonreduced Jacobian singular scheme.

## Assumptions and scope
Work over \(\mathbb C\) and assume \(r\) is odd and \(r\ge7\). The subscheme \(X_r\) is defined by its homogeneous ideal of **three** specified quadrics, not merely by a set-theoretic vanishing condition. The terminology \(A_k\) refers to a quadratic suspension of the hypersurface germ \(u^2+v^{k+1}=0\). All local isomorphisms are completed/complex analytic; no assertion is made in positive characteristic.

For \(r=2p+3\), Massri's complete-intersection theorem applies with \(N=\binom{r-2p-1}{2}=1\) and \(p>1\). It gives an integral codimension-three complete intersection, hence its scheme-theoretic singular locus has support determined by Jacobian rank.

## Proof
**1. Moment-map Jacobian and its exact rank-drop set.** Because \(r\) is odd, \(V\) has a nondegenerate \(SL_2\)-invariant alternating form \(\Omega\). The quadratic map
\[
\mu:V\longrightarrow\mathfrak{sl}_2^*,\qquad
\mu(f)(A)=\tfrac12\Omega(Af,f)
\]
is \(SL_2\)-equivariant and nonzero. The multiplicity-one decomposition of \(\operatorname{Sym}^2(V)\) shows that its three coordinate quadrics span exactly the coefficients of \((f,f)_{r-1}\), up to an invertible change of target basis. Its differential is
\[
(d\mu)_f(v)(A)=\Omega(Af,v).
\]
By nondegeneracy of \(\Omega\), \((d\mu)_f\) fails to have rank three exactly when some nonzero \(A\in\mathfrak{sl}_2\) satisfies \(Af=0\). Every nonzero \(A\) is either semisimple or nilpotent. A nonzero semisimple element has **no** zero weight on \(\operatorname{Sym}^r\mathbb C^2\), since its weights are the odd integers \(r,r-2,\ldots,-r\). A nonzero nilpotent element has a one-dimensional kernel on \(V\), spanned by the \(r\)-th power of its highest-weight linear form. Consequently the rank drops precisely on the affine cone over \(C_r\) (away from the origin). Pure powers lie in \(\mu^{-1}(0)\). Since \(X_r\) is a codimension-three complete intersection, the Jacobian criterion proves \(\operatorname{Sing}(X_r)_{\mathrm{red}}=C_r\).

**2. A transverse slice and its equation.** By transitivity, work at \([x^r]\). Use Massri's binomial coordinates \(f=\sum_{i=0}^{r} \binom ri a_i x^{r-i}y^i\), set \(a_0=1\), and take the local slice \(a_1=0\), transverse to the smooth curve \(C_r\). Denote the transvectant's three antidiagonal equations in consecutive weights by \(q_0,q_1,q_2\). With their harmless common scalar normalization,
\[
q_0=2a_{r-1}+P_0,\qquad
P_0=\sum_{i=2}^{r-3}(-1)^i\binom{r-1}{i}a_i a_{r-1-i},
\]
while \(q_1\) is linear in \(a_r\) with coefficient \(2\). Solve these two equations for \(a_{r-1},a_r\). The remaining third equation is the following *exact* polynomial in \(t=a_2\) and \(u=(a_3,\ldots,a_{r-2})\):
\[
F_r(t,u)=(r-1)tP_0+
\sum_{i=3}^{r-2}(-1)^{i+1}\binom{r-1}{i-1}a_i a_{r+1-i}=0.
\]
This formula follows directly from the coefficient formula for the transvectant and substitution \(a_{r-1}=-P_0/2\). Every monomial of \(F_r\) has weighted degree \(r+1\) when \(a_i\) receives weight \(i\). Furthermore \(F_r\) has ordinary polynomial degree at most two in the variables \(u\).

**3. Nondegenerate transverse quadratic block.** At \(t=0\), the quadratic part of \(F_r\) in \(u\) is the displayed antidiagonal quadratic form. For each \(i\) with \(3\le i\le r-2\), the coefficient \((-1)^{i+1}\binom{r-1}{i-1}\) is nonzero. Its Hessian is an invertible antidiagonal matrix of size \(r-4\). Write
\[
F_r(t,u)=\tfrac12 u^{\mathsf T}H(t)u+b(t)^{\mathsf T}u+c_0(t),\qquad\det H(0)\ne0.
\]
The analytic change \(u'=u+H(t)^{-1}b(t)\) completes the square; an analytic linear change in \(u'\) makes its nonsingular quadratic form \(\sum z_j^2\). Because the equation and the stationary section both respect the positive weights, the residual one-variable function is *exactly* \(c\,t^{(r+1)/2}\), for a constant \(c\). (In particular, no higher-order residual powers are possible.)

**4. The residual coefficient cannot vanish.** If \(c=0\), the stationary section \(u=-H(t)^{-1}b(t)\) for all sufficiently small \(t\) would consist entirely of singular points of the transverse hypersurface. For \(t\ne0\), these points do not belong to \(C_r\), because the chosen slice meets \(C_r\) only at its origin. This contradicts the rank calculation in Step 1. Therefore \(c\ne0\). A complex rescaling of \(t\) gives the asserted suspended \(A_{(r-1)/2}\) form. The local \(SL_2\) action gives a smooth curve-coordinate factor, and transitivity makes this type uniform along \(C_r\). The Jacobian algebra of the transverse normal form has basis \(1,t,\ldots,t^{(r-3)/2}\), so its Milnor and Tjurina numbers are \((r-1)/2\). \(\square\)

## Verification
The standalone program `verify_moment.py` uses integer binomial coefficients and exact rational Gaussian elimination to reconstruct \(F_r\), check the full transverse Hessian rank, and compute the nonzero stationary coefficients for \(r=7,9,11,13,15,17,19\). For the first three degrees, the coefficients in the normalization of Step 2 are respectively \(405\), \(8960\), and \(984375/4\). These finite computations illustrate, but do not replace, the arbitrary-degree proof, whose critical steps are the moment-map differential and the nonvanishing argument.

## Relationship to prior work
C. Massri's *Quadratic hulls of osculating varieties of rational normal curves* (2026), Theorem 1.1, proves integrality and the three-quadric complete-intersection description in this range, and its local analysis studies the tangent cone. The present finding uses these results as premises but identifies the exact global singular support and the transverse analytic \(A\)-type for **all** odd degrees in the strict range. Massri's *Quadratic equations of projective PGL2(C)-varieties* (2013), Theorem 12, already proves the codimension-three degree-eight assertion and notes that the rational normal curve consists of singular points; it does not there prove equality of the singular support or classify the transverse local germ. The general cotangent-lift moment-shell results of Herbig–Schwarz–Seaton involve a different representation construction and do not supply this explicit analytic classification.

## Limitations
No claim is made for even \(r\), fields other than \(\mathbb C\), or the case \(r=3\). The result concerns the completed/complex analytic local type, not a global product decomposition, a resolution, or the embedded scheme structure of the Jacobian locus. The local isolated hypersurface singularity in a transverse slice is a suspension of an ADE form; it does not assert the global singular locus consists of isolated points. Earlier literature might contain an equivalent classification under Hamiltonian-reduction terminology; this is a residual originality risk, not a proof of uniqueness.

## References
1. C. Massri, *Quadratic hulls of osculating varieties of rational normal curves*, arXiv:2610.28499v1 (first posted 2026-10-20), especially Theorem 1.1 and Sections 2–6. https://arxiv.org/abs/2610.28499
2. C. Massri, *Quadratic equations of projective PGL2(C)-varieties*, arXiv:1105.0724v3 (2013), especially Theorem 12. https://arxiv.org/abs/1105.0724
3. H.-C. Herbig, G. W. Schwarz and C. Seaton, *When does the zero fiber of the moment map have rational singularities?*, arXiv:2108.07306 (2021; later journal edition); cotangent-lift setting. https://arxiv.org/abs/2108.07306
