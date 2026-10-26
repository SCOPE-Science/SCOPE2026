# Near-resonance asymptotics for a two-grid Gabor phase-retrieval ambiguity

## Finding

Let the normalized Gaussian be \(\varphi(t)=2^{1/4}e^{-\pi t^2}\), let \(T_d\varphi(t)=\varphi(t-d)\), and define \(f_\pm=\varphi\pm iT_{1/a}\varphi\) for a fixed \(a>0\). For an integer \(m\ge1\), take irrational \(\varepsilon\) with \(0<|\varepsilon|<1/2\) and put \(b_\varepsilon=a(m+\varepsilon)\) and \(\Lambda_\varepsilon=a\mathbb Z\cup b_\varepsilon\mathbb Z\).

Write \(\mathcal G\) for the normalized Gaussian Gabor transform and define the line-data discrepancy

\[
\Delta_\varepsilon^2=\sum_{\omega\in\Lambda_\varepsilon}\int_{\mathbb R}\left(|\mathcal Gf_+(x,\omega)|-|\mathcal Gf_-(x,\omega)|\right)^2\,dx.
\]

Define

\[
\rho_a(x)=e^{\pi x/a-\pi/(2a^2)},\qquad I(a)=\int_{\mathbb R}e^{-\pi x^2}\frac{\rho_a(x)^2}{1+\rho_a(x)^2}\,dx,
\]

and

\[
S_m(a)=\sum_{k\in\mathbb Z}k^2e^{-\pi m^2a^2k^2},\qquad C(a,m)=2\pi\sqrt{I(a)S_m(a)}.
\]

Then the exact first-order near-resonance law is

\[
\boxed{\lim_{\substack{\varepsilon\to0\\ \varepsilon\notin\mathbb Q}}\frac{\Delta_\varepsilon}{|\varepsilon|}=C(a,m).}
\]

At the same time, the phase-invariant signal distance is independent of \(\varepsilon\) and equals

\[
\operatorname{dist}_{\mathrm{phase}}(f_+,f_-)=2\sqrt{1-e^{-\pi/(2a^2)}}>0.
\]

For every irrational \(\varepsilon\), the line-level set \(\Lambda_\varepsilon\) is not contained in an arithmetic progression. The published uniqueness criterion for parallel-line Gabor phase retrieval therefore applies: each such measurement set is injective up to global phase, although the fixed pair above becomes arbitrarily close in the line-data metric as \(b_\varepsilon/a\) approaches the integer \(m\).

## Assumptions and scope

The parameter \(a\) is fixed and positive; \(m\) is a fixed positive integer; \(\varepsilon\) tends to zero through irrational values with \(|\varepsilon|<1/2\). The signals \(f_\pm\) are Schwartz functions, so the displayed sum of linewise squared discrepancies is finite. The result concerns this explicit pair and this specified data metric. It does not assert a uniform stability theorem for arbitrary signals or for a fixed irrational grid pair.

## Proof

For the normalized Gaussian and the translated-Gaussian pair, the explicit Gabor-transform formula established by Alaifari and Wellershoff gives

\[
|\mathcal Gf_\pm(x,\omega)|=e^{-\pi(x^2+\omega^2)/2}\left|1\pm i\rho_a(x)e^{-i\pi\omega/a}\right|.
\]

If \(\omega=ak\), the exponential factor \(e^{-i\pi\omega/a}=(-1)^k\) is real, hence \(|\mathcal Gf_+|=|\mathcal Gf_-|\) on every line in \(\mathbb R\times a\mathbb Z\). The discrepancy therefore comes only from the added lines \(\omega=b_\varepsilon k\). On these lines, the squared moduli inside the absolute values are

\[
1+\rho_a(x)^2\pm 2\rho_a(x)(-1)^{mk}\sin(\pi\varepsilon k).
\]

Consequently, after squaring the difference, the factor \((-1)^{mk}\) has no effect. For each fixed \(x\) and integer \(k\), rationalizing the difference of square roots yields

\[
\lim_{\varepsilon\to0}\frac{1}{|\varepsilon|}\left|\sqrt{1+\rho_a(x)^2+2\rho_a(x)\sin(\pi\varepsilon k)}-\sqrt{1+\rho_a(x)^2-2\rho_a(x)\sin(\pi\varepsilon k)}\right|=\frac{2\pi|k|\rho_a(x)}{\sqrt{1+\rho_a(x)^2}}.
\]

The denominator in the rationalized expression is at least \(2\), since it is the sum of the two moduli \(|1+iu|+|1-iu|\). Using \(|\sin(\pi\varepsilon k)|\le\pi|\varepsilon k|\) gives the bound

\[
\frac{\delta_{\varepsilon,k}(x)^2}{\varepsilon^2}\le 4\pi^2k^2e^{-\pi(x^2+b_\varepsilon^2k^2)}\rho_a(x)^2,
\]

where \(\delta_{\varepsilon,k}(x)\) is the magnitude discrepancy on the line \(\omega=b_\varepsilon k\). Since \(|\varepsilon|<1/2\), one has \(b_\varepsilon\ge a(m-1/2)>0\), and

\[
e^{-\pi x^2}\rho_a(x)^2=e^{-\pi(x-1/a)^2}.
\]

Thus the right-hand side is dominated by an integrable function of \(x\) and a summable sequence in \(k\), uniformly for the stated range of \(\varepsilon\). Dominated convergence for the integral and the series gives

\[
\lim_{\varepsilon\to0}\frac{\Delta_\varepsilon^2}{\varepsilon^2}=4\pi^2 I(a)S_m(a),
\]

which proves the claimed limit after taking the nonnegative square root.

For the signal distance, \(\|\varphi\|_2=\|T_{1/a}\varphi\|_2=1\) and \(\langle\varphi,T_{1/a}\varphi\rangle=e^{-\pi/(2a^2)}\). Hence \(\|f_\pm\|_2^2=2\), \(|\langle f_+,f_-\rangle|=2e^{-\pi/(2a^2)}\), and the standard phase-orbit distance formula gives the displayed positive distance.

Finally, if \(\Lambda_\varepsilon\) were contained in an arithmetic progression, the fact that it contains \(0,a,b_\varepsilon\) would force \(b_\varepsilon/a\) to be rational. This contradicts irrationality of \(\varepsilon\). Liehr's published characterization of parallel-line Gabor uniqueness therefore supplies the injectivity statement.

## Verification

The proof uses an exact transform identity, square-root rationalization, and dominated convergence; it does not infer an infinite statement from finite enumeration. The positive finite constant is well-defined because \(0<I(a)\le1\) and the Gaussian-weighted series \(S_m(a)\) converges absolutely. A standalone numerical stress test is embedded at `verification/verify_near_resonance.py`. For \(a=1/2\), \(m=1\), and \(\varepsilon=\sqrt2\,10^{-j}\), the computed ratios \(\Delta_\varepsilon/|\varepsilon|\) converge to the predicted coefficient \(0.683705172855\); the relative errors for \(j=2,3,4\) are approximately \(2.12\times10^{-2}\), \(2.12\times10^{-3}\), and \(2.12\times10^{-4}\). These finite computations are supplementary checks only; the proof establishes the limit.

## Relationship to prior work

Alaifari and Wellershoff provide the explicit pair \(f_\pm\) with identical Gabor magnitudes on a single arithmetic family of parallel lines. Liehr characterizes exactly which parallel-line level sets give uniqueness; in particular, the union of the two grids above is a uniqueness set when their spacing ratio is irrational. Alaifari, Bartolucci, Steinerberger, and Wellershoff study the distinction between sampled uniqueness and stability. The present claim does not restate the uniqueness classification or the general ill-posedness results: it computes the exact first-order discrepancy coefficient for one fixed, non-equivalent pair as a second line grid approaches arithmetic resonance.

## Limitations

The coefficient describes one explicit pair and one linewise \(L^2\) data metric. It does not quantify reconstruction error for noisy data, establish optimality among all pairs, or determine stability constants for any fixed irrational ratio. The literature search did not prove global novelty; an equivalent asymptotic in an unlocated source remains a priority risk.

## References

1. R. Alaifari and M. Wellershoff, “Phase retrieval from sampled Gabor transform magnitudes: Counterexamples,” *Journal of Fourier Analysis and Applications* 28 (2022), article 9. First public preprint: arXiv:2010.01078, 2020-10-02. DOI: 10.1007/s00041-021-09901-7.
2. L. Liehr, “Arithmetic progressions and holomorphic phase retrieval,” *Bulletin of the London Mathematical Society* 56(11) (2024), 3316–3330. First published 2024-08-13. DOI: 10.1112/blms.13134.
3. R. Alaifari, F. Bartolucci, S. Steinerberger, and M. Wellershoff, “On the connection between uniqueness from samples and stability in Gabor phase retrieval,” *Sampling Theory, Signal Processing, and Data Analysis* 22 (2024), article 6. DOI: 10.1007/s43670-023-00079-1.
