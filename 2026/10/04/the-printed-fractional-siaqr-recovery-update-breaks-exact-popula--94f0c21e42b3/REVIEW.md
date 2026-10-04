# Same-model review

## Correctness

PASS. The continuous five-compartment right-hand sides sum identically to zero. The recovery recurrence in equation (5.22) is then compared term by term with the other four component recurrences: its first history term uses \(R\), but its two higher history differences use \(Q\). For the exact invariant submodel
\[
I=A=Q=0,\qquad N=1,\qquad \delta=\omega=\frac12,\qquad \gamma=\frac12,
\]
the source model has
\[
R(t)=e^t\operatorname{erfc}(\sqrt t).
\]
Substitution into the \(m=2\) recurrence gives an uncancelled population change
\[
-0.49207893684378897699\ldots.
\]
The bundled high-precision checker independently reconstructs the coefficients and value.

## Originality

PASS. Population conservation and scalar Newton-polynomial history quadrature are prior methodology. The accepted result is source-specific: equation (5.22) changes the recovered-state argument to the quarantine state inside the higher \(g_5\) history corrections, and this exact substitution breaks conservation on an explicit fractional-order solution history. Searches by exact DOI/title, \(g_5/Q/R\) aliases, recovered-compartment wording, and erratum terminology found no published correction.

## Value

PASS. The model is explicitly a closed five-compartment epidemic model, so preservation of total population is a natural structural check. The printed update loses approximately \(49.2\%\) of the total population in the exact witness after a single evaluated recurrence level. The repair is minimal and directly useful for reproducing the algorithm. The assessment is limited to the printed scheme because the simulation code is unavailable.

## Closest literature and limitations

Earlier stochastic-delay SIAQR work treats positivity and persistence in a different model. Independent descriptions of Newton-polynomial Caputo stepping keep the same scalar component function throughout a history interpolation. Neither supplies the later article's \(Q\)-for-\(R\) substitution.

The result does not claim that the published figures were generated with the malformed recurrence, nor does it certify the remaining numerical coefficients or the convergence order of the method.

Same-model review: passed. Independent audit: not yet performed.
