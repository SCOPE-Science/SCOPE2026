# Self-review

## Correctness
**PASS.** The period-two propagator is obtained directly from the discrete-time SIS linearization. Its determinant at eigenvalue one factors into two explicit terms; one is strictly negative throughout the parameter domain and the other has the unique positive zero \(\lambda^2=\mu^2(2-\mu)/(1-\mu)\). Perron monotonicity identifies this zero as the unique spectral-radius crossing. The aggregate threshold follows from the spectral radius of the half-weighted three-vertex path. Minimality follows because two vertices support only one simple edge, whereas any two distinct edges on three vertices form the same path up to relabeling. The packaged verifier returns `VERIFY_OK`.

Risk: the formal critical value can lie above the probability range \([0,1]\) at high recovery probability; the claim states this explicitly rather than treating such a value as physically reachable.

## Originality
**PASS.** Valdano et al. supply the general infection-propagator threshold criterion, and Speidel et al. prove a broader aggregate lower bound for a different stochastic snapshot protocol—random sampling with replacement—and discuss single-link snapshots. Those results own the framework and the qualitative possibility that discrete-time temporality raises a threshold. The inspected sources and targeted searches did not state the deterministic two-snapshot three-node closed form, its minimality, or the exact temporal-to-aggregate ratio.

Risk: the calculation is elementary once the three-node sequence is isolated, so an unindexed lecture note or worked example could contain the same matrix identity.

## Value
**PASS.** The aggregate approximation is a standard simplification of temporal contact data. This result gives the smallest nontrivial deterministic example in which the approximation has a strict, analytically quantifiable bias, and the exact ratio separates finite-step discreteness from graph-size complexity. It also provides a clean benchmark for testing temporal-SIS implementations and for explaining why the discrete-time direction differs from familiar continuous-time results.

Self-review: passed. Independent audit: not yet performed.
