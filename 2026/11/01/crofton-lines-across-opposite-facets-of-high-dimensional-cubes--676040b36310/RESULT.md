# Crofton lines across opposite facets of high-dimensional cubes

## Finding

Let \(d\ge 2\) be an integer and let \(Q_d=[0,1]^d\). Choose an unoriented affine line according to Euclidean-motion-invariant Crofton line measure, conditioned on intersecting \(Q_d\). Let \(B_d\) be the event that its two chord endpoints lie in the relative interiors of a pair of opposite facets, and let \(L_d\) be the chord length conditional on \(B_d\). Endpoints at lower-dimensional faces form a null event.

Set \(\mu=\sqrt{2/\pi}\) and define for \(x>0\)
\[
F(x)=\operatorname{erf}(x/\sqrt2)-\frac{\mu}{x}(1-e^{-x^2/2}).
\]
The **exact probability in every dimension** is
\[
\boxed{p_d:=\Pr(B_d)=\int_0^\infty x e^{-x^2/2}F(x)^{d-1}\,dx.}
\]
In particular \(p_2=\sqrt2-1\). With \(q_d=(\mu(d-1))^{1/3}\), the sharp stretched-exponential expansion is
\[
\boxed{p_d\sim\sqrt{\frac{2\pi}{3}}\,q_d\exp\!\left(-\frac{3q_d^2}{2}-\frac{\mu q_d}{2}-\frac{\mu^2}{6}\right),\qquad d\to\infty.}
\]
For the crossing-coordinate Gaussian amplitude \(X_d\) defined in the proof, the conditional fluctuation law is
\[
\boxed{X_d-q_d\ \Longrightarrow\ N(\mu/3,\,1/3),\quad\text{conditionally on }B_d.}
\]
The **conditional chord length** satisfies
\[
\boxed{\frac{L_d}{\sqrt d/q_d}\longrightarrow1\quad\text{in probability},\qquad d^{1/6}\!\left(L_d-\frac{\sqrt d}{q_d}\right)\Longrightarrow-\mu^{-2/3}Z,}
\]
where \(Z\sim N(\mu/3,1/3)\). Thus opposite-facet Crofton chords are much longer than typical axis-scale chords, but occur with probability \(\exp(-\Theta(d^{2/3}))\).

## Assumptions and scope

Crofton sampling means the unique (up to a factor) isometry-invariant measure on unoriented affine lines in \(\mathbb R^d\), conditioned on meeting \(Q_d\); it **does not** mean joining two independently sampled interior points, or picking two independently sampled face endpoints. Equivalently, choose a line direction with density proportional to the \((d-1)\)-dimensional orthogonal projection volume of the cube, then select a uniform offset in that projected region. The cube has side length one; for side length \(a\), the probability is unchanged and lengths scale by \(a\). All stated asymptotic limits hold along integer dimensions \(d\to\infty\). The Gaussian amplitude \(X_d\) is an auxiliary random variable defined by size-biasing one coordinate of a standard Gaussian direction; its exact conditional density is given below.

## Proof

**Step 1: Crofton flux and face-to-face event.** Fix a unit vector \(u\in S^{d-1}\), orient the line along \(u\), and consider the family of offsets in \(u^\perp\). The entering facet with outward normal \(-\operatorname{sgn}(u_i)e_i\) contributes projected measure \(|u_i|\); the cube's projected \((d-1)\)-volume is therefore \(\sum_i|u_i|\). Conditional on entering facet \(i\), the other \(d-1\) entry coordinates are independent \(\operatorname{Unif}[0,1]\). Traversal to the opposite \(i\)-facet requires parameter displacement \(1/|u_i|\), and for each \(j\ne i\) the admissible entry-coordinate fraction is \((1-|u_j|/|u_i|)_+\). Consequently
\[
p_d=\frac{\displaystyle\int_{S^{d-1}}\sum_{i=1}^d |u_i|\prod_{j\ne i}(1-|u_j|/|u_i|)_+\,d\sigma(u)}{\displaystyle\int_{S^{d-1}}\sum_{i=1}^d |u_i|\,d\sigma(u)}.
\]
These are disjoint events outside zero-measure ties. Both numerator and denominator are homogeneous of degree one in the nonzero vector \(u\). By polar decomposition of a standard Gaussian vector \(G=(G_1,\ldots,G_d)\), their ratio is the corresponding ratio of Gaussian expectations. Coordinate symmetry then yields
\[
p_d=\frac{\mathbb E\left[|G_1|\prod_{j=2}^d(1-|G_j|/|G_1|)_+\right]}{\mathbb E|G_1|}.
\]
Size-biasing the half-normal \(|G_1|\) by \(|G_1|/\mu\) gives the Rayleigh density \(x e^{-x^2/2}\,dx\). For independent \(N\sim N(0,1)\), integration gives
\[
\mathbb E(1-|N|/x)_+=\mu\int_0^x(1-y/x)e^{-y^2/2}\,dy=F(x).
\]
Conditioning on \(x\) proves the exact integral and the conditional amplitude density
\[
\boxed{\Pr(X_d\in dx\mid B_d)=\frac{x e^{-x^2/2}F(x)^{d-1}}{p_d}\,dx.}
\]
For \(d=2\), expressing the flux ratio using a single first-quadrant direction angle \(\theta\) gives
\[
p_2=\frac{\int_0^{\pi/2}|\cos\theta-\sin\theta|\,d\theta}{\int_0^{\pi/2}(\cos\theta+\sin\theta)\,d\theta}=\sqrt2-1.
\]

**Step 2: local saddle and global control.** The exact formula for \(F\) yields the large-\(x\) expansion
\[
F(x)=1-\frac{\mu}{x}+O(e^{-x^2/2}/x^3),\quad
-\log F(x)=\frac{\mu}{x}+\frac{\mu^2}{2x^2}+\frac{\mu^3}{3x^3}+O(x^{-4}).
\]
Let \(m=d-1\), \(q=(\mu m)^{1/3}\) and \(\Phi_m(x)=x^2/2-m\log F(x)\). Substituting \(x=q+s\), uniformly over each fixed compact range of \(s\), gives
\[
\Phi_m(q+s)=\frac{3q^2}{2}+\frac{\mu q}{2}+\frac{\mu^2}{3}+\frac{3s^2}{2}-\mu s+o(1).
\]
To justify global Laplace convergence, first observe that on every compact subinterval of \(t\in(0,\infty)\), \(q^{-2}\Phi_m(qt)\to t^2/2+1/t\) uniformly; this strictly convex function has unique minimizer \(t=1\), with value \(3/2\). The lower tail \(x\le\delta q\) is suppressed using monotonicity of \(F\) and \(-m\log F(\delta q)\sim q^2/\delta\); take \(\delta<1/3\). The upper tail \(x\ge Bq\) is suppressed by \(e^{-x^2/2}\) for \(B>2\). On a fixed neighborhood of \(t=1\), the quadratic term from \(x^2/2+q^3/x\), and bounded derivatives of the remaining \(\mu q^3/(2x^2)+\mu^2q^3/(3x^3)\), yield a uniform Gaussian bound \(C\exp(-c s^2+C|s|)\) for the centered integrands. Dominated convergence and the local expansion therefore show
\[
\begin{aligned}
p_d&\sim q\exp(-3q^2/2-\mu q/2-\mu^2/3)
\int_{\mathbb R}\exp(-3s^2/2+\mu s)\,ds\\
&=\sqrt{2\pi/3}\,q\exp(-3q^2/2-\mu q/2-\mu^2/6).
\end{aligned}
\]
The same dominated convergence applied to the conditional density gives \(X_d-q\Longrightarrow N(\mu/3,1/3)\). The logarithmic stretched-exponential exponent follows immediately.

**Step 3: actual chord lengths.** Let \(R=\|G\|_2\). In Gaussian polar coordinates, any degree-one homogeneous flux/event weight multiplies the standard radial density by \(R\); hence even **after conditioning on** \(B_d\), the radial variable is independent of direction and has the \(\chi_{d+1}\) distribution. In particular \(R/\sqrt d\to1\), and \(R-\sqrt d=O_{\mathsf P}(1)\). The opposite-facet chord length is exactly
\[
L_d=\frac1{|u_i|}=\frac{R}{X_d}.
\]
Since \(X_d=q_d+O_{\mathsf P}(1)\), expansion of the reciprocal yields
\[
L_d-\frac{\sqrt d}{q_d}=-\frac{\sqrt d}{q_d^2}(X_d-q_d)+o_{\mathsf P}(d^{-1/6}),
\]
where the radial fluctuation contributes only \(O_{\mathsf P}(d^{-1/3})\). Finally \(d^{1/6}\sqrt d/q_d^2\to\mu^{-2/3}\), proving both chord-length limits.

## Verification

Run `python verify.py` after installing packages listed in `requirements.txt`. It computes the exact integral numerically and independently generates Crofton lines using their offset-direction measure, directly tracing exit facets. It also checks saddlepoint ratios and conditional amplitude moments through dimension \(20{,}000\). The recorded execution ended with `ALL_CROFTON_HYPERCUBE_CHECKS_PASSED`. These experiments cross-check normalization, low-dimensional probabilities and asymptotic trends; the infinite-dimensional statements rest on the preceding analytical proof.

## Relationship to prior work

Kabluchko, Prochno and Thäle (2019, arXiv:1910.02676) analyze Haar random projections and large deviations for high-dimensional cubes and product measures; their fixed-projection-dimension laws do not give the Crofton line opposite-facet event. Akopyan, Edelsbrunner and Nikitenko (2020, arXiv:2007.07783) apply Crofton's formula to random **inscribed spherical polytopes**, rather than to cube face-to-face chords. Egan's *Pick Two Points* determines a superficially similar cube event using a different line sampling distribution: the line through two independent volume-uniform points has opposite-facet probability \(2/(d+1)\), not the Crofton law here (already \(2/3\ne\sqrt2-1\) in dimension two). Coleman (1969) examines several random-path mechanisms and chord-length distributions in a rectangle and cube; the full article was not available for comparison, a historical-priority limitation. MathWorld's opposite-face cube segment law concerns points sampled on opposite faces, not the Crofton line intensity. An equivalent result in unindexed integral-geometry literature remains possible; failed keyword searches are not a proof of priority.

## Limitations

The event is conditioned on an affine line meeting the cube and subsequently on opposite-facet exit. The limit is for \(d\to\infty\) along integers, not fixed dimension with a shrinking geometric parameter. The result does not establish analogous asymptotics for noncubical orthotopes, arbitrary convex bodies, lines sampled from two interior points, or the unconditional chord-length distribution. Historical priority has not been independently certified.

## References

1. Z. Kabluchko, J. Prochno, C. Thäle, *A new look at random projections of the cube and general product measures*, arXiv:1910.02676, first posted 2019-10-07, https://arxiv.org/abs/1910.02676.
2. A. Akopyan, H. Edelsbrunner, A. Nikitenko, *The Beauty of Random Polytopes Inscribed in the 2-Sphere*, arXiv:2007.07783, first posted 2020-07-15, https://arxiv.org/abs/2007.07783.
3. G. Egan, *Pick Two Points*, https://www.gregegan.net/SCIENCE/PickTwoPoints/PickTwoPoints.html (different two-interior-point line sampling model).
4. R. Coleman, *Random paths through convex bodies*, Journal of Applied Probability **6** (1969), 430–441, DOI:10.2307/3212012 (abstract consulted; full text unavailable).
5. E. Weisstein, *Cube Line Picking—Face and Face*, MathWorld, https://mathworld.wolfram.com/CubeLinePickingFaceandFace.html (face-endpoint sampling model).
