# Universal competing-diagonal diameter fluctuations of boundary-sampled near-rectangles

## Finding
Fix side lengths \(a,b>0\). For each integer \(n\ge3\), take a Euclidean parallelogram \(P_n\) with adjacent side lengths \(a,b\) and included angle \(0<\theta_n<\pi\). Draw \(n\) points independently and uniformly by arclength on \(\partial P_n\), and let \(M_n\) be the largest pairwise Euclidean distance. Define
\[
 d_0=\sqrt{a^2+b^2},\qquad d_n=\sqrt{a^2+b^2+2ab|\cos\theta_n|},\qquad T_n=\frac{nd_0}{2ab}(d_n-M_n).
\]
If \(n|\cos\theta_n|\to\tau\ge0\), then the exact limiting law is
\[
 T_n\Longrightarrow T_\tau=\min\{G_1,\tau+G_2\},\qquad G_1,G_2\ \text{independent with distribution }\operatorname{Gamma}(2,1).
\]
Here gamma is parameterized by **shape two and rate one**. Every fixed positive integer moment converges. The survival function and first two moments are
\[
 \Pr(T_\tau>t)=(1+t)e^{-t}(1+(t-\tau)_+)e^{-(t-\tau)_+},\qquad t\ge0,
\]
\[
 \mathbb ET_\tau=2-\frac{(\tau+3)e^{-\tau}}4,\qquad
 \mathbb ET_\tau^2=6-\frac{(2\tau^2+10\tau+15)e^{-\tau}}4.
\]
At an exact rectangle, \(T_0\) has mean \(5/4\), second moment \(9/4\), and variance \(11/16\). The crossover is universal: no aspect-ratio parameter appears in its law. If instead \(\theta_n\to\pi/2\) and \(n|\cos\theta_n|\to\infty\), the same \(T_n\) converges, with all positive integer moments, to \(\operatorname{Gamma}(2,1)\). In particular, the mean passes from \(5/4\) at the rectangular threshold toward \(2\) as the longer diagonal wins decisively.

## Assumptions and scope
The side lengths \(a,b\) are fixed positive real numbers; \(n\) varies; all samples are independent and arclength-uniform on the *entire* perimeter. The angle may approach a right angle from either side. The normalization subtracts the **true geometric diameter** \(d_n\), not the rectangular reference \(d_0\). The positive-part notation is \((x)_+=\max\{0,x\}\). The result concerns the Euclidean diameter of the sampled point set, equivalently the diameter of its convex hull. It does not assert a finite-sample gamma law.

## Proof
**1. Joint local point process.** Write the perimeter as \(L=2(a+b)\). At each of the four corners, parameterize the adjacent edges by increasing physical arclength \(s\ge0\) from that corner. Rescale by \(ns/L\). For any finite family of bounded disjoint intervals along these eight edge-rays, their sample counts have multinomial probabilities with cell masses equal to \(L/n\) times their rescaled lengths divided by \(L\). For any prescribed finite vector of counts, the elementary multinomial-to-Poisson limit therefore gives independent rate-one Poisson point processes on all eight rays. In particular, the two nearest rescaled arclengths at each corner converge jointly to independent unit-rate exponential random variables, and all eight limiting variables are independent. This direct triangular-array calculation remains valid because the side lengths are fixed and the four corner neighborhoods are disjoint for large \(n\); it does not require the angle to be fixed.

**2. Endpoint loss.** Put the adjacent vectors of \(P_n\) equal to \(u_n,v_n\). At \(\theta_n\to\pi/2\), a diagonal has length tending to \(d_0\). If a point at its endpoint moves a distance \(s\) along the incident side of length \(a\), its first-order loss of distance to the opposite vertex is \(as/d_0+o(s)\); moving distance \(s\) along the side of length \(b\) gives \(bs/d_0+o(s)\). The expansions are uniform for \(\theta_n\to\pi/2\), with remainder \(O(s^2+|\cos\theta_n|s)\). Let \(E_a,E_b\) denote the two independent unit exponentials on these rays. After multiplying distance losses by \(nd_0/(2ab)\), the smallest possible loss at one corner converges to
\[
 H=\min\left\{\frac{a+b}{b}E_a,\frac{a+b}{a}E_b\right\}.
\]
Its survival probability is
\[
 \Pr(H>t)=\exp\left(-t\frac{b}{a+b}-t\frac{a}{a+b}\right)=e^{-t}.
\]
This *rate cancellation* is responsible for aspect-ratio universality. The two endpoints of a diagonal are distinct corners, so their local losses add to an independent sum \(G\sim\operatorname{Gamma}(2,1)\). The two diagonals use disjoint pairs of corners, hence yield independent \(G_1,G_2\).

**3. Localization and maximum diameter.** At the limit rectangle, only the two pairs of diagonally opposite vertices realize the geometric diameter. By compactness, for every fixed sufficiently small corner-neighborhood radius \(\delta>0\), every other pair of points of the rectangle's boundary is separated from its diameter by a strictly positive amount. This gap persists for the near-right-angle \(P_n\). Since each corner receives sampled points within arclength \(O_{\Pr}(1/n)\), the sampled diameter is \(d_n-O_{\Pr}(1/n)\). It follows that, with probability tending to one, every maximizing pair lies within the \(\delta\)-neighborhoods of one of the two diagonal pairs. The positive linear directional coefficients from step 2 imply that, within such a pair of neighborhoods, any optimizer must have endpoint arclengths \(O_{\Pr}(1/n)\); otherwise the loss would exceed a feasible \(O_{\Pr}(1/n)\) competitor. Taylor's remainder is therefore \(o_{\Pr}(1/n)\). Optimizing separately at the two endpoints yields the sum of their corner losses plus \(o_{\Pr}(1)\) after normalization. The two diagonal candidates thus have independent limiting losses \(G_1,G_2\), before accounting for their different geometric lengths.

**4. Critical detuning.** The two geometric diagonal lengths satisfy
\[
 d_{+,n}=\sqrt{d_0^2+2ab\cos\theta_n},\qquad d_{-,n}=\sqrt{d_0^2-2ab\cos\theta_n}.
\]
Their absolute difference, expressed in the deficit normalization, is exactly
\[
 \frac{nd_0}{2ab}|d_{+,n}-d_{-,n}|=\frac{2nd_0|\cos\theta_n|}{d_{+,n}+d_{-,n}}\longrightarrow\tau.
\]
Subtracting the largest sampled distance from the longer geometric diagonal length and taking the better of the two corner-pair candidates gives
\[
 T_n\Longrightarrow\min\{G_1,\tau+G_2\}.
\]
The sign of \(\cos\theta_n\) merely interchanges the labels. If \(n|\cos\theta_n|\to\infty\) while \(\theta_n\to\pi/2\), the inferior diagonal incurs a divergent normalized gap; the same localization and tightness arguments leave only \(G_1\).

**5. Moment convergence.** Take the geometric longer diagonal with endpoints \(v,w\). Let \(A_{n,v}\) be the shortest boundary arclength from \(v\) to any sampled point; define \(A_{n,w}\) similarly. The triangle inequality gives the deterministic comparison \(0\le d_n-M_n\le A_{n,v}+A_{n,w}\). For any boundary vertex and \(0\le s\le L/2\), the two oriented boundary arcs of length \(s\) occupy total perimeter length \(2s\), and hence
\[
 \Pr(A_{n,v}>s)=\left(1-\frac{2s}{L}\right)^n\le\exp(-2ns/L).
\]
Therefore \(nA_{n,v}\) and \(nA_{n,w}\) have uniformly bounded moments of every order. The displayed deterministic comparison bounds \(T_n\) by a constant depending only on \(a,b\) times their sum. Thus all powers of \(T_n\) are uniformly integrable, establishing convergence of every fixed positive integer moment, both at finite detuning and in the diverging-detuning regime.

**6. Explicit limiting moments.** As each gamma survival is \((1+t)e^{-t}\), independence immediately gives the displayed product survival. Integrating \(\mathbb ET_\tau=\int_0^\infty\Pr(T_\tau>t)\,dt\) and \(\mathbb ET_\tau^2=2\int_0^\infty t\Pr(T_\tau>t)\,dt\), split at \(t=\tau\), yields the two formulas. At \(\tau=0\), these give \(5/4\), \(9/4\), and variance \(9/4-25/16=11/16\). This completes the proof.

## Verification
The accompanying standalone `verify.py` uses Python's standard library only. It independently checks the survival integral against the closed moment expressions at six detunings; checks the exact corner-rate cancellation for four different aspect ratios; confirms that per-edge extreme sample points yield the same exact diameter as all sampled pairs in 48 cases; checks the geometric detuning identity numerically; and compares five finite-sample simulations to the limiting means. Run `python3 verify.py`. The analytic local-process and compactness arguments, not the finite simulations, establish the infinite limiting law.

## Relationship to prior work
Reitzner, Schütt and Werner [1] study boundary-sampled random polytopes, emphasizing expected face counts and volume deficits; they do not state a sample-diameter law. Prochno, Schütt, Sonnleitner and Werner [2] prove sharp Hausdorff approximation results for boundary samples of polygons. Their joint local-Poisson-process method is a direct antecedent of proof step 1; the present work instead analyzes two competing **global diameter** pairs, proves a critical \(n|\cos\theta_n|\) crossover, and derives its gamma minima and full moments. The general uniform deviation results of Brunel [3] bound geometric functionals including diameter but do not provide this distribution or the near-rectangle detuning law. The formula is not a restatement of the maximum-of-corner-loss Hausdorff law: global sample diameter takes a minimum over two **sums of distinct-corner endpoint costs**. The literature-priority assessment is provisional and is not an independent certification.

## Limitations
The side lengths remain fixed while the angle tends to a right angle; no uniformity is claimed over degenerating aspect ratios. The samples are independent and arclength-uniform, and the statistic is the Euclidean diameter. The limit does not determine the exact finite-sample diameter distribution, other sampling measures, or arbitrary quadrilateral crossover behavior. Historical priority is provisional; a more general theorem concerning extreme interpoint distances for boundary-supported samples could subsume this statement despite the checked literature.

## References
[1] M. Reitzner, C. Schütt, E. M. Werner, *The convex hull of random points on the boundary of a simple polytope*, arXiv:1911.05917 (first publicly available 2019-11-14), https://arxiv.org/abs/1911.05917.

[2] J. Prochno, C. Schütt, M. Sonnleitner, E. M. Werner, *Random approximation of convex bodies in Hausdorff metric*, arXiv:2404.02870 (first publicly available 2024-04-03), https://arxiv.org/abs/2404.02870.

[3] V.-E. Brunel, *Uniform Behaviors of Random Polytopes under the Hausdorff Metric*, arXiv:1503.01504 (2015), https://arxiv.org/abs/1503.01504.
