# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

PASS.

For \(x=m e^{-u}\), \(y=m e^u\), the final 2007 definition gives
\[
J_\alpha(r)=m\left[
\frac{\operatorname{sinhc}(u(r+\alpha))}
{\operatorname{sinhc}(ur)}
\right]^{1/\alpha}.
\]
With \(\phi(z)=\log(\operatorname{sinhc}z)\), the logarithm is
\[
L(r)=\log m+\frac{\phi(u(r+\alpha))-\phi(ur)}{\alpha}.
\]
The function \(\phi\) is even. Therefore \(L''(-\alpha/2)=0\), while
\[
L'(-\alpha/2)=\frac{2u}{\alpha}
\left(\coth\frac{\alpha u}{2}-\frac{2}{\alpha u}\right)>0.
\]
The positivity follows from \(z\cosh z-\sinh z>0\) for \(z>0\). Consequently
\[
J_\alpha''(-\alpha/2)=J_\alpha(-\alpha/2)[L'(-\alpha/2)]^2>0.
\]
Since \(J_\alpha\) is smooth in \(r\), its second derivative stays positive immediately to the right of \(-\alpha/2\). This directly contradicts strict concavity on the whole interval \((-\alpha/2,\infty)\).

For the product \(P(r)=J_\alpha(r)J_\alpha(-r)\),
\[
(\log P)''=
\frac{u^2}{\alpha}
\left[
\phi''(u(r+\alpha))+\phi''(u(\alpha-r))-2\phi''(ur)
\right].
\]
Using
\[
\phi''(z)=\frac13-\frac{z^2}{15}+\frac{2z^4}{189}+O(z^6),
\]
the constant terms cancel and the quadratic terms give
\[
(\log P)''=-\frac{2\alpha}{15}u^4+O(u^6).
\]
The coefficient is strictly negative for every \(\alpha>0\), independently of fixed \(r\). Hence at every prescribed \(r\) outside the conjectured central interval, sufficiently close unequal inputs give logarithmic concavity rather than logarithmic convexity. The remainder is uniform on compact \(r\)-sets by analyticity.

The supplementary expansion
\[
J_\alpha''(r)=m\frac{5-6r-3\alpha}{45}u^4+O(u^6)
\]
was rederived independently from \(J''/J=L''+(L')^2\). The verification artifact checks both leading coefficients symbolically.

## Originality

PASS, to the best of our knowledge.

The final 2007 Taiwanese Journal of Mathematics article was inspected at the definition of \(J_\alpha\), Theorem 3, and the open-problem section. It includes the \(1/\alpha\) power in the generalized mean and explicitly poses both claims addressed here.

Searches covered the paper title and DOI, exact and synonymous formulations of Open Problems 1 and 2, generalized one-parameter means, Stolarsky means, ordinary concavity, logarithmic convexity of the symmetric product, the reflection center \(-\alpha/2\), and near-diagonal or hyperbolic-function reformulations. No published counterexample or equivalent curvature expansion was located.

The 2009 alternative-proof paper was checked through its bibliographic record and accessible author-posted text; it concerns monotonicity and logarithmic convexity of the ordinary one-parameter mean and monotonicity of the product, not the ordinary-concavity assertions here.

A particularly relevant current-status check is Yang--Qi's 2025 survey of bivariate homogeneous functions of two parameters. Its accessible full text cites the 2007 paper and reviews the one-parameter mean's monotonicity and logarithmic convexity/concavity, as well as product monotonicity, but no resolution of the two 2007 curvature questions was found in that discussion or by full-text searches for the open-problem and strict-concavity language.

Residual risk remains because the first counterexample mechanism is a short consequence of formulas already close to the original conjecture. It could have appeared in correspondence, an unindexed note, or a differently phrased observation that the searches did not recover.

## Value

PASS.

The result gives a universal negative resolution of Open Problem 1, not merely a single counterexample: every unequal input pair has a convex right-neighborhood at the conjectured endpoint. It also supplies a distinct analytic obstruction to the exterior half of Open Problem 2, showing that every prescribed finite exterior point becomes strictly log-concave near the diagonal. The two mechanisms clarify the separation between logarithmic concavity and ordinary concavity and identify how the product's proposed curvature transition degenerates as the inputs coalesce.

## Limitations

- The full ordinary-curvature sign diagram of \(J_\alpha\) for arbitrary input ratio is not classified.
- The full logarithmic-curvature sign diagram of \(J_\alpha(r)J_\alpha(-r)\) is not classified.
- The central concavity and logarithmic-concavity clauses of Open Problem 2 are not resolved here.
- The value \(5/6-\alpha/2\) is a leading near-diagonal transition, not an exact global inflection point for finite \(u\).
- A poorly indexed or unpublished prior observation remains a residual originality risk.
- Independent audit has not been performed.
