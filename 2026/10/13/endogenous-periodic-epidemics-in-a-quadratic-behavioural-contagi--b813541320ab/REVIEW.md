# Scientific review: endogenous periodic epidemics in a quadratic behavioural-contagion SIS model

## Correctness — PASS

The proof starts from equations (7)–(8) of Plank et al. under the original invariant independence condition. The exact reduction, the disease-free saddle, and the unique endemic equilibrium are checked algebraically. A strict derivative bound \(15185/28800>0\) excludes other endemic equilibria, and the exact endemic Jacobian has positive trace \(8387/52440\), positive determinant \(1075/6992\), and negative characteristic discriminant. The epidemic–behaviour system therefore has a hyperbolic interior repeller. The explicit barrier \(L=Ie^{-30B}\) rules out convergence to the boundary for every initially interior trajectory. A compact forward trapping rectangle and Poincaré–Bendixson then prove periodic \(\omega\)-limits, independently of numerical simulation. Hyperbolicity, root monotonicity, and the persistence barrier remain valid for nearby \(q_c<1\). The standard-library rational checker returned `VERIFY_OK`.

## Originality — PASS (restricted to the stated system and conclusion)

The motivating article's main model, appendices, parameter table, and associated numerical code were inspected. Its regime diagrams use \(\alpha=1/4\), \(\chi=1/5\); they do not demonstrate periodic solutions at the displayed parameter set. The stronger literature comparison is Zhou–Levin–Leonard's active-control SIS model, which proves oscillation in a heterogeneous four-dimensional risk-response setting, not this quadratic social-contagion two-dimensional model. The Ryan–Brindal–Roberts–Hickson precursor uses linear behavioural contagion, and the exact present result does not follow from its conclusions. Published mathematical records queried for the title, parameter tuple, behavioural SIS periodicity, equivalent models, and broader Hopf results returned no exact covering statement. This search is not a guarantee of absolute priority. The remaining source-version and broader-literature uncertainties are recorded in the structured review.

## Mathematical value — PASS

The source paper's ten-regime equilibrium classification gives a natural reason to test whether sustained periodic motion was overlooked. The theorem identifies a qualitatively different recurrent regime in the same two-variable model, with physically admissible positive parameters, no external seasonal forcing, and \(\tau<4\), where behaviour-only disease-free states are absent. Its global planar argument identifies sustained endogenous infection cycles for every interior non-equilibrium initial condition. The left-neighbourhood persistence in \(q_c\) shows the mechanism does not rely only on perfect protective behaviour. This is a substantive bifurcation boundary, not a routine recomputation of an existing fixed point.

## Closest prior results and limitations

Plank et al., arXiv:2604.10995v1, equations (7)–(8), Supplement S1.1–S1.3; associated public code `getPar.m`. Zhou, Levin, and Leonard, arXiv:2007.01424, Secs. 3–4 and Theorem 4.1; Ryan et al., J. R. Soc. Interface 21 (2024), 20240038. The proof does not determine the number, period, or stability type of all periodic orbits, and makes no empirical forecast. The observed source model may have later versions not yet evaluated. Results in unpublished or unindexed literature cannot be ruled out.

Self-review: passed. Independent audit: not yet performed.
