# Sharp rank-one section-profile defect of ellipsoids and opposite high-eccentricity limits

## Finding

For a centered three-dimensional ellipsoid \(E_Q\), the *relative least-squares rank-one defect* of its parallel section-area function on all directions and all common interior offsets has a closed formula involving just three angular moments. This defect vanishes exactly for balls. Near a ball, it detects the squared traceless anisotropy with sharp coefficient \(1/24\), but it is not a global measure of eccentricity: a prolate family has a strictly positive limiting defect whereas an equally eccentric oblate family has defect tending to zero.

More precisely, let \(Q\) be any real symmetric positive-definite \(3\times3\) matrix. Set
\[
E_Q=\{x\in\mathbb R^3:x^\mathsf{T}Q^{-1}x\le1\},\qquad
 a=\sqrt{\lambda_{\min}(Q)},\qquad
q(u)=\frac{u^\mathsf{T}Qu}{a^2},\quad u\in S^2.
\]
Write \(A_Q(u,t)\) for the Euclidean area of \(E_Q\cap\{x:u\cdot x=t\}\). Normalize its profile to
\[
F_Q(u,s)=\frac{a}{\pi\sqrt{\det Q}}A_Q(u,as),\qquad -1\le s\le1.
\]
The domain is the largest centered offset interval common to every direction. With normalized spherical area \(d\sigma\) and normalized uniform measure \(ds/2\), define
\[
\mathscr E(Q)=\inf_{\alpha\in L^2(S^2),\ \beta\in L^2([-1,1])}
\frac{\|F_Q-\alpha(u)\beta(s)\|_{L^2(d\sigma\,ds/2)}^2}
{\|F_Q\|_{L^2(d\sigma\,ds/2)}^2}.
\]
Let
\[
m_j=\int_{S^2}q(u)^{-j}\,d\sigma(u)\quad(j=1,2,3),\qquad
S=m_1-\frac23m_2+\frac15m_3,\qquad D=m_1m_3-m_2^2.
\]
Then \(S>0\) and
\[
\boxed{\mathscr E(Q)=\frac12\left(1-\sqrt{1-\frac{16D}{45S^2}}\right).}
\]
In particular, \(\mathscr E(Q)=0\) if and only if \(E_Q\) is a Euclidean ball.

For any fixed real symmetric \(B\), and \(Q_\varepsilon=I+\varepsilon B+O(\varepsilon^2)\) remaining positive definite as \(\varepsilon\to0\),
\[
\boxed{\mathscr E(Q_\varepsilon)=\frac{\varepsilon^2}{24}\left\|B-\frac{\operatorname{tr}B}{3}I\right\|_F^2+o(\varepsilon^2).}
\]
Both the coefficient and the null-space (scalar perturbations) are exact.

For \(L>1\), take the prolate and oblate ellipsoids with squared-semiaxis matrices
\[
Q_L^{\mathrm{pro}}=\operatorname{diag}(L^2,1,1),\qquad
Q_L^{\mathrm{obl}}=\operatorname{diag}(L^2,L^2,1).
\]
Their rank-one defects have **opposite limiting behavior**, despite having the same axis ratio \(L\):
\[
\boxed{\lim_{L\to\infty}\mathscr E(Q_L^{\mathrm{pro}})
=\frac12\left(1-\frac{\sqrt{7281}}{89}\right)>0,\qquad
\mathscr E(Q_L^{\mathrm{obl}})\sim\frac{1}{45\log L}\longrightarrow0.}
\]
Thus there is no global rigidity bound forcing bounded ellipsoidal eccentricity from a small rank-one section-profile defect alone. The exact scalar moment formula also gives an elementary one-variable evaluation for each axial family at every \(L>1\).

## Assumptions and scope

All matrices are positive definite, and all section areas are two-dimensional Euclidean Hausdorff measures. Both probability measures have total mass one. The functions \(\alpha,\beta\) are arbitrary real square-integrable functions; the product is understood in the tensor-product Hilbert space. The infimum is attained (the section profile has rank at most two). The common offset interval is \([-a,a]\), where \(a\) is the smallest semiaxis; measuring outside this interval in a direction-dependent way would define a different quantity. The defect is unchanged under rotations and positive homotheties of the ellipsoid. The three-dimensional restriction is essential to the quadratic-in-offset section-area formula used here.

The near-ball family is quantified as \(\varepsilon\to0\) through positive-definite matrices with the indicated operator-norm expansion, which permits repeated eigenvalues of \(B\) and both signs of \(\varepsilon\) when the family is defined. The two high-eccentricity limits refer to fixed, explicit prolate and oblate axis patterns; no assertion is made about arbitrary degeneration sequences.

## Proof

**1. Exact geometry of a parallel section.** Write \(E_Q=Q^{1/2}B_2^3\). The plane \(u\cdot x=t\) pulls back to a plane in the ball with normal \(Q^{1/2}u\). Its circular radius is \(\sqrt{1-t^2/(u^\mathsf TQu)}\); the two-dimensional affine Jacobian on the plane is \(\sqrt{\det Q}/\sqrt{u^\mathsf TQu}\). Hence for \(|t|<\sqrt{u^\mathsf TQu}\),
\[
A_Q(u,t)=\frac{\pi\sqrt{\det Q}}{\sqrt{u^\mathsf TQu}}
\left(1-\frac{t^2}{u^\mathsf TQu}\right).
\]
Since \(q(u)\ge1\), all \(|s|\le1\) belong to the common interior range (with possible tangent endpoints), and
\[
F_Q(u,s)=q(u)^{-1/2}-s^2q(u)^{-3/2}.
\]
This is the sum of two separated terms; it is rank one if and only if their angular factors are linearly dependent.

**2. Best rank-one error and exact constants.** Let the angular pair be \(f_0=q^{-1/2}\), \(f_1=-q^{-3/2}\), and the offset pair be \(g_0=1\), \(g_1=s^2\). Their Gram matrices in the stated probability measures are
\[
G=\begin{pmatrix}m_1&-m_2\\-m_2&m_3\end{pmatrix},\qquad
H=\begin{pmatrix}1&1/3\\1/3&1/5\end{pmatrix}.
\]
The two possibly nonzero squared singular values \(\lambda_+\ge\lambda_-\ge0\) of the Hilbert–Schmidt kernel \(F_Q\) are the eigenvalues of \(H^{1/2}GH^{1/2}\). Therefore
\[
\lambda_++\lambda_-=\operatorname{tr}(GH)=S,
\qquad \lambda_+\lambda_-=\det G\det H=\frac4{45}D.
\]
In particular, \(S=\|F_Q\|^2>0\). The Hilbert-space Eckart–Young principle, or orthogonal projection followed by the Rayleigh quotient for this two-dimensional range, makes the best rank-one squared residual equal to \(\lambda_-\); division by \(S\) gives the boxed formula. The discriminant is nonnegative because the Gram matrices are positive semidefinite. Cauchy–Schwarz gives \(D\ge0\), with equality exactly when \(q^{-1/2}\) and \(q^{-3/2}\) are proportional almost everywhere. Their ratio is \(q\), so equality forces \(q\) constant, and continuity then implies \(Q\) is scalar. The converse is immediate. This also proves that every nonspherical ellipsoid has exactly two nonzero singular values on this common interval.

**3. Exact second variation near a ball.** Write \(c=\lambda_{\min}(B)\). Uniformly on \(S^2\), first-order eigenvalue perturbation and the assumed matrix expansion give
\[
q_\varepsilon(u)=1+\varepsilon\bigl(u^\mathsf TBu-c\bigr)+O(\varepsilon^2)
\]
when \(\varepsilon\downarrow0\). The two-sided statement follows by the analogous minimum-eigenvalue expansion, replacing \(c\) by \(\lambda_{\max}(B)\) for negative \(\varepsilon\); this only changes a constant in the angular function. Put \(z(u)=u^\mathsf TBu-c\). Expanding the three moments, with constant second-order contributions canceling in the determinant, gives
\[
D=\varepsilon^2\left[\int z^2d\sigma-\left(\int z\,d\sigma\right)^2\right]
+o(\varepsilon^2).
\]
The spherical moments \(\int u_i^2d\sigma=1/3\), \(\int u_i^4d\sigma=1/5\), and \(\int u_i^2u_j^2d\sigma=1/15\) for \(i\ne j\) yield
\[
\operatorname{Var}_{\sigma}(u^\mathsf TBu)
=\frac2{15}\left\|B-\frac{\operatorname{tr}B}{3}I\right\|_F^2.
\]
At the ball, \(m_1=m_2=m_3=1\), hence \(S\to8/15\). Taylor expansion of the square root therefore gives
\[
\mathscr E(Q_\varepsilon)=\frac4{45}\frac{D}{S^2}+o(D)
=\frac5{16}\operatorname{Var}_{\sigma}(u^\mathsf TBu)\varepsilon^2+o(\varepsilon^2)
=\frac{\varepsilon^2}{24}\|B_0\|_F^2+o(\varepsilon^2).
\]
The derivative is positive on every nonzero traceless deformation and zero on scalar deformations, establishing sharp local quadratic response.

**4. Exact axial moments.** For a uniformly distributed \(u\in S^2\), any fixed coordinate \(z=u_i\) is uniform on \([-1,1]\). Consequently, for the prolate family,
\[
m_j^{\mathrm{pro}}=\int_0^1[1+(L^2-1)z^2]^{-j}\,dz.
\]
Elementary integration and recurrence give
\[
\begin{aligned}
m_1^{\mathrm{pro}}&=\frac{\arctan\sqrt{L^2-1}}{\sqrt{L^2-1}},\\
m_2^{\mathrm{pro}}&=\frac12\left(m_1^{\mathrm{pro}}+L^{-2}\right),\\
m_3^{\mathrm{pro}}&=\frac14\left(3m_2^{\mathrm{pro}}+L^{-4}\right).
\end{aligned}
\]
For the oblate family,
\[
m_j^{\mathrm{obl}}=\int_0^1[1+(L^2-1)(1-z^2)]^{-j}\,dz,
\]
with
\[
\begin{aligned}
m_1^{\mathrm{obl}}&=\frac{\operatorname{arcosh}L}{L\sqrt{L^2-1}},\\
m_2^{\mathrm{obl}}&=\frac{m_1^{\mathrm{obl}}+1}{2L^2},\\
m_3^{\mathrm{obl}}&=\frac{3m_2^{\mathrm{obl}}+1}{4L^2}.
\end{aligned}
\]
These formulas, substituted into the exact rank-one-defect expression, evaluate both profiles at any finite axis ratio without numerical optimization.

**5. Prolate limit.** Under \(y=Lz\), dominated convergence gives, for each \(j=1,2,3\),
\[
L m_j^{\mathrm{pro}}\longrightarrow\int_0^\infty(1+y^2)^{-j}\,dy
=\frac{\sqrt\pi\,\Gamma(j-1/2)}{2\Gamma(j)}.
\]
These constants are \(\pi/2,\pi/4,3\pi/16\), respectively. Hence \(LS\to89\pi/240\) and \(L^2D\to\pi^2/32\), giving
\[
\frac{16D}{45S^2}\longrightarrow\frac{640}{7921},\qquad
\mathscr E(Q_L^{\mathrm{pro}})\longrightarrow\frac12\left(1-\frac{\sqrt{7281}}{89}\right)>0.
\]

**6. Oblate limit and failure of global stability.** The elementary arcosh expression gives
\[
m_1^{\mathrm{obl}}\sim\frac{\log(2L)}{L^2}.
\]
The two exact recurrences then imply
\[
m_2^{\mathrm{obl}}\sim\frac{1}{2L^2},\qquad
m_3^{\mathrm{obl}}\sim\frac{1}{4L^2}.
\]
Thus \(S\sim\log(2L)/L^2\), \(D\sim\log(2L)/(4L^4)\), and consequently
\[
\mathscr E(Q_L^{\mathrm{obl}})\sim\frac{1}{45\log(2L)}\sim\frac{1}{45\log L}.
\]
The axis ratio of this family is nevertheless \(L\to\infty\). This proves the contrasting high-eccentricity behavior and the absence of a global inverse bound in the stated metric.

## Verification

The proof is analytical. The accompanying standalone `verify_rank_one.py` uses the Python standard library to check the rational Gram determinant and ball normalization, both exact axial-moment recurrences against independently quadrature-evaluated integrals, the geometric section-area formula against an independently restricted quadratic form on the section plane, the near-sphere \(1/24\) coefficient on explicit traceless directions, and the prolate/oblate asymptotic constants. These finite tests detect algebraic, factor, and sign mistakes; they are not proofs of the universal quantifiers or limiting claims. The estimates in Steps 3, 5, and 6 establish those infinite claims.

Run from a directory containing the extracted files using `python3 verify_rank_one.py`. A successful replay prints `VERIFY_OK`.

## Relationship to prior work

Fish, Ryabogin, Sun and Yaskin (arXiv:2610.10229, first posted 7 October 2026) prove, in particular, that in odd dimension a convex body with a **finite-rank locally separable** parallel section function must be an ellipsoid (their Theorem 4.2). Yaskin and Zawalski (arXiv:2306.17127, Theorem 2.2) study classification under a finite-separability assumption on an integrated section functional. Those are qualitative structure statements, not the relative **optimal rank-one approximation error** of an ellipsoid's complete common-offset section profile. The present theorem develops that quantitatively different observable for the ellipsoids, gives an exact formula in terms of three angular moments, and exhibits the sharp near-sphere anisotropy and the contrasting extreme axial limits.

Related ellipsoid section-recovery results concern reconstruction from selected noncentral areas or moment data. For instance, global Barker–Larman rigidity for ellipsoids uses prescribed-offset directional measurements to prove injectivity; recovery of ellipsoid axes from a finite number of section-volume moments concerns a different functional and data model. Neither type of result entails an \(L^2\) best separable-factor residual. The singular-value principle and spherical quadratic moments used here are classical; novelty is asserted only for the specific geometric deficit and its quantified local/global behavior, not for those tools.

## Limitations

This theorem covers centered ellipsoids in \(\mathbb R^3\), and the chosen normalized common-offset sampling model. It does not prove a stability inequality for all convex bodies, characterize all anisotropic degenerations, solve geometric reconstruction under noisy or finitely sampled data, or supply independence/priority certification. The near-ball expansion is local; the oblate example specifically rules out a naive global extension. Historical works involving statistical separability, singular values of geometric transforms, or differently normalized ellipsoid section kernels could contain an equivalent quantitative formula; a remaining originality risk cannot be removed by unsuccessful searches alone.

## References

1. A. Fish, D. Ryabogin, W. R. Sun and V. Yaskin, *On determination of convex bodies by their section functions*, arXiv:2610.10229v1, first public 2026-10-07. https://arxiv.org/abs/2610.10229.
2. V. Yaskin and B. Zawalski, *On separably integrable symmetric convex bodies*, arXiv:2306.17127, first public 2023-06-29; later *Advances in Mathematics* 441 (2024), 109527. https://arxiv.org/abs/2306.17127.
3. M. Agranovsky, *Convex bodies with algebraic section volume functions*, arXiv:2409.19373, first public 2024-09-28. https://arxiv.org/abs/2409.19373.
4. E. Schmidt, *Zur Theorie der linearen und nichtlinearen Integralgleichungen* (1907), foundational singular-system approximation; the rank-one approximation step also follows directly from the finite-dimensional Rayleigh quotient.
