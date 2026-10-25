# A sharp double-peak onset and unique global-brightness switch for a Lambertian eccentric exoplanet

## Finding

A perfectly Lambert-reflecting spherical planet on an eccentric Kepler orbit can have competing reflected-light peaks: one at full phase, the others away from full phase. For an edge-on orbit whose periastron coincides with new phase and apastron with full phase, the complete idealized phase diagram has a sharp fold eccentricity \(e_{\mathrm f}\approx0.324898008977667\) and a strictly larger, **unique global-brightness exchange** \(e_{\mathrm s}\approx0.325836262906187\), both below \(1/3\). Two off-full stationary maxima are born at the fold, but they become globally brightest only at the exchange. The full-phase peak survives as a strict local maximum for \(e_{\mathrm s}<e<1/3\), so the transition concerns *global* dominance rather than just local stability.

Formally, let \(f\in[0,\pi]\) be the true anomaly from periastron to apastron and let
\[
B_e(f)=\frac{(1+e\cos f)^2}{\pi}(\sin f-f\cos f), \qquad 0\le e<1.
\]
The full orbital curve is obtained by reflection about apastron. Write
\[
T(f)=\frac{2\sin f}{f}-3\cos f\quad(0<f\le\pi).
\]
There is a unique \(f_0\in(0,\pi)\) maximizing \(T\), characterized by
\[
(3f_0^2-2)\sin f_0+2f_0\cos f_0=0.
\]
The maximum obeys \(T(f_0)>3\); set \(e_{\mathrm f}=1/T(f_0)<1/3\).

For \(0\le e<e_{\mathrm f}\), the apastron/full-phase point is the unique global maximum. At equality the one half-orbit has an interior horizontal stationary point that is not an extremum. For \(e_{\mathrm f}<e<1/3\), exactly two interior stationary points \(f_-(e)<f_0<f_+(e)<\pi\) exist: the first is a strict local maximum and the second a strict local minimum. Apastron remains a strict local maximum. There is a unique \(e_{\mathrm s}\in(e_{\mathrm f},1/3)\) such that
\[
B_{e_{\mathrm s}}(f_-(e_{\mathrm s}))=B_{e_{\mathrm s}}(\pi)=(1-e_{\mathrm s})^2.
\]
Below \(e_{\mathrm s}\) the full-phase peak is globally greatest; above it the pair of off-full peaks is globally greatest. At \(e_{\mathrm s}\), precisely three full-orbit maxima tie: the apastron point and two symmetric off-full anomalies. For \(1/3\le e<1\), the apastron point is a local minimum and the two symmetric off-full peaks are the only global maxima. At \(e=1/3\) the apastron minimum is degenerate.

Numerically, \(f_-(e_{\mathrm s})\approx2.813426935188429\), the common normalized brightness is about \(0.454496744412295\), and the global maximizer jumps \(0.328165718401364\) radians from full phase. This change is small in flux height but finite in angular location.

## Assumptions and scope

The planet is a perfectly Lambertian sphere with fixed scattering/albedo and radius. The stellar source is point-like, the Kepler orbit is fixed with eccentricity \(0\le e<1\), and the observer views it edge-on with periastron at new phase and apastron at full phase. Thermal emission, finite star size, eclipses, transits, occultations, atmospheric variability, rings and instrumental noise are excluded. The phase-angle law for the illuminated Lambert sphere is \(\Phi(\alpha)=[\sin\alpha+(\pi-\alpha)\cos\alpha]/\pi\). Here \(\alpha=\pi-f\) on the outbound half, so \(\Phi=(\sin f-f\cos f)/\pi\). The star–planet inverse-square illumination contributes \((1+e\cos f)^2\) after division by its positive orbit-wide scale; this positive normalization does not change peak locations or comparisons. Monotonic motion in true anomaly means extrema in true anomaly correspond to extrema in observation time away from endpoints. Full phase is included even though actual eclipses are explicitly excluded.

## Proof

**1. Stationary points and their order.** Put \(U(f)=\sin f-f\cos f\). For \(0<f<\pi\), \(U'(f)=f\sin f>0\) and \(U(f)>0\). Direct differentiation yields the exact factorization
\[
\pi B'_e(f)=(1+e\cos f) f\sin f\,[1-eT(f)].
\]
All prefactors are strictly positive for \(0<f<\pi\), \(0\le e<1\). Therefore the positive-anomaly stationary points are exactly the intersections \(T(f)=1/e\) for \(e>0\); for \(e=0\) there are none.

Now
\[
f^2T'(f)=G(f):=(3f^2-2)\sin f+2f\cos f,
\quad G'(f)=f(4\sin f+3f\cos f).
\]
The bracket is positive through \(\pi/2\) and strictly decreasing on \((\pi/2,\pi)\) because its derivative is \(7\cos f-3f\sin f<0\). It has one zero in that interval. Consequently \(G\), which starts at zero, first increases and then decreases strictly to \(G(\pi)=-2\pi<0\), crossing zero exactly once. This proves that \(T\) strictly increases on \((0,f_0)\) and decreases on \((f_0,\pi)\). Furthermore \(T(0+)=-1\), \(T(\pi)=3\), \(T'(\pi)=-2/\pi<0\), and thus \(T(f_0)>3\). The stated classification and the signs \(+, -, +\) of \(B'_e\) for \(e_{\mathrm f}<e<1/3\) follow immediately. For \(e\ge1/3\), only the increasing-branch intersection lies strictly in the interval; \(B'_e\) is negative from that peak to \(\pi\), proving that full phase is a local minimum (possibly degenerate at equality). Symmetry gives the complete full-orbit counts.

**2. Exactly one global-height exchange.** For \(e_{\mathrm f}<e<1/3\), define \(f_-(e)\) as the inverse of the increasing restriction of \(T\). Its local-maximum brightness is \(M(e)=B_e(f_-(e))\). Let \(D(e)=\log[M(e)/(1-e)^2]\). Because \(B'_e(f_-(e))=0\), the envelope theorem here is simply the chain rule, and gives
\[
D'(e)=\frac{2\cos f_-(e)}{1+e\cos f_-(e)}+\frac{2}{1-e}
=\frac{2[1+\cos f_-(e)]}{(1-e)[1+e\cos f_-(e)]}>0.
\]
At \(e=e_{\mathrm f}\), the interior stationary point does not reverse the increasing trend, so its brightness is strictly below \(B_e(\pi)\); thus \(D\) is negative immediately above the fold. At \(e=1/3\), \(B'_e<0\) between the surviving interior maximum and the endpoint, so that maximum is strictly brighter than the endpoint; thus \(D\) is positive immediately below \(1/3\). Continuity and strict monotonicity imply exactly one zero \(e_{\mathrm s}\), and establish all global comparisons, including endpoint cases.

**3. Exact implicit characterization.** At a stationary peak set \(V(f)=2\sin f-3f\cos f=fT(f)\). Then \(e=f/V\), \(1+e\cos f=2U/V\), and \(1-e=(V-f)/V\). Equality of off-full and apastron heights becomes
\[
4U(f)^3=\pi[V(f)-f]^2.
\]
The solution defining \(e_{\mathrm s}\) is the unique solution on the *increasing branch* of \(T\) for which \(3<T(f)<T(f_0)\), namely \(f\in(f_a,f_0)\), where \(T(f_a)=3\). Other formal solutions outside this restricted branch do not define this dominance exchange.

**4. Fold onset.** At the maximum \(T'(f_0)=0\) and \(T''(f_0)=G'(f_0)/f_0^2=[4\sin f_0+3f_0\cos f_0]/f_0<0\). Taylor expansion of \(T(f)=1/e\) at \((e_{\mathrm f},f_0)\) gives
\[
f_\pm(e)=f_0\pm\sqrt{\frac{2}{-e_{\mathrm f}^2T''(f_0)}}\sqrt{e-e_{\mathrm f}}+O(e-e_{\mathrm f}).
\]
Thus the two extrema separate with a square-root law, but the global-height exchange is strictly later.

## Verification

The accompanying `verify_lambert.py` is standalone Python using only the standard library. It independently checks 4,500 fourth-order finite-difference derivative comparisons, 513 full-domain grids (3,201 points each) against the analytically classified maxima, existence/sign comparisons of stationary points, exact phase-order checks, and sample monotonic-envelope derivative comparisons. It reports \(e_{\mathrm f}=0.324898008977667\) and \(e_{\mathrm s}=0.325836262906187\). These are numerical checks, not replacements for the continuous proofs above. Reproduce with `python3 verify_lambert.py`.

## Relationship to prior work

The Lambert sphere phase function, inverse-square orbital illumination and eccentric-orbit reflected-light curves are established. Arnold and Schneider (2004) use Lambertian reflection in their planet/ring photometry and study circular orbital geometry in the inspected sections. Dyudina and coauthors (2004 preprint; 2005 journal article) numerically exhibit the substantial role of eccentricity and shifted/double-brightness peaks for Jupiter/Saturn scattering laws, including Lambert-like comparisons. Sudarsky and coauthors (2005) analyze eccentric planet phase curves and offsets of optical maxima in their more physical wavelength-dependent models. Those sources establish **qualitative** light-curve complexity; it is not attributed to this result. The result isolated here is the **exact eccentricity-domain classification** for the specified aligned Lambertian baseline, including its one fold, unique global-height crossover, intermediate three-maxima regime and explicit square-root onset. Coverage by a more general, as-yet-unidentified phase-curve optimization theorem remains a historical-priority risk.

## Limitations

The exact periastron/new-phase alignment and edge-on geometry are special. Fixed Lambert scattering, suppressed eclipses, prescribed orbital elements and absent observational noise limit physical inference. The brightness separation close to the crossover is very small. The theorem is not an assertion that a real exoplanet light curve permits reliable recovery of the global-switch eccentricity. The classification is mathematical for the normalized ideal response; it is not a claim about atmospheric physics, instrument sensitivity, or arbitrary viewing orientations.

## References

- Arnold, L. and Schneider, J. (2004), *The detectability of extrasolar planet surroundings I. Reflected-light photometry of unresolved rings*, arXiv:astro-ph/0403330 (first public submission 2004-03-13), https://arxiv.org/abs/astro-ph/0403330.
- Dyudina, U. A., et al. (2004), *Phase light curves for extrasolar Jupiters and Saturns*, arXiv:astro-ph/0406390 (first public submission 2004-06-17), https://arxiv.org/abs/astro-ph/0406390.
- Sudarsky, D., Burrows, A., Hubeny, I. and Li, A. (2005), *Phase functions and light curves of wide-separation extrasolar giant planets*, arXiv:astro-ph/0501109 (first public submission 2005-01-06), https://arxiv.org/abs/astro-ph/0501109.
