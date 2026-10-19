# A sharp charge-changing bifurcation in the first-Hermite spectrogram of two equal tones

## Finding
For each real frequency gap \(\Delta>0\), set \(d=\Delta/2\), \(f_\Delta(s)=e^{2\pi i d s}+e^{-2\pi i d s}\), and \(g(s)=s e^{-\pi s^2}\). The latter is the first Hermite function up to a nonzero constant. Define
\[
V_gf_\Delta(t,\nu)=\int_{\mathbb R}f_\Delta(s)g(s-t)e^{-2\pi i\nu s}\,ds.
\]
This absolutely convergent integral is meaningful for the bounded, non-square-integrable signal \(f_\Delta\). Its zero set is periodic in time with fundamental zero-period \(T=1/\Delta\). The following gives **every zero** on \(0\le t<T\), \(\nu\in\mathbb R\).

There is a unique \(v_{\mathrm{out}}>d\) satisfying
\[
\log\frac{v_{\mathrm{out}}+d}{v_{\mathrm{out}}-d}=4\pi d v_{\mathrm{out}}.
\]
Write \(\Delta_*=\sqrt{2/\pi}\). For \(0<\Delta\le\Delta_*\), the complete zero set is precisely
\[
\left\{(0,0),\left(\frac{T}{2},-v_{\mathrm{out}}\right),\left(\frac{T}{2},v_{\mathrm{out}}\right)\right\}.
\]
For \(\Delta>\Delta_*\), there is additionally a unique \(u\in(0,1)\) solving
\[
\frac{\operatorname{artanh}u}{u}=\frac{\pi\Delta^2}{2},
\]
and the complete zero set comprises the above three points and \((0,-du)\), \((0,du)\). In particular, the number of distinct zeros per time-frequency cylinder jumps **from three to five** at the sharp gap \(\Delta_*\).

Every zero off the threshold is regular. With the oriented coordinate order \((t,\nu)\), the two exterior zeros have Jacobian sign \(-1\) for all \(\Delta>0\); the central zero has sign \(+1\) below \(\Delta_*\) and \(-1\) above; the two additional interior zeros both have sign \(+1\). At the threshold the central zero alone is degenerate, with cubic transverse contact and local winding \(+1\). The total signed zero index per time period is always \(-1\).

The interior pair emerges with the square-root law
\[
\nu_{\mathrm{in}}=du=d\sqrt{3\varepsilon}\bigl(1+O(\varepsilon)\bigr),\qquad
\varepsilon=\frac{\pi\Delta^2}{2}-1\downarrow0.
\]

## Assumptions and scope
All quantifiers refer to real \(\Delta>0\), real time \(t\), and real frequency \(\nu\). A zero means an exact complex zero of the indicated STFT, not a spectrogram local minimum or a numerically small value. Charges are local degrees (phase windings) of the complex STFT around isolated zeros using the positively oriented \((t,\nu)\)-plane. The frequency origin is the midpoint of the two equal-amplitude tones, and no claim is made for unequal amplitudes, higher Hermite orders, noisy signals, or arbitrary signals. Changing the nonzero normalization of the first Hermite window does not affect the zeros or winding signs.

## Proof
The Fourier transform of \(s e^{-\pi s^2}\) under the indicated convention is \(-i\nu e^{-\pi\nu^2}\). Thus, with
\[
A(\nu)=(\nu-d)e^{-\pi(\nu-d)^2},\qquad
B(\nu)=(\nu+d)e^{-\pi(\nu+d)^2},\qquad
\theta=\pi\Delta t,
\]
we have the exact nonvanishing-gauge factorization
\[
V_gf_\Delta(t,\nu)=-i e^{-2\pi i\nu t}W(t,\nu),\qquad
W=Ae^{i\theta}+Be^{-i\theta}
=(A+B)\cos\theta+i(A-B)\sin\theta.
\]
For real \(\nu\), both \(A\) and \(B\) are real, and they cannot vanish simultaneously because \(d>0\). Hence \(W=0\) is equivalent to one of two exclusive alternatives: \(\sin\theta=0\) and \(A+B=0\), or \(\cos\theta=0\) and \(A-B=0\). Modulo \(T\), these force respectively \(t=0\) and \(t=T/2\).

If \(|\nu|<d\), then \(A<0<B\). Only \(A+B=0\) is possible. The symmetry \(A(-\nu)=-B(\nu)\) shows that \(\nu=0\) is always a root and nonzero roots occur in opposite pairs. For \(0<\nu<d\), put \(u=\nu/d\). Cancellation becomes
\[
\frac{d-\nu}{d+\nu}=e^{-4\pi d\nu}
\quad\Longleftrightarrow\quad
\frac{\operatorname{artanh}u}{u}=2\pi d^2=\frac{\pi\Delta^2}{2}.
\]
The function \(u\mapsto\operatorname{artanh}(u)/u\) is strictly increasing on \((0,1)\), from \(1\) to infinity: use the positive termwise derivative of its power series \(\sum_{k\ge0}u^{2k}/(2k+1)\). Thus an interior positive root exists uniquely exactly when \(2\pi d^2>1\), and the only interior roots are \(0\) and, above the threshold, \(\pm du\). No zero exists at \(\nu=\pm d\), where precisely one of \(A,B\) vanishes.

If \(\nu>d\), then \(A,B>0\), so only \(A-B=0\) is possible. It is equivalent to
\[
H(\nu):=\log\frac{\nu+d}{\nu-d}-4\pi d\nu=0.
\]
Here \(H'(\nu)=-2d/(\nu^2-d^2)-4\pi d<0\), while \(H(\nu)\to+\infty\) as \(\nu\downarrow d\) and \(H(\nu)\to-\infty\) as \(\nu\to\infty\). There is therefore exactly one positive exterior root. The same symmetry yields its negative, and there are no other cases. This proves the complete zero classification.

For regularity and charge, note that multiplication by the nonzero complex gauge in the factorization preserves local Jacobian orientation. Let \(F=A+B\) and \(G=A-B\). At \(t=0\) the Jacobian determinant of \((\operatorname{Re}W,\operatorname{Im}W)\) with column variables \((t,\nu)\) is
\[
J_0=-\pi\Delta\,G(\nu)F'(\nu).
\]
For \(|\nu|<d\), \(G<0\), and \(F'(0)=2(1-2\pi d^2)e^{-\pi d^2}\). Thus the central sign changes at the stated threshold. At each nonzero interior root above the threshold, the positive-side ratio
\[
R(\nu)=\frac{|A(\nu)|}{B(\nu)}
=\frac{d-\nu}{d+\nu}e^{4\pi d\nu}
\]
crosses strictly downward through \(1\), by strict increase of \(\operatorname{artanh}(u)/u\); hence \(F'(\nu)>0\) there. By reflection \(F'\) is even. These two roots therefore each have positive Jacobian.

At \(t=T/2\), the Jacobian is
\[
J_{1/2}=-\pi\Delta\,[A(\nu)+B(\nu)]\,[A'(\nu)-B'(\nu)].
\]
For \(\nu>d\), the quotient \(A/B\) crosses \(1\) strictly upward since \(\frac d{d\nu}\log(A/B)=2d/(\nu^2-d^2)+4\pi d>0\). Hence \(A+B>0\) and \(A'-B'>0\) at the exterior zero; the Jacobian is negative. Reflection proves the same conclusion for the negative exterior zero.

At \(\Delta=\Delta_*\), direct differentiation gives \(F'(0)=0\), \(F'''(0)=8\pi e^{-1/2}\), and therefore
\[
F(\nu)=\frac{4\pi}{3}e^{-1/2}\nu^3+O(\nu^5).
\]
The imaginary time derivative at this zero is \(\partial_t W(0,0)=-i4\pi d^2e^{-1/2}\ne0\). Near the zero, the imaginary equation forces \(t=0\) while the real equation has the displayed cubic contact, giving local degree \(+1\). Finally \(\operatorname{artanh}(u)/u=1+u^2/3+O(u^4)\) yields the stated square-root law. The sum of indices is \((+1)-2=-1\) below, \((-1)+2-2=-1\) above, and \((+1)-2=-1\) at the threshold.

## Verification
A standalone Python-standard-library script, `verify.py`, checks analytic STFT values against direct quadrature, numerically isolates both types of zero, evaluates analytic Jacobians and verifies the cubic leading term at the critical gap. Run it with `python verify.py` from the extracted package directory. This script is supplementary: all quantified statements above follow from the exact proof, not an extrapolation from numerical cases. The check's finite gap list stays away from the nearly singular large-gap floating-point regime.

## Relationship to prior work
Bellourak, Meignen, Polisano, and Nahon analyze Hermite-window spectrogram zeros and their positive/negative local charges for complex white noise; their results concern stochastic zero intensities and pair correlations, not the deterministic equal-two-tone zero census or its sharp separation threshold. Chand, Nolen, and Wu analyze two-component spectral interference and phase zeros with a Gaussian window, including auxiliary differentiated-window expressions in reassignment analysis; these do not classify first-Hermite STFT zeros. Poinas and Bardenet derive a Gaussian-window zero lattice for pairs of parallel chirps, again with a different window. The contribution here is the complete first-Hermite two-tone bifurcation diagram, including interior/exterior root equations, precise index transfer, and the unique cubic transition.

## Limitations
The tone signal is tempered but not in \(L^2(\mathbb R)\). Nothing is asserted about perturbation stability, noise, unequal weights, or higher Hermite order. The result is a deterministic time-frequency theorem, not a statistical claim or an independent audit of historical priority. Its exact gap is specific to the window \(s e^{-\pi s^2}\) and this Fourier normalization.

## References
- C. Bellourak, S. Meignen, K. Polisano, M. Nahon, *Zeros of the Spectrogram of White Noise with Hermite Windows*, arXiv:2610.13531v1 (first submitted 2026-10-09). https://arxiv.org/pdf/2610.13531
- S. Chand, J. Nolen, H.-T. Wu, *On spectral interference of the short-time Fourier transform and its nonlinear variations*, arXiv:2601.10910 (first submitted 2026-01-15). https://arxiv.org/abs/2601.10910
- A. Poinas, R. Bardenet, *On two fundamental properties of the zeros of spectrograms of noisy signals*, arXiv:2507.13829 (first submitted 2025-07-18). https://arxiv.org/pdf/2507.13829
