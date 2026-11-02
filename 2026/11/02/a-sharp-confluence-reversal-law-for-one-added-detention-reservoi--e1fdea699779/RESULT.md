# A sharp confluence reversal law for one added detention reservoir

## Finding

**Theorem (peak reversal and globally sharp amplification).** Let \(a,b>0\), \(r=b/a\), \(\beta\geq1\), and \(\Delta\geq0\). Two tributaries deliver instantaneous runoff volumes \(1\) and \(\beta\), at times \(0\) and \(\Delta\) respectively. Before intervention, each pulse passes through a first-order linear reservoir with outflow rate \(a\). A new *serial* linear reservoir with rate \(b\) is inserted on the **first** tributary only, without loss of volume. At their ideal storage-free confluence, let \(P_0\) and \(P_b\) be the respective global peak discharges before and after intervention. Put \(\delta=a\Delta\) and

\[
m(r)=\begin{cases}\log r/(r-1),&r\ne1,\\1,&r=1.\end{cases}
\]

For **every** such set of parameters,

\[
\operatorname{sgn}(P_b-P_0)=\operatorname{sgn}(\delta-m(r)).
\]

Thus the added detention decreases the peak for \(\delta<m(r)\), leaves it unchanged exactly at \(\delta=m(r)\), and *increases* it for \(\delta>m(r)\). This threshold does not depend on the second tributary's volume \(\beta\ge1\).

The maximum harmful increase, optimized over all \(\Delta\ge0\) for fixed \(a,b,\beta\), is unique and occurs at \(\delta=2m(r)\):

\[
\max_{\Delta\ge0}(P_b-P_0)=a\begin{cases}r^{-(r+1)/(r-1)},&r\ne1,\\e^{-2},&r=1.\end{cases}
\]

Optimizing additionally over **all** \(b>0\) gives the universal sharp bound

\[
P_b-P_0\le ae^{-2},
\]

with equality if and only if \(b=a\) and \(\Delta=2/a\). The bound remains sharp for each fixed \(\beta\ge1\).

## Assumptions and scope

An instantaneous unit runoff volume traversing an initially empty first-order reservoir with constant outflow rate \(a\) gives \(ae^{-at}\) for \(t\ge0\) and zero before the pulse. The second branch has the same original rate but pulse volume \(\beta\ge1\), arriving \(\Delta\) later. The first branch is changed by a second independent, *serial* linear storage stage of rate \(b\). All rates and volumes are fixed, all systems are linear and conservative, and the confluence sums its inputs without further routing. The finite peak is the supremum of the right-continuous downstream discharge for \(t\ge0\). No channel backwater, spatially distributed precipitation, nonlinear outflow, multiple storms, or empirical fitting is modeled.

After nondimensionalizing \(x=at\), the first branch's modified impulse response is

\[
g_r(x)=\begin{cases}
\displaystyle \frac{r}{r-1}\left(e^{-x}-e^{-rx}\right),&r\ne1,\\
x e^{-x},&r=1,
\end{cases}\quad x\ge0.
\]

We set \(g_r(x)=0\) for negative \(x\). The dimensionless original and modified confluence discharges are

\[
q_0(x)=e^{-x}+\beta\mathbf1_{x\ge\delta}e^{-(x-\delta)},\qquad
q_b(x)=g_r(x)+\beta\mathbf1_{x\ge\delta}e^{-(x-\delta)}.
\]

## Proof

**1. Exact routing and the unmodified peak.** Convolution of \(e^{-x}\mathbf1_{x\ge0}\) with \(re^{-rx}\mathbf1_{x\ge0}\) gives \(g_r\), including its continuous value at \(r=1\). Before the second pulse, the original discharge is decreasing from \(1\); at the second pulse it jumps to \(\beta+e^{-\delta}\) and then decreases. As \(\beta\ge1\),

\[
P_0/a=\beta+e^{-\delta}.
\]

For every finite \(r>0\), \(0\le g_r(x)<1\), since it is a proper positive convolution with a strictly subunit exponential factor over an interval of strictly less than full kernel mass. Consequently \(g_r(x)<P_0/a\) before the second pulse, and the modified global peak occurs at or after that pulse.

**2. One mode and one peak after arrival.** Differentiation gives

\[
g_r'(x)=\frac{r}{r-1}\left(-e^{-x}+re^{-rx}\right)
\]

when \(r\ne1\), and \(g_1'(x)=(1-x)e^{-x}\). It is positive for \(0\le x<m(r)\), zero precisely at \(m(r)\), and negative beyond. Moreover,

\[
g_r(x)-e^{-x}=\begin{cases}\displaystyle\frac{e^{-x}-re^{-rx}}{r-1},&r\ne1,\\(x-1)e^{-x},&r=1.\end{cases}
\]

Its sign is precisely the sign of \(x-m(r)\).

For \(x\ge\delta\), write \(h_\delta(x)=g_r(x)+\beta e^{\delta-x}\). The quantity \(e^xh_\delta'(x)\) is **strictly decreasing** in \(x\): its derivative is \(-r^2e^{-(r-1)x}<0\) for \(r\ne1\), and \(-1\) for \(r=1\). Hence \(h_\delta\) has a unique global maximizer on \([\delta,\infty)\), either at \(x=\delta\) or at the unique interior solution of \(h_\delta'=0\).

If an interior maximizer exists, it can only occur when \(r>\beta\ge1\), and is explicitly

\[
x_*(\delta)=\frac{1}{r-1}\log\left(\frac{r^2}{r+(r-1)\beta e^{\delta}}\right)>\delta.
\]

Otherwise the maximizer is \(x=\delta\). In particular, once \(\delta\ge m(r)\), both \(g_r\) and the second-tributary term decrease on \([\delta,\infty)\), so

\[
P_b/a=\beta+g_r(\delta)\qquad(\delta\ge m(r)).
\]

**3. Exact safe/harmful boundary.** For \(\delta\ge m(r)\), the formula above and the sign of \(g_r(\delta)-e^{-\delta}\) settle the comparison, including equality and strict harm. For \(0\le\delta<m(r)\), define

\[
D(\delta)=\max_{x\ge\delta}h_\delta(x)-\beta-e^{-\delta}.
\]

At the endpoint \(\delta=m(r)\), the maximizing time is \(x=\delta\) and \(D=0\). On a parameter interval where the maximizing time is at the boundary, the derivative is \(D'(\delta)=g_r'(\delta)+e^{-\delta}>0\) below \(m(r)\). Where it is interior, the envelope derivative is \(D'(\delta)=\beta e^{\delta-x_*(\delta)}+e^{-\delta}>0\). There can be at most one switch between these regimes below \(m(r)\): on \([0,m(r)]\), \(g_r'\) decreases strictly from \(r\) to zero, so the boundary criterion \(g_r'(\delta)\le\beta\) changes at most once. Continuity at the switch yields that \(D\) is strictly increasing on \([0,m(r)]\). Since \(D(m(r))=0\), it is strictly negative for every smaller lag. No exceptional case occurs at \(r=1\), \(\beta=1\), or \(\delta=0\).

**4. The sharp worst-case penalty.** For \(\delta>m(r)\), the dimensionless excess is

\[
E_r(\delta)=\frac{P_b-P_0}{a}=
\begin{cases}\displaystyle\frac{e^{-\delta}-re^{-r\delta}}{r-1},&r\ne1,\\(\delta-1)e^{-\delta},&r=1.\end{cases}
\]

It increases strictly on \((m(r),2m(r))\), decreases strictly on \((2m(r),\infty)\), and tends to zero at infinity. Its unique positive maximum equals

\[
E_r(2m(r))=\frac{e^{-2m(r)}}r
=r^{-(r+1)/(r-1)}
\]

for \(r\ne1\), with limiting value \(e^{-2}\) at \(r=1\). To optimize over rate contrast write \(r=e^{2u}\); then

\[
-\log E_r(2m(r))=2u\coth u\ge2,
\]

where the inequality is strict for \(u\ne0\) because \(\tanh |u|<|u|\) for \(u\ne0\). This proves the universal bound, and the strict equality characterization. The expression is independent of \(\beta\ge1\), completing the proof.

## Verification

The standalone `checker.py` reproduces the convolution formulas, the peak-time calculation, the mode and twice-mode identities, and the universal bound over a deterministic grid of positive rate contrasts, downstream volume ratios, and arrival lags. It also contains exact-rational checks for the contrasts \(r=2\) and \(r=1/2\). Run `python3 checker.py`; no external packages or network access are required. The proof above—not the finite grid—establishes the assertions for all parameters.

For instance, at \(a=b=1\), \(\beta=1\), and \(\Delta=2\), the unmodified peak is \(1+e^{-2}\), while the modified peak is \(1+2e^{-2}\), a rise of exactly \(e^{-2}\) even though the first tributary's individual peak falls from \(1\) to \(e^{-1}\).

## Relationship to prior work

The qualitative downstream danger of local stormwater detention is **not new**. McCuen (1979) reported an applied watershed example in which basin management increased downstream peak flow; only the available abstract and publication information were inspected. Pattison et al. (2014), available in full publisher HTML, studied tributary peak timing, sequencing, and downstream amplification with numerical hydraulic simulation and documented nonmonotone effects of delays. Those statements motivate, but do not directly yield, the explicit *all-rate* threshold \(m(r)\), the twice-mode worst delay, the invariance under \(\beta\ge1\), or the global sharp constant \(e^{-2}\). Błażejewski and Murat-Błażejewska (2003) discuss analytical routing through a single detention basin for trapezoidal inflow; its abstract was accessible, but its full text was not inspected. No claim of a new general attenuation paradox, new convolution principle, or empirical flood-risk prediction is made.

The precise universal bound and equality classification were not identified in the accessible sources or relevant published-record searches, but historical priority remains provisional. In particular, an uninspected older analytical routing or linear-systems source might already imply the same statement.

## Limitations

The theorem requires two isolated input impulses, matching original rate parameters, a storage-free confluence, only one added serial linear reservoir, and \(\beta\ge1\). For smaller downstream contributions the initial tributary peak may dominate, invalidating the universal decision rule. Finite-width rainfall, nonlinear storage, controlled release, backwater and channel geometry are not covered. A dimensionless peak increase of \(e^{-2}\) is not a bound on observed flood stage or damage. No independent audit has been performed.

## References

1. Pattison, I., Lane, S. N., Hardy, R. J., and Reaney, S. M. (2014). *The role of tributary relative timing and sequencing in controlling large floods.* Water Resources Research **50**, 5444–5458. First published 2014-06-06. https://doi.org/10.1002/2013WR014067
2. McCuen, R. H. (1979). *Downstream Effects of Stormwater Management Basins.* Journal of the Hydraulics Division **105**(11), 1343–1356. https://doi.org/10.1061/JYCEAJ.0005300
3. Błażejewski, R., and Murat-Błażejewska, S. (2003). *Analytical solutions of a routing problem for storm water in a detention basin.* Hydrological Sciences Journal **48**(4), 665–671. https://doi.org/10.1623/hysj.48.4.665.51413
