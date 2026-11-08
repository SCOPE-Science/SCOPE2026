# Independent mathematical audit

## correctness

PASS

The BDF2 update reuses the Gaussian increment ξ_{n−1}; replacing it by fresh noise would change the theorem. Its 3D Markov state (Y_n,Y_{n−1},ξ_n) has a stable linear covariance Lyapunov equation for every z=λh>0. Explicit solution gives C0/(σ²h)=(5z+4)/(2z(z+1)(z+4)) and C1/C0=(12+11z−3z²)/((2z+3)(5z+4)). For k>=2 the homogeneous covariance recurrence has real positive roots for 0<z<=1/2, with q above the larger root, and a positive repeated-root boundary. For z>1/2 roots are R exp(±iθ), whose nonzero real sinusoid has both signs infinitely often (rational and irrational angular orbits). BDF2 underestimates invariant OU variance by relative z²/((z+1)(z+4)) but is strictly closer than backward Euler. Independently numerically solved six covariance Lyapunov systems and computed the exact rational z=1 lag-four witness C4/(σ²h)=−3/2500; finite lags are corroboration, not the infinite sign proof.

## originality

PASS

The 2015 Andersson–Kruse and 2021 Kruse–Weiske source publications define the colored-increment BDF2–Maruyama scheme and analyze convergence, not exact stationary OU covariance at all lags. Published deterministic BDF2 sign-loss result already supplies the root transition z=1/2; this known discriminant is not new. The exact stationary C0,C1 and BEM bias comparison and stochastic all-lag sign classification are the assessed increment. Specialist stochastic multistep invariant covariance literature, including Buckwar–Winkler 2006, remains a qualified priority risk because the latter full text was inaccessible via authorized routes.

## value

PASS

The stationary marginal variance may converge with second-order bias even while lag correlations become eventually negative, unlike the exact OU dynamics. The exact all-lag positivity boundary and lag-one delay are meaningful tests for equilibrium time-series simulation and stochastic numerical method selection.

The dated certificate retains the supplied scientific assessment, sources and limitations.
