# Sharp barycentric area profile of planar triangle intersection bodies

## Finding
Let \(T\subset\mathbb R^2\) be a nondegenerate triangle, and let \(z\) lie in its interior with positive barycentric coordinates \((a,b,c)\), \(a+b+c=1\). For the planar intersection body \(I(T-z)\), defined by its radial function
\[
\rho_{I(T-z)}(u)=\operatorname{length}\bigl((T-z)\cap u^\perp\bigr),\qquad |u|=1,
\]
the area ratio has the following exact, affine-invariant formula:
\[
\boxed{\frac{|I(T-z)|}{|T|}=2+4\sum_{t\in\{a,b,c\}}t(1-t)\log\frac{1-t}{t}.}
\]
On the open barycentric simplex, this ratio is strictly Schur-concave. Consequently,
\[
\boxed{2<\frac{|I(T-z)|}{|T|}\le 2+\frac83\log2,}
\]
with equality on the right if and only if \(z\) is the centroid of \(T\). The lower value \(2\) is the continuous boundary limit for every approach to any boundary point of the barycentric simplex; it is not attained by an interior center.

## Assumptions and scope
Areas are ordinary two-dimensional Lebesgue areas. All logarithms are natural. The point \(z\) is strictly interior; no assertion about the geometric intersection-body construction at a boundary-centered triangle is required. For a general invertible affine transformation \(x\mapsto Ax+d\), triangle area and intersection-body area both multiply by \(|\det A|\), so the ratio is affine-invariant in dimension two. This is a statement only for nondegenerate triangles in the Euclidean plane, not for arbitrary polygons or higher dimensions.

## Proof
**1. Affine normalization and area integral.** If \(A\) is invertible, then the planar intersection-body covariance is \(I(AK)=|\det A|A^{-T}I(K)\). Indeed, each central line section transforms by its one-dimensional Jacobian, and the cofactor relation in dimension two sends section normals by \(A^{-T}\). Taking areas gives \(|I(AK)|=|\det A|\,|I(K)|\). Translate \(z\) to the origin and apply such a map to put the three vertices at
\[
(1,0),\quad(0,1),\quad(-p,-q),\qquad p,q>0.
\]
Write \(S=1+p+q\). The normalized triangle has area \(S/2\), and the origin has barycentric coordinates \((p/S,q/S,1/S)\).

For each real slope \(m\), let \(d(m)\) denote the horizontal span of the chord formed by intersecting this triangle with the line \(y=mx\). Direct intersection of that line with the three sides gives
\[
d(m)=\begin{cases}
\displaystyle\frac{S(q-pm)}{[q-(p+1)m][q+1-pm]},&m<0,\\[5pt]
\displaystyle\frac{S}{(1+m)(q+1-pm)},&0\le m\le q/p,\\[5pt]
\displaystyle\frac{Sm}{(1+m)[(p+1)m-q]},&m>q/p.
\end{cases}
\]
At the dividing slopes the adjoining expressions agree. The chord length is \(\sqrt{1+m^2}\,d(m)\). The polar area formula for a centrally symmetric star body is one half the integral of squared radial length over the unit circle; identifying the two antipodal directions and substituting \(d\theta=dm/(1+m^2)\) yields precisely
\[
|I(T-z)|=\int_{-\infty}^{\infty}d(m)^2\,dm.
\]

**2. Exact integration.** Each interval is elementary. On the negative-slope interval substitute \(x=[q-(p+1)m]/[q+1-pm]\), with primitive (including the Jacobian and multiplicative factor)
\[
\frac1S\left(-\frac{q^2}{x}+2pq\log x+p^2x\right),
\]
evaluated from \(x=q/(q+1)\) to \(x=(p+1)/p\). For the middle interval substitute \(u=(1+m)/(q+1-pm)\), giving the primitive
\[
\frac1S\left(-\frac1u+2p\log u+p^2u\right),
\]
evaluated from \(u=1/(q+1)\) to \(u=(p+q)/p\). On the positive outer interval substitute \(m^{-1}\) and exchange \(p\) with \(q\); the corresponding limits are \(u=1/(p+1)\) to \(u=(p+q)/q\) and the same primitive with \(q\) in place of \(p\). Summing the rational endpoint contributions gives \(S\). Collecting the logarithms gives the exact total
\[
|I(T-z)|=S+\frac2S\left[pq\log\frac{(p+1)(q+1)}{pq}
+p\log\frac{(p+q)(q+1)}p+q\log\frac{(p+q)(p+1)}q\right].
\]
Substituting \(a=p/S\), \(b=q/S\), \(c=1/S\), dividing by \(S/2\), and collecting the coefficients of \(\log a\), \(\log b\), and \(\log c\), yields the stated barycentric formula. In particular, both the quantities and normalization are exact, with no numerical approximation.

**3. Strict Schur concavity and sharp bounds.** Define \(g(t)=t(1-t)\log((1-t)/t)\) for \(0<t<1\), extended by continuity with \(g(0)=g(1)=0\). Then
\[
g'(t)=(1-2t)\log\frac{1-t}{t}-1,\qquad
 g'(1-t)=g'(t),\qquad
 g''(t)=-2\log\frac{1-t}{t}-\frac{1-2t}{t(1-t)}<0\quad(0<t<\tfrac12).
\]
Take two distinct barycentric coordinates \(a>b>0\), with \(a+b<1\). When \(a\le 1/2\), the strict decrease of \(g'\) on \((0,1/2)\) gives \(g'(a)<g'(b)\). When \(a>1/2\), the inequalities \(b<1-a<1/2\), together with \(g'(a)=g'(1-a)\), give the same strict comparison. Therefore replacing any unequal pair of coordinates by a more equal pair, holding their sum fixed, strictly increases \(\sum g\). This proves strict Schur concavity throughout the open simplex, with the unique maximum at \((1/3,1/3,1/3)\).

At a boundary vector \((t,1-t,0)\), the extended sum is \(g(t)+g(1-t)+g(0)=0\). Every interior vector is reached by nontrivial averaging from a boundary vector; the preceding strict comparison therefore gives a positive sum in the interior. Finally \(3g(1/3)=2\log2/3\); substituting establishes both sharp inequalities and all equality or limiting cases.

## Verification
The accompanying standard-library script `verification.py` evaluates the independent chord-slope area integral numerically on seven normalizations, checks exact rational intersections for multiple slopes in each regime, verifies the barycentric identity against that integral, and stress-tests the sharp upper bound on a finite sample. These checks are diagnostics, not substitutes for the quantified analytic integration and strict-concavity proof above. Run `python verification.py` from the directory containing the two files.

## Relationship to prior work
Brandenburg and Meroni, *Intersection Bodies of Polytopes: Translations and Convexity* (initial arXiv release 2023-02-23), examine section polynomials, translations, and convexity, including the planar characterization of convex intersection bodies; those results motivate asking for an exact translation-sensitive area functional. Brandenburg, Berlow, Meroni, and Shankar, *Intersection Bodies of Polytopes* (2021), develop the semialgebraic section framework. Neither inspected treatment states this complete barycentric triangle area profile or its sharp centroid extremum. The present result concerns **area of the star body**, not the triangular floating body, a centrally symmetric core, or convexity of the intersection body. A general intersection-body volume inequality does not immediately entail the present triangle-only sharp constant or equality classification.

## Limitations
An independent mathematical audit has not been performed. The literature comparison covers identified primary sources and targeted searches but does not establish absolute publication priority; an older chordal-symmetral calculation might be equivalent. The barycentric profile is for strictly interior centers; the lower boundary value is a limit, not a claim about the boundary-centered section construction. Finite numerical tests cannot establish universal validity.

## References
1. M.-C. Brandenburg and C. Meroni, *Intersection Bodies of Polytopes: Translations and Convexity*, arXiv:2302.11764v1 (2023), doi:10.48550/arXiv.2302.11764.
2. K. Berlow, M.-C. Brandenburg, C. Meroni, and I. Shankar, *Intersection Bodies of Polytopes*, arXiv:2110.05996 (2021).
