# Scientific review: Gaussian-sketched one-mode decay

## Correctness — PASS

The sketched Galerkin identity reduces to a single scalar rate. Decomposing the noninvariant trial vector's residual into an orthogonal component and using independent Gaussian images of orthogonal vectors gives exactly a standard normal numerator divided by the square root of an independent chi-square denominator. Integration against the chi-square density at zero proves divergence of every positive frozen exact-time moment; this is an infinite-dimensional-in-time analytic integral, not an inference from sampling. Student moments exist exactly below their degree threshold, proving that frozen Euler has a finite squared moment precisely for sketch rows greater than twice the step count. Repeated independent fresh sketches yield a geometric squared-moment factor and its sharp stability interval. The special invariant-vector boundary is explicitly excluded and treated separately. The embedded checker passed its finite diagnostics, without substituting computation for proof.

## Originality — PASS, with documented residual risk

The assessed claim is the combination of unconditional frozen positive-time moment explosion, the exact frozen Euler finite-moment horizon, and the independent-refreshed Euler stability boundary. The Student-ratio representation, Student tail-moment facts, and fixed-vector negative-rate/sign-loss probability are recognized prior ingredients, not independent novelties. The closest inspected 2026 dynamics paper treats oblique and orthogonal sketches under embedding hypotheses and numerical experiments, rather than this unconditional moment frontier; the inspected 2025 sketched Krylov ODE work supplies a projected ODE formula but not the sharp laws. The 2018 Gaussian model-reduction Galerkin source develops high-probability embedding bounds, which do not imply unconditional moments. Targeted published-record searches and recovered local historical claims disclosed no statement implying the whole theorem. An earlier equivalently formulated Gaussian sketched-flow theorem could still exist in unindexed or inaccessible literature.

## Value — PASS

The result addresses an actual choice in sketched time propagation: freezing a sketch versus independently redrawing it. It proves that finite sketch dimension can give apparently consistent rates in probability while destroying every positive-time expected energy, and identifies the exact finite sketch-size and stepsize boundary for fresh Euler. The sharp distinction holds for a natural fixed-trial Galerkin model of a dissipative positive-definite system, and is relevant as a boundary example when designing numerical time propagators. It does not establish instability of higher-rank, conditioned, stabilized, or application-specific solvers.

## Closest sources and limits

Carrel and Grigori, arXiv:2607.03402v1 (first publicly posted July 3, 2026), especially Sections 4 and 6. Krieger and Schweitzer, arXiv:2510.17538v1 (October 20, 2025), Section 4. Balabanov and Nouy, arXiv:1803.02602 (March 7, 2018), the Galerkin embedding analysis. The published-record comparison with a two-component PAGE mean-square stability law concerns a different stochastic optimization update, not Gaussian projected ODEs. Independent mathematical and bibliographic review remains unperformed.

Self-review: passed. Independent audit: not yet performed.
