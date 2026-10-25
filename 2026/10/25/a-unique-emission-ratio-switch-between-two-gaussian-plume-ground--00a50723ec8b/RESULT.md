# A unique emission-ratio switch between two Gaussian-plume ground-level hotspots

## Finding

Consider two co-located horizontal point-source locations at distinct positive effective heights \(0<H_1<H_2\). In the steady Gaussian plume approximation with constant along-wind speed \(u>0\), reflected ground boundary, no deposition, and dispersion widths \(\sigma_y(x)=k_yx\), \(\sigma_z(x)=k_zx\) for \(k_y,k_z>0\), suppose emission rates are \(Q_1,Q_2>0\). The ground-level centerline concentration at downwind distance \(x>0\) is

\[
C(x)=\frac{Q_1e^{-H_1^2/(2k_z^2x^2)}+Q_2e^{-H_2^2/(2k_z^2x^2)}}{\pi u k_yk_zx^2}.
\]

Set \(r=(H_2/H_1)^2>1\), \(q=Q_2/Q_1\), and \(t=H_1^2/(2k_z^2x^2)\). The normalized profile is \(F_{r,q}(t)=t(e^{-t}+qe^{-rt})\). Write

\[
r_c=3+2\sqrt2,\qquad
 t_\pm(r)=\frac{r+1\pm\sqrt{r^2-6r+1}}{2r},\qquad
h_r(t)=e^{(r-1)t}\frac{1-t}{rt-1}.
\]

**Global-hotspot switch theorem.** For \(1<r\le r_c\) there is exactly one ground-level centerline maximum for every \(q>0\). For \(r>r_c\), put \(q_-(r)=h_r(t_-(r))\) and \(q_+(r)=h_r(t_+(r))\). Then \(0<q_-<q_+\); there are exactly two strict local maxima separated by one strict local minimum precisely when \(q_-<q<q_+\). Within that open interval there is exactly one \(q_b(r)\) at which the two maxima have **equal height** and are both global maximizers. For \(q_-<q<q_b\) the maximum closer to the stacks (smaller downwind \(x\)) is globally higher; for \(q_b<q<q_+\), the maximum farther downwind is globally higher. No endpoints or additional maxima compete. Outside the open interval, there is one global maximum; the endpoints \(q=q_\pm\) may have an additional stationary shoulder but not a second local maximum.

The balance parameter has the **large-height-contrast law**

\[
q_b(r)=r-e+\frac{e(1-e/2)}r+O(r^{-2})\quad(r\longrightarrow\infty).
\]

The **onset law** at \(r_c\), writing \(\delta=r-r_c\downarrow0\), is

\[
q_+(r)-q_-(r)\sim
\frac{8\,2^{3/4}e^{2\sqrt2}}{3r_c^2(1+\sqrt2)}\delta^{3/2},
\qquad
q_b(r)=q_c+q_c(6-4\sqrt2)\delta+o(\delta),
\]

where \(q_c=e^{2\sqrt2}/r_c\). At the balance point the two modal coordinates, ordered \(t_f<t_n\) (farther and nearer downwind respectively), satisfy

\[
t_n-t_f\sim\frac{2\sqrt{3\sqrt2}}{r_c}\sqrt\delta.
\]

In particular, varying the taller stack's emission rate continuously through \(q_b\) produces a discontinuous relocation of the global maximum concentration, while the maximized concentration itself is continuous.

## Assumptions and scope

All parameters are strictly positive, and sources are coincident in their horizontal coordinates but have unequal fixed effective heights. The receptor moves only along their common downwind, ground-level centerline. The wind direction and speed, turbulence-opening coefficients, effective heights, and first emission rate remain fixed as \(q\) varies. The classical Gaussian point-source approximation is steady, linear, reflected at the ground, and has no deposition, chemistry, terrain effects, downwash, wake interaction, or time-varying meteorology. The exactly linear dispersion-width assumption is essential to the stated universal constants. No assertion is made about full-plane maxima under moving wind or about a regulatory exposure measure.

## Proof

**1. Exact normalization and stationary points.** Direct substitution of \(t\) gives

\[
C(x)=\frac{2Q_1k_z}{\pi uk_yH_1^2}\,F_{r,q}(t),\qquad
F_{r,q}(t)=t(e^{-t}+qe^{-rt}).
\]

The change \(x\mapsto t\) is a bijection from \((0,\infty)\) onto \((0,\infty)\) reversing the coordinate order. Both limits of \(F\) at \(0\) and \(+\infty\) are zero, so every global maximum is interior. Differentiating gives

\[
F'_{r,q}(t)=e^{-t}(1-t)+qe^{-rt}(1-rt).
\]

For \(0<t\le1/r\), this derivative is positive, and for \(t\ge1\), negative. On \((1/r,1)\), its sign equals that of \(h_r(t)-q\). The logarithmic derivative of \(h_r\) is exactly

\[
\frac{h_r'(t)}{h_r(t)}
=(r-1)\left(1-\frac{1}{(1-t)(rt-1)}\right).
\]

The concave quadratic \((1-t)(rt-1)\), maximized at \((r+1)/(2r)\), exceeds one somewhere precisely when \((r-1)^2>4r\), equivalently \(r>r_c\). Thus for \(r\le r_c\), \(h_r\) is strictly decreasing from \(+\infty\) to zero, and there is exactly one maximum. For \(r>r_c\), \(h_r\) decreases from infinity to its strict minimum \(q_-\) at \(t_-\), increases to its strict maximum \(q_+\) at \(t_+\), then decreases to zero. Every \(q\in(q_-,q_+)\) has exactly three intersections \(1/r<t_f<t_m<t_n<1\); the signs of \(F'\) make \(t_f,t_n\) strict maxima and \(t_m\) a strict minimum. The remaining shape assertions follow from the same sign chart.

**2. Unique global-height exchange.** Denote the two peak heights by \(M_f(q)=F_{r,q}(t_f(q))\) and \(M_n(q)=F_{r,q}(t_n(q))\). The roots are smooth inside the open bimodality interval. The envelope identities give

\[
\frac{d}{dq}(M_f-M_n)
=t_fe^{-rt_f}-t_ne^{-rt_n}>0,
\]

because \(t\mapsto te^{-rt}\) is strictly decreasing on \((1/r,\infty)\). As \(q\downarrow q_-\), the first two critical points merge into a stationary shoulder; the surviving rightmost maximum is strictly higher. Hence \(M_f-M_n<0\) in that limit. As \(q\uparrow q_+\), the last two critical points merge and the surviving leftmost maximum is strictly higher, so \(M_f-M_n>0\) in that limit. The intermediate value theorem and strict derivative sign give one and only one balance \(q_b\), with the asserted strict global ordering on either side.

**3. Singular high-contrast comparison.** For \(r\to\infty\), the near-downwind mode has \(t=1+O(r^2e^{-r})\) when \(q/r\) remains bounded above and away from zero, and its height is \(e^{-1}+O(re^{-r})\). At the far-downwind mode put \(t=y/r\). For \(q=\kappa r+O(1)\), its leading profile is \(\kappa ye^{-y}\), whose maximum is \(\kappa/e\). The unique balance and comparison of these peaks force \(q_b/r\to1\). Write \(q_b=r+a+b/r+O(r^{-2})\); expanding the small-\(t\) peak uniformly for \(y\) near one gives

\[
F_{r,q_b}(y/r)=ye^{-y}+\frac{y+aye^{-y}}r
+\frac{-y^2+bye^{-y}}{r^2}+O(r^{-3}).
\]

The maximizing \(y\) is \(1+e/r+O(r^{-2})\); substituting yields far-mode height

\[
\frac1e+\frac{1+a/e}{r}
+\frac{-1+b/e+e/2}{r^2}+O(r^{-3}).
\]

Equating this with the exponentially close \(1/e\) near-mode height gives \(a=-e\), \(b=e(1-e/2)\). The smooth local maximizer equation near \(y=1\) and the strict balance derivative justify the indicated remainder by the implicit function theorem; terms from the other mode are exponentially small.

**4. Cusp and the width of the two-hotspot window.** Set \(t_c=2-\sqrt2\), \(q_c=e^{2\sqrt2}/r_c\) and \(q_{\mathrm{ref}}(r)=h_r(t_c)\). At \((t_c,r_c,q_c)\), the first three stationary derivative conditions coalesce. With \(\delta=r-r_c\) and \(s=t-t_c\), Taylor expansion of \(G=F'_{r,q}\), evaluated at \(q=q_{\mathrm{ref}}(r)\), gives uniformly near zero

\[
G(t_c+s,r,q_{\mathrm{ref}}(r))
=A\delta s+Bs^3+O(\delta^2|s|+\delta s^2+|s|^4),
\]

where the **explicit, nonzero** coefficients are

\[
A=\frac{2\sqrt2}{r_c}e^{-2+\sqrt2}>0,
\qquad B=-\frac{2r_c}{3}e^{-2+\sqrt2}<0.
\]

The corresponding stationary-parameter expansion is \(q-q_{\mathrm{ref}}=-(A\delta s+Bs^3)/G_q+o(\delta^{3/2})\), with \(G_q=(1-r_ct_c)e^{-r_ct_c}<0\). Its two folds occur at \(s=\pm\sqrt{-A/(3B)}\sqrt\delta+o(\sqrt\delta)\). Their separation in the \(q\) direction is \(4A\sqrt{-A/(3B)}\delta^{3/2}/(3|G_q|)+o(\delta^{3/2})\), which simplifies to the displayed window-width constant.

At the equal-height point, the scaled stationary derivative \(\delta^{-3/2}G(t_c+\sqrt\delta z,r,q)\) tends along subsequences to \(Az+Bz^3+G_q\beta\), where \(\beta=(q-q_{\mathrm{ref}})/\delta^{3/2}\) stays bounded. Integrating this cubic between its two outer roots gives their scaled height difference. As a function of \(\beta\), that difference is strictly monotone and vanishes at \(\beta=0\) by oddness; hence at balance \(\beta\to0\). The two outer roots therefore approach \(\pm\sqrt{-A/B}=\pm\sqrt{3\sqrt2}/r_c\), yielding the square-root separation. Finally, \(q_{\mathrm{ref}}(r)=q_c+q_c(6-4\sqrt2)\delta+O(\delta^2)\), proving the displayed linear balance onset. All limits are taken from \(r>r_c\).

## Verification

The standalone program `verification/verify_plume_hotspot.py` uses only the Python standard library, deterministic bisection, a fixed-seed randomized suite, independent physical normalization checks, and comparisons at the global and cusp thresholds. Execute it using `python3 verification/verify_plume_hotspot.py` after extracting this package. It checks 450 global-switch parameter sets, 120 physical normalizations, three cusp-limit approaches and four large-contrast cases. Its output is numerical corroboration; the universal statements are proved above.

For \(r=9\), the critical ratios are \(q_-\approx4.420142106601\), \(q_b\approx6.119571217609\), and \(q_+\approx20.252290288604\). At balance the three stationary \(t\)-coordinates are approximately \((0.169712209798,\ 0.426099613550,\ 0.981332067309)\), with two equal peak heights \(0.368691240492\) in the normalized profile. In downwind coordinates \(x/(H_1/k_z)\), the far and near maxima lie at approximately \(1.716439333\) and \(0.713800761\).

## Relationship to prior work

The Gaussian plume formula, its additivity across point sources and computational searches for maximum pollution concentration are established; none is claimed as new. In particular, Zoumakis (1998) optimizes worst-case multiple-source concentrations numerically over meteorology and receptor location, while Lushi and Stockie (2009) derive multiple-source plume inversion methods. These do not give the stated uniform, analytic emission-ratio **global-hotspot exchange** at fixed meteorology and distinct effective heights.

The normalized profile is also, up to a positive factor, a mixture of **shape-two gamma densities with unequal rates**. This is a genuine mathematical reduction, not merely an analogy. Ahmed, Goria and Hussein (2008) study bimodality and inflection geometry for gamma mixtures; Došlá (2009, Proposition 6) gives a necessary-and-sufficient equal-shape gamma-mixture bimodality criterion. Accordingly the local two-mode boundary \(r_c\) and its fold formulas are **pre-existing coverage**, used here as setup and not claimed as independently original. The distinct contribution assessed here is the unique global-height switch, its strict dominance ordering, the offset \(-e\) and next term in the large-height-ratio emission threshold, and the quantified cubic-cusp balancing law. Those statements were not located in the inspected primary passages. Since general mixture-density methods may imply them through additional arguments, historical originality remains provisional.

## Limitations

The result is exact only within a simplified Gaussian approximation with linear downwind dispersion widths and co-located horizontal sources. A switch of the **model's centerline concentration maximum** is not a claim about maximum population exposure, regulatory compliance, or hazard in real terrain; changes in plume rise, deposition, crosswind offsets, variable stability, chemical kinetics, or finite-distance receptor placement can alter the classification. A second plausible-source study of maxima for multiple sources is computational, rather than a uniqueness theorem, but a specialized previously unnoticed analytic treatment remains a residual priority risk. No independent validation has been conducted.

## References

1. N. M. Zoumakis (1998), “Characteristics of Maximum Concentrations from Multiple Point Sources,” *Journal of Applied Meteorology* **37**, 730–739, DOI `10.1175/1520-0450(1998)037<0730:COMCFM>2.0.CO;2`, published 1998-07-01.
2. S. E. Ahmed, M. N. Goria and A. Hussein (2008), “Gamma Mixture: Bimodality, Inflexions and L-Moments,” *Communications in Statistics—Theory and Methods* **37**, 1147–1161, DOI `10.1080/03610920701713286`.
3. Š. Došlá (2009), “Conditions for bimodality and multimodality of a mixture of two unimodal densities,” *Kybernetika* **45**, 279–292, Proposition 6, https://www.kybernetika.cz/content/2009/2/279/paper.pdf.
4. E. Lushi and J. M. Stockie (2009), “An inverse Gaussian plume approach for estimating atmospheric pollutant emissions from multiple point sources,” arXiv:0908.1589v1, first posted 2009-08-11, https://arxiv.org/abs/0908.1589.
