# Hyperbolic curvature paths and quantitative triangle rigidity

## Finding
Let \(K\subset\mathbb R^2\) be a compact convex body with nonempty interior and let \(B\) be the Euclidean unit disk. Its **outer-parallel centroid path** is \(\gamma_K(t)=\operatorname{centroid}(K+tB)\), \(t\ge0\), with endpoint \(\gamma_K(\infty)=\lim_{t\to\infty}\gamma_K(t)\). Write \(A=|K|>0\), \(L=\operatorname{per}(K)>0\); denote its area centroid by \(G\), perimeter centroid by \(H\), and curvature-weighted Steiner point by \(S\).

**One classification theorem.** If \(G,H,S\) are not collinear, the entire path is an injective, strictly curved segment of a **nondegenerate hyperbola**, with no inflection, connecting \(G\) to \(S\) and having endpoint tangent lines parallel to \(GH\) and \(HS\). In barycentric coordinates \((\lambda_G,\lambda_H,\lambda_S)\) relative to the three centers, it is precisely the positive arc of
\[
\lambda_H^2=\frac{L^2}{A\pi}\lambda_G\lambda_S,
\qquad\lambda_G+\lambda_H+\lambda_S=1.
\]
Its signed curvature determinant has the exact sign-and-size identity
\[
\det\!\bigl(\gamma_K'(t),\gamma_K''(t)\bigr)
=\frac{2AL\pi\,\det(H-G,S-G)}{(A+Lt+\pi t^2)^3}.
\]
When the three centers are collinear, the path instead lies on their common line (or is constant).

For every nondegenerate Euclidean triangle \(T\), the **nondegenerate hyperbola case occurs if and only if the triangle is scalene**. Every non-equilateral isosceles triangle has a straight, injective, strictly monotone centroid path on its symmetry axis, whereas an equilateral triangle has a constant path. More quantitatively, for a counterclockwise triangle with area \(A\), perimeter \(L\), circumradius \(R\), and angles \(\alpha_1,\alpha_2,\alpha_3\in(0,\pi)\),
\[
\left|\det(H-G,S-G)\right|
\ge \frac{AR\min_i\sin\alpha_i}{6L\pi}
\left|(\alpha_1-\alpha_2)(\alpha_2-\alpha_3)(\alpha_3-\alpha_1)\right|.
\]
The right-hand side is strictly positive for a scalene triangle. Thus its three-center noncollinearity is quantitatively controlled by the pairwise angle gaps.

## Assumptions and scope
All distances, perimeters, Minkowski sums, centroids, and curvatures use the **Euclidean** structure. \(H=L^{-1}\int_{\partial K}x\,d\mathcal H^1(x)\). The point \(S\) is the *Steiner curvature centroid*, not a distinct triangle-center convention sometimes also called a Steiner point: for a polygon with counterclockwise vertices \(v_i\), interior angles \(\alpha_i\), and exterior turning angles \(\theta_i=\pi-\alpha_i\),
\[
S=\frac1{2\pi}\sum_i\theta_i v_i.
\]
For a general convex body, this is the continuous extension under convex-body approximation (equivalently its first curvature moment). Barycentric coordinates of \(\gamma_K(t)\) refer to the affine triangle formed by \(G,H,S\), **not** the vertices of \(K\). An injective curved path means \(t\mapsto\gamma_K(t)\) injective for \(0\le t\le\infty\). The result is restricted to dimension two and does not assert that arbitrary collinear-center bodies have monotone paths.

## Proof
**1. Exact moment polynomial.** The classical planar Steiner area formula gives \(|K+tB|=q(t)=A+Lt+\pi t^2\). For a convex polygon, partition the added material into outward edge strips and circular vertex sectors. Each edge strip of length \(\ell\) contributes \(t\ell\) times its midpoint plus the vector \((t^2/2)\ell n\) in its outward-normal direction \(n\); the latter vectors sum to zero because \(\sum\ell n=0\). A sector of exterior angle \(\theta_i\) at \(v_i\) contributes first moment \((t^2/2)\theta_i v_i\) and a radial third-order term \((t^3/3)\int_{I_i}n(\phi)\,d\phi\). The normal arcs \(I_i\) partition the full circle up to finitely many points, so these radial terms sum to zero. Consequently
\[
\int_{K+tB}x\,dx=AG+LtH+\pi t^2S.
\]
Approximation by convex polygons, convergence of perimeters and first moments, and continuity of the Steiner point extend this identity to every planar convex body with interior. Hence
\[
\boxed{\gamma_K(t)=\frac{AG+LtH+\pi t^2S}{A+Lt+\pi t^2}}.\tag{1}
\]
This identity itself is a specialization of the **already established** curvature-centroid Steiner formula; originality is **not** claimed for (1).

**2. Hyperbola and curvature.** Suppose \(G,H,S\) are noncollinear. Equation (1) yields barycentric weights \(\lambda_G=A/q\), \(\lambda_H=Lt/q\), and \(\lambda_S=\pi t^2/q\), which imply the displayed quadratic equation. Put \(u=\lambda_H\), \(v=\lambda_S\), and \(k=L^2/(A\pi)\). The equation becomes \(u^2+kuv+kv^2-kv=0\). Its quadratic-part discriminant equals \(k(k-4)>0\): the strict planar isoperimetric inequality \(L^2>4\pi A\) applies because the disk has coincident centers. The conic is nondegenerate because its full homogeneous equation \(\lambda_H^2-k\lambda_G\lambda_S=0\) has nonzero determinant when \(k>0\). Its nonnegative barycentric arc is traced once: \(\lambda_H/\lambda_G=Lt/A\) is strictly increasing for finite \(t\). Differentiating (1) twice and expanding the two-by-two determinant yields the displayed identity, whose right-hand side never vanishes and has fixed sign. Differentiating at zero gives a tangent parallel to \(H-G\), while expansion in \(1/t\) at infinity gives a tangent parallel to \(S-H\).

**3. Which triangles degenerate?** For a triangle with vertices \(v_i\), opposite side lengths \(a_i\), and interior angles \(\alpha_i\), the three center vectors have vertex-barycentric weights
\[
G:\left(\frac13\right)_i,\qquad
H:\left(\frac{L-a_i}{2L}\right)_i,\qquad
S:\left(\frac{\pi-\alpha_i}{2\pi}\right)_i.
\]
Since counterclockwise barycentric coordinate determinants are multiplied by \(2A\) in physical coordinates, an exact computation gives
\[
\det(H-G,S-G)
=\frac{A}{6L\pi}\det\begin{pmatrix}
1&a_1&\alpha_1\\
1&a_2&\alpha_2\\
1&a_3&\alpha_3
\end{pmatrix}.
\tag{2}
\]
The sine rule \(a_i=2R\sin\alpha_i\) converts (2) into \((AR/(3L\pi))\det(1,\sin\alpha_i,\alpha_i)\). Three points on the strictly concave graph of \(\sin x\) over \((0,\pi)\) cannot be collinear when their abscissae are pairwise distinct. Thus three distinct angles imply \(G,H,S\) noncollinear. Conversely, if any two angles coincide, reflection across the triangle's symmetry axis fixes all three centers, making them collinear. Equal angles are equivalent to equal opposing sides, which gives exactly the claimed scalene/isosceles classification.

**4. Quantitative triangular nonflatness.** For three distinct arguments \(x_1,x_2,x_3\), the determinant of the columns \(1,x,\sin x\) is the Vandermonde factor \(\prod_{i<j}(x_j-x_i)\) times the second divided difference of \(\sin\). The Hermite–Genocchi integral formula expresses this divided difference as an integral of \(-\sin(s_1x_1+s_2x_2+s_3x_3)\) over the standard two-simplex of area \(1/2\). Because sine is concave and positive on \((0,\pi)\), the integrand's absolute value is at least \(\min_i\sin x_i\). Hence the absolute divided difference is at least \(\min_i\sin x_i/2\). Insert this bound into (2) and the sine rule to obtain the stated nonflatness inequality. Repeated-angle cases follow by continuity with zero right-hand side.

**5. Monotonicity of isosceles paths.** Let \(\theta\) be the apex angle and normalize the equal legs to unit length. The barycentric weights at the apex of \(G,H,S\) are, respectively,
\[
\frac13,\qquad\frac1{2+2\sin(\theta/2)},\qquad\frac{\pi-\theta}{2\pi}.
\]
The strict concavity of \(f(\theta)=(\pi-\theta)\sin(\theta/2)-\theta\), which vanishes at \(\theta=0\) and \(\theta=\pi/3\), shows that these three apex coordinates are strictly increasing for \(0<\theta<\pi/3\) and strictly decreasing for \(\pi/3<\theta<\pi\). All points lie on the same axis. Differentiation of (1) gives
\[
q(t)^2\gamma_K'(t)=AL(H-G)+2A\pi t(S-G)+L\pi t^2(S-H).
\]
The three vectors on the right point strictly in the same axial direction if \(\theta\ne\pi/3\), proving injective strict monotonicity. At \(\theta=\pi/3\), the three centers coincide, so the path is constant.

## Verification
The accompanying standard-library Python program `verify.py` independently integrates the mass moments of polygonal outer-parallel bodies using disjoint edge rectangles and vertex sectors; compares these to formula (1) at 875 polygon/offset combinations; checks the exact curvature determinant formula; samples 278 scalene triangle instances with separated angles; and checks monotonicity on eight isosceles apex-angle configurations. Numerical tests are *regression checks, not proofs*. The universal arguments above provide the infinite-domain proof.

## Relationship to prior work
The 2021 paper by Gollapudi, Guruganesh, Kollias, Manurangsi, Paes Leme, and Schneider provides the general curvature-centroid rational formula and uses curvature paths for geometric algorithms. Equation (1), rationality, and the existence of the three curvature centers are therefore **prior knowledge**. Chen's 2020 article identifies the exterior-angle mass centroid and develops Steiner-center theory; that definition is likewise **prior knowledge**. The contribution assessed here is the geometric **hyperbola/line dichotomy**, its signed noninflection identity, and especially the **complete angle-based triangle rigidity and quantitative nonflatness bound**, with monotone straight-path behavior at the precise isosceles degeneracy. The source's general formula by itself does not state these geometric and angular classifications. Prior mathematical implications and remaining priority uncertainty are discussed in `REVIEW.md` and `AUDIT.json`.

## Limitations
No classification of all planar convex bodies with collinear \(G,H,S\) is asserted. The bound on triangular noncollinearity is explicit and strictly positive for scalene triangles, but global sharpness over triangles is not claimed. An earlier source might contain an equivalent geometric classification, including as a corollary of other center-geometry results. Independent audit, external verification, and publication-priority certification have not been performed.

## References
- S. Gollapudi, G. Guruganesh, K. Kollias, P. Manurangsi, R. Paes Leme, and J. Schneider, *Contextual Recommendations and Low-Regret Cutting-Plane Algorithms*, arXiv:2106.04819v1, submitted June 9, 2021. Section 5.1, equation (9). https://arxiv.org/abs/2106.04819
- B.-Y. Chen, *g-Steiner, co-Steiner and Normal Points of Bounded Euclidean Submanifolds*, International Electronic Journal of Geometry **13** (2020), 1–10, publicly listed October 15, 2020; doi:10.36890/iejg.689803. https://dergipark.org.tr/en/pub/iejg/article/689803
