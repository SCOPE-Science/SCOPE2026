# A sharp storm-duration cutoff for double-crested runoff in parallel two-stage reservoirs

## Finding

A single, constant-intensity rain-excess pulse routed through two parallel **two-stage Nash cascades** can have two strict discharge crests, despite the fact that each pathway has just one impulse-response maximum. There is an exact common storm-duration limit above which this phenomenon is impossible for *every* routing mixture.

**Theorem (sharp duration--modality law).** Let \(r>1\), \(\beta>0\), \(d>0\), and \(0<p<1\). The faster and slower pathway transit-time kernels are respectively
\[
 f_{r\beta}(t)=(r\beta)^2t e^{-r\beta t},\qquad
 f_{\beta}(t)=\beta^2t e^{-\beta t}\qquad(t\ge0),
\]
with each kernel set to zero for negative time. The normalized discharge from one rectangular effective-rainfall pulse is
\[
 H_d(t)=\frac1d\int_{\max(0,t-d)}^t
 \left[p f_{r\beta}(u)+(1-p)f_\beta(u)\right]du,\qquad t\ge0.
\]
Put \(D=\beta d\) and
\[
 K_r(D)=\frac D{e^{rD}-1},\quad K_1(D)=\frac D{e^D-1},
 \quad L_r(D)=K_1(D)-K_r(D).
\]
The following classification is exact:

1. If \(1<r\le3+2\sqrt2\), then \(H_d\) has exactly one strict local and global maximum for every positive \(D\) and every mixture \(p\).
2. If \(r>3+2\sqrt2\), there is a **unique** \(D_c(r)>0\) satisfying
   \[
       (r-1)L_r(D_c)=4.
   \]
   For \(D\ge D_c(r)\), every mixture is strictly single-peaked. For each \(0<D<D_c(r)\), the following explicitly determined, nonempty open interval of \(p\) produces **exactly two strict local maxima** separated by exactly one strict local minimum; all other positive mixing fractions produce exactly one strict maximum.

For the explicit interval in (2), define
\[
 s_\pm=\frac{K_1(D)+K_r(D)\pm
 \sqrt{L_r(D)^2-4L_r(D)/(r-1)}}2
\]
and, for \(K_r(D)<s<K_1(D)\),
\[
 R_D(s)=\frac{1-e^{-D}}{r^2(1-e^{-rD})}
 e^{(r-1)s}\frac{K_1(D)-s}{s-K_r(D)}.
\]
Exactly two strict discharge crests occur if and only if
\[
 \frac{R_D(s_-)}{1+R_D(s_-)}<p<
 \frac{R_D(s_+)}{1+R_D(s_+)}.
\]
At either mixing-interval endpoint, a stationary shoulder appears but only one strict maximum remains. The constant \(3+2\sqrt2\) is the sharp **rate-separation threshold for any positive storm duration**; the new finite-duration cutoff \(D_c(r)\) and the complete mixing interval are the finite-storm conclusions.

**Exact witness.** Take \(r=8\), \(p=1/12\). A single pulse of duration \(d=(\log2)/\beta\) produces exactly two strict maxima, whereas the same routing network under one pulse lasting \(d=2(\log2)/\beta\) has exactly one strict maximum. The longer pulse lies above \(D_c(8)\approx1.030551266305\), so *every* routing mixture is single-peaked at the longer duration.

## Assumptions and scope

The two routes are independent, linear, mass-conserving, two-reservoir cascades with nonzero transit rates \(r\beta\) and \(\beta\). Both paths receive the **same** one rectangular rain-excess pulse and their outputs are summed with positive fractions \(p\) and \(1-p\). Time is continuous. There is no antecedent baseflow, nonlinear channel storage, spatially varying rainfall, infiltration feedback, or routing interaction. A crest means a strict local maximum of the continuous discharge \(H_d\); the count concerns \(t>0\) and includes neither artificial dry-time extensions nor zero-flow endpoints. The factor \(1/d\) normalizes total rain-excess volume and does not affect modality.

The dimensionless parameter \(D=\beta d\) measures rainfall duration relative to the slower pathway storage time. Exchanging route labels permits \(r>1\) without loss; equal rates give a single Nash cascade and are outside the separated-rate theorem.

## Proof

**Step 1: The only potential extrema occur after the pulse ends.** Rescale time by \(\beta\), hence set \(\beta=1\). Write \(f(t)=p r^2t e^{-rt}+(1-p)t e^{-t}\) for \(t\ge0\), and \(f(t)=0\) otherwise. Then
\[
  D H_D'(x)=f(x)-f(x-D).
\]
For \(0<x\le D\), the latter difference is \(f(x)>0\). For \(x>D\), let \(s=x-D>0\), and factor each component:
\[
 D H_D'(D+s)=p r^2 e^{-rs}(1-e^{-rD})(K_r(D)-s)
 +(1-p)e^{-s}(1-e^{-D})(K_1(D)-s).
 \tag{1}
\]
Since \(K_r(D)<K_1(D)\), expression (1) is strictly positive for \(0<s\le K_r(D)\) and strictly negative for \(s\ge K_1(D)\). Every stationary point therefore lies in the open interval \((K_r(D),K_1(D))\).

**Step 2: A scalar crossing problem determines every peak.** For \(K_r(D)<s<K_1(D)\), rearranging the two terms in (1) shows
\[
 \operatorname{sgn}H_D'(D+s)
 =\operatorname{sgn}\left(R_D(s)-\frac p{1-p}\right).
 \tag{2}
\]
The positive function \(R_D\) tends to \(+\infty\) as \(s\downarrow K_r(D)\) and to \(0\) as \(s\uparrow K_1(D)\). Direct differentiation gives
\[
 \frac{d}{ds}\log R_D(s)
 =(r-1)-\frac1{K_1(D)-s}-\frac1{s-K_r(D)}.
 \tag{3}
\]
For \(u=s-K_r(D)>0\), \(v=K_1(D)-s>0\), \(u+v=L_r(D)\) and \(1/u+1/v\ge4/L_r(D)\), with equality only at the midpoint. Consequently, if \((r-1)L_r(D)\le4\), expression (3) is nonpositive and vanishes at most at one isolated point; \(R_D\) is **strictly decreasing**, crosses \(p/(1-p)\) exactly once, and (2) yields one strict discharge maximum.

If \((r-1)L_r(D)>4\), (3) has exactly two distinct zeros, at \(s_-\) and \(s_+\). Its signs are negative, positive, negative on the three complementary intervals. Thus \(R_D\) has a strict local minimum at \(s_-\) and a strict local maximum at \(s_+\), with \(0<R_D(s_-)<R_D(s_+)\). Horizontal levels strictly between them cut the graph three times; all other positive levels cut it once, except the endpoint levels which give one crossing and one tangency. Through (2), three simple crossings are exactly maximum--minimum--maximum of the discharge. This proves the stated sharp mixing-window formula and behavior on its boundary.

**Step 3: The storm cutoff exists uniquely.** Let \(g(z)=z/(e^z-1)\) for \(z>0\). Since
\[
  L_r(D)=g(D)-r^{-1}g(rD),\qquad
  L_r'(D)=g'(D)-g'(rD),
\]
strict convexity of \(g\) implies \(L_r'(D)<0\). For completeness,
\[
 g''(z)=\frac{e^z\big[(z-2)e^z+z+2\big]}{(e^z-1)^3}>0.
\]
Indeed, \(h(z)=(z-2)e^z+z+2\) satisfies \(h(0)=h'(0)=0\) and \(h''(z)=ze^z>0\) for \(z>0\). The endpoint limits are
\[
 \lim_{D\downarrow0}L_r(D)=1-r^{-1},\qquad
 \lim_{D\to\infty}L_r(D)=0.
\]
Thus \((r-1)L_r(D)\) decreases strictly from \((r-1)^2/r\) to zero. It crosses 4 at a positive \(D\) if and only if \((r-1)^2>4r\), equivalent (for \(r>1\)) to \(r>3+2\sqrt2\). There is exactly one such \(D_c(r)\), and Steps 1--2 finish the classification.

**Step 4: Exact two-crest/one-crest witness.** For \(r=8\) and \(D=\log2\),
\[
 K_1=\log2,\quad K_8=\frac{\log2}{255},\quad
 7L_8=\frac{1778}{255}\log2>4.
\]
(The elementary inequality \(\log2>2/3\), obtained from strict midpoint integration of the convex function \(1/t\) on \([1,2]\), suffices.) At \(s_m=m(\log2)/7\), for \(m\in\{1,2,4,6\}\), formula (2) has the exact odds ratio
\[
 R_D(s_m)=\frac{2^{m+1}(7-m)}{255m-7}.
\]
With \(p=1/12\), the comparison threshold is \(1/11\). At \(m=1,2,4,6\), the signs of \(R_D(s_m)-1/11\) are respectively \(+,-,+,-\), by rational arithmetic. The intermediate value theorem gives at least three crossings, and Step 2 gives at most three, hence exactly two strict maxima. At \(D=2\log2\),
\[
 7L_8(D)<7K_1(D)=\frac{14\log2}{3}<\frac72<4,
\]
using \(\log2<3/4\). Step 2 then guarantees a single strict maximum for **all** mixing fractions, including \(1/12\). \(\square\)

## Verification

Run `python3 checker.py` from the directory containing this manuscript. The standard-library checker independently evaluates the convolution, its derivative, the analytical turning-point criterion and their agreement over parameter stress tests. It also checks the four **exact rational** signs in Step 4 using `fractions.Fraction`. In the packaged replay it reported **1797 passed assertions** and \(D_c(8)\approx1.030551266305\).

Numerical grid tests are non-exhaustive and do not establish the universal theorem; the analytical inequalities in Steps 1--4 do. The explicit rational sign changes rigorously certify the double-crest witness, independently of floating-point peak-finding. The approximate value of \(D_c(8)\) is for orientation, not a substitute for its exact defining equation.

## Relationship to prior work

The 1978 parallel-cascades urban watershed model motivates the two-route architecture; the available publisher abstract confirms that it handles parallel linear-reservoir cascades, but its full text could not be accessed. Bárdossy, Mascellani and Franchini (2006) explain Nash gamma-type unit hydrographs and their convolution with effective rain. Their model provides the hydrologic primitives, not the present finite-storm two-crest phase diagram in the inspected material. Došlá (2009), Theorem 2, already gives a **general modality criterion for mixtures of two unimodal densities**, and Proposition 6 already analyzes **instantaneous** gamma mixtures with the same shape parameter. Thus neither the general mixture criterion nor the limiting rate-ratio boundary \(3+2\sqrt2\) is claimed as new. The present work evaluates the finite-rectangular-convolution components within that broad framework and proves the additional strict **uniqueness and exact location of the storm-duration cutoff**, which the general condition does not explicitly resolve. Ahmed, Goria and Hussein (2008) likewise study mode changes in gamma mixtures. The present claim concerns the *finite positive duration* of **one rectangular storm**, the unique disappearance threshold \(D_c(r)\), and the exact mixing-window classification after rectangular convolution. Those are not covered by merely stating an instantaneous gamma-mixture criterion.

## Limitations

This is a deterministic linear-routing theorem, not a calibration or forecast for a specific watershed. Strong nonlinearity, heterogeneous rainfall, storm clustering, different cascade orders, or delayed paths can change crest counts. An instantaneous two-gamma mixture threshold is established prior work, and the finite-storm result does not imply novelty of that older boundary. The 1978 original parallel-cascades text was not available in full, and complete historical-priority review of all hydrologic and probability literature remains outstanding. No independent validation or experimental replication has been performed.

## References

1. A. Diskin, A. Oben-Nyarko, and S. Ince (1978), *Parallel Cascades Model for Urban Watersheds*, *Journal of the Hydraulics Division*. DOI: https://doi.org/10.1061/JYCEAJ.0004936. Publisher abstract inspected; full paper inaccessible.
2. A. Bárdossy, G. Mascellani, and M. Franchini (2006), *Fuzzy unit hydrograph*, *Water Resources Research*, DOI: https://doi.org/10.1029/2004WR003751. Relevant hydrologic modeling sections inspected.
3. Š. Došlá (2009), *Conditions for bimodality and multimodality of a mixture of two unimodal densities*, *Kybernetika*, accessible full text: https://dml.cz/dmlcz/140075. Proposition 6 and its surrounding argument inspected.
4. A. Ahmed, M. Goria, and A. Hussein (2008), *Gamma Mixture: Bimodality, Inflexions and L-Moments*, DOI: https://doi.org/10.1080/03610920701713286. Relevant original gamma-mixture modality sections inspected.
5. V. Singh, G. Mishra, and S. Jain (2014), *A review of the synthetic unit hydrograph*, DOI: https://doi.org/10.1080/02626667.2013.870664. Indexed parallel-cascade section inspected; complete text inaccessible.
