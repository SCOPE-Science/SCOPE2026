# Uniform basin separators and negative dependence in a cubic chaotic skew product

## Finding
Fix \(0<\beta<1\) and define
\[
a_\beta(y)=y(1-y)(y-\beta),\qquad g_\pm(y)=y\pm a_\beta(y),\quad 0\le y\le1.
\]
Let \((\varepsilon_n)_{n\ge0}\) be independent fair signs and set \(Y_0(y)=y\), \(Y_{n+1}(y)=g_{\varepsilon_n}(Y_n(y))\). One driving sequence is shared by all initial conditions. With probability one there are unique thresholds \(U_\beta\in(0,\beta)\), \(V_\beta\in(\beta,1)\) with the following global basin partition:
\[
\lim_{n\to\infty}Y_n(y)=\begin{cases}
0,&0\le y<U_\beta,\\
\beta,&U_\beta<y<V_\beta,\\
1,&V_\beta<y\le1.
\end{cases}
\]
The points \(0,\beta,1\) are fixed, and no conclusion is asserted for trajectories starting at the thresholds themselves. The separator marginal laws are exactly
\[
\Pr(U_\beta<u)=\frac{u}{\beta}\quad(0<u<\beta),\qquad
\Pr(V_\beta<v)=\frac{v-\beta}{1-\beta}\quad(\beta<v<1).
\]
They are nevertheless strictly negatively quadrant dependent. For all \(0<u<\beta<v<1\),
\[
\begin{aligned}
&\Pr(U_\beta<u,V_\beta<v)-\frac{u(v-\beta)}{\beta(1-\beta)}\\
&\quad=\frac{1}{\beta(1-\beta)}\sum_{n=0}^{\infty}
\mathbb E[a_\beta(Y_n(u))a_\beta(Y_n(v))]<0.
\end{aligned}
\]
The series is absolutely convergent, and every individual term is strictly negative. In particular,
\[
\Pr(U_\beta<u,V_\beta<v)
\le\frac{u(v-\beta)+a_\beta(u)a_\beta(v)}{\beta(1-\beta)}
<\frac{u(v-\beta)}{\beta(1-\beta)}.
\]
As one concrete, exact consequence, at \(\beta=1/2\), \(u=1/4\), \(v=3/4\), the joint probability is at most \(247/1024<1/4\). In the skew product with a Lebesgue-uniform doubling-map base, the three expected vertical attraction-basin lengths (for 0, \(\beta\), 1) are, respectively, \(\beta/2\), \(1/2\), and \((1-\beta)/2\). The separator covariance is strictly negative.

## Assumptions and scope
The signs are independent with probability \(1/2\) each, independent of the deterministic initial fiber height. The probability space may equivalently be the itinerary space of the Lebesgue-preserving doubling map \(x\mapsto2x\pmod1\); dyadic coding ambiguity lies in a null set. The parameter \(\beta\) is any fixed real number in \((0,1)\), and all fiber maps use this same parameter. The assertions of almost-sure global partition and threshold distributions concern the randomness of the base itinerary, not random fiber updates with independent signs at different starting heights. The statements at threshold initial conditions are deliberately left unspecified.

## Proof
**1. Order preservation and trapping.** The derivative
\[
a_\beta'(y)=-3y^2+2(1+\beta)y-\beta
\]
is concave with endpoint values \(-\beta\) and \(\beta-1\), both greater than \(-1\), and maximum \((1-\beta+\beta^2)/3<1\). Thus \(\lvert a_\beta'(y)\rvert<1\) on \([0,1]\), so both \(g_+\) and \(g_-\) are increasing homeomorphisms. They fix precisely \(0,\beta,1\) and preserve both open strips \((0,\beta)\) and \((\beta,1)\). Two trajectories with the same driving sequence preserve their strict ordering at every finite time.

**2. Endpoint selection at each fixed height.** For a fixed initial height \(y\), independence of the fair sign and the past yields \(\mathbb E[Y_{n+1}(y)\mid\mathcal F_n]=Y_n(y)\). This bounded martingale converges almost surely and in \(L^2\) to \(Y_\infty(y)\). The exact conditional quadratic-variation identity is
\[
\mathbb E[Y_{n+1}(y)^2-Y_n(y)^2\mid\mathcal F_n]=a_\beta(Y_n(y))^2.
\]
Summing expectations gives \(\sum_{n\ge0}\mathbb E[a_\beta(Y_n(y))^2]\le1\); hence \(\sum_n a_\beta(Y_n(y))^2<\infty\) almost surely. Continuity now forces \(a_\beta(Y_\infty(y))=0\). For \(y\in(0,\beta)\), the limit is in \(\{0,\beta\}\); for \(y\in(\beta,1)\), it is in \(\{\beta,1\}\). Taking expectations of the martingale limit gives
\[
\Pr(Y_\infty(y)=\beta)=y/\beta\quad (0<y<\beta),\qquad
\Pr(Y_\infty(y)=1)=(y-\beta)/(1-\beta)\quad(\beta<y<1).
\]

**3. A simultaneous, almost-sure global partition.** Intersect the probability-one convergence events for all rational initial heights in the two open strips. Because every composition of the increasing fiber maps preserves order, the rational heights converging to 0 form a lower initial segment of \((0,\beta)\), and those converging to 1 form an upper terminal segment of \((\beta,1)\). Define \(U_\beta\) as the cut between the rational heights selecting 0 and \(\beta\); define \(V_\beta\) as the cut between the rational heights selecting \(\beta\) and 1. For any real \(y\) strictly on one side of its cut, choose two rational heights between \(y\) and that cut or the relevant endpoint. Monotonicity squeezes \(Y_n(y)\) between trajectories converging to the same endpoint. This proves the displayed partition **simultaneously for all real initial heights other than the two cuts**, not merely separately for each prescribed height.

For \(0<t<\beta\), the event \(U_\beta<t\) is the union over rational \(r<t\) of the event \(Y_\infty(r)=\beta\). By the nested rational events and Step 2, its probability is \(\sup_{r<t}r/\beta=t/\beta\). Similarly \(\Pr(V_\beta<t)=(t-\beta)/(1-\beta)\) for \(\beta<t<1\). In particular the cuts lie strictly in their respective strips almost surely and have no atoms. Their means imply \(\mathbb E U_\beta=\beta/2\) and \(\mathbb E V_\beta=(1+\beta)/2\), giving the exact expected basin lengths.

**4. Negative dependence, with an exact deficit.** Couple the lower and upper initial heights \(u<\beta<v\) by the same signs, and write \(X_n=Y_n(u)\), \(Z_n=Y_n(v)\). Their product has the conditional drift
\[
\mathbb E[X_{n+1}Z_{n+1}-X_nZ_n\mid\mathcal F_n]=a_\beta(X_n)a_\beta(Z_n).
\]
For every finite time \(X_n\in(0,\beta)\), \(Z_n\in(\beta,1)\), so this drift is **strictly negative**. The individual quadratic-variation sums in Step 2 and Cauchy–Schwarz give the absolute convergence estimate
\[
\sum_{n\ge0}\mathbb E|a_\beta(X_n)a_\beta(Z_n)|
\le\left(\sum_n\mathbb E a_\beta(X_n)^2\right)^{1/2}
\left(\sum_n\mathbb E a_\beta(Z_n)^2\right)^{1/2}<\infty.
\]
Telescope in expectation and take the bounded limit. The partition and atomless cuts give
\[
X_\infty=\beta\mathbf1_{\{U_\beta<u\}},\quad
Z_\infty=\beta+(1-\beta)\mathbf1_{\{V_\beta<v\}}
\]
almost surely. Therefore
\[
\beta(1-\beta)\Pr(U_\beta<u,V_\beta<v)-u(v-\beta)
=\sum_{n\ge0}\mathbb E[a_\beta(X_n)a_\beta(Z_n)].
\]
The first summand is \(a_\beta(u)a_\beta(v)<0\) and every later summand is negative, giving the strict formula and bound. Integrating the strictly negative quadrant-covariance defect over both marginal coordinates also yields \(\operatorname{Cov}(U_\beta,V_\beta)<0\).

## Verification
The accompanying standalone `verify_basins.py` uses exact rational arithmetic and exhaustively evaluates all sign words through length four for three distinct interior parameters. It verifies conditional product and square-increment identities, martingale means, strict opposite-strip signs, and the explicit \(247/1024\) bound. The checker produces 101 exact finite-depth identity checks. The almost-sure and infinite-series assertions are established analytically by Steps 1–4, not by these finite tests. Reproduce with `python verify_basins.py` from the directory containing this file and the checker.

## Relationship to prior work
Rabiee, Ghane, Zaj and Karimi introduced this exact cubic-fiber example as Equation (5) in their 2021 preprint and proved intermingled attraction basins on its diagonal parameter locus (Theorem 14). Gharaei and Homburg previously established the qualitative random separating-graph theorem (Theorem 3.1), which the former authors apply to the two invariant fiber intervals. The present claim is the explicit uniform law of **both** separators, their exact joint covariance-deficit series, and strict negative dependence across all lower/upper height pairs. These quantitative statements do not follow by mere renaming of the qualitative two-basin theorem, and neither inspected primary text states them. The exact uniform marginals use the special complementary identity \(g_+(y)+g_-(y)=2y\), which need not hold for general random interval diffeomorphisms.

## Limitations
This result assumes independent fair branch itineraries and identical cubic parameters in the two branches; it does not claim the same uniform marginals for biased branching, asymmetric parameters, or correlated driving. No characterization is given of the trajectories beginning exactly at either separating graph. Strict negative quadrant dependence does not determine the entire joint copula numerically; the displayed series is exact but not evaluated in elementary closed form. Previously unindexed equivalent statements remain a possible priority risk, and independent mathematical review has not been performed.

## References
- M. Rabiee, F. H. Ghane, M. Zaj, S. Karimi, *The Occurrence of Riddled Basins and Blowout Bifurcations in a Parametric Nonlinear System*, arXiv:2103.03308v1 (first public version 2021-03-04), especially Eq. (5), Theorems 11 and 14; https://arxiv.org/pdf/2103.03308.
- M. Gharaei, A. J. Homburg, *Random Interval Diffeomorphisms*, arXiv:1611.07248v1 (2016-11-22), especially Theorem 3.1; https://arxiv.org/pdf/1611.07248.
