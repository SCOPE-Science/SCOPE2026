# Sharp two-crest threshold for delayed four-reservoir runoff pulses

## Finding

For two identical, instantaneous, equal-volume runoff inputs into identical four-stage Nash linear-reservoir routing cascades, the downstream sum changes from one strict local discharge maximum to exactly two at a unique dimensionless arrival separation. With reservoir outflow rate \(k>0\) and pulse separation \(\Delta\geq0\), set \(\tau=k\Delta\). Define
\[
F(\tau)=6\cosh\tau-2\tau\sinh\tau+6-3\tau^2+\frac{\tau^4}{4}.
\]
There is exactly one positive zero \(\tau_*\) of \(F\), satisfying
\[
2<\tau_*=2.95880814824387897254\ldots<3.
\]
The discharge has exactly one strict local maximum for \(0\leq\tau\leq\tau_*\), and exactly two for \(\tau>\tau_*\). At the transition there is an additional stationary shoulder but not an additional local maximum. Thus \(\Delta_*=\tau_*/k\) is a sharp, scale-invariant boundary for the appearance of a second crest. The result is about local crests, not a claim that the later crest is necessarily the global maximum.

## Assumptions and scope

A Nash cascade consists of four consecutive identical linear reservoirs with outflow rate \(k>0\), initially empty, governed by linear flow equations. The resulting normalized instantaneous unit hydrograph is
\[
h_k(t)=\begin{cases}\displaystyle\frac{k}{6}(kt)^3e^{-kt},&t\geq0,\\0,&t<0.\end{cases}
\]
Two sources deliver identical positive input volumes, routed through identical cascades. Their arrivals to the cascades are instantaneous at times \(0\) and \(\Delta\geq0\). The downstream discharge is a positive scalar multiple of \(H(t)=h_k(t)+h_k(t-\Delta)\). With \(x=kt\) and \(\tau=k\Delta\), multiplying by the positive constant \(6/k\) gives the dimensionless function
\[
G_\tau(x)=x^3e^{-x}+\mathbf1_{\{x\geq\tau\}}(x-\tau)^3e^{-(x-\tau)},\qquad x\geq0.
\]
Maxima are strict two-sided local maxima at positive times, with the natural one-sided interpretation if the input starts at zero. At \(x=0\) discharge is zero, so it is not a maximum. The assertion covers every real \(\tau\geq0\); no discretization or finite range restriction is made.

## Proof

**1. Derivative and cubic discriminant.** For \(x>\tau\), direct differentiation yields
\[
G_\tau'(x)=e^{-x}P_\tau(x),\quad
P_\tau(x)=x^2(3-x)+e^\tau(x-\tau)^2(3-x+\tau).
\]
Write \(E=e^\tau\). The cubic coefficients in descending degree are
\[
-(1+E),\quad 3+E(3+3\tau),\quad -E(6\tau+3\tau^2),\quad E(3\tau^2+\tau^3).
\]
Substitution in the cubic discriminant identity \(b^2c^2-4ac^3-4b^3d-27a^2d^2+18abcd\) gives the **exact** identity
\[
\operatorname{Disc}_x(P_\tau)=-108\tau^2e^{2\tau}F(\tau).
\]
The formula is algebraic and holds for every \(\tau>0\), with no numerical approximation.

**2. Uniqueness of the boundary.** Expanding the entire hyperbolic functions at zero gives
\[
F'(\tau)=-4\tau+\frac23\tau^3-\frac1{20}\tau^5+
\sum_{j\geq4}\frac{6-4j}{(2j-1)!}\tau^{2j-1}.
\]
All terms in the sum are negative for \(\tau>0\). Moreover,
\[
4-\frac23 u+\frac1{20}u^2>0\qquad\text{for all real }u,
\]
because the quadratic's discriminant is \(-16/45\). Hence \(F'(\tau)<0\) for every \(\tau>0\). Explicitly,
\[
F(2)=e^2+5e^{-2}-2>0,\qquad F(3)=6e^{-3}-\frac34<0.
\]
Thus the positive zero \(\tau_*\) is unique and lies in \((2,3)\). The stated digits are obtained by sign-preserving high-precision bisection, as reproduced in the checker.

**3. Classification before the isolated peak time.** For \(0<\tau<3\), the derivative before the second arrival is \(x^2e^{-x}(3-x)>0\) for \(0<x<\tau\). Every real root of \(P_\tau\) is in \((3,3+\tau)\): both terms of its defining expression are positive for \(x\leq3\) (including negative \(x\), except harmless zero factors), and both are negative for \(x\geq3+\tau\). These roots therefore all belong to the physical domain after the second arrival. For \(0<\tau<\tau_*\) the cubic discriminant is negative, so \(P_\tau\) has exactly one simple real root, with a sign change from positive to negative, hence exactly one maximum. For \(\tau_*<\tau<3\) the discriminant is positive: there are three distinct real roots, all in the stated interval. The alternating derivative signs give two strict maxima separated by one strict minimum.

At \(\tau=\tau_*\) the discriminant is zero. The cubic cannot have a triple root, because the discriminant of its quadratic derivative is
\[
36\left[(1+e^\tau)^2-e^\tau\tau^2\right]>0.
\]
Indeed \(2\cosh(\tau/2)>\tau\) for all positive \(\tau\). Consequently one root is double and another is simple. The double zero of the derivative gives a stationary shoulder without a sign change; the simple root gives the sole strict maximum. For \(\tau=0\), \(G_0(x)=2x^3e^{-x}\), with unique maximum at \(x=3\).

**4. Classification at and beyond the isolated peak time.** For \(\tau\geq3\), the first component has a strict local maximum at \(x=3\). For \(\tau>3\), the derivative immediately after the second input is negative, since \(P_\tau(\tau)=\tau^2(3-\tau)<0\); at \(\tau=3\), the same right-hand sign follows from \(P_3(3)=0\) and \(P_3'(3)=-9\). But
\[
P_\tau(\tau+2)=4e^\tau-(\tau+2)^2(\tau-1)>0,
\qquad P_\tau(\tau+3)=-\tau(\tau+3)^2<0.
\]
The first inequality follows because \(e^{-\tau}(\tau+2)^2(\tau-1)\) is strictly decreasing for \(\tau\geq3\) and has value \(50e^{-3}<4\) at \(3\). There must therefore be two distinct roots on \((\tau,\tau+3)\), one a local minimum and the other a strict local maximum. There can be no third such root: for \(\tau>3\), \(P_\tau(0)>0>P_\tau(\tau)\) already forces a third polynomial root before the second input, and for \(\tau=3\) the cubic has the root \(3\) at the boundary. The cubic degree excludes any further roots. This yields exactly two strict discharge maxima for every \(\tau\geq3\), completing the proof.

## Verification

The accompanying `verify.py` requires only the Python standard library. Executing `python verify.py` checks the cubic discriminant at rational test points using exact rational arithmetic, computes the unique positive zero of \(F\) by 80-digit Decimal arithmetic, compares the physical derivative with the cubic independently at thousands of points, and checks the one-crest/two-crest root counts across and near the boundary. The run produced `VERIFY_OK assertions= 3491`. These are reproducibility checks, **not** a substitute for the all-parameter analytic proof above. The finite assertion count does not certify originality or field applicability.

## Relationship to prior work

Nash (1957) introduced the linear-reservoir cascade and the gamma-form unit hydrograph, which is the model's foundation. Pattison, Lane, Hardy and Reaney (2014) demonstrated the importance of relative tributary timing for flood behavior in an empirical/numerical watershed study. Santos, Thirel and Perrin (2018) developed a continuous state-space hydrological model using Nash cascades and derived the single-input response, time-to-peak and peak formulas. None of the inspected material states the exact two-impulse four-reservoir crest-count phase transition or the strictly monotone hyperbolic discriminant equation above. Earlier mixture-mode results or results for nonlinear routing may still establish related coverage; no exhaustive priority claim is made. The present claim is specifically a complete local-crest count for **two equal impulses through identical four-store cascades**, not a new hydrograph or a general flood prediction rule.

## Limitations

Instantaneous equal inputs, identical four-reservoir linear kernels and no additional attenuation or channel nonlinearities are essential to the stated theorem. Unequal volumes, unequal shapes, continuous-duration storms, base flow, travel-time uncertainty and nonlinear flood levels are not classified. The threshold identifies the birth of a second local crest, not an absolute flood-stage threshold, the global-peak optimizer, or a validated intervention in any named watershed. A highly relevant accepted manuscript of the Pattison study could not be retrieved from its OA portal; its visible abstract, selected indexed primary-text excerpts and conclusion were considered but do not justify a full-document negative-coverage assertion. Historical priority may depend on other inaccessible shifted-gamma mixture literature.

## References

1. J. E. Nash, *The Form of the Instantaneous Unit Hydrograph*, IAHS General Assembly, Toronto (1957), pp. 114–121. Open historical full text: https://iahs.info/uploads/dms/045011.pdf.
2. I. Pattison, S. N. Lane, R. J. Hardy and S. M. Reaney, *The role of tributary relative timing and sequencing in controlling large floods*, Water Resources Research **50** (2014), 5444–5458. First published online June 6, 2014. https://doi.org/10.1002/2013WR014067.
3. L. Santos, G. Thirel and C. Perrin, *Continuous state-space representation of a bucket-type rainfall-runoff model: a case study with the GR4 model using state-space GR4 (version 1.0)*, Geoscientific Model Development **11** (2018), 1591–1605. https://doi.org/10.5194/gmd-11-1591-2018.
