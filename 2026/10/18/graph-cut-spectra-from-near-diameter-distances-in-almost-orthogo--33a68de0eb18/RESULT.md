# Graph-cut spectra from near-diameter distances in almost orthogonal parallelotopes

## Finding

The Euclidean distance distribution of two uniform random points in a nearly orthogonal parallelotope has a singular endpoint profile whose breakpoints and multiplicities are precisely the weighted cuts of a graph. The resulting limit yields both a complete weighted-cut-spectrum measurement and an exact failure of commutation between the geometric and distance-endpoint limits.

**Theorem (weighted-cut crossover and endpoint coefficient).** Let \(d\ge 2\), and let \(\Gamma=([d],E,w)\) be a finite simple graph with strictly positive, finite edge weights \(w_{ij}\); isolated vertices and the empty graph are allowed. Let \(H\) be its real symmetric weighted adjacency matrix, with zero diagonal. Write \(W=\sum_{\{i,j\}\in E}w_{ij}\), \(a_i=\sum_{j:\{i,j\}\in E}w_{ij}\), and let \(c\) be the number of connected components, counting isolated vertices. For \(h>0\) sufficiently small that \(I_d+hH\) is positive definite, choose any real invertible \(A_h\) with \(A_h^{\mathsf T}A_h=I_d+hH\), and set \(K_h=A_h[0,1]^d\).

For independent uniform points \(X_h,Y_h\) of \(K_h\), write \(Z_h=\|X_h-Y_h\|_2^2\) and \(D_h=\operatorname{diam}(K_h)\). For \(s\in\{\pm1\}^d\), put \(C_\Gamma(s)=\sum_{\{i,j\}\in E:s_i\ne s_j}w_{ij}\). Then:

1. The squared diameter is exactly \(D_h^2=d+2hW\).
2. Uniformly for \(t\) in every fixed compact subset of \([0,\infty)\),

\[
\lim_{h\downarrow0}h^{-2d}\mathbb P\bigl(D_h^2-Z_h\le ht\bigr)
=F_\Gamma(t)
:=\frac{1}{4^d(2d)!}\sum_{s\in\{\pm1\}^d}\bigl(t-4C_\Gamma(s)\bigr)_+^{2d}.
\]

3. Extending \(F_\Gamma\) by zero to negative arguments, its distributional derivative is

\[
F_\Gamma^{(2d+1)}=\frac{1}{4^d}\sum_{s\in\{\pm1\}^d}\delta_{4C_\Gamma(s)}.
\]

Consequently the complete **multiset** of weighted graph cuts, including multiplicities and zeros, is recoverable from the geometric boundary-layer profile. In particular, the zero cut has multiplicity \(2^c\), determining the number of components. This does not assert recovery of the graph's labels or isomorphism class from its cut multiset.

4. For each fixed admissible \(h>0\),

\[
\lim_{\varepsilon\downarrow0}\varepsilon^{-2d}
\mathbb P\bigl(D_h^2-Z_h\le\varepsilon\bigr)
=\frac{2^c}{4^d(2d)!\prod_{i=1}^d(1+ha_i)^2}.
\]

For the undeformed cube (\(h=0\)), the corresponding coefficient is \(2^d/[4^d(2d)!]\). Hence the ratio between the limiting positive-deformation endpoint coefficient and the cube's coefficient is exactly \(2^{c-d}\); this is strictly below one whenever the graph has at least one edge.

For one edge of weight \(w>0\) in dimension two, the crossover is particularly transparent:

\[
F_\Gamma(t)=\frac{t_+^4+(t-4w)_+^4}{192}.
\]

## Assumptions and scope

The ambient Euclidean dimension is a fixed integer \(d\ge2\), independent of the deformation parameter. Edge weights are fixed, strictly positive real numbers. The graph may be disconnected. One sufficient positive-definiteness condition is \(0<h<1/\max_i a_i\) when at least one edge is present; if the graph is empty, any \(h>0\) gives the undeformed cube. The points are independent and uniform for Euclidean volume, and all distance deficits are in **squared Euclidean distance**. The perturbation parameter \(h\downarrow0\) and the tolerance \(\varepsilon\downarrow0\) are distinct limits.

## Proof

**1. Reduction to a cube with its exact difference density.** By linear change of variables, the displacement of \(X_h-Y_h\) equals \(A_hz\), where \(z\in[-1,1]^d\) has independent triangular coordinate densities \(1-|z_i|\). Therefore \(Z_h=z^{\mathsf T}(I_d+hH)z\) and its probability density in cube difference coordinates is exactly \(\prod_{i=1}^d(1-|z_i|)\). The Jacobian of the affine change of variables cancels under uniform sampling.

**2. Diameter and maximizing corners.** Positive definiteness makes \(z\mapsto z^{\mathsf T}(I_d+hH)z\) convex on \([-1,1]^d\), so its maximum is achieved at a sign vector. At \(s\in\{\pm1\}^d\),

\[
s^{\mathsf T}(I_d+hH)s=d+2h\sum_{\{i,j\}\in E}w_{ij}s_is_j=d+2hW-4hC_\Gamma(s).
\]

All positive weights imply the maximum is \(d+2hW\). Equality holds exactly for spins constant on each connected component, giving \(2^c\) maximizing sign vectors.

**3. Uniform localization at corners.** For \(z\in[-1,1]^d\), each edge satisfies \(2w_{ij}z_iz_j\le2w_{ij}\), whence

\[
D_h^2-z^{\mathsf T}(I_d+hH)z\ge d-\sum_i z_i^2\ge \sum_i(1-|z_i|).
\]

If the squared-distance deficit is at most \(ht\) with \(t\le T<\infty\), every coordinate therefore lies at distance at most \(hT\) from a sign. For sufficiently small \(h\), the contributing neighborhoods of distinct sign vectors are disjoint. Write \(z_i=s_i(1-hy_i)\), with \(0\le y_i\le T\). Uniformly in these bounded variables,

\[
\frac{D_h^2-z^{\mathsf T}(I_d+hH)z}{h}
=4C_\Gamma(s)+2\sum_i y_i+O_{\Gamma,T}(h).
\]

The joint difference-density times the Jacobian is exactly \(h^{2d}\prod_i y_i\,dy\). Dominated convergence gives a sum of elementary Dirichlet integrals:

\[
\int_{\substack{y_i\ge0\\2\sum_i y_i\le b}}
\prod_i y_i\,dy=\frac{b_+^{2d}}{4^d(2d)!}.
\]

This proves pointwise convergence for every \(t\ge0\). The finite-parameter probability profiles are nondecreasing in \(t\); their continuous limiting profile therefore gives uniform convergence on every compact \(t\)-interval (by a finite partition and monotonicity).

**4. Cut-spectrum recovery.** The distributional \((2d+1)\)-st derivative of \((t-u)_+^{2d}/(2d)!\) is \(\delta_u\). Thus the derived atomic measure has an atom of mass \(4^{-d}\) for each sign vector of cut weight \(u/4\), with repeated cuts appearing with their multiplicity. Its zero atom has mass \(2^c/4^d\).

**5. Endpoint law at fixed deformation.** Fix \(h>0\). The only maximizing corners are the \(2^c\) component-constant sign vectors. Near one such corner put \(z_i=s_i(1-v_i)\), \(v_i\ge0\). As \(\|v\|\to0\),

\[
D_h^2-z^{\mathsf T}(I_d+hH)z
=2\sum_{i=1}^d(1+ha_i)v_i+O_h(\|v\|^2).
\]

The density remains exactly \(\prod_i v_i\). Scaling \(v_i=\varepsilon y_i/[2(1+ha_i)]\), using the same simplex integral and summing the \(2^c\) separated maximizing corners yields the coefficient in assertion 4. No other corner contributes for sufficiently small \(\varepsilon\), because its diameter gap is at least \(4h\min\{C_\Gamma(s)>0\}>0\) whenever such a cut exists; in the empty graph, every corner is maximal and the same calculation applies. At \(h=0\), all \(2^d\) corners are maximal and have unit linear coefficients, giving the cube coefficient. This proves the noncommuting endpoint limit.

## Verification

The standalone standard-library script `checks/check_distance_tail.py` enumerates all spin configurations for four weighted graphs, verifies the squared-diameter/cut-energy identity exactly with rational arithmetic and checks that the zero-cut multiplicity is \(2^c\). For a one-edge graph in dimension two, it integrates the **original triangular difference density** by composite Simpson quadrature and compares the small-\(h\) boundary layer with the explicit quartic spline. It separately checks the fixed-\(h\), small-\(\varepsilon\) coefficient at three deformation levels. Run `python3 checks/check_distance_tail.py`; the final line is `VERIFY_OK`. These finite checks are consistency tests, not a replacement for the proof in arbitrary dimension.

## Relationship to prior work

Wang studies the general two-point Euclidean distance distribution of a convex body through its covariogram, and obtains Brunn–Minkowski and rigidity results. The present theorem uses this natural geometric-probability observable but focuses on a singular diameter-endpoint regime for a prescribed family of near-orthogonal parallelotopes, recovering a weighted cut multiset.

Lao studies extreme diameters of **many-sample** point sets in a cube, including a Weibull-type limit associated with its diametral corners. That is a different limit in sample size from the present one-pair, small-deformation crossover. Henze and Jammalamadaka examine largest interpoint distances for smooth ellipsoids, while Schrempp examines related smooth-body extremes. These works do not furnish the graph-cut breakpoint identity, or the exact \(2^{c-d}\) endpoint coefficient transition. Classical identities between weighted cuts and Ising energies are used here as ingredients and are not claimed as discoveries.

## Limitations

The theorem concerns positive weighted adjacency deformations, sufficiently small \(h\), fixed dimension, and squared Euclidean distances. It gives no quantitative rate uniform over growing dimension or variable weights. The cut multiset does not generally identify a graph up to isomorphism; inverse uniqueness is not asserted. Only the first leading order of the fixed-geometry endpoint tail and the limiting crossover profile are determined. Possible equivalent formulations in older extreme-value or graph-spectral literature cannot be ruled out by the searches performed, and independent peer validation remains outstanding.

## References

- Sinan Wang, *A Brunn–Minkowski Theory for the Distribution of Random Pairs of Points in Convex Bodies*, arXiv:2610.01916, first public version 2026-10-01. https://arxiv.org/abs/2610.01916
- Wei Lao, *Some Weak Limit Laws for the Diameter of Random Point Sets in Bounded Regions*, doctoral thesis, Karlsruhe Institute of Technology, 2010, Chapter 6.3 (Theorem 6.6). https://publikationen.bibliothek.kit.edu/1000019800/105664897
- Norbert Henze and Sreenivasa Rao Jammalamadaka, *The Limit Law of the Largest Interpoint Distance in a \(d\)-Dimensional Ellipsoid*, arXiv:2606.29036 (2026). https://arxiv.org/abs/2606.29036
- Michael Schrempp, *The Limit Distribution of the Largest Interpoint Distance for Distributions Supported by an Ellipse and Generalizations*, arXiv:1505.01597 (2015). https://arxiv.org/abs/1505.01597
