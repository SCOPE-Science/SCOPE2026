# Sharp finite-zero ceiling and exact resonance lines for two-tone Hermite spectrograms

## Finding
For each integer \(n\ge 0\), every nonresonant separation \(\Delta>0\) of two equal tones has at most \(4n+1\) zeros, counted with the **one-variable real multiplicities defined below**, in one period of the **spectrogram zero pattern** with the \(n\)-th Hermite window. This upper bound is sharp: for every fixed \(n\), all sufficiently large separations have exactly \(4n+1\) **distinct, nondegenerate** zeros.

The exceptional separations are completely explicit in terms of Hermite roots. If \(\rho_1<\cdots<\rho_n\) are the real zeros of the window, set
\[
\mathcal R_n=\{\rho_j-\rho_i:1\le i<j\le n\}.
\]
At \(\Delta\in\mathcal R_n\), there is an entire horizontal-in-time line of zeros at each frequency \(\nu=(\rho_i+\rho_j)/2\) with \(\rho_j-\rho_i=\Delta\); **these are exactly all nonisolated zero components**. Outside \(\mathcal R_n\), every zero is isolated and occurs at either \(t=0\) or \(t=1/(2\Delta)\), modulo the period \(1/\Delta\).

In particular, \(\mathcal R_0=\mathcal R_1=\varnothing\). At order two, \(\mathcal R_2=\{1/\sqrt\pi\}\), with one complete zero line at \(\nu=0\). At order three, put \(r=\sqrt{3/(4\pi)}\). Then \(\mathcal R_3=\{r,2r\}\): separation \(r\) has precisely two zero lines, at \(\nu=\pm r/2\), and separation \(2r\) has precisely one, at \(\nu=0\).

## Assumptions and scope
We use the Fourier convention \(\widehat g(\nu)=\int_{\mathbb R}g(s)e^{-2\pi i\nu s}\,ds\). Let \(H_n\) be the physicists' Hermite polynomial, so \(H_0=1\), \(H_1(z)=2z\), and \(H_{n+1}(z)=2zH_n(z)-2nH_{n-1}(z)\). Define the unnormalized Hermite window
\[
h_n(x)=(2\pi)^{n/2}H_n(\sqrt{2\pi}\,x)e^{-\pi x^2}.
\]
For a separation \(\Delta>0\), put \(d=\Delta/2\), \(f_\Delta(s)=e^{2\pi i d s}+e^{-2\pi i d s}\), and
\[
V_{h_n}f_\Delta(t,\nu)=\int_{\mathbb R} f_\Delta(s)h_n(s-t)e^{-2\pi i\nu s}\,ds.
\]
The integral converges absolutely for every real \(t,\nu\), despite the tones not belonging to \(L^2(\mathbb R)\). The **zero set** and spectrogram descend to the time cylinder \(t\in\mathbb R/(\Delta^{-1}\mathbb Z)\), \(\nu\in\mathbb R\): the complex STFT itself is quasiperiodic, with \(V(t+1/\Delta,\nu)=-e^{-2\pi i\nu/\Delta}V(t,\nu)\). Multiplying \(h_n\) by a nonzero constant does not change its zeros.

For nonresonant \(\Delta\), define the real analytic functions
\[
S_{n,d}(\nu)=h_n(\nu-d)+h_n(\nu+d),\qquad
D_{n,d}(\nu)=h_n(\nu-d)-h_n(\nu+d).
\]
The **count with multiplicity** is the sum of the ordinary one-variable orders of all real zeros of \(S_{n,d}\) and \(D_{n,d}\). Each such zero represents exactly one distinct point of the two-dimensional zero set, on the appropriate time slice. It is not defined by an unproved complex-analytic multiplicity for the nonholomorphic STFT.

## Proof
**1. Exact transform and time slices.** The generating series
\[
\sum_{n\ge0}\frac{z^n}{n!}h_n(s)=e^{-\pi s^2+4\pi sz-2\pi z^2}
\]
shows by elementary Gaussian integration that \(\widehat h_n=(-i)^n h_n\). Consequently
\[
V_{h_n}f_\Delta(t,\nu)=(-i)^n e^{-2\pi i\nu t}
\left(e^{2\pi i d t}A(\nu)+e^{-2\pi i d t}B(\nu)\right),
\]
where \(A(\nu)=h_n(\nu-d)\) and \(B(\nu)=h_n(\nu+d)\) are real.

If not both \(A,B\) vanish, their sum with these phase factors is zero only if \(|A|=|B|\ne0\). The ratio of the factors must then be a real unit number, hence \(+1\) or \(-1\). Exactly the possibilities \(t=0\), \(S_{n,d}(\nu)=0\), and \(t=1/(2\Delta)\), \(D_{n,d}(\nu)=0\), follow modulo \(1/\Delta\). Conversely, all such slice zeros are genuine.

**2. Exact line-resonance classification.** Since all \(n\) roots of \(h_n\) are simple and real, \(A(\nu)=B(\nu)=0\) precisely when \(\nu-d=\rho_i\) and \(\nu+d=\rho_j\) for a pair \(i<j\). Eliminating \(d\) and \(\nu\) gives \(\Delta=\rho_j-\rho_i\) and \(\nu=(\rho_i+\rho_j)/2\). At each such frequency, the STFT vanishes identically for every \(t\). Conversely, any zero outside these lines lies on one of two fixed time slices and is isolated, since neither of their nonzero real analytic functions is identically zero. The asserted complete classification of nonisolated components follows.

**3. Finite-zero ceiling.** Write \(h_n(x)=P_n(x)e^{-\pi x^2}\), with \(P_n\) a real polynomial of exact degree \(n\). Multiplying \(S_{n,d}\) or \(D_{n,d}\) by the strictly positive factor \(e^{\pi(\nu^2+d^2)}\) gives
\[
P_n(\nu-d)e^{2\pi d\nu}\ \pm\ P_n(\nu+d)e^{-2\pi d\nu}.
\]
Any nonzero function of this form has at most \(2n+1\) real zeros counted with multiplicity. Indeed, multiplying once more by \(e^{2\pi d\nu}\) produces \(F(\nu)=P_n(\nu-d)e^{4\pi d\nu}\pm P_n(\nu+d)\). Its \((n+1)\)-st derivative is \(e^{4\pi d\nu}Q_n(\nu)\), where \(Q_n=(\partial_\nu+4\pi d)^{n+1}P_n(\nu-d)\) has exact degree \(n\) and nonzero leading coefficient because \(d>0\). Repeated Rolle's theorem, with multiplicities, implies the \(2n+1\) bound.

Parity now sharpens the joint bound. Since \(h_n(-x)=(-1)^n h_n(x)\), the function \(S_{n,d}\) has parity \((-1)^n\) and \(D_{n,d}\) has parity \((-1)^{n+1}\). Thus one is even and the other odd. The finite total real-zero multiplicity of an even real analytic function is even, so the even branch has at most \(2n\); the odd branch has at most \(2n+1\). Their sum is at most \(4n+1\).

**4. Attainment and nondegeneracy.** Fix \(n\) and let \(d\to\infty\). In a small fixed neighborhood of each simple root \(\rho_j\), the shifted Gaussian \(h_n(\nu-d)\), viewed around \(\nu=d+\rho_j\), dominates \(h_n(\nu+d)\) in the \(C^1\) sense after translation. The implicit function theorem yields exactly one simple zero of each of \(S_{n,d}\) and \(D_{n,d}\) near every \(d+\rho_j\). The same holds near each \(-d+\rho_j\), giving \(2n\) simple zeros per branch. The odd branch additionally has its symmetry-forced zero at \(\nu=0\); this zero is simple for sufficiently large \(d\), since its derivative is, up to a nonzero scalar, \(h_n'(d)\), whose polynomial factor has only finitely many roots. Thus there are at least \(4n+1\) simple branch zeros, and the upper bound proves completeness. For sufficiently large \(d\), no two roots of \(h_n\) differ by \(2d\), so there are no zero lines. At every branch-simple zero, the nonvanishing complementary phase derivative makes the real two-dimensional STFT Jacobian nonsingular. This proves the claimed \(4n+1\) distinct nondegenerate points.

**5. Concrete resonances.** The explicit polynomials \(P_2(x)=16\pi^2x^2-4\pi\) and \(P_3(x)=16\pi^2x(4\pi x^2-3)\) yield the stated two- and three-level root differences and exact line frequencies.

## Verification
The standalone standard-library script `verify.py` checks the STFT against direct Simpson-quadrature evaluation of its defining integral in 30 independent cases (orders zero through four); checks 51 resonance-line evaluations for orders two and three; and checks the sharp \(4n+1\) zero count at separation \(\Delta=8\) for each order zero through six, with two branches per order. The completed run reported `VERIFY_OK 95 integral, resonance, and sharp-count checks; n=0..6; gap=8`. These checks corroborate, but do not replace, the all-orders proof using Gaussian Fourier diagonalization, Rolle's theorem, and the implicit function theorem.

## Relationship to prior work
Bellourak, Meignen, Polisano and Nahon (arXiv:2610.13531v1, first public October 9, 2026), Sections 2–5, investigate the almost-surely isolated charged zeros of white-noise spectrograms with Hermite windows. Their object is a random polyanalytic field rather than deterministic two-tone data. The deterministic resonance lines above are therefore not implied by their probability-one isolation result. Chand, Nolen and Wu (arXiv:2601.10910, first public January 15, 2026) analyze two-tone *Gaussian*-window interference and phase geometry, corresponding to the order-zero window only. Alaifari and Yang (arXiv:2410.05486, October 2024) use Hermite-window ambiguity functions for multiwindow phase retrieval, rather than determining these deterministic two-tone STFT zeros. The elementary exponential-polynomial zero-count lemma and standard Hermite-root facts are classical tools and are not claimed as new.

The present contribution is the **joint all-Hermite-order sharp ceiling and exact root-gap resonance classification**, including the dimension jump to whole frequency lines at the exceptional gaps. Earlier work on the first-Hermite two-tone case establishes sharper gap-dependent counts at order one, but cannot imply line resonances or all-order sharpness.

## Limitations
The theorem does not give the exact number of isolated zeros at every nonresonant separation, nor their winding numbers. The finite multiplicity is precisely the sum of scalar branch orders, not an analytically continued complex multiplicity. The two-tone signal is periodic rather than square-integrable, but the STFT integral is absolutely convergent against each Hermite window. Historical priority relative to any unindexed exponential-polynomial or Hermite-window literature remains uncertain. No independent audit is asserted.

## References
1. C. Bellourak, S. Meignen, K. Polisano, M. Nahon, *Zeros of the Spectrogram of White Noise with Hermite Windows*, arXiv:2610.13531v1 (2026-10-09), https://arxiv.org/pdf/2610.13531.
2. S. Chand, J. Nolen, H.-T. Wu, *On spectral interference of the short-time Fourier transform and its nonlinear variations*, arXiv:2601.10910 (2026-01-15), https://arxiv.org/abs/2601.10910.
3. R. Alaifari, Y. Yang, *Multi-Window Approaches for Direct and Stable STFT Phase Retrieval*, arXiv:2410.05486 (2024-10-07), https://arxiv.org/abs/2410.05486.
