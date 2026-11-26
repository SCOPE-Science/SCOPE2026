# Independent mathematical audit

## correctness

PASS

For positive rho the last-reset age has the exponential stationary law, and running the reset-free dynamics from the prescribed state for that age constructs the unique stationary law. Equal thermal variances cancel and heading reflection gives zero transverse mean and cross-covariance, even at D=0. Using times 0≤s≤u in a reset-free cycle, Brownian independent increments give E cos(Theta_s+Theta_u)=exp(−3s−u); put u=s+z and age=u+w in the double-convolution integral. The three independent Laplace denominators are rho+4, rho+beta+1 and rho+2beta, giving the positive raw difference. The mean is the analogous single convolution, v rho/[(rho+1)(rho+beta)]; its derivative has sign beta−rho². Subtracting its square gives the bracket 2(rho+1)^2(rho+beta)^2−rho(rho+4)(rho+beta+1)(rho+2beta), which expands to the given Q. With r=sqrt(beta), Q(r)=−beta(3 beta r+3 beta+5r+2); positivity at zero and infinity yields a positive root on each side. Descartes counts exactly two sign changes even when beta=1, so there is no additional positive root and these two roots are simple. The four coefficient limits on the specified scales are 2−4c−2c² and rho²(rho−2)(rho+1) at small beta, and 2−4rho and c³−4c at large beta. Bracketing the simple positive root of each limit on compact intervals gives the asserted scales; the two brackets are disjoint for sufficiently extreme beta. This proves the result for all positive beta, rho, v and all D≥0, under joint, fixed-state resetting, not for other resetting protocols. The supplied script was inspected, not executed. Its hardcoded total counts 18 standalone symbolic checks, whereas lines 26–55 contain 14 standalone assertions; this is a reporting discrepancy, not a failed scientific identity or a premise of the proof.

## originality

PASS

Pass for the all-trap-strength two-crossing theorem and the boundary asymptotics, not for the raw or centered moment formulas or the mean optimum. Shee's exact moments mechanically imply the compact difference and quartic, but the inspected model passages do not settle its positive-root count, the location of the optimum inside the transverse region, or the two singular limits of the boundary curves. No exact or stronger statement of that scoped classification was established in the close comparisons.

## value

PASS

The geometry is not read off from the known uncentered inequality, which always favors the reset axis. The theorem gives a complete covariance-axis diagram for every positive confinement, proves the longitudinal mean is maximized strictly in the transverse-dominant regime, and quantifies how both boundaries separate in each limiting trap regime. These are useful sign and scaling results even though exact moment inputs and the mean optimizer are known.

The dated certificate retains the supplied scientific assessment, sources and limitations.
