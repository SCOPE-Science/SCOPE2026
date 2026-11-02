# Independent mathematical audit

## correctness

PASS

Writing tau=L/v, u=1/(2 gamma0), w=1/(2 gammaL), H=tau+u+w, the stationary wall probabilities are u/H and w/H, independent of alpha. Polynomial Poisson correctors built from J_j(s)=p_j s+u(p_j-1_{j=0}) and K_j(s)=alpha p_j s^2+2alpha u(p_j-1_{j=0})s satisfy every bulk generator and wall-release equation. The martingale/coboundary formula yields Sigma00=2u^2[2alpha tau^3+6alpha tau^2 w+6alpha tau w^2+3tau^2+6tau w+6w^2]/(3H^3), with SigmaLL by u↔w, and Sigma0L=−2uw[alpha(tau^3+3tau^2(u+w)+6tau uw)+3tau(u+w)+6uw]/(3H^3). Every denominator is positive for positive parameters, giving Sigma0L<0 and a strictly negative derivative in alpha. Known speed and interval length plus the two wall means solve for u,w; the cross covariance then uniquely solves alpha. An independent SymPy construction from the actual generator symbolically checked all boundary identities and three closed forms. The result is an infinite-time stationary CLT covariance, not a finite-time law, and assumes alpha,gamma0,gammaL,v,L positive.

## originality

PASS

Bressloff 2023 is a strong exact-object precursor: it defines *two* wall occupation times and solves joint Laplace-time boundary value problems for sticky run-and-tumble particles, but its explicit Section 5 double-Laplace formulas use a common detachment rate gamma and are developed for encounter-based absorption and splitting, rather than the stationary unequal-release covariance matrix, its negative cross monotonicity or parameter inversion. Angelani 2023 gives a general boundary framework and mean exit times, also not that stationary covariance. The new theorem is narrowly the closed asymmetrically released covariance matrix and identifiability. Stronger joint-propagator results might yield its equal-release specialization by nontrivial differentiation; do not claim all underlying renewal/Laplace techniques as new.

## value

PASS

Stationary means are exactly blind to the tumbling rate, whereas the cross covariance is strictly monotone in it. The theorem supplies exact quantitative anti-correlation and a nontrivial identifiability mechanism for a physically natural asymmetric boundary model; the sign is not just a tautology that occupation times compete, since asymptotic covariance includes temporal memory and wall dynamics.

The dated certificate retains the supplied scientific assessment, sources and limitations.
