# Exact axis-shift profile and strict monotonicity of random hypercube section vertices

## Finding
Let \(n\ge3\) be an integer, \(Q_n=[-1,1]^n\), and \(U\) be uniform on the Euclidean unit sphere \(S^{n-1}\). For \(0\le t\le1\), intersect the cube with the random hyperplane
\[
H_t(U)=\{z\in\mathbb R^n:\langle U,z\rangle=tU_1\}.
\]
Let \(F_n(t)=\mathbb E f_0(Q_n\cap H_t(U))\), where \(f_0\) counts vertices. Define
\[
r_n=\sqrt{n-1},\qquad \phi_n(v)=\arctan\frac1{\sqrt{n-2+v^2}}.
\]
Then the *complete axial shift profile* is
\[
F_n(t)=\frac{2^{n-1}}\pi\left[\arctan\frac{1-t}{r_n}+\arctan\frac{1+t}{r_n}+(n-1)\bigl(\phi_n(1-t)+\phi_n(1+t)\bigr)\right]. \tag{1}
\]
For every \(n\ge3\), this function is **strictly decreasing** on \([0,1]\), so its unique maximum occurs at the central section. At the center,
\[
F_n(0)=\frac{2^n n}{\pi}\arcsin\frac1{\sqrt n}.
\]
The exact quadratic departure is
\[
F_n(0)-F_n(t)=\frac{2^{n-1}}\pi\frac{n-2}{n\sqrt{n-1}}t^2+O_n(t^4)\quad(t\to0),\tag{2}
\]
and, uniformly for \(0\le t\le1\),
\[
\frac{\pi\sqrt n}{2^{n-1}}\bigl(F_n(0)-F_n(t)\bigr)=t^2+O(n^{-1})\quad(n\to\infty).\tag{3}
\]
The two-dimensional exception is exact: the analogous expectation is identically \(2\) for every interior shift along a coordinate axis, since a generic section of a square is a line segment.

## Assumptions and scope
The hyperplane is Haar-uniform in orientation **conditional on containing the fixed point** \(te_1\), not uniformly sampled by signed offset among all affine hyperplanes. Side length is normalized to \(2\). The range \(0\le t\le1\) joins the center to the center of one facet. All face incidences are interpreted almost surely, excluding the measure-zero set of hyperplanes passing through cube vertices or containing cube edges. The formula extends at \(t=1\) by direct continuity; almost every section still meets a generic collection of edges transversely.

## Proof
**Edge-angle probability.** Almost surely, every vertex of the \((n-1)\)-dimensional section lies in the relative interior of exactly one original cube edge. For an edge with endpoints \(v,w\), its intersection probability is
\[
\mathbb P\bigl(\langle U,v-te_1\rangle\langle U,w-te_1\rangle<0\bigr)=\frac1\pi\angle(v-te_1,w-te_1),\tag{4}
\]
by rotational invariance in their two-dimensional span. Summing (4) over all edges and grouping by coordinate direction gives (1). In the first coordinate direction there are \(2^{n-1}\) congruent edge-angle terms, each
\[
A_n(t)=\arctan\frac{1-t}{\sqrt{n-1}}+\arctan\frac{1+t}{\sqrt{n-1}}.
\]
In each of the remaining \(n-1\) directions there are \(2^{n-2}\) edges with fixed first coordinate \(+1\), and the same number with \(-1\). Their angles are, respectively, \(2\phi_n(1-t)\) and \(2\phi_n(1+t)\). This yields (1), with no independence assertion between different edge intersections. At zero, \(\phi_n(1)=\arcsin(1/\sqrt n)\), giving the stated central value.

**Strict monotonicity when \(n\ge4\).** Put \(c=n-2\ge2\), and write \(\phi(v)=\arctan(1/\sqrt{c+v^2})\) for \(v\ge0\). Then
\[
\phi'(v)=-h_c(v),\qquad h_c(v)=\frac{v}{\sqrt{c+v^2}(c+v^2+1)}.
\]
The derivative of \(\phi(1-t)+\phi(1+t)\) equals \(h_c(1-t)-h_c(1+t)\). Both arguments are nonnegative, and clearing positive factors in the comparison of their squares shows
\[
h_c(1+t)^2>h_c(1-t)^2
\quad\Longleftrightarrow\quad
4t B_c(t)>0,\quad(t>0),
\]
where
\[
B_c(t)=c^3+2c^2-2c-4+(6c+6)t^2-3ct^4-2t^6.
\]
Since \(0<t\le1\),
\[
B_c(t)\ge c^3+2c^2-2c-4+(3c+4)t^2>0\quad(c\ge2).
\]
Also
\[
A_n'(t)=-\frac{4\sqrt{n-1}\,t}{(n+t^2)^2-4t^2}<0.
\]
Thus every summand in (1) strictly decreases for \(0<t<1\).

**The three-dimensional endpoint.** For \(n=3\) let \(\phi(v)=\arctan(1/\sqrt{1+v^2})\). Direct differentiation gives, with \(z=v^2\),
\[
\phi''(v)=\frac{2z^2+z-2}{(1+z)^{3/2}(2+z)^2}\le\frac19\qquad(v\ge0).\tag{5}
\]
Here is a purely algebraic bound for (5). For \(z\le3/4\), its numerator is nonpositive; for \(3/4\le z\le1\), the numerator is at most \(1\) and the denominator exceeds \(9\). For \(z\ge1\), after squaring the desired inequality (only where its numerator is positive), it suffices that
\[
P(z)=(1+z)^3(2+z)^4-81(2z^2+z-2)^2\ge0.
\]
For \(1\le z\le2\), letting \(w=z-1\in[0,1]\) gives
\[
P(w+1)=w^7+18w^6+138w^5+260w^4-147w^3-135w^2+1026w+567>0,
\]
because \(1026w-147w^3-135w^2\ge744w\). For \(z\ge2\), the polynomial \(P(w+2)\) has strictly positive coefficients (in descending order \(1,25,267,1255,2668,2655,2160,1728\)); hence (5). Therefore
\[
\frac{d}{dt}\,2\bigl(\phi(1-t)+\phi(1+t)\bigr)
=2\int_{1-t}^{1+t}\phi''(v)\,dv\le\frac{4t}{9}.
\]
But \(A_3'(t)=-4\sqrt2\,t/((3+t^2)^2-4t^2)\le-\sqrt2\,t/3\), since the denominator is at most \(12\) on \([0,1]\). As \(\sqrt2/3>4/9\), the total derivative in (1) is strictly negative. This completes strict monotonicity for all \(n\ge3\).

**Quadratic and high-dimensional coefficients.** Twice differentiating (1) at zero gives
\[
F_n''(0)=-\frac{2^{n-1}}\pi\frac{2(n-2)}{n\sqrt{n-1}},
\]
so Taylor's theorem and evenness in \(t\) prove (2). Uniformly for \(v\in[0,2]\),
\[
\phi_n(v)=n^{-1/2}-\left(\frac{v^2-2}{2}+\frac13\right)n^{-3/2}+O(n^{-5/2}).
\]
Consequently \((n-1)(2\phi_n(1)-\phi_n(1-t)-\phi_n(1+t))=t^2n^{-1/2}+O(n^{-3/2})\) uniformly \(0\le t\le1\), while \(A_n(0)-A_n(t)=O(n^{-3/2})\). Substitution in (1) yields (3).

## Verification
Run `python check.py` from the embedded package. The script independently sums Euclidean edge angles, simulates Gaussian normal directions and counts edge crossings without using the closed formula, checks monotonicity on sampled parameters, and checks the high-dimensional normalization. It reports 2477 successful deterministic assertions on the saved run. These finite computations do not prove the all-real or all-dimension statements; the preceding algebra does.

## Relationship to prior work
Schange, *Solid-Angle Formulas for Simplicial Cones and Random Shifted Sections of Polytopes* (arXiv:2610.28084v1, first public 2026-10-20) derives shifted-face expectations for acute orthocentric simplices and (a)symmetric crosspolytopes, while citing the earlier **central** cube computations of Kabluchko and Seidel. The present theorem treats a noncentral hypercube family not listed in those stated applications. Kabluchko and Seidel, *Convex cones spanned by regular polytopes* (arXiv:2006.09492), covers central random sections. Lonke's *On Random Sections of the Cube* treats random linear sections. Prior same-object mathematical records concern **central** sections or different projection invariants. Formula (1), strict axial displacement monotonicity, exact quadratic stability, and uniform normalized deficit form one connected result; central values and edge-angle/Crofton methods are not claimed as new.

## Limitations
This does not classify arbitrary translations in the full cube, other codimensions, higher face-number distributions, or arbitrary sampling measures on affine hyperplanes. The uniqueness of the maximum is along the specified coordinate axis only, not a global optimizer claim. Historical priority may be affected by inaccessible or unindexed treatments of noncentral cube sections. There has been no independent mathematical audit.

## References
1. Philipp Schange, *Solid-Angle Formulas for Simplicial Cones and Random Shifted Sections of Polytopes*, arXiv:2610.28084v1, 2026-10-20, https://arxiv.org/html/2610.28084v1 .
2. Zakhar Kabluchko and Hauke Seidel, *Convex cones spanned by regular polytopes*, arXiv:2006.09492, https://arxiv.org/abs/2006.09492 .
3. Yossi Lonke, *On Random Sections of the Cube*, Discrete & Computational Geometry 23 (2000), 157–169, doi:10.1007/PL00009493.
4. Hunter Swan, *Expected Number of Vertices of a Hypercube Slice*, American Mathematical Monthly 123 (2016), 600–604; arXiv:1808.09482 (alternate preprint).
