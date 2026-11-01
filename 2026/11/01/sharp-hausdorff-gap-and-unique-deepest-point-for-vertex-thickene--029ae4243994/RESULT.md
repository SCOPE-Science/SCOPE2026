# Sharp Hausdorff gap and unique deepest point for vertex-thickened regular simplices

## Finding

Let \(P\subset\mathbb R^d\) be a regular, nondegenerate Euclidean simplex with vertices \(v_0,\ldots,v_d\), edge length \(\ell>0\), and finite vertex set \(V=\{v_0,\ldots,v_d\}\). For every real \(\lambda\ge0\), define the finite union of homothetic simplices
\[
A_\lambda=V+\lambda P=\bigcup_{i=0}^{d}(v_i+\lambda P).
\]
Its convex hull is \((1+\lambda)P\). The exact Euclidean Hausdorff distance is
\[
\boxed{d_H\bigl(A_\lambda,(1+\lambda)P\bigr)=\frac{\ell\,(d-\lambda)_+}{\sqrt{2d(d+1)}}.}
\]
Here \((t)_+=\max\{t,0\}\). For \(0\le\lambda<d\), **only the centroid of the enlarged simplex** maximizes the Euclidean distance to \(A_\lambda\). At \(\lambda=d\) the gap vanishes, and at every larger parameter the two sets coincide.

There is an explicit strict stability envelope. For a point \(z=\sum_i x_i v_i\in(1+\lambda)P\) represented by scaled barycentric coordinates with \(x_i\ge0\) and \(\sum_i x_i=s=1+\lambda\), write \(m=\max_i x_i\). Whenever \(m<1\),
\[
\operatorname{dist}(z,A_\lambda)^2\le \frac{\ell^2}{2}\frac{s(1-m)^2}{s-m}.
\]
For fixed \(\lambda\ge0\), this upper envelope is strictly decreasing in \(m\) wherever defined. In particular, points whose largest barycentric coordinate is bounded away from \(s/(d+1)\) have a strictly smaller squared distance to the union than its unique deepest point does.

## Assumptions and scope

The ambient norm is Euclidean and \(d\) is an integer at least two; the parameter \(\lambda\) is any real number at least zero. Both operations use the same ambient origin: \(\lambda P=\{\lambda p:p\in P\}\) and \((1+\lambda)P=\{(1+\lambda)p:p\in P\}\). The result is independent of a simultaneous translation of the original vertices because both the union and its convex hull undergo the same translation scaled by \(1+\lambda\). No centeredness assumption on \(P\) is needed. The uniqueness statement applies only when the gap is strictly positive; for \(\lambda\ge d\) all points have zero distance.

## Proof

**1. Barycentric caps.** Put \(n=d+1\) and \(s=1+\lambda\). Every \(z\in sP\) has a unique representation \(z=\sum_{i=1}^{n}x_i v_i\) with \(x_i\ge0\), \(\sum_i x_i=s\). The translate \(v_i+\lambda P\) is precisely the part of \(sP\) where \(x_i\ge1\). Indeed, \(z-v_i\in\lambda P\) is equivalent to the nonnegative coefficient vector \(x-e_i\) having total mass \(\lambda\). Consequently,
\[
A_\lambda=\bigl\{z\in sP:\max_i x_i\ge1\bigr\}.
\]
Since \(n\) nonnegative numbers of total mass \(s\) have maximum at least \(s/n\), we obtain \(A_\lambda=sP\) whenever \(s\ge n\), equivalently \(\lambda\ge d\). For \(s<n\), the centroid has all coordinates \(s/n<1\), hence is not in the union, proving strict nonconvexity.

**2. Euclidean normalization.** For any coefficients \(a_i\) satisfying \(\sum_i a_i=0\), regular-simplex geometry gives
\[
\left\|\sum_i a_i v_i\right\|^2=\frac{\ell^2}{2}\sum_i a_i^2.
\]
To verify this, subtract the simplex centroid from every vertex. The resulting centered Gram matrix has diagonal \(\ell^2d/[2(d+1)]\) and all off-diagonal entries \(-\ell^2/[2(d+1)]\). Substitution and \(\sum_i a_i=0\) yield the displayed identity. Thus Euclidean distances inside \(sP\) are exactly \(\ell/\sqrt2\) times the \(\ell_2\) distances of their barycentric coefficient vectors.

**3. Pointwise upper bound.** Consider \(z\in sP\) with \(m=\max_i x_i<1\); otherwise \(z\in A_\lambda\) and its distance is zero. Choose an index \(i\) with \(x_i=m\). Since \(s\ge1\), the segment from \(x\) to \(s e_i\) meets the cap \(x_i=1\) at
\[
y=x+\theta(se_i-x),\qquad \theta=\frac{1-m}{s-m}.
\]
The vector \(y\) has nonnegative entries, sum \(s\), and \(y_i=1\), so it corresponds to a point of \(A_\lambda\). Its squared coefficient distance is
\[
\begin{aligned}
\|x-y\|_2^2
&=(1-m)^2\left(1+\frac{\sum_{j\ne i}x_j^2}{(s-m)^2}\right)\\
&\le (1-m)^2\left(1+\frac{m(s-m)}{(s-m)^2}\right)
=\frac{s(1-m)^2}{s-m},
\end{aligned}
\]
because \(0\le x_j\le m\) implies \(\sum_{j\ne i}x_j^2\le m\sum_{j\ne i}x_j=m(s-m)\). Restoring the Euclidean scale proves the pointwise envelope.

**4. Strict global optimum.** The largest coordinate satisfies \(m\ge s/n\). For fixed \(s\ge1\), define \(g_s(m)=s(1-m)^2/(s-m)\) on \(s/n\le m<1\). Direct differentiation gives
\[
g_s'(m)=\frac{s(1-m)(m+1-2s)}{(s-m)^2}<0,
\]
because \(s\ge1\) and \(m<1\). Hence
\[
\operatorname{dist}(z,A_\lambda)^2\le\frac{\ell^2}{2}g_s(s/n)
=\frac{\ell^2}{2}\frac{(n-s)^2}{n(n-1)}.
\]
If \(m>s/n\), strict monotonicity makes this inequality strict. The only vector with \(m=s/n\) is the constant vector \(x_i=s/n\) for all \(i\), giving the centroid. This proves that the centroid is the only possible maximizer when \(s<n\).

**5. Sharp attainment at the centroid.** At the constant coefficient vector \(x=(s/n,\ldots,s/n)\), the closest point in any fixed cap \(C_i=\{y\ge0:\sum_j y_j=s,\ y_i\ge1\}\) has coefficient \(y_i=1\) and equal other coefficients \((s-1)/(n-1)=\lambda/d\). This follows from strict convexity of the squared Euclidean distance and averaging the \(n-1\) other coordinates; alternatively it is the orthogonal projection to the affine hyperplane \(y_i=1\), which is feasible. By symmetry all caps give the same distance, and
\[
\|x-y\|_2^2
=\left(1-\frac{s}{n}\right)^2+(n-1)\left(\frac{s/n-1}{n-1}\right)^2
=\frac{(n-s)^2}{n(n-1)}.
\]
This meets the upper bound in Step 4. Since \(n-s=d-\lambda\), the displayed Hausdorff profile follows after multiplication by \(\ell/\sqrt2\). The second directed Hausdorff distance is zero because \(A_\lambda\subset sP\), completing the proof. \(\square\)

## Verification

The accompanying standalone `verify.py` uses rational arithmetic and an independent active-set implementation of Euclidean projection onto a simplex. It computed squared distance to **each** barycentric cap, rather than using the radial trial point in the proof. Across dimensions \(2\) through \(6\), nine dilation parameters, deterministic rational grids, and independently generated seeded rational interior points, it passed **16,848 rational test instances**. Each instance checks the sharp centroid value, the global upper bound, and the pointwise envelope where applicable, with strict inequality off the centroid in the positive-gap regime. Run `python verify.py` with Python 3 and no external dependencies. These finite tests are corroboration only; the universal theorem follows from Steps 1–5.

## Relationship to prior work

Meyer, *Finite convexification by Minkowski summation* (2026), studies whether \(A+\lambda K\) eventually becomes convex using exposed-face covering radii; the full accessible HTML was inspected. The present theorem specializes to a canonical finite-vertex pair but answers a **different quantitative question**, determining the exact Euclidean Hausdorff gap at **every** dilation and the unique deepest point, plus a strict pointwise stability bound. The convexification threshold alone implies none of those metric values.

The work of Artstein-Avidan, Falah, and Slomka on vertex-generated polytopes studies related covering/Schneider-type parameters, while van Hintum studies Hausdorff distances for iterated Minkowski averages of a fixed nonconvex set. The latter operation \(k^{-1}(A+\cdots+A)\) is not the present one-sided union \(V+\lambda P\). Indexed mathematical records on the deep holes of **discrete** Minkowski vertex averages and on finite convexification of simplex skeletons likewise use different sets and do not state the dilation-dependent Euclidean Hausdorff law. Their publicly indexed summaries were compared; their full texts were not inspected. This distinction establishes non-implication of the known cited statements, not a guarantee of historical novelty.

## Limitations

This exact metric profile and unique deepest-point classification concern regular Euclidean simplices. Affine images retain the cap-membership description, but the Euclidean metric normalization in Step 2 fails for arbitrary nonsimilar affine images. The analysis does not describe the complete distance-to-union function at each point, only its exact supremum and a sharp strict envelope. Priority remains uncertain because older unindexed work, especially on vertex-generated polytopes and covering radii, may contain equivalent formulas; some related texts were available only as abstracts or search summaries. No independent mathematical audit has been performed.

## References

1. Mark Meyer, “Finite convexification by Minkowski summation,” arXiv:2610.26744v1, first posted 2026-10-19, https://arxiv.org/html/2610.26744v1.
2. Peter van Hintum, “The sharp threshold for Hausdorff convexification under Minkowski addition,” arXiv:2606.10815v1 (2026-06-09), https://arxiv.org/abs/2606.10815.
3. Shiri Artstein-Avidan, Tomer Falah, Boaz A. Slomka, “Vertex generated polytopes,” arXiv:2407.20604v1 (2024-07-30), https://arxiv.org/abs/2407.20604.
4. Matthieu Fradelizi, Mokshay Madiman, Arnaud Marsiglietti, Artem Zvavitch, “The convexification effect of Minkowski summation” (2018), DOI:10.4171/EMSS/26.
5. “Exact deep-hole spectrum of regular-simplex Minkowski vertex averages,” published mathematical research record (2026-10-11), https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-exact-deep-hole-spectrum-of-regular-simplex-minkowski-vertex-ave--a5282e569b3d (indexed summary inspected).
6. “Sharp finite convexification thresholds for every skeleton of a simplex,” published mathematical research record (2026-10-11), https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-sharp-finite-convexification-thresholds-for-every-skeleton-of-a--92b027220722 (indexed summary inspected).
