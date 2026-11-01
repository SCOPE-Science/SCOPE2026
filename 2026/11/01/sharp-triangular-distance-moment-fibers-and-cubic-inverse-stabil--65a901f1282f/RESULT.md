# Sharp triangular distance-moment fibers and cubic inverse stability

## Finding

Let \(T\) be any nondegenerate Euclidean triangle, let \(X,Y\) be independent uniformly area-distributed points in \(T\), and define \(m_j(T)=\mathbb E[|X-Y|^{2j}]\) for \(j=1,2,3\). The first two moments determine the triangle's area but, except for equilateral triangles, leave a full one-parameter continuum of incongruent triangles. The third moment resolves that ambiguity. More precisely, put \(\mu=m_1\), \(\nu=m_2\),
\[
\alpha=6\mu,\qquad h=\sqrt{40\nu-72\mu^2},\qquad
M_0=\frac{249}{35}\mu\nu-\frac{1494}{175}\mu^3.
\]
A pair \((\mu,\nu)\) is feasible for a nondegenerate triangle if and only if
\[
\mu>0,\qquad \frac95\mu^2\le\nu<\frac{27}{10}\mu^2.
\]
For each feasible pair, **all** feasible sixth-distance moments form exactly the closed sharp interval
\[
\boxed{\quad M_0-\frac{h^3}{840}\le m_3\le M_0+\frac{h^3}{840}.\quad}
\]
When \(h>0\), both endpoints are attained by different isosceles triangles, and every intermediate value by a triangle with the same first two moments. When \(h=0\), the unique shape is equilateral. The triple \((m_1,m_2,m_3)\) determines the unordered side lengths and hence the congruence class uniquely. Moreover the inverse has a locally uniform Hölder modulus of exponent \(1/3\) on compact families of nondegenerate triangles, and this exponent cannot be increased uniformly, even arbitrarily close to the equilateral triangle.

## Assumptions and scope

Sampling means the normalized two-dimensional area measure, with replacement and independently; it does **not** mean boundary sampling, a random line chord, or a random direction. All side lengths are positive and satisfy the strict triangle inequalities. Translation, rotation, and reflection do not affect the statistics, so congruence includes reflection. Let the three squared side lengths be \(A,B,C\) and their elementary symmetric functions be \(e_1=A+B+C\), \(e_2=AB+BC+CA\), and \(e_3=ABC\).

## Proof

**Step 1: exact forward moments.** Choose vertices \(0,u,v\) so that \(|u|^2=A\), \(|v|^2=B\) and \(|u-v|^2=C\). Write \(X=xu+yv\) and \(Y=x'u+y'v\), where the two coordinate pairs are independent and uniform in the reference simplex \(x,y\ge0\), \(x+y\le1\). Their joint monomial moments are explicit:
\[
\mathbb E[x^iy^j]=\frac{2i!j!}{(i+j+2)!},
\qquad i,j\in\{0,1,\ldots\}.
\]
The squared distance equals
\[
Q=A(x-x')^2+B(y-y')^2+(A+B-C)(x-x')(y-y').
\]
Expanding \(Q,Q^2,Q^3\), using the displayed factorial formula and independence, and collecting symmetric terms gives the three **exact polynomial identities**
\[
\boxed{\quad m_1=\frac{e_1}{18},\qquad
m_2=\frac{e_1^2-2e_2}{60},\qquad
m_3=\frac{23e_1^3-62e_1e_2+20e_3}{4200}.\quad} \tag{1}
\]
The executable exact-arithmetic check independently expands and integrates the four coordinate variables for all three exponents. Identity (1), rather than finite sampling, supplies the analytic foundation for the inverse results.

**Step 2: area, feasibility, and the complete two-moment fiber.** Heron's identity expressed in squared sides is
\[
16\,\operatorname{Area}(T)^2=4e_2-e_1^2.
\]
Using (1) gives the exact area recovery
\[
\boxed{\quad \operatorname{Area}(T)^2=\frac{81}{4}\mu^2-\frac{15}{2}\nu.\quad}\tag{2}
\]
Put \(s=e_1=18\mu\) and \(S_2=A^2+B^2+C^2=60\nu\). By Cauchy, \(S_2\ge s^2/3\), with equality only at \(A=B=C\). By strict positivity of Heron's expression, \(S_2<s^2/2\). These are precisely the displayed feasible bounds on \((\mu,\nu)\).

Conversely, for any pair satisfying these bounds, put \(\alpha=s/3\) and \(h=\sqrt{(2/3)(S_2-s^2/3)}\). They obey \(0\le h<\alpha\). Every unordered real triple with the required sum and square sum is represented, up to coordinate permutation, by
\[
\boxed{\quad
\begin{aligned}
A&=\alpha+h\cos\theta,\\
B&=\alpha+h\cos(\theta+2\pi/3),\\
C&=\alpha+h\cos(\theta+4\pi/3),
\end{aligned}
\quad 0\le\theta\le\pi/3.\quad}\tag{3}
\]
Indeed the intersection of a plane and a centered sphere is a circle, whose dihedral coordinate permutations reduce its angular fundamental domain to the indicated interval. Each squared side is positive since it is at least \(\alpha-h>0\). The fixed Heron expression is strictly positive by the strict upper bound on \(\nu\); hence every triple in (3) actually consists of squared side lengths of a nondegenerate triangle. No other triangles have those first two moments.

**Step 3: sharp third-moment interval and reconstruction.** Elementary trigonometric identities applied to (3) give
\[
 e_3=\alpha^3-\frac{3\alpha h^2}{4}+\frac{h^3}{4}\cos(3\theta).
\]
Substitution into (1) and simplifying all \(\mu,\nu\) terms yields
\[
\boxed{\quad m_3=M_0+\frac{h^3}{840}\cos(3\theta).\quad}\tag{4}
\]
Since \(\cos(3\theta)\) decreases continuously from \(1\) to \(-1\) on the fundamental domain, (4) proves the full interval, its sharpness, and the complete realizability criterion. The endpoints correspond to \(\theta=0\) and \(\theta=\pi/3\), where two squared side lengths coincide, i.e. to two isosceles shapes. For \(h>0\), (4) is strictly monotone in \(\theta\), so the moment triple determines the unordered squared sides uniquely. Equivalently, inversion of (1) reconstructs \(e_1,e_2,e_3\), and the squared sides are precisely the positive roots of \(z^3-e_1z^2+e_2z-e_3\).

**Step 4: two moments are genuinely insufficient.** For an exact illustrative collision, consider squared-side triples
\[
\left(\frac54,\frac78,\frac78\right),\qquad
\left(1+\frac{\sqrt3}{8},1,1-\frac{\sqrt3}{8}\right).
\]
Both satisfy strict triangle inequalities and have \(m_1=1/6\), \(m_2=33/640\), and squared area \(45/256\), but their third moments differ by exactly \(1/53760\). More generally, for each \(h>0\) with \(h<\alpha\), the interval of distinct \(\theta\)-values in (3) gives a continuum of incongruent triangles having identical \(m_1,m_2\).

**Step 5: sharp stability exponent.** Fix any compact side-length bounds \(0<r\le\text{every side}\le R<\infty\), and consider two feasible moment triples whose componentwise discrepancies are at most \(\varepsilon\) after dividing the \(j\)-th discrepancy by \(R^{2j}\). Formula (1) and boundedness show that the coefficients of the two **scaled** monic cubic side-square polynomials differ by at most \(C\varepsilon\), where \(C\) depends only on \(r/R\). On a sufficiently large fixed root disk their polynomial values differ by at most \(C'\varepsilon\). Surround the three roots of the first polynomial by closed disks of radius \(t=(2C'\varepsilon)^{1/3}\), enlarging \(t\) infinitesimally if needed to avoid tangencies. On every component boundary of their union, the modulus of the first polynomial is at least \(t^3>C'\varepsilon\). Rouché's theorem, applied componentwise, puts exactly the same number of roots of each polynomial in each connected component. A component made from at most three disks has diameter at most \(6t\), so the roots can be matched with squared-root error at most \(6t\). Since all original and reconstructed sides are at least \(r\), taking square roots proves
\[
\boxed{\quad
\min_{\sigma\in S_3}\max_i|\ell_i-\ell'_{\sigma(i)}|
\le C_{r,R}R\varepsilon^{1/3}.\quad}\tag{5}
\]
The exponent is optimal. Fix \(\alpha=1\), let \(h=\delta\downarrow0\), and compare (3) at \(\theta=0\) and \(\theta=\pi/6\). Their first two moments coincide and their third moments differ by exactly \(\delta^3/840\), whereas the best matching side-length discrepancy is bounded above **and below** by positive constants times \(\delta\). Thus no uniformly valid inverse Hölder bound with exponent greater than \(1/3\) holds in any neighborhood of the equilateral triangle.

## Verification

Run `python verify_triangle_moments.py` with Python, SymPy, and NumPy installed. The checker expands the two independent reference-simplex samples exactly, integrates all monomials using rational factorial weights, and verifies (1) for every symbolic squared-side triple. It independently checks (2), an exact noncongruent collision and its sixth-moment gap, and evaluates moments by independent four-dimensional Gauss–Legendre quadrature on four specified nondegenerate triangles. A successful execution prints `VERIFY_OK`. The analytic proof establishes the continuum, optimality, and stability claims; finite quadrature alone cannot establish them.

## Relationship to prior work

Bäsel (arXiv:1208.6228, first publicly available August 30, 2012) derived complete point-distance distributions for right triangles. Tong and Pan (arXiv:1602.03407) derived arbitrary-triangle point-distance distributions. Reichenwallner (2017, DOI below), Proposition 4, provides a general formula for all order moments of distances between two independent area-uniform points in arbitrary triangles. **Forward moment computation and existence of all moments are known**; (1) is provided as the explicit low-order starting point, not asserted as independent novelty. The distinct claim here is a *complete sharp inverse* description of the feasible moment region and every fixed-two-moment fiber, including the exact isosceles extremizers of the sixth moment, a sharp minimal-moment cutoff, and the optimal cubic inverse-stability exponent. Gravin, Lasserre, Pasechnik and Robins (arXiv:1106.5723) study reconstruction from directional polynomial moments, which retain different data from the rotationally invariant pair-distance moments considered here. Closely related findings on geometric projection-width tomography, short-distance coefficients, and arbitrary-triangle second-moment comparisons concern different observables; their conclusions do not imply the stated sharp inverse fiber or stability classification without additional analysis.

## Limitations

The theorem concerns nondegenerate planar Euclidean triangles and independent area-uniform sampling. The stability constant depends on bounds excluding arbitrarily short or arbitrarily long sides. The theorem does not determine arbitrary polygons, address finite-sample statistical estimators, or give a statistical noise-rate theorem. Formula (5) is a deterministic inverse modulus. The source comparison does not establish definitive historical priority; earlier equivalent algebraic inverse statements remain possible, especially given known general forward-moment formulas. No independent validation or external mathematical audit has been performed.

## References

1. U. Bäsel, *The distribution function of the distance between two random points in a right-angled triangle*, arXiv:1208.6228 (2012), https://arxiv.org/abs/1208.6228.
2. F. Tong and J. Pan, *Random Distances Associated with Arbitrary Polygons: An Algorithmic Approach between Two Random Points*, arXiv:1602.03407 (2016), https://arxiv.org/abs/1602.03407.
3. B. Reichenwallner, *Moments of volumes of lower-dimensional random simplices are not monotone*, Monatshefte für Mathematik 186 (2018), 481–501, online June 21, 2017, https://doi.org/10.1007/s00605-017-1077-3; especially Proposition 4.
4. N. Gravin, J. B. Lasserre, D. V. Pasechnik and S. Robins, *The inverse moment problem for convex polytopes*, arXiv:1106.5723 (2011), https://arxiv.org/abs/1106.5723.
