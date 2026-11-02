# Sharp conditional envelopes for the \(L^2\)-Cartesian numerical radius

## Finding

Let \(T\ne0\) be a bounded operator on a nonzero complex Hilbert space. Put \(R=\omega(T)>0\), where \(\omega\) is the numerical radius, and let
\[
Q^2=\omega_2(T)^2=\frac1{2\pi}\int_0^{2\pi}\|\operatorname{Re}(e^{-i\theta}T)\|^2\,d\theta.
\]
Let \(d(T)=\inf_{\alpha\in\mathbb R,\ S=S^*}\|T-e^{i\alpha}S\|\), and write \(u=d(T)/R\in[0,1]\). Define for \(0\le u\le1\), with \(\phi=\arccos u\), \(s=\sqrt{1-u^2}\),
\[
L(u)=u^2+\frac{(1-2u^2)\phi+us}{\pi},\qquad
U(u)=1-\frac{\phi-us}{\pi}.
\]
Then the **complete sharp conditional interval** is
\[
\boxed{L(u)\,R^2\le Q^2\le U(u)\,R^2.}
\]
For each \(u\in[0,1]\), both endpoints and every intermediate value occur for bounded normal operators on separable infinite-dimensional complex Hilbert spaces, with that exact value of \(d(T)/R\). In fact,
\[
\boxed{U(u)-L(u)=\frac2\pi(1-u^2)\arcsin u.}
\]
Set \(C_T=\operatorname{conv}(\overline{W(T)}\cup-\overline{W(T)})\subset\mathbb C\). For \(0<u<1\), equality on the lower side holds exactly when \(C_T\), after scaling by \(1/R\) and rotation, equals \(\operatorname{conv}(u\overline{\mathbb D}\cup\{\pm i\})\); equality on the upper side holds exactly when it equals \(\overline{\mathbb D}\cap\{z:|\operatorname{Re}z|\le u\}\). At \(u=0\), both endpoints equal \(1/2\) and \(C_T\) is a diameter segment, up to rotation and scale; at \(u=1\), both equal \(1\) and \(C_T\) is the disk.

A consequential **optimal global cubic stability constant** is
\[
\boxed{\omega_2(T)^2-\frac{\omega(T)^2}{2}\ge\frac4{3\pi}\frac{d(T)^3}{\omega(T)}.}
\]
The coefficient \(4/(3\pi)\) is the largest valid universal coefficient. The complementary upper-endpoint deficit satisfies
\[
\frac{R^2-Q^2}{R^2}\ge\frac{\arccos u-u\sqrt{1-u^2}}\pi
\sim\frac{4\sqrt2}{3\pi}(1-u)^{3/2}\quad(u\uparrow1),
\]
with a sharp asymptotic constant and exponent, attained by the upper-envelope normal family.

## Assumptions and scope

No separability, normality, compactness, finite dimension, or norm-attainment hypothesis is used for the universal inequalities. The nonzero hypothesis gives \(R>0\). The numerical range is \(W(T)=\{\langle Tx,x\rangle:\|x\|=1\}\), and overlines mean complex closure. The Hilbert-space inner-product convention does not affect any formula. The unit disk is \(\overline{\mathbb D}=\{z\in\mathbb C:|z|\le1\}\). Endpoint realization is on separable infinite-dimensional Hilbert spaces; no finite-dimensional endpoint-attainment assertion for \(0<u<1\) is needed.

## Proof

**1. Distance is the minimum directional support.** For any bounded \(A\), its imaginary part is contractive in operator norm, and \(\operatorname{Re}A\) is self-adjoint. Consequently, for each fixed \(\alpha\),
\[
\inf_{S=S^*}\|e^{-i\alpha}T-S\|=\|\operatorname{Im}(e^{-i\alpha}T)\|.
\]
The infimum is achieved by \(S=\operatorname{Re}(e^{-i\alpha}T)\). Shifting the phase by \(\pi/2\) gives
\[
d(T)=\min_\theta \|\operatorname{Re}(e^{-i\theta}T)\|.
\]
Continuity makes the phase minimum attained. Let \(h(\theta)=\max_{z\in C_T}\operatorname{Re}(e^{-i\theta}z)\). The central symmetry of \(C_T\) gives the exact identity
\[
h(\theta)=\|\operatorname{Re}(e^{-i\theta}T)\|.
\]
Thus \(\min h=d(T)\), \(\max h=R\), and \(Q^2=(2\pi)^{-1}\int h^2\). In particular \(0\le d(T)\le R\).

**2. Universal geometric containment.** Divide \(C_T\) by \(R\) and call the result \(K\). It is compact, convex, centrally symmetric, has support function \(h_K\), and satisfies \(\min h_K=u\), \(\max h_K=1\). Support-function comparison gives \(u\overline{\mathbb D}\subset K\subset\overline{\mathbb D}\). Since \(\max h_K=1\), there is a point \(v\in K\) with \(|v|=1\); central symmetry supplies \(-v\), hence
\[
\operatorname{conv}(u\overline{\mathbb D}\cup\{\pm v\})\subset K.
\]
Choose a unit direction \(w\) where \(h_K(w)=u\). Symmetry implies \(|\operatorname{Re}(z\bar w)|\le u\) for all \(z\in K\), so
\[
K\subset\overline{\mathbb D}\cap\{z:|\operatorname{Re}(z\bar w)|\le u\}.
\]
The two bounding bodies may have different orientations, but circular averaging of their squared support functions is rotation invariant. Their supports bound \(h_K\) pointwise in the respective orientations and are nonnegative.

**3. Evaluation of the two exact integrals.** Normalize the first extreme body to \(K_-=\operatorname{conv}(u\overline{\mathbb D}\cup\{\pm i\})\), and the second to \(K_+=\overline{\mathbb D}\cap\{|\operatorname{Re}z|\le u\}\). By symmetry, their squared-support means are four times the first-quadrant integrals divided by \(2\pi\). Put \(\phi=\arccos u\), \(s=\sqrt{1-u^2}\). In the first quadrant,
\[
h_{K_-}(\theta)=\max\{u,\sin\theta\},\qquad
h_{K_+}(\theta)=\begin{cases}u\cos\theta+s\sin\theta,&0\le\theta\le\phi,\\1,&\phi\le\theta\le\pi/2.\end{cases}
\]
The first formula switches at \(\theta=\pi/2-\phi\). Elementary integration gives
\[
\begin{aligned}
\frac2\pi\left[\int_0^{\pi/2-\phi}u^2\,d\theta+\int_{\pi/2-\phi}^{\pi/2}\sin^2\theta\,d\theta\right]&=L(u),\\
\frac2\pi\left[\int_0^\phi(u\cos\theta+s\sin\theta)^2\,d\theta+\int_\phi^{\pi/2}1\,d\theta\right]&=U(u).
\end{aligned}
\]
Indeed, the second integral inside the upper expression equals \((\phi+us)/2\). Squaring and integrating the inclusions in Step 2 proves the claimed inequalities. Subtracting the two closed forms yields \(U(u)-L(u)=2(1-u^2)\arcsin(u)/\pi\).

**4. Exact equality, sharpness, and interval filling.** If equality holds in either bound, the continuous nonnegative difference of the relevant squared support functions has zero integral, hence the support functions agree at every direction. Compact convex sets are uniquely determined by support functions. This forces exactly the asserted extremal bodies (up to rotations), including the endpoint cases.

Both \(K_-\) and \(K_+\) contain the disk of radius \(u\), are contained in the unit disk, meet the imaginary axis at \(\pm i\), and have support exactly \(u\) in the horizontal direction. Moreover \(K_-\subset K_+\). Therefore each Minkowski interpolation \(K_t=(1-t)K_-+tK_+\), \(0\le t\le1\), has \(\min h_{K_t}=u\) and \(\max h_{K_t}=1\). Its squared-support integral varies continuously from \(L(u)\) to \(U(u)\), filling the whole interval. To realize any such compact convex \(K_t\) as a numerical-range closure, choose a countable dense subset \(\{z_n\}\subset K_t\) and take the normal diagonal operator \(Ne_n=z_ne_n\) on \(\ell^2\). The spectral theorem, or elementary diagonal-vector convex combinations plus approximation, gives \(\overline{W(N)}=K_t\), so its invariants are the required ones.

**5. Optimal cubic coefficient and upper endpoint law.** Differentiate the explicit lower profile to obtain \(L'(u)=4u\arcsin(u)/\pi\) and note \(L(0)=1/2\). Hence
\[
L(u)-\frac12=\frac4\pi\int_0^u t\arcsin t\,dt\ge\frac4{3\pi}u^3.
\]
The elementary inequality \(\arcsin t\ge t\) proves the global bound. Moreover \(L(u)-1/2=(4/(3\pi))u^3+O(u^5)\) as \(u\downarrow0\). The realized \(K_-\) family therefore makes any larger coefficient impossible. Similarly \(1-U(u)=[\phi-\frac12\sin(2\phi)]/\pi\), where \(u=\cos\phi\), so Taylor expansion at \(\phi=0\) proves the stated \(3/2\)-power asymptotic with coefficient \(4\sqrt2/(3\pi)\). The realized \(K_+\) family proves sharpness.

## Verification

The proof above is dimension-free. The supplementary standalone script `verify_cartesian_profiles.py` checks both quadratures, both phase-profile endpoint values, the profile-width formula, a family of Minkowski interpolations, and finite diagonal normal examples. Its finite tests are corroborating diagnostics and are not used as proofs of universal quantification or optimal constants.

## Relationship to prior work

Audeh, Moradi, and Sahoo [1, Theorem 4] introduced \(\omega_2\) and proved the unconditional sharp bounds \(R/\sqrt2\le Q\le R\). Their Theorems 12 and 17 provide different Cartesian-part and commuting-part estimates; the inspected full text does not give conditional envelopes at fixed phase-self-adjoint distance, exact extremal numerical-range shapes, or the complete interval. The published result [2] proves a cubic **lower** stability estimate with coefficient \(1/(2\pi)\), explicitly without claiming the best coefficient. The present lower profile implies the optimal coefficient \(4/(3\pi)\), while the upper profile and interval filling are different information. The separate unitary spectral-gap classification [3] concerns unitary spectra and does not imply a complete profile for arbitrary bounded operators. Standard convex support-function duality [4] supplies the geometric containment tools, not the operator-specific averaged norm envelopes.

## Limitations

The extremal sets are closures of symmetrized numerical ranges, not necessarily numerical ranges themselves; numerical-range closure must not be silently discarded. The sharp realizations are infinite-dimensional normal diagonal operators; no claim is made that both extreme shapes occur as finite-matrix numerical ranges for interior \(u\). The parameter \(d(T)\) uses operator norm and phase-self-adjoint approximation, not a Schatten norm. Possible equivalent convex-geometric integral inequalities under another name remain a literature-priority risk.

## References

[1] W. Audeh, H. R. Moradi, and S. Sahoo, *The \(L^2\)-Cartesian Numerical Radius of Hilbert Space Operators*, arXiv:2610.04844v1, first public 4 October 2026, https://arxiv.org/html/2610.04844v1.

[2] *Cubic operator-norm stability for the \(L^2\)-Cartesian numerical radius*, published research record `ffd07fee0727` (2026), full proof inspected.

[3] *Exact projective spectral-gap formula and optimal finite spectra for the \(L^2\)-Cartesian radius of unitaries*, published research record `f6644dc86b39` (2026), full proof inspected.

[4] R. Schneider, *Convex Bodies: The Brunn--Minkowski Theory*, second expanded edition, Cambridge University Press (2014), support functions and convex-set inclusion, Section 1.7.
