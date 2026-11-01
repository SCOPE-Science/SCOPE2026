# Singular-curvature extreme-chord tails and Dirichlet endpoint limits for Euclidean \(\ell_p\) balls

## Finding
For every integer \(d\ge2\) and every real \(1<p<2\), put \(q=d-1\) and regard the unit \(\ell_p\) ball \(B_p^d=\{x\in\mathbb R^d:\sum_{i=1}^d|x_i|^p\le1\}\) as a Euclidean convex body. Under Euclidean-motion-invariant sampling of unoriented affine lines conditioned on intersection with this body, the Euclidean chord length \(L\) obeys
\[
\Pr(L>2-\varepsilon)=C_{d,p}\varepsilon^{2q/p}+o(\varepsilon^{2q/p})\quad(\varepsilon\downarrow0),
\]
where, denoting Euclidean boundary area by \(S_p=\mathcal H^q(\partial B_p^d)\) and the unit \(q\)-ball volume by \(\kappa_q=\pi^{q/2}/\Gamma(1+q/2)\),
\[
C_{d,p}=\frac{d\,2^{q+1}p^{2q/p}\Gamma(1+1/p)^{2q}}{\kappa_q S_p\Gamma(1+2q/p)}.
\]
There is also a universal conditional shape law. For each sufficiently near-maximal chord, select its unique nearest coordinate diameter \(\{\pm e_i\}\), label its endpoints so their \(i\)-coordinates are positive and negative, and write their respective \(q\) transverse coordinate vectors as \(u\) and \(v\) in the same coordinate ordering. Then
\[
\left.\frac{(u,v)}{(p\varepsilon)^{1/p}}\ \right|\ \{L>2-\varepsilon\}\ \Longrightarrow\ \operatorname{Unif}(B_p^{2q}).
\]
The chosen diameter index converges to the uniform law on \(\{1,\dots,d\}\), independent of this limit. Equivalently, the \(2q\) absolute-coordinate powers of that limiting vector, together with their residual slack to one, have the \(\operatorname{Dirichlet}(1/p,\ldots,1/p,1)\) law. This last expression has \(2q+1\) parameters.

## Assumptions and scope
Lines are unoriented and carry Euclidean-motion-invariant line measure \(d\mu\), normalized through local coordinates near any specified oriented hemisphere as \(d\mu=d\sigma(e)\,dz\), with \(z\in e^\perp\), and \(\sigma\) the spherical area measure. Division by the total hitting measure makes the normalization choice immaterial. All lengths and areas are Euclidean. The exponent \(p\) is fixed strictly between one and two before \(\varepsilon\downarrow0\). A finite collection of diameter ties or endpoint coordinate zeros has line probability zero, and the nearest-diameter label is well-defined for all sufficiently near-maximal chords. The theorem makes no assertion uniform as \(p\) approaches either endpoint.

## Proof
**1. Isolated diameter pairs.** The inequality \(\|x\|_2\le\|x\|_p\le1\) holds in \(B_p^d\); for \(1<p<2\), equality in the first inequality at a nonzero point holds only when exactly one coordinate is nonzero. Thus the Euclidean diameter is two and is achieved at exactly the \(d\) unoriented pairs \(\{e_i,-e_i\}\). By compactness, all chords with lengths tending to two have both endpoints converging to one of these pairs; the neighborhoods may be chosen disjoint.

**2. Uniform singular local deficit.** Near \(\{e_1,-e_1\}\) write endpoints \(x_+(u)=(f(u),u)\) and \(x_-(v)=(-f(v),v)\), where \(u,v\in\mathbb R^q\), \(A(u)=\sum_{j=1}^q|u_j|^p\), and \(f(u)=(1-A(u))^{1/p}\). For \(A(u)+A(v)=T\to0\), Taylor's theorem gives \(f(u)+f(v)=2-T/p+O(T^2)\). Since \(\|u-v\|_2^2\le C_{p,q}T^{2/p}=o(T)\) uniformly as \(T\to0\), the Euclidean endpoint distance satisfies
\[
2-\|x_+(u)-x_-(v)\|_2=\frac{T}{p}+O(T^{2/p})+O(T^2)=\frac{T}{p}(1+o(1)),
\]
with the \(o(1)\) uniform over directions of \((u,v)\). This also furnishes two-sided bounds of the form \((1\pm\delta)T/p\) on sufficiently small neighborhoods.

**3. Local line-measure Jacobian.** Represent the line through the above endpoints by its slope \(\theta=(u-v)/(f(u)+f(v))\) relative to the first coordinate axis and its transverse intersection with the first-coordinate-zero hyperplane,
\[
h=\frac{f(v)u+f(u)v}{f(u)+f(v)}.
\]
At \((u,v)=0\), the differential of \((u,v)\mapsto(\theta,h)\) is the block matrix \(\frac12\begin{psmallmatrix}I&-I\\I&I\end{psmallmatrix}\) and has absolute determinant \(2^{-q}\). This local parametrization is a diffeomorphism for sufficiently small endpoints: any nearby line meeting the body has one endpoint on each graph, and the intersection is transverse at the axes. The unit direction is \(e=(1,\theta)/\sqrt{1+\|\theta\|_2^2}\). The spherical-direction Jacobian in the slope chart is \((1+\|\theta\|_2^2)^{-(q+1)/2}\), while projection of the intercept \((0,h)\) onto \(e^\perp\) has Jacobian \((1+\|\theta\|_2^2)^{-1/2}\). Therefore \(d\mu=(1+\|\theta\|_2^2)^{-(q+2)/2}d\theta\,dh=(2^{-q}+o(1))du\,dv\).

**4. Sharp volume and line normalization.** Set \((u,v)=(p\varepsilon)^{1/p}w\), where \(w\in\mathbb R^{2q}\). By step 2 the rescaled admissible endpoint domain tends in measure to \(B_p^{2q}=\{w:\sum|w_j|^p<1\}\); two-sided bounds from that step yield dominated convergence on a fixed bounded set. Its volume is
\[
V_{p,2q}=\frac{(2\Gamma(1+1/p))^{2q}}{\Gamma(1+2q/p)}.
\]
For one maximizing diameter, the leading hitting-line measure is \(2^{-q}V_{p,2q}(p\varepsilon)^{2q/p}\). Multiplying by the \(d\) disjoint maximizing neighborhoods yields the numerator. Cauchy's projection identity for the invariant line measure gives \(\mu\{\ell:\ell\cap B_p^d\ne\varnothing\}=\kappa_q S_p/2\). Division proves the coefficient and exponent.

**5. Conditional mark distribution.** In each rescaled neighborhood the joint measure density converges to the positive constant \(2^{-q}\) on the same unit \(\ell_p^{2q}\) ball and vanishes off it. Since every diameter has identical limiting measure, the diameter label is uniform and independent of the limiting transverse coordinates. Under \(w\mapsto(|w_1|^p,\ldots,|w_{2q}|^p)\), integrating signs transforms Lebesgue measure on \(B_p^{2q}\) into constant times \(\prod_j y_j^{1/p-1}dy\) on \(\{y_j\ge0,\sum y_j\le1\}\). Adding slack \(y_{2q+1}=1-\sum y_j\) is exactly the asserted Dirichlet law. This proves the full joint statement.

## Verification
The standalone file `verify_lp_chords.py` tests endpoint-to-line Jacobians in transverse dimensions one through five, computes the planar Euclidean boundary perimeter by numerical quadrature for \(p=1.25,1.5,1.75\), and independently evaluates actual convex-body chord intersections on a deterministic Sobol sample. At deficit \(\varepsilon=10^{-8}\), the ratios of direct numerical probability to the theorem's prediction are respectively approximately \(1.0000314\), \(1.0013043\), and \(1.0391284\); the slower convergence at the largest \(p\) is consistent with the \(\varepsilon^{(2-p)/p}\) local correction. The verifier additionally tests the limiting Dirichlet coordinate means and the exact separate Euclidean-ball boundary case. These finite tests corroborate but do not certify the infinite mathematical claim; steps 1–5 provide the proof.

## Relationship to prior work
Bäsel (2012) gives chord laws for regular polygons and supplies an early dated reference for invariant random-line chord sampling. García-Pelayo (2015) computes multi-chord distributions of convex and concave polygons. Schneider's integral-geometric notes provide the general invariant-measure and Crofton framework. These polygonal and general-measure results do not directly evaluate the present singular-curvature \(\ell_p\) family or its Dirichlet endpoint limit. Earlier smooth-positive-curvature diameter asymptotics apply to a different local quadratic regime, while polytope tangent-cone asymptotics are piecewise-linear; neither directly includes the nonpolyhedral \(1<p<2\) bodies with singular axial curvature.

Ren (2014), *Random chord distributions and containment functions*, is a materially relevant general chord-distribution paper. Its complete text was not accessible for a statement-by-statement comparison; its abstract describes a general integral representation and several examples but does not identify the present exact power law or conditional endpoint distribution. Wilkinson, Li and Patchigolla (2006) discuss chord measurements for non-spherical particles including superellipsoids; only the conference abstract was accessible. Historical priority therefore requires independent full-text investigation and is not guaranteed by the searches reported here.

## Limitations
The statement is fixed-dimensional and fixed-exponent; in particular it cannot be specialized to \(p=2\), where every diameter direction maximizes and the exact Euclidean-ball tail becomes \((\varepsilon-\varepsilon^2/4)^{q/2}\) instead. It does not give a full chord-length CDF, an all-exponent-uniform error constant, or an independently audited historical-priority certificate. The endpoint distribution is a limiting law, not an exact finite-deficit distribution. Unavailable older superellipsoid and general chord literature remains a priority risk.

## References
- U. Bäsel, *Random chords and point distances in regular polygons* (initial arXiv submission 2012-04-12), arXiv:1204.2707, https://arxiv.org/abs/1204.2707 .
- R. García-Pelayo, *Computation of the multi-chord distribution of convex and concave polygons* (2015), arXiv:1501.00292, https://arxiv.org/abs/1501.00292 .
- R. Schneider, *Integral Geometric Tools for Stochastic Geometry*, lecture notes, https://home.mathematik.uni-freiburg.de/rschnei/CIME.R.S.29.11.04.pdf .
- Ren, *Random chord distributions and containment functions*, *Advances in Applied Mathematics* (2014), DOI:10.1016/j.aam.2014.05.003 (full text not inspected).
- Wilkinson, Li, and Patchigolla, *Determining particle size distribution of non-spheres from chord length measurements* (conference abstract, 2006; full text not inspected).
