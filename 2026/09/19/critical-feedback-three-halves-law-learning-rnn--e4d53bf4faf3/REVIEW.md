# Review

Same-model review: passed. Independent audit: not yet performed.

## Correctness

**PASS.** The stationary critical equation follows directly from the source's Eqs. (4.2)--(4.3) after setting the equal-time and plateau correlations equal at the well-collapse point. The Gaussian variable must remain in the nonlinear argument. With the source's marginal condition, the literal printed Eq. (4.6) gives a negative squared critical feedback at g=1.3, whereas the corrected equation gives 0.195822866873, consistent with the source's stated value about 0.2.

The small-gain expansion was derived independently from Gaussian moments and checked symbolically through higher order. A standalone verifier reproduces the series coefficients, the g=1.3 value, the inconsistency of the literal printed equation, and a representative non-asymptotic target crossing. The target-feasibility statement is conditional only on the source's stated monotone path from zero to A/sqrt(N).

## Originality

**PASS, with a deliberately narrow claim.** The SCS chaos transition, its marginal-stability criterion, and suppression of chaos by external driving are established prior art and are excluded from the novelty claim. The new claim is restricted to arXiv:2609.19288v1: the corrected stationary critical equation required by its displayed DMFT, the sharp three-halves expansion of its learned critical feedback, and the induced small-target feasibility boundary. No matching SCOPE record or source-specific prior statement was found by searches using the source identifier/title, critical-feedback terminology, and equivalent scaling language.

A residual risk remains that older random-network work contains an algebraically equivalent expansion for a static bias or drive, since the local marginal equations belong to the established SCS family. Accordingly, this record does not claim broad priority for a three-halves exponent in random neural networks.

## Value

**PASS.** The source reports a numerical critical feedback and notes that it increases with gain. The result supplies a sharp critical exponent and coefficient, explains why small learned targets can fail to reach the freezing bifurcation, and identifies a printed self-consistency error that is quantitatively incompatible with the source's own representative critical point. The target law gives a direct scaling prediction for a regime the source explicitly identifies as interesting but does not analyze quantitatively.

## Scientific limitations

All exact statements concern the quasi-static DMFT critical equations rather than the full finite-size learning process. The non-asymptotic q=1 crossing is numerical. No independent audit has been performed.
