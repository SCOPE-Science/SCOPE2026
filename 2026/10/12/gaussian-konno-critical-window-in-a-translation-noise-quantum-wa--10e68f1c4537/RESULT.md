# Gaussian–Konno critical window in a translation-noise quantum walk

## Finding

Fix a coin angle \(0<\theta<\pi/2\). In the unmonitored discrete-time quantum stochastic walk on \(\mathbb Z\) described below, let \(p_t\in[0,1]\) be the probability of a coin-independent symmetric classical spatial shift at each of \(t\) steps, and write \(q_t=1-p_t\). Let \(X_t\) be the position measured only after all \(t\) steps. Let \(Z\) be standard normal, independent of the random variable \(V_\theta\) with density
\[
f_\theta(v)=\frac{\sin\theta}{\pi(1-v^2)\sqrt{\cos^2\theta-v^2}}\,\mathbf 1_{\{|v|<\cos\theta\}}.
\]
The following trichotomy holds for every sequence of probabilities \((p_t)_{t\ge1}\):

1. If \(q_t\sqrt t\to0\), then \(X_t/\sqrt t\Rightarrow Z\).
2. If \(q_t\sqrt t\to\lambda\in(0,\infty)\), then
\[
\frac{X_t}{\sqrt t}\Rightarrow Z+\lambda V_\theta.
\]
3. If \(q_t\sqrt t\to\infty\), then
\[
\frac{X_t}{tq_t}\Rightarrow V_\theta.
\]

Thus the sharp crossover scale is \(1-p_t\asymp t^{-1/2}\). Within its finite positive window, the limiting density is the explicitly specified Gaussian–Konno convolution
\[
h_{\lambda,\theta}(x)=\int_{-\cos\theta}^{\cos\theta}
\frac{e^{-(x-\lambda v)^2/2}}{\sqrt{2\pi}}\,f_\theta(v)\,dv.
\]
It has variance \(1+\lambda^2(1-\sin\theta)\) and **strictly negative fourth cumulant**
\[
\kappa_4(Z+\lambda V_\theta)
=-\frac{\lambda^4}{2}(1-\sin\theta)^2(4-\sin\theta)<0.
\]
Consequently the critical law is non-Gaussian for every \(\lambda>0\) and every stated coin angle. The endpoint \(\lambda=0\) is exactly Gaussian.

A stronger finite-time statement underlies all three limits. If \(Q_k\) denotes the position after \(k\) steps of the corresponding *pure* coined quantum walk, \(K_t\sim\operatorname{Bin}(t,q_t)\), and \(S_j\) denotes an independent symmetric simple random walk after \(j\) steps, then
\[
X_t\overset{\mathrm d}=Q_{K_t}+S_{t-K_t},
\]
where, conditional on \(K_t=k\), the pure-walk variable \(Q_k\) and the random-walk variable \(S_{t-k}\) are independent. This identity holds for every integer \(t\ge0\), every \(p_t\in[0,1]\), and the stated initial coin state, without any asymptotic approximation.

## Assumptions and scope

Take \(\mathcal H=\mathbb C^2\otimes\ell^2(\mathbb Z)\) with coin basis \(\{|R\rangle,|L\rangle\}\). Define right translation \(T|x\rangle=|x+1\rangle\), coin
\[
C_\theta=\begin{pmatrix}\cos\theta&\sin\theta\\\sin\theta&-\cos\theta\end{pmatrix},
\]
and conditional-shift unitary
\[
U_\theta=(|R\rangle\langle R|\otimes T+|L\rangle\langle L|\otimes T^{-1})(C_\theta\otimes I).
\]
The initial state is \(|\psi_0\rangle=(|R\rangle+i|L\rangle)\otimes|0\rangle/\sqrt2\). Its relative imaginary coin phase makes the coherent-walk position law symmetric. For fixed probability \(p\) during a given \(t\)-step experiment, evolve by the trace-preserving quantum channel
\[
\mathcal E_p(\rho)=(1-p)U_\theta\rho U_\theta^\dagger
+\frac p2 (I\otimes T)\rho(I\otimes T^{-1})
+\frac p2 (I\otimes T^{-1})\rho(I\otimes T).
\]
Read out position at time \(t\), tracing over the coin. No intermediate position measurement or absorbing return test is made. The parameter \(p=p_t\) may change *between* experiments of different lengths, but is fixed across the \(t\) steps of each experiment. Position steps are on the infinite line, with no reflecting or periodic boundary.

## Proof

**Exact finite-time decomposition.** Write \(R=I\otimes T\), so \(R\) commutes with \(U_\theta\) and \(R^{-1}\): spatially homogeneous conditional shifts commute with global translations, as does \(C_\theta\otimes I\). A Kraus trajectory of length \(t\) is a word made of \(U_\theta,R,R^{-1}\). Every word with \(k\) coherent letters reduces, by commutation, to \(R^s U_\theta^k\), where \(s\) is the sum of the signs of its \(t-k\) stochastic letters. Summing probabilities of all these words gives the binomial weight \(\binom tk(1-p)^kp^{t-k}\) and an independent, symmetric \((t-k)\)-step displacement. Since the shift is coin-independent, the conditional position law is the convolution of the pure \(k\)-step quantum position distribution with the classical displacement distribution. This proves the exact identity and, equivalently, the reproducible formula
\[
\Pr\{X_t=x\}=\sum_{k=0}^{t}\binom tk q_t^kp_t^{t-k}
\sum_{j=0}^{t-k}2^{-(t-k)}\binom{t-k}{j}
\Pr\{Q_k=x-2j+(t-k)\}.
\]
At endpoints interpret the binomial terms by their probability laws, so no ambiguous convention about \(0^0\) is required.

**Coherent velocity law.** Spatial Fourier transformation diagonalizes the translation-invariant walk into
\[
U_\theta(k)=\operatorname{diag}(e^{ik},e^{-ik})C_\theta,
\quad -\pi\le k<\pi.
\]
Its eigenvalues are \(e^{i\omega(k)}\) and \(-e^{-i\omega(k)}\), with \(\sin\omega(k)=\cos\theta\sin k\). Their group velocities are \(\pm v(k)\), where
\[
v(k)=\frac{\cos\theta\cos k}{\sqrt{1-\cos^2\theta\sin^2 k}}.
\]
Because \(0<\theta<\pi/2\), both spectral projections are smooth and separated. In the initial coin vector \((1,i)/\sqrt2\), the two spectral weights are
\[
w_\pm(k)=\frac12\left(1\mp\frac{\sin\theta\sin k}{\sqrt{1-\cos^2\theta\sin^2 k}}\right).
\]
The usual Fourier-eigenphase argument for bounded-range translation-invariant quantum walks shows that \(Q_k/k\) converges weakly to the corresponding weighted group-velocity distribution: in the characteristic function, the eigenphases at momentum separation \(\xi/k\) yield \(e^{\pm i\xi v(k)}\), and cross-band terms vanish owing to separation of the projectors. In the integral over \(k\), the odd \(\sin k\) correction to \(w_\pm(k)\) cancels. Hence the limit is the pushforward of uniform \(k\in[-\pi,\pi)\) under \(v(k)\). The change of variables
\[
\cos^2 k=\frac{\sin^2\theta\,v^2}{\cos^2\theta(1-v^2)}
\]
gives the stated density \(f_\theta\). It is symmetric, supported on \([ -\cos\theta,\cos\theta]\), and integrates to one. This recovers the standard Konno weak limit for this initial coin state without assuming an unproved numerical convergence rate. In particular, \(Q_k/k\Rightarrow V_\theta\) as \(k\to\infty\) and \(|Q_k|\le k\).

**Triangular-array limit.** Let \(K_t\sim\operatorname{Bin}(t,q_t)\), independent of classical increments. When \(q_t\sqrt t\to\lambda\in[0,\infty)\), binomial concentration gives
\[
\frac{K_t}{\sqrt t}\longrightarrow\lambda\quad\text{in probability},
\]
since its mean is \(q_t\sqrt t\) and its variance after dividing by \(t\) is \(q_t(1-q_t)\to0\). If \(\lambda>0\), then \(K_t\to\infty\) in probability, so the coherent weak limit implies \(Q_{K_t}/\sqrt t\Rightarrow\lambda V_\theta\). If \(\lambda=0\), the bound \(|Q_{K_t}|\le K_t\) gives convergence to zero. Moreover \(K_t/t\to0\); conditioned on \(K_t\), the characteristic function of the classical term \(S_{t-K_t}/\sqrt t\) is
\[
\left[\cos\left(\frac\xi{\sqrt t}\right)\right]^{t-K_t}\longrightarrow e^{-\xi^2/2}
\]
in probability for each fixed \(\xi\in\mathbb R\). Its conditional independence from \(Q_{K_t}\) yields the factorization of limiting characteristic functions, proving the Gaussian–Konno law including its Gaussian endpoint.

When \(q_t\sqrt t\to\infty\), the binomial mean \(tq_t\to\infty\), and Chebyshev gives \(K_t/(tq_t)\to1\). Thus \(Q_{K_t}/(tq_t)\Rightarrow V_\theta\). The classical term has mean zero and variance at most \(t\), so
\[
\mathbb E\left[\left(\frac{S_{t-K_t}}{tq_t}\right)^2\right]
\le\frac1{tq_t^2}\to0.
\]
This proves the third regime, including every fixed \(p<1\).

**Moments and non-Gaussianity.** Let \(s=\sin\theta\), \(a=\cos^2\theta=1-s^2\). Symmetry makes all odd moments zero. With \(v=\cos\theta\sin u\), direct integration gives
\[
\begin{aligned}
\mathbb E V_\theta^2&=\frac{2s}{\pi}\int_0^{\pi/2}\frac{a\sin^2u}{1-a\sin^2u}\,du=1-s,\\
\mathbb E V_\theta^4&=\frac{2s}{\pi}\int_0^{\pi/2}\frac{a^2\sin^4u}{1-a\sin^2u}\,du
=1-\frac32s+\frac12s^3.
\end{aligned}
\]
Here \(\int_0^{\pi/2}(1-a\sin^2u)^{-1}du=\pi/(2s)\), and polynomial division gives both identities. The fourth cumulant is
\[
\mathbb E V_\theta^4-3(\mathbb E V_\theta^2)^2
=-\frac12(1-s)^2(4-s).
\]
Cumulants of independent sums add, and the normal has fourth cumulant zero; scaling by \(\lambda\) multiplies the fourth cumulant by \(\lambda^4\). This proves the claimed variance and strict non-Gaussianity. As an additional check on convergence of moments, in the critical window the bounded pure velocities \(|Q_k/k|\le1\) and binomial moment bounds give uniform integrability through fourth order, so these expressions agree with the normalized finite-walk moment limits, not merely formal derivatives of weak limits.

## Verification

The included `verify_crossover.py` is a standalone NumPy-based finite check. From the extracted directory, run `python verify_crossover.py` with NumPy at least version 1.24. It independently constructs Kraus matrices for the full mixed-state dynamics (up to six steps), then compares the resulting position probabilities against the explicit binomial convolution for three interior coin angles and five noise levels. It also checks normalization, symmetry, Konno density integrals, coherent second/fourth moment convergence, and a critical-window binomial-moment calculation. The actual run returned `VERIFY_OK 297 independent Kraus/mixture, Konno moments, critical moments`. Numerical finite examples establish neither the convergence theorem nor priority; those conclusions rely on the proof and literature comparisons above.

## Relationship to prior work

Štefaňák, Potoček, Yalçınkaya, Gábris, and Jex [1] define exactly the unmonitored channel used here (their equations (9)–(11)) and then study **monitored first-return probabilities**, a different observable. Their main results do not state the unmonitored critical-window position law or its cumulant. The standard one-dimensional ballistic density is due to Konno [2]; its coherent part is not new. Chisaki, Konno, Segawa, and Shikano [3] prove central-limit crossovers when quantum walks are interrupted by **position measurements and restarts**, rather than by independent commuting spatial translations. Konno, Matsue, and Segawa [4] study a stripe-controlled open-quantum-walk interpolation with another channel. Ahlbrecht, Vogts, A. H. Werner, and R. F. Werner [5] provide general Fourier methods and a commuting-Kraus ballistic result; those fixed-parameter observations are acknowledged. Their stated generic diffusive theorem requires a simple peripheral eigenvalue, which commuting spatial translations here violate, and they do not state the triangular-array Gaussian–Konno convolution.

Ellinas, Bracken, and Smyrnakis [6] additionally identify a crossover scale of noise strength squared times time for **coin-reshuffling noise**, whose Kraus operators and position statistics differ from global shift noise; that scaling analogy is acknowledged rather than claimed uniquely.

The contribution is the exact unmonitored random-time/convolution representation together with the **sharp all-regime critical-window classification**, explicit density, and strictly nonzero fourth cumulant. General facts about the pure Konno law, Gaussian classical limits, Kraus model, and Fourier techniques are not claimed as original. Searches did not establish absolute priority; an implicit prior derivation from these ingredients may exist.

## Limitations

The theorem assumes the infinite homogeneous line, the specified unbiased complex coin state, independent symmetric translations, one fixed channel parameter during each experiment, and no intermediate measurement. It does not apply unchanged to coin-selective decoherence, position measurement/restarting, monitored first return, finite boundaries, or noncommuting noise. It asserts weak convergence and moments through order four, not uniform local-limit estimates or finite-time error bars. The limiting convolution is **not** asserted to equal an exact finite-time density on the lattice. Novelty remains subject to independent literature assessment, including possibly implicit earlier uses of the commutation argument.

## References

[1] M. Štefaňák, V. Potoček, İ. Yalçınkaya, A. Gábris, I. Jex, *Recurrence in discrete-time quantum stochastic walks*, arXiv:2501.08674 (first public 2025-01-15), *Quantum* 10 (2026), 1982, DOI 10.22331/q-2026-01-22-1982; https://quantum-journal.org/papers/q-2026-01-22-1982/pdf/.

[2] N. Konno, *Quantum random walks in one dimension*, arXiv:quant-ph/0206053; and *A new type of limit theorems for the one-dimensional quantum random walk*, *J. Math. Soc. Japan* 57 (2005). The density is also presented in quantum-walk surveys.

[3] K. Chisaki, N. Konno, E. Segawa, Y. Shikano, *Crossovers induced by discrete-time quantum walks*, *Quantum Information & Computation* 11 (2011), 741–760; https://www.rintonpress.com/xxqic11/qic-11-910/0741-0760.pdf.

[4] N. Konno, K. Matsue, E. Segawa, *A crossover between open quantum random walks to quantum walks*, arXiv:2007.00940 (2020); https://arxiv.org/pdf/2007.00940.

[5] A. Ahlbrecht, H. Vogts, A. H. Werner, R. F. Werner, *Asymptotic evolution of quantum walks with random coin*, arXiv:1009.2019 (2010/2011); https://arxiv.org/pdf/1009.2019.

[6] D. Ellinas, A. J. Bracken, I. Smyrnakis, *Discrete Randomness in Discrete Time Quantum Walk: Study via Stochastic Averaging*, arXiv:1207.5257 (2012); https://arxiv.org/pdf/1207.5257.
