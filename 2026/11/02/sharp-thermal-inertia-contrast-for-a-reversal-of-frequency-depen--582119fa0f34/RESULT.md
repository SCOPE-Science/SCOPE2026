# Sharp thermal-inertia contrast for a reversal of frequency-dependent planetary phase lag

## Finding

A disk-integrated two-surface thermal response can have a phase lag that *decreases* as the forcing frequency increases, although neither individual surface can do this. This happens for a mixture of two independent first-order radiative relaxation responses **if and only if** their relaxation-time ratio exceeds the universal constant
\[
r_c=7+4\sqrt{3}=13.9282032302755\ldots,
\]
and the surface mixing weight lies in an explicit open interval specified below. At smaller contrasts the lag is strictly increasing for every positive mixture. At the threshold the only exceptional mixture has one horizontal tangent but no lag reversal. Above the threshold every reversing mixture has exactly one local maximum and one later local minimum; no additional turns are possible.

## Assumptions and scope

Two thermal-response regions obey the independent linear equations
\[
\tau_j\dot y_j(t)+y_j(t)=u(t),\qquad j=1,2,
\]
where \(0<\tau_1<\tau_2\). Their measured linearized signal is \(y(t)=f y_1(t)+(1-f)y_2(t)\) with \(0<f<1\). Assume common sinusoidal forcing \(u(t)=\operatorname{Re}(e^{i\omega t})\), positive angular frequency \(\omega>0\), and no frequency-dependent observational weights or inter-region heat exchange. A constant positive overall gain does not affect phase.

Set \(a=\tau_1\), \(r=\tau_2/\tau_1>1\), and \(m=1+f(r-1)\), so \(1<m<r\). The complex transfer response and its positive principal phase lag are
\[
H(\omega)=\frac{f}{1+i a\omega}+\frac{1-f}{1+i ra\omega}
=\frac{1+i ma\omega}{(1+i a\omega)(1+i ra\omega)},
\]
\[
\Phi(\omega)=-\arg H(\omega)
=\arctan(a\omega)+\arctan(ra\omega)-\arctan(ma\omega).
\]
Because each constituent response has positive real part and negative imaginary part, \(0<\Phi(\omega)<\pi/2\) without an angle-branch ambiguity.

**Complete classification.** Define
\[
m_{\pm}(r)=\frac{r^2-6r+1\pm(r-1)\sqrt{r^2-14r+1}}{2(r+1)},\qquad
f_{\pm}(r)=\frac{m_{\pm}(r)-1}{r-1}.
\]
If \(1<r<r_c\), \(\Phi\) is strictly increasing on \((0,\infty)\) for all \(f\in(0,1)\). If \(r=r_c\), the same remains true; a unique mixture \(m=\sqrt r\), or \(f=(\sqrt r+1)^{-1}\), has a horizontal tangent at \(\omega=1/\sqrt{\tau_1\tau_2}\), and otherwise the derivative is positive. If \(r>r_c\), then \(1<m_-(r)<m_+(r)<r\), and the lag has exactly two distinct critical frequencies, with a strict local maximum followed by a strict local minimum, precisely when
\[
f_-(r)<f<f_+(r).
\]
Outside that open interval the lag is strictly increasing; at its two endpoints it has one horizontal tangent but no reversal. These assertions hold for all continuous \(\omega>0\), without discretization.

In the reversing regime write
\[
C=1+r-m,\quad B=(r+1)m^2-(r^2+1)m+r(r+1),\quad A=rm((r+1)m-r),\quad \Delta=B^2-4AC.
\]
Here \(A,C>0\), \(B<0\), \(\Delta>0\). The complete critical-frequency formula is
\[
\omega_{\pm}=\frac1a\sqrt{\frac{-B\pm\sqrt\Delta}{2A}},
\]
where \(\omega_-<\omega_+\), the former is a strict local maximum of \(\Phi\), and the latter a strict local minimum.

## Proof

Differentiate the exact phase expression, and introduce \(x=(a\omega)^2\). Direct collection over a positive denominator gives
\[
\Phi'(\omega)=a\frac{C+Bx+Ax^2}{(1+x)(1+r^2x)(1+m^2x)}.
\]
For \(1<m<r\), \(C=1+r-m>0\) and \(A=rm((r+1)m-r)>0\). Therefore a negative-derivative interval exists precisely when the numerator quadratic has two distinct positive zeros, equivalent to \(B<0\) and \(\Delta>0\).

The exact discriminant factors as
\[
\Delta=(r-m)(m-1)(r+1)Q_r(m),
\]
where
\[
Q_r(m)=-(r+1)m^2+(r^2-6r+1)m-r(r+1).
\]
The auxiliary identity \(B+Q_r(m)=-6rm\) implies that \(Q_r(m)>0\) automatically forces \(B<0\). Hence the lag reverses if and only if \(Q_r(m)>0\). This equivalence includes the positive-zero requirement and does not rely on numerical root searches.

As a concave quadratic in \(m\), \(Q_r\) has discriminant
\[
\operatorname{Disc}_m(Q_r)=(r-1)^2(r^2-14r+1).
\]
For \(1<r<7+4\sqrt3\), the discriminant is negative and \(Q_r(m)<0\) everywhere. At \(r=r_c\), its unique zero is \(m=\sqrt r\). In that case the derivative numerator has a repeated positive zero at \(x=1/r\); it remains nonnegative and vanishes at only one frequency, implying strict monotonicity of \(\Phi\) as a function, not a reversal.

For \(r>r_c\), observe that \(Q_r(1)=-8r<0\), \(Q_r(r)=-8r^2<0\), but
\[
Q_r(\sqrt r)=\sqrt r(\sqrt r+1)^2(r-4\sqrt r+1)>0.
\]
Consequently the two distinct roots lie strictly within \((1,r)\), and solving the quadratic gives \(m_-\) and \(m_+\) above. The inequality \(Q_r(m)>0\) holds exactly between these roots. In that interval the derivative numerator changes signs positive–negative–positive as \(x\) increases, establishing the two critical frequencies and their types. At each boundary \(Q_r=0\), the positive derivative polynomial is a perfect square times \(A\), with only one isolated zero, so \(\Phi\) remains strictly increasing. This completes all cases.

## Verification

The standalone \(\texttt{verify.py}\) checks the transfer-function reduction, derivative polynomial, factorization of the discriminant, threshold factorization and stationary-frequency identity by exact symbolic algebra. It additionally tests 108 rational parameter pairs at five positive frequencies each, checks the derivative signs using exact expressions, and reproduces the explicit reversing example. The checker prints \(\texttt{VERIFY_OK assertions= 879}\) on a successful run. It is a diagnostic replay, not a substitute for the algebraic proof of statements quantified over all real parameters.

For \(\tau_1=1\), \(\tau_2=20\), and \(m=\sqrt{20}\) (so \(f=(\sqrt{20}+1)^{-1}\)), the local maximum and minimum occur at \(\omega_-=0.14196407209494566\ldots\) and \(\omega_+=0.3522017878337553\ldots\). The lag falls by approximately \(2.5336814273\) degrees between them. Every single-pole constituent remains strictly increasing in lag throughout.

## Relationship to prior work

The motivating planetary heat-storage literature identifies disk-integrated mixing of slow (ocean) and fast (land/sea-ice) thermal responses as an obstacle to reading thermal inertia from measured phase lags. Cowan, Voigt and Abbot derive a single-relaxation linear phase-lag relation and discuss this mixed-surface limitation. The present statement is not their single-pole result: it classifies, with a sharp universal contrast threshold and all equality cases, when positive parallel sums of *two* such responses have nonmonotone **phase as frequency varies**. Relevant earlier work on terrestrial lightcurves considers inverse thermal characterization but does not supply the present algebraic classification in the accessible material inspected. The question also translates to the phase of a positive two-Debye parallel transfer function; an earlier result in the broader network/filter literature may cover it without planetary terminology.

## Limitations

This is an exact theorem for a fixed, two-component **linear time-invariant** model, not a result for nonlinear radiative cooling, atmospheric transport, coupled reservoirs, a frequency-dependent mixing weight, a full planetary climate model, or empirical detectability. Inferring both constituent time constants from observations is not proved. The two-component threshold does not assert an analogue for three or more components. Historical priority has not been independently established; specifically a related 2004 seasonal-lightcurve article was available only at abstract level, and equivalent results could exist in general linear-filter literature.

## References

1. N. B. Cowan, A. Voigt and D. S. Abbot, *Thermal Phases of Earth-Like Planets: Estimating Thermal Inertia from Eccentricity, Obliquity, and Diurnal Forcing*, arXiv:1205.5034v1, first public 2012-05-22, https://arxiv.org/abs/1205.5034 .
2. E. Gaidos and D. M. Williams, *Seasonality on terrestrial extrasolar planets: Inferring obliquity and surface conditions from infrared light curves*, New Astronomy 10 (2004), 67–77, https://doi.org/10.1016/j.newast.2004.04.009 .
3. E. Gaidos, N. Moskovitz and D. M. Williams, *Terrestrial Exoplanet Light Curves*, arXiv:astro-ph/0511668v1, first public 2005-11-23, https://arxiv.org/abs/astro-ph/0511668 .
