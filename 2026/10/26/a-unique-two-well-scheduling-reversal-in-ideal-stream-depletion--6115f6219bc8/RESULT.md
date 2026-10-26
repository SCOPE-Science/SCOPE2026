# A unique two-well scheduling reversal in ideal stream depletion

## Finding

Let two wells at different positive distances from a straight fully penetrating stream pump consecutively, each at the same constant discharge for the same duration. Under the linear Glover–Balmer model, the order minimizing **instantaneous stream-depletion rate at the instant the second pumping interval ends** changes exactly once as the shared pumping duration increases. The unique changeover is characterized by a dimensionless scalar equation; its normalized location increases strictly with the far-to-near well distance ratio and has two sharp, universal limiting constants.

More precisely, let \(0<d_1<d_2\), aquifer storativity \(S>0\), transmissivity \(\mathcal T>0\), discharge \(Q>0\), and interval duration \(\Delta>0\). Define
\[
\alpha_i=d_i\sqrt{\frac{S}{4\mathcal T}},\qquad r=\frac{d_2}{d_1}>1,\qquad z_0=\sqrt{3\log 2},\qquad
G(z)=\operatorname{erfc}(z/\sqrt 2)-2\operatorname{erfc}(z).
\]
There is exactly one \(z_r\) in \((z_0/r,z_0)\) satisfying \(G(z_r)=G(rz_r)\). Put \(\Delta_c=(\alpha_1/z_r)^2\). If \(D_{NF}\) is the depletion rate with the **near** well first and the far well second, and \(D_{FN}\) that with the **far** well first, then
\[
\Delta<\Delta_c\Longrightarrow D_{NF}>D_{FN},\qquad
\Delta=\Delta_c\Longrightarrow D_{NF}=D_{FN},\qquad
\Delta>\Delta_c\Longrightarrow D_{NF}<D_{FN}.
\]
All inequalities are strict away from the unique crossing. Thus far-first minimizes end-of-schedule depletion for short intervals; near-first does so for long intervals. The normalized changeover \(\Delta_c/\alpha_1^2=z_r^{-2}\) grows strictly with \(r\), and
\[
\lim_{r\downarrow1}\frac{\Delta_c}{\alpha_1^2}=\frac1{3\log2},\qquad
\lim_{r\to\infty}\frac{\Delta_c}{\alpha_1^2}=\frac1{z_p^2},
\]
where \(z_p\in(0,z_0)\) is the unique positive zero of \(G\). In particular, for every \(r>1\),
\[
\frac{1}{3\log2}<\frac{\Delta_c}{\alpha_1^2}<\frac{1}{z_p^2},
\]
with limiting values \(0.4808983469629878\ldots\) and \(1.015641829748788\ldots\). These bounds are sharp as the distance ratio approaches its two endpoints.

## Assumptions and scope

The aquifer is homogeneous, isotropic, linearly diffusive, laterally unbounded on the aquifer side of a straight perfectly connected river, and initially undisturbed. The straight fully penetrating stream is held at fixed head. Both wells are fully penetrating point wells with identical positive discharge \(Q\). Storativity \(S\), transmissivity \(\mathcal T\), and distances \(d_i\) are fixed. There is no pumping outside \([0,2\Delta]\). Exactly one well pumps on \([0,\Delta]\), and the other pumps on \([\Delta,2\Delta]\); both pump for exactly \(\Delta\). The objective is the **instantaneous** river-depletion rate at \(t=2\Delta\), not total depleted volume, delayed peak, long-run streamflow, or an unconstrained multiwell policy.

The classical Glover–Balmer constant-pumping depletion-rate fraction at elapsed time \(t>0\) is
\[
K_i(t)=\operatorname{erfc}\left(\frac{\alpha_i}{\sqrt t}\right),\quad K_i(0)=0.
\]
Linear superposition is assumed, so a well pumping at discharge \(Q\) from \(s\) until \(u\) contributes \(Q[K_i(t-s)-K_i(t-u)]\) at \(t\ge u\). This statement uses the ideal Glover kernel directly; extensions to bounded, anisotropic, heterogeneous, or partially penetrating aquifers are not asserted.

## Proof

**1. Exact endpoint response.** At the end of the second interval, superposition gives
\[
D_{NF}=Q\bigl[K_1(2\Delta)-K_1(\Delta)+K_2(\Delta)\bigr],\quad
D_{FN}=Q\bigl[K_2(2\Delta)-K_2(\Delta)+K_1(\Delta)\bigr].
\]
Set \(z=\alpha_1/\sqrt\Delta\), so \(\alpha_2/\sqrt\Delta=rz\). Subtraction gives the **exact identity**
\[
\frac{D_{NF}-D_{FN}}Q=G(z)-G(rz). \tag{1}
\]
This accounts for the residual stream-depletion rate from the well that has already stopped pumping; replacing that residual by zero would give an incorrect ordering problem.

**2. Shape of the comparison kernel.** For every \(z>0\),
\[
G'(z)=\frac{4e^{-z^2}-\sqrt2e^{-z^2/2}}{\sqrt\pi}.
\]
The derivative vanishes if and only if \(e^{z^2/2}=2\sqrt2\), or \(z=z_0=\sqrt{3\log2}\). It is positive before \(z_0\) and negative afterward. Thus \(G\) is strictly increasing on \((0,z_0)\) and strictly decreasing on \((z_0,\infty)\). Moreover, \(G(0)=-1\), \(G(z)\to0\) as \(z\to\infty\), and \(G(z_0)>0\): the latter follows because the function strictly decreases to zero on \((z_0,\infty)\). Hence exactly one \(z_p\in(0,z_0)\) satisfies \(G(z_p)=0\).

**3. One crossing for every pair.** If \(0<z\le z_0/r\), both \(z\) and \(rz\) are on the increasing branch, so \(G(z)<G(rz)\). If \(z\ge z_0\), both are on the decreasing branch, so \(G(z)>G(rz)\). On the intervening open interval \((z_0/r,z_0)\), the first term \(G(z)\) is strictly increasing while \(G(rz)\) is strictly decreasing. Thus \(G(z)-G(rz)\) increases strictly from a negative value to a positive value and has exactly one zero \(z_r\) there. At that zero \(rz_r>z_0\), hence \(G(rz_r)>0\) and \(G(z_r)>0\), giving the sharper bound \(z_p<z_r<z_0\).

Because \(z=\alpha_1/\sqrt\Delta\) decreases continuously from \(+\infty\) to \(0\) as \(\Delta\) increases, identity (1) gives precisely the stated end-depletion order and equality threshold.

**4. Strict changeover monotonicity and sharp limits.** On the root branch, write \(F(z,r)=G(z)-G(rz)=0\). Its partial derivatives are
\[
F_z=G'(z)-rG'(rz)>0,\qquad F_r=-zG'(rz)>0,
\]
since \(z<z_0<rz\). Consequently implicit differentiation yields
\[
\frac{dz_r}{dr}=-\frac{F_r}{F_z}<0.
\]
Thus \(\Delta_c/\alpha_1^2=z_r^{-2}\) increases strictly with \(r\). As \(r\downarrow1\), the bracket \(z_0/r<z_r<z_0\) forces \(z_r\to z_0\). For \(r\to\infty\), the bound \(z_r>z_p>0\) implies \(rz_r\to\infty\), hence \(G(rz_r)\to0\). Since \(G(z_r)=G(rz_r)\) and \(z_r\in(z_p,z_0)\), strict increase of \(G\) there forces \(z_r\to z_p\). The claimed limits and sharp strict bounds follow.

**5. Explicit distance-ratio illustration.** With \(\alpha_1=1\), \(\alpha_2=2\), the unique solution satisfies \(z_2\approx1.078577852072479\), giving \(\Delta_c\approx0.8596011817017304\). At \(\Delta=1/4\), the arguments \(z=2\), \(rz=4\) both lie above \(z_0\); strict decrease of \(G\) proves \(D_{NF}>D_{FN}\). At \(\Delta=4\), the arguments \(z=1/2\) and \(rz=1\) both lie below \(z_0\); strict increase proves \(D_{NF}<D_{FN}\). No floating-point value is needed to establish either sign.

## Verification

Run the supplied standalone Python-standard-library program with `python verify.py`. It evaluates the closed-form response and independently superposes four step-response terms for 5,000 reproducible parameter draws, checks both signs at duration multiples of each analytically defined transition, verifies 999 strict distance-ratio comparisons, and independently brackets the stated dimensionless constants and illustrative crossing. It completed successfully. These finite checks are supplementary; the uniqueness, strict inequalities, and limits are established by the foregoing proof, not by sampling.

## Relationship to prior work

The original Glover–Balmer analysis supplies the step-response kernel for an ideal well beside a straight river. Jenkins develops stream-depletion rates for intermittent pumping by step-response superposition. The reviewed Miller–Durnford–Halstead–Altenhofen–Flory 2007 analysis displays this kernel and develops semianalytical stream-depletion-factor corrections for bounded aquifers, but its inspected model and conclusions do not provide the particular two-well finite-horizon one-crossing order classification. Wallace–Darama–Annable (1990) addresses cyclic pumping from a well and the rate/volume of depletion over cycles. Bredehoeft–Kendy (2007 online) studies seasonal pumping and offsetting recharge with matched depletion factors. These are closely related environmental-control problems, but their accessible descriptions concern different schedules, objectives, or well arrangements. The last two full papers could not be accessed for statement-by-statement exclusion; broader results in those papers or in the general theory of totally positive kernels may imply this special two-well law. The claim is a new self-contained derivation, not a claim of established historical priority.

## Limitations

This is an ideal linear-response schedule classification for two wells, two equal-duration intervals, equal fixed discharge, and a single endpoint instantaneous stream-depletion objective. It does not prove optimality for more wells, unequal discharges or durations, spatially restricted pumping, cumulative depletion, peak-over-time constraints, ecological low-flow thresholds, stream–aquifer disconnection, drawdown interference beyond linearity, finite boundaries, or non-Glover response laws. Independent external mathematical audit has not been performed; the accessible original literature is not exhaustive.

## References

1. Glover, R. E., and Balmer, G. G. (1954). “River depletion resulting from pumping a well near a river.” *Transactions of the American Geophysical Union*, **35**(3), 468–470. DOI: 10.1029/TR035i003p00468. Public date verified to month only (June 1954).
2. Jenkins, C. T. (1968). *Computation of rate and volume of stream depletion by wells.* USGS Techniques of Water-Resources Investigations, book 4, chapter D1. DOI: 10.3133/twri04D1.
3. Wallace, R. B., Darama, Y., and Annable, M. D. (1990). “Stream depletion by cyclic pumping of wells.” *Water Resources Research*, **26**(6), 1263–1270. DOI: 10.1029/WR026i006p01263. Abstract inspected; complete text not available.
4. Miller, C. D., Durnford, D., Halstead, M. R., Altenhofen, J., and Flory, V. (2007). “Stream depletion in alluvial valleys using the SDF semianalytical model.” *Groundwater*, **45**, 506–514. DOI: 10.1111/j.1745-6584.2007.00311.x. First online 2007-03-23; accessible full text and displayed response inspected.
5. Bredehoeft, J., and Kendy, E. (2008 print; 2007 online). “Strategies for offsetting seasonal impacts of pumping on a nearby stream.” *Groundwater*, **46**, 23–29. DOI: 10.1111/j.1745-6584.2007.00367.x. First online 2007-09-18; abstract inspected, complete text not available.
