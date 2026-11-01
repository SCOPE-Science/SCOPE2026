# Sharp vertex-near-hit law for random central sections of regular simplices

## Finding

Let \(d\ge2\), and let \(\Delta_d\) be the Euclidean regular \(d\)-simplex with centroid at the origin and vertices \(v_0,\ldots,v_d\) normalized by \(\|v_i\|_2=1\). Choose a Haar-uniform unoriented linear hyperplane \(H\) through the origin. Its **origin-centered outer radius** is
\[
R_d(H)=\max\{\|x\|_2:x\in\Delta_d\cap H\},\qquad D_d(H)=1-R_d(H)^2.
\]
This is a radius *about the fixed centroid*, not the least enclosing-ball radius of the section. Let \(Z_1,\ldots,Z_d\) be independent standard Gaussians, set \(\mu_d=\mathbb E\max_{1\le j\le d}Z_j\), and define
\[
C_d=\frac{\sqrt{d(d+1)}}{\sqrt{2\pi}}\,\mu_d,\qquad
\mu_d=\int_0^\infty\bigl[1-\Phi(t)^d-(1-\Phi(t))^d\bigr]dt.
\]
Then \(C_d>0\), and the upper-endpoint law is
\[
\boxed{\mathbb P\{D_d\le\varepsilon\}=C_d\varepsilon+O_d(\varepsilon^2),\qquad\varepsilon\downarrow0.} \tag{1}
\]
In particular, \(C_2=\sqrt3/\pi\) and \(C_3=3\sqrt6/(2\pi)\). For \(N\) independent Haar hyperplanes with maximal radius \(M_{d,N}\),
\[
\boxed{N(1-M_{d,N}^2)\ \Longrightarrow\ \mathrm{Exp}(\text{rate }C_d),}\tag{2}
\]
and \(\mathbb E(1-M_{d,N}^2)\sim1/(C_dN)\).

For \(d=2\) the entire distribution is elementary: \(0\le D_2\le2/3\) almost surely, and, for \(0\le\varepsilon\le2/3\), writing
\[
k_\varepsilon=\frac{1-\sqrt{1-4\varepsilon/3}}{1+\sqrt{1-4\varepsilon/3}},
\]
one has
\[
\boxed{\mathbb P\{D_2\le\varepsilon\}=
\frac6\pi\arcsin\left(\frac{\sqrt3\,k_\varepsilon}{2\sqrt{1-k_\varepsilon+k_\varepsilon^2}}\right).}\tag{3}
\]
The probability is \(0\) for \(\varepsilon<0\) and \(1\) for \(\varepsilon\ge2/3\).

## Assumptions and scope

All norms and angular measures are Euclidean. The regular simplex vertices obey \(\langle v_i,v_j\rangle=-1/d\) for distinct indices. The hyperplane is chosen via a uniform unit normal \(U\in S^{d-1}\), with \(U\) and \(-U\) identified. Sections are central, and the dimension \(d\) is held fixed in the small-\(\varepsilon\) expansion. The sampling limit fixes \(d\) before \(N\to\infty\). No formula for the entire law in dimensions greater than two is claimed. The event of a section containing a simplex vertex has probability zero.

## Proof

**1. The section vertices and the near-vertex criterion.** Almost surely, the heights \(a_i=\langle U,v_i\rangle\) are nonzero. Every section vertex lies in the relative interior of a simplex edge with opposite-signed endpoint heights; conversely every such crossed edge contributes a distinct section vertex. For the crossed edge joining \(v_i\) and \(v_j\), the intersection is \(x=(1-t)v_i+tv_j\) with \(t=|a_i|/(|a_i|+|a_j|)\), and the regular-simplex Gram matrix gives
\[
\|x\|_2^2=1-\frac{2(d+1)}d\,t(1-t). \tag{4}
\]
The norm is convex along a segment; hence its maximum on the section is attained at a section vertex. Put, for sufficiently small \(\varepsilon>0\),
\[
q_\varepsilon=\frac{1-\sqrt{1-2d\varepsilon/(d+1)}}2,
\qquad k_\varepsilon=\frac{q_\varepsilon}{1-q_\varepsilon}
=\frac{d}{2(d+1)}\varepsilon+O_d(\varepsilon^2).\tag{5}
\]
By (4), the event \(D_d\le\varepsilon\) is exactly the union, over the \(d+1\) vertices, of the **near-hit events**
\[
A_i(k)=\left\{\text{some }j\ne i\text{ has }a_ia_j<0
\text{ and } |a_i|\le k|a_j|\right\}.\tag{6}
\]
This exact equivalence holds while \(q_\varepsilon<1/2\).

**2. The first-order area of a near-hit belt.** Fix \(i\). Outside a null set, uniquely decompose \(U=s v_i+\sqrt{1-s^2}\,w\), with \(w\in S^{d-2}\subset v_i^\perp\). Put \(\beta_j(w)=\langle w,v_j+v_i/d\rangle\). Then \(a_i=s\) and \(a_j=-s/d+\sqrt{1-s^2}\,\beta_j\). Since \(\sum_{j\ne i}\beta_j=0\), both positive and negative \(\beta_j\) occur for all but a null set of \(w\). For \(s>0\), condition (6) is exactly
\[
s(1-k/d)\le k\sqrt{1-s^2}\,\max_{j\ne i}(-\beta_j),
\]
and for \(s<0\) the same condition uses \(|s|\) and \(\max_{j\ne i}\beta_j\). Uniformly in \(w\), the two endpoint positions are
\[
 s_+(w)=k\max(-\beta_j)+O_d(k^2),\qquad
 |s_-(w)|=k\max(\beta_j)+O_d(k^2).
\]
Uniform surface measure on \(S^{d-1}\) has \(s\)-density at zero
\[
f_d(0)=\frac{\Gamma(d/2)}{\sqrt\pi\,\Gamma((d-1)/2)}.
\]
Because this density is even and smooth near zero (also for \(d=2\)), integration gives
\[
\mathbb P(A_i(k))=k f_d(0)\,
\mathbb E_w\left[\max_j\beta_j(w)-\min_j\beta_j(w)\right]
+O_d(k^2).\tag{7}
\]
The \(O_d(k^2)\) remainder is uniform: all \(\beta_j\) are bounded and the implicit boundary equations have derivatives bounded away from zero for small \(k\).

**3. Gaussian range and the union.** Let \(G\) be standard Gaussian in \(v_i^\perp\) and write \(G=\|G\|w\). The covariance matrix of the Gaussian vector \((\beta_j(G))_{j\ne i}\) equals that of
\[
\sqrt{\frac{d+1}d}(Z_j-\overline Z)_{j=1}^d,
\qquad \overline Z=d^{-1}\sum_{j=1}^dZ_j.
\]
Thus its expected range is \(2\sqrt{(d+1)/d}\,\mu_d\). By independence of \(\|G\|\) and \(w\), and
\[
\mathbb E\|G\|=\sqrt2\,\frac{\Gamma(d/2)}{\Gamma((d-1)/2)},
\]
the factor multiplying \(k\) in (7) is \(\sqrt{2/\pi}\sqrt{(d+1)/d}\,\mu_d\).

If \(i\ne j\), the normals \(v_i,v_j\) are linearly independent; a spherical neighborhood on which simultaneously \(|\langle U,v_i\rangle|=O_d(k)\) and \(|\langle U,v_j\rangle|=O_d(k)\) has probability \(O_d(k^2)\) for \(d\ge3\). In dimension \(2\), the two near-hit belts are disjoint for sufficiently small \(k\). Therefore the first-order union probability is the sum of the \(d+1\) vertex probabilities. Substituting (5) into (7) proves (1). The Gaussian integral for \(\mu_d\) follows by splitting \(\mathbb E\max_jZ_j\) at zero and using its cdf \(\Phi^d\); the special constants follow from \(\mu_2=1/\sqrt\pi\), \(\mu_3=3/(2\sqrt\pi)\).

**4. Exact planar law.** For \(d=2\), the two tangent projections adjacent to any vertex are \(\beta=\pm\sqrt3/2\) when \(w\in S^0\). Solving the exact inequality in step 2 gives a symmetric angular belt around each projective vertex-normal axis, of half-width
\[
\theta(k)=\arcsin\left(\frac{\sqrt3 k}{2\sqrt{1-k+k^2}}\right).
\]
The three projective axes are separated by \(\pi/3\), so the belts have disjoint interiors for \(k\le1/2\), and cover the projective angular circle at \(k=1/2\). Their total normalized length is \(3(2\theta)/\pi\), proving (3). Formula (4) implies that the largest possible squared deficit is \(2/3\), since these three belts already cover all normals at that threshold.

**5. Extreme-value consequence.** Since the deficit is supported in \([0,1]\) and its cdf is \(C_d\varepsilon+O_d(\varepsilon^2)\) at zero, independence gives
\[
\Pr\{N\min_{1\le j\le N}D_d(H_j)>t\}
=\bigl(1-F_d(t/N)\bigr)^N\longrightarrow e^{-C_dt}.
\]
A fixed-small-neighborhood exponential domination, and an exponentially small bound outside that neighborhood, justify integrating the tails and yield the stated mean asymptotic. This establishes (2).

## Verification

The standalone file `verify.py` checks the exact planar endpoint, half-mass, and parameter identities; it also independently reconstructs section radii from all crossed simplex edges for reproducible Gaussian-oriented samples in dimensions two and three. Seeded numerical diagnostics agree with the entire planar cdf and the leading three-dimensional coefficient within stated finite-sample tolerances. These are diagnostics, not substitutes for the analytic surface-area and overlap arguments above. Run with `python verify.py` (Python standard library only).

## Relationship to prior work

Guédon, Litvak, Tatarko, and Vritsiou analyze high-probability diameters of random sections of general convex bodies, with applications to \(p\)-ellipsoids, without this exact regular-simplex origin-centered endpoint constant. König studies extremal **volumes** of sections of regular simplices, whereas Hinrichs and coauthors study random **ellipsoid** section radii. The prior geometric results on random simplex-section vertex and face counts encode sign patterns of normals, but not their height ratios: knowing the signs leaves the radial extent undetermined. The present law depends explicitly on these ratios, hence is not a corollary of face-number distributions. The one-spike ellipsoid beta law is structurally distinct and has different angular singularities. The quoted primitive Gaussian-range integral is a standard order-statistic identity; no novelty is claimed for it by itself.

## Limitations

The only full distribution classified is planar. The high-dimensional assertion is a fixed-dimensional small-deficit expansion; its remainder is not uniform when dimension grows. The origin-centered outer radius is not the section's optimal circumradius. The leading constant comes from known Gaussian order-statistic expectations, but its appearance as this section probability is the proposed new connection. An independently performed literature audit could identify an equivalent older spherical tube or simplex-section calculation; no exhaustive historical-priority certification is claimed. No independent mathematical audit has been performed.

## References

- O. Guédon, A. E. Litvak, K. Tatarko, B.-H. Vritsiou, “On random diameters of convex bodies,” arXiv:2609.24131, first posted 2026-09-21, https://arxiv.org/abs/2609.24131.
- H. König, “Non-central sections of the regular n-simplex,” arXiv:2312.01325, first posted 2023-12-03, https://arxiv.org/abs/2312.01325.
- A. Hinrichs, D. Krieg, E. Novak, J. Prochno, M. Ullrich, “Random sections of ellipsoids and the power of random information,” arXiv:1901.06639, first posted 2019-01-20, https://arxiv.org/abs/1901.06639.
- “Exact mean and chi-square fluctuations of Haar central simplex-section vertex counts,” public published-finding corpus record `2026/10/11/SCOPE-exact-mean-and-chi-square-fluctuations-of-haar-central-simplex-s--d3f9b0447a8e`.
- “Joint chi-square face-vector fluctuations of random central regular-simplex sections,” public published-finding corpus record `2026/10/11/SCOPE-joint-chi-square-face-vector-fluctuations-of-random-central-regu--aa90c887fe90`.
