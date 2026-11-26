# Independent mathematical audit

## correctness

PASS

The cube is forward invariant. The local cubic is r-Lipschitz on it, giving V'<=-2(mu-r)V. Expanding the cubic exactly gives the stated mean drift and an integrable error. Integrating the scalar potential with derivative minus the uniform cubic gives a finite integral of its squared drift; bounded derivatives and the connected scalar limit set force a single uniform limit. At theta=0 the mean is nondecreasing and tends to 1, and at theta=1 it is nonincreasing and tends to 0, using the same convergence argument and the interior initial mean. The basins of the hyperbolic endpoint attractors are open in theta. Comparison orders trajectories downward with theta, so two different parameters cannot both tend to their own interior equilibrium; this both proves uniqueness and determines the sides. For the critical trajectory variation of constants with the integrating factor gives theta_c-q0 as an integral of the centered forcing and first shows theta_c-q0=O(r/mu). In fast time, the projected local reaction has RMS norm at most r times the RMS deviation, so the centered deviations differ from their pure-mixing exponential by O((r/mu) tau exp(-c tau)), c<1. Bounded mean drift and the integrating factor contribute O((r/mu) tau) errors multiplied by integrable moment tails. Integrating exp(-2 tau) and exp(-3 tau) gives the 1/2 and 1/3 coefficients and a second-order remainder. For binary data the boundary-drift identity at q=p follows from V=p(1-p)w^2, T=(1-2p)wV. The initial positive second derivative for p<1/2 and strictly upward boundary thereafter prevent a return; a limit at p is excluded because both parts of the drift would be positive eventually just above p. Complementation proves p>1/2 and fixes the balanced case. Exact substitutions give the three-patch and skewness examples. Inspected RESULT.md, VERIFICATION.md and check.py; the reported 67,180 finite checks were not rerun and are not the basis of the threshold theorem.

## originality

PASS

The supported distinct claims are the finite-mixing all-n strict binary sign at unequal occupied fractions and the quantitative first centered-moment correction for general vectors. The qualitative fast-dispersal mean heuristic and the balanced two-patch behavior are not distinct claims. The inspected same-cubic two-patch theorems and stochastic complete-graph analogues do not supply the two principal conclusions. This is a best-of-knowledge decision, not a priority guarantee.

## value

PASS

A sharp establishment boundary for a classical idealized cubic patch model is a motivated question. The exact unbalanced binary sign shows which way rapid but finite mixing shifts the threshold, and the first correction separates initial conditions with equal mean and variance but opposite skewness. These are distinct from fitting an empirical invasion prediction or claiming universality on other exchange networks.

The dated certificate retains the supplied scientific assessment, sources and limitations.
