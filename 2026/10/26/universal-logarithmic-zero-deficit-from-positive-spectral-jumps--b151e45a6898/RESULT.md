# Universal logarithmic zero deficit from positive spectral jumps

## Finding
Let \(f(z)=\sum_{n\ge0}\xi_nz^n\) be a centered proper complex Gaussian analytic series whose coefficient sequence is stationary and has a strictly positive, piecewise \(C^2\) spectral density \(w\) on the unit circle. Assume finitely many distinct jump points \(\theta_j\), with positive one-sided limits \(w_{j,-},w_{j,+}\). Write \(\Delta_j=w_{j,+}-w_{j,-}\), and let \(N(r)\) count zeros of \(f\) in \(|z|<r\), with multiplicity. Then

\[
\boxed{\mathbb E N(r)=\frac{r^2}{1-r^2}-\frac{1}{4\pi^2}\left(\sum_j\frac{\Delta_j^2}{w_{j,-}w_{j,+}}\right)\log\frac{1}{1-r}+O(1)}
\qquad(r\uparrow1).
\]

In particular, every genuine positive jump produces a strictly positive logarithmic deficit, even though the spectral density has **no zeros**. The coefficient is additive over interfaces, unaffected by their locations, and invariant under rescaling \(w\) by a positive constant.

The same theorem gives a local boundary-interface law. Let \(\rho(z)\) be the expected zero intensity per unit Euclidean area, let \(\varepsilon=1-r\), and put
\[
W_j(x)=w_{j,-}+\Delta_j\left(\frac12+\frac1\pi\arctan x\right).
\]
For each jump \(\theta_j\), uniformly for \(x\) in compact subsets of \(\mathbb R\),
\[
\boxed{\pi(1-r^2)^2\rho\!\left(r e^{i(\theta_j+\varepsilon x)}\right)
\longrightarrow 1-\frac{\Delta_j^2}{\pi^2(1+x^2)W_j(x)^2}.}
\]
These two expressions are the global and local forms of one interface-energy law.

## Assumptions and scope
* The spectral measure of the two-sided coefficient process is \(w(\theta)d\theta/(2\pi)\). The process is proper/circular: \(\mathbb E[\xi_n\xi_m]=0\). Its covariance \(\mathbb E[\xi_n\overline{\xi_m}]\) is the Fourier transform of \(w\).
* \(w\) is periodic, real, satisfies \(0<m\le w(\theta)\le M<\infty\), and is \(C^2\) on each of finitely many open arcs, with bounded one-sided derivatives through the closures. Values assigned at jump points are immaterial. Every listed jump has \(\Delta_j\ne0\).
* \(\rho\) is the one-point expected complex zero density, not the intensity of real zeros or a zero-process convergence statement. No independence of the coefficient variables is assumed.
* The result is valid for arbitrarily small fixed positive jumps. The \(O(1)\) bound can depend on the spectral density. It is not claimed uniformly as the lower bound \(m\downarrow0\).

## Proof
**Step 1: covariance and the exact deficit identity.** Define the normalized Poisson extension
\[
u(r,\theta)=\frac1{2\pi}\int_{-\pi}^{\pi}\frac{1-r^2}{|e^{it}-re^{i\theta}|^2}w(t)\,dt.
\]
Stationarity gives
\[
K(z,z):=\mathbb E|f(z)|^2=\frac{u(z)}{1-|z|^2}.
\]
Since \(u\) is positive and harmonic, \(\Delta\log u=-|\nabla u|^2/u^2\). The Edelman–Kostlan identity therefore yields the **exact** formula
\[
\rho(z)=\frac{1}{\pi(1-|z|^2)^2}-\frac{|\nabla u(z)|^2}{4\pi u(z)^2}.
\tag{1}
\]
Let \(E(r)=\int_{-\pi}^{\pi}|\nabla u(re^{i\theta})|^2/u(re^{i\theta})^2\,d\theta\). Integrating (1) around a circle gives
\[
\frac{d}{dr}\left(\frac{r^2}{1-r^2}-\mathbb E N(r)\right)=\frac{r}{4\pi}E(r).
\tag{2}
\]
All quantities in (1)–(2) are finite for \(r<1\), by \(u\ge m\). In particular, no interchange at the singular boundary has been made.

**Step 2: separate the jumps from a Lipschitz remainder.** On the circle define the periodic sawtooth \(S_j(\theta)=(\theta-\theta_j\bmod2\pi)-\pi\); it has a jump of \(-2\pi\) at \(\theta_j\). Set \(J_j=-\Delta_jS_j/(2\pi)\). Then \(g=w-\sum_jJ_j\) is a continuous, globally Lipschitz periodic function. Writing \(v=P[g]\) for its Poisson extension, one has, for \(\varepsilon=1-r\downarrow0\),
\[
\sup_\theta|v(r,\theta)-g(\theta)|\le C\varepsilon\log\frac{e}{\varepsilon},
\qquad
\sup_\theta|\nabla v(r,\theta)|\le C\log\frac{e}{\varepsilon}.
\tag{3}
\]
For completeness, the first bound follows by inserting the Lipschitz modulus \(C|t|\) into the Poisson convolution. The tangential derivative is the Poisson integral of the bounded a.e. derivative \(g'\); its norm is bounded. Its radial derivative is the conjugate Poisson integral of \(g'\), whose kernel has \(L^1\) norm \(O(\log(e/\varepsilon))\). These arguments also establish (3) for piecewise \(C^1\) Lipschitz data.

The Poisson extension of the sawtooth is explicit:
\[
P[J_j](z)=-\frac{\Delta_j}{\pi}\operatorname{Im}\log(1-ze^{-i\theta_j}),
\tag{4}
\]
with the principal analytic logarithm on \(|z|<1\). Its gradient magnitude is \(|\Delta_j|/(\pi|1-ze^{-i\theta_j}|)\), as follows by differentiating the logarithm. Contributions from every other sawtooth are smooth and have uniformly bounded gradients in a fixed small arc around \(\theta_j\).

**Step 3: a uniform local interface estimate.** Fix \(\delta>0\) small enough that \(|\theta-\theta_j|<\delta\) contains no other jump. Put \(s=\theta-\theta_j\), \(\varepsilon=1-r\), and introduce the half-plane harmonic step profile
\[
U_j(\varepsilon,s)=\frac{w_{j,+}+w_{j,-}}2+\frac{\Delta_j}{\pi}\arctan\frac{s}{\varepsilon}=W_j(s/\varepsilon).
\tag{5}
\]
Equations (3)–(4), the expansion \(1-re^{is}=\varepsilon-is+O(\varepsilon|s|+s^2)\), and the Lipschitz property of the remaining boundary data imply the uniform bounds
\[
|u(re^{i(\theta_j+s)})-U_j(\varepsilon,s)|\le C\left(|s|+\varepsilon\log\frac e\varepsilon\right),
\tag{6}
\]
\[
|\nabla u(re^{i(\theta_j+s)})-\nabla U_j(\varepsilon,s)|
\le C\log\frac e\varepsilon.
\tag{7}
\]
In (7), both gradients are expressed in the same orthonormal polar frame: for the model the components are \((-\partial_\varepsilon U_j,\partial_s U_j)\), and for \(u\) they are \((\partial_r u,r^{-1}\partial_\theta u)\). The metric factor \(1/r=1+O(\varepsilon)\) adds only a uniformly bounded error. In the same coordinates,
\[
|\nabla U_j|^2=\frac{\Delta_j^2}{\pi^2(\varepsilon^2+s^2)},
\qquad U_j\ge m.
\tag{8}
\]
Both \(u\) and \(U_j\) are at least \(m\), so subtracting their normalized squared gradients and using (6)–(8) gives an integrable error bounded by a constant times
\[
\frac{\log(e/\varepsilon)}{\sqrt{\varepsilon^2+s^2}}
+\log^2\frac e\varepsilon
+\frac{|s|+\varepsilon\log(e/\varepsilon)}{\varepsilon^2+s^2}.
\]
The integral of this error over \(|s|<\delta\) is \(O(\log^2(e/\varepsilon))\). On the complementary arcs, (3)–(4) give the same bound for the integral of the complete energy. Consequently,
\[
E(r)=\sum_j\frac{\Delta_j^2}{\pi^2}\int_{-\delta}^{\delta}
\frac{ds}{(\varepsilon^2+s^2)W_j(s/\varepsilon)^2}
+O\left(\log^2\frac e\varepsilon\right).
\tag{9}
\]
Notice that (9) is an infinite-family analytic estimate, not an inference from numerical sampling.

**Step 4: evaluate the universal interface mass.** Substitute \(s=\varepsilon x\) and then \(t=\tfrac12+\pi^{-1}\arctan x\). The omitted tails \(|x|>\delta/\varepsilon\) contribute \(O(1)\) to (9), and
\[
\int_{\mathbb R}\frac{dx}{(1+x^2)W_j(x)^2}
=\pi\int_0^1\frac{dt}{(w_{j,-}+\Delta_jt)^2}
=\frac{\pi}{w_{j,-}w_{j,+}}.
\tag{10}
\]
Thus
\[
E(r)=\frac{1}{\pi(1-r)}\sum_j\frac{\Delta_j^2}{w_{j,-}w_{j,+}}
+O\left(\log^2\frac{e}{1-r}\right).
\tag{11}
\]
The error in (11) is integrable in \(r\) at one. Substituting into (2) and integrating from a fixed interior radius to \(r\) proves the stated logarithmic asymptotic with a **bounded remainder**.

**Step 5: local density.** For fixed \(x\), (6)–(8) imply \(u\to W_j(x)\) and \(\varepsilon^2|\nabla u|^2\to\Delta_j^2/[\pi^2(1+x^2)]\) at \(\theta=\theta_j+\varepsilon x\). These limits are compact-uniform in \(x\). Since \((1-r^2)^2/(4\varepsilon^2)\to1\), (1) gives the claimed interface profile.

## Verification
The independent numerical corroboration program `check_jump_zeros.py` uses explicit two-arc Poisson extensions and direct quadrature. It tests jump ratios \(1:2\), \(1:4\), \(3:1\), and the equal-height control, both jump locations, several boundary scales, the energy coefficient, the local intensity profile, and boundedness of the log-subtracted disk deficit. All **120 assertions** passed in the documented run. These computations are finite corroboration only; the proof of (9)–(11) is analytical.

One exact test model is \(w=a\) on the upper semicircle and \(w=b\) on the lower semicircle, with \(a,b>0\). Its Poisson extension is
\[
u(z)=\frac{a+b}{2}+\frac{a-b}{\pi}\operatorname{Im}\log\frac{1+z}{1-z},
\quad |\nabla u(z)|^2=\frac{4(a-b)^2}{\pi^2|1-z^2|^2}.
\]
There are two jumps, and the logarithmic deficit coefficient is exactly \((a-b)^2/(2\pi^2ab)\). Both the exact model and the general theorem are invariant under positive rescaling of \(w\).

## Relationship to prior work
Noda and Shirai (arXiv:2106.02860, first posted June 5, 2021) derived the covariance/expected-zero framework and sharp disk-count asymptotics for **finitely dependent** coefficients, whose spectral densities are trigonometric polynomials. Their strictly positive trigonometric-polynomial examples have bounded corrections, while vanishing spectral densities can give fractional-power corrections. The present theorem supplies an additional **positive but discontinuous** spectral regime and calculates the complete logarithmic interface coefficient; their formulas do not state that regime.

Shirai (arXiv:2501.02586, 2025) analyzes **fixed radial directions** whose spectral density is smooth in a neighborhood of the direction, including directions inside a spectral gap. It presents a piecewise-constant support example, but its fixed-direction formulas do not give the joint tangential–radial jump profile or the disk-integrated logarithmic deficit for strictly positive interfaces. The general Poisson/correlation representation in that work is consistent with (1), not a statement of (9)–(11).

A separate half-Sobolev/logarithmic jump law for truncated double-Hilbert operators concerns a different functional, not Gaussian analytic zero counts. A proof of the present theorem requires the nonlinear reciprocal Poisson weight in (10); matching the words “jumps” and “logarithm” does not imply this coefficient.

## Limitations
This is a one-point expectation theorem for spectral densities uniformly bounded away from zero. It does not treat vanishing one-sided limits, infinitely many jumps, spectral atoms, varying jump heights as \(r\uparrow1\), zero-count variance, or convergence of the full zero point process. The result's novelty is judged against the specifically inspected literature; an unindexed equivalent result or an unstated consequence of a more general nonlinear Poisson-energy theorem remains a historical-priority risk. Independent mathematical validation has not been performed.

## References
1. K. Noda and T. Shirai, “Expected Number of Zeros of Random Power Series with Finitely Dependent Gaussian Coefficients,” arXiv:2106.02860 (first version June 5, 2021); *Journal of Theoretical Probability* 36 (2023), 1534–1554, DOI:10.1007/s10959-022-01203-y. https://arxiv.org/abs/2106.02860
2. T. Shirai, “The density of zeros of random power series with stationary complex Gaussian coefficients,” arXiv:2501.02586 (2025). https://arxiv.org/abs/2501.02586
3. Edelman–Kostlan expected-zero identity, as recalled in Noda and Shirai, Proposition 2.1 (reference 1).
