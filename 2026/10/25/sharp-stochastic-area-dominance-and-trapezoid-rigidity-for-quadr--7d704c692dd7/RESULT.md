# Sharp stochastic area dominance and trapezoid rigidity for quadrilateral inellipses

## Finding
Let \(Q\) be a strictly convex quadrilateral in the Euclidean plane, excluding parallelograms. Write \(J\) for the segment joining the two diagonal midpoints. For each point \(c\) in the relative interior of \(J\), there is a unique ellipse \(E_c\) tangent to all four sides and centered at \(c\). If \(C\) is uniform along \(J\), define the normalized area
\[
B_Q=\frac{\operatorname{Area}(E_C)}{\max_{c\in J}\operatorname{Area}(E_c)}.
\]
Then for every \(0<u<1\),
\[
\boxed{\Pr(B_Q>u)\le\sqrt{1-u^2}.}
\]
Equality at **one** interior threshold is equivalent to \(Q\) being a trapezoid. For every nontrapezoid the inequality is strict for **every** interior threshold. For trapezoids the exact distribution is
\[
\Pr(B_Q\le u)=1-\sqrt{1-u^2},\qquad 0\le u\le1.
\]
Consequently, for every \(p>0\),
\[
\mathbb E B_Q^p\le \frac{\sqrt\pi\,\Gamma(1+p/2)}{2\Gamma(3/2+p/2)},
\]
with equality precisely for trapezoids. In particular the sharp second-moment bound is \(\mathbb E B_Q^2\le2/3\); the equality class is the entire family of genuine trapezoids, independent of aspect ratio.

## Assumptions and scope
Here *inscribed ellipse* means a positive-area ellipse contained in \(Q\) and tangent to all four sides. A *trapezoid* means a quadrilateral with at least one pair of opposite sides parallel; parallelograms are excluded because their two diagonal midpoints coincide and there is no positive-length center segment on which to sample. The measure is normalized Euclidean length along the straight segment \(J\), not the area measure inside \(Q\) or a random choice of tangent points. Any nonsingular affine map restricts to a constant length rescaling along \(J\), so the uniform-center law and normalized ellipse areas are affine invariant. Endpoints have probability zero; their limiting degenerate ellipses have area zero.

## Proof
**1. Reduction to a cubic density.** The ellipse-center theorem of Horwitz [1] gives one and only one four-side-tangent inellipse for each interior point of \(J\). For a nontrapezoid, the standard affine normalization and area identity of Horwitz [2, Eq. (5)] give, after writing the center parameter as \(z\in(0,1)\),
\[
\operatorname{Area}(E_z)^2=\frac{\pi^2}{4}z(1-z)[a+bz],\quad
 a=s+t-1>0,\quad a+b=st>0,\quad b=(s-1)(t-1)\ne0.
\]
Here the normalized quadrilateral vertices are \((0,0),(1,0),(0,1),(s,t)\), with the choice of vertex order made as in [2]; a reflection or reversal of \(J\) may change the sign of the slope but cannot make it zero. The formula is a known input from [2], not claimed as new. Under \(x=2z-1\), uniform arclength is uniform \(x\in(-1,1)\) and the normalized squared-area *profile before dividing by its maximum* is proportional to
\[
f_q(x)=(1-x^2)(1+qx),\qquad q=\frac{b}{2a+b}\in(-1,1)\setminus\{0\}.
\]
For trapezoids one obtains this same profile with \(q=0\) by the direct calculation in Step 3. Replacing \(x\) by \(-x\) allows us to assume \(q\ge0\).

**2. Sharp distributional comparison.** Let \(M_q=\max_{[-1,1]}f_q\). The positive factors in \(f_q\) have strictly concave logarithms on \((-1,1)\), so \(f_q\) is strictly unimodal. For any \(0<\lambda<M_q\), its superlevel set is one interval \([c-h,c+h]\) with \(0<h<1\), and
\[
f_q(c-h)=f_q(c+h)=\lambda.
\]
When \(q>0\), the midpoint satisfies \(c>0\): indeed \(f_q(x)>f_q(-x)\) for positive \(x\), and the superlevel interval has its right endpoint farther from the origin than its left endpoint. (This also follows directly by checking that \(f_q\) increases strictly on \((-1,0]\).) Expanding the two equal endpoint values, with no approximation,
\[
\lambda=f_q(c)-h^2(1+3qc),
\]
and therefore
\[
(1-h^2)f_q(c)-\lambda
 =h^2\{1+3qc-f_q(c)\}
 =h^2(c^2+2qc+qc^3)>0.
\]
Since \(f_q(c)\le M_q\), it follows that \(\lambda<(1-h^2)M_q\), hence \(h<\sqrt{1-\lambda/M_q}\). The uniform measure of the superlevel interval is exactly its half-length \(h\). Put \(\lambda=u^2M_q\) to obtain \(\Pr(B_Q>u)<\sqrt{1-u^2}\) for nontrapezoids. When \(q=0\), the superlevel interval is symmetric with half-length \(\sqrt{1-u^2}\), so equality holds at every threshold.

**3. Trapezoid profile and equality class.** By an invertible affine transformation and, if needed, exchanging its parallel bases, every genuine trapezoid has vertices \((-1,0),(1,0),(-r,1),(r,1)\) for some \(0<r<1\). Set \(k=1-r\). The center segment has coordinates \((c,1/2)\) with \(-k/2<c<k/2\). An inellipse written as \(\{y:(y-m)^TQ^{-1}(y-m)\le1\}\), with center \(m=(c,1/2)\) and positive-definite shape matrix \(Q\), touches both horizontal bases exactly when \(Q_{22}=1/4\). Tangency to the two slanted sides gives
\[
Q_{12}=-\frac{(1+r)c}{2k},\qquad
Q_{11}=r+c^2,
\]
where the latter identity uses \(((1+r)/2)^2-k^2/4=r\). Therefore
\[
\det Q=\frac r4\left(1-\frac{4c^2}{k^2}\right),\qquad
\frac{\operatorname{Area}(E_c)^2}{\max\operatorname{Area}(E)^2}
=1-\frac{4c^2}{k^2}.
\]
Thus the uniform coordinate \(x=2c/k\in(-1,1)\) gives \(B_Q=\sqrt{1-x^2}\), establishing the exact trapezoid CDF. Conversely, for a nontrapezoid \(b\ne0\) in Step 1, so \(q\ne0\), and Step 2 proves strictness at every interior threshold.

**4. Moment consequences.** Stochastic dominance of the nonnegative variables proves the moment statement for all \(p>0\), with strictness for nontrapezoids. The trapezoid integral is
\[
\int_0^1(1-x^2)^{p/2}\,dx
=\frac{\sqrt\pi\,\Gamma(1+p/2)}{2\Gamma(3/2+p/2)}.
\]
This completes the proof.

## Verification
The polynomial endpoint identity in Step 2 is exact and can be checked by expansion. The trapezoid formula follows from the standard support-function tangency conditions \(n\cdot m+\sqrt{n^TQn}=h_Q(n)\). Numerical or finite grids are **not** used to infer the theorem. An optional standalone script, `CHECK.py`, evaluates the algebraic identities symbolically when SymPy is installed and tests finitely many thresholds as supplementary diagnostics.

## Relationship to prior work
Horwitz [1] proved uniqueness of the inscribed ellipse at every point of the diagonal-midpoint segment; Horwitz [2] supplied the explicit cubic area profile used as an input here. Hayes [3] studied particular quadrilateral inellipse families and maximal area. Those works are substantially stronger concerning the **individual inellipse area function** than a mere existence statement; the new result is the *cross-quadrilateral sharp stochastic comparison*, including strict ordering at every threshold and equality characterization. This comparison requires the additional superlevel-midpoint inequality proved above and is not presented as a new formula for the underlying ellipse family. Searches for the probabilistic comparison and its affine-equivalent formulations did not identify a direct earlier theorem; this is bibliographic evidence, not proof of uniqueness.

## Limitations
Parallelograms have a collapsed center segment and are outside the sampling model. The theorem applies only to the canonical uniform-center measure, not uniformly sampled tangent points, perimeter-uniform ellipse points, or arbitrary area-weighted distributions on inellipses. The proof depends on the published Horwitz cubic identity. A 2024 monograph devoted to quadrilateral inellipses was not available in full text and may contain a related comparison; independent external validation has not been performed.

## References
[1] Alan Horwitz, *The locus of centers of ellipses inscribed in quadrilaterals*, arXiv:math/0312403 (first public 2003-12-22), https://arxiv.org/abs/math/0312403.

[2] Alan Horwitz, *An Area Inequality for Ellipses Inscribed in Quadrilaterals*, arXiv:0907.1647 (first public 2009-07-09), https://arxiv.org/abs/0907.1647; *Journal of Mathematical Inequalities* **4** (2010), 431–443, especially Eq. (5).

[3] M. J. D. Hayes, *Maximum Area Ellipses Inscribing Specific Quadrilaterals* (2016), open manuscript inspected for comparisons.
