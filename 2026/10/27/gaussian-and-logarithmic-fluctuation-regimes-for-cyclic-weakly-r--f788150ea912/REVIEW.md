# Independent mathematical audit

## correctness

PASS

The process and positive deterministic initial weights fit Qin's LLN, with regular-graph edge rate 2/2=1. A vertex ring changes exactly one edge, so the compensated jump noise has diagonal predictable variation, with instantaneous diagonal tending to I. Differentiating the two endpoint probabilities gives the stated circulant J. Its Fourier spectrum is alpha sin^2(pi k/d); maximizing over integer k gives the stated threshold and odd/even ranks. For z=N/t-1 the localized normalized drift is (J-I)z/t+O(||z||^2/t). Killing at exit adds a nonpositive contribution to the squared-norm estimate. With beta_max<=1/2 its integrated expectation is O(t^(-1+epsilon)) for any small epsilon>0, and the probability of any exit after T goes to zero by the LLN. The resulting localized quadratic drift error in mode beta<1/2 is bounded after rescaling by a constant times t^(beta-1/2) times the integral of s^(-beta-1+epsilon); this vanishes including the borderline logarithm beta=epsilon. At beta=1/2 the corresponding integral is finite and the prefactor is (log t)^(-1/2). The finite-time random initial term also vanishes with these scalings. The stochastic convolution has integrable normalized bracket weights: their scalar masses tend to (1-2 beta)^(-1) or 1, and the mass on each fixed finite time interval vanishes. Off-block brackets tend to zero using orthogonal projections and the limiting identity bracket; a mixed critical/noncritical term has an additional (log t)^(-1/2) bound. Uniformly vanishing jumps give the multivariate martingale CLT and independent Gaussian blocks. The variance one for the total-count mode means projection onto the unit vector 1/sqrt(d); the unnormalized count sum has variance rate d, as expected from the Poisson clocks. The critical inverse is only on the complement. Frozen verify.py was inspected but not executed; its recorded 315 tests concern finite inputs. The independent bounded complex-step/eigenspectrum replay in python /workspace/reproductions/reproduce.py confirms critical multiplicities for d=3,4,7,8 and does not test or prove infinite-time convergence.

## originality

PASS

Credit is limited to the explicit cycle covariance and joint critical split with different log-enhanced ranks for the two cycle parities. Homogenization, generic stochastic approximation methods, and the occurrence of a log-enhanced critical mode on a different WARM graph are not new here.

## value

PASS

The cycle has a simple equilibrium but exhibits a geometry-sensitive fluctuation threshold that the LLN cannot resolve. The exact covariance and critical rank distinguish the two parities and separate the log-enhanced modes from the ordinary ones. This is a finite-cycle distributional benchmark, not a supercritical or growing-graph result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
