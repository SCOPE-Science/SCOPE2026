# Self-review

## Correctness
PASS. The exact-line warm start gives \(s_0=\alpha_0b\) and \(y_0=\alpha_0Ab\), hence the long BB step equals \(\alpha_0\) and the short step is \((b^{\mathsf T}Ab)/(b^{\mathsf T}A^2b)\). Every interval choice yields
\[
x^{(2)}=\alpha_0\alpha_1(\theta I-A)b,
\qquad
\theta=\alpha_0^{-1}+\alpha_1^{-1}\ge2\mu.
\]
For \(\kappa\le2\), this shift is at least \(L\), so the Stieltjes sign pattern makes the matrix entrywise nonnegative. For \(\kappa>2\), the two-dimensional diagonal family makes even the largest interval shift, attained at the short BB endpoint, smaller than \(L\); therefore every interval choice has a negative high-curvature coordinate. The exact witness and endpoint arithmetic replay successfully.

## Originality
PASS with residual literature risk. The inspected BB review gives the delayed Cauchy-step interpretation and standard long-step formula; later spectral-gradient literature treats long/short combinations and convergence. The closest published semantic-index result proves a condition-number-two frontier for objective monotonicity over the BB interval, which does not imply coordinatewise positivity. Searches for positive-orthant, Stieltjes, nonnegative-iterate, BB1/BB2, spectral-gradient, and second-iterate formulations did not locate the entrywise theorem or the all-selector two-dimensional obstruction. Older spectral-gradient or monotone-iteration literature may contain an equivalent statement under different terminology.

## Value
PASS. Spectral-gradient methods are used precisely because their aggressive delayed curvature steps improve over ordinary gradient descent, while constrained variants often add projection to enforce nonnegativity. The theorem isolates the exact conditioning boundary at which the raw BB interval itself is safe after an exact-line warm start and proves that beyond that boundary even choosing the conservative short endpoint cannot avoid a two-dimensional sign failure. This is a complete invariant-preservation classification, not a single counterexample.

Self-review: passed. Independent audit: not yet performed.
