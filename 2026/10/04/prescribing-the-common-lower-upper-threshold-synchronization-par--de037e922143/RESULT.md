# Prescribing the common lower–upper threshold synchronization parameter
## Finding
Consider the lattice generalized Friedrichs family of Rasulov and Dilmurodov with
\[
\varepsilon(t)=\sum_{j=1}^3(1-\cos t_j),\qquad
\Lambda=\{k: k_j\in\{-2\pi/3,2\pi/3\}\}.
\]
For every prescribed \(\gamma_*\in(0,9)\), there is a strictly positive real-analytic form factor \(v:\mathbb T^3\to\mathbb R\), even in each coordinate, for which all eight lower–upper synchronization parameters of the source are equal to \(\gamma_*\). If
\[
I_v=\int_{\mathbb T^3}\frac{v(t)^2}{\varepsilon(t)}\,dt,
\]
then the common critical coupling is
\[
\mu_*=\sqrt{\frac{2\gamma_*}{I_v}}.
\]
At this coupling, \(A_{\mu_*}(0)\) has a virtual level at energy \(0\), while every \(A_{\mu_*}(k)\) with \(k\in\Lambda\) has a virtual level at energy \(27/2\). Thus the attainable set of common synchronization parameters, even within positive coordinate-even analytic form factors, is exactly \((0,9)\).

## Assumptions and scope
The operator family, dispersion, Fredholm determinant, and threshold terminology are those of Rasulov–Dilmurodov. The parameter satisfies \(0<\gamma_*<9\). The form factor is required to be real analytic, strictly positive, and even separately in each coordinate. The torus measure is the same Haar measure as in the source; its normalization changes \(I_v\) and \(\mu_*\) together but does not affect the synchronization parameter.

The result concerns the nine extremal fibers consisting of \(k=0\) and the eight points of \(\Lambda\). It does not claim that other fibers have no discrete spectrum.

## Proof
For \(k\in\Lambda\), the source's upper-threshold denominator has the exact identity
\[
9-\varepsilon(k+t)-\varepsilon(t)=\varepsilon(t-k).
\]
Indeed, for each coordinate \(k_j=\pm2\pi/3\),
\[
\cos(t_j+k_j)+\cos t_j=\cos(t_j+k_j/2)=-\cos(t_j-k_j).
\]
Hence, with
\[
I(v)=\int_{\mathbb T^3}\frac{v(t)^2}{\varepsilon(t)}\,dt,
\qquad
J_k(v)=\int_{\mathbb T^3}\frac{v(t)^2}{\varepsilon(t-k)}\,dt,
\]
the source formulas become
\[
\mu_l(\gamma)^2=\frac{2\gamma}{I(v)},\qquad
\mu_r^{(k)}(\gamma)^2=\frac{9-\gamma}{J_k(v)}.
\]
If \(v\) is even in each coordinate, then \(J_k(v)\) is independent of the signs of the coordinates of \(k\). Write this common value as \(J(v)\). The common synchronization condition is therefore
\[
\frac{J(v)}{I(v)}=r_*,\qquad
r_*:=\frac{9-\gamma_*}{2\gamma_*}>0.
\]
It remains to show that every positive value of this quotient is attained by a positive coordinate-even analytic form factor.

Put \(a=2\pi/3\). For \(B>0\), define two positive coordinate-even analytic functions
\[
u_B(t)=\exp\!\left(B\sum_{j=1}^3\cos t_j\right),
\]
and
\[
w_B(t)=\exp\!\left(-B\sum_{j=1}^3(\cos t_j+1/2)^2\right).
\]
The function \(u_B\) localizes at \(0\). Standard local quadratic bounds at that nondegenerate maximum, together with \(\varepsilon(t)\asymp |t|^2\) near \(0\), give
\[
I(u_B)\asymp e^{6B}B^{-1/2},\qquad
J(u_B)=O(e^{6B}B^{-3/2}),
\]
so \(J(u_B)/I(u_B)\to0\).

The zero set of \(\sum_j(\cos t_j+1/2)^2\) is exactly \(\Lambda\), and each zero is nondegenerate. Therefore \(w_B\) localizes equally at those eight points. Since \(\varepsilon\) is bounded away from zero on \(\Lambda\), while \(\varepsilon(t-k)\asymp|t-k|^2\) at the selected point \(k\), the same local comparison gives
\[
I(w_B)\asymp B^{-3/2},\qquad
J(w_B)\asymp B^{-1/2},
\]
so \(J(w_B)/I(w_B)\to+\infty\).

Choose \(B\) large enough that
\[
\frac{J(u_B)}{I(u_B)}<r_*<\frac{J(w_B)}{I(w_B)}.
\]
For \(0\le\theta\le1\), set
\[
v_\theta=(1-\theta)u_B+\theta w_B.
\]
Every \(v_\theta\) is strictly positive, real analytic, and coordinate-even. Both \(I(v_\theta)\) and \(J(v_\theta)\) are finite positive continuous quadratic functionals of \(v_\theta\), so their quotient is continuous in \(\theta\). The intermediate value theorem gives \(\theta_*\) with \(J(v_{\theta_*})/I(v_{\theta_*})=r_*\).

For this form factor, all eight source parameters \(\gamma_i\) equal \(\gamma_*\), and the lower and all eight upper critical couplings equal \(\mu_*\). Strict positivity gives \(v(0)\ne0\) and \(v(k)\ne0\) for every \(k\in\Lambda\); the source's threshold classification therefore makes all nine critical states virtual levels rather than threshold eigenvalues.

## Verification
The proof is analytic. The endpoint quotient limits use only local two-sided quadratic bounds around finitely many nondegenerate extrema and the three-dimensional integrability of \(|t|^{-2}\). The accompanying script checks the exact trigonometric identity at all eight upper points on a deterministic test set, checks the sign-symmetry reduction for coordinate-even test functions, and checks the algebraic inversion \(r_*=(9-\gamma_*)/(2\gamma_*)\). These finite checks are corroborative and are not used as a substitute for the localization proof.

## Relationship to prior work
Rasulov and Dilmurodov derive, for an arbitrary analytic form factor, separate lower and upper critical couplings and a form-factor-dependent synchronization number \(\gamma_i\) for each of the eight upper extrema. Their paper does not determine the attainable set of these synchronization numbers as the form factor varies, nor does it construct a single symmetric form factor that makes all eight \(\gamma_i\) equal to an arbitrary prescribed value.

Their earlier paper arXiv:1911.04918 studies a different, simpler dispersion with a constant form factor and obtains a simultaneous lower/upper virtual-level point at \(\gamma=6\). That fixed-model result does not imply the present full-interval inverse-design statement for the later dispersion. The 2020 block-operator work arXiv:2011.09650 concerns a different one-/two-particle operator and discrete-spectrum counting rather than prescription of the generalized-Friedrichs synchronization parameter.

## Limitations
The theorem is an existence result. It does not give a closed elementary formula for \(\theta_*\) as a function of \(\gamma_*\), and it does not optimize the analytic form factor under additional norm, bandwidth, or locality constraints. It also makes no claim about simultaneous threshold behavior away from the nine extremal fibers.

## References
1. T. H. Rasulov and E. B. Dilmurodov, “Threshold analysis for a family of \(2\times2\) operator matrices,” Nanosystems: Physics, Chemistry, Mathematics 10(6) (2019), 616–622, DOI 10.17586/2220-8054-2019-10-6-616-622; arXiv:1912.09794v1.
2. T. H. Rasulov and E. B. Dilmurodov, “Eigenvalues and virtual levels of a family of \(2\times2\) operator matrices,” arXiv:1911.04918v1.
3. E. B. Dilmurodov, “Discrete Eigenvalues of a \(2\times2\) Operator Matrix,” arXiv:2011.09650v1.
