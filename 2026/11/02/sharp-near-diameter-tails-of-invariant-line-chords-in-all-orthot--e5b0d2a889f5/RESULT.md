# Sharp near-diameter tails of invariant line chords in all orthotopes

## Finding
For every integer \(d\ge4\) and positive half-side lengths \(a_1,\ldots,a_d\), let \(A=(\sum_i a_i^2)^{1/2}\) and draw a random affine line meeting the orthotope \(K=\prod_i[-a_i,a_i]\) from motion-invariant line measure. Its chord length \(L\) satisfies, as \(\varepsilon\downarrow0\),
\[
\Pr\{L>2A-\varepsilon\}=C_d(a)\varepsilon^{2d-2}+o(\varepsilon^{2d-2}),\quad
C_d(a)=\frac{2^{1-d}A^{d+1}\Gamma((d+1)/2)}{\pi^{(d-1)/2}(2d-2)!\,(\prod_i a_i)^3\sum_i a_i^{-1}}.
\]
For fixed diameter \(2A\), the sharp leading coefficient is minimized uniquely by cubes. For \(K=[-1,1]^4\), this is \(\Pr\{L>4-\varepsilon\}\sim\varepsilon^6/(960\pi)\).

## Assumptions and scope
Here \(d\) is a fixed integer at least four, each \(a_i\) is strictly positive, and \(\varepsilon\) tends to zero with the orthotope fixed. A line is parametrized by an unoriented direction \(u\in S^{d-1}/\{\pm1\}\) and perpendicular offset \(z\in u^\perp\). The underlying invariant measure is spherical direction measure times \((d-1)\)-dimensional Lebesgue measure \(dz\); condition on lines meeting \(K\). This differs from choosing directions uniformly *after* conditioning on intersection, from selecting random pairs of body points, and from sampling lines through the center. Normalizations cancel in the probability ratio. Sets of tangent lines have measure zero. The diameter is \(2A\).

## Proof
**1. An exact exceedance integral.** For any fixed unit \(u\), the offsets whose line-chord contains a segment of length greater than \(\ell>0\) are, up to measure-zero boundaries, the projection onto \(u^\perp\) of \(K\cap(K-\ell u)\). Its coordinate widths are \(b_i=2a_i-\ell|u_i|\). If any \(b_i\le0\), the projected set has zero \((d-1)\)-volume. Otherwise the Cauchy projection formula for an orthotope gives
\[
F_\ell(u)=\mathbf1_{\{b_i>0\ \forall i\}}\sum_{i=1}^d|u_i|\prod_{j\ne i}b_j.
\]
Consequently \(\Pr(L>\ell)=\mathbb E_uF_\ell(u)/Z\), where \(u\) is uniform on the entire unit sphere and the normalizing projection volume is
\[
Z=\mathbb E_u\operatorname{vol}_{d-1}(\operatorname{proj}_{u^\perp}K)
=2^{d-1}\left(\prod_i a_i\right)\left(\sum_i a_i^{-1}\right)
\frac{\Gamma(d/2)}{\sqrt\pi\,\Gamma((d+1)/2)}.
\]
In deriving this identity use \(\mathbb E|u_i|=\Gamma(d/2)/(\sqrt\pi\Gamma((d+1)/2))\).

**2. Localization and scaling.** Let \(\ell=2A-\varepsilon\). The inequalities \(b_i>0\) imply \(|u_i|<2a_i/\ell\). In the limit these constraints and \(\sum u_i^2=1\) force the direction into arbitrarily small neighborhoods of exactly \(2^d\) body-diagonal unit vectors with coordinates \(\pm a_i/A\). By coordinate reflections, it suffices to study \(q=(a_1/A,\ldots,a_d/A)\). Parametrize a neighborhood via
\[
u(v,\varepsilon)=\frac{q+\varepsilon v}{\sqrt{1+\varepsilon^2\|v\|^2}},\qquad v\in q^\perp.
\]
The surface element is \(\varepsilon^{d-1}(1+\varepsilon^2\|v\|^2)^{-d/2}\,dH(v)\). Put \(w_i=a_i/(2A^2)-v_i\); then \(\sum_i a_iw_i=1/2\), and
\[
b_i=2A\varepsilon w_i+O(\varepsilon^2).
\]
All contributing \(v\) remain in a fixed bounded set, because the limiting conditions \(w_i\ge0\) together with \(\sum_i a_iw_i=1/2\) define a compact simplex. Away from its facets the scaled integrand converges pointwise, while a uniform bound on the compact region gives dominated convergence. Hence the leading integral over one diagonal is
\[
(2A)^{d-1}\varepsilon^{2d-2}
\int_{\substack{\sum_i a_i w_i=1/2\\ w_i\ge0}}
\left(\sum_i\frac{a_i}{A}\prod_{j\ne i}w_j\right)dH(w).
\]
The two powers \(d-1\) arise respectively from the angular neighborhood and from the projected overlap.

**3. Simplex evaluation and exact constant.** Substitute \(y_i=a_iw_i\). The induced hyperplane Jacobian satisfies \(dH(w)=A(\prod_i a_i)^{-1}dy_1\cdots dy_{d-1}\) with \(y_d=1/2-\sum_{i<d}y_i\). By the standard Dirichlet integral,
\[
\int_{\substack{\sum_i a_i w_i=1/2\\w_i\ge0}}
\left(\sum_i\frac{a_i}{A}\prod_{j\ne i}w_j\right)dH(w)
=\frac{A^2}{2^{2d-2}(2d-2)!\,(\prod_i a_i)^2}.
\]
Summing all \(2^d\) diagonals and dividing by sphere area \(2\pi^{d/2}/\Gamma(d/2)\) gives the spherical numerator
\[
\mathbb E_uF_{2A-\varepsilon}(u)
\sim\frac{2A^{d+1}}{(2\pi^{d/2}/\Gamma(d/2))(2d-2)!\,(\prod_i a_i)^2}\,\varepsilon^{2d-2}.
\]
Dividing by \(Z\) proves the stated coefficient. The value for the four-cube follows by direct substitution and \(\Gamma(5/2)=3\sqrt\pi/4\).

**4. Sharp rigidity.** For fixed \(A\), minimizing \(C_d(a)\) means maximizing
\[
(\prod_i a_i)^3\sum_i a_i^{-1}
=(\prod_i a_i)^2e_{d-1}(a_1,\ldots,a_d),
\]
where \(e_{d-1}\) is the elementary symmetric sum. AM–GM and Cauchy–Schwarz give \(\prod_i a_i\le(A/\sqrt d)^d\). Maclaurin's inequality followed by Cauchy–Schwarz gives
\[
e_{d-1}(a)\le d\left(\frac{\sum_i a_i}{d}\right)^{d-1}
\le d(A/\sqrt d)^{d-1}.
\]
All equalities hold simultaneously only if \(a_1=\cdots=a_d=A/\sqrt d\). This is the unique minimizer up to rigid motions and coordinate permutation.

## Verification
A standalone Python/SciPy script `verify_chords.py` numerically integrates the exact intersecting-line formula for selected planar and spatial boxes, and independently performs seeded quasi-Monte Carlo integration on the localized direction chart in dimensions four and five. The computed quotient of exact/numerical tail probability by \(C_d(a)\varepsilon^{2d-2}\) approaches one as \(\varepsilon\) decreases. Representative dimension-four cube quotients at \(\varepsilon=0.1,0.05,0.025\) are approximately \(1.1412,1.0673,1.0329\); the dimension-five cube gives approximately \(1.1643,1.0776,1.0381\). Computations test constants but are not used as proof of the infinite asymptotic. Execute `python verify_chords.py` with NumPy and SciPy.

## Relationship to prior work
Classical invariant-line chord distributions of two- and three-dimensional rectangles and boxes are established in earlier literature, notably Coleman (1981), Gille (1988), and Clement (2013). Bäsel (2012) develops related planar chord laws. Ren (2014) treats general random chord distribution and containment functions. These are acknowledged as foundations rather than claimed as new. The claim here is the explicit near-diameter exponent and leading coefficient for every fixed dimension at least four, plus the sharp cube minimizing property under fixed diagonal; the inspected available material does not establish that combination. The full texts of Coleman, Gille and Ren were not available for complete exclusion of equivalent results.

## Limitations
The theorem concerns invariant-measure random affine lines, not uniform-direction-conditioned chord sampling. It does not determine the full chord distribution, any uniform-in-dimension remainder or a generalization to arbitrary convex bodies. Exact historical priority remains subject to independent literature review because several plausible older sources were only accessible through abstracts or bibliographic records. No independent audit has been performed.

## References
- U. Bäsel, *Random chords and point distances in regular polygons*, arXiv:1204.2707, initial preprint 12 April 2012.
- G. T. Clement, *Joint probability density functions of random trajectories through a box*, arXiv:1312.5292, initial preprint 18 December 2013.
- R. Coleman, *Intercept lengths of random probes through boxes*, Journal of Applied Probability 18 (1981), 276–282, doi:10.2307/3213189.
- W. Gille, *The chord length distribution of parallelepipeds with their limiting cases*, Experimental Techniques of Physics 36 (1988), 197–208.
- D. Ren, *Random chord distributions and containment functions*, Advances in Applied Mathematics 58 (2014), 1–20, doi:10.1016/j.aam.2014.05.003.
