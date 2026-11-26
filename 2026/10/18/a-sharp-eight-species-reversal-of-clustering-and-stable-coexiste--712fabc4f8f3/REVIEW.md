# Independent mathematical audit

## correctness

PASS

For cubic A, A1=3·1 gives the positive equilibrium 1/(1+3tau) at every tau>=0. Its Jacobian is -(I+tau A)/(1+3tau). At any positive equilibrium the negative diagonal-times-symmetric Jacobian is similar to the negative symmetric congruence by diag(sqrt(x)); hence inertia excludes strict linear asymptotic stability at or above -1/lambda_min. Below that boundary the displayed Lyapunov derivative is -(x-x*)^T(I+tau A)(x-x*), strictly negative off equilibrium, with compact positive sublevel sets, establishing convergence among positive states. Since mean local clustering is T/n for cubic degree, the comparison is exactly triangle count against -1/lambda_min. An independent exhaustive degree recursion, full relabeling orbits, integer characteristic coefficients and exact rational Sturm bounds reproduced (all labeled, connected labeled, connected orbits)=(1,1,1),(70,70,2),(19355,19320,5) at 4,6,8. Cubic orders are even and at least four; the prism ranks above K3,3 both in triangles and stability. At eight the thresholds for 4,2,1 triangles are 1/sqrt(5), sqrt(2)-1, 2/(1+sqrt(17)), and the two triangle-free classes give sqrt(2)-1 (Wagner) and 1/3 (cube). Their exact order is 1/3 < 2/(1+sqrt(17)) < sqrt(2)-1 < 1/sqrt(5); the tie between Wagner and the two-triangle class is not an inversion. This identifies the single inverse pair. The switch deletes 15,24 and adds 12,45; H has exactly triangle 012. The difference of slowest linear decay rates is tau times the positive difference of the two least eigenvalues divided by 1+3tau, equal to the displayed expression throughout the common positive stable interval. Both abundances are the same by regularity. Independent replay source: /workspace/branches/0987e4af-274f-4971-a8d3-5142a45cae7f/census.py, with exact outputs census_n4.json, census_n6.json, census_n8.json in that directory. No frozen script was executed.

## originality

PASS

Credit the exact minimum and unique inverse pair for the connected cubic class, with the explicit one-switch witness. The model, spectral ingredients, small graph orbit counts, and Wagner spectrum are prior background. The inspected positive-association result is statistical, the exact existing graph table concerns a different invariant, and the adjacent six-species reversal is noncubic. None provides the same cubic inverse-ordering classification.

## value

PASS

This is a motivated counterexample to using higher clustering as a monotone proxy for robustness in a fixed-degree family, without disputing the measured average association. Holding regular degree fixed removes feasibility and abundance changes and isolates the stability comparison. The sharp small order, uniqueness and single-switch realization give a reusable test case; the return-rate inequality extends its interpretation to the entire shared stable interval.

The dated certificate retains the supplied scientific assessment, sources and limitations.
