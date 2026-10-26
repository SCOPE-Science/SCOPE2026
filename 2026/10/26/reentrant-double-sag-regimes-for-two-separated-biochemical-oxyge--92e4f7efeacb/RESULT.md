# Reentrant double-sag regimes for two separated biochemical oxygen-demand sources

## Finding

**Theorem (sharp two-outfall phase diagram).** Fix deoxygenation and reaeration rates \(0<a<b\), a positive scale \(A\), a secondary-to-primary oxygen-demand load ratio \(k>0\), and a positive downstream travel-time separation \(s\). Consider the oxygen saturation deficit
\[
D(t)=A\left[g(t)+k\,\mathbf 1_{\{t\ge s\}}g(t-s)\right],\qquad
 g(t)=e^{-at}-e^{-bt},\quad t\ge0.
\]
Let
\[
t_0=\frac{\log(b/a)}{b-a},\qquad
\kappa(s)=\frac{a e^{-as}-b e^{-bs}}{b-a}\quad(s>t_0),
\qquad \kappa_*=\left(\frac ab\right)^{(a+b)/(b-a)}.
\]
There are exactly **two distinct strict local maxima** of the continuous deficit profile on \((0,\infty)\) if and only if \(s>t_0\) and \(k>\kappa(s)\). In every other case there is exactly one strict local maximum. At the equality \(k=\kappa(s)\) there is no second maximum.

The critical load function \(\kappa\) rises strictly from zero on \((t_0,2t_0)\), reaches its **unique** maximum \(\kappa_*\) at \(2t_0\), and decreases strictly to zero as \(s\to\infty\). Hence, for each \(0<k<\kappa_*\), unique separations \(t_0<s_-(k)<2t_0<s_+(k)\) satisfy \(\kappa(s_\pm(k))=k\); precisely the intervals
\[
(t_0,s_-(k))\ \text{and}\ (s_+(k),\infty)
\]
have two local maxima, while the intermediate closed interval has one. This is a **two-sag to one-sag to two-sag reentrance** as the outfall separation increases (with a single sag also for \(s\le t_0\)). At \(k=\kappa_*\), every \(s>t_0\) except \(s=2t_0\) gives two maxima; for \(k>\kappa_*\), every \(s>t_0\) gives two maxima.

The sharp universal contrast bound is \(0<\kappa_*<e^{-2}\) for all \(b>a>0\), with \(\kappa_*\to e^{-2}\) as \(b/a\downarrow1\) and \(\kappa_*\to0\) as \(b/a\to\infty\). At the weak-secondary-load and fold boundaries,
\[
s_-(k)=t_0+\frac{k}{a e^{-at_0}}+O(k^2),\qquad
s_+(k)=\frac1a\log\frac{a}{(b-a)k}+o(1)\quad(k\downarrow0),
\]
and
\[
s_\pm(\kappa_*(1-\varepsilon))
=2t_0\pm\sqrt{\frac{2\varepsilon}{ab}}+O(\varepsilon)
\quad(\varepsilon\downarrow0).
\]
The \(O\)-terms concern fixed \(a,b\) and are dimensionally interpreted relative to the chosen travel-time unit.

## Assumptions and scope

Travel time \(t\) is proportional to downstream distance in a uniform-velocity, plug-flow river. The ideal model has a saturated upstream boundary, spatially constant positive rates \(a\) and \(b\), and two instantaneous fully mixed **biochemical oxygen-demand increments**, one at \(t=0\) and the second at \(t=s\). Oxygen demand evolves by \(L'=-aL\) between the outfalls and induces deficit by \(D'=aL-bD\). At \(t=s\), the BOD concentration jumps upward by exactly the stipulated amount, but the dissolved-oxygen deficit is continuous (there is **no direct instantaneous oxygen shock or flow dilution**). The first BOD increment is \(L_1>0\), the second is \(L_2=kL_1>0\), and \(A=aL_1/(b-a)\). In particular, \(D(t)\) represents the linear no-settling Streeter–Phelps response. A sufficiently small common scale \(L_1\) keeps the deficit below any prescribed physically admissible saturation level without altering the count of its extrema.

The assertion concerns the number of **strict local** oxygen-deficit maxima (equivalently dissolved-oxygen minima), not which is the global worst deficit. Extrema at a discontinuity of the derivative are interpreted by the usual local-value definition; \(D\) itself is continuous at \(s\).

## Proof

**1. Reduction and single-source maximum.** Solving the linear equation for deficit after the first BOD increment gives \(D_1(t)=A(e^{-at}-e^{-bt})\). Superposing the solution from the second increment gives the stated \(D\). Since
\[
g'(t)=-ae^{-at}+be^{-bt},
\]
its sign is strictly positive on \((0,t_0)\), zero only at \(t_0\), and negative on \((t_0,\infty)\). Thus the profile restricted to \((0,s)\) has a strict maximum exactly when \(s>t_0\).

**2. Exact downstream extremum test.** On \(t>s\), write
\[
D(t)/A=(1+ke^{as})e^{-at}-(1+ke^{bs})e^{-bt}.
\]
Its derivative has **at most one** zero, and when that zero is in the downstream reach it is necessarily a strict local maximum, since the ratio of the positive to negative exponential derivative terms strictly decreases with \(t\). The unique formal zero is
\[
t_p=\frac1{b-a}\log\frac{b(1+ke^{bs})}{a(1+ke^{as})}.
\]
The derivative immediately after the second outfall equals
\[
D'(s+)/A=(b-a)k+g'(s).
\]
For \(s\le t_0\), this is positive and there is exactly one maximum, downstream. For \(s>t_0\), it is positive exactly when \(k>\kappa(s)\). In that case \(t_p>s\), and \(t_0\) and \(t_p\) are the two strict maxima, separated by a strict **corner minimum at \(s\)**. When \(k\le\kappa(s)\), the downstream profile decreases strictly for \(t>s\) (at equality its right derivative is zero at \(s\), then strictly negative), so only the upstream maximum at \(t_0\) remains. These exhaust every boundary case.

**3. Sharp load–separation phase diagram.** Direct differentiation gives
\[
\kappa'(s)=\frac{b^2e^{-bs}-a^2e^{-as}}{b-a},\qquad
\kappa''(s)=\frac{a^3e^{-as}-b^3e^{-bs}}{b-a}.
\]
The first derivative changes from positive to negative exactly at \(s=2t_0\). Since \(\kappa(t_0)=0\), \(\lim_{s\to\infty}\kappa(s)=0\), and \(\kappa(2t_0)=(a/b)^{(a+b)/(b-a)}\), the stated phase diagram follows by strict monotonicity and the intermediate value theorem. The asymptotic statements at \(k\downarrow0\) follow by Taylor expansion at \(t_0\), where \(\kappa'(t_0)=ae^{-at_0}\), and from \(\kappa(s)\sim (a/(b-a))e^{-as}\) as \(s\to\infty\). At the unique fold,
\[
\kappa''(2t_0)=-ab\kappa_*<0,
\]
so quadratic Taylor expansion and inversion give the displayed square-root root-splitting law.

**4. Universal contrast bound.** With \(r=b/a>1\), write
\[
-\log\kappa_* =\frac{r+1}{r-1}\log r.
\]
The derivative of the right-hand side has numerator \(r-r^{-1}-2\log r\), divided by \((r-1)^2\). This numerator vanishes at \(r=1\) and has derivative \((r-1)^2/r^2>0\). Thus \(\kappa_*\) strictly decreases from \(e^{-2}\) toward zero as \(r\) increases.

**5. Exact reentrant example.** Set \(a=1\), \(b=2\), \(k=1/16\). Then \(t_0=\log2\), \(\kappa_*=1/8\), and with \(y=e^{-s}\), \(\kappa(s)=y-2y^2\). At the three increasing separations
\[
s_1=\log(9/4),\qquad s_2=\log4,\qquad s_3=\log16,
\]
all of which exceed \(t_0\), the right-hand derivative signs, after removing the positive factor \(A\), are respectively
\[
\frac{17}{1296}>0,\qquad -\frac1{16}<0,\qquad\frac1{128}>0.
\]
Thus the number of strict local maxima is exactly \(2,1,2\), with no use of numerical approximation.

## Verification

Run `python3 verify.py` using only the Python standard library. It independently checks three exact-rational separation witnesses, superposition continuity, the closed-form downstream stationarity point, the sign classification, the claimed peak of the critical-load function, and 15,000 reproducible randomized parameter instances including the downstream derivative sign on multiple positive travel times. The checked script's output is:

```
Phase witnesses: 3 exact rational cases
Randomized derivative/comparison checks: 15000
```

This computational verification is finite and does **not** certify the universal assertions; the full proof is analytical and given above. The asymptotics and boundary cases follow from Taylor expansion and strict monotonicity, not empirical fitting.

## Relationship to prior work

Streeter and Phelps (1925) derive the underlying single-source oxygen-deficit equation and discuss known intermediate increments of pollution along a river. Bhargava (1986, 2007) develops multi-outfall and compound sag models, with additional settling and fast BOD removal not included in the idealized model here. The contribution claimed here is limited to the **sharp local-extremum count, the reentrant weak-load separation intervals, the exact universal critical ratio and the root-splitting laws for the no-settling two-source specialization**, not the classical transport or superposition formula itself.

The publicly available primary material for Streeter–Phelps (1925), including the single-source critical point and intervening pollutant inflows, was inspected. The relevant Bhargava 2007 abstract and publisher metadata and the 1986 abstract were inspected, but their full texts were unavailable; hence priority over possible broader analytical statements in those papers is unresolved. Derivation from the prior ODE alone is not presented as historical novelty. Exact equality of claims in an uninspected multi-outfall treatment remains a residual risk.

## Limitations

This result does not model nonzero initial oxygen deficit, instantaneous oxygen shocks, effluent dilution, flow-rate changes, nonconstant reaction coefficients, settling, sediment oxygen demand, photosynthesis, thermal changes, or hydrodynamic dispersion. Two separated local oxygen minima need not correspond to two distinct violations of a water-quality standard. Real-world monitoring design requires water-quality calibration, not just this phase classification. Historical originality remains subject to stronger multi-outfall references not accessible in full text.

## References

- H. W. Streeter and E. B. Phelps (1925), *A Study of the Pollution and Natural Purification of the Ohio River, III*, U.S. Public Health Bulletin 146, February 1925, pp. 18–21 (printed pagination). Public-domain full scan: https://udspace.udel.edu/server/api/core/bitstreams/6f57c427-5f4f-4435-9d8c-87e3c8c02a66/content .
- D. S. Bhargava (1986), *Modelling for compounded DO sags*, Civil Engineering Transactions (Institution of Engineers, Australia) 28(3), 222–230. Bibliographic record cited in https://link.springer.com/article/10.1007/s10669-007-9120-x ; full text not inspected.
- D. S. Bhargava (1986), *DO Sag Model for Extremely Fast River Purification*, Journal of Environmental Engineering 112(3), 572–585, DOI:10.1061/(ASCE)0733-9372(1986)112:3(572). Abstract inspected.
- D. S. Bhargava (first public 6 September 2007), *Dissolved oxygen sag analysis for a settling fields overlapping type multi-wastewater-outfall*, The Environmentalist 28, 128–136 (2008), DOI:10.1007/s10669-007-9120-x. Publisher abstract and release date inspected; full text not inspected.
