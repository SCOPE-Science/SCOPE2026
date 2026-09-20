# Review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

The result reduces the small-shift Hellinger problem to the \(L^2\) translation modulus of \(g_\kappa=\sqrt{f_\kappa}\).

Near either support endpoint, writing \(t\) for distance to the endpoint gives
\[
g_\kappa\asymp t^{1/2}(\log(1/t))^{-\kappa/2},
\qquad
|g_\kappa'|^2
\sim
\frac{1}{2Z_\kappa}\frac1{t(\log(1/t))^\kappa}.
\]
There are two endpoints. For \(\kappa\le1\), after multiplying the truncated endpoint Dirichlet energy by \(h^2\) and the Hellinger factor \(1/2\), the leading term is
\[
\frac{h^2}{2Z_\kappa}
\int_h^c\frac{dt}{t(\log(1/t))^\kappa}.
\]
The support-mismatch strip contributes only
\(O(h^2(\log(1/h))^{-\kappa})\), and a fixed interior contributes \(O(h^2)\), both negligible against the displayed divergent endpoint integral. Evaluating the integral gives the claimed powers of \(\log(1/h)\) and the \(\log\log(1/h)\) critical case with the stated constants.

For \(\kappa>1\), the endpoint Dirichlet integral converges, so \(\sqrt{f_\kappa}\in H^1(\mathbb R)\). Standard \(L^2\) translation differentiability then gives
\[
H^2(f_{\kappa,0},f_{\kappa,h})
\sim h^2\|(\sqrt{f_\kappa})'\|_2^2/2
=I_\kappa h^2/8.
\]
Direct differentiation verifies the displayed Fisher-information formula, whose endpoint integral is finite exactly for \(\kappa>1\).

The log-concavity check is independent of the Hellinger calculation. With \(q=-\log(1-x^2)\) and \(L=1+q\),
\[
(\log f_\kappa)''
=
-(1+\kappa/L)q''+\kappa q'^2/L^2,
\]
and \(q'^2/q''=2x^2/(1+x^2)\le1\), making the second derivative strictly negative on \((0,1)\). Symmetry gives the left half.

The inverse-Hellinger constants were rederived by substituting \(h=2r\), and the product limits follow exactly from affinity tensorization. The statistical rate statements are only order statements inherited from the universal-constant adaptive theorem of Wang and Gao; no sharp estimation constant is asserted.

## Originality

Wang and Gao (2026) explicitly include the power-log density
\[
(1-x^2)^\alpha/\{\log(e/(1-x^2))\}^\kappa
\]
only for \(\alpha\in(0,1)\), \(\kappa>0\), and separately list the Epanechnikov case corresponding to \(\alpha=1,\kappa=0\). Their paper gives the Hellinger-modulus framework and the general adaptive theorem, but does not state the \(\alpha=1,\kappa>0\) phase diagram or its constants.

Laha's symmetric log-concave location paper identifies the pure-power Fisher-information threshold: in its symmetrized beta family, Fisher information is infinite at and below the exponent corresponding to \(\alpha=1\), and finite above it. It does not treat logarithmic modifiers or the critical Hellinger modulus.

Pollard's differentiability-in-quadratic-mean theory and the classical Fisher-information criterion explain the regular \(\kappa>1\) mechanism abstractly. The \(\kappa=0\) Epanechnikov order is already present in Wang and Gao. Neither is claimed as new.

Searches used the exact source title and combinations of power-log, critical exponent, compact support, Hellinger translation, location estimation, logarithmic boundary, iterated logarithm, Fisher information, symmetrized beta, Epanechnikov, nonregular location, cusp, regular variation, and translation modulus. No inspected source stated the exact \(\alpha=1\) three-regime Hellinger asymptotics, the \(\kappa=1\) \(\log\log\) transition, or the product-Hellinger critical profiles.

The main residual originality risk is older nonregular-location and approximation-theoretic modulus-of-smoothness literature: the endpoint calculation is a special \(L^2\) translation-modulus asymptotic and could appear there under different terminology. No concrete older source matching this density and statistical phase diagram was located. The originality judgment is therefore to the best of our knowledge.

## Value

The result completes a delicate boundary left between two regimes visible in the recent instance-optimal location paper. On the critical power line \(\alpha=1\), a slowly varying logarithmic factor alone decides whether Fisher information is infinite, produces a continuum of faster-than-root-\(n\) rates, creates an iterated-logarithm rate exactly at \(\kappa=1\), or restores ordinary root-\(n\) behavior.

Because Wang and Gao's estimator adapts to every symmetric log-concave density through the inverse Hellinger modulus, the calculation is not merely a known-shape example: it yields a new family of explicit instance-wise adaptive rates for the same estimator. The exact product-Hellinger profiles also identify the two-point separation scale and constants independently of estimation upper bounds.

## Limitations

Only the one-dimensional compact-support family above is treated. No likelihood-ratio limit experiment, estimator limit distribution, or sharp minimax estimation constant is derived. The statistical adaptation consequence is only up to universal constants. Older nonregular-location or approximation-theory literature may contain an equivalent translation-modulus result under different language.
