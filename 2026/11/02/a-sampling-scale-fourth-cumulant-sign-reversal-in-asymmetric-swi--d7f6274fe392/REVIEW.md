# Independent mathematical audit

## correctness

PASS

For stationary two-state chain Z in {0,1} with π=P(Z=1), a=q01+q10, S=Z-π and b=π(1-π), conditional E[S(t+h)|S(t)]=e^-ah S(t) and S^2=b+(1-2π)S. Consequently the ordered four-time joint cumulant is b exp[-a(t4-t1)]((1-2π)^2-2b exp[-a(t3-t2)]). Integrating this kernel over four disjoint intervals gives exactly δ^4 b Δ^4 e^(-2aΔ) H(aΔ)^2[(1-2π)^2-2b H(aΔ)^2], H(x)=(1-e^-x)/x. Each independent position error eps_j appears in at most two of the four consecutive increments, so its contribution to their joint 4th cumulant is zero despite arbitrary finite kurtosis; independent Brownian increments and deterministic drift also cancel. The covariance-matched Gaussian OU velocity has identical second moments but zero fourth mixed cumulant. H strictly decreases 1->0, giving the unique sign-reversal band 0<|1-2π|<1/sqrt(3), symmetric all-negative and more asymmetric all-positive regimes, including strict equality boundary at positive Delta. Independently reconstructed the four-point symbolic transition-matrix cumulant and checked signs at several π and Δ, not relying solely on stored program output.

## originality

PASS

Cywiński et al arXiv:0712.2225 Appendix A already derives symmetric random-telegraph four-time correlators/cumulants; telegraph fourth moments are not new. López–Ratanov asymmetric telegraph and Kolesnik moment work may provide general one-time/sometimes multitime formulas, but the accessed material does not establish this integrated four-displacement stationary-asymmetry and sampling-cadence sign phase classification with localization-error cancellation. Fleming/Blackwell animal-movement papers use Gaussian covariance/switching trajectory approaches, not the explicit identified mixed fourth-cumulant frontier. A general multitime telegraph theorem remains a meaningful historical priority risk.

## value

PASS

Second moments of the switching-velocity trajectory and exactly covariance-matched OU movement cannot distinguish the two latent models. The minimal 5 observations/4 separated displacements generate a higher-order observable that survives independent, even heavy-tailed (finite 4th moment), position noise; the exact blind sampling interval warns when this test loses power. This is a natural motivated sharp observational design fact, not a finite-simulation artifact; no finite-sample statistical guarantee is implied.

The dated certificate retains the supplied scientific assessment, sources and limitations.
