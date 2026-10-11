# Singular half-grid selection and exponentially weak attraction in rational EOS maps

## Finding

Fix coprime integers \(1\le k<n\), \(n\ge2\), and consider the Euler–Osipov–Söderbacka (EOS) family
\[
F_a(x)=x+\frac{k}{n}-\frac{1}{1+e^{-ax}},\qquad a>0.
\]
For all sufficiently large \(a\) there is a unique attracting orbit of primitive period \(n\). Put \(\epsilon_a=e^{-a/(2n)}\), \(J=\{k-n,k-n+1,\ldots,k-1\}\), and define a permutation of \(J\) by
\[
\tau(j)=\begin{cases}j+k,&j<0,\\j+k-n,&j\ge0.\end{cases}
\]
Since \(\gcd(k,n)=1\), \(\tau\) is an \(n\)-cycle. Define \(s_{-1}=1/2\) and, on one complete traversal, propagate
\[
s_{\tau(j)}-s_j=-\mathbf 1_{\{j=-1\}}+\mathbf 1_{\{j=0\}}.
\]
Equivalently, \(s_j=-1/2\) exactly on the forward \(\tau\)-arc starting immediately after \(-1\) and ending at \(0\), and \(s_j=1/2\) on its complement. The attracting orbit contains exactly one point \(x_{a,j}\) for every \(j\in J\), with uniform-in-\(j\), fixed-\(k,n\) expansion
\[
\boxed{x_{a,j}=\frac{j+1/2}{n}+s_j\epsilon_a+O_{n,k}(a\epsilon_a^2).}
\]
Its full-period multiplier is
\[
\boxed{\Lambda_a=(F_a^n)'(x_{a,j})=1-2a\epsilon_a+O_{n,k}(a^2\epsilon_a^2).}
\]
In particular, the orbit becomes asymptotically *neutral*, although it is attracting for every sufficiently large finite \(a\); the reciprocal full-return contraction gap obeys
\[
\boxed{(1-\Lambda_a)^{-1}\sim\frac{e^{a/(2n)}}{2a}.}
\]
The leading contraction coefficient depends on the rotation denominator \(n\), but **not** its coprime numerator \(k\). The first-order *spatial* correction remembers \(k\) through the cyclic permutation \(\tau\).

## Assumptions and scope

The limit is \(a\to+\infty\) with \(n,k\) fixed. The statements concern the real EOS map on its attracting interval \([k/n-1,k/n]\), its attracting primitive \(n\)-cycle, and the derivative of its \(n\)-th return map. The asymptotic constants implicit in \(O_{n,k}\) are not asserted to be uniform in an increasing denominator. The multiplier is independent of the selected point of this orbit by the chain rule.

## Proof

Write \(g_a(x)=(1+e^{-ax})^{-1}\) and introduce the discontinuous rotation representative \(G(x)=x+k/n-\mathbf 1_{\{x>0\}}\). For nonzero \(x\),
\[
e_a(x):=F_a(x)-G(x)=\begin{cases}-g_a(x),&x<0,\\1-g_a(x),&x>0.\end{cases}
\]
Thus \(e_a(x)\) has sign opposite to \(x\) and \(|e_a(x)|\le e^{-a|x|}\). The reference half-grid is \(p_j=(j+1/2)/n\) for \(j\in J\). It lies a distance at least \(h=1/(2n)\) from the discontinuity, and \(G(p_j)=p_{\tau(j)}\).

**1. Existence close to the half-grid.** Let \(\epsilon=e^{-ah}\), \(\eta=\sqrt\epsilon\), and start a trajectory at \(p_0+t=h+t\) with \(|t|\le\eta\). For all sufficiently large \(a\), \(a\eta\to0\) and induction over the fixed number \(n\) of steps shows that its itinerary is exactly the permutation \(\tau\): the visited point labeled \(j\) equals \(p_j+t+O_{n,k}(\epsilon)\), uniformly in \(|t|\le\eta\). Indeed each discrepancy from the rotation step is bounded by \(C\epsilon e^{a\eta}\), and no point approaches zero closer than \(h-\eta-O(\epsilon)\).

After \(n\) steps the integer branch corrections cancel because exactly \(k\) of the \(p_j\) are positive. The return displacement is therefore the sum of the individual \(e_a\) terms. The two closest sites \(j=-1,0\) contribute respectively \(-\epsilon e^{at}\) and \(+\epsilon e^{-at}\), up to \(O_{n,k}(a\epsilon^2+\epsilon^3)\); all other sites, at distance at least \(3h\), contribute \(O_{n,k}(\epsilon^3)\). Uniformly for \(|t|\le\eta\),
\[
F_a^n(h+t)-(h+t)=\epsilon(e^{-at}-e^{at})+O_{n,k}(a\epsilon^2+\epsilon^3).
\]
At \(t=-\eta\) this is positive and at \(t=+\eta\) negative: \(a\epsilon\eta\gg a\epsilon^2+\epsilon^3\). There is a fixed point between them. On this branch all derivatives \(F_a'(x)=1-a g_a(x)(1-g_a(x))\) are strictly between zero and one when \(a\) is large, so the return map is strictly increasing with derivative less than one and this fixed point is unique within the indicated neighborhood. Its itinerary visits all \(n\) distinct labels and thus has primitive period exactly \(n\).

**2. Location of the phase.** Label the orbit by the sites \(J\) and set \(\delta_j=x_{a,j}-p_j\). The first step gives \(\delta_j=t+O_{n,k}(\epsilon)\), where initially \(|t|\le\eta\). Summing the \(n\) periodic orbit equations yields \(\sum_{j\in J}e_a(x_{a,j})=0\). Every term except those with \(j=-1,0\) has magnitude \(O_{n,k}(\epsilon^3)\), whence
\[
|g_a(x_{a,-1})-g_a(-x_{a,0})|\le C_{n,k}\epsilon^3.
\]
Here the equality \(g_a(-x)=1-g_a(x)\) is essential. By the mean-value theorem, since both arguments belong to \(-h+[-\eta-O(\epsilon),\eta+O(\epsilon)]\), the derivative \(g_a'\) between them is bounded below by \(c a\epsilon\) for large \(a\). Consequently
\[
x_{a,-1}+x_{a,0}=\delta_{-1}+\delta_0=O_{n,k}(\epsilon^2/a).
\]
Together with \(\delta_{-1}=t+O(\epsilon)\) and \(\delta_0=t\), this implies \(t=O_{n,k}(\epsilon)\), so all \(\delta_j=O_{n,k}(\epsilon)\).

**3. First-order orbit profile.** With this improved location, the exact recurrence is
\[
\delta_{\tau(j)}-\delta_j=e_a(x_{a,j})=
\begin{cases}-\epsilon+O_{n,k}(a\epsilon^2),&j=-1,\\+\epsilon+O_{n,k}(a\epsilon^2),&j=0,\\O_{n,k}(\epsilon^3),&j\notin\{-1,0\}.
\end{cases}
\]
Following the \(\tau\)-arc from \(-1\) to \(0\) and using \(\delta_{-1}+\delta_0=O(\epsilon^2/a)\) gives \(\delta_{-1}=+\epsilon/2+O(a\epsilon^2)\), \(\delta_0=-\epsilon/2+O(a\epsilon^2)\). Propagating around the entire orbit gives \(\delta_j=s_j\epsilon+O_{n,k}(a\epsilon^2)\), as claimed.

**4. Multiplier.** The logistic derivative satisfies \(g_a'(x)=a g_a(x)(1-g_a(x))\). At the two nearest points \(j=-1,0\), the factor \(a g_a(x_{a,j})(1-g_a(x_{a,j}))\) equals \(a\epsilon+O_{n,k}(a^2\epsilon^2)\); at every other point it is \(O_{n,k}(a\epsilon^3)\). Multiplication of the \(n\) derivative factors proves \(\Lambda_a=1-2a\epsilon+O_{n,k}(a^2\epsilon^2)\) and the reciprocal-gap limit.

**5. Identifying the attracting orbit.** The constructed orbit has an open attracting basin. Theorem 3.3 of Bielawski et al. proves that for fixed rational \(k/n\) and sufficiently large \(a\) an attracting period-\(n\) orbit attracts Lebesgue-almost every real initial point. Two disjoint attracting periodic orbits cannot coexist with that almost-everywhere attraction, because each has an open positive-measure basin. Hence the constructed orbit is that orbit and is the unique attracting periodic orbit of the map.

## Verification

The companion `check_eos.py` uses high-precision decimal arithmetic to construct the orbit by Newton iteration on the \(n\)-step return equation, verify every itinerary label and periodic residual, compare \((x_{a,j}-p_j)/\epsilon_a\) with the exact sign profile \(s_j\), and compare \((1-\Lambda_a)/(2a\epsilon_a)\) with one. It checks \((n,k)=(2,1),(3,1),(5,2),(7,3),(11,4)\) at \(a=24n\). These are finite consistency tests only; the proof above establishes the infinite claims.

## Relationship to prior work

Bielawski, Chotibut, Falniowski, Misiurewicz and Piliouras [1] prove existence and almost-everywhere attraction of a rational-rotation-type \(n\)-cycle for sufficiently steep EOS maps. Their Section 5 explains approximate independence of the numerator using a piecewise-rotation surrogate; it explicitly does not give quantitative estimates. The new statement determines the selected half-grid, all first-order point displacements, and the sharp limiting contraction gap \(2a e^{-a/(2n)}\). In particular it quantifies the increasing *slowness* of attraction, which does not follow from mere existence of an attracting cycle. Chotibut et al. [2] prove symmetric-period-two attraction and broader dynamical properties in the original game-theory parametrization, without the present general-denominator profile or contraction asymptotic.

## Limitations

Nothing here gives a uniform error estimate as \(n\to\infty\), an explicit smallest admissible \(a\), a global mixing or basin-entry time, or a classification of repelling higher-period cycles. Reciprocal multiplier gap measures local asymptotic contraction of a full return near the attracting cycle; it is not a uniform hitting-time bound for arbitrary initial points. The bound \(O_{n,k}(a\epsilon_a^2)\) is intentionally not claimed optimal beyond first order. Prior literature on related singularly smoothed rotations could contain equivalent formulas; comparisons in the accompanying review give the inspected scope.

## References

[1] J. Bielawski, T. Chotibut, F. Falniowski, M. Misiurewicz, G. Piliouras, *Interval maps mimicking circle rotations*, arXiv:2411.01495v1 (first public version November 3, 2024), Sections 2–5. https://arxiv.org/html/2411.01495v1 ; journal version DOI 10.1016/j.cnsns.2025.108963.

[2] T. Chotibut, F. Falniowski, M. Misiurewicz, G. Piliouras, *Family of chaotic maps from game theory*, arXiv:1807.06831v1 (2018), Sections 2–3. https://arxiv.org/html/1807.06831v1 ; DOI 10.1080/14689367.2020.1795624.
