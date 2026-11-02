# Two distance moments reconstruct a lollipop metric graph with sharp square-root stability

## Finding
Let \(G(a,b)\) be a compact intrinsic metric graph obtained by joining one point of a circle of circumference \(a>0\) to one endpoint of a line segment of length \(b>0\). Its total arclength \(L=a+b\) is assumed known. Choose \(X,Y\) independently according to normalized arclength on \(G(a,b)\), and put \(D=d_G(X,Y)\), \(t=a/L\), \(\mu=\mathbb E[D]/L\), and \(\nu=\mathbb E[D^2]/L^2\).

**Theorem.** For every \(a,b>0\),
\[
\mu=\frac{5t^3-6t^2+4}{12},\qquad
\nu=\frac{-t^4+6t^3-6t^2+2}{12}.
\]
The ordered pair \((\mu,\nu)\), together with \(L\), determines \(a,b\) uniquely. Explicitly, the contrast
\[
H=\nu-\frac45\mu
=-\frac{5t^4-10t^3+6t^2+6}{60}
\]
is a strictly decreasing bijection from \(0<t<1\) onto \((-7/60,-1/10)\), so its unique inverse gives \(a=Lt\), \(b=L(1-t)\).

The mean alone has the sharp range \(17/75\le\mu<1/3\). It has exactly two distinct positive-shape preimages for every \(17/75<\mu<1/4\), and exactly one for every other feasible mean. Its unique minimum is attained at \(a:b=4:1\).

For any two such graphs with the *same* total length, write \((t_i,\mu_i,\nu_i)\) for their normalized parameters. They obey
\[
|t_1-t_2|\le
\sqrt{160\left(\left|\nu_1-\nu_2\right|+\frac45\left|\mu_1-\mu_2\right|\right)}.
\]
The exponent \(1/2\) is optimal for a uniform inverse bound over all \(0<t<1\); on each fixed subfamily \(t\ge\delta>0\), the inverse is Lipschitz.

## Assumptions and scope
The graph has **one** intrinsic circle and **one** pendant segment, with both lengths strictly positive. Points are sampled with density constant with respect to the combined arclength (not uniformly among constituent edges, and not by choosing vertices). The distance is the shortest-path distance along the metric graph, never an ambient Euclidean chord distance. The total arclength \(L\) is known externally and is the same in the stability comparison. No statement is made for arbitrary unicyclic graphs, more pendant edges, unknown total length, or random finite-sample moments.

The complete admissible normalized-moment locus is the curve \(\{(\mu(t),\nu(t)):0<t<1\}\). To test exact data, solve the strictly monotone contrast equation for its unique \(t\in(0,1)\) and check that each of the two observed moments equals the displayed polynomial at that \(t\); merely placing \(H\) in the stated open interval is necessary but not sufficient.

## Proof
**1. Conditional distance laws.** A point lies on the loop with probability \(a/L\) and on the pendant segment with probability \(b/L\). For two points on the segment, \(D\) is the absolute difference of two independent uniforms on \([0,b]\), so the conditional first and second moments are \(b/3\) and \(b^2/6\). For two points on the loop, their intrinsic circular distance is uniform on \([0,a/2]\), so the moments are \(a/4\) and \(a^2/12\). For one point on each part, the distance is \(U+V\), where \(U\) is uniform on \([0,b]\), \(V\) is uniform on \([0,a/2]\), and they are independent. The corresponding moments are \(b/2+a/4\) and \(b^2/3+ab/4+a^2/12\). The three unordered cases have respective probabilities \(b^2/L^2\), \(a^2/L^2\), and \(2ab/L^2\). Weighted averaging gives
\[
\begin{aligned}
\mathbb E[D]&=\frac{b^3}{3L^2}+\frac{a^3}{4L^2}+\frac{2ab}{L^2}\left(\frac b2+\frac a4\right),\\
\mathbb E[D^2]&=\frac{b^4}{6L^2}+\frac{a^4}{12L^2}+\frac{2ab}{L^2}\left(\frac{b^2}3+\frac{ab}4+\frac{a^2}{12}\right).
\end{aligned}
\]
Substitute \(a=Lt\), \(b=L(1-t)\) and simplify to obtain the two polynomial formulas in the theorem.

**2. Two-moment injectivity.** Direct algebra gives the stated expression for \(H(t)\) and
\[
H'(t)=-\frac{t}{30}\left(10t^2-15t+6\right),\qquad
10t^2-15t+6=10\left(t-\frac34\right)^2+\frac38.
\]
Therefore \(H'(t)<0\) for every \(t>0\), and the endpoint limits are \(H(0)=-1/10\) and \(H(1)=-7/60\). This proves bijectivity onto the asserted open interval and recovers both lengths from known \(L\).

**3. Exact ambiguity of the first moment.** Differentiate:
\[
\mu'(t)=\frac{t(5t-4)}4.
\]
Thus \(\mu\) decreases strictly on \((0,4/5)\) and increases strictly on \((4/5,1)\), with \(\mu(0)=1/3\), \(\mu(1)=1/4\), and \(\mu(4/5)=17/75\). Counting intersections with horizontal levels proves the range and all multiplicities. In particular, the distinct ratios
\[
t_1=\frac35,\qquad t_2=\frac{3+3\sqrt5}{10}
\]
both lie strictly between zero and one and satisfy \(\mu(t_1)=\mu(t_2)=73/300\), while \(\nu(t_1)=629/7500\) and \(\nu(t_2)=(1123+27\sqrt5)/15000\) differ. Thus a second moment is actually necessary for identification from these first moments.

**4. Global inverse stability and sharp exponent.** For \(0\le t<s\le1\), the completed-square identity above implies
\[
H(t)-H(s)
=\int_t^s\frac{r(10r^2-15r+6)}{30}\,dr
\ge\frac{s^2-t^2}{160}
\ge\frac{(s-t)^2}{160}.
\]
The triangle inequality for contrasts yields the stated square-root inverse estimate. If \(t,s\ge\delta>0\), the same integral is at least \(\delta(s-t)/80\), proving the sharper local Lipschitz estimate
\[
|t-s|\le\frac{80}{\delta}|H(t)-H(s)|.
\]
For optimality, compare \(t=\varepsilon\) and \(s=2\varepsilon\) with \(\varepsilon\downarrow0\): both normalized moment differences are \(O(\varepsilon^2)\), while \(|s-t|=\varepsilon\). An inverse Hölder exponent larger than \(1/2\), with a constant valid for every positive ratio, would imply \(\varepsilon\le C\varepsilon^{2\beta}\) for some \(\beta>1/2\) and arbitrarily small \(\varepsilon\), a contradiction.

## Verification
The accompanying `verify.py` (standard-library Python 3) independently computes the conditional geometric moments, compares them as exact fractions against the expanded polynomials at 199 rational ratios, verifies 7,260 exact pairwise inverse inequalities, integrates the two-point distance on a grid independent of the conditional formulas, checks a seeded sample-based implementation of shortest-path distance, and checks the mean-collision and small-circle asymptotics. It prints `VERIFY_OK 22414 checks: exact identities, sharp inequalities, independent integration, seeded simulation` when successful. These finite checks are supplementary: the proof above establishes the universal statements.

## Relationship to prior work
Doyle and Graver (1982) introduced mean distance for one-dimensional shapes, including several network classes; their paper is relevant to forward means but its full text was not available for direct comparison here. Dey, Shi, and Wang (first arXiv version 25 March 2015) compare metric graphs through persistence distortion rather than through moments of random pair distances. Wei, Walteros, and Batta (2019) supply general formulas for arbitrary forward network-distance moments and distributions; the moment *calculation itself* is therefore not asserted to be novel. Garijo, Márquez, and Silveira (2023) develop the computation of forward continuous mean distance for fixed weighted graphs. The retained contribution is the **complete fixed-total-length two-moment inverse** on the one-loop/one-tail class, the exact one-moment ambiguity interval, and the optimal global inverse-conditioning exponent. These conclusions are not supplied merely by a forward formula, which does not establish injectivity, fiber sizes, or optimal stability. A complete historical priority guarantee is not claimed.

## Limitations
Knowledge of \(L\) is an explicit hypothesis: without it the two raw moments also carry an unknown overall scale, and no claim of their sufficiency is made. The inverse estimate concerns exact population moments; it is not a finite-sample confidence bound. The graph family is topologically fixed to one loop and one pendant interval. The inverse is poorly conditioned near collapse of the loop, which is why the best uniform exponent is \(1/2\). Historical novelty remains provisional; an older equivalent inverse deduction in inaccessible literature cannot be ruled out.

## References
- J. K. Doyle and J. E. Graver, *Mean distance for shapes*, Journal of Graph Theory **6** (1982), 453–471, DOI: 10.1002/jgt.3190060410.
- T. K. Dey, D. Shi, and Y. Wang, *Comparing Graphs via Persistence Distortion*, arXiv:1503.07414, first publicly submitted 2015-03-25; SoCG 2015, DOI: 10.4230/LIPIcs.SOCG.2015.491.
- N. Wei, J. L. Walteros, and R. Batta, *On the Distance Between Random Events on a Network*, Networks **75** (2020), 203–231, first published online 2019, DOI: 10.1002/net.21919.
- E. Garijo, A. Márquez, and M. Silveira, *Continuous Mean Distance of a Weighted Graph*, Results in Mathematics **78** (2023), DOI: 10.1007/s00025-023-01902-w.
