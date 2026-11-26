# Independent mathematical audit

## correctness

PASS

The two orientation-resolved currents vanish separately at both ends. Adding the stationary equations gives Dρ′=vm, and subtracting gives Dm″−vρ′−2αm=0 and endpoint identity D²ρ″=v²ρ. The stated symmetric density solves these equations, normalizes to one, and gives nonnegative orientation densities: the possibly negative excess from the hyperbolic terms in ρ±Dρ′/v is bounded by q(Dκ/v−1)=1/(√(1+1/q)+1)<1. The mean reflecting regulator rate on a wall is D times its contact density, giving k_BT times that density as the force; independence of reflected coordinate processes justifies the exact tensorization. The displaced volume cancels the V in the pressure, giving the exact work differential. Since tanh(z)−z sech²(z) has positive derivative for z>0, F′>0 and the sum of the H terms is strictly Schur-convex at fixed log-volume. Anisotropy here is ordered by log-majorization, not by arbitrary scalar measures of shape. The even two-axis perturbation gives the stated quadratic coefficient; its derivative differs from q at positive infinity by an integrable exponential error. The Hessian is K−2nk_BT aF′(a); below threshold, evenness and coercivity give nonzero paired global minima. A trial t of order 1/K drives the minimum to minus infinity, so all positive minimizers diverge and stationarity yields Kt_K→nk_BTq. No uniqueness, critical-stiffness classification or dynamical instability is required. The frozen check.py and check_output.json were inspected, not executed. The script's counters sum to 1670, as in RESULT.md and the recorded JSON; VERIFICATION.md's prose gives 356, an inconsistent diagnostic count, not a defect in the analytic argument.

## originality

PASS

The exact one-dimensional density and pressure are prior, and endpoint path independence is an immediate consequence of Li–Eichhorn–Dabelow's separable higher-dimensional approximate work law. Tensorization of the exact one-dimensional law in the stated Cartesian model and the convex-order implication of separability should not be presented as new pressure formulas or an exact spherical-RTP result. The supported distinct finding is the exact fixed-volume shape law in the diffusive Cartesian product, taken with its compliant-box consequences: the sharp instability threshold of the force-balance potential, existence of global distorted minima, and the quantified weak-stiffness law. The nearby discrete-cardinal model covers similar shape optimization but not the same dynamics or compliant law.

## value

PASS

A diffusive product model is a motivated exact test of runaway distortion at fixed volume. It distinguishes zero work on closed cycles from positive work along increasing anisotropy, and the elastic calculation gives both a finite, parameter-explicit onset and the scale of globally preferred large distortions. This goes beyond reusing the pressure formula alone, without claiming general dynamical buckling or behavior for spherical reorientation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
