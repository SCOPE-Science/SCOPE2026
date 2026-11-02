# Sharp spectral-peak onset in inhibitory delayed telegraph noise

## Finding

For the stationary symmetric two-state process with strictly positive delayed switching rate
\[
q_t=\frac12\left(c+h\,\sigma_{t-}\sigma_{t-T}\right),\qquad c>h>0,\quad T>0,
\]
let \(S_T(\omega)=\int_{\mathbb R}e^{-i\omega t}\mathbb E[\sigma_0\sigma_t]dt\) be its two-sided power spectral density. Define the critical delay
\[
T_*=\frac{1}{h+\sqrt{h(c+h)}}.
\]
For \(0<T\le T_*\), the unique global maximum of \(S_T\) is at zero frequency. For \(T>T_*\), zero frequency is a strict local minimum and every global maximizer is nonzero. There is \(\varepsilon>0\) such that for \(T_*<T<T_*+\varepsilon\), the only global maximizers are the pair \(\pm\omega_*(T)\), where
\[
\omega_*(T)=\left(\frac{12(1+cT_*)}{T_*^3(4+cT_*)}\right)^{1/2}(T-T_*)^{1/2}+O((T-T_*)^{3/2}).
\]
This is a threshold in the *location of the dominant fluctuation frequency*, not an instability of the stationary process.

## Assumptions and scope

The state \(\sigma_t\) takes values in \(\{-1,+1\}\); at time \(t\) its conditional flip intensity, given the strict past, equals \(q_t\). Both parameters \(c,h\) are fixed positive reals satisfying \(h<c\); \(T>0\) is a fixed deterministic memory delay. The Fourier convention is \(S_T(\omega)=\int_{-\infty}^{\infty}e^{-i\omega t}C(t)dt\), with \(C(t)=\mathbb E[\sigma_0\sigma_t]\), so \(\int S_T(\omega)d\omega/(2\pi)=1\). No claim is made at \(h=0\), \(h=c\), or about asymmetric two-state intensities, arbitrary memory kernels, or unique global peaks at delays far above the threshold.

The process has a unique stationary law. To construct it, use Poisson updates at rate \(c\). With probability \(1-h/c\), replace the spin by an independent fair sign; with probability \(h/c\), replace it by the *negative* sign seen exactly \(T\) earlier. Conditional on the current and delayed signs, the chance of a flip at an update gives precisely the specified intensity. Tracing the state backward through update events encounters a fresh fair sign after an almost surely finite geometric number of ancestral steps, establishing the unique stationary version. Global sign symmetry gives \(\mathbb E\sigma_t=0\).

## Proof

**Stationary linear innovation and spectrum.** The compensated jump martingale \(M\) satisfies the semimartingale equation
\[
d\sigma_t=\bigl(-c\sigma_{t-}-h\sigma_{t-T}\bigr)dt+dM_t.
\]
Its predictable quadratic variation obeys \(d\langle M\rangle_t=4q_tdt\). Stationarity gives the nonrandom expected innovation rate
\[
A=\mathbb E[4q_t]=2\bigl(c+hC(T)\bigr)>2(c-h)>0.
\]
(The strict lower bound uses \(|C(T)|\le1\).) The causal delay resolvent \(G\), defined by \(G(t)=0\) for \(t<0\), \(G(0)=1\), and \(G'(t)=-cG(t)-hG(t-T)\), is absolutely integrable and square integrable. Indeed its Volterra-series absolute \(L^1\) norm is bounded above by \(\sum_{n\ge0}h^n/c^{n+1}=(c-h)^{-1}\); boundedness follows from the convolution equation, and homogeneous solutions decay because \(c>h\). Thus the stationary solution has the causal \(L^2\) representation \(\sigma_t=\int_{-\infty}^t G(t-s)dM_s\). Orthogonality of disjoint martingale increments yields
\[
S_T(\omega)=A\left|\frac{1}{c+i\omega+h e^{-i\omega T}}\right|^2
=\frac{A}{F_T(\omega)},
\]
where
\[
F_T(\omega)=\bigl(c+h\cos(\omega T)\bigr)^2+
\bigl(\omega-h\sin(\omega T)\bigr)^2.
\]
The normalization follows from \(C(0)=\mathbb E\sigma_0^2=1\). One may compute \(C(T)\) without the spectrum: the stationary covariance equation \(C'(t)=-cC(t)-hC(t-T)\) for positive \(t\), with \(C(-t)=C(t)\) and \(C(0)=1\), gives for \(\eta=\sqrt{c^2-h^2}\)
\[
C(T)=\frac{\eta-h\sinh(\eta T)}{\eta\cosh(\eta T)+c\sinh(\eta T)}.
\]
This determines the positive spectral numerator \(A\) explicitly. The Fourier denominator itself also follows from the general memory-kernel transform already in the literature; the novelty assessed here lies in its sharp global optimization and onset law.

**Sharp global threshold.** Direct subtraction gives, for every real \(\omega\),
\[
F_T(\omega)-F_T(0)=\omega^2-2ch\bigl(1-\cos(\omega T)\bigr)-2h\omega\sin(\omega T).
\]
The expression is even. For \(\omega>0\), the inequalities \(1-\cos u\le u^2/2\) and \(\sin u\le u\) yield
\[
F_T(\omega)-F_T(0)\ge\omega^2\bigl(1-2hT-chT^2\bigr),
\]
with strict inequality whenever \(\omega\ne0\) and the last factor is zero. The factor is positive for \(T<T_*\), vanishes at \(T=T_*\), and is negative for \(T>T_*\). This proves the asserted unique zero-frequency global maximum for \(T\le T_*\). For \(T>T_*\), a Taylor expansion exhibits \(F_T(\omega)<F_T(0)\) for small nonzero frequencies, so zero is a strict local minimum of \(S_T\). Since \(F_T(\omega)\to\infty\) as \(|\omega|\to\infty\), a nonzero global minimum of \(F_T\) exists.

**Critical square-root law and local uniqueness.** An even analytic expansion at zero is
\[
F_T(\omega)=(c+h)^2+b(T)\omega^2+a_4(T)\omega^4+O(\omega^6),
\]
with \(b(T)=1-2hT-chT^2\), \(a_4(T)=hT^3(4+cT)/12>0\). At \(T=T_*\), \(b(T_*)=0\) and \(b'(T_*)=-2h(1+cT_*)<0\). By the strict global gap at criticality, coercivity, and uniform continuity, every global minimizer of \(F_T\) for \(T\) sufficiently close to \(T_*\) lies in an arbitrarily small fixed neighborhood of zero. Within that neighborhood the analytic equation \(\partial_\omega F_T/(2\omega)=0\) is a strictly increasing function of \(\omega^2\), beginning at \(b(T)<0\). It has exactly one positive root and thereby precisely two symmetric global minimizers. The implicit function theorem at \((\omega^2,T)=(0,T_*)\) gives
\[
\omega_*(T)^2=\frac{12(1+cT_*)}{T_*^3(4+cT_*)}(T-T_*)+O((T-T_*)^2),
\]
which proves the asserted square-root law.

## Verification

The accompanying `checker.py` independently evaluates the exact spectral denominator, checks the critical inequality and its strict onset, numerically optimizes dominant frequencies for several parameter pairs, checks near-threshold square-root convergence, and verifies the spectrum's unit-variance normalization by quadrature. Computational tests confirm selected instances but are not substitutes for the global inequality and analytic proof above. Run from a Python environment with NumPy and SciPy using `python checker.py`.

## Relationship to prior work

Apostolov, Usatenko, Yampol'skii, Melnyk, Grigolini, and Krokhin (2024) introduced the nonlocal-memory telegraph construction and solved its delta-delay covariance equations; the rate family here is the symmetric, *negative-memory* specialization. Melnyk, Usatenko, and Yampol'skii (2025), Eq. (22), already established the general Fourier transfer formula for arbitrary memory, and therefore covers the spectral denominator as a special case. Neither result, in the material inspected, establishes the sharp global zero-to-nonzero peak threshold or the locally unique pair with its square-root onset coefficient. This is a comparison of precise implications, not a claim that the spectral transform itself is new.

## Limitations

The threshold describes stationary spectral maxima rather than a dynamical bifurcation or a deterministic-delay Hopf instability. The theorem does not count possible extra sidelobe maxima well beyond the threshold, does not handle multiple or distributed delays, and assumes \(0<h<c\). Analytical correctness and initial literature comparisons have been assessed in the accompanying review; priority has not undergone independent specialist validation.

## References

1. S. S. Apostolov, O. V. Usatenko, V. A. Yampol'skii, S. S. Melnyk, P. Grigolini, and A. Krokhin, *Random telegraph processes with non-local memory*, arXiv:2402.11038v1 (16 February 2024), https://arxiv.org/html/2402.11038v1.
2. S. S. Melnyk, O. V. Usatenko, and V. A. Yampol'skii, *Non-Markov random telegraph processes with arbitrary nonlocal memory*, Physical Review E 112, 014127 (2025), Eq. (22), https://doi.org/10.1103/xvck-7n24.
