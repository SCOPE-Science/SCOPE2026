# Clock-resolution frontier for harvesting telegraph-noise qubit capacity

## Finding

For a qubit exposed to stationary symmetric random-telegraph dephasing, a single ideal rotation about the \(x\)-axis can preserve a nonzero long-time battery capacity. The preservation becomes sharply dependent on pulse-clock uncertainty as the noise coupling increases. With a clock error independent of the telegraph noise and unknown to a fixed-angle controller, Gaussian jitter of standard deviation \(\sigma_\nu\) has the limiting normalized optimized capacity
\[
\lim_{\nu\to\infty}\frac{B_\nu(\sigma_\nu)}{2\varepsilon}
=H\exp(-s^2/2),\qquad
s=\lim_{\nu\to\infty}\sqrt{4\nu^2-\xi^2}\,\sigma_\nu,
\]
provided \(\sigma_\nu\to0\), with the convention \(\exp(-\infty)=0\). Here \(\omega=2\varepsilon\),
\[
 t_H=\omega^{-1}\arctan(\omega/\xi),\qquad
 H=\frac{\omega}{\sqrt{\xi^2+\omega^2}}e^{-\xi t_H}>0.
\]
If the actual pulse time is observed and the pulse's sign may be selected accordingly, the corresponding limit is \(H b(s)\), where
\[
 b(s)=\max_{\varphi\in[0,\pi]}\mathbb E\bigl|\cos(\varphi+sZ)\bigr|,
 \qquad Z\sim N(0,1),\quad b(\infty)=2/\pi.
\]
In particular, for \(\sigma_\nu=a/\nu\), the blind-controller suppression factor is exactly \(e^{-2a^2}\); if \(\sigma_\nu\to0\) while \(\nu\sigma_\nu\to\infty\), blind-control capacity tends to zero but timing-informed capacity tends to \(2H/\pi\) after normalization. At every finite \(s>0\), \(b(s)>e^{-s^2/2}\). For each fixed \(\sigma>0\), blind optimized capacity vanishes as \(\nu\to\infty\), while timing-informed optimized capacity converges to an explicit strictly positive Gaussian-smoothed envelope given below. This is a statement about the capacity of the **ensemble-averaged terminal state**, not the average of individual-shot capacities.

## Assumptions and scope

Let \(\varepsilon,\xi>0\), let \(\nu>\xi/2\), and let \(c(t)\in\{-1,1\}\) be a stationary, symmetric, continuous-time Markov chain that switches sign at rate \(\xi\), initially independent of the qubit. The noisy Hamiltonian is
\[
 H(t)=(\varepsilon+\nu c(t))\sigma_z.
\]
The qubit starts in \(\lvert+\rangle=(\lvert0\rangle+\lvert1\rangle)/\sqrt2\). Its bare battery Hamiltonian is \(H_0=\varepsilon\sigma_z\). An instantaneous control \(U_\theta=\exp(-i\theta\sigma_x)\) is applied once at
\[
 T=\max\{0,t_0+\sigma Z\},\qquad t_0\ge0,
\]
where the standard Gaussian \(Z\) is independent of the qubit and noise. Negative proposed times are clipped to zero (a pulse at zero does not change this particular initial state for the relevant capacity observable). All free dynamics after the pulse are left uninterrupted and the terminal time tends to infinity. No bound on pulse-angle switching speed is assumed.

For **blind control**, \(\theta\) is a fixed constant and cannot depend on the realization of \(T\). For **time-informed control**, \(\theta=\theta(T)\) is measurable in the observed actual pulse time but does not depend on the instantaneous telegraph state. In each class both \(t_0\) and the permitted angles are optimized. The final mixed state is first averaged over the independent pulse-clock randomness and telegraph trajectories, and its qubit capacity is then calculated as \(\mathcal C(\rho;H_0)=2\varepsilon\lVert\boldsymbol r\rVert\), where \(\boldsymbol r\) is the Bloch vector. These idealized controls change neither the noise law nor the qubit's free Hamiltonian.

## Proof

**1. Exact telegraph coherence.** Let \(G_\nu(t)=\mathbb E\exp(2i\nu\int_0^t c(u)\,du)\). The conditional characteristic functions of the two noise states obey a two-by-two constant-coefficient linear system. Taking their sum and using the stationary unbiased initialization gives
\[
 G_\nu''+2\xi G_\nu'+4\nu^2G_\nu=0,
 \qquad G_\nu(0)=1,\quad G_\nu'(0)=0.
\]
With \(\delta=\sqrt{4\nu^2-\xi^2}\), its unique solution is
\[
 G_\nu(t)=e^{-\xi t}\left[\cos(\delta t)+\frac{\xi}{\delta}\sin(\delta t)\right]
 =R_\delta e^{-\xi t}\cos(\delta t-\phi_\delta),
\]
where \(R_\delta=\sqrt{1+\xi^2/\delta^2}\) and \(\phi_\delta=\arctan(\xi/\delta)\).

**2. Exact terminal pulse observable.** Before the pulse the average Bloch components are \((G_\nu(t)\cos(\omega t),G_\nu(t)\sin(\omega t),0)\), with \(\omega=2\varepsilon\). A rotation about \(x\) by Bloch angle \(2\theta\) produces longitudinal component \(G_\nu(t)\sin(\omega t)\sin(2\theta)\). Longitudinal components are exactly conserved by every subsequent realization of the diagonal Hamiltonian. Transverse conditional components decay at long times because the nonzero complex eigenvalues of the coupled telegraph-coherence generator have real part \(-\xi\). Dominated convergence handles the finite almost-sure random pulse time. Therefore the averaged terminal state is diagonal, and
\[
 \mathcal C_\infty(t_0,\theta,\sigma)
 =2\varepsilon\left|\mathbb E\left[G_\nu(T)\sin(\omega T)\sin(2\theta(T))\right]\right|.
\]
Define the two exactly optimized capacities
\[
 \begin{split}
 B_\nu(\sigma)&=2\varepsilon\sup_{t_0\ge0}\bigl|\mathbb E[G_\nu(T)\sin(\omega T)]\bigr|,\\
 F_\nu(\sigma)&=2\varepsilon\sup_{t_0\ge0}\mathbb E\bigl|G_\nu(T)\sin(\omega T)\bigr|.
 \end{split}
\]
For blind control, \(\lvert\sin(2\theta)\rvert=1\) is optimal. For informed control, choosing \(\sin(2\theta(T))\) equal to the sign of \(G_\nu(T)\sin(\omega T)\) attains the absolute-value average. This uses only the observed time and known model parameters, not the telegraph trajectory.

**3. Global slow envelope.** Extend \(h(t)=e^{-\xi t}\sin(\omega t)\) by zero to negative \(t\), and write \(u(t)=\lvert h(t)\rvert\). These functions are globally Lipschitz, with Lipschitz constant at most \(L=\sqrt{\omega^2+\xi^2}\), and \(\sup_{t\ge0}u(t)=H\). Indeed, the unique largest lobe peak occurs at \(t_H=\arctan(\omega/\xi)/\omega\); later peaks are its successive multiples of \(e^{-\xi\pi/\omega}\). For any desired phase modulo \(\pi\), a nominal time within \(\pi/(2\delta)\) of \(t_H\) achieves that phase for the cosine factor. Consequently,
\[
 \sup_{t\ge0}\lvert h(t)\cos(\delta t-\phi_\delta)\rvert=H+O(\delta^{-2}),
\]
with constants depending only on \(\varepsilon,\xi\). The bound follows from global \(u\le H\) and Taylor expansion at the nondegenerate maximum \(t_H\), not from a finite scan of oscillations.

**4. Exact Gaussian-clock filtering.** Put \(s_\nu=\delta\sigma_\nu\). The Gaussian characteristic identity gives
\[
 \mathbb E\cos(\delta(t_0+\sigma Z)-\phi_\delta)
 =e^{-\delta^2\sigma^2/2}\cos(\delta t_0-\phi_\delta).
\]
Since \(h(t)=0\) for negative times, replacing \(h(t_0+\sigma Z)\) by \(h(t_0)\) in the expectation incurs a **uniform** error at most \(L\sigma\mathbb E\lvert Z\rvert=L\sigma\sqrt{2/\pi}\). It follows that, whenever \(\sigma_\nu\to0\),
\[
 \frac{B_\nu(\sigma_\nu)}{2\varepsilon}
 =R_\delta H e^{-s_\nu^2/2}+O(\sigma_\nu+\delta^{-2}).
\]
The big-O is absolute and uniform even when \(s_\nu\to\infty\). This proves the blind-control limit.

For time-informed control the corresponding uniform estimate is
\[
 \frac{F_\nu(\sigma_\nu)}{2\varepsilon}
 =R_\delta H\,b(s_\nu)+O(\sigma_\nu+\delta^{-2}),
\]
where \(b(s)=\max_{\varphi\in[0,\pi]}\mathbb E\lvert\cos(\varphi+sZ)\rvert\). The upper bound follows from \(u\le H\). For the lower bound choose a phase maximizing \(b(s_\nu)\) and a nominal time of that phase within \(\pi/(2\delta)\) of \(t_H\); Taylor's theorem gives \(u(t_0)=H+O(\delta^{-2})\). These bounds hold uniformly in the phase and in \(s_\nu\).

The periodic absolutely convergent Fourier series
\[
 \lvert\cos y\rvert=\frac2\pi+\frac4\pi\sum_{k=1}^{\infty}
 \frac{(-1)^{k-1}}{4k^2-1}\cos(2ky)
\]
shows
\[
 b(s)=\max_{\varphi\in[0,\pi]}\left\{\frac2\pi+\frac4\pi\sum_{k=1}^{\infty}
 \frac{(-1)^{k-1}}{4k^2-1}e^{-2k^2s^2}\cos(2k\varphi)\right\}.
\]
This yields \(b(0)=1\) and \(b(s)\to2/\pi\) as \(s\to\infty\), uniformly in \(\varphi\). For any \(s>0\), \(b(s)\ge\mathbb E\lvert\cos(sZ)\rvert>\lvert\mathbb E\cos(sZ)\rvert=e^{-s^2/2}\), because the Gaussian phase has positive probability of both signs. With \(\delta/\nu\to2\), the \(\sigma_\nu=a/\nu\) and intermediate-jitter statements follow.

**5. Fixed nonzero clock uncertainty.** For each \(\sigma>0\), let \(k_\sigma(t-x)\) denote the Gaussian density in \(t\) centered at \(x\). The oscillatory integrals of \(h(t)k_\sigma(t-x)\) admit a uniform integration-by-parts bound \(O((\delta\sigma)^{-1})\), because \(h(0)=0\), the function \(h\) and its derivative are integrable, \(\sup k_\sigma=(\sqrt{2\pi}\sigma)^{-1}\), and \(\int\lvert k_\sigma'\rvert=\sqrt{2/\pi}/\sigma\). Hence \(B_\nu(\sigma)\to0\). Using the absolutely summable Fourier series for \(\lvert\cos\rvert\), applying the same uniform estimate to each nonconstant harmonic, and passing through the uniformly summable series gives
\[
 \lim_{\nu\to\infty}\frac{F_\nu(\sigma)}{2\varepsilon}
 =\frac2\pi\sup_{t_0\ge0}\mathbb E\bigl[u(t_0+\sigma Z)\bigr]>0.
\]
This verifies the fixed-width, blind-versus-informed distinction without any assumption that the clock width shrinks.

## Verification

Run `python verify.py` with Python, NumPy and SciPy. The standalone code independently exponentiates the two conditional telegraph generators, compares density-matrix pulse rotations with the analytic \(G_\nu\) expression, checks the Gaussian convolution error bound over several parameter families, tests near-revival scheduling, and evaluates the timing-adaptation Fourier factor. Its tests are bounded numerical corroboration. The ODE reduction, global optimization and Fourier/analytic estimates in the proof establish the continuum and strong-coupling claims.

For \(\xi=\omega=1\), the slow-envelope value is \(H=e^{-\pi/4}/\sqrt2\approx0.32239694\). In the intermediate regime \(\sigma_\nu\to0\), \(\nu\sigma_\nu\to\infty\), the asymptotic blind normalized value is zero, whereas the informed normalized value is \(2H/\pi\approx0.20524427\).

## Relationship to prior work

The exact stationary telegraph dephasing family and its Markovian/non-Markovian transition appear in Hadipour (2025), and the importance of choosing error-correction times under telegraph noise appears in Udupa et al. (2025). Those studies do not supply the mixed-output pulse-clock frontier or the time-informed versus blind capacity separation proved here. Jiang et al. (publicly posted 2026-10-28) give the deterministic single-\(x\)-pulse retained-capacity expression in this model; that deterministic identity is explicitly prior work, not a new claim here. The new statement adds independent Gaussian pulse-time uncertainty, optimizes before mixing the terminal state, and distinguishes two information classes with sharp joint coupling–precision limits. Earlier echo/control-precision studies by Cywiński et al., Hodgson et al. and Heshami et al. address different pulse sequences and dephasing objectives. General Gaussian characteristic-function filtering and Fourier averaging are standard mathematical tools and are not claimed as new.

## Limitations

The theorem assumes symmetric stationary telegraph noise, a pure equatorial input state, one ideal instantaneous \(x\)-pulse, Gaussian independent timing jitter, and arbitrarily late readout. A time-informed controller is assumed to know the actual clock time accurately enough to choose an angle with arbitrarily fast sign changes; bounded electronic bandwidth could remove its advantage. A different noise initialization, pulse axis, finite terminal time or non-Gaussian jitter can change the profile. Capacity is a unitary-orbit energy range and is **not** the net energetic work after accounting for the pulse hardware. The result is an exact model theorem, not an experimental prediction with calibrated device parameters. Publication-priority comparisons are based on accessible literature, not an independent novelty certification.

## References

1. M. Hadipour, *Quantum Speed Limits in Qubit Dynamics Driven by Bistable Random Telegraph Noise: From Markovian to Non-Markovian Regimes*, arXiv:2504.15808, first posted 2025-04-22, https://arxiv.org/abs/2504.15808.
2. A. Udupa et al., *Performance of rotation-symmetric bosonic codes in the presence of random telegraph noise*, arXiv:2505.08670, first posted 2025-05-13, https://arxiv.org/abs/2505.08670.
3. J.-L. Jiang et al., *Harnessing Non-Markovian Memory for Quantum-Battery Capacity*, arXiv:2610.38527, first posted 2026-10-28, https://arxiv.org/abs/2610.38527. Deterministic one-pulse capacity is prior work.
4. Ł. Cywiński et al., *How to enhance dephasing time in superconducting qubits*, arXiv:0712.2225, first posted 2007-12-13, https://arxiv.org/abs/0712.2225.
5. T. E. Hodgson, L. Viola and I. D'Amico, *Towards optimized suppression of dephasing in systems subject to pulse timing constraints*, arXiv:0912.2035, first posted 2009-12-10, https://arxiv.org/abs/0912.2035.
6. K. Heshami et al., *Precision requirements for spin-echo based quantum memories*, arXiv:1012.0544, first posted 2010-12-02, https://arxiv.org/abs/1012.0544.
