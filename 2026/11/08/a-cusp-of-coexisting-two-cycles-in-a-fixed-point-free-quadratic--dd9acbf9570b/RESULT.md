# A cusp of coexisting two-cycles in a fixed-point-free quadratic interval map

## Finding

For the piecewise-quadratic interval family introduced by Lawnik, Moysis and Volos, the natural **strictly alternating regime** admits an exact global dynamical classification and an explicit saddle-node cusp. Write
\[
P_{a,b,c}(x)=\begin{cases}
1-(1-a)((b-x)/b)^2,&0\le x\le b,\\
c((x-b)/(1-b))^2,&b<x\le1,
\end{cases}
\]
where \(0<b<a<1\) and \(0<c<b\). Define \(q=(1-a)/(1-b)\in(0,1)\), \(k=c/b\in(0,1)\). Every orbit alternates between \([0,b]\) and \((b,1]\); every orbit converges, in its even and odd phases, to one of **at most three primitive two-cycles**, and there are no periodic orbits of any other period.

For \(q\le3/4\), there is exactly one two-cycle, except that at \(q=k=3/4\) its multiplier is one (it is still globally attracting). For \(q>3/4\), put
\[
\delta(q)=\sqrt{4-3/q},\qquad
u_\pm(q)=(2\pm\delta(q))/3,\qquad
K_\pm(q)=\frac{(4-3u_\pm(q))^2}{16(1-u_\pm(q))}.
\]
Here \(K_-(q)<K_+(q)\). There are **three** distinct two-cycles exactly when \(K_-(q)<k<K_+(q)\); there are **two** exactly when \(k\) equals one of these fold values and belongs to \((0,1)\); otherwise there is **one**. Whenever there are three, the outer cycles attract and the intermediate cycle repels, with exact basin separation at that intermediate cycle.

For \((a,b,c)=(3/5,1/2,2/5)\), equivalently \((q,k)=(4/5,4/5)\), the normalized left coordinates of the three two-cycles are
\[
t_-=(3-\sqrt5)/8,\qquad
t_0=(13-\sqrt{105})/8,\qquad
t_+=(3+\sqrt5)/8.
\]
The two outer cycles have return multiplier \(4/5\); the middle one has multiplier \((26-2\sqrt{105})/5>1\). In particular, this fixed-point-free system has two open attraction basins, not a single globally attracting cycle.

At the cusp \(q=k=3/4\), for every left starting coordinate \(t\ne1/3\), its normalized even-phase orbit obeys the sharp slowdown
\[
\lim_{n\to\infty}\sqrt n\,|t_n-1/3|=2/3.
\]

## Assumptions and scope

All maps are exact real maps on \([0,1]\), with the branch value at \(x=b\) belonging to the left branch. The parameter inequalities are strict: \(0<b<a<1\), \(0<c<b\), and the exponent is exactly \(d=2\). A primitive two-cycle means a pair of distinct points interchanged by the map; both points lie on opposite sides of \(b\). An attracting two-cycle here means asymptotic attraction of both subsequences, not eventual finite-time equality. The cusp limit uses \(t_0=x_0/b\) for \(x_0\in[0,b]\), and \(t_{n+1}=G(t_n)\) as defined below.

## Proof

**Exact return.** Since the left branch takes \([0,b]\) into \([a,1]\subset(b,1]\) and the right branch takes \((b,1]\) into \((0,c]\subset(0,b)\), the dynamics alternates strictly. Setting \(t=x/b\) on the left gives the two-step return
\[
G(t)=k[1-q(1-t)^2]^2,\quad 0\le t\le1.
\]
It satisfies \(G(0)=k(1-q)^2>0\), \(G(1)=k<1\), and
\[
G'(t)=4kq(1-t)[1-q(1-t)^2]\ge0,
\]
with strict increase for \(0\le t<1\). For any \(t\), if \(G(t)>t\), its successive iterates increase, and if \(G(t)<t\), they decrease. Bounded monotone convergence and continuity force convergence to a fixed point of \(G\). An increasing map has no cycles with least period greater than one, so \(P\) has only primitive two-cycles.

**Maximum count and folds.** Let \(H(t)=G(t)-t\). Since \(H(0)>0>H(1)\), at least one interior root exists. The derivative \(G'(t)\) is unimodal, because after \(u=1-t\), it is proportional to \(u(1-qu^2)\), whose derivative is \(1-3qu^2\). Therefore \(H'\) has at most two zeros, and Rolle's theorem bounds \(H\) to at most three distinct interior zeros. A multiple zero solves \(H=H'=0\). Writing \(u=1-t\) and eliminating \(k\) gives
\[
q\,u(4-3u)=1,\qquad
k=\frac{(4-3u)^2}{16(1-u)}.
\]
For \(q\in(0,1)\), the tangency equation has a solution \(u\in(0,1)\) exactly when \(q\ge3/4\). At equality \(u=2/3\), \(k=3/4\), and \(G(t)-t=(t-3)(3t-1)^3/64\), a triple root at \(t=1/3\). For \(q>3/4\) the two tangencies occur at \(u_\pm\). Their levels satisfy
\[
K_+(q)-K_-(q)=\frac{3\delta(q)^3}{8[1-\delta(q)^2]}>0.
\]
Because roots cannot cross \(t=0\) or \(t=1\) for \(k\in(0,1)\), and root count changes by two at each ordinary tangency, the claimed one/two/three-cycle phase diagram follows. Equivalently, for fixed \(q>3/4\) the lower fold creates two roots when \(k\) passes \(K_-\), and the upper fold destroys two if \(K_+<1\) is passed. At a strict three-root configuration, signs of \(H\) alternate, forcing the outer fixed points to have \(0\le G'<1\) and the middle to have \(G'>1\); monotonicity makes the middle point the exact boundary of the two attracting basins.

**Exact coexistence and basins.** For \(q=k=4/5\), one has
\[
G(t)-t=\frac{(4t^2-13t+4)(16t^2-12t+1)}{125}.
\]
Its fourth real root \((13+\sqrt{105})/8\) is greater than one; the other three roots and their multipliers are as stated above. For a left initial point \(x\in[0,b]\), let \(t=x/b\): convergence is to the lower cycle for \(t<t_0\), to the upper cycle for \(t>t_0\), and to the middle cycle if \(t=t_0\). For a right initial point \(x\in(b,1]\), use instead \(t=P(x)/b\); the same strict comparisons apply after this one step. In the rational example, the right-branch basin boundary is the unique point
\[
x_*=\frac12+\frac12\sqrt{\frac{5t_0}{4}}\in(1/2,1).
\]

**Critical slowdown.** At \(q=k=3/4\), the factorization above implies global monotone convergence to \(t_*=1/3\). Put \(e_n=t_n-t_*\). Near zero,
\[
e_{n+1}=e_n-\frac98e_n^3+O(e_n^4).
\]
No nonzero orbit can hit zero, by strict monotonicity of \(G\). Thus \(e_{n+1}^{-2}-e_n^{-2}=9/4+O(e_n)\to9/4\). Telescoping and Cesàro averaging give \(e_n^{-2}/n\to9/4\), hence the stated limit.

## Verification

The included `check.py` uses exact symbolic arithmetic to verify the two-iterate reduction's derivative, both fold identities, the triple-root and rational-example polynomial factorizations, the three exact multipliers, the fourth root's exclusion, and several additional rational parameter regimes using exact real-root counts. Run `python check.py` with SymPy installed. These checks support, but do not replace, the global calculus argument; no finite parameter grid certifies the continuum phase diagram.

## Relationship to prior work

Lawnik, Moysis and Volos introduced the piecewise power family and proved that its exponent-\(d\ge1\) branch has no fixed points. Their Section 4.1 supplies numerical phase diagrams and Lyapunov landscapes, but not the exact alternating-regime return map, three-cycle census, fold locus, global basins or cusp asymptotic derived here. Their follow-up with Baptista (2024) concerns a different piecewise map-generating transformation; its available abstract does not imply these precise formulas. A published result on the same source family with fractional exponents \(0<d<1\) concerns fixed points and does not subsume the exponent-two cycle statement. The general monotone-interval-map convergence principle is standard and not claimed as new. Specific quantitative classification is the assessed contribution.

## Limitations

This theorem is restricted to the strictly alternating parameter region and exponent two. It says nothing about other regions of the same family, where chaotic behavior is possible. At fold parameters, the neutral two-cycle can attract from only one side, so no assertion of hyperbolic attraction is made there. The result supplies no cryptographic security conclusion. Priority remains uncertain outside the inspected sources; the 2024 follow-up's accepted manuscript was linked in an institutional repository but was inaccessible in the inspected route, so its full text was not used for a noncoverage claim.

## References

1. M. Lawnik, L. Moysis and C. Volos, *A Family of 1D Chaotic Maps without Equilibria*, Symmetry **15** (2023), 1311, doi:10.3390/sym15071311. Public article: https://www.researchgate.net/publication/372001778_A_Family_of_1D_Chaotic_Maps_without_Equilibria . Earliest verified public date: 2023-06-27.
2. M. Lawnik, L. Moysis, M. S. Baptista and C. Volos, *Discrete one-dimensional piecewise chaotic systems without fixed points*, Nonlinear Dynamics **112** (2024), 6679–6693, doi:10.1007/s11071-024-09349-6. Abstract and accepted-manuscript listing: https://abdn.elsevierpure.com/en/publications/discrete-one-dimensional-piecewise-chaotic-systems-without-fixed-/ .
