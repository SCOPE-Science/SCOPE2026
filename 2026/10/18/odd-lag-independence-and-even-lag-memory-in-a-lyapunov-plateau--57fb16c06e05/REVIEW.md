# Scientific self-review

## Correctness — PASS

The claim is restricted to the source's absolutely continuous stationary law and the closed/open parameter limits stated in `RESULT.md`. The one-step event is exactly the interval \(0<X<\beta/2\); independent integrations of the source's five- and nine-segment density formulas give the two affine covariance laws. At the critical parameter, each of four cells maps into whole successor cells, yielding the stated transition matrix and invariant masses. The finite matrix identity \(P^2v=-v/2\) together with the exact vanishing of the lag-one weighted dot product proves all infinitely many odd/even cases. The direct exact-rational checker succeeds with `VERIFY_OK`; finite checks are supplementary to the algebraic infinite-lag proof.

## Originality — PASS with residual bibliographic uncertainty

The source [1] contains the same natural invariant densities and the constant Lyapunov value, but its primary theorems address invariant measures, Lyapunov exponents and entropy—not the stated autocovariance classification. Later matching research [2] studies exactly this model and supplies broader entropy and matching descriptions without giving the specific sensor memory law. A pre-existing same-map claim covers only \(2<\beta<3\); comparisons concerning baker and Chebyshev observations involve different maps and do not imply the parameter-four parity law. Explicit published-source and mathematical-result searches found no equivalent or dominating theorem. A differently coded historical time-series formula could remain undiscovered; absolute priority needs an independent assessment.

## Mathematical value — PASS

The stationary right-branch indicator is the fundamental observable entering the Lyapunov exponent. Its first-lag covariance changes sign across a plateau on which the Lyapunov exponent remains fixed, and the exact four-cell degeneration produces independence of every odd-lag pair despite persistent dependence at all positive even lags. The all-lag formula is a natural nontrivial quantitative invariant of the induced binary process rather than an isolated finite computation.

## References and boundaries

See [1] Botella-Soler et al., arXiv:1205.5360v1, Appendix A and §4; [2] Bruin et al., arXiv:1707.07488v1, matching and entropy theorems; [3] Botella-Soler et al., arXiv:0812.4551, predecessor-map dynamics. All claims use the specified absolutely continuous stationary measure. No statement about other invariant measures or the upper endpoint \(\beta=9/2\) is made. The scope and bibliographic residual risk are retained in the complete result and the structured review.

Self-review: passed. Independent audit: not yet performed.
