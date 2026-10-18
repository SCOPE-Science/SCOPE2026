# Two-scale volume asymptotics for length-three theta-graph Lipschitz balls

## Finding

Let \(\Theta_m^{(3)}\), for an integer \(m\ge 3\), be the finite simple graph with two distinguished vertices \(a,b\) connected by \(m\) internally vertex-disjoint paths, each consisting of three unit edges \(a-u_i-v_i-b\). The vertices are equipped with the shortest-path metric. Let \(Q_m\) be the unit ball of the real Banach space \(\operatorname{Lip}_0(V(\Theta_m^{(3)}))\), with potentials anchored by \(f(a)=0\), and let \(V_m\) be its Lebesgue volume in coordinates \((f(b),f(u_1),f(v_1),\ldots,f(u_m),f(v_m))\). The dimension is \(2m+1\).

**Theorem.** For every integer \(m\ge3\), the exact volume is
\[
V_m=2\int_0^1(3-h^2)^m\,dh+\frac{2^{m+2}}{2m+1}
=2\sum_{j=0}^{m}\frac{(-1)^j\binom mj3^{m-j}}{2j+1}+\frac{2^{m+2}}{2m+1}.
\]
It is also the \(m\)-th moment of a positive density supported on \((0,3)\):
\[
V_m=\int_0^3 x^m w(x)\,dx,\qquad
w(x)=\begin{cases}\sqrt{2/x},&0<x<2,\\(3-x)^{-1/2},&2<x<3.\end{cases}
\]
The same integral formula extends to \(m=0,1,2\), with the auxiliary value \(V_0=6\). For all integers \(m\ge0\),
\[
V_mV_{m+2}>V_{m+1}^{\,2},\qquad
\frac{V_{m+1}}{V_m}<3,
\]
and the consecutive ratios increase strictly to \(3\).

More sharply, put \(B_m=3^{m+1/2}\operatorname{B}(m+1,\tfrac12)=3^m\sqrt{3\pi}\,\Gamma(m+1)/\Gamma(m+\tfrac32)\). Then
\[
V_m-B_m=\int_0^2x^m\left(\sqrt{2/x}-(3-x)^{-1/2}\right)dx>0,
\]
and the **second exponential scale** has the sharp coefficient
\[
V_m-B_m=\frac{3\,2^m}{(m+1)(m+2)}+O\!\left(\frac{2^m}{m^3}\right)
\quad(m\to\infty).
\]
In particular,
\[
V_m=3^m\sqrt{\frac{3\pi}{m}}\left(1-\frac{3}{8m}+O(m^{-2})\right),\qquad
\frac{V_{m+1}}{V_m}=3\frac{m+1}{m+3/2}+O\!\left((2/3)^m m^{-3/2}\right).
\]
The leading Gaussian scale and the exponentially smaller correction have different geometric origins: potentials close to equal at the two poles versus the change in the cross-sectional polynomial at pole difference \(1\).

## Assumptions and scope

All edges have length one and all potential values are real. The shortest-path metric enforces the edge Lipschitz inequalities, and conversely the edge inequalities enforce every pairwise metric inequality. Write \(h=f(b)\), \(r_i=f(u_i)\), and \(s_i=f(v_i)\). Thus
\[
Q_m=\left\{(h,r_1,s_1,\ldots,r_m,s_m):
|r_i|\le1,\ |r_i-s_i|\le1,\ |s_i-h|\le1\ \text{for each }i\right\}.
\]
The volume convention is the ordinary coordinate volume after fixing one potential at zero. A change of anchored vertex acts by an integer determinant-one (up to sign) linear map, so this volume does not depend on which vertex is anchored. It is **not** a Euclidean volume in an arbitrarily rescaled orthonormal quotient basis.

The case \(m=2\) is a six-cycle and is not presented as a new cycle-volume calculation; \(m=1\) is a path. The asserted new infinite-family statement concerns \(m\ge3\).

## Proof

**1. Exact cross-sectional area.** For a fixed pole difference \(h\), the \(m\) arm-coordinate pairs are independent and share the same feasible planar area
\[
A(h)=\iint_{\mathbb R^2}\mathbf{1}_{[-1,1]}(r)\mathbf{1}_{[-1,1]}(s-r)\mathbf{1}_{[-1,1]}(h-s)\,dr\,ds.
\]
This is the three-fold convolution of the indicator of \([-1,1]\), evaluated at \(h\). Convolution or direct intersections of three unit-width slabs give
\[
A(h)=\begin{cases}
3-h^2,&|h|\le1,\\
(3-|h|)^2/2,&1\le|h|\le3,\\
0,&|h|\ge3.
\end{cases}
\]
For example, a length-three chain has total unconstrained edge-increment volume \(2^3=8\), and \(\int_{-3}^3 A(h)dh=8\), checking the Jacobian. Fubini's theorem now gives \(V_m=\int_{-3}^3 A(h)^m dh\). Splitting at \(|h|=1\), integrating the outer quadratic piece, and expanding the inner binomial establish both exact expressions in the theorem.

**2. The moment density and strict inequalities.** On \(h\ge0\), \(A(h)\) decreases from \(3\) to \(2\) on \([0,1]\) and from \(2\) to \(0\) on \([1,3]\). Push forward \(dh\) under \(h\mapsto A(h)\), doubling for negative \(h\). The first branch contributes density \(1/\sqrt{3-x}\) on \((2,3)\); the second contributes \(\sqrt{2/x}\) on \((0,2)\). Both are integrable and strictly positive on their indicated intervals. The auxiliary zeroth moment is \(\int_0^3w(x)dx=6\).

The Cauchy--Schwarz inequality applied to \(x^{m/2}\) and \(x^{(m+2)/2}\) in this positive measure yields \(V_{m+1}^2\le V_mV_{m+2}\). Equality would require \(x\) to be almost surely constant, impossible for this strictly positive continuous-spectrum density; hence the inequality is strict. The ratios therefore rise strictly. Each \(V_{m+1}/V_m\) is a strict weighted mean of \(x\in(0,3)\), so it is below \(3\). Positivity of the measure arbitrarily close to \(3\) ensures that the ratios tend to \(3\): for every \(\varepsilon>0\), the moments are eventually dominated by \(x\in(3-\varepsilon,3)\).

**3. Exact beta comparison.** The beta integral gives
\[
B_m=\int_0^3 x^m(3-x)^{-1/2}\,dx=3^{m+1/2}\operatorname{B}(m+1,\tfrac12).
\]
Subtracting this integral from the moment representation yields the exact stated formula for \(V_m-B_m\). Its integrand is positive on \((0,2)\), since \(2(3-x)>x\) there. Thus no cancellation or unproved sign approximation is used.

**4. Sharp smaller exponential scale.** Substitute \(s=2-x\). As \(s\downarrow0\), elementary Taylor expansion gives
\[
\sqrt{\frac{2}{2-s}}-\frac1{\sqrt{1+s}}=\frac34s+O(s^2).
\]
The measure away from \(x=2\) contributes an exponentially smaller quantity than \(2^m/m^3\), because it is integrable and bounded by \((2-\varepsilon)^m\) there. In a fixed neighborhood of \(x=2\), integrating the Taylor remainder is bounded by a constant multiple of
\[
\int_0^2(2-s)^m s^2\,ds=\frac{2^{m+4}}{(m+1)(m+2)(m+3)}.
\]
The linear term integrates exactly:
\[
\frac34\int_0^2(2-s)^m s\,ds
=\frac{3\,2^m}{(m+1)(m+2)}.
\]
Together these give \(V_m-B_m=3\,2^m/((m+1)(m+2))+O(2^m/m^3)\), proving the claimed second scale.

**5. Main asymptotic and ratio.** The classical gamma-ratio expansion gives
\[
\frac{\Gamma(m+1)}{\Gamma(m+3/2)}
=m^{-1/2}\left(1-\frac{3}{8m}+O(m^{-2})\right).
\]
Since the exact remainder is only \(O(2^m/m^2)\), this establishes the displayed leading expansion. Moreover \(B_{m+1}/B_m=3(m+1)/(m+3/2)\). The relative remainder \((V_m-B_m)/B_m\) is \(O((2/3)^m m^{-3/2})\), which yields the displayed ratio estimate.

## Verification

The standalone standard-library program `artifacts/verify.py` independently counts integer graph-Lipschitz potentials at every nonnegative integral dilation needed for the Ehrhart leading coefficient. It never evaluates the analytic cross-sectional integral in the counting routine. The graph incidence system has a totally unimodular constraint matrix; hence its integer dilates have an Ehrhart polynomial of degree \(2m+1\), whose leading coefficient is \(V_m\). The program recovers that coefficient by the exact \((2m+1)\)-st finite difference divided by \((2m+1)!\), then compares it with the explicit formula using rational arithmetic.

The exact checks passed for \(m=1,2,3,4,5,6,7\), with values
\[
8,\quad \frac{88}{5},\quad \frac{1536}{35},\quad
\frac{12128}{105},\quad \frac{72320}{231},\quad
\frac{865152}{1001},\quad \frac{1727488}{715}.
\]
Nineteen finite strict-log-convexity comparisons and twenty finite upper-ratio comparisons also passed. The infinite-domain claims follow from the proof above, not from finite experiments. To replay: run `python3 artifacts/verify.py` from the extracted finding directory.

## Relationship to prior work

The dual-ball normalization and geometry are those of finite-dimensional Lipschitz-free spaces and their Lipschitz duals, as treated by Alexander, Fradelizi, García-Lirola and Zvavitch (arXiv:1911.10642, Section 5). That paper establishes general volume-product results and, in particular, an equilateral-volume computation; it does not provide this theta-graph volume sequence or the secondary exponential term. The geometric framework of Aliaga (arXiv:2102.01219, Theorem 1) concerns extreme molecules and gives a distinct invariant. Ostrovska and Ostrovskii (arXiv:2112.02689, Sections 1--3) develop the graph/transportation representation and cycle-roadmap structure, not volume moments.

The known six-cycle case \(m=2\), general graph-metric facet enumerations, and complete-bipartite (two-edge-arm) cases are not being claimed independently. A record concerning these same length-three theta graphs supplies their Vietoris--Rips persistence and symmetry, rather than the anchored Lipschitz-dual volume. A separate related record concerns facets of a *mixed* theta graph with an additional length-two arm. These are different quantities and in the latter case a different graph. This comparison does not establish mathematical novelty in every unindexed source; see the limitations below.

## Limitations

The result concerns exactly the unit-edge, equal-arm length-three theta family in finite real Lipschitz dual spaces. It does not compute the primal volume, Mahler product, individual face numbers, or arbitrary weighted-arm graph volumes. No claim of independent external verification is made. The comparison against recorded and accessible literature cannot exclude an equivalent unpublished or differently indexed formula, or an unexamined general theorem that implies the special formula.

## References

1. M. Alexander, M. Fradelizi, L. C. García-Lirola and A. Zvavitch, *Geometry and volume product of finite dimensional Lipschitz-free spaces*, arXiv:1911.10642 (first public 2019-11-24), Section 5, especially the complete-graph dual-volume computation.
2. R. J. Aliaga, *Extreme points in Lipschitz-free spaces over compact metric spaces*, arXiv:2102.01219 (first public 2021-02-01), Theorem 1; primary 2020 MSC 46B20.
3. S. Ostrovska and M. I. Ostrovskii, *Isometric structure of transportation cost spaces on finite metric spaces*, arXiv:2112.02689 (first public 2021-12-05), canonical-graph definitions and Theorem 1.9.
