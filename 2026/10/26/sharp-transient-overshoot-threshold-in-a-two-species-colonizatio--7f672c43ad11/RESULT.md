# Sharp transient-overshoot threshold in a two-species colonization hierarchy

## Finding

In the classical two-species competition–colonization model, recovery of the superior competitor after disturbance can generate a **single transient maximum** of inferior-species occupancy above its eventual coexistence value, but this overshoot is not inevitable. The initial inferior occupancy has a sharp threshold when superior-species recovery is faster than the inferior equilibrium relaxation.

For the notation below, put \(r=c_1-m_1>0\), \(K=r/c_1\), \(B=c_1+c_2\), \(C=c_2\), \(\lambda=c_2-m_2-BK>0\), and \(q=K/x_0-1>0\). The inferior species' limiting occupancy is \(y_*=\lambda/C\), and its instantaneous nullcline \(h(t)=(c_2-m_2-Bx(t))/C\) is strictly decreasing.

If \(r>\lambda\), define
\[
\begin{aligned}
I_\infty&=\frac{BKq}{r}(1+q)^{BK/r}\int_0^1\frac{u^{-\lambda/r}}{(1+qu)^{1+BK/r}}\,du,\\
y_{\rm crit}&=\frac{\lambda}{C(1+I_\infty)}.
\end{aligned}
\]
For any biologically admissible \(0<x_0<K\) and \(0<y_0\le 1-x_0\), the occupancy \(y(t)\) has exactly one strict interior maximum if and only if \(y_{\rm crit}<y_0<h(0)\). This maximum exceeds \(y_*\). If \(0<y_0\le y_{\rm crit}\), then \(y(t)\) increases strictly to \(y_*\), without a finite maximum. If \(y_0\ge h(0)\), it decreases strictly for positive time (apart from a possible zero initial derivative). If \(r\le\lambda\), the same one-peak conclusion holds for every \(0<y_0<h(0)\), whereas \(y_0\ge h(0)\) again gives decrease.

In the nontrivial threshold case \(r>\lambda\), write \(d=BKq\), \(\zeta=(1+q)^{BK/r}\), \(L(y_0)=1/y_{\rm crit}-1/y_0\), and \(A_0= C\zeta d r/[\lambda^2(r-\lambda)]\). As \(y_0\downarrow y_{\rm crit}\) from above, the unique peak time \(t_*\) and its amplitude satisfy
\[
t_*=\frac{1}{r-\lambda}\log\frac{A_0}{L(y_0)}+o(1),\qquad
y(t_*)-y_*\sim\frac dC\left(\frac{L(y_0)}{A_0}\right)^{r/(r-\lambda)}.
\]
Thus the finite peak disappears through logarithmic critical delay, with a noninteger peak-height power in general.

## Assumptions and scope

Consider the deterministic patch-occupancy equations introduced for a strict competitive hierarchy:
\[
\dot x=c_1x(1-x)-m_1x,\qquad
\dot y=c_2y(1-x-y)-m_2y-c_1xy.
\]
Here \(x\) is occupancy of the superior competitor and \(y\) is occupancy of the inferior competitor, with colonization rates \(c_i>0\) and local extinction rates \(m_i>0\). Assume \(c_1>m_1\), the coexistence inequality \(c_2-m_2>(c_1+c_2)(1-m_1/c_1)\), and \(0<x_0<K\), \(0<y_0\le1-x_0\). The closed biological triangle is forward-invariant because on \(x+y=1\), \(\dot x+\dot y=-m_1x-m_2y<0\). The theorem concerns this deterministic mean-field system, not stochastic extinction times, spatially resolved landscapes, or model classes with reverse displacement.

## Proof

**1. Superior recovery and an exact reciprocal solution.** Direct solution of the logistic equation gives
\[
x(t)=\frac{K}{1+q e^{-rt}},\quad a(t)=c_2-m_2-Bx(t)=\lambda+\delta(t),\quad
\delta(t)=\frac{d e^{-rt}}{1+q e^{-rt}}>0.
\]
The inferior equation is \(\dot y=y(a(t)-Cy)\), with strictly decreasing \(a(t)>\lambda\). Set \(F(t)=\int_0^t a(s)\,ds=\lambda t+(BK/r)\log[(1+q)/(1+q e^{-rt})]\). Since \(z=1/y\) solves \(\dot z=-a(t)z+C\),
\[
z(t)=e^{-F(t)}\left[\frac1{y_0}+C\int_0^t e^{F(s)}\,ds\right],\qquad
z(t)-\frac C\lambda=e^{-F(t)}\left[\frac1{y_0}-\frac C\lambda-\frac C\lambda I(t)\right],
\]
where \(I(t)=\int_0^t\delta(s)e^{F(s)}\,ds\). Since \(a(t)\to\lambda>0\), the first representation implies \(y(t)\to y_*\), e.g. by l'Hôpital's rule.

**2. At most one peak.** Write \(h(t)=a(t)/C\), so \(h'(t)<0\) and \(\dot y=Cy(h-y)\). At any meeting \(y=h\), the derivative of \(y-h\) is \(-h'(t)>0\). Therefore all such meetings cross from below to above; there is at most one, necessarily an interior strict maximum when the initial occupancy is below \(h(0)\). If \(y_0\ge h(0)\), the solution remains above the moving nullcline and decreases for every positive time.

**3. Exact existence criterion.** The integrand defining \(I\) is asymptotic to \(d\zeta e^{(\lambda-r)t}\). Consequently \(I(t)\to\infty\) exactly when \(r\le\lambda\), and \(I_\infty<\infty\) exactly when \(r>\lambda\). In the former case the reciprocal representation makes \(y(t)>y_*\) eventually; since a trajectory staying below \(h(t)\) increases to \(y_*\), this forces a crossing if \(y_0<h(0)\). In the latter case \(y_{\rm crit}=\lambda/[C(1+I_\infty)]\). If \(y_0\le y_{\rm crit}\), then \(z(t)>C/\lambda\) at all finite times, so \(y(t)<y_*<h(t)\), and \(y\) increases. If \(y_0>y_{\rm crit}\), the reciprocal bracket eventually becomes negative, so \(y(t)>y_*\) for large time; the same no-crossing contradiction forces exactly one maximum provided \(y_0<h(0)\). Substituting \(u=e^{-rt}\) gives the displayed integral for \(I_\infty\).

**4. Critical delay and peak height.** Suppose \(r>\lambda\) and \(y_0\downarrow y_{\rm crit}\). Put \(J(t)=I_\infty-I(t)\). At a peak \(y(t_*)=h(t_*)\), hence \(z(t_*)=C/a(t_*)\). The reciprocal identity yields the exact scalar equation
\[
L(y_0)=G(t_*),\qquad
G(t)=\frac C\lambda\left[J(t)+\frac{e^{F(t)}\delta(t)}{a(t)}\right].
\]
Here \(G'(t)=C e^{F(t)}\delta'(t)/a(t)^2<0\), \(G(t)\to0\), and \(G(0)=1/y_{\rm crit}-1/h(0)\). This independently shows existence and uniqueness for precisely \(y_{\rm crit}<y_0<h(0)\). Since \(e^{F(t)}\sim\zeta e^{\lambda t}\), \(\delta(t)\sim d e^{-rt}\), and \(J(t)\sim d\zeta e^{-(r-\lambda)t}/(r-\lambda)\), we obtain \(G(t)\sim A_0 e^{-(r-\lambda)t}\). Inverting gives the peak-time asymptotic. Finally \(y(t_*)=a(t_*)/C=y_*+\delta(t_*)/C\) gives the asserted height law.

## Verification

A self-contained script, `CHECK.py`, evaluates the explicit parameter example and checks the threshold and peak numerically. No finite computation is used to justify the theorem for all real admissible parameters; the proof above is analytic.

For \(c_1=2\), \(m_1=3/2\), \(c_2=2\), \(m_2=3/4\), and \(x_0=1/8\), one has \(r=1/2\), \(K=1/4\), \(\lambda=1/4\), \(q=1\), \(BK/r=2\), \(h(0)=3/8\), \(y_*=1/8\), and
\[
I_\infty=4+\frac{3\pi}{2},\qquad y_{\rm crit}=\frac1{40+12\pi}\approx0.01287015998,\qquad A_0=256.
\]
Starting from \(y_0=1/100\) produces monotone increase; \(y_0=1/50\) produces a single peak near \(t=8.69557\), followed by decrease to \(1/8\). For \(y_0=y_{\rm crit}(1+0.01)\), the peak time is approximately \(28.774985\), consistent with the logarithmic asymptotic estimate \(28.774994\).

## Relationship to prior work

Tilman (1994), equations (3.1a)–(3.1b), supplies the exact mean-field two-species hierarchical occupancy system and the coexistence equilibrium, as well as ecological motivation concerning recolonization and competition. This finding is not a new model or a new coexistence condition. It is the sharp **initial-value classification of an inferior-occupancy transient maximum**, together with the singular threshold law for its time and height. Doncaster, Pound and Cox (2003) analyze regional coexistence for competing species with a related mean-field spatial framework, but the inspected exposition does not state this classification or critical asymptotic. Hastings (1980) is a closely related antecedent, but its complete text was not accessible for comparison. General results about scalar logistic equations with time-dependent coefficients do not automatically contain the specific threshold, biological interpretation, and peak-delay coefficient without the computations above.

## Limitations

The novelty assessment is limited by inaccessible complete text of Hastings (1980), and by the possibility of an equivalent moving-nullcline overshoot result in other dynamical-systems literature. The formula assumes \(0<x_0<K\); above-equilibrium superior starts give a different forcing orientation. The finite peak theorem is deterministic, assumes strictly positive coexistence equilibrium and a hierarchy with displacement at rate \(c_1\), and makes no stochastic or spatially explicit assertion. The numerical script only supports the displayed example and is not a proof of the continuous parameter classification. Independent validation has not been performed.

## References

1. Tilman, D. (1994). *Competition and biodiversity in spatially structured habitats*. Ecology 75(1), 2–16. DOI: 10.2307/1939377. Lawful full text: https://users.wfu.edu/silmanmr/bio377/assignments/Readings/tilman1994.pdf (especially pp. 5–6).
2. Doncaster, C. P., Pound, G. E., and Cox, S. J. (2003). *Dynamics of regional coexistence for more or less equal competitors*. Journal of Animal Ecology 72, 116–126. DOI: 10.1046/j.1365-2656.2003.00687.x.
3. Hastings, A. (1980). *Disturbance, coexistence, history, and competition for space*. Theoretical Population Biology. DOI: 10.1016/0040-5809(80)90059-3. Only abstract and publication record accessible in this review.
4. Ovaskainen, O., and Hanski, I. (2002). *Transient dynamics in metapopulation response to perturbation*. Theoretical Population Biology. DOI: 10.1006/tpbi.2002.1586. Abstract inspected; concerns one-species metapopulation recovery.
