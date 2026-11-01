# Quadratic Arnold-tongue onset from complementary Fourier harmonics

## Finding

For every coprime pair of integers \(1\le p<q\), \(q\ge3\), a perturbation of a circle rotation by exactly two **complementary** Fourier harmonics has a rational mode-locking tongue that opens quadratically rather than at the high order familiar from a single low-frequency sine forcing. More precisely, if the frequencies \(m,n\) are distinct and satisfy \(m+n=q\), its leading width is
\[
\omega_+(\varepsilon)-\omega_-(\varepsilon)
=\pi|AB|\sqrt{q^2+(n-m)^2\cot^2(\pi pm/q)}\,\varepsilon^2
+O(|\varepsilon|^3).
\]
This coefficient never vanishes for nonzero amplitudes and is independent of both Fourier phases. The center is shifted at second order by \(\frac\pi2(mA^2-nB^2)\cot(\pi pm/q)\,\varepsilon^2\). For every odd denominator, complementary frequencies are also **necessary** for a nonzero quadratic-order width among all two-harmonic forcings with distinct positive frequencies below that denominator.

The smallest example, \(p/q=1/3\) with frequencies \(1\) and \(2\), has width \(\pi|AB|\sqrt{28/3}\,\varepsilon^2+O(|\varepsilon|^3)\). It specializes to a weak-forcing parameter slice of the two-harmonic sine-circle map in reference [1].

## Assumptions and scope

Let \(q\ge3\) be an integer, \(p\in\{1,\dots,q-1\}\) with \(\gcd(p,q)=1\), and let \(1\le m,n<q\) be **distinct** positive integers satisfying \(m+n=q\). Fix real \(A,B\ne0\) and arbitrary real phase angles \(\phi,\psi\). Put
\[
h(x)=A\sin(2\pi mx+\phi)+B\sin(2\pi nx+\psi),\qquad
F_{\omega,\varepsilon}(x)=x+\omega+\varepsilon h(x).
\]
The map is understood modulo one on the circle, but \(F\) always denotes the displayed real lift. For sufficiently small \(|\varepsilon|\), \(1+\varepsilon h'(x)>0\) at every point; hence the circle map is an orientation-preserving analytic diffeomorphism. Its lifted rotation number is \(\rho(F)=\lim_{k\to\infty}(F^k(x)-x)/k\), independent of \(x\). Define the exact local locking interval \(I_{p/q}(\varepsilon)=\{\omega:\rho(F_{\omega,\varepsilon})=p/q\}\). Its two endpoints are \(\omega_-(\varepsilon)\le\omega_+(\varepsilon)\), near \(p/q\) for small forcing.

The error \(O(|\varepsilon|^3)\) is for each fixed choice of the discrete and real parameters; it is not asserted uniformly as \(q\to\infty\), nor when the amplitudes themselves vary with \(\varepsilon\).

## Proof

**1. A uniform return expansion.** Set \(r=p/q\) and \(\omega=r+\delta\). Write the unperturbed orbit as \(x_j=x+jr\). Ordinary Taylor expansion through the \(q\)-fold composition gives, uniformly in \(x\) as \((\delta,\varepsilon)\to(0,0)\),
\[
F_{r+\delta,\varepsilon}^{q}(x)-x-p
=q\delta+\varepsilon\sum_{j=0}^{q-1}h(x+jr)
+\varepsilon^2 S_2(x)
+O(|\varepsilon|^3+|\delta\varepsilon|+\delta^2),
\]
where
\[
S_2(x)=\sum_{0\le i<j<q}h'(x+jr)h(x+ir).
\]
Since neither of the two forcing frequencies is divisible by \(q\), the first-order sum is identically zero. We will only use the expansion for \(\delta=O(\varepsilon^2)\); the remainder is then \(O(|\varepsilon|^3)\), uniformly also in the first two spatial derivatives.

**2. Exact resonant Fourier selection.** Put \(\zeta=e^{2\pi ip/q}\). Expand \(h(x)=\sum_k c_ke^{2\pi ikx}\), with frequencies \(k\in\{\pm m,\pm n\}\), and coefficients
\[
c_m=\frac{Ae^{i\phi}}{2i},\quad c_{-m}=-\frac{Ae^{-i\phi}}{2i},\quad
c_n=\frac{Be^{i\psi}}{2i},\quad c_{-n}=-\frac{Be^{-i\psi}}{2i}.
\]
For a pair of frequencies \(k,\ell\) with \(0<|k|,|\ell|<q\), its contribution to the coefficient of \(e^{2\pi i(k+\ell)x}\) in \(S_2\) is
\[
2\pi ikc_kc_\ell\sum_{j=0}^{q-1}\zeta^{kj}\sum_{i=0}^{j-1}\zeta^{\ell i}
= -\frac{2\pi iqk c_kc_\ell}{1-\zeta^\ell}
\mathbf{1}_{\{q\mid(k+\ell)\}}.
\]
The equality uses the finite geometric sum and \(\sum_{j=0}^{q-1}\zeta^{kj}=0\). Therefore **only** resonant total frequencies divisible by \(q\) survive. Given \(m+n=q\) and \(m\ne n\), the possible ones are \(0,\pm q\). Let \(c=\cot(\pi pm/q)\). The identity \(\frac1{1-e^{i\theta}}=\frac12+\frac i2\cot(\theta/2)\) yields
\[
S_2(x)=C_0+C_qe^{2\pi iqx}+\overline{C_q}e^{-2\pi iqx},
\]
where
\[
C_0=-\frac{\pi q}2(mA^2-nB^2)c,
\qquad C_q=\frac{\pi qAB}{4}\bigl[-(n-m)c+iq\bigr]e^{i(\phi+\psi)}.
\]
Consequently,
\[
|C_q|=\frac{\pi q|AB|}{4}\sqrt{q^2+(n-m)^2c^2}>0.
\]
The terms depending on the phases merely rotate the nonconstant harmonic: its amplitude is phase-independent.

**3. Exact plateau endpoints from return zeros.** For each fixed \(x\) and sufficiently small forcing, the equation \(F_{\omega,\varepsilon}^q(x)=x+p\) has a unique smooth solution \(\omega=\Omega_\varepsilon(x)\) close to \(p/q\). Indeed \(\partial_\omega F^q=q+O(\varepsilon)>0\). By the preceding expansion and the implicit-function theorem,
\[
\Omega_\varepsilon(x)=\frac pq-\frac{\varepsilon^2}q S_2(x)+O(|\varepsilon|^3)
\]
uniformly in \(x\). An orientation-preserving circle homeomorphism has rotation number \(p/q\) exactly when its lift has a point satisfying \(F^q(x)=x+p\). Thus \(I_{p/q}(\varepsilon)\) is exactly the image of \(x\mapsto\Omega_\varepsilon(x)\), a closed interval, and its endpoints are the minimum and maximum of that continuous function. Since the extrema of \(S_2\) are \(C_0\pm2|C_q|\), one obtains
\[
\boxed{\omega_\pm(\varepsilon)=\frac pq+\frac\pi2(mA^2-nB^2)c\,\varepsilon^2
\pm\frac{\pi|AB|}2\sqrt{q^2+(n-m)^2c^2}\,\varepsilon^2+O(|\varepsilon|^3).}
\]
Subtracting proves the width law. For fixed detuning strictly inside the leading second-order endpoint coefficients, the return map has \(2q\) simple fixed points, comprising one attracting and one repelling period-\(q\) orbit. The nondegenerate sine-wave extrema give the usual local saddle-node tongue boundaries.

**4. Converse selection for odd denominators.** Now let \(q\ge3\) be odd, and allow arbitrary distinct \(1\le m<n<q\) with nonzero real amplitudes. The return expansion and Fourier geometric-sum identity are unchanged. Frequencies in the quadratic return can have absolute values at most \(2q-2\); a nonconstant resonant term at order two therefore requires a signed pair of input frequencies summing to \(\pm q\). A same-frequency pair cannot sum to \(\pm q\) because \(q\) is odd. A mixed pair can do so exactly when \(m+n=q\), since \(|m-n|<q\). In the complementary case, its coefficient \(C_q\) above is always nonzero; otherwise the quadratic return is constant in space, so \(\omega_+(\varepsilon)-\omega_-(\varepsilon)=O(|\varepsilon|^3)\). This establishes the claimed if-and-only-if selection rule for **positive quadratic leading width**. It makes no assertion about a possible cubic or higher-order leading term when the complementary resonance is absent.

## Verification

The included `CHECK.py` is self-contained Python using the standard library. Running `python CHECK.py` performs 306 numerical tests across seven different reduced rational rotations, varied frequencies, signs and phase angles. It independently compares the finite-sum quadratic return with its Fourier coefficient formula at 41 points per setting, verifies cubic-order residual decrease upon halving forcing, and locates actual fixed-point detuning thresholds by bisection on 600 spatial points in five settings. No floating-point computation is used to prove the asymptotic theorem: the proof is the exact finite-Fourier calculation and the implicit-function argument above.

## Relationship to prior work

Mugnaine, Sales, Szezech and Viana [1] introduce and study the two-harmonic sine-circle nontwist map \(x\mapsto x+\alpha-\beta\sin(2\pi x)+\gamma\cos(4\pi x)\). Their full paper derives the model and studies numerical dynamical regimes, bifurcations and multistability. The case \(q=3,m=1,n=2\) above supplies a new explicit local rational-locking width along the weak-forcing slice \(\phi=0\), \(\psi=\pi/2\), \(\beta=-\varepsilon A\), \(\gamma=\varepsilon B\), which is not given by their stated bifurcation formulas. Standard Arnold-family resonance tongues, the computational Taylor-expansion methods of Luque and Villanueva [2], and Boyland's generic pinching theory [3] are established background. Unlike [2]'s irrational-rotation expansion and [3]'s no-pinching result, the present theorem identifies an explicit, positive **rational** width coefficient, its arithmetic numerator dependence, and the odd-denominator two-frequency selection rule. These are specific coefficient and structure calculations within a well-developed perturbation theory, not a claim that second-order normal forms or Arnold tongues themselves are newly discovered.

## Limitations

The results are local as \(\varepsilon\to0\) for fixed \(q,p,m,n,A,B,\phi,\psi\); uniformity in increasing denominator is not asserted. The odd-denominator converse establishes the order of the first potentially nonzero term but does not classify higher-order resonances. Analyticity and orientation preservation can fail outside the weak-forcing range; nothing is claimed there. No comprehensive historical priority determination or independent scientific audit is provided. General normal-form literature may permit the explicit coefficient to be derived by specialization, and priority for the exact expression remains subject to further expert review.

## References

[1] M. Mugnaine, M. R. Sales, J. D. Szezech Jr., and R. L. Viana, “Dynamics, multistability, and crisis analysis of a sine-circle nontwist map,” *Physical Review E* **106** (2022), 034203. DOI: 10.1103/PhysRevE.106.034203. Published 2022-09-06. Author-hosted full text: https://fisica.ufpr.br/viana/artigos/2022/PhysRevE.106.034203.pdf.

[2] A. Luque and J. Villanueva, “Computation of derivatives of the rotation number for parametric families of circle diffeomorphisms,” *Physica D* **237** (2008), 2599–2615. Public author-manuscript text: https://web.ma.utexas.edu/mp_arc/c/09/09-180.pdf

[3] P. Boyland, “Pinched Arnol’d tongues for families of circle maps,” arXiv:2506.02988v1 (2025). Full open version: https://arxiv.org/html/2506.02988v1.
