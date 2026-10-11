# Same-model review

## Correctness
PASS. The printed Example 4.1 has no current-state linear term at the coexistence equilibrium; direct differentiation yields a single delayed matrix. Factoring its characteristic determinant with \(z=s^q e^{s\tau}\) gives the stated quadratic exactly. On \(-1<k\le0\) the quadratic has one conjugate pair, so modulus and phase determine the complete imaginary-axis crossing ladders. The upper branch has the earliest positive phase; the lower branch and all later phase turns occur strictly later. At \(k=-1/2\) the exact formula reproduces the published frequency \(0.9085\) but gives \(\tau_*=1.147739992150082\ldots\). Direct substitution into the original quasipolynomial has negligible numerical residual, and implicit differentiation gives a strictly positive real crossing speed.

## Originality
PASS. The motivating paper was inspected in full at the model, characteristic equation, phase equations, theorem, numerical example, and figures. Its equation (3.3) supplies the quasipolynomial, but neither the exact common-delay quadratic reduction nor the corrected phase thresholds are stated; the published numerical threshold is different. Exact DOI/title/correction searches and source-specific database searches found no checked correction or equivalent statement. The closest inspected predecessor studies feedback control in a different fractional predator--prey model, and the closest open full-text three-species paper has a different dimension and delayed matrix. Residual risk remains because searches cannot exclude obscure or unindexed commentary.

## Value
PASS. The reduction replaces a fragile trigonometric calculation by an exact spectral normal form for the whole displayed gain range \(-1<k\le0\), yields every imaginary-axis crossing ladder, corrects the source's principal numerical benchmark, and explains why the source's stable trajectory at \(\tau=0.93\) and oscillatory trajectory at \(\tau=1.16\) are mutually consistent. This is a structural correction to the bifurcation boundary, not a rounding adjustment.

## Closest literature and limitations
The primary article is the decisive comparison because it contains exactly the same model and characteristic equation. Huang et al. (2018) and Li et al. (2019) address related fractional delayed predator--prey feedback systems but do not state or imply this Example 4.1 quadratic and threshold. The result is limited to the printed linearized spectrum; nonlinear Hopf direction and periodic-orbit stability are not established.

Same-model review: passed. Independent audit: not yet performed.
