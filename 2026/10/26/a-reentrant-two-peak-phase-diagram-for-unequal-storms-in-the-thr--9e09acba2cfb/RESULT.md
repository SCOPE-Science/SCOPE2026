# A reentrant two-peak phase diagram for unequal storms in the three-reservoir Nash cascade

## Finding

Consider two instantaneous rainfall-excess pulses of positive volumes \(V_1,V_2\), separated by \(D>0\), routed through the same linear cascade of **three** identical reservoirs, each with storage-time coefficient \(K>0\). Put \(d=D/K\), \(m=V_2/V_1\), and \(h(x)=\tfrac12x^2e^{-x}\) for \(x\ge0\), with \(h(x)=0\) otherwise. The normalized outflow is
\[
q_{d,m}(x)=h(x)+m h(x-d),\qquad x\ge0.
\]
Here and throughout, a peak means a **strict local maximum** of the continuous outflow on positive time, rather than merely a stationary point.

**Complete classification.** For every \(m,d>0\), the function \(q_{d,m}\) has either one or two strict local maxima. For \(0<d\le2\), it has exactly one. For \(d>2\), set
\[
C(d)=\frac{e^{-d}}4\left(d+\sqrt{d^2-4}\right)^2.
\]
It has exactly **two** strict local maxima if and only if \(m>C(d)\); if \(m\le C(d)\), including equality, it has exactly **one**. In the two-peak regime, the first peak is exactly at \(x=2\); a strict intervening minimum and a later strict maximum occur after \(x=d\).

**Reentrant separation effect.** The exact boundary \(C\) increases strictly on \((2,2\sqrt2)\), decreases strictly on \((2\sqrt2,\infty)\), and has the unique global maximum
\[
m_*=\left(3+2\sqrt2\right)e^{-2\sqrt2}.
\]
Moreover \(\lim_{d\downarrow2}C(d)=e^{-2}\) and \(\lim_{d\to\infty}C(d)=0\). Consequently, every fixed relative second-pulse volume satisfying
\[
e^{-2}<m<m_*
\]
produces precisely two transition separations \(2<d_-<2\sqrt2<d_+\) defined by \(C(d_\pm)=m\). As \(d\) increases **within \((2,\infty)\)**, the number of strict outflow peaks is two on \((2,d_-)\), one on \([d_-,d_+]\), and two on \((d_+,\infty)\). Thus increasing storm separation can temporarily *erase*, then restore, a second peak.

For example, with \(m=3/10\) and increasing separations \(d=21/10,3,5\), the exact peak counts are \(2,1,2\), respectively.

## Assumptions and scope

The cascade is linear, time invariant, initially empty, and driven by exactly two idealized instantaneous **nonnegative** rainfall-excess inputs. All three stages have the same positive time constant \(K\), and neither routing losses nor variable catchment conditions are included. The first and second storm excess volumes are strictly positive. The object being classified is the number of strict local maxima of the **continuous outlet hydrograph**; no inference about empirical flood risk, peak heights, or detection thresholds follows from mode count alone.

The unnormalized response of a unit impulse is \(H_K(t)=K^{-1}h(t/K)\); hence \(Q(t)=(V_1/K)q_{d,m}(t/K)\). Positive changes in units and overall discharge scale do not change local-maximum counts. Dimensionless \(d,m\) specify the entire problem.

## Proof

First, \(h'(x)=\tfrac12e^{-x}x(2-x)\) for \(x>0\), and both \(h\) and \(h'\) vanish at zero. Therefore, before the second impulse, \(q'_{d,m}(x)=h'(x)\). For \(x>d\), set \(M=me^d>0\). Multiplication of \(q'_{d,m}\) by the strictly positive factor \(2e^x\) gives the concave quadratic
\[
F(x)=x(2-x)+M(x-d)(2-x+d)
=-(1+M)x^2+2[1+M(1+d)]x-Md(d+2).
\]
Its discriminant is
\[
\Delta_F=4\big((1+M)^2-d^2M\big),
\]
and its vertex is \(x_v=[1+M(1+d)]/(1+M)=1+Md/(1+M)\).

If \(0<d<2\), then \(q'_{d,m}>0\) on \((0,d]\) and \(F(d)=d(2-d)>0\). A strictly concave quadratic positive at \(d\) and negative at infinity has exactly one zero to the right of \(d\), at which the derivative changes from positive to negative. There is exactly one strict maximum.

At \(d=2\), the pre-impulse derivative is positive on \((0,2)\). For \(x=2+u\), \(u>0\), the derivative sign is that of
\[
F(2+u)=u\big(2(M-1)-(1+M)u\big).
\]
If \(M\le1\), the unique strict maximum is at \(x=2\); otherwise the derivative stays positive immediately after \(2\) and changes sign once at a later point. There is again exactly one strict maximum. The possible stationary shoulder at \(x=2\) is not counted as an additional peak.

Now let \(d>2\). The first isolated response has its strict maximum at \(x=2<d\). Since \(F(d)=d(2-d)<0\) and \(F(x)\to-\infty\), there is an additional strict maximum precisely when the quadratic is positive somewhere for \(x>d\). This requires \(x_v>d\), equivalent to \(M>d-1\), together with \(\Delta_F>0\). Because \(d>2\), the discriminant inequality holds exactly for \(0<M<M_-(d)\) or \(M>M_+(d)\), where
\[
M_\pm(d)=\frac{d^2-2\pm d\sqrt{d^2-4}}2,
\quad M_-(d)<1<d-1<M_+(d).
\]
The vertex requirement rules out the lower branch. Hence two distinct zeros strictly after \(d\), with derivative signs negative/positive/negative, exist exactly when \(M>M_+(d)\), or equivalently \(m>C(d)=e^{-d}M_+(d)\). At equality, the quadratic merely touches zero at its vertex, with no derivative sign reversal, so only the first peak remains. Below equality, \(F\le0\) after \(d\) and again only the first peak remains. This proves the exhaustive classification.

For the boundary, \(C(d)=\exp(2\operatorname{arcosh}(d/2)-d)\). Differentiation gives
\[
\frac{C'(d)}{C(d)}=\frac{2}{\sqrt{d^2-4}}-1.
\]
This changes sign exactly at \(d=2\sqrt2\), from positive to negative. Direct substitution gives \(m_*\); the two limits follow from the explicit expression. The intermediate value theorem, strict monotonicity on both sides, and \(e^{-2}<m<m_*\) yield exactly two transition separations and the stated reentrant sequence.

For the example \(m=3/10\), one has \(e^{-2}<3/10<m_*\) rigorously: \(e^2>7\) proves the first inequality; using \(7/5<\sqrt2<29/20\), \(8/3<e<11/4\), and \(e^{1/10}>11/10\) gives \(m_*>(29/5)/(605/32)=928/3025>3/10\). At \(d=21/10\), \(\sqrt{d^2-4}<7/10\), so \(M_+(d)<97/50\), whereas \(me^d>(3/10)e^2>21/10\); this proves two peaks. At \(d=3\), \(M_+(3)=(7+3\sqrt5)/2>13/2\), while \(me^3<(3/10)(11/4)^3<13/2\); this proves one peak. At \(d=5\), \(M_+(5)<24\) and \(me^5>(3/10)(8/3)^5>24\), proving two peaks. The elementary bounds \(8/3<e<11/4\) and \(e^2>7\) follow directly from the convergent exponential series (with its geometrically bounded positive tail). No numerical root isolation is needed for the example.

## Verification

The included standalone `verify.py` evaluates the stationary-point quadratic, tests derivative sign changes and the \(m>C(d)\) classification on 3,999 reproducible random parameter choices away from fold boundaries, and checks the exact example \(d=21/10,3,5\). It also checks the unique maximizing separation numerically at five nearby offsets. Run with `python verify.py`; it requires only the Python standard library. The proof above, not these finite checks, establishes all positive real parameter cases and boundary equalities.

## Relationship to prior work

Nash's linear-reservoir impulse-response construction gives the gamma/Erlang hydrograph. Muneepeerakul et al. (2010), section 2 and conclusions, model streamflow as overlapping gamma-shaped event pulses and study its statistical distribution and autocorrelation; they do not provide this deterministic two-storm local-maxima phase diagram. Gnecco, Palla and La Barbera (2018), sections 2–4, study a dimensionless gamma IUH and the global runoff peak under a constant-duration hyetograph, not unequal delayed instantaneous pulses or a reentrant *number-of-maxima* boundary. Gioia (2016) studies double-peak design floods via superposed equal-peak Weibull-shaped inputs and reservoir-routing heights; accessible source material does not establish the unequal three-stage Nash classification here. All three are close contextual precedents and not sources of this theorem.

The equal-impulse, three-reservoir special case \(m=1\) is already covered by existing work: two maxima occur exactly for \(d>2\). That special case is **not** claimed as new; indeed \(m=1>m_*\) recovers it immediately. The substantive difference here is the exact free amplitude-ratio threshold, including the nonmonotone boundary and the \(2\to1\to2\) peak-count reversal at fixed \(m\). An unknown broader theorem on translates of gamma densities could imply the special structure; absence from the consulted sources is not proof of absolute historical priority.

## Limitations

All maxima are ideal mathematical local maxima, including tiny secondary peaks that may be undetectable in noisy records. No claim is made for finite-width storms, nonlinear channel routing, unequal reservoir time constants, variable rainfall intensity, water storage limits, empirically estimated peaks or hydrologic safety. Boundary equality has a degenerate stationary point but not a second maximum. The value of a reentrant peak-count classification lies in preventing simplistic monotonicity assumptions about how temporal storm separation resolves two runoff waves; it does not prescribe flood-management actions.

## References

1. J. E. Nash, *Systematic determination of unit hydrograph parameters*, Journal of Geophysical Research **64** (1959), 111–115. DOI: 10.1029/JZ064i001p00111.
2. R. Muneepeerakul, S. Azaele, G. Botter, A. Rinaldo, I. Rodriguez-Iturbe, *Daily streamflow analysis based on a two-scaled gamma pulse model*, Water Resources Research **46** (2010), W11546. DOI: 10.1029/2010WR009286. First published 2010-11-23.
3. A. Gioia, *Reservoir Routing on Double-Peak Design Flood*, Water **8** (2016), 553. DOI: 10.3390/w8120553.
4. I. Gnecco, A. Palla, P. La Barbera, *A dimensionless approach for the runoff peak assessment: effects of the rainfall event structure*, Hydrology and Earth System Sciences **22** (2018), 943–956. DOI: 10.5194/hess-22-943-2018.
