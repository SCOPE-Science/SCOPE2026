# Sharp spherical-harmonic stability of Gaussian localization purity in higher dimensions

## Finding

Fix an integer \(d\ge 2\) and put \(N=2d\). Let \(\varphi(x)=2^{d/4}e^{-\pi|x|^2}\) be the normalized Gaussian on \(\mathbb R^d\), let \(V_\varphi\) be its short-time Fourier transform, and let \(L_\Omega=V_\varphi^*\mathbf1_\Omega V_\varphi\) for a bounded measurable subset \(\Omega\subset\mathbb R^N\). Set
\[
J(\Omega)=\|L_\Omega\|_{S_2}^2=\iint_{\Omega\times\Omega}e^{-\pi|x-y|^2}\,dx\,dy.
\]
For each \(R>0\), write \(B_R=\{x\in\mathbb R^N:|x|<R\}\). Consider an exactly volume-preserving, twice continuously differentiable family of star-shaped domains
\[
\Omega_\varepsilon=\{r\omega:\omega\in S^{N-1},\ 0\le r<\rho_\varepsilon(\omega)\},\quad
\rho_0\equiv R,\quad \partial_\varepsilon\rho_\varepsilon|_0=u\in C^2(S^{N-1};\mathbb R),
\quad |\Omega_\varepsilon|=|B_R|.
\]
Let \(u=\sum_{m=0}^{\infty}u_m\) be its orthogonal decomposition into spherical harmonics of degree \(m\), with the usual surface measure on \(S^{N-1}\). Exact volume preservation forces \(u_0=0\). Put \(t=2\pi R^2\), and let \(I_\nu\) denote the modified Bessel function of the first kind. Then
\[
\boxed{\lim_{\varepsilon\to0}\frac{J(B_R)-J(\Omega_\varepsilon)}{\varepsilon^2}
=R^{2N-2}e^{-t}\sum_{m=2}^{\infty}\bigl(\Lambda_1(t)-\Lambda_m(t)\bigr)\|u_m\|_{L^2(S^{N-1})}^2,}
\]
where
\[
\Lambda_m(t)=(2\pi)^{N/2}t^{1-N/2}I_{m+N/2-1}(t).
\]
The degree-one (infinitesimal translation) modes are exactly the Hessian kernel among volume-preserving deformations. All higher degrees are strictly stable. More precisely, the best quadratic bound is
\[
\lim_{\varepsilon\to0}\frac{J(B_R)-J(\Omega_\varepsilon)}{\varepsilon^2}
\ge G_{N,R}\sum_{m\ge2}\|u_m\|_2^2,
\qquad
\boxed{G_{N,R}=R^{2N-2}(2\pi)^{N/2}t^{1-N/2}e^{-t}
\bigl(I_{N/2}(t)-I_{N/2+1}(t)\bigr)>0.}
\]
Equality for a nonzero transverse perturbation holds exactly when only degree two is present (in addition to any degree-one translational component). Thus quadrupolar deformations are the unique least-penalized shape modes modulo translations. Writing \(v_N=\pi^{N/2}/\Gamma(N/2+1)\), the sharp coefficient has both exact extreme-radius laws:
\[
\boxed{G_{N,R}\sim2\pi v_N R^{2N}\quad(R\downarrow0),\qquad
G_{N,R}\sim\frac{N+1}{4\pi}R^{N-3}\quad(R\to\infty).}
\]
These are statements for every fixed even dimension \(N\ge4\); no assertion of a global sharp nonlinear stability constant is made.

## Assumptions and scope

The deformation parameter varies in a neighborhood of zero; \(\rho_\varepsilon\) is positive and \(C^2\) in \(\varepsilon\) with values in \(C^2(S^{N-1})\). Domain volumes agree **exactly** for every sufficiently small \(\varepsilon\). The functions \(u_m\) are orthogonal projections of the initial normal velocity in ordinary \(L^2(S^{N-1},d\sigma)\); no normalized probability surface measure is used. The limit is along a **fixed** deformation family. It is not a uniform estimate over families depending on \(\varepsilon\), and it is not a statement about the individual eigenvalues of \(L_\Omega\). All results apply to \(d\ge2\), so the multi-dimensional claim is not a restatement of a planar weighted-Bergman shape formula.

## Proof

**1. Normalization and shape derivatives.** The standard Gaussian coherent-state identity gives the displayed Gaussian double integral for \(J\). Define \(\Phi_R(x)=\int_{B_R}e^{-\pi|x-y|^2}\,dy\). Rotational invariance makes \(\Phi_R\) radial. Write \(\rho_\varepsilon=R+\varepsilon u+\varepsilon^2v+o(\varepsilon^2)\) in \(C^2\), where \(v=(1/2)\partial_\varepsilon^2\rho_\varepsilon|_0\). Expanding \(|\Omega_\varepsilon|=N^{-1}\int_S\rho_\varepsilon^N\,d\sigma\) yields
\[
\int_Su\,d\sigma=0,\qquad
\int_Sv\,d\sigma=-\frac{N-1}{2R}\int_Su^2\,d\sigma.
\]
Twice differentiating the smooth-kernel double integral using polar upper limits gives
\[
\begin{aligned}
J''(0)={}&2R^{2N-2}\iint_{S\times S}e^{-\pi R^2|\omega-\eta|^2}u(\omega)u(\eta)\,d\sigma(\omega)d\sigma(\eta)\\
&+2R^{N-1}\bigl(\Phi_R'(R)+(N-1)\Phi_R(R)/R\bigr)\int_Su^2\,d\sigma
+4R^{N-1}\Phi_R(R)\int_Sv\,d\sigma.
\end{aligned}
\]
The volume identity cancels the two terms containing \(\Phi_R(R)\). This leaves
\[
J''(0)=2R^{2N-2}\iint_{S\times S}e^{-\pi R^2|\omega-\eta|^2}u(\omega)u(\eta)\,d\sigma d\sigma
+2R^{N-1}\Phi_R'(R)\int_Su^2\,d\sigma.
\]
The first derivative vanishes because the sphere-potential is constant and \(\int_Su=0\).

**2. Boundary derivative and harmonics.** Since the kernel depends only on \(x-y\), the divergence theorem gives, at \(x=R\omega\),
\[
\Phi_R'(R)=-R^{N-1}\int_S e^{-\pi R^2|\omega-\eta|^2}(\omega\cdot\eta)\,d\sigma(\eta)
=-R^{N-1}e^{-t}\Lambda_1(t).
\]
For \(t=2\pi R^2\), the Funk--Hecke formula or the spherical plane-wave expansion shows that the operator
\[
(\mathcal K_t f)(\omega)=\int_S e^{t\omega\cdot\eta}f(\eta)\,d\sigma(\eta)
\]
acts on every degree-\(m\) spherical harmonic as multiplication by
\[
\Lambda_m(t)=(2\pi)^{N/2}t^{1-N/2}I_{m+N/2-1}(t).
\]
For clarity, this normalization is fixed by \(\Lambda_0(t)=\int_S e^{t\omega\cdot\eta}\,d\sigma(\eta)\). Inserting the orthogonal expansion of \(u\) yields
\[
J''(0)=2R^{2N-2}e^{-t}\sum_{m\ge1}\bigl(\Lambda_m(t)-\Lambda_1(t)\bigr)\|u_m\|_2^2.
\]
The \(m=1\) contribution cancels exactly. Taylor's formula proves the announced defect expansion.

**3. Strict ordering and sharp constant.** For each \(\nu>-1/2\) and \(t>0\), the positive integral representation
\[
I_\nu(t)=\frac{(t/2)^\nu}{\sqrt\pi\,\Gamma(\nu+1/2)}\int_{-1}^{1}e^{ts}(1-s^2)^{\nu-1/2}\,ds
\]
combined with integration by parts shows that \(I_{\nu+1}(t)/I_\nu(t)\) equals the expectation of \(s\) under the probability density proportional to \(e^{ts}(1-s^2)^{\nu-1/2}\). This expectation lies strictly between zero and one: strict positivity follows by pairing \(s\) and \(-s\), and strict upper boundedness follows because \(s<1\) almost surely. Thus \(I_\nu(t)>I_{\nu+1}(t)>0\). Applied to \(\nu=m+N/2-1\), this gives \(\Lambda_1>\Lambda_2>\Lambda_3>\cdots>0\). The least transverse penalty is consequently the degree-two coefficient, and it is attained precisely by degree-two harmonics modulo degree one. Such perturbations occur in actual exactly-volume-preserving families, for example by multiplying \(R+\varepsilon u(\omega)\) by the unique positive scalar making the enclosed volume equal to \(|B_R|\).

**4. Radius laws.** As \(t\downarrow0\), \(I_\nu(t)=(t/2)^\nu/\Gamma(\nu+1)(1+O(t^2))\) and \(I_{\nu+1}(t)=O(t^{\nu+1})\). With \(\nu=N/2\), substitution gives \(G_{N,R}=2\pi v_NR^{2N}(1+O(R^2))\). As \(t\to\infty\), for each fixed order \(\nu\),
\[
e^{-t}I_\nu(t)=(2\pi t)^{-1/2}\left(1-\frac{4\nu^2-1}{8t}+O(t^{-2})\right).
\]
Subtracting the orders \(\nu=N/2\) and \(\nu+1\) gives \((N+1)/(2t\sqrt{2\pi t})(1+O(t^{-1}))\); substituting \(t=2\pi R^2\) yields \(G_{N,R}=\frac{N+1}{4\pi}R^{N-3}(1+O(R^{-2}))\). Every error term here is for fixed dimension.

## Verification

The accompanying script `verify_multidimensional_gaussian_hessian.py` evaluates the Funk--Hecke multipliers independently by Gegenbauer quadrature in dimensions four, six and eight; it compares them against the modified-Bessel formulas, checks strict finite-order eigenvalue ordering, and checks both extreme-radius constants. It passed 69 finite tests using NumPy and SciPy. These finite computations provide a reproducible normalization check, **not** a proof of the full harmonic expansion or the asymptotic limits. Those follow from the derivations above.

## Relationship to prior work

Nicola and Riccardi's 2024 work establishes the Gaussian double-integral representation, global isoperimetric optimality, equality rigidity, and a quantitative (but not sharp-local-spectral) bound for the Hilbert--Schmidt localization norm. Its Sections 3--5, including the sharpness discussion, do not state the dimension-dependent spherical-harmonic Hessian, its degree-two sharp spectral gap, or the two exact radius asymptotics above. Nicola and Tilli's 2022 work studies operator-norm extremizers, not this full Hilbert--Schmidt shape Hessian. The multidimensional Gaussian curvature law here should not be conflated with the different two-dimensional hyperbolic Bergman coherent-state shape Hessian: a planar contraction limit does not cover spherical harmonics in dimensions four and above. The Gaussian interaction functional itself, Fourier--Bessel machinery, and general quantitative rearrangement framework are established tools and are not claimed as new.

## Limitations

This establishes second-order stability only for smooth, fixed, star-shaped equal-volume deformations. The first spherical-harmonic component corresponds to infinitesimal translations, and exact translations are truly neutral by translation invariance. No global nonlinear stability constant, arbitrary measurable-set stability estimate, unbounded-dimension uniform remainder, or stability of individual eigenvalues is asserted. Independent mathematical validation and complete historical-priority certification have not been performed; an equivalent all-dimensional Gaussian interaction Hessian under a different terminology may exist.

## References

- F. Nicola and F. Riccardi, *The quantitative isoperimetric inequality for the Hilbert-Schmidt norm of localization operators*, arXiv:2401.04659 (first public January 9, 2024), particularly Sections 3--5. https://arxiv.org/abs/2401.04659
- F. Nicola and P. Tilli, *The norm of time-frequency and wavelet localization operators*, arXiv:2207.08624 (first public July 18, 2022), Sections 1--2. https://arxiv.org/abs/2207.08624
- Classical Funk--Hecke spherical harmonic formula and integral and asymptotic representations of modified Bessel functions, as employed and proved in the relevant steps above.
