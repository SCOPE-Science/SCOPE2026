# Two strict Mahler peaks and a cusp in the symmetric two-apex cubical family

## Finding
Let \(C=[-1,1]^3\) and, for \(t\geq0\), define the centrally symmetric polytope
\[
K_t=\operatorname{conv}\bigl(C\cup\{\pm(1+t,1,1),\ \pm(1,1+t,1)\}\bigr).
\]
Let \(K_t^\circ=\{y\in\mathbb R^3:x\cdot y\leq1\ \text{for every }x\in K_t\}\), and put \(M(t)=\operatorname{vol}_3(K_t)\operatorname{vol}_3(K_t^\circ)\). Then the **exact complete volume-product profile** is
\[
M(t)=\begin{cases}
\dfrac{4(t+6)(32+28t-t^3)}{9(t+2)(t+4)},&0\leq t\leq2,\\[5pt]
\dfrac{32(3t^3+12t^2+12t-16)}{9t^2(t+4)},&t\geq2.
\end{cases}
\]
The origin-centered cube is the only finite-parameter minimizer: \(M(0)=32/3\), and \(M(t)>32/3\) for every \(t>0\), while \(\lim_{t\to\infty}M(t)=32/3\). On \((0,\infty)\) there are **exactly two strict local maxima**, at
\[
t_1=\sqrt5-1,\qquad M(t_1)=\frac{200-40\sqrt5}{9},
\qquad t_2=\frac4{\sqrt3},\qquad M(t_2)=\frac{8+16\sqrt3}{3}.
\]
The first maximum is strictly larger and is the unique global maximum of \(M\) on \([0,\infty)\). The transition \(t=2\) is a **strict cusped local minimum**, with \(M(2)=320/27\), left derivative \(-88/81\), and right derivative \(32/81\).

## Assumptions and scope
All parameters \(t\) are real and nonnegative, and all volumes are ordinary three-dimensional Lebesgue volumes. The convex hull includes exactly two antipodal pairs of outlying points, whose positive representatives are cube-facet corner apices on two adjacent coordinate facets. The functional is the centered Mahler product because \(K_t=-K_t\). No affine normalization or smoothness hypothesis is imposed. The formulas make no assertion about more general collections of cube apices or about arbitrary centrally symmetric convex bodies.

## Proof
**1. Exact polyhedral chambers.** The eight vertices of \(C\), together with the four marked apices, generate \(K_t\). At positive parameters there are two open combinatorial regimes \(0<t<2\) and \(t>2\). A supporting-plane triangulation, with each face oriented outward, has sixteen triangles in each chamber; the corresponding polar has twelve distinct vertices and twenty outward triangles. Every face normal for the primal triangle \((a,b,c)\) is \(n=(b-a)\times(c-a)\), oriented so \(q=n\cdot a>0\). The dual vertex is \(n/q\). For each claimed face and every input vertex \(v\), the exact certificate checks \(q-n\cdot v\geq0\), and the resulting closed triangulation has each edge incident to exactly two triangles. Dual support inequalities and reconstruction of all generating primal vertices certify that no primal or polar facets are missing.

Here the certificate is **uniform in the real parameter**, not a finite-parameter enumeration. On the first chamber it substitutes \(t=2u/(1+u)\), and on the second \(t=2+u\), always with \(u>0\). Every supporting-plane gap and relevant signed offset then simplifies to a rational function of \(u\) whose numerator and denominator have coefficients of one sign; these explicit polynomial coefficient tests give exact nonnegativity over the entire chamber. The candidate combinatorics are initially proposed by a numerical convex hull at one interior sample, but no conclusion depends on the floating-point output without the subsequent exact, universal inequalities. The standalone `verify_two_apex.py` contains all input coordinates, triangulations, inequalities, dual reconstruction, and exact determinant sums.

**2. The two volumes.** For an origin-interior convex polytope with outward triangle boundary \((a,b,c)\), divergence (equivalently, signed tetrahedron decomposition from the origin) gives \(\operatorname{vol}_3(P)=\frac16\sum\det(a,b,c)\). Applying this formula to the exact outward triangulations of the primal and polar gives
\[
\operatorname{vol}_3(K_t)=\begin{cases}
\dfrac{2(t+2)(t+6)}3,&0<t<2,\\[3pt]
\dfrac{4(t+2)^2}3,&t>2,
\end{cases}
\]
\[
\operatorname{vol}_3(K_t^\circ)=\begin{cases}
\dfrac{2(32+28t-t^3)}{3(t+2)^2(t+4)},&0<t<2,\\[3pt]
\dfrac{8(3t^3+12t^2+12t-16)}{3t^2(t+2)^2(t+4)},&t>2.
\end{cases}
\]
The independent chamber expressions agree at \(t=2\). At \(t=0\) the convex hull is the cube, whose polar is the octahedron of volume \(4/3\). Continuity of convex-body and polar volume fills both chamber boundaries. Multiplication yields the claimed product.

**3. All critical points and the global order.** Direct algebraic differentiation gives
\[
M'(t)=-\frac{8(t^2+2t-4)(t^3+10t^2+36t+56)}{9(t+2)^2(t+4)^2}\quad(0<t<2)
\]
and
\[
M'(t)=-\frac{256(3t^2-16)}{9t^3(t+4)^2}\quad(t>2).
\]
The cubic factor on the first branch is positive for \(t>0\); the quadratic changes sign only at \(\sqrt5-1\). The derivative on the second branch changes sign only at \(4/\sqrt3\). The left and right derivatives at \(t=2\) have opposite signs, proving the strict cusp minimum. Direct exact substitution gives the two displayed heights, and \((200-40\sqrt5)/9>(8+16\sqrt3)/3\). Together with \(M(0)=32/3\) and the limit at infinity, this determines every global and local extremum.

**4. Strict Mahler gap on the whole family.** The two deficit factorizations are
\[
M(t)-\frac{32}{3}=
-\frac{4t(t^3+6t^2-4t-56)}{9(t+2)(t+4)}>0\quad(0<t<2)
\]
and
\[
M(t)-\frac{32}{3}=\frac{128(3t-4)}{9t^2(t+4)}>0\quad(t>2).
\]
For the first interval, \(t^3+6t^2-4t-56<8+24-56=-24\) since \(-4t\leq0\); for the second, \(3t-4>2\). Continuity handles \(t=2\). The limit follows from the leading cubic coefficients.

## Verification
Run `python verify_two_apex.py` in a Python environment with SymPy, NumPy and SciPy installed. The script independently proposes primal facet triangles in each open chamber, verifies **all** primal support inequalities symbolically over that chamber, constructs every polar vertex from a primal facet, verifies polar support, checks closed oriented triangulations, reconstructs all primal vertices from polar facets, and computes the primal/polar volumes by exact determinants. Finally, it checks both rational product formulas, differentiation identities, strict gaps, endpoint matching, and the strict order of the two maxima. The tests succeeded when run with the embedded script. Floating-point convex hulls select candidate face incidences only; each derived statement is subsequently checked exactly in symbols. No appeal to finite sampling is used to infer the infinite-parameter statements.

## Relationship to prior work
Shen and Dubovski, *A sharp minimum for cube-apex bodies in every dimension* (first public version 7 October 2026, arXiv:2610.11014), prove a sharp constrained **minimum** among compatible arrays at prescribed total outward height; their Theorem 3 gives a **lower bound** for a two-apex construction, and their Corollary 4 proves a lower inequality for a specified four-dimensional two-apex example. Those results neither state nor algebraically supply the exact three-dimensional full-parameter product here, nor the two strict maxima and intervening combinatorial cusp. Their Figure 1 illustrates a **single** opposite apex pair, not this two-pair family. Nazarov, Petrov, Ryabogin and Zvavitch, *A remark on the Mahler conjecture: local minimality of the unit cube* (arXiv:0905.0867), prove local cube minimality for nearby symmetric bodies, not a global exact profile of this family. Other cube–cross-polytope intersection and symmetric corner-truncation profiles involve different combinatorial families. More concretely, this two-apex polytope has twelve facets at each nondegenerate parameter, whereas a three-dimensional intersection of a cube with a centered scaled cross-polytope has eight, fourteen, or six facets according to its scale (the middle regime has all six coordinate facets and all eight diagonal facets). Since affine isomorphisms preserve facet counts, the two generically parameterized bodies are not affinely equivalent. No remaining implication of the exact profile was identified. The global inequality for the present family is a consequence of the new explicit formulas, not a claim to prove Mahler's conjecture in general.

## Limitations
Originality means no mathematically covering statement was identified in the searched indexed literature and available historical claims, not a proof of absolute priority. Equivalent polytope-volume formulas in older unindexed literature may exist. The parameter value \(t=2\) is treated by continuity, not by applying generic-combinatorics formulas directly at the degeneration. The certificate relies on exact symbolic rational arithmetic following a finite candidate face discovery; the included checker specifies all computational dependencies. The result is special to dimension three and exactly two adjacent symmetric corner-apex pairs.

## References
1. Hanyue Shen and Pavel B. Dubovski, *A sharp minimum for cube-apex bodies in every dimension*, arXiv:2610.11014v1, first posted 2026-10-07, https://arxiv.org/html/2610.11014v1 . Relevant material: Section 2, Theorem 1; Section 3, Theorems 2–3 and Corollary 4.
2. Fedor Nazarov, Fedor Petrov, Dmitry Ryabogin and Artem Zvavitch, *A remark on the Mahler conjecture: local minimality of the unit cube*, arXiv:0905.0867, https://arxiv.org/html/0905.0867v1 . Relevant material: Theorem in Section 1 and Sections 2–5.
