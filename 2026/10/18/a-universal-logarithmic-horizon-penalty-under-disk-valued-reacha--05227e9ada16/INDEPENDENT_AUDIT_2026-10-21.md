# Independent mathematical audit

## correctness

PASS

The stochasticity condition follows from max(a+b)=r(1+sqrt(2))<1. For a fixed kernel, success by t is a geometric sum; for fixed a, failure probability is minimized on the lower disk boundary beta(a). The minimizer is localized to a~(log t)/t, where a uniform expansion of the deficit gives the +1 constant and log(2rt). The adaptive Bellman step is the disk support function; rationalization gives the exact deficit recursion, and reciprocal increments tend to r/2, proving 1-D_t~2/(rt). The ratio follows. For every fixed kernel, positive failure probability or a=0 gives infinite expected hitting time, while the eventual success supremum tends to one as a approaches zero along the boundary. Finite script tests are not used for the asymptotic proof.

## originality

PASS

The closest full primary sources establish qualitative eventual-hit nonattainment and general imprecise-chain hitting-time characterizations, but not the smooth disk family or the sharp finite-horizon stationary/adaptive rates. Searches found no exact covering table or theorem; unindexed equivalent asymptotics remain a risk.

## value

PASS

The example quantifies a meaningful policy-class penalty that is invisible from the common infinite-horizon upper hitting value: commitment to one kernel costs a logarithmically larger finite-horizon deficit than horizon-dependent control. The exact leading constants and the explicit three-state disk make a useful boundary example for robust reachability, not merely a routine expectation counterexample or finite numerical slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
