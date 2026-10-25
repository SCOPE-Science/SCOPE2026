# Marginal inverse-cube transport and a two-parameter logarithmic crossover

## Finding
For the continuum kinetic spectral observable specified below, both the inverse-cube collision kernel and the inverse-cube harmonic interaction are **marginal**. Their simultaneous near-critical variation produces a finite, strictly positive two-variable crossover. In particular, at their common critical point,
\[
J_{3,3}(t)\sim\frac{\sqrt\pi}{2\sqrt{2\gamma\zeta(3)}}\sqrt{\frac{\log t}{t}}\qquad(t\to\infty).
\]
The numerator's positive half-logarithm comes from the divergent group velocity, and the denominator's negative half-logarithm from inverse-cube collision relaxation.

Define the continuous function
\[
\Phi(z)=\begin{cases}2(1-e^{-z/2})/z,&z\ne0,\\1,&z=0.\end{cases}
\]
For fixed \(r,s\in\mathbb R\), put \(\delta_t=3+r/\log t\) and \(\alpha_t=3+s/\log t\). Then
\[
\boxed{\lim_{t\to\infty}\frac{J_{\alpha_t,\delta_t}(t)}{J_{3,3}(t)}=\frac{\Phi(r)}{\sqrt{\Phi(s)}}.}
\]
This convergence is uniform on compact subsets of \(\mathbb R^2\), and captures either side of both marginal exponents.

For fixed \(\delta>2\), a separate collision-range crossover holds:
\[
\boxed{\lim_{t\to\infty}\frac{J_{3+s/\log t,\delta}(t)}{J_{3,\delta}(t)}=\Phi(s)^{-\nu_\delta/2}},
\qquad \nu_\delta=\begin{cases}\delta-2,&2<\delta<3,\\1,&\delta\ge3.\end{cases}
\]
Convergence is uniform for \(s\) in compact intervals.

## Assumptions and scope
Let \(\gamma>0\) and \(\alpha>1,\delta>2\). For \(0<k\le\pi\), define the convergent spectral sums, dispersion, group speed, and collision rate
\[
S_p(k)=\sum_{n=1}^\infty\frac{1-\cos(nk)}{n^p},\quad
\omega_\delta(k)=\left(\frac{2S_\delta(k)}{\zeta(\delta)}\right)^{1/2},\quad
v_\delta(k)=\omega_\delta'(k),\quad
\mu_\alpha(k)=\frac{2\gamma S_\alpha(k)}{\zeta(\alpha)}.
\]
Consider the **defined mathematical observable**
\[
J_{\alpha,\delta}(t)=\int_0^\pi v_\delta(k)^2e^{-t\mu_\alpha(k)}\,dk,\qquad t>0.
\]
The nonnegative integral is finite for each \(t>0\) because \(\delta>2\). It is the one-sided spectral integral arising from the diagonal kinetic approximation to deterministic energy-current correlations in Andreucci–Lepri–Mejía-Monasterio–Ruffo, without their temperature and wave-number normalization factors. We prove asymptotics **only for this exact mathematical integral**, not for the full microscopic stochastic current, which may have additional noise contributions.

Write
\[
a_\delta=-\frac{2\Gamma(1-\delta)\sin(\pi\delta/2)}{\zeta(\delta)},\quad
Z_\delta=a_\delta\left(\frac{\delta-1}{2}\right)^2
\qquad(2<\delta<3),
\]
and \(b_\delta=\zeta(\delta-2)/\zeta(\delta)\) for \(\delta>3\). These are strictly positive. At fixed \(\alpha=3\), the complete amplitude trichotomy is
\[
\boxed{J_{3,\delta}(t)\sim
\begin{cases}
\displaystyle\frac{Z_\delta}{2}\Gamma\left(\frac{\delta-2}{2}\right)
\left(\frac{2\zeta(3)}{\gamma t\log t}\right)^{(\delta-2)/2},&2<\delta<3,\\[2mm]
\displaystyle\frac{\sqrt\pi}{2\sqrt{2\gamma\zeta(3)}}\sqrt{\frac{\log t}{t}},&\delta=3,\\[2mm]
\displaystyle b_\delta\sqrt{\frac{\pi\zeta(3)}{2\gamma t\log t}},&\delta>3.
\end{cases}}
\]
The exponents and amplitudes correspond precisely to the definitions above. No limit with \(\delta\le2\), infinite-volume microscopic noise current, or simultaneous particle-number growth is claimed.

## Proof
**1. The marginal spectral kernel.** Splitting the convergent series at \(n=\lfloor1/k\rfloor\), using \(1-\cos z=z^2/2+O(z^4)\) on the first piece and an integral bound on its tail, gives
\[
S_3(k)=\frac{k^2}{2}\log(1/k)+O(k^2),\qquad
S_3'(k)=k\log(1/k)+O(k)
\quad (k\downarrow0).
\]
For fixed \(2<\delta<3\), the standard Abelian sum expansion, also obtained by the polylogarithm expansion in the cited source, gives \(2S_\delta(k)/\zeta(\delta)\sim a_\delta k^{\delta-1}\), and differentiation yields
\[
v_\delta(k)^2\sim Z_\delta k^{\delta-3}.
\]
At \(\delta=3\), direct differentiation of the displayed dispersion yields
\[
v_3(k)^2\sim\frac{\log(1/k)}{\zeta(3)}.
\]
For fixed \(\delta>3\), dominated convergence on the second moment of the coupling gives \(v_\delta(k)^2\to b_\delta\). Meanwhile
\[
\mu_3(k)\sim\frac{\gamma}{\zeta(3)}k^2\log(1/k).
\]
These expansions prove that \(J_{\alpha,\delta}(t)\) is locally integrable at zero precisely in the stated \(\delta>2\) domain.

**2. Critical Laplace asymptotics.** Let \(k_t=[2\zeta(3)/(\gamma t\log t)]^{1/2}\). For each fixed \(u>0\),
\[
t\mu_3(k_tu)\longrightarrow u^2,
\qquad\frac{\log(1/(k_tu))}{\log t}\longrightarrow\frac12.
\]
Substitute \(k=k_tu\) and insert the three respective group-speed asymptotics. The required Gaussian Mellin integral is
\[
\int_0^\infty u^{\delta-3}e^{-u^2}\,du=
\frac12\Gamma\left(\frac{\delta-2}{2}\right),
\]
with the familiar \(\int_0^\infty e^{-u^2}du=\sqrt\pi/2\) for the other two branches. After collecting powers of \(k_t\) and \(\log t\), one obtains all three displayed amplitudes.

For rigor in exchanging limits and integrals, first fix \(0<\varepsilon<M<\infty\). The expansions above converge uniformly on \(\varepsilon\le u\le M\). Their positive spectral-sum representations give locally uniform Potter-type power bounds for small \(k\), with the lower-tail exponent integrable because \(\delta>2\); the rate is bounded below on the remaining wave-number interval. Dominated Gaussian tails and exponential suppression for \(k\) bounded away from zero justify first sending \(t\to\infty\), then \(\varepsilon\downarrow0\), \(M\uparrow\infty\).

**3. Uniform near-marginal collision expansion.** For \(p=3+\epsilon\) and \(|\epsilon|\le K/\log t\), the same sum split gives, uniformly for \(k=k_tu\) with \(u\) in a compact positive interval,
\[
S_{3+\epsilon}(k)=\frac{k^2}{2}
\frac{1-e^{-\epsilon\log(1/k)}}{\epsilon}
+O_K(k^2+k^{2+\epsilon}),
\]
where the quotient is interpreted as \(\log(1/k)\) at \(\epsilon=0\). Put \(\epsilon=s/\log t\) and use \(\epsilon\log(1/(k_tu))\to s/2\). The continuous limiting kernel is
\[
t\mu_{3+s/\log t}(k_tu)\longrightarrow\Phi(s)u^2,
\]
locally uniformly in \((s,u)\). Consequently, rescaling \(u\mapsto u/\sqrt{\Phi(s)}\) inside the Gaussian Mellin integrals yields the fixed-\(\delta\) ratio with exponent \(-\nu_\delta/2\).

**4. Simultaneous marginality of dispersion.** Apply the same split with \(p=3+r/\log t\), now to both \(S_p(k)\) and \(S_p'(k)\). Uniformly on compact positive \(u\)-ranges and bounded \(r\),
\[
S_{3+r/\log t}(k_tu)\sim\frac{(k_tu)^2\log t}{4}\Phi(r),
\qquad
S_{3+r/\log t}'(k_tu)\sim\frac{k_tu\log t}{2}\Phi(r).
\]
Since \(v_p^2=S_p'^2/(2\zeta(p)S_p)\), it follows that
\[
\frac{v_{3+r/\log t}(k_tu)^2}{\log t}
\longrightarrow\frac{\Phi(r)}{2\zeta(3)}.
\]
Multiplying by the collision factor from step 3 and integrating gives
\[
J_{3+s/\log t,\;3+r/\log t}(t)
\sim\frac{\sqrt\pi}{2\sqrt{2\gamma\zeta(3)}}
\sqrt{\frac{\log t}{t}}\frac{\Phi(r)}{\sqrt{\Phi(s)}}.
\]
The same uniform split bounds as step 2, applied to \(|r|,|s|\le K\), control both tails and establish local uniformity. This completes the proof.

## Verification
The included standalone program evaluates \(S_p(k)\) by the polylogarithm identity \(S_p(k)=\zeta(p)-\operatorname{Re}\operatorname{Li}_p(e^{ik})\), differentiates the dispersion through \(\operatorname{Im}\operatorname{Li}_{p-1}(e^{ik})\), and numerically integrates the resulting exact spectral kernel over its late-time characteristic wave-number scale. It compares two increasing observation times at fixed interaction exponents, and several near-critical parameter paths to the predicted crossover surfaces. The computations are finite-precision corroboration, not the basis of the infinite-time proof. The script requires Python, NumPy and mpmath and prints the measured and limiting ratios.

## Relationship to prior work
Andreucci, Lepri, Mejía-Monasterio, and Ruffo (arXiv:2409.11832v1, Sections 4–5 and Appendix B) supply the kinetic mode integral and the non-marginal power-law classification; their Section 5.1 explicitly restricts its leading power-law expansions to noninteger range exponents. Their equations directly motivate, but do not state, the two simultaneous logarithmic critical layers or the \(\Phi(r)/\sqrt{\Phi(s)}\) crossover.

Tamaki and Saito (arXiv:1906.08457, Sections II–III) already derive logarithmic corrections at the *harmonic interaction* endpoint \(\delta=3\), for a different model with nearest-neighbor momentum exchanges. The present theorem does not claim that one-parameter interaction marginality with short-range exchange is new. Its distinguishable contribution is the **long-range collision endpoint** \(\alpha=3\) and the **joint** continuously tuned long-range collision/interaction crossover in the specified spectral integral. Their fixed-nearest-neighbor collision assumptions do not supply \(\alpha_t\) or its simultaneous coupling to \(\delta_t\).

## Limitations
The continuum kernel is a **kinetic diagonal approximation** to deterministic-current correlations, not the full current of the stochastic chain. The normalization is stated explicitly to avoid inferring unproved physical prefactors. The theorem takes the infinite-volume spectral integral as its object before the long-time limit; finite-size cutoffs can change observed time scales. The crossover paths are mathematical variation of model exponents with observation time, and are not predictions of actual time-varying microscopic couplings. No independent scientific assessment or publication-priority certification has been performed; an unidentified general two-parameter regular-variation theorem could imply the result.

## References
1. F. Andreucci, S. Lepri, C. Mejía-Monasterio, S. Ruffo, *Thermal transport in long-range interacting harmonic chains perturbed by long-range conservative noise*, arXiv:2409.11832v1, first posted 2024-09-18, https://arxiv.org/html/2409.11832v1 ; DOI:10.1007/s10955-024-03383-9.
2. S. Tamaki, K. Saito, *Energy current correlation in solvable long-range interacting systems*, arXiv:1906.08457, first posted 2019-06-20, https://arxiv.org/abs/1906.08457 ; DOI:10.1103/PhysRevE.101.042118.
