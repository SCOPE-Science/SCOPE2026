# An attracting two-cycle disappears into a nonstationary ghost at a discontinuity

## Finding
Consider the power-map family of Lawnik, Moysis and Volos at any real exponent \(d\geq1\). In the explicit open contraction regime \(0<c<b/d^2\), varying the left endpoint parameter through \(a=b\) destroys **every invariant Borel probability measure** despite preserving bounded dynamics and uniform convergence of the maps. On the side \(b<a<1\), a unique globally attracting prime-two orbit supports the unique invariant probability. At \(a=b\), every orbit instead approaches the same non-invariant two-point set, and all empirical measures converge to the same **non-invariant** two-point probability. For \(d>1\), the disappearing cycle has a sharp power-law amplitude and a multiplier tending to zero rather than to one.

More precisely, fix \(d\geq1\) and \(0<c<b/d^2\) with \(b<1\), and for \(b\leq a<1\) define
\[
F_a(x)=\begin{cases}
1-(1-a)(1-x/b)^d,&0\leq x\leq b,\\
c((x-b)/(1-b))^d,&b<x\leq1.
\end{cases}
\]
For each \(a>b\) there are exactly two periodic points, \(\xi_a\in(0,b)\) and \(\eta_a\in(b,1)\), forming a prime-two orbit, and every orbit converges to it by parity. The unique invariant Borel probability is
\[
\mu_a=\tfrac12(\delta_{\xi_a}+\delta_{\eta_a}).
\]
At \(a=b\), there are no periodic points of any period and no invariant Borel probability, although every orbit has \(\omega\)-limit set \(\{0,b\}\), and for each initial point \(x\in[0,1]\),
\[
\frac1N\sum_{j=0}^{N-1}\delta_{F_b^j(x)}\ \xrightarrow[N\to\infty]{\mathrm{weak}}\ \nu=\tfrac12(\delta_0+\delta_b).
\]
Here \((F_b)_*\nu=\tfrac12(\delta_b+\delta_1)\ne\nu\), whereas \(\mu_a\Rightarrow\nu\) and \(\|F_a-F_b\|_\infty=a-b\) as \(a\downarrow b\).

For every \(d>1\), with \(\Delta=a-b\downarrow0\), the cycle and its two-step multiplier \(\rho_a\) have the sharp asymptotics
\[
\xi_a\sim\frac{c}{(1-b)^d}\Delta^d,\qquad
\eta_a-b\sim\Delta,\qquad
\rho_a\sim\frac{cd^2}{b}\left(\frac{\Delta}{1-b}\right)^{d-1}.
\]
For \(d=1\), the exact expressions instead are
\[
\xi_a=\frac{bc(a-b)}{b(1-b)-c(1-a)},\quad
\eta_a=a+\frac{1-a}{b}\xi_a,\quad
\rho_a=\frac{c(1-a)}{b(1-b)}\ \longrightarrow\ \frac cb.
\]

## Assumptions and scope
The phase space is the full compact interval \([0,1]\) with the branch convention that \(x=b\) belongs to the left branch. The exponent is an arbitrary real \(d\geq1\); the strict assumptions \(0<c<b/d^2\) and \(b\leq a<1\) ensure a common contracting two-step return map. Borel probability and weak convergence have their usual measure-theoretic meanings. The word “unique” quantifies over **all** invariant Borel probabilities, with no density, moment or ergodicity restriction. No assertion is made outside the displayed contraction regime.

## Proof
**1. Alternating branches and the contracting return.** Put
\[
P_a(x)=1-(1-a)(1-x/b)^d\quad(0\le x\le b),\qquad
Q(y)=c((y-b)/(1-b))^d\quad(b<y\le1).
\]
If \(a>b\), then \(P_a([0,b])=[a,1]\subset(b,1]\), and \(Q((b,1])=(0,c]\subset(0,b)\). Thus every orbit alternates branches immediately. The return on the closed left interval is
\[
G_a(x)=Q(P_a(x))=\frac{c}{(1-b)^d}\left[a-b+(1-a)\big(1-(1-x/b)^d\big)\right]^d.
\]
The chain rule, \(d\geq1\), and \(1-a\leq1-b\) give
\[
0\le G_a'(x)\le\frac{d(1-a)}b\frac{cd}{1-b}
\le\frac{cd^2}{b}=:\kappa<1
\]
(interpreting derivatives at endpoints one-sided). Since \(G_a([0,b])\subset(0,c]\), the contraction theorem gives exactly one fixed point \(\xi_a\in(0,b)\), and \(G_a^n(x)\to\xi_a\) geometrically for every \(x\in[0,b]\). Set \(\eta_a=P_a(\xi_a)\in(b,1)\); then \(Q(\eta_a)=\xi_a\). Any periodic point must alternate and therefore be a fixed point of \(G_a\) or its opposite-parity counterpart. Thus these are the only periodic points and the orbit has least period two. Every initial point in either branch converges to its appropriate parity of this cycle.

**2. All stationary probabilities above the boundary.** For any continuous \(\varphi:[0,1]\to\mathbb R\), the preceding parity convergence implies, for every starting point \(x\),
\[
\lim_{N\to\infty}\frac1N\sum_{j=0}^{N-1}\varphi(F_a^j(x))
=\tfrac12\big(\varphi(\xi_a)+\varphi(\eta_a)\big).
\]
If \(\sigma\) is an invariant Borel probability, integrate this identity using dominated convergence and invariance: \(\int\varphi\,d\sigma=\tfrac12[\varphi(\xi_a)+\varphi(\eta_a)]\). Continuous functions determine Borel probabilities on \([0,1]\), hence \(\sigma=\mu_a\). Its invariance follows directly from the two-cycle.

**3. The critical ghost.** When \(a=b\), for every \(x\in(0,b]\), one has \(P_b(x)>b\), so the true two-step return is given by the same formula \(G_b(x)=Q(P_b(x))\). It extends continuously to \([0,b]\) with \(G_b(0)=0\), and the derivative bound in step 1 shows \(0<G_b(x)\le\kappa x\) for \(x>0\). Consequently, a trajectory starting in \((0,b]\) has even iterates tending to \(0\) and odd iterates tending to \(P_b(0)=b\). Every starting point in \((b,1]\) enters \((0,c]\) after one step. The exceptional point \(0\) has the exact initial itinerary \(0\mapsto b\mapsto1\mapsto c\), and then enters \((0,b]\). Thus **every** orbit has the same alternating asymptotic pair \(\{0,b\}\). No orbit can be periodic: once it reaches positive left coordinates, its two-step coordinate strictly decreases toward zero; the exceptional zero point itself moves to \(b\ne0\).

For every continuous \(\varphi\), Cesàro averaging gives \(\frac1N\sum_{j<N}\varphi(F_b^j(x))\to[\varphi(0)+\varphi(b)]/2\) for all \(x\). If a Borel invariant probability \(\sigma\) existed, dominated convergence and stationarity would force \(\sigma=\nu\). But \(F_b(0)=b\), \(F_b(b)=1\), so \((F_b)_*\nu=(\delta_b+\delta_1)/2\ne\nu\). Contradiction. In particular, the compactness of the phase space does not imply existence of an invariant probability for this discontinuous map.

**4. Uniform perturbation, weak loss, and exponent.** Only the first branch depends on \(a\), and its difference is exactly \((a-b)(1-x/b)^d\). Thus \(\|F_a-F_b\|_\infty=a-b\). The fixed-point identity and the contraction inequality imply
\[
0<\xi_a\le\frac{G_a(0)}{1-\kappa}
=\frac{c}{(1-\kappa)(1-b)^d}(a-b)^d.
\]
Therefore \(\xi_a\to0\), \(\eta_a=P_a(\xi_a)\to b\), and \(\mu_a\Rightarrow\nu\). If \(d>1\), then \(\xi_a=o(a-b)\), whence \(P_a(\xi_a)-b=(a-b)(1+o(1))\). Substitution in \(G_a(\xi_a)=\xi_a\) yields the first two sharp asymptotics. Applying the chain rule at \((\xi_a,\eta_a)\) gives
\[
\rho_a=\frac{d(1-a)}b(1-\xi_a/b)^{d-1}
\frac{cd}{1-b}\left(\frac{\eta_a-b}{1-b}\right)^{d-1},
\]
so \(\rho_a\sim(cd^2/b)((a-b)/(1-b))^{d-1}\). For \(d=1\), \(G_a(x)=c(a-b)/(1-b)+c(1-a)x/[b(1-b)]\), which solves to the exact formulas displayed in the Finding.

## Verification
Every step above is analytic. A standalone `verify.py` uses rational arithmetic to recheck the affine case, boundary itinerary and contraction parameters, and tests the displayed nonlinear maps at representative rational points. These checks corroborate the formulas but are not substitutes for the quantified proof. A particularly transparent strictly piecewise-contracting example is \(b=3/4\), \(c=1/16\), \(d=2\): both individual branch Lipschitz constants are at most \(2/3\) and \(1/2\), while the critical system has no invariant Borel probability. Here the disappearing cycle satisfies \(\xi_a\sim(a-b)^2\) and \(\rho_a\sim4(a-b)/3\).

## Relationship to prior work
Lawnik, Moysis and Volos introduced the precise discontinuous power family and proved absence of **fixed points** for \(d\ge1\); their study does not state this all-period orbit census, loss of invariant probabilities, weak stationary-limit mechanism, or the exponent-dependent multiplier law. Kryzhevich's 2018 work already gives an elementary **different** discontinuous interval map without invariant probability, and identifies failure of classical compact-continuous invariant-measure arguments; the abstract absence phenomenon is **not claimed to be new**. Catsigeras, Guiraud, Meyroneinc and Ugalde developed the general concept of ghost orbits for piecewise contractions. Calderón, Catsigeras and Guiraud obtained a spectral decomposition under additional assumptions, including that branch endpoint images avoid forward discontinuity encounters; their relevant hypothesis fails here since \(P_b(0)=b\), the discontinuity. These papers provide context and partial structural parallels, not this parameterized theorem and quantitative cycle-collapse law. The recorded fractional-power fixed-point classification for \(0<d<1\) is disjoint from the present \(d\ge1\) result.

## Limitations
The condition \(cd^2<b\) is a transparent sufficient two-step contraction hypothesis, not a claimed necessary boundary. The theorem does not classify all dynamical behavior for larger \(c\), nor stochastic forcing or changes to the branch convention at \(b\). The nonstationarity phenomenon is known abstractly; the originality claim is only for this exact model's full measure bifurcation and sharp parameter-dependent asymptotics. An unindexed equivalent calculation may exist. There is no independent mathematical audit.

## References
1. M. Lawnik, L. Moysis, C. Volos, “A Family of 1D Chaotic Maps without Equilibria”, *Symmetry* 15 (2023), article 1311, equation (15), https://doi.org/10.3390/sym15071311 (first published 2023-06-27).
2. S. Kryzhevich, “Invariant measures for interval translations and some other piecewise continuous maps”, arXiv:1812.04534 (2018), especially Introduction, Example 0.1.
3. E. Catsigeras, P. Guiraud, A. Meyroneinc, E. Ugalde, “On the asymptotic properties of piecewise contracting maps”, *Dynamical Systems* 31 (2016), 107–135; arXiv:1108.1501, on ghost orbits.
4. A. Calderón, E. Catsigeras, P. Guiraud, “A spectral decomposition of the attractor of piecewise contracting maps of the interval”, *Ergodic Theory Dynam. Systems*, arXiv:1903.08591 (2019); note the endpoint-image hypothesis in their main theorem.
