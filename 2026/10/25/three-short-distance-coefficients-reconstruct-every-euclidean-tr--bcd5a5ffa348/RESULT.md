# Three short-distance coefficients reconstruct every Euclidean triangle

## Finding

Let \(K\) be any nondegenerate Euclidean triangle, with area \(A\), perimeter \(P\), and interior angles \(\alpha_1,\alpha_2,\alpha_3\). Take two independent points uniformly with respect to area in \(K\), and write \(F_K(t)\) for the distribution function of their Euclidean distance. There exists \(t_0(K)>0\) such that, **exactly** for \(0\le t<t_0(K)\),
\[
F_K(t)=\frac{\pi}{A}t^2-\frac{2P}{3A^2}t^3+\frac{Q}{8A^2}t^4,
\qquad Q=\sum_{i=1}^3\left[1+(\pi-\alpha_i)\cot\alpha_i\right].
\]
The central finding is **finite-jet inverse rigidity**: the three displayed coefficients determine the triangle uniquely up to rigid motion and reflection. No data at intermediate or large distances and no higher moments are needed. The angular coefficient formula itself is prior work; the inverse-rigidity conclusion is the contribution of this result.

## Assumptions and scope

The triangle is a compact, convex, full-dimensional subset of \(\mathbb R^2\); points are sampled independently from normalized planar Lebesgue area, not from the boundary. All angles lie in \((0,\pi)\), sum to \(\pi\), and are in radians. Equality of distributions on any nonempty common interval beginning at zero implies congruence. The statement includes all nondegenerate isosceles and equilateral triangles. It does not assert that finite jets identify arbitrary convex polygons.

If the coefficients of \(t^2,t^3,t^4\) are \(c_2,c_3,c_4\), respectively, the observed invariants are recovered exactly by
\[
A=\pi/c_2,\qquad P=-3A^2c_3/2,\qquad Q=8A^2c_4.
\]

## Proof

**1. Exact local distribution.** A polygon's covariogram is \(g_K(z)=\operatorname{Area}(K\cap(K+z))\), and
\[
F_K(t)=A^{-2}\int_{\lVert z\rVert\le t}g_K(z)\,dz.
\]
For outward edge normals \(n_i\), the intersection \(K\cap(K+tu)\) is formed by moving the \(i\)-th support line inward by \(t\max(0,-n_i\cdot u)\). For sufficiently small \(t\), uniformly over unit directions \(u\), the polygon retains its cyclic support-line adjacency. Polygonal area is exactly quadratic in these small support-line offsets. Integrating the constant and linear terms over directions gives \(2\pi A\) and \(-2P t\). Integrating the quadratic part gives
\[
\frac{t^2}{2}\sum_i\left[1+(\pi-\alpha_i)\cot\alpha_i\right].
\]
Indeed, the directional integrals for a single positive normal projection, its square, and the product at neighboring normals are, respectively, \(2\), \(\pi/2\), and \((\sin\alpha_i-\alpha_i\cos\alpha_i)/2\). Radial integration with factor \(t\,dt/A^2\) gives the exact quartic. This formula is established more generally for convex polygons in the cited published short-distance coefficient theorem; it is reproduced here to make the inverse argument self-contained.

**2. Reduce shape reconstruction to two angle sums.** Set
\[
f(x)=\cot(x/2),\qquad g(x)=(\pi-x)\cot x.
\]
If \(s=P/2\) and \(r=A/s=2A/P\) is the triangle's inradius, the usual incircle tangency identity gives \(s-\ell_i=r\cot(\alpha_i/2)\). Summing yields
\[
\sum_i f(\alpha_i)=s/r=\frac{P^2}{4A},\qquad
\sum_i g(\alpha_i)=Q-3.
\]
Consequently it suffices to show that these two symmetric sums, together with \(\sum_i\alpha_i=\pi\), determine the unordered angle triple.

**3. A strict curvature-ratio lemma.** Direct differentiation gives
\[
f''(x)=\tfrac12\cot(x/2)\csc^2(x/2)>0,\qquad
g''(x)=2\csc^2x\,[1+(\pi-x)\cot x]>0.
\]
Put \(\beta=\pi-x\) and \(v=\beta/2\). Their curvature ratio satisfies
\[
R(x):=\frac{g''(x)}{f''(x)}
=\frac{\sin(2v)-2v\cos(2v)}{2\sin^4v},
\]
and differentiation with respect to \(v\) yields
\[
\frac{dR}{dv}=\frac{4\cos^2v}{\sin^5v}\,(v\cos v-\sin v)<0,
\qquad 0<v<\pi/2.
\]
The inequality follows from \(\tan v>v\). Since \(v=(\pi-x)/2\), **\(R(x)\) is strictly increasing** throughout \(0<x<\pi\). Positivity of \(g''\) follows as well from \(\sin\beta-\beta\cos\beta>0\), whose derivative is \(\beta\sin\beta>0\).

**4. Injectivity on the ordered angle chamber.** Sort the angles as \(a\le b\le c=\pi-a-b\) and define
\[
H(a,b)=f(a)+f(b)+f(c),\qquad J(a,b)=g(a)+g(b)+g(c).
\]
For \(0<a<\pi/3\), the admissible interval is \(a\le b\le(\pi-a)/2\). By strict convexity of \(f\), \(H\) is strictly decreasing as \(b\) increases toward \((\pi-a)/2\). Its endpoint functions
\[
H_{\max}(a)=2f(a)+f(\pi-2a),\qquad
H_{\min}(a)=f(a)+2f((\pi-a)/2)
\]
are both strictly decreasing from infinity to \(3\sqrt3\) as \(a\) rises from zero to \(\pi/3\). Thus for each fixed \(H_0>3\sqrt3\), the level \(H=H_0\) in the ordered chamber is a single connected continuous arc joining the two isosceles edges, parametrized by increasing \(a\). For \(H_0=3\sqrt3\), strict Jensen equality gives only the equilateral triple.

In the scalene interior \(a<b<c\), write \(f'_a=f'(a)\), etc. The quotients
\[
\lambda_{ac}=\frac{g'(c)-g'(a)}{f'(c)-f'(a)},\qquad
\lambda_{bc}=\frac{g'(c)-g'(b)}{f'(c)-f'(b)}
\]
are weighted averages of \(R=g''/f''\), with weights \(f''>0\), over \([a,c]\) and \([b,c]\). Strict increase of \(R\) implies \(\lambda_{ac}<\lambda_{bc}\). Consequently
\[
\det\frac{\partial(H,J)}{\partial(a,b)}
=(f'(a)-f'(c))(f'(b)-f'(c))
(\lambda_{bc}-\lambda_{ac})>0.
\]
Moreover \(H_b=f'(b)-f'(c)<0\). Along the connected level \(H=H_0\), implicit differentiation yields
\[
\frac{dJ}{da}=-\frac{\det\partial(H,J)/\partial(a,b)}{H_b}>0.
\]
Continuity extends strict ordering through the isosceles endpoints. Hence \(H\) and \(J\) uniquely determine the sorted angle triple, including boundary and equilateral cases.

**5. Recover lengths.** With \(A,P\) known, set \(r=2A/P\), \(s=P/2\). For each recovered angle,
\[
\ell_i=s-r\cot(\alpha_i/2)=\frac P2-\frac{2A}{P}\cot(\alpha_i/2).
\]
These are the opposite side lengths, uniquely specified up to permutation. Side-side-side congruence proves the claim.

## Verification

The standalone standard-library script `verify.py` independently intersects translated triangles with the originals and numerically integrates their covariograms. It checks five nonequivalent triangles against the exact quartic for a small positive radius (relative discrepancies between \(7.03\times10^{-6}\) and \(1.04\times10^{-5}\) at the stated quadrature resolution), tests strict increase of the analytic curvature ratio on 5,000 sampled angle triples, and checks monotonicity of \(J\) along five fixed-\(H\) level arcs. Executing `python3 verify.py` prints `VERIFY_OK`. These computations are finite checks; the proof above establishes the global result.

## Relationship to prior work

Bäsel's 2012 preprint [1] derives complete Euclidean two-point distance laws for regular polygons, and Pure et al. [2] give an algorithmic law for arbitrary polygons; neither their method alone supplies the three-coefficient triangle reconstruction. The published convex-polygon small-distance theorem [3] already gives the exact quartic and its optimal angular stability bound, **so the quartic and coefficient are not claimed as novel**. Gates [4] established recognition of triangles from odd moments of their full random-chord-length distributions, while O'Hara [5] treats full distance distributions of generic polygonal domains. These full-profile identifiability results do not imply that only the three coefficients at zero suffice. The added theorem is the global injectivity of the angle-sum pair at fixed area and perimeter, proved by the strict curvature-ratio lemma and ordered-level analysis. The general covariogram and orientation-dependent recognition results of Gasparyan and Ohanyan [6] use stronger directional data than the scalar local distance coefficients here.

## Limitations

The result identifies exact noiseless triangles from an infinitesimal distributional jet; no uniform quantitative inverse stability or finite-sample statistical recovery is claimed, especially near isosceles and degenerate shape boundaries. The general-polygon quartic is already published, and the theorem is restricted to triangles. The full text of Gates [4] was not obtained, so a historical equivalent local three-coefficient characterization cannot be completely excluded from the bibliographic record; the accessible statement covers a different all-moments recognition criterion. Full text of [6] was likewise unavailable. The 2019 arbitrary-polygon framework and the later 2026 generic-polygon theorem are relevant general contexts, not proofs of local three-jet injectivity.

## References

1. U. Bäsel, *Random chords and point distances in regular polygons*, arXiv:1204.2707, initially public 12 April 2012, https://arxiv.org/pdf/1204.2707.
2. R. Pure, S. Durrani, F. Tong, J. Pan, *Distance Distribution Between Two Random Nodes in Arbitrary Polygons*, arXiv:1903.07757 (2019), https://arxiv.org/pdf/1903.07757.
3. *Sharp uniform angular stability for the short-pair distance coefficient of convex polygons*, published research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-uniform-angular-stability-for-the-short-pair-distance-coef--24e8bcd8655b.
4. J. Gates, *Recognition of triangles and quadrilaterals by chord length distribution*, Journal of Applied Probability **19** (1982), 873–879, https://doi.org/10.2307/3213843.
5. J. O'Hara, *Identification of generic polygonal domains by integral-geometric invariants*, arXiv:2608.02288 (2026), https://arxiv.org/pdf/2608.02288.
6. A. Gasparyan, V. Ohanyan, *Recognition of triangles by covariogram*, J. Contemporary Mathematical Analysis **48** (2013), 110–122, https://www.aragasparyan.com/projects/recognition-triangles.html.
