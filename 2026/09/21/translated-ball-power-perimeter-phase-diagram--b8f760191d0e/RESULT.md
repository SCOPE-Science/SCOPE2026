# Translated-ball phase diagram for radial power perimeter

Let \(n\ge 3\), \(R>0\), \(a\in\mathbb R^n\), and
\[
P_p(a;R):=\int_{\partial B_R(a)} |x|^p\,d\mathcal H^{n-1}(x).
\]
Write \(t=|a|/R\) and
\[
\Phi_{n,p}(t):=\frac1{\omega_{n-1}}\int_{S^{n-1}}|t e_1+\theta|^p\,d\sigma(\theta),
\]
so that
\[
P_p(a;R)=\omega_{n-1}R^{n-1+p}\Phi_{n,p}(t).
\]

## Theorem

For \(t\ne1\), the translation profile has the following complete monotonicity classification.

1. If \(p>0\), then \(\Phi_{n,p}\) is strictly increasing on \((0,\infty)\).
2. If \(p=0\), then \(\Phi_{n,0}\equiv1\).
3. If \(2-n<p<0\), then \(\Phi_{n,p}\) is strictly decreasing on \((0,\infty)\).
4. If \(p=2-n\), then
   \[
   \Phi_{n,2-n}(t)=
   \begin{cases}
   1,&0\le t\le1,\\
   t^{2-n},&t\ge1.
   \end{cases}
   \]
5. If \(p<2-n\), then \(\Phi_{n,p}\) is strictly increasing on \((0,1)\) and strictly decreasing on \((1,\infty)\).

At the touching position \(t=1\), \(\Phi_{n,p}(1)<\infty\) exactly when \(p>1-n\). In that integrable range,
\[
\Phi_{n,p}(1)
=
2^{p+n-2}
\frac{\Gamma(n/2)\Gamma((p+n-1)/2)}
{\sqrt\pi\,\Gamma(n-1+p/2)}.
\]
Hence, when \(1-n<p<2-n\), \(t=1\) is the unique global maximum of the translated-ball profile. When \(p\le1-n\), the profile tends to \(+\infty\) as \(t\to1^\pm\).

In particular, at the critical exponent \(p=2-n\),
\[
P_{2-n}(a;R)=\omega_{n-1}R
\qquad\text{for every }|a|\le R.
\]
Thus every radius-\(R\) ball whose closure contains the origin has exactly the same \(|x|^{2-n}\)-weighted perimeter. For \(|a|\ge R\),
\[
P_{2-n}(a;R)
=
\omega_{n-1}R^{n-1}|a|^{2-n}.
\]

## Proof

Rotation and scaling reduce the problem to the normalized spherical mean \(\Phi_{n,p}\).

For \(0<t<1\), differentiate with respect to the translation variable \(a\). Since the sphere stays a positive distance from the singularity,
\[
\Delta_a |a+\theta|^p
=
p(p+n-2)|a+\theta|^{p-2}.
\]
Because the spherical average is radial,
\[
\Phi_{n,p}''(t)+\frac{n-1}{t}\Phi_{n,p}'(t)
=
p(p+n-2)\Phi_{n,p-2}(t),
\]
or
\[
\bigl(t^{n-1}\Phi_{n,p}'(t)\bigr)'
=
p(p+n-2)t^{n-1}\Phi_{n,p-2}(t).
\]
The right-hand factor \(\Phi_{n,p-2}(t)\) is strictly positive. Radial regularity at the origin gives
\[
\lim_{t\downarrow0}t^{n-1}\Phi_{n,p}'(t)=0.
\]
Therefore, on \(0<t<1\), the sign of \(\Phi_{n,p}'\) is exactly the sign of \(p(p+n-2)\), except at the two zero factors \(p=0\) and \(p=2-n\). This gives all interior monotonicity statements and shows that the critical profile is constant on \([0,1)\).

For \(t>1\), direct differentiation gives
\[
\Phi_{n,p}'(t)
=
\frac{p}{\omega_{n-1}}
\int_{S^{n-1}}
(t+\theta_1)|t e_1+\theta|^{p-2}\,d\sigma(\theta).
\]
Since \(t+\theta_1>0\) on the whole sphere, the derivative has the sign of \(p\). This gives all exterior monotonicity statements.

At \(p=2-n\), the interior constant equals \(\Phi_{n,2-n}(0)=1\). Outside the unit sphere the same spherical average is a radial harmonic function tending asymptotically to \(t^{2-n}\); hence it is exactly \(t^{2-n}\). This is the classical Newton-shell/mean-value identity for the fundamental solution.

At \(t=1\), use the first-coordinate density on \(S^{n-1}\):
\[
\Phi_{n,p}(1)
=
\frac{\Gamma(n/2)}
{\sqrt\pi\,\Gamma((n-1)/2)}
\int_{-1}^{1}
[2(1+u)]^{p/2}(1-u^2)^{(n-3)/2}\,du.
\]
The integral is finite exactly when \(p>1-n\). A beta-integral evaluation yields
\[
\Phi_{n,p}(1)
=
2^{p+n-2}
\frac{\Gamma(n/2)\Gamma((p+n-1)/2)}
{\sqrt\pi\,\Gamma(n-1+p/2)}.
\]
For \(p\le1-n\), the same local singularity shows divergence at \(t=1\), and Fatou's lemma gives divergence of the one-sided limits.

Combining the interior and exterior derivative signs with continuity at \(t=1\) whenever \(p>1-n\) proves the phase diagram.

## Relation to the weighted-isoperimetric literature

Csató's 2018 paper studies the fixed-volume isoperimetric problem with perimeter density \(|x|^p\). In Example 11 it computes the first and second variations of translated centered balls and identifies the local sign change at \(p=2-n\). It also observes that for \(2-n<p<0\) moving the ball away lowers the weighted perimeter, while for \(1-n<p<2-n\) the centered ball is locally stable even though it is not a global minimizer among all admissible sets.

The theorem above upgrades that local translation calculation to a global one-parameter classification. In the stable-but-not-global range
\[
1-n<p<2-n,
\]
the centered ball is in fact the unique minimizer among all translates that still contain the origin (\(|a|<R\)); the translation profile then rises to a unique maximum when the sphere first touches the origin. Thus the global failure in that range cannot be witnessed by merely translating a ball while preserving the origin-containment condition.

At the degenerate second-variation exponent \(p=2-n\), the local test misses a stronger phenomenon: the entire family \(|a|\le R\) is flat. This is explained by the harmonicity of the fundamental-solution kernel.

A 2026 paper of Csató, Giovagnoli and Roy again uses translation variations for weighted perimeter functionals and emphasizes the role of the sign of \(\Delta |x|^p\). Its translation argument yields rigidity for \(p>2-n\), while the critical and more singular regimes require different information. The complete translated-ball profile above was not located in that paper.

## Originality scope

The spherical-mean differential identity and the \(p=2-n\) Newton-shell formula are classical potential theory; no originality is claimed for those facts in isolation. The claim here is the explicit full translation phase diagram for the weighted-perimeter functional, including the critical flat family and the sharp interpretation of the \(1-n<p<2-n\) stable-but-not-global regime. Searches of the source paper, later weighted-isoperimetric literature, spherical-mean/Riesz-kernel terminology, and the 2026 weighted-perimeter paper did not locate this combined statement, to the best of our knowledge.

## Limitations

- This classifies only translations of a fixed Euclidean ball, not arbitrary shape perturbations.
- It does not alter Csató's global isoperimetric classification; in particular, non-ball competitors are essential in the range \(1-n<p<2-n\).
- At \(p=2-n\), the flat translation identity is a direct manifestation of the classical Newton-shell theorem, so the novelty claim is limited to its weighted-perimeter interpretation and the complete phase diagram around it.
- A prior potential-theoretic statement phrased purely in terms of Riesz spherical means could subsume part of the theorem even if it was not found under weighted-perimeter terminology.
- Independent audit has not been performed.

## References

1. G. Csató, *On the isoperimetric problem with perimeter density \(r^p\)*, Communications on Pure and Applied Analysis 17 (2018), 2729–2749. https://doi.org/10.3934/cpaa.2018129 ; arXiv:1706.09619.
2. G. Csató, D. Giovagnoli, P. Roy, *Weighted Perimeters and pth Moments of Inertia of Convex Curves and Surfaces*, arXiv:2608.19851 (2026).
