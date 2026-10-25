# Curvature-controlled onset of the first intrinsic-volume metric beyond translation contact

## Finding
Let \(n\ge 2\), let \(K\subset\mathbb R^n\) be a convex body whose support function is \(C^2\) on the unit sphere, and assume its curvature-radius matrix \(\nabla_S^2h_K+h_K\operatorname{Id}\) is everywhere positive definite. Fix a unit vector \(v\). Define the difference body \(D=K-K\), its radial reach \(T=\max\{t\ge0:tv\in D\}\), the unique outer normal \(u_0\) at \(Tv\), and \(\gamma=\langle u_0,v\rangle>0\). Let \(\kappa_G(D,Tv)\) be the positive Gauss curvature of \(D\) at \(Tv\).

For the Besau–Hoehner first intrinsic-volume metric \(\delta_1\), one has \(\delta_1(K,K+tv)=2t\) for \(0\le t\le T\), while \(\delta_1(K,K+tv)<2t\) for \(t>T\). Moreover,
\[
\lim_{\varepsilon\downarrow0}\frac{2(T+\varepsilon)-\delta_1\bigl(K,K+(T+\varepsilon)v\bigr)}{\varepsilon^{(n+1)/2}}
=\frac{2^{(n+3)/2}}{n+1}\,\gamma^{(n+1)/2}\sqrt{\kappa_G(D,Tv)}.
\]
Thus the sharp post-contact exponent is \((n+1)/2\), and the leading coefficient recovers the Gauss curvature of the difference body from the metric's translation-distance deficit when \(T\) and \(\gamma\) are given.

## Assumptions and scope
The stated \(C^2\) positivity condition means that for every spherical tangent vector \(z\ne0\), \(\langle(\nabla_S^2h_K+h_K\operatorname{Id})z,z\rangle>0\). It is equivalent to positive curvature radii in the support parametrization. In particular, \(D\) is strictly convex with positive curvature radii and has the origin in its interior. The metric \(\delta_1\) is normalized as in Besau–Hoehner, arXiv:2208.13927, Definition 1.1, using Haar *probability* measure on lines and the usual intrinsic-volume normalization.

Write \(\kappa_m=\pi^{m/2}/\Gamma(1+m/2)\) for the unit \(m\)-ball volume and \(\omega_n=n\kappa_n\) for the surface area of the unit sphere. The constant in Kubota's line formula is \(c_n=\omega_n/(2\kappa_{n-1})\). Neither translation of the reference body nor central symmetry of \(K\) is assumed; central symmetry of \(D=K-K\) is automatic. A normal need not equal the radial direction \(v\), which is why the incidence factor \(\gamma\) is necessary.

## Proof
**1. Exact translation profile and contact criterion.** For every unit vector \(u\), the projected interval of \(K\) onto the line it spans has length \(w_K(u)=h_K(u)+h_K(-u)=h_D(u)\), and translation by \(tv\) shifts the projected interval by \(t\langle u,v\rangle\). The one-dimensional symmetric difference of intervals of equal length \(w\) shifted by \(s\) has length \(2\min\{|s|,w\}\). Using antipodal symmetry of spherical probability measure \(\sigma\), the definition of the intrinsic-volume metric yields the exact identity, for every \(t\ge0\),
\[
\delta_1(K,K+tv)=2c_n\int_{S^{n-1}}\min\bigl\{t|\langle u,v\rangle|,h_D(u)\bigr\}\,d\sigma(u).
\tag{1}
\]
Since \(c_n\int |\langle u,v\rangle|\,d\sigma=1\), the nonnegative defect is
\[
F(t):=2t-\delta_1(K,K+tv)=2c_n\int_{S^{n-1}}\bigl(t|\langle u,v\rangle|-h_D(u)\bigr)_+\,d\sigma(u).
\tag{2}
\]
The support inequality for \(tv\in D\) is \(h_D(u)\ge t|\langle u,v\rangle|\) for all \(u\), because both \(tv\) and \(-tv\) then lie in \(D\). Conversely, these inequalities for every \(u\) imply \(\pm tv\in D\) by the support half-space representation. Thus \(F(t)=0\) exactly when \(0\le t\le T\); for \(t>T\), the inequality is strictly reversed in an open cap around the outer normal at \(Tv\), hence \(F(t)>0\).

**2. Isolate the only two critical directions.** Put \(x=Tv\). Since \(D\) is strictly convex and has \(C^2\) strictly positive curvature radii, there is a unique outer normal \(u_0\) at \(x\), and the only equality directions in \(h_D(u)\ge T|\langle u,v\rangle|\) are \(u_0\) and \(-u_0\). Here \(T\gamma=h_D(u_0)>0\), so \(\gamma>0\). Compactness gives a strictly positive support gap outside disjoint small caps around those normals, hence for sufficiently small \(\varepsilon>0\) the positive integrand in (2) is confined to those caps. The two cap integrals are equal because \(h_D\) and \(|\langle u,v\rangle|\) are even.

**3. Quadratic support gap and curvature.** Identify the tangent space at \(u_0\) with \(\mathbb R^{n-1}\). Parametrize a normal cap by \(u(\xi)=(u_0+\xi)/\sqrt{1+|\xi|^2}\), where \(\xi\perp u_0\). Define \(G(u)=h_D(u)-T\langle u,v\rangle\) in that cap. The supporting point at \(u_0\) is \(x=Tv\), so \(G(u_0)=0\) and its spherical gradient vanishes. The spherical Hessian is
\[
Q=\nabla_S^2h_D(u_0)+h_D(u_0)\operatorname{Id},
\]
because \(\nabla_S^2(T\langle u,v\rangle)=-T\langle u,v\rangle\operatorname{Id}\). It is positive definite. Consequently,
\[
G(u(\xi))=\tfrac12\langle Q\xi,\xi\rangle+o(|\xi|^2),\qquad \langle u(\xi),v\rangle=\gamma+O(|\xi|),
\]
and uniformly for \(|\xi|=O(\sqrt\varepsilon)\),
\[
((T+\varepsilon)\langle u(\xi),v\rangle-h_D(u(\xi)))_+
=\bigl(\varepsilon\gamma-\tfrac12\langle Q\xi,\xi\rangle+o(\varepsilon)\bigr)_+.
\tag{3}
\]
The strictly positive least eigenvalue of \(Q\) ensures that the support of (3) is contained in a tangent ball of radius \(C\sqrt\varepsilon\) independent of \(\varepsilon\). The spherical area Jacobian in these coordinates tends uniformly to one. By dominated convergence after \(\xi=\sqrt{\varepsilon\gamma}\,Q^{-1/2}z\), the contribution of the cap at \(u_0\) to the **unnormalized** surface integral is
\[
(\varepsilon\gamma)^{(n+1)/2}(\det Q)^{-1/2}
\int_{|z|<\sqrt2}\bigl(1-|z|^2/2\bigr)dz
+o\bigl(\varepsilon^{(n+1)/2}\bigr).
\tag{4}
\]
By polar integration in dimension \(m=n-1\),
\[
\int_{|z|<\sqrt2}(1-|z|^2/2)dz
=\frac{2^{(n+1)/2}\kappa_{n-1}}{n+1}.
\tag{5}
\]
The eigenvalues of \(Q\) are the principal curvature radii of \(\partial D\) at \(x\), so \((\det Q)^{-1/2}=\sqrt{\kappa_G(D,x)}\). There are precisely two identical antipodal caps. Multiplying (4)–(5) by \(2\), then the probability-sphere conversion \(1/\omega_n\), and then \(2c_n\) from (2), and using \(c_n=\omega_n/(2\kappa_{n-1})\), gives
\[
F(T+\varepsilon)=\frac{2^{(n+3)/2}}{n+1}
\gamma^{(n+1)/2}\sqrt{\kappa_G(D,x)}\varepsilon^{(n+1)/2}
+o(\varepsilon^{(n+1)/2}).
\]
Every factor is positive. This proves the threshold, coefficient, and strict sharpness of the exponent.

## Verification
The full derivation rests on the elementary interval symmetric-difference identity, the support-function Hessian, the exact spherical normalization, and dominated convergence on the two rescaled caps. All four steps are explicit above. As independent arithmetic consistency checks, for a Euclidean ball \(K=rB_2\) the predicted coefficient equals \(4/(3\sqrt r)\), and for \(K=rB_3\) it equals \(1/r\). In the plane the defect is exactly
\[
F(2r+\varepsilon)=2\sqrt{(2r+\varepsilon)^2-4r^2}-4r\arccos\!\frac{2r}{2r+\varepsilon},
\]
whose leading term is \(4\varepsilon^{3/2}/(3\sqrt r)\). In three dimensions the exact defect is \(F(2r+\varepsilon)=2\varepsilon^2/(2r+\varepsilon)\). The companion standard-library program `verify.py` evaluates these identities and also noncircular planar ellipses to test the curvature normalization. Such finite tests check constants only; the proof above covers every dimension and all specified smooth bodies.

## Relationship to prior work
Besau and Hoehner introduce \(\delta_j\) and establish, in their Proposition 2.6(v), that \(\delta_1=\rho_1\) when two bodies intersect. For translates, this **already implies the entire equality \(\delta_1(K,K+tv)=2t\) up to contact**; that covered equality is not claimed as a new result. Their definition also directly supplies the exact shadow integral (1), and Proposition 2.6(ii) supplies the global bound \(\delta_1\le\rho_1\). What the present finding adds is the **post-contact curvature-sensitive exponent and explicit local coefficient**, for arbitrary smooth strictly convex \(K\) and translations along any unit direction. The 2025 follow-up by Hoehner addresses topology of \(\delta_j\) for \(2\le j\le n-1\), a different invariant/regime. Relevant distinctions are recorded in the accompanying review.

## Limitations
The expansion is one-sided as \(\varepsilon\downarrow0\). It uses uniform positive principal curvature radii: polyhedral bodies, singular normals, vanishing curvature, and degenerate contact can have different exponents and are not covered. It gives neither a global closed formula for general \(K\) and large displacement nor higher terms without stronger smoothness. It does not establish absolute publication priority beyond the documented primary-literature and indexed-claim comparisons. The result is analytically proved here but not independently audited.

## References
1. F. Besau and S. Hoehner, *An intrinsic volume metric for the class of convex bodies in \(\mathbb R^n\)*, arXiv:2208.13927, first posted 29 August 2022; Definition 1.1 and Proposition 2.6 (especially part (v)). https://arxiv.org/abs/2208.13927 ; accessible full text https://arxiv.org/html/2208.13927v3.
2. S. Hoehner, *Some topological properties of the intrinsic volume metric*, arXiv:2512.02379, posted 2 December 2025, abstract and introduction; treats \(2\le j\le n-1\). https://arxiv.org/abs/2512.02379.
