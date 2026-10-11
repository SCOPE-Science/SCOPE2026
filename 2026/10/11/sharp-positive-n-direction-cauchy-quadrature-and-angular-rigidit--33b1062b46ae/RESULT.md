# Sharp positive \(N\)-direction Cauchy quadrature and angular rigidity

## Finding

Fix an integer \(N\ge2\). Over all normalized nonnegative rules with at most \(N\) unoriented directions in the Euclidean plane, the sharp worst-convex-body error in the Cauchy perimeter formula is
\[
\boxed{\displaystyle E_N=\frac1\pi\left(1-\frac\pi{2N}\cot\frac\pi{2N}\right).}
\]
Its unique optimizers, up to rotation, reflection, relabeling and reversing representatives of unoriented directions, are the equally spaced projective directions \(\theta_j=\theta_0+j\pi/N\) with weights \(1/N\). In particular,
\[
E_N=\frac{\pi}{12N^2}+\frac{\pi^3}{720N^4}+O(N^{-6}).
\]

There is also a quantitative angular-rigidity theorem. Put \(x=\pi/(2N)\) and \(r_N=\cot(x)/N\). For a rule with \(N\) positive weights and distinct unoriented directions, list in cyclic order the \(2N\) outward normal angles of its associated zonogon, and let \(\Delta_1,\ldots,\Delta_{2N}\in(0,\pi)\) be successive angular gaps (including the closing gap). Write \(\delta=E(\mu)-E_N\). If \(0\le\delta\le r_N/4\), then
\[
\boxed{\displaystyle \sum_{i=1}^{2N}\left(\Delta_i-\frac\pi N\right)^2\le \frac{48}{x r_N^2}\,\delta.}
\]
More precisely, for \(0\le\delta<r_N/2\), the right side may be replaced by \(24\delta/[x r_N(r_N-2\delta)]\). The exponent \(1/2\) in the resulting angular-distance bound is sharp: a prescribed tangential deformation has angular deviation proportional to \(\sqrt\delta\).

## Assumptions and scope

Let \(K\subset\mathbb R^2\) be any compact convex body with nonempty interior, and \(P(K)>0\) its Euclidean perimeter. A rule is \(\mu=\sum_{j=1}^{m}w_j\delta_{u_j}\), where \(1\le m\le N\), \(u_j\in S^1/\{\pm1\}\), \(w_j\ge0\) and \(\sum_jw_j=1\). Define the sampled Cauchy brightness and normalized worst error by
\[
Q_\mu(K)=\sum_jw_j\operatorname{length}(K\mid u_j^\perp),\qquad
E(\mu)=\sup_{K}\frac{|Q_\mu(K)-P(K)/\pi|}{P(K)}.
\]
The positive weights, number of unoriented directions, calibration \(\sum_jw_j=1\), normalization by perimeter, and full-dimensional testing class are essential. The associated origin-symmetric zonogon is \(Z_\mu=\sum_jw_j[-u_j,u_j]\). Distinct positive directions generate exactly \(2N\) sides; the rigidity estimate concerns this full-dimensional noncoalesced class. No minimax claim is made for signed rules, adaptive data-dependent directions, other metrics, or dimensions above two.

## Proof

**1. The exact convex-body defect.** Cauchy's projection formula and the planar surface-area measure \(S_K\) give
\[
\operatorname{length}(K\mid u^\perp)=\frac12\int_{S^1}|u\cdot v|\,dS_K(v),\quad
\frac{P(K)}\pi=\frac12\int_{S^1}\frac2\pi\,dS_K(v).
\]
Thus, with \(F_\mu(v)=h_{Z_\mu}(v)=\sum_j w_j|u_j\cdot v|\) and \(R=2/\pi\),
\[
\frac{Q_\mu(K)-P(K)/\pi}{P(K)}=\frac1{2P(K)}\int_{S^1}(F_\mu-R)\,dS_K.
\]
The upper bound \(E(\mu)\le\tfrac12\|F_\mu-R\|_\infty\) is immediate. To prove equality, choose a direction at which the even continuous discrepancy attains its maximal modulus and approximate the surface-area measure \(\tfrac12(\delta_v+\delta_{-v})\) by the normalized surface-area measures of increasingly thin, long rectangles with major edge normals \(\pm v\). This gives
\[
\boxed{E(\mu)=\tfrac12\max\{R-r_\mu,\ R_\mu-R\}},
\]
where \(r_\mu=\min_{S^1}h_{Z_\mu}\) is the origin-centered inradius and \(R_\mu=\max_{S^1}h_{Z_\mu}\) is the origin-centered circumradius. In particular \(E(\mu)\ge(R-r_\mu)/2\). This duality identity is the planar case of the already published sharp defect theorem of An; it is an ingredient, not a novelty claim.

**2. The sharp finite-side inradius bound.** The zonogon \(Z_\mu\) has perimeter \(4\): Cauchy's perimeter identity and \(\int_0^{2\pi}|\cos\theta|\,d\theta=4\) give \(P(Z_\mu)=\sum_j4w_j=4\). If all generators are parallel, \(r_\mu=0\), which is strictly below the claimed optimal radius. Otherwise let \(m=2k\le2N\) be the number of its genuine sides, with outward normals in cyclic order and gaps \(\Delta_i\in(0,\pi)\) summing to \(2\pi\). The intersection of their inward-shifted supporting halfplanes at distance \(r_\mu\) from the origin is a tangential \(m\)-gon \(T\subseteq Z_\mu\). The sum of the two tangent lengths adjacent to each vertex yields
\[
P(T)=2r_\mu\sum_{i=1}^m\tan\frac{\Delta_i}{2}\le P(Z_\mu)=4.
\]
Strict convexity of tangent, Jensen's inequality, and monotonicity of \(m\tan(\pi/m)\) in integers \(m\ge4\) give
\[
\sum_{i=1}^m\tan\frac{\Delta_i}{2}\ge m\tan\frac\pi m\ge2N\tan x.
\]
Consequently \(r_\mu\le1/(N\tan x)=r_N\), and therefore
\[
E(\mu)\ge\frac12(R-r_N)=\frac1\pi(1-x\cot x)=E_N.
\]
If equality holds then all positive weights correspond to \(N\) distinct projective directions, all gaps equal \(\pi/N\), and \(P(T)=P(Z_\mu)\). Inclusion of planar convex bodies and equality of perimeters force equality of their support functions (apply Cauchy's perimeter formula to their nonnegative width differences), so \(T=Z_\mu\). Thus \(Z_\mu\) is a centered regular \(2N\)-gon and its generating directions and lengths force equal weights and equal projective spacings.

**3. Attainment and the exact error.** The uniform \(N\)-direction rule generates a centered regular \(2N\)-gon of perimeter \(4\), with exact inradius \(r_N=\cot x/N\) and circumradius \(R_N=1/(N\sin x)\). Its negative support discrepancy dominates its positive discrepancy, because
\[
R_N+r_N=\frac1N\cot\frac x2<\frac4\pi=2R,
\]
where the strict inequality is \((x/2)\cot(x/2)<1\). Therefore \(E(\mu)=(R-r_N)/2=E_N\). The Taylor series for \(x\cot x\) proves the displayed \(N^{-2}\) asymptotics.

**4. Quantitative rigidity.** Suppose all \(N\) weights are positive and directions distinct. Put \(r=r_\mu\). The bound from step 1 implies \(r\ge r_N-2\delta\), whereas the tangential-polygon comparison from step 2 implies
\[
0\le\sum_i\tan\frac{\Delta_i}{2}-2N\tan x\le\frac2r-\frac2{r_N}\le\frac{4\delta}{r(r_N)}.
\]
For \(y\in[0,\pi/2)\), \(\tan''y=2\tan y\sec^2y\ge2y\). Integrating twice on either side of \(x>0\) establishes the global quantitative tangent Jensen bound
\[
\tan y-\tan x-\sec^2x\,(y-x)\ge\frac{2x}{3}(y-x)^2.
\]
Since \(\sum_i\Delta_i/2=2Nx=\pi\), the linear terms cancel in the sum, giving
\[
\sum_i\tan\frac{\Delta_i}{2}-2N\tan x\ge\frac x6\sum_i(\Delta_i-2x)^2.
\]
For \(\delta<r_N/2\), combine these inequalities and \(r\ge r_N-2\delta\) to obtain
\[
\sum_i(\Delta_i-2x)^2\le\frac{24\delta}{x r_N(r_N-2\delta)}.
\]
For \(\delta\le r_N/4\), its denominator is at least \(x r_N^2/2\), which gives the simpler stated estimate. At \(\delta=0\) equality implies all normal gaps regular.

**5. Optimality of the square-root exponent.** Start with the regular \(2N\)-gon and deform its consecutive normal gaps by setting \(\Delta_1=\Delta_{N+1}=2x+t\), \(\Delta_2=\Delta_{N+2}=2x-t\), and all other gaps equal to \(2x\), for sufficiently small nonzero real \(t\). There is a centrally symmetric tangential polygon with these gaps, inradius
\[
r(t)=\frac2{\sum_i\tan(\Delta_i/2)}
\]
and perimeter \(4\). Its opposite facets have equal lengths, so it is a zonogon of \(N\) positive segment generators; since its perimeter is \(4\), the generator weights sum to one. At \(t=0\) the negative support discrepancy strictly dominates the positive discrepancy, and this remains true for sufficiently small \(|t|\). Expanding the tangent sum at \(x\) then gives
\[
\delta(t)=\frac{r_N-r(t)}2=\frac{r_N^2\tan''x}{8}t^2+O(t^4)>0,
\quad
\sum_i(\Delta_i-2x)^2=4t^2.
\]
Thus angular deviation is of exact order \(\sqrt{\delta}\), so no globally uniform exponent greater than \(1/2\) is possible on this class.

## Verification

All constants are derived analytically for every integer \(N\ge2\), not from a finite enumeration. Running `python3 verify.py` with the standard Python library outputs `VERIFY_OK 2944 normalizations, sample perturbations, and sharpness checks`. The deterministic checks independently evaluate zonogon inradii from facet normals and circumradii from vertices; they test uniform-rule equality, \(2944\) sample configurations, the explicit stability bound, and the tangential second-order coefficient. Floating-point checks corroborate—but do not establish—the infinite statements in the proof.

## Relationship to prior work

Cauchy's perimeter and projection formulas are classical. An (2026, arXiv:2609.05869v1, Theorems 3.2, 4.3, 6.1) proved the general sharp convex-body defect identity, impossibility of finite exact Cauchy rules, and a uniform \(O(t^{-1})\) estimate for spherical \(t\)-designs. That paper does not state the sharp planar positive \(N\)-direction minimax value, uniqueness, angular stability, or sharp exponent. The present reduction openly reuses its norm identity and classical regular-polygon tangent geometry; the claimed additional result is their exact optimized combination and quantitative rigidity. Gui, Hu, and Li (arXiv:2607.28768v2) give angular Jensen deficits for *torsional rigidity* of tangential polygons, not a Cauchy quadrature error. Akiyama and Kamae (arXiv:2201.06736v1) study normalized \(L^2\) directional width deviation *of a given polygon*, not the present uniform perimeter-reconstruction error over all convex bodies. Audet, Hansen and Messine (2009, DOI 10.1007/s00454-008-9103-9) prove the different general bound \(w(P)/P(P)\le\cot(\pi/(2m))/(2m)\) for width of arbitrary \(m\)-gons; it is not sharp for the regular centrally symmetric \(2N\)-gons here, and does not state the Cauchy quadrature optimization or an angular-error stability theorem. These distinctions involve different quantifiers and objectives, not just titles.

## Limitations

Only positive normalized fixed-direction rules, Euclidean two-dimensional convex bodies, and perimeter-normalized worst-case error are covered. The stability theorem requires distinct positive generators; it controls facet-normal angular gaps and does not assert quantitative weight stability. The exact result is a mathematical derivation rather than independent certification. Existing polygon comparison and Jensen inequalities are essential ingredients; a historically unindexed equivalent quadrature or quantitative-stability result cannot be excluded merely by searches. No signed-rule or higher-dimensional optimization is implied.

## References

1. C. An, *Exact Finite Integral Geometry: Directional Kernels and Spherical Designs*, arXiv:2609.05869v1, publicly posted 2026-09-05, especially Sections 3, 4, and 6.
2. C. Gui, Y. Hu, and Q. Li, *A Quantitative Pólya–Szegő Theorem for Tangential Polygons*, arXiv:2607.28768v2, 2026, especially Theorem 1.1 and Section 2.
3. S. Akiyama and T. Kamae, *Width deviation of convex polygons*, arXiv:2201.06736v1, 2022.
4. S. Arya and D. M. Mount, *Cauchy's Surface Area Formula in the Funk Geometry*, SoCG 2026, DOI 10.4230/LIPIcs.SoCG.2026.8.
5. C. Audet, P. Hansen, and F. Messine, *Isoperimetric Polygons of Maximum Width*, *Discrete & Computational Geometry* **41** (2009), 45–60, DOI 10.1007/s00454-008-9103-9.
6. R. Schneider, *Convex Bodies: The Brunn–Minkowski Theory*, 2nd expanded edition, Cambridge University Press, 2014.
