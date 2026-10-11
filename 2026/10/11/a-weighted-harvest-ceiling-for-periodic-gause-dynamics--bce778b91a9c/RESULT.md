# A weighted harvest ceiling for periodic Gause dynamics

## Finding

Consider the periodic Gause-type predator–prey model
\[
\dot x=r(t)\left(1-\frac{x}{K}\right)(x-m(t))x-\frac{s(t)x^2}{x^2+a(t)^2}y-H_1(t),
\]
\[
\dot y=\left(\frac{p(t)x^2}{x^2+a(t)^2}-b(t)y-c(t)\right)y-H_2(t).
\]
Assume \(K>0\), all displayed coefficient functions are positive and \(T\)-periodic, \(p,s\in C^1\), and
\[
0<m(t)<K\qquad\text{for every }t.
\]
Define
\[
q(t)=\frac{s(t)}{p(t)},\qquad
\eta(t)=q(t)c(t)-\dot q(t).
\]
If \(\eta(t)\ge0\) for all \(t\), then every strictly positive \(T\)-periodic solution obeys the exact balance
\[
\overline{H_1}+\overline{qH_2}+\overline{qb y^2}+\overline{\eta y}
=\overline{G(t,x(t))}, \tag{1}
\]
where
\[
G(t,u)=r(t)u\left(1-\frac{u}K\right)(u-m(t))
\]
and \(\overline f=T^{-1}\int_0^T f(t)\,dt\).

For each \(t\), set
\[
u_*(t)=\frac{K+m(t)+\sqrt{K^2-Km(t)+m(t)^2}}3
\]
and
\[
G_*(t)=\frac{r(t)}K\,u_*(t)[K-u_*(t)][u_*(t)-m(t)].
\]
Then every strictly positive \(T\)-periodic solution necessarily satisfies
\[
\boxed{\ \overline{H_1}+\overline{qH_2}<\overline{G_*}\ }. \tag{2}
\]
Thus violation of (2) is a nonexistence certificate for positive locked cycles. Notably, the ceiling contains no \(a(t)\): the Holling-III half-saturation coefficient disappears from the exact budget.

There is also an explicit predator-mean bound. Define
\[
\theta_L=\min_{0\le t\le T}q(t)b(t)>0,\qquad
\eta_L=\min_{0\le t\le T}\eta(t)\ge0,
\]
\[
\Delta=\overline{G_*}-\overline{H_1}-\overline{qH_2}.
\]
For every positive periodic solution, \(\Delta>0\) and
\[
\overline y\le
\frac{\sqrt{\eta_L^2+4\theta_L\Delta}-\eta_L}{2\theta_L}. \tag{3}
\]
The fixed-ratio case \(s(t)=\kappa p(t)\) is the simple corollary \(q\equiv\kappa\), for which \(\eta=\kappa c\).

## Assumptions and scope

The claim is conditional on a strictly positive \(T\)-periodic solution. It does not assert existence. The source allows positive continuous periodic coefficients; the present balance additionally requires \(p\) and \(s\) to be continuously differentiable so that \(q=s/p\) has a classical derivative. The pointwise condition \(0<m(t)<K\) is imposed to make the positive prey-production maximum explicit, and \(\eta(t)\ge0\) is the checkable condition
\[
c(t)-\frac{d}{dt}\log q(t)\ge0.
\]
No conclusion is claimed when this sign condition fails.

## Proof

Let
\[
\Phi(t)=x(t)+q(t)y(t),\qquad q(t)=\frac{s(t)}{p(t)}.
\]
Differentiating and substituting the system gives
\[
\begin{aligned}
\dot\Phi
={}&r(t)x\left(1-\frac{x}{K}\right)(x-m(t))-H_1(t)\\
&-\frac{s(t)x^2}{x^2+a(t)^2}y
+q(t)\frac{p(t)x^2}{x^2+a(t)^2}y\\
&-q(t)b(t)y^2-q(t)c(t)y-q(t)H_2(t)+\dot q(t)y.
\end{aligned}
\]
Because \(q(t)p(t)=s(t)\), the two Holling-III terms cancel identically. Therefore
\[
\dot\Phi=G(t,x)-H_1-qH_2-qb y^2-\eta y. \tag{4}
\]
Averaging (4) over a period and using \(\Phi(T)=\Phi(0)\) proves (1).

It remains to maximize \(G(t,u)\) pointwise. For fixed \(t\), write \(m=m(t)\) and \(r=r(t)\). Since \(0<m<K\), the factor
\[
u(K-u)(u-m)
\]
is negative on \((0,m)\) and on \((K,\infty)\), and positive on \((m,K)\). Its derivative is
\[
-3u^2+2(K+m)u-Km.
\]
The unique critical point in \((m,K)\) is
\[
u_*=\frac{K+m+\sqrt{K^2-Km+m^2}}3.
\]
Hence \(G(t,u)\le G_*(t)\) for every \(u\ge0\). Combining this pointwise inequality with (1) gives
\[
\overline{H_1}+\overline{qH_2}+\overline{qb y^2}+\overline{\eta y}
\le\overline{G_*}.
\]
For a strictly positive solution, \(q(t)b(t)y(t)^2>0\) at every time. Thus the third term on the left has strictly positive mean, while the fourth is nonnegative, proving the strict ceiling (2).

For (3), (1) and \(G(t,x(t))\le G_*(t)\) imply
\[
\overline{qb y^2}+\overline{\eta y}\le\Delta.
\]
By the definitions of \(\theta_L\) and \(\eta_L\), and Jensen's inequality,
\[
\overline{qb y^2}\ge\theta_L\overline{y^2}\ge\theta_L\overline y^2,
\qquad
\overline{\eta y}\ge\eta_L\overline y.
\]
Thus
\[
\theta_L\overline y^2+\eta_L\overline y\le\Delta.
\]
Solving this quadratic inequality for the nonnegative quantity \(\overline y\) gives (3).

## Verification

The standalone `verify.py` file symbolically checks the cancellation in (4), verifies the critical-point formula for \(u_*\), and verifies the quadratic root used in (3). Running that packaged file returns `VERIFY_OK`.

The proof itself is analytic. No finite simulation, numerical quadrature, or parameter sampling is used to infer the periodic identity or the nonexistence ceiling.

## Relationship to prior work

Yu, Liu, and Lin introduce exactly the positive \(T\)-periodic Gause-type system above, with Allee effect, Holling type III response, predator competition, and harvesting of both species. Their main result gives sufficient conditions for multiple positive periodic solutions using coincidence degree. The inspected full text treats the predation and harvesting terms separately and does not state the weighted identity (1), the ceiling (2), or the mean bound (3).

Etoua and Rousseau study an earlier autonomous generalized Gause model with Holling type III response and constant prey harvesting. Their full text develops the bifurcation diagram and frames maximum sustainable yield as a central issue. That model has no Allee factor, no predator harvest, and no periodic coefficient ratio \(q=s/p\); its stated results do not imply (1)--(3). It is nevertheless the closest inspected structural predecessor because it combines Gause predation, Holling III response, and harvesting.

Semantic searches also compared the claim with published balance-law records for other dynamical systems. Those records concern different vector fields and do not specialize to this periodic predator–prey budget.

## Limitations

The ceiling is necessary, not sufficient. It applies only to strictly positive locked \(T\)-cycles and under \(\eta=q c-\dot q\ge0\). The coefficient assumptions are slightly stronger than the source because \(p\) and \(s\) must be \(C^1\). The pointwise maximization uses \(0<m(t)<K\); no claim is made for other Allee-threshold regimes. The mean-predator bound uses only coefficient minima and is not claimed to be globally sharp. Energy-balance cancellations are classical in predator–prey modeling, so related identities may exist elsewhere under different notation; the originality assessment is limited to the inspected literature and indexed comparisons.

## References

S. Yu, J. Liu, X. Lin, *Multiple positive periodic solutions of a Gause-type predator-prey model with Allee effect and functional responses*, AIMS Mathematics 5 (2020), 6135--6148, DOI 10.3934/math.2020394. First public publisher date used here: 2020-07-29.

R. M. Etoua, C. Rousseau, *Bifurcation analysis of a generalized Gause model with prey harvesting and a generalized Holling response function of type III*, Journal of Differential Equations 249 (2010), 2316--2356, DOI 10.1016/j.jde.2010.06.021.
