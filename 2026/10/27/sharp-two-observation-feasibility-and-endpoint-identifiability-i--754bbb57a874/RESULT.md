# Sharp two-observation feasibility and endpoint identifiability in ponded Green–Ampt infiltration

## Finding

Consider cumulative infiltration \(F(t)\), with \(F(0)=0\), governed under uninterrupted ponding by
\[
\frac{dF}{dt}=K\left(1+\frac{B}{F}\right),\qquad K>0,\ B>0,\quad t>0.
\]
Fix any \(0<F_1<F_2\) and \(t_1>0\), and ask whether finite positive \(K,B\) can satisfy \(F(t_i)=F_i\) at times \(0<t_1<t_2\). Write \(\rho=F_2/F_1>1\) and \(q=t_2/t_1>1\). Then **such parameters exist, and are unique, if and only if**
\[
\boxed{\rho<q<\rho^2.}
\]
Both inequalities are sharp and strict. If either fails, the ideal constant-parameter model cannot interpolate the two observations exactly. For admissible data, let \(u\) denote the unique positive solution of
\[
\frac{\rho u-\log(1+\rho u)}{u-\log(1+u)}=q.
\]
The uniquely reconstructed parameters are
\[
\boxed{B=\frac{F_1}{u},\qquad K=\frac{F_1\,[u-\log(1+u)]}{t_1u}.}
\]
In addition, at fixed \(F_1,t_1,\rho\), these inverse parameters have **different sharp boundary-layer laws**. If \(\delta=\rho^2-q\downarrow0\), then
\[
B\sim\frac{2F_1\rho^2(\rho-1)}{3\delta},\qquad
K\sim\frac{3F_1\delta}{4t_1\rho^2(\rho-1)}.
\]
If instead \(\varepsilon=q-\rho\downarrow0\), then
\[
B\sim\frac{F_1\varepsilon}{(\rho-1)\log(1/\varepsilon)},\qquad
\frac{F_1}{t_1}-K\sim\frac{F_1\varepsilon}{t_1(\rho-1)}.
\]
Thus the two ends of the feasible observation region correspond respectively to a large-capillary/small-conductivity degeneration and a vanishing-capillary/finite-conductivity degeneration, with unequal pole and logarithmic parameter-conditioning scales.

## Assumptions and scope

The mathematical model describes one homogeneous soil with constant strictly positive saturated conductivity \(K\) and effective capillary length \(B\), permanent surface ponding from known initial time zero, no infiltration-limiting rainfall, and an initially zero cumulative infiltrated depth. The singular rate at \(F=0\) is interpreted through the unique increasing integral solution. The two observations are positive *cumulative* infiltration depths with exact known times measured from the start of ponding. The claim concerns exact data and positive finite parameters, not statistical stability under measurement error, a falling-head boundary, variable rainfall, layered soil, or moisture redistribution. \(B\) represents the product of suction head and moisture deficit in the standard Green–Ampt parameterization, not a separately identified suction and deficit.

## Proof

**1. Forward integral and parameter reduction.** For \(F>0\), separate variables:
\[
Kt=\int_0^F\frac{s}{s+B}\,ds=F-B\log(1+F/B).
\]
Put \(g(u)=u-\log(1+u)\). It is strictly positive for \(u>0\), and the forward equation is \(Kt=B g(F/B)\). With \(u=F_1/B\), the ratio of the two observation equations becomes \(q=R_\rho(u):=g(\rho u)/g(u)\); conversely any positive solution \(u\) reconstructs the displayed \(K,B\) and exactly satisfies both data.

**2. Strict monotonicity, without numerical root-counting.** Define logarithmic elasticity
\[
h(u)=\frac{ug'(u)}{g(u)}=\frac{u^2}{(1+u)g(u)}.
\]
Let \(H(u)=u^2/(u+2)-g(u)\). Direct differentiation gives
\[
H(0)=0,\qquad H'(u)=\frac{u^2}{(1+u)(u+2)^2}>0\quad (u>0).
\]
Therefore \(H(u)>0\), and
\[
\frac{h'(u)}{h(u)}
=\frac{(u+2)g(u)-u^2}{u(1+u)g(u)}
=-\frac{(u+2)H(u)}{u(1+u)g(u)}<0.
\]
Thus \(h\) decreases strictly, and
\[
u\frac{d}{du}\log R_\rho(u)=h(\rho u)-h(u)<0
\]
for every \(\rho>1\) and \(u>0\). Since \(g(u)\sim u^2/2\) as \(u\downarrow0\) and \(g(u)\sim u\) as \(u\to\infty\), the continuous strictly decreasing map \(R_\rho\) has range exactly \((\rho,\rho^2)\). This proves necessity, sufficiency, uniqueness, and exclusion of finite positive solutions at both boundary equalities.

**3. Upper-boundary pole.** The expansion \(g(u)=u^2/2-u^3/3+O(u^4)\) yields
\[
R_\rho(u)=\rho^2\left[1-\frac23(\rho-1)u+O(u^2)\right].
\]
Hence \(u\sim3\delta/[2\rho^2(\rho-1)]\). Substitute into \(B=F_1/u\) and \(K=F_1 g(u)/(t_1u)\sim F_1u/(2t_1)\) to obtain the first pair of sharp asymptotic laws.

**4. Lower-boundary logarithm.** The exact identity
\[
R_\rho(u)-\rho=\frac{\rho\log(1+u)-\log(1+\rho u)}{g(u)}
\]
gives \(R_\rho(u)-\rho\sim(\rho-1)\log u/u\) as \(u\to\infty\). Asymptotic inversion of this strictly decreasing relation gives
\[
u\sim\frac{\rho-1}{\varepsilon}\log(1/\varepsilon).
\]
Therefore \(B=F_1/u\) has the asserted logarithmic law. Finally \(K=(F_1/t_1)[1-\log(1+u)/u]\), whence \(F_1/t_1-K\sim (F_1/t_1)\varepsilon/(\rho-1)\). Every asymptotic assumes \(F_1,t_1,\rho\) are fixed, with the limiting observation ratio varying as stated.

## Verification

The included standard-library script `verification.py` checks the rational derivative identity in exact fraction arithmetic, verifies the inverse formulas for 4,000 reproducible positive parameter quadruples, checks the exclusion of the four benchmark inadmissible boundaries, reproduces the exact example below, and tests both asymptotic regimes numerically. Run `python3 verification.py` from the directory containing this file. These finite tests are reproducibility diagnostics; the continuum assertions and uniqueness follow from the preceding derivative proof, not the tests.

For an exactly checkable instance take \(K=B=F_1=1\), \(F_2=2\), \(t_1=1-\log2\), \(t_2=2-\log3\). Then \(\rho=2\), \(q\approx2.93752461840417\), which lies strictly between \(2\) and \(4\); inversion recovers \(K=B=1\).

## Relationship to prior work

The Green–Ampt infiltration equation itself is classical, and two-parameter inverse soil-hydraulic calibration is established. Zeleke and Si (2005), whose complete public article was inspected, study numerical uniqueness of conductivity and capillary parameters from **falling-head** experimental data, including the effects of noise and prior information. Their observation scheme and findings do not present this exact constant-head, two-cumulative-point feasibility region with unequal boundary rates. Rucker (2009) presents a coupled resistivity/wetting-front inverse model and direct recovery of front velocity, rather than the present two-parameter ratio inversion. Lai, Ogden, Steinke and Talbot (2015) analyze more general transient infiltration/redistribution simulation and give the forward Green–Ampt equation, without this two-point inverse phase classification. Mohammadzadeh-Habili and Heidarpour (2011) develop an upward-infiltration parameter-estimation method; the accessible abstract concerns a different setup, but full-text priority was not resolved. Earlier inverse-scaling work by Warrick (1993) is a further named historical-priority risk, since its complete text was not inspected. The forward law, usual parameter meanings, and qualitative importance of calibration are not claimed as new.

## Limitations

This is a mathematical classification under an idealized sharp-front, uninterrupted-ponding model. It is not evidence that real two-observation data are noise-free or that the corresponding positive parameters can be recovered accurately near either boundary. Existing inverse methodology may contain a more general statement implying some or all of these conclusions; historical priority is provisional until the identified inaccessible sources are compared in full. Nothing here establishes existence or uniqueness for falling-head experiments, layered soils, changing rainfall, unknown ponding onset, or three independently unknown hydraulic factors.

## References

1. Green, W. H., and Ampt, G. A. (1911), "Studies on soil physics, I: The flow of air and water through soils," *Journal of Agricultural Science*, 4, 1–24. Foundational law.
2. Zeleke, T. B., and Si, B. C. (2005), "Parameter estimation using the falling head infiltration model: Simulation and field experiment," *Water Resources Research*, 41(2), DOI: 10.1029/2004WR003407. First published February 23, 2005.
3. Lazarovitch, N., Ben-Gal, A., Šimůnek, J., and Shani, U. (2007), "Uniqueness of soil hydraulic parameters determined by a combined Wooding inverse approach," *Soil Science Society of America Journal*, 71, 860–865, DOI: 10.2136/sssaj2005.0420.
4. Rucker, D. (2009), "A coupled electrical resistivity–infiltration model for wetting front evaluation," *Vadose Zone Journal*, 8, 383–388, DOI: 10.2136/vzj2008.0080.
5. Mohammadzadeh-Habili, J., and Heidarpour, M. (2011), "Estimating soil hydraulic parameters by using Green and Ampt infiltration equation," *Journal of Hydrologic Engineering*, 16, 772–780, DOI: 10.1061/(ASCE)HE.1943-5584.0000373.
6. Lai, W., Ogden, F. L., Steinke, R. C., and Talbot, C. A. (2015), "An efficient and guaranteed stable numerical method for continuous modeling of infiltration and redistribution with a shallow dynamic water table," *Water Resources Research*, 51, 1514–1528, DOI: 10.1002/2014WR016487.
7. Warrick, A. W. (1993), "Inverse estimations of soil hydraulic properties with scaling: One-dimensional infiltration," *Soil Science Society of America Journal*, 57, 631–636, DOI: 10.2136/sssaj1993.03615995005700030001x. Full-text priority comparison outstanding.
