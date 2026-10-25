# A sharp disk-to-annulus transition in farthest-pair geodesic statistics

## Finding

Let \(A_{r,R}=\{x\in\mathbb R^2:r\leq\lVert x\rVert\leq R\}\), with \(0\leq r<R\), carry the **intrinsic length metric** (the shortest length of a rectifiable curve constrained to remain in \(A_{r,R}\)). Let \(X,Y\) be independent uniform-area points of this region, let \(D=d_{A_{r,R}}(X,Y)\), and set \(K=R^2-r^2\). The following are parts of one endpoint-and-reconstruction theorem.

**Exact diameter and inverse reconstruction.** The distance support has endpoint
\[
M(r,R)=2\sqrt K+2r\arctan\left(\frac r{\sqrt K}\right),
\]
including \(M(0,R)=2R\). The short-distance law satisfies
\[
\lim_{t\downarrow0}\frac{\Pr(D\leq t)}{t^2}=\frac1K.
\]
Together these two observable quantities uniquely determine both radii: after recovering \(K\), the right side defining \(M\) is strictly increasing with \(r\geq0\), and \(R=\sqrt{K+r^2}\).

**Fixed positive hole.** For every fixed \(0<r<R\),
\[
\Pr(D>M(r,R)-\varepsilon)
\sim\frac{2R^4}{3\pi rK^3}\varepsilon^3
\quad(\varepsilon\downarrow0).
\]
If \(\rho=\lVert X\rVert\), \(\sigma=\lVert Y\rVert\) and \(\theta\in[0,\pi]\) is their minor angular separation, then, conditional on the same upper-tail event, the vector
\[
\left(\frac{\sqrt K(R-\rho)}{R\varepsilon},
\frac{\sqrt K(R-\sigma)}{R\varepsilon},
\frac{r(\pi-\theta)}{\varepsilon}\right)
\]
converges in distribution to the uniform probability measure (density \(6\)) on \(\{(x,y,z)\in\mathbb R_{\ge0}^3:x+y+z<1\}\).

**Disk and sharp vanishing-hole crossover.** At \(r=0\),
\[
\Pr(D>2R-\varepsilon)\sim\frac{32}{15\pi R^{5/2}}\varepsilon^{5/2}.
\]
Fix \(R>0\) and \(a\geq0\). For \(\varepsilon>0\) small enough, take \(r_\varepsilon=a\sqrt{R\varepsilon}\), \(M_\varepsilon=M(r_\varepsilon,R)\), and define
\[
F_a(z)=\begin{cases}az,&0\leq z\leq2a,\\a^2+z^2/4,&z\geq2a,\end{cases}\qquad
J(a)=\begin{cases}
\dfrac4{15}\bigl(4(1-a^2)^{5/2}+5a^3-4a^5\bigr),&0\leq a\leq1/\sqrt2,\\
\dfrac1{3a},&a\geq1/\sqrt2.
\end{cases}
\]
(The formulas for \(J\) agree at their shared endpoint.) Then
\[
\boxed{\lim_{\varepsilon\downarrow0}\frac{\Pr(D>M_\varepsilon-\varepsilon)}{\varepsilon^{5/2}}
=\frac2{\pi R^{5/2}}J(a).}
\]
Conditioned on this upper-tail event, the marked defects
\[
\left(\frac{R-\rho}{\varepsilon},\frac{R-\sigma}{\varepsilon},
\sqrt{\frac R\varepsilon}(\pi-\theta)\right)
\]
converge to the probability density \(2/J(a)\) on \(\{x,y,z\geq0:x+y+F_a(z)<1\}\), zero elsewhere. The threshold \(a=1/\sqrt2\) is exactly where the straight-chord contribution vanishes from the limiting event. This is a limiting theorem at fixed \(a\), not a uniform error estimate when \(a\) grows with \(\varepsilon^{-1}\).

## Assumptions and scope

All radii are real with \(0\leq r<R<\infty\). Probability is normalized two-dimensional Lebesgue area, not uniform boundary arclength; the distance is intrinsic, not the ambient Euclidean chord. Statements for a fixed positive hole keep \(r,R\) fixed as \(\varepsilon\to0\); the crossover keeps \(R,a\) fixed while the hole shrinks. Boundary points have zero sampling probability, but belong to the closed annulus for intrinsic paths. All distributional limits concern ordinary bounded continuous test functions of the displayed variables; strict versus non-strict distance events are immaterial at the limiting scales.

## Proof

**1. Exact shortest-path geometry and diameter.** For \(r>0\), write the endpoint radii as \(\rho,\sigma\in[r,R]\) and the minor angular separation as \(\theta\in[0,\pi]\). Let \(\alpha(t)=\arccos(r/t)\) and \(g(t)=\sqrt{t^2-r^2}-r\alpha(t)\). A shortest path has the straight-chord form when the segment misses the inner disk, and otherwise consists of two tangent segments and the shorter intervening inner-circle arc. In the obstructed angular range \(\theta\geq\alpha(\rho)+\alpha(\sigma)\), the exact length is
\[
d=g(\rho)+g(\sigma)+r\theta.
\]
In the other angular range it is the Euclidean chord \(\sqrt{\rho^2+\sigma^2-2\rho\sigma\cos\theta}\). These branches agree at tangency. Each branch increases with \(\theta\) on its relevant range. Thus \(d(\rho,\sigma,\theta)\leq d(\rho,\sigma,\pi)=g(\rho)+g(\sigma)+\pi r\). Since \(g'(t)=\sqrt{t^2-r^2}/t>0\) for \(t>r\), its unique maximal endpoint radii are \(\rho=\sigma=R\), proving the asserted diameter. As \(\alpha(R)=\arctan(\sqrt K/r)\), the identity \(\pi-2\alpha(R)=2\arctan(r/\sqrt K)\) yields the displayed form. For \(r=0\) the Euclidean disk gives diameter \(2R\).

**2. Small distances and global injectivity.** At an interior point more than \(t\) from the boundary, its intrinsic radius-\(t\) ball has area \(\pi t^2\); boundary strips of width \(t\) have area \(O(t)\), and a ball has area at most \(\pi t^2\) (intrinsic distance dominates Euclidean distance). Averaging gives \(\Pr(D\leq t)=\pi t^2/(\pi K)+O(t^3)=t^2/K+O(t^3)\). Keeping \(K\) fixed, differentiation of \(M=2\sqrt K+2r\arctan(r/\sqrt K)\) with respect to \(r\) gives
\[
\frac{\partial M}{\partial r}=2\arctan\!\frac r{\sqrt K}+\frac{2r\sqrt K}{K+r^2}>0\quad(r>0).
\]
This proves full-radius reconstruction including the disk endpoint.

**3. Positive-hole upper tail and its marks.** Fix \(r>0\), and put \(c=g'(R)=\sqrt K/R\). For \(\rho,\sigma\to R\) and \(\theta\to\pi\), the detour branch applies, and
\[
M-d=c(R-\rho)+c(R-\sigma)+r(\pi-\theta)
+O((R-\rho)^2+(R-\sigma)^2).
\]
Maximizing geometry from step 1 and strict increase away from the maximizing set force these three defects to be \(O(\varepsilon)\) under \(d>M-\varepsilon\). The independent radial densities are \(2\rho/K\) and \(2\sigma/K\), while \(\theta\) is uniform on \([0,\pi]\). In scaled variables \(x=c(R-\rho)/\varepsilon\), \(y=c(R-\sigma)/\varepsilon\), \(z=r(\pi-\theta)/\varepsilon\), the probability Jacobian tends to
\[
\frac{4R^2}{\pi K^2c^2r}\varepsilon^3\,dx\,dy\,dz.
\]
The limiting event is the unit three-simplex, of volume \(1/6\). Consequently the leading coefficient is \(2R^4/(3\pi rK^3)\), and normalizing the same Lebesgue integral establishes the marked uniform law.

**4. Simultaneous hole closure.** Fix \(R>0\) and \(a\geq0\), and put \(r=a\sqrt{R\varepsilon}\). The diameter has the expansion
\[
M=2R+\frac{r^2}{R}+O(r^4/R^3)=2R+a^2\varepsilon+O(\varepsilon^2).
\]
For near-diametral pairs use \(\rho=R-\varepsilon x\), \(\sigma=R-\varepsilon y\), \(\theta=\pi-\sqrt{\varepsilon/R}\,z\). The chord-to-detour switching angle obeys
\[
\pi-\alpha(\rho)-\alpha(\sigma)=2a\sqrt{\varepsilon/R}+O(\varepsilon^{3/2}),
\]
for bounded \(x,y\). The tangent-arc formula therefore yields \((M-d)/\varepsilon=x+y+az+o(1)\) on \(z<2a\), whereas the unobstructed chord formula yields \((M-d)/\varepsilon=x+y+a^2+z^2/4+o(1)\) on \(z>2a\). The formulas match at \(z=2a\). These expansions are uniform on every compact set of nonnegative \(x,y,z\). They also provide tightness: away from the outer-antipodal maximizing configurations the gap is uniformly positive, and near them the positive radial and angular defect bounds restrict the scaled upper-tail event to a fixed compact region (for each fixed \(a\)). Thus dominated convergence applies.

The joint polar probability measure transforms to
\[
\frac4{\pi R^{5/2}}\varepsilon^{5/2}(1+o(1))\,dx\,dy\,dz.
\]
Integrating \(x+y+F_a(z)<1\) over \(x,y\) gives the cross-sectional area \(\tfrac12[1-F_a(z)]_+^2\). Hence the coefficient is \(2J(a)/(\pi R^{5/2})\), with
\[
J(a)=\int_0^\infty[1-F_a(z)]_+^2\,dz.
\]
For \(a\geq1/\sqrt2\), only \(0<z<1/a\) contributes, and direct integration gives \(1/(3a)\). For \(0\leq a\leq1/\sqrt2\), splitting at \(2a\) and at \(2\sqrt{1-a^2}\) yields
\[
\int_0^{2a}(1-az)^2dz+
\int_{2a}^{2\sqrt{1-a^2}}(1-a^2-z^2/4)^2dz
=\frac4{15}\bigl(4(1-a^2)^{5/2}+5a^3-4a^5\bigr).
\]
The same integration, divided by the limiting total mass, proves the marked limiting density \(2/J(a)\). In particular \(J(0)=16/15\), giving the disk coefficient \(32/(15\pi R^{5/2})\).

## Verification

The supplementary `verify_annulus.py` evaluates upper-tail probabilities directly using high-order Gauss–Legendre quadrature of the **exact angular threshold** at given endpoint radii. It compares these non-asymptotic probabilities to both limiting formulas for several hole sizes and small deficits. Eighteen numerical test cases passed their stated relative-error tolerances, including both sides of the crossover threshold, the disk, and thick annuli. SymPy independently verified the piecewise integral identity for \(J(a)\). These are finite numerical/algebraic diagnostics; neither they nor any numerical extrapolation supplies the proof of an asymptotic theorem. The geometric reductions and dominated-convergence argument above supply the infinite statements.

## Relationship to prior work

Geometric shortest paths avoiding a circular disk, composed of tangent segments and circular boundary arcs, are established background (Chang–Choi–Kwon–Park–Yap, 2005). Sheng (1985) studies probability laws and moments of **ambient Euclidean chord distances** in plane regions including concentric circular regions, not shortest paths avoiding a hole. Bäsel (first public preprint 2012-08-30) likewise treats Euclidean distances between uniformly random points in triangles. Blumberg–Gal–Mandell–Pancia (first public preprint 2012-06-20) develop metric-measure statistical invariants and include an annulus experiment with its **subspace Euclidean metric**; their object is persistent homology and empirical distances, not these exact obstacle-avoiding upper-tail laws. The assessed contribution is the explicit fixed-hole cubic endpoint, the marked critical \(r\asymp\sqrt{R\varepsilon}\) crossover and its closed coefficient, and the resulting global annulus recovery using the small-distance coefficient and diameter. These are claim-level distinctions, not title-level novelty evidence.

## Limitations

The crossover is proved for fixed \(a\), not uniformly for \(a\to\infty\); it does not by itself justify interchanging the fixed-hole and vanishing-hole limits. The numerical checker uses quadrature and does not certify its numerical integration errors rigorously. No claim is made for nonconcentric holes, multiple obstacles, nonuniform sampling, or higher-dimensional shells. Sheng's older full manuscript was not inspected; its accessible abstract explicitly defines ambient Euclidean chord distance, and historical specialist literature could still contain an equivalent geodesic-tail statement.

## References

1. E.-C. Chang, S. W. Choi, D. Kwon, H. Park, and C. K. Yap, *Shortest Path amidst Disc Obstacles is Computable*, Proceedings of the 21st Annual Symposium on Computational Geometry, 2005, full text: https://cs.nyu.edu/exact/doc/computable.pdf.
2. T. K. Sheng, *The distance between two random points in plane regions*, Advances in Applied Probability **17** (1985), 748–773, DOI: https://doi.org/10.2307/1427086. The accessible abstract specifies ambient distance.
3. A. J. Blumberg, I. Gal, M. A. Mandell, and M. Pancia, *Robust statistics, hypothesis testing, and confidence intervals for persistent homology on metric measure spaces*, arXiv:1206.4581, first posted 2012-06-20, https://arxiv.org/abs/1206.4581; §7 discusses an annulus with its Euclidean subspace metric.
4. U. Bäsel, *The distribution function of the distance between two random points in a right-angled triangle*, arXiv:1208.6228, first posted 2012-08-30, https://arxiv.org/abs/1208.6228.
