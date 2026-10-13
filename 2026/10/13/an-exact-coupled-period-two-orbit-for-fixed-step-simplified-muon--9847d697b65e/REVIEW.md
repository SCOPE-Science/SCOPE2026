# Self-review

## Correctness
PASS. The source model has \(\widehat K=2rI_3/n+r^2\Sigma\); with \(n=3r\), the displayed \(\Sigma\) realizes the claimed coupled matrix and is positive definite for \(0<\chi<1/3\). The factor-manifold polar calculation reduces each block update to the sign of the factor times its reduced force. At \(X^+\), all factors and forces are positive, so one step subtracts \(\eta\) blockwise. At \(X^-\), the identity \(t^2=2\delta-\delta^2\) makes the two coupled forces exactly opposite, while the nuisance factor signs make all three gradient blocks negative. The next step therefore adds \(\eta\) blockwise and returns exactly to \(X^+\). All blocks are nonzero, so no set-valued polar ambiguity is used.

## Originality
PASS. The motivating source states qualitative persistent oscillation and gives diagonal and coupled numerical examples, but full-text searches find no period or two-cycle theorem. Its coupled theory proves one-step river-energy behavior rather than an exact recurrent orbit. The closest analytic predecessor derives decoupled scalar Muon recurrences for matrix factorization and uses geometrically decaying learning rates; those scalar recurrences do not imply the off-diagonal signal--nuisance sign pattern constructed here. Targeted statement-level published-result searches returned no coupled mixed-spiked period-two result. Residual risk remains because constant-step sign dynamics are elementary once a suitable coupled state pair is guessed.

## Value
PASS. The source explicitly separates a fully decoupled diagonal sanity check from its genuinely coupled positive-semidefinite regime. The construction closes a natural structural question left by that separation: coupling does not merely preserve qualitative oscillation numerically, but permits an exact nonconvergent orbit of the actual factor-level method for every fixed step in a whole continuum of valid covariances. This makes the fixed-step late-stage limitation independent of diagonal decoupling or plotting truncation.

## Closest literature and limitations
The river-valley source is the closest work and already motivates switching away from fixed-step Muon for late refinement. The present result sharpens its qualitative and numerical oscillation evidence to an exact off-diagonal periodic witness. The matrix-factorization preconditioning paper gives exact scalar recurrences but only for independent spectral modes and decaying learning rates. The result here does not classify attraction, momentum, stochastic gradients, or approximate polar computation.

Self-review: passed. Independent audit: not yet performed.
