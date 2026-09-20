# Review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness — PASS

The result starts from the exact scalar inequality in Lassak's 2005 proof:
\[
\operatorname{area}(R)\le \frac{\Delta^2}{2}\sum_i f(\psi_i),
\qquad
\sum_i\psi_i=\pi,
\]
with
\[
f(x)=(1-\tan^2(x/2))\tan(x/2).
\]
The source also computes \(f''<0\) on \((0,\pi/2)\).

Differentiation gives
\[
q(x)=-f''(x)
=\tan(x/2)+4\tan^3(x/2)+3\tan^5(x/2),
\]
so \(q\) is strictly increasing. The tangent deficit
\[
D_\mu(x)=f(\mu)+f'(\mu)(x-\mu)-f(x)
\]
therefore has the one-sided lower bounds
\[
D_\mu(x)\ge c_n(\mu-x)^2\quad(x\le\mu),
\qquad
D_\mu(x)\ge h_n(x-\mu)^2\quad(x\ge\mu),
\]
where
\[
c_n=\frac{f(\mu)-\mu f'(\mu)}{\mu^2},
\qquad
h_n=\frac{-f''(\mu)}2.
\]
These follow from the displayed integral representations in RESULT.md and do
not require a uniform lower bound on \(-f''\).

For the negative and positive deviations, equality of their total masses and
Cauchy's inequality imply
\[
V_2\ge U_2/(n-1),
\]
hence \(V_2\ge(U_2+V_2)/n\). This justifies the coefficient
\[
C_n=c_n+(h_n-c_n)/n.
\]
The linear tangent terms cancel because the canonical angles sum to \(\pi\).
Combining the resulting Jensen-deficit estimate with Lassak's butterfly-area
inequality gives the claimed polygonal area stability bound.

The asymptotic expansions follow by expanding
\(f(x)=x/2-x^3/12-13x^5/480-107x^7/20160+O(x^9)\). They give
\[
C_n=\frac{\pi}{6n}+\frac{\pi}{12n^2}
+\frac{13\pi^3}{120n^3}+O(n^{-4}).
\]
For the angle-simplex sharpness statement, the admissible limiting family
\[
x_1\to0,\qquad x_2,\ldots,x_n\to\frac{\pi}{n-1}
\]
is valid for every \(n\ge5\). Its quotient expands as
\[
R_n=\frac{\pi}{6n}+\frac{\pi}{12n^2}
+\frac{\pi(10+13\pi^2)}{120n^3}+O(n^{-4}),
\]
which sandwiches the best scalar coefficient \(K_n\) between \(C_n\) and
\(R_n\) and proves the two-term asymptotic.

The case \(n=3\) is excluded from the quantitative statement because the
only reduced Euclidean triangles are regular; no nontrivial stability issue
arises there.

## Originality — PASS (to the best of our knowledge)

The 2005 primary source was checked at the theorem and proof level. It proves
only the qualitative strict inequality for non-regular reduced \(n\)-gons,
using concavity and Jensen's inequality, and does not state a quantitative
variance deficit.

Later surveys on reduced Euclidean and normed-space convex bodies were
checked for the status and citation trail of this area estimate. Recent
literature on reduced polygons in constant-curvature geometries was also
searched. Searches combining “reduced polygon”, area, regularity, stability,
quantitative Jensen, the 2005 title, and the explicit scalar function found
the original qualitative theorem and later geometric analogues, but no
matching angle-variance stability estimate or the two-term scalar stability
constant above.

A generic strong-concavity estimate based only on
\(\inf(-f'')\) does not imply this result, since that infimum is zero on the
closed interval because \(f''(0)=0\). The present estimate uses the fixed mean,
monotone curvature, and the zero-sum deviation constraint.

Residual originality risk remains from unindexed or differently phrased
literature, and from general Jensen-refinement results that may imply related
inequalities after specialization.

## Value — PASS

The 2005 extremal theorem distinguishes the regular polygon only
qualitatively. The new estimate gives a robust inverse statement: an
area-near-maximizing reduced polygon must have its canonical angle vector
close to the regular vector in squared Euclidean distance.

The coefficient is explicit for every odd \(n\ge5\), has a transparent
large-\(n\) expansion, and its first two asymptotic terms are optimal for the
underlying angle-sum problem. The result therefore identifies the quantitative
scale hidden in the original Jensen argument rather than merely restating
strict concavity.

## Scientific limitations

1. Angle stability is not yet a Hausdorff or vertex-position stability theorem.
2. The explicit coefficient is not claimed globally optimal over geometrically
   realizable reduced polygons.
3. The two-term optimality statement concerns the scalar angle-simplex
   inequality, where geometric realizability and butterfly overlap are
   deliberately not imposed.
4. Originality remains “to the best of our knowledge.”
