# Sharp reentrant drawdown reversals from delayed pumping and injection wells

## Finding

In the infinite homogeneous confined-aquifer Theis model, a pumping well operates constantly from time zero; a separate recharge/injection well begins at a positive delay. At a fixed observation point, the drawdown time series can have **two distinct strict post-injection turning points**, an initial maximum followed by a minimum, despite a smaller continuous injection rate than the pumping rate. The following complete criterion identifies the regime and an unexpected reentrant dependence on the injection delay.

Put \(a=d_P^2S/(4\mathcal T)>0\) and \(b=d_I^2S/(4\mathcal T)>0\), where \(d_P,d_I>0\) are the observation-point distances to the extraction and injection wells, \(S>0\) is storativity, and \(\mathcal T>0\) is transmissivity. Let \(\tau>0\) be injection-start delay and \(\lambda=Q_I/Q_P>0\) the ratio of injection to extraction rates. Define for \(t>\tau\)

\[
\Phi_\tau(t)=\frac{t-\tau}{t}\exp\!\left(-\frac a t+\frac b{t-\tau}\right).
\]

When \(C=\tau+a-b>0\), this function has precisely one strict minimum at

\[
t_m=\frac{\tau(\tau+2a+\sqrt{\tau^2+4ab})}{2(\tau+a-b)},\qquad m(\tau)=\Phi_\tau(t_m)\in(0,1).
\]

For \(0<\lambda<1\), **there are exactly two distinct strict post-injection extrema if and only if**

\[
\boxed{\tau+a>b\quad\hbox{and}\quad m(\tau)<\lambda<1.}
\]

If equality \(\lambda=m(\tau)\) holds, the single post-injection stationary time is a horizontal inflection, not a strict extremum. If \(\tau+a\le b\), the drawdown is strictly increasing whenever \(\lambda\le1\). If \(\lambda\ge1\), there is never a pair of strict post-injection extrema (one maximum exists for \(\lambda>1\), and for \(\lambda=1\) precisely when \(\tau+a>b\)).

**Reentrant delay law.** If the injection well is nearer the observation point than the pumping well, so \(a>b\), the minimum level \(m(\tau)\), viewed as a function of delay, strictly increases on \((0,a-b)\), strictly decreases on \((a-b,\infty)\), tends to zero at both endpoints, and reaches the exact global maximum

\[
\boxed{\max_{\tau>0}m(\tau)=\frac ba\quad\text{at}\quad \tau=a-b.}
\]

Consequently, for **every** fixed rate ratio \(0<\lambda<b/a\), there exist exactly two positive delays \(\tau_-<a-b<\tau_+\) solving \(m(\tau_\pm)=\lambda\). Two strict post-injection drawdown turning points occur for \(0<\tau<\tau_-\) and \(\tau>\tau_+\), but not for \(\tau_-\le\tau\le\tau_+\). At each boundary there is a stationary inflection. For \(b/a<\lambda<1\), two strict turning points exist at every positive delay; when \(\lambda=b/a\), they exist at every positive delay except \(\tau=a-b\). For \(a\le b\), \(m(\tau)\) decreases on its domain \(\tau>b-a\) from limit one (or from its continuous \(a=b\) zero-delay limit) to zero, so for each \(0<\lambda<1\) there is a single onset delay and no reentrant middle gap.

For the exact example \(a=4\), \(b=1\), \(\lambda=1/10\), the delays \(\tau=1/10\), \(3\), and \(100\) yield respectively **two, zero, and two** strict post-injection turning points. No numerical approximation is needed to verify these three classifications.

## Assumptions and scope

This is the infinite horizontal, homogeneous isotropic confined-aquifer, fully penetrating point-well approximation with constant \(\mathcal T,S\), initially uniform head, linear superposition, and wells a positive distance from the monitoring point. A pumping well extracts \(Q_P>0\) from time zero indefinitely. A distinct injection well adds \(Q_I>0\) at time \(\tau>0\) indefinitely. Define the exponential integral \(E_1(z)=\int_z^\infty e^{-u}u^{-1}\,du\) for \(z>0\), and normalize monitoring-point drawdown by \(4\pi\mathcal T/Q_P\):

\[
B(t)=\begin{cases}E_1(a/t),&0<t\le\tau,\\ E_1(a/t)-\lambda E_1(b/(t-\tau)),&t>\tau.\end{cases}
\]

The count of *strict extrema* is on the open interval \((\tau,\infty)\), not the count of zero-derivative times. Physical hydraulic head varies as minus the drawdown; its maxima and minima are interchanged but the number of turning points is unchanged.

## Proof

1. **Derivative comparison.** The fundamental identity \(\frac{d}{dt}E_1(c/t)=e^{-c/t}/t\), valid for \(c,t>0\), gives for \(t>\tau\)

\[
B'(t)=\frac{e^{-a/t}}t-\lambda\frac{e^{-b/(t-\tau)}}{t-\tau}.
\]

The second summand's positive unit-rate kernel shows that \(\operatorname{sign}B'(t)=\operatorname{sign}(\Phi_\tau(t)-\lambda)\). In particular \(\Phi_\tau(t)\to\infty\) as \(t\downarrow\tau\), and \(\Phi_\tau(t)\to1\) as \(t\to\infty\). Before injection, \(B'(t)>0\).

2. **Unique kernel minimum.** Differentiate its logarithm:

\[
\frac{d}{dt}\log\Phi_\tau(t)=\frac{Q(t)}{t^2(t-\tau)^2},\qquad
Q(t)=(\tau+a-b)t^2-\tau(\tau+2a)t+a\tau^2.
\]

Since \(Q(\tau)=-b\tau^2<0\), when \(C=\tau+a-b>0\) the quadratic has precisely one zero in \((\tau,\infty)\), namely \(t_m\) as stated: its discriminant is \(\tau^2(\tau^2+4ab)\). The derivative is strictly negative before that zero and strictly positive afterward. The limiting value at infinity is one, approached from below, whence \(0<m(\tau)<1\). When \(C\le0\), \(Q'(t)=2Ct-\tau(\tau+2a)<0\) on \((\tau,\infty)\), so \(Q(t)<0\) throughout and \(\Phi_\tau\) decreases strictly to one from above. The sign sequence of \(B'\) proves the exact extremum counts and the equality case.

3. **Delay envelope.** On the region \(C>0\), the minimizer \(t_m(\tau)\) is smooth. At its stationary point, the envelope derivative is

\[
\frac{d}{d\tau}\log m(\tau)=\frac{b-(t_m-\tau)}{(t_m-\tau)^2}.
\]

For fixed \(\tau\), evaluate the sign of \(\frac{d}{dt}\log\Phi_\tau\) at \(t=\tau+b\). The terms in \(b\) cancel, leaving exactly \((a-\tau-b)/(\tau+b)^2\). Since the derivative switches once from negative to positive at \(t_m\), it follows that \(t_m-\tau<b\) if \(\tau<a-b\), equality if \(\tau=a-b\), and \(t_m-\tau>b\) if \(\tau>a-b\). This proves the claimed strict monotonicity of \(m\) without differentiating its radical formula.

4. **Exact critical value and endpoint limits.** When \(a>b\) and \(\tau=a-b\), the unique minimizer is \(t_m=a\), so \(m=\frac ba e^{-a/a+b/b}=b/a\). To show \(m(\tau)\to0\) as \(\tau\downarrow0\), evaluate the positive function at \(t=\sqrt\tau\) for small \(\tau\), giving \(\log\Phi_\tau(\sqrt\tau)=(b-a)/\sqrt\tau+O(1)\to-\infty\). As \(\tau\to\infty\), evaluation at \(t=\tau+b\) yields \(\Phi_\tau(\tau+b)=\frac b{\tau+b}\exp(1-a/(\tau+b))\to0\). Positivity gives both minimum limits. If \(a\le b\), the existence interval starts at \(\tau>b-a\), and the minimizer tends to infinity as \(\tau\downarrow b-a\) when \(a<b\); thus \(m\to1\). If \(a=b\), continuity yields \(m\to1\) as \(\tau\downarrow0\). The strict derivative signs and the intermediate value theorem finish every threshold classification.

5. **Exact reentrant example.** At \(a=4,b=1\), the delay \(\tau=3\) has minimum \(m(3)=1/4>1/10\), so no strict extremum occurs. At \(\tau=1/10\), the admissible time \(t=1\) gives \(\Phi_{1/10}(1)=\frac9{10}e^{-26/9}<1/10\), since \(e^{26/9}>9\) already follows from its first four nonnegative Taylor terms. At \(\tau=100\), the time \(t=101\) gives \(\Phi_{100}(101)=101^{-1}e^{1-4/101}<e/101<3/101<1/10\). In both cases \(C>0\), \(0<\lambda<1\), and the minimum falls below \(\lambda\), forcing exactly two strict extrema.

## Verification

Run `python verify.py` with Python 3 and SciPy installed. The standalone program tests 4,500 reproducible parameter triples for the unique-kernel-minimum classification, independently compares 100 derivatives computed by Theis exponential integrals against differentiated analytic expressions, numerically brackets the two turning times in each reentrant example, and verifies exact inequality witnesses. The proof above, rather than the randomized checks or numerical roots, establishes the infinite-parameter statement. See `VERIFICATION.md` for reproducibility boundaries.

## Relationship to prior work

Theis (1935) supplies the transient single-well exponential-integral response, and linear groundwater superposition supplies its source-sign and timing combinations. Rushton (1985) and Weber--Chapuis (2013) analyze neighboring-well interference in pumping tests, concentrating on parameter inference and preceding/interfering pumping. The accessible detailed groundwater chapter explicitly treats additive pumping/recharge terms and uses a same-location, equal-rate negative source to represent pump cessation. The present result instead classifies **two distinct source locations, a positive injection delay, a strictly smaller injection rate, two strict transient turning points and their reentrant dependence on delay**, including the exact global \(b/a\) boundary. These historical response formulas are necessary premises but do not by themselves state this phase classification. Complete texts of the two closest interference papers were not accessible; broader coverage remains a real priority risk, not a claim of proven uniqueness.

## Limitations

The result is specific to the linear Theis idealization, continuous indefinitely operated point wells, perfect response observation, and fixed monitoring location. It does not incorporate heterogeneity, regional boundaries, leakage, wellbore storage, finite pump shutoff, spatially distributed recharge, or measurement noise. The formal infinite-time log drawdown can diverge under unequal net rates and should not be extrapolated as a physical field prediction. A critical-time pair may be observationally too close or its signal too weak to distinguish in practice. No field validation, policy optimization, or claim of independent review is made.

## References

1. C. V. Theis, "The relation between the lowering of the piezometric surface and the rate and duration of discharge of a well using ground-water storage," *Transactions, American Geophysical Union* **16** (1935), 519--524. DOI: 10.1029/TR016i002p00519.
2. K. R. Rushton, "Interference Due to Neighboring Wells During Pumping Tests," *Ground Water* **23** (1985), 361--366. DOI: 10.1111/j.1745-6584.1985.tb00781.x.
3. S. Weber and R. P. Chapuis, "Interpretation of a Pumping Test with Interference from a Neighboring Well," *Groundwater* **51** (2013), 935--944. DOI: 10.1111/gwat.12014; first online 2013-01-03.
4. Amanzi technical verification documentation, "Transient One-Dimensional Confined Flow to a Pumping Well (Theis)," https://amanzi.github.io/amanzi/UserGuide/verification/confined_flow/theis_isotropic_1d/amanzi_theis_isotropic_1d.html.
5. "Chapter 13 Groundwater," *Hydraulics and Water Resources: Examples Using R*, section 13.4.2 (time-varying well drawdowns, additive injection/superposition), https://edm44.github.io/hydr-watres-book/groundwater.html.
