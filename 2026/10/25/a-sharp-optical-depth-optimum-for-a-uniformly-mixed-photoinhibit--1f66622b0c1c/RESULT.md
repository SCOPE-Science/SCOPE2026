# A sharp optical-depth optimum for a uniformly mixed photoinhibited water column

## Finding

Fix a water-column depth \(L>0\), a physiological optimal irradiance \(I_*>0\), and a surface irradiance \(I_s=qI_*\) with \(q>0\). Under the classical Steele photoinhibition response and exponential light attenuation, the depth-mean instantaneous gross photosynthetic rate has a **complete optical-depth classification**. For \(0<q\le1\), zero attenuation is its unique maximum. For every \(q>1\), there is exactly one positive optimal optical depth \(t_*(q)\), and this optimum increases strictly with surface irradiance. It has the two sharp asymptotic regimes

\[
 t_*(q)=\frac32(q-1)+O((q-1)^2)\quad(q\downarrow1),
 \qquad
 t_*(q)=\log q+\log\log q+o(1)\quad(q\to\infty).
\]

The extreme-light law identifies the unusual double-logarithmic increase in the optimal attenuation beyond the usual \(\log q\) penetration scale. This is an exact conditional result for a *frozen photosynthetic response*, not a claim that increasing natural-water turbidity always improves ecosystem productivity.

## Assumptions and scope

Let \(P_{\max}>0\) be the peak per-unit-biomass photosynthetic rate. Throughout the comparison, hold the biomass density, \(P_{\max}\), \(I_*\), \(I_s\), and \(L\) fixed. The instantaneous response is Steele's curve

\[
 P(I)=P_{\max}\frac{I}{I_*}\exp\!\left(1-\frac{I}{I_*}\right),\qquad I\ge0.
\]

The stationary vertical light field obeys Beer attenuation \(I(z)=I_s e^{-kz}\), for depth \(0\le z\le L\) and adjustable attenuation coefficient \(k\ge0\). The optimized objective is the uniformly biomass-weighted depth-average instantaneous gross rate, not depth-integrated net growth or seasonally varying production. Define \(t=kL\) and

\[
 M_q(t)=\frac1{LP_{\max}}\int_0^L P(I_s e^{-kz})\,dz.
\]

With the continuous value at \(t=0\), direct integration gives

\[
 M_q(t)=\frac e t\bigl(e^{-q e^{-t}}-e^{-q}\bigr)\quad(t>0),
 \qquad M_q(0)=q e^{1-q}.
\]

All conclusions are for every \(q>0\) and every \(k\ge0\) within these precise assumptions.

## Proof

**1. Exact integration and the sharp transition.** Introduce

\[
 f_q(u)=q e^{-u}e^{-q e^{-u}},\qquad
 M_q(t)=\frac e t\int_0^t f_q(u)\,du.
\]

Indeed, the substitution \(v=q e^{-u}\) evaluates the integral as \(e^{-q e^{-t}}-e^{-q}\). Since

\[
 f_q'(u)=f_q(u)(q e^{-u}-1),
\]

for \(q\le1\) this integrand is strictly decreasing on \(u>0\); hence its initial running mean is strictly decreasing on \(t>0\), with unique maximum \(t=0\).

For \(q>1\), define

\[
 g_q(t)=t f_q(t)-\int_0^t f_q(u)\,du.
\]

The sign of \(M'_q(t)\) is the sign of \(g_q(t)\). For \(t>0\),

\[
 g_q'(t)=t f_q'(t).
\]

Thus \(g_q\) increases strictly from zero on \((0,\log q)\), then decreases strictly on \((\log q,\infty)\). Moreover

\[
 \lim_{t\to\infty}g_q(t)=-(1-e^{-q})<0
\]

because \(t f_q(t)\to0\) and \(\int_0^\infty f_q=1-e^{-q}\). Consequently exactly one zero \(t_*(q)>\log q\) exists, with \(M_q\) increasing strictly before it and decreasing strictly afterward. As \(M_q(t)\to0\) at infinity, this zero is the unique global maximum.

**2. An exact equation and strict parameter monotonicity.** Put \(y=q e^{-t}\). The zero condition is equivalent to

\[
 G(q,t):=t y-1+e^{y-q}=0.
\]

At its solution, \(0<y<1\), because \(t>\log q\). Holding \(q\) fixed and differentiating gives

\[
 \partial_tG=t y(y-1)<0.
\]

At the same zero, write \(d=q-y>0\). Differentiation at fixed \(t\), followed by using \(t y=1-e^{-d}\), gives

\[
 \partial_qG=\frac{1-(1+d)e^{-d}}q>0,
\]

since \(e^d>1+d\) for \(d>0\). By the implicit-function theorem,

\[
 \frac{dt_*}{dq}=-\frac{\partial_qG}{\partial_tG}>0
\]

for all \(q>1\). The optimal optical depth grows strictly with surface irradiance.

**3. Near-onset asymptotic.** The unique zero tends to zero as \(q\downarrow1\): otherwise a positive limiting zero would contradict the strictly decreasing running mean at \(q=1\). Taylor expansion at \(u=0\) yields

\[
 g_q(t)=\frac12 f'_q(0)t^2+\frac13 f''_q(0)t^3+O(t^4),
\]

uniformly for \(q\) near one and \(t\) near zero, with

\[
 f'_q(0)=q e^{-q}(q-1),\qquad
 f''_q(0)=q e^{-q}\bigl((q-1)^2-q\bigr).
\]

The analytic continuation of \(g_q(t)/t^2\) has, at \((q,t)=(1,0)\), partial derivatives \(1/(2e)\) with respect to \(q\) and \(-1/(3e)\) with respect to \(t\). The implicit-function theorem gives

\[
 t_*(q)=\frac32(q-1)+O((q-1)^2).
\]

**4. High-light asymptotic.** At the unique optimum, \(y=q e^{-t_*}<1\) and

\[
 t_*y=1-e^{y-q}=1+O(e^{-q}).
\]

(The error is uniform because \(0<y<1\).) Since \(t_*>\log q\), we have \(t_*\to\infty\), and hence \(y\sim1/t_*\). Taking logarithms of \(y=q e^{-t_*}\) gives

\[
 t_*=\log q+\log t_*+O(e^{-q}).
\]

This implies first \(t_*/\log q\to1\) (for large \(t_*\), \(\log t_*=o(t_*)\)), and therefore \(\log t_*=\log\log q+o(1)\). Thus

\[
 t_*(q)=\log q+\log\log q+o(1),\quad
 q e^{-t_*(q)}\sim\frac1{\log q},\quad
 M_q(t_*(q))\sim\frac e{\log q}.
\]

This concludes the classification and asymptotics.

## Verification

The independently executable standard-library program `verify.py` evaluates the exact integral against Simpson quadrature for 400 deterministic parameter cases; checks the decreasing regimes for five \(q\) values; checks twelve supercritical optima, sign brackets and monotonicity; tests three near-onset scales and four high-light cases. It is not a substitute for the analytical proof. Execute it as `python verify.py`.

For \(q=2\) the unique optimal depth is approximately \(t_*=1.081888832312\), with normalized mean gross rate \(M_2(t_*)=0.935521607887\); at \(t=0\) it is \(2/e=0.735758882343\). This is a model-relative improvement, not a field prediction.

## Relationship to prior work

Steele (1962) introduced the light-response curve incorporating high-light photoinhibition. Ryther (1956) formulated depth and daily integration for photosynthesis. Bannister (1974, especially equation (20)) wrote a general water-column production integral with the same Steele exponential kernel, and is a particularly close antecedent for the **formula**, not an original source of the optical-depth integral itself. Walsby (1997) studied numerical integration under time-dependent light and vertically varying populations. Their inspected materials do not state the present all-\(q\) unique optimum, strict monotonicity of its depth, or both of the sharp asymptotic laws. Therefore, the contribution is the **global optimization classification and its scales**, not the underlying photosynthesis law or the integrated-production formula.

Idso and Foster (1975) analytically studied several kinds of depth-integrated photosynthetic response, including complete inhibition. Their abstract is directly relevant, but a complete text was unavailable for checking whether a more general result implies this optimization. Murphy (1962) studied mixing depth, turbidity and water productivity under a different feedback formulation; only its abstract was available. Earlier or more general literature on optimizing uniform running averages of unimodal response functions may also subsume part of the result. These are residual originality risks; a failed search does not establish publication priority.

## Limitations

The optimizable parameter represents optical attenuation while phytoplankton biomass and physiological light response remain fixed. In nature, turbidity may influence nutrient transfer, composition, sedimentation and self-shading, and the optimal irradiance can adapt. The model neglects temporal forcing, nonuniform phytoplankton density, spectral and UV effects, respiration, and light modification by the biomass itself. Increasing attenuation may not improve net community productivity. This result proves neither optimal field management nor a new mechanism of photosynthesis. The precise exact parameter dependence is conditional on Steele's curve and Beer attenuation; replacement by another empirical response need not preserve the same asymptotics.

## References

1. J. H. Steele, “Environmental Control of Photosynthesis in the Sea,” *Limnology and Oceanography* **7** (1962), 137–150. DOI: `10.4319/lo.1962.7.2.0137`. First published April 1962.
2. J. H. Ryther, “Photosynthesis in the Ocean as a Function of Light Intensity,” *Limnology and Oceanography* **1** (1956), 61–70. DOI: `10.4319/lo.1956.1.1.0061`.
3. T. T. Bannister, “Production Equations in Terms of Chlorophyll Concentration, Quantum Yield, and Upper Limit to Production,” *Limnology and Oceanography* **19** (1974), 1–12. DOI: `10.4319/lo.1974.19.1.0001`.
4. S. B. Idso and J. M. Foster, “An Analytical Study of Three Characteristic Forms of Light-Forced Primary Production in Aquatic Ecosystems,” *Oecologia* **18** (1975), 145–154. DOI: `10.1007/BF00348095` (abstract examined; complete text unavailable).
5. A. E. Walsby, “Numerical Integration of Phytoplankton Photosynthesis Through Time and Depth in a Water Column,” *New Phytologist* **136** (1997), 189–209. DOI: `10.1046/j.1469-8137.1997.00736.x`.
6. G. I. Murphy, “Effect of Mixing Depth and Turbidity on the Productivity of Fresh-Water Impoundments,” *Transactions of the American Fisheries Society* **91** (1962), 69–76. DOI: `10.1577/1548-8659(1962)91[69:EOMDAT]2.0.CO;2` (abstract examined; complete text unavailable).
