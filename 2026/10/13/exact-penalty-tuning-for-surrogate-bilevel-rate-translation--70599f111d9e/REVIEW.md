# Self-review

## Correctness

PASS. Substituting the affine certificates stated in the source remark into Proposition 1(iii) gives
\[
U(\rho)=a_0+a_1\rho+\ell\sqrt{2\left(b_1+\frac{b_0}{\rho}\right)}
\]
under the explicit additional assumption that the same Lipschitz constant \(\ell\) is valid throughout the tuning range. Direct differentiation yields a strictly positive second derivative when \(b_0>0\). For \(a_1>0\), the derivative changes sign exactly once, and the resulting stationary equation is equivalent to the displayed monotone quartic. The minimum-value identity and every degenerate case were rederived independently.

The uniform-Lipschitz qualification is necessary because the level set used by the source may vary with \(\rho\); the final claim includes that qualification rather than silently treating the constant as fixed.

## Originality

PASS. The primary source provides the translation bound, states affine dependence on \(\rho\), and observes only that a finite minimizer may exist. It does not give uniqueness conditions, the algebraic optimizer, the minimum-value formula, or the boundary regimes. The inspected lifting precursor and general quadratic-penalty literature address related mechanisms but do not imply this source-specific tuning theorem. Formula-level and source-specific searches found no equivalent result.

A residual risk is that the same elementary optimization may occur in specialized parameter-selection literature under different notation. No such dominating statement was located.

## Value

PASS. The source explicitly flags \(\rho\) as a trade-off parameter whose best value is unresolved at the level of its translated guarantee. The result supplies a complete horizon-wise selection rule and tells users when a finite optimum does not exist. The parameter is structurally motivated by the surrogate construction, and the exact phase diagram is more informative than a numerical one-dimensional search.

Self-review: passed. Independent audit: not yet performed.
