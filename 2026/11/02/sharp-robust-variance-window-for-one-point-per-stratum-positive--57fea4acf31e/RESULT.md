# Sharp robust variance window for one-point-per-stratum positive quadratic quadrature

## Finding

Fix an integer \(m\ge3\). Partition the unit interval into closed equal strata and select one, otherwise arbitrary, node from each:
\[
I_j=\left[\frac{j-1}{m},\frac jm\right],\qquad x_j\in I_j,\qquad 1\le j\le m.
\]
For a probability measure \(\mu\) with first moment \(1/2\) and variance \(v\in(0,1/4)\), consider strict-positive polynomial exactness
\[
w_j>0,\quad\sum_{j=1}^m w_j=1,\quad\sum_{j=1}^m w_jx_j=\frac12,\quad\sum_{j=1}^m w_jx_j^2=\frac14+v.
\]
The above equations admit weights for **every** admissible selection of the nodes, including allowed bin-boundary collisions, precisely when
\[
\boxed{\alpha_m<v<\beta_m},\qquad
\alpha_m=\begin{cases}\dfrac1{m^2}&m\text{ even},\\[2pt]\dfrac3{4m^2}&m\text{ odd},\end{cases}\qquad
\beta_m=\frac{(m-2)^2}{4m^2}.
\]
The admissible variance interval is empty at \(m=3,4\), and the case \(m=2\) admits no positive variance for all node choices. For the uniform target law, \(v=1/12\), the smallest universally sufficient stratum count is exactly \(m=5\): the sharp interval at five is \((3/100,9/100)\). In particular this is a **certainty under arbitrary stratified node positions**, not an independent-sampling high-probability assertion.

## Assumptions and scope

The strata are closed and share endpoints, which may produce duplicate nodes. Weights are attached to all \(m\) labelled samples and must all be strictly positive, although weights for coincident nodes can be combined for the moment calculation. The target probability measure need not be uniform: its first two moments alone matter. The conclusion asserts existence after the sample positions are known; it does not require equal weights, a uniformly lower-bounded weight, or exactness above polynomial degree two. The permitted primary classification is MSC2020 \(65D32\).

## Proof

**1. Exact moment-polytope vertical section.** For fixed ordered sample positions \(x_1\le\cdots\le x_m\), write \(c=1/2\). For \(m\ge3\), the first node is at most \(1/m<c\) and the last at least \((m-1)/m>c\). Let \(x_i\le c\le x_{i+1}\) be consecutive nodes straddling \(c\); when a node equals \(c\), take the corresponding zero-variance boundary. A probability distribution supported on the nodes and having mean \(c\) has variance in the closed interval \([L,U]\), where
\[
L=(c-x_i)(x_{i+1}-c),\qquad
U=(c-x_1)(x_m-c).
\]
To establish the upper bound, integrate \((X-x_1)(x_m-X)\ge0\) to obtain \(\operatorname{Var}(X)\le(c-x_1)(x_m-c)\); mixing the two endpoints attains equality. For the lower bound, the polygonal interpolation of the strictly convex parabola \(t\mapsto t^2\) through the ordered distinct nodes forms the lower boundary of the convex hull of the moment points \((x_j,x_j^2)\). At mean \(c\) its boundary segment is the chord joining the adjacent bracketing nodes, whose variance is \((c-x_i)(x_{i+1}-c)\). Equivalently, any nonconsecutive two-point law bracketing \(c\) has no smaller variance, and every feasible moment vector is a convex combination of such laws.

For \(m\ge5\) there are at least three distinct nodes, even allowing adjacent bin-boundary collisions. Hence the moment polygon is two-dimensional. Since \(x_1<c<x_m\), every moment point with \(L<v<U\) is in its relative (indeed ordinary) interior. Every point in the interior of the convex hull of finitely many points has a convex representation with **all coefficients strictly positive**: first average all generating points using a small common positive coefficient, then represent the remaining perturbed interior target by a nonnegative convex combination. Conversely, any all-positive representation cannot lie on a supporting boundary line if some generating node is strictly off that line. Thus the strict inequalities are sufficient and, for the sharp witness choices below, necessary.

**2. Worst upper endpoint.** The first and last strata give \(x_1\le1/m\) and \(x_m\ge(m-1)/m\). Therefore
\[
U\ge\left(\frac12-\frac1m\right)^2=\beta_m.
\]
Equality is attained by choosing the first and last nodes at their inward-facing endpoints, and the other nodes at their bin midpoints. For \(m\ge5\), there are interior nodes strictly between those endpoints. Therefore if \(v\ge\beta_m\), the equality witness cannot support strictly positive moment-exact weights.

**3. Worst lower endpoint and parity.** If \(m=2k\) is even, the central pair satisfies
\[
x_k\in[c-1/m,c],\qquad x_{k+1}\in[c,c+1/m].
\]
The adjacent-chord variance is thus at most \(1/m^2\). This is attained with \(x_k=(k-1)/m\) and \(x_{k+1}=(k+1)/m\), taking every other node at its bin midpoint. If \(m=2k+1\) is odd, its central node lies in \([c-1/(2m),c+1/(2m)]\). If it lies below \(c\), the next node is at most \(c+3/(2m)\); if above, the preceding node is at least \(c-3/(2m)\). In either case the straddling adjacent-chord variance is at most \(3/(4m^2)\), with equality achieved by setting the central node at the left endpoint of its bin and its right neighbour at the right endpoint of the following bin (and taking the remaining nodes at bin midpoints). This proves \(\sup L=\alpha_m\). For \(m\ge5\), the selected witnesses contain sample positions strictly off the bounding chord. Thus \(v\le\alpha_m\) cannot have all weights strictly positive for every selection.

Combining steps 1–3 gives the if-and-only-if interval for \(m\ge5\). For \(m=3,4\), the sharp upper and lower witnesses separately imply \(\alpha_m\ge\beta_m\), so no variance meets all selections. At \(m=2\), choose both nodes at the shared midpoint \(c\), which forces zero variance. This settles every integer \(m\ge2\).

**4. Uniform threshold.** The uniform measure on \([0,1]\) has mean \(c\) and variance \(1/12\). At \(m=5\),
\[
\frac3{100}<\frac1{12}<\frac9{100},
\]
so every five-stratum sample set permits all-positive exact quadratic weights. At \(m=4\), take \(x_1=1/4\), \(x_4=3/4\) and arbitrary interior points in their strata; the upper achievable variance at mean \(c\) is \(1/16<1/12\). Counts two and three also fail by the classification, proving sharpness.

## Verification

The standalone standard-library checker `verify.py` tests, with exact rational arithmetic, all sharp boundary witnesses for \(3\le m\le150\), every endpoint-corner choice for \(3\le m\le10\), and 21,000 pseudorandom rational interior node selections. It additionally constructs all-strict-positive exact-rational weights for 120 admissible sets and independently checks their three moments. The output reports 2,040 endpoint cases and the exact five-stratum uniform witness. These computations are supplementary; the quantification over all integer sizes and all real node positions follows from the preceding analytical inequalities and convex hull argument, not from enumeration.

## Relationship to prior work

Neumayer–Schäfer–Ullrich [1], first public on October 23, 2026, prove positive exact quadrature for sufficiently numerous independent random nodes with high probability, supported by \(L_1\) discretization and a Lewis-density sampling argument; their Theorem 1.1 also controls relative weights. The present result instead classifies exact degree-two universal feasibility for **adversarial** one-per-equal-stratum samples, with unbounded freedom to adapt positive weights. Its sharp parity-dependent variance window and five-stratum cutoff are not consequences of the paper's i.i.d. high-probability theorem.

Van den Bos–Sanderse–Bierbooms–van Bussel [2] provide positive nested quadrature methods based on arbitrary sample sets, including moment-matching/subsampling procedures. The supplied data-based method does not establish a universal deterministic selection guarantee for prescribed first two *population* moments under one sample from each equal stratum. Classical convex-hull/moment geometry is used here as a proof technique and is not claimed as novel. A potentially equivalent earlier specialized stratified-support theorem outside the inspected sources is a residual historical-priority risk.

## Limitations

The result is one-dimensional, degree-two, centered-mean, equal-stratum and unbounded-adaptive-weight specific. It does not guarantee higher-order exactness, near-equal weights, a uniform positive lower bound on weights, independent random sampling guarantees, or a rate of quadrature error for nonsmooth functions. The mathematical proof is self-contained, but external independent validation has not been performed. Completeness of the historical literature search is not asserted.

## References

[1] S. Neumayer, M. Schäfer and T. Ullrich, *Random nodes with positive weights: Richter–Tchakaloff rules and optimal positive quadrature*, arXiv:2610.32699v1, first public October 23, 2026. https://arxiv.org/html/2610.32699v1

[2] L. M. M. van den Bos, B. Sanderse, W. A. A. M. Bierbooms and G. J. W. van Bussel, *Generating nested quadrature rules with positive weights based on arbitrary sample sets*, arXiv:1809.09842v1 (2018). https://arxiv.org/abs/1809.09842
