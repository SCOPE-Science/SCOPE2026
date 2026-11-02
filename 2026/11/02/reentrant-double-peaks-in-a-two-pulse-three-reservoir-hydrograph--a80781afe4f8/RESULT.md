# Reentrant double peaks in a two-pulse three-reservoir hydrograph

## Finding

For every delay \(\delta>0\) and second-to-first effective rainfall-volume ratio \(r>0\), define the dimensionless discharge response
\[
Q_{\delta,r}(t)=h(t)+r h(t-\delta),\qquad
h(u)=\begin{cases}u^2e^{-u},&u\ge0,\\0,&u<0.\end{cases}
\]
This is the superposition of two instantaneous inputs processed by the same three-stage Nash (Erlang-3) linear reservoir response. Multiplication by a positive constant or scaling all times by a fixed response time does not change the number of peaks.

**Exact classification.** There are exactly two distinct strict local maxima of \(Q_{\delta,r}\) on \([0,\infty)\) if and only if
\[
\delta>2,\qquad r>R(\delta):=
\frac{e^{-\delta}}2\left(\delta^2-2+\delta\sqrt{\delta^2-4}\right).
\]
For every other admissible parameter pair there is exactly one strict local maximum. On equality \(r=R(\delta)\) with \(\delta>2\), there is additionally one horizontal stationary shoulder after the second input, but no second maximum.

**Reentrant mode number.** The threshold \(R\) increases strictly on \((2,2\sqrt2)\), decreases strictly on \((2\sqrt2,\infty)\), and has
\[
\lim_{\delta\downarrow2}R(\delta)=e^{-2},\qquad
\max_{\delta>2} R(\delta)=R_*=(3+2\sqrt2)e^{-2\sqrt2},\qquad
\lim_{\delta\to\infty}R(\delta)=0.
\]
Thus for each \(r\in(e^{-2},R_*)\), there are unique delays \(2<\delta_-(r)<2\sqrt2<\delta_+(r)\) satisfying \(R(\delta_\pm)=r\). As the delay grows, the response is **bimodal** for \(2<\delta<\delta_-\), **unimodal** for \(\delta_-\le\delta\le\delta_+\), and **bimodal** again for \(\delta>\delta_+\). For \(\delta\le2\), it is always unimodal.

For \(0<r\le e^{-2}\), bimodality occurs only beyond the unique descending-branch solution to \(R(\delta)=r\); for \(r>R_*\), it occurs for every \(\delta>2\). At \(r=R_*\), every \(\delta>2\) is bimodal except \(\delta=2\sqrt2\), where a stationary shoulder replaces the second peak.

## Assumptions and scope

The two inputs are instantaneous, positive, separated by \(\delta\) response-time units, and additive; both traverse the identical three-stage linear reservoir cascade. There is no background discharge and no nonlinearity, routing heterogeneity, storm duration, or storage-capacity constraint. A *peak* means a strict local maximum of the continuous response, and a horizontal inflection is not a peak. Every \(\delta>0\) and \(r>0\) is included, with all equality boundaries.

## Proof

**1. Before the second input.** For \(0<t<\delta\), the derivative is
\[
Q'_{\delta,r}(t)=t(2-t)e^{-t}.
\]
If \(\delta>2\), the first peak is therefore a strict local maximum at \(t=2\), and \(Q'\) is strictly negative throughout \((2,\delta)\). If \(0<\delta<2\), the response increases until the second input. The case \(\delta=2\) is treated below.

**2. Exact post-input quadratic.** Put \(x=t-\delta\ge0\) and \(k=re^\delta>0\). Direct differentiation gives
\[
Q'_{\delta,r}(\delta+x)=e^{-(\delta+x)}P(x),\qquad
P(x)=-(1+k)x^2+2(1+k-\delta)x+\delta(2-\delta).
\]
Its discriminant is
\[
\operatorname{disc}(P)=4\left[k^2+(2-\delta^2)k+1\right].
\]
If \(0<\delta<2\), its constant coefficient is positive and its leading coefficient negative; it therefore has exactly one positive root, with derivative sign changing from positive to negative. Hence there is one maximum. If \(\delta=2\), then
\[
P(x)=x\{2(k-1)-(1+k)x\}.
\]
For \(k\le1\), the sole maximum is \(t=2\); for \(k>1\), the response increases through \(t=2\) and then has exactly one later maximum. No positive delay at most two produces two maxima.

**3. Exactly when a second maximum forms.** For \(\delta>2\), \(P(0)<0\) and \(P(x)\to-\infty\) as \(x\to\infty\). Two additional simple positive roots occur precisely if its vertex is positive and the discriminant is positive, namely
\[
k>\delta-1,\qquad k^2+(2-\delta^2)k+1>0.
\]
The latter quadratic in \(k\) has positive roots
\[
k_\pm(\delta)=\frac{\delta^2-2\pm\delta\sqrt{\delta^2-4}}2,
\quad k_-k_+=1.
\]
For \(\delta>2\), one has \(0<k_-<1<\delta-1<k_+\). Consequently both inequalities hold exactly when \(k>k_+\), equivalently \(r>e^{-\delta}k_+=R(\delta)\). In that case the two positive roots of \(P\) lie after the second input, and \(P\) changes sign negative–positive–negative. The earlier is a local minimum, the later a strict local maximum, in addition to the first maximum at \(t=2\). The stationary locations are
\[
t_\pm=\delta+\frac{k+1-\delta\pm\sqrt{k^2+(2-\delta^2)k+1}}{k+1}.
\]
At \(k=k_+\), the discriminant vanishes and \(P\) is nonpositive with a double positive root: the post-input stationary point is a non-extremal horizontal shoulder. For \(k<k_+\), the derivative never develops a positive interval post-input, so the first maximum remains unique. This proves the complete mode classification.

**4. The reentrant boundary.** The identity
\[
k_+(\delta)=\left(\frac{\delta+\sqrt{\delta^2-4}}2\right)^2
\]
implies
\[
\frac{d}{d\delta}\log R(\delta)=-1+\frac2{\sqrt{\delta^2-4}}.
\]
This derivative is positive until \(\delta=2\sqrt2\), zero there, and negative thereafter. The endpoint limits and maximal value above follow immediately. Strict monotonicity on both branches proves the asserted unique crossings and all equality cases.

## Verification

The accompanying `verify_hydrograph.py` is standalone Python using only the standard library. It checked 12,732 assertions, including exact-rational derivative-polynomial and discriminant identities for a grid of parameters, post-input positive-root geometry, and 70-digit decimal evaluations of selected phase points. None of these finite checks replaces the four analytic proof steps above.

With a fixed volume ratio \(r=1/5\), a small lag \(\delta=2.01\) gives \(R(2.01)\approx0.163641<r\) and two peaks; the intermediate lag \(\delta=3\) gives \(R(3)\approx0.341246>r\) and one peak; the larger lag \(\delta=5\) gives \(R(5)\approx0.154679<r\) and two peaks. Its two threshold delays are approximately \(2.0483558496\) and \(4.5209520275\).

To reproduce, run `python3 verify_hydrograph.py` in a directory containing the checker. No input data or external packages are required.

## Relationship to prior work

Muneepeerakul et al. (2010) model streamflow as overlapping gamma-shaped rainfall-response pulses and study streamflow distributions and autocorrelation. The present theorem fixes two inputs and instead classifies the *number of temporal discharge peaks*, exactly, for the three-stage response. Yang, Endreny and Nowak (2015) analyze double-peaked events using two advection–diffusion runoff components driven by a single event; their hydrological motivation is related, but their kernels and question differ.

Došlá (2009) gives general mixture-modality criteria and explicit gamma-mixture results for *different rates* or *different shapes* at a common origin. Its general theorem supplies an implicit framework applicable to shifted component distributions, so it is a genuine and material broader predecessor. It does not provide the explicit translated Erlang-3 threshold, its single turning point as lag varies, or the resulting two–one–two reentrance; those rely on the positive-shift derivative quadratic and its exact global parameter geometry. Historical priority for that specialization remains provisional.

## Limitations

The theorem is exact only for two idealized instantaneous pulses with a common Erlang-3 response kernel. It does not establish that a given observed double-peaked hydrograph arises from two storms, nor that actual catchments obey identical linear three-stage routing. Other gamma shapes, finite storm durations, spatial routing, antecedent storage, nonlinear response, or measurement smoothing can alter the mode count. The amplitudes of the two peaks are not ranked by this theorem. A strict local peak may be small and observationally unresolved. General mixture criteria and unexamined hydrological literature remain residual historical-priority risks; this is not independently audited.

## References

- Muneepeerakul, R., Azaele, S., Botter, G., Rinaldo, A., and Rodriguez-Iturbe, I. (2010). *Daily streamflow analysis based on a two-scaled gamma pulse model*. Water Resources Research 46, W11546. First online November 23, 2010. https://doi.org/10.1029/2010WR009286
- Yang, Y., Endreny, T. A., and Nowak, D. J. (2015). *Simulating double-peak hydrographs from single storms over mixed-use watersheds*. Journal of Hydrologic Engineering 20(11), 06015003. https://doi.org/10.1061/(ASCE)HE.1943-5584.0001225
- Došlá, Š. (2009). *Conditions for bimodality and multimodality of a mixture of two unimodal densities*. Kybernetika 45(2), 279–292. https://dml.cz/handle/10338.dmlcz/140075
