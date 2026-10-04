# Same-model review

## Correctness
PASS. Stationarity of \(x\), \(y\), \(x^2/2\), and \(xy\) reconstructs the mean identities and rigidity step. Averaging the \(z\)-equation gives the exact quadratic-plus-nonnegative-defect decomposition. The sign property \(z\operatorname{erf}(z)\ge0\) holds globally, with equality only at \(z=0\). The compact-set obstruction uses an invariant probability measure supported on a compact invariant set, so it is not inferred from finite simulation. Exact hidden-parameter arithmetic was independently replayed from the bundled checker.

## Originality
PASS. The closest source is the introducing Rasul–Salih article itself; its inspected sections provide equation (4.1), equilibria, local bifurcations, and numerical hidden/self-excited attractors but not the compact-recurrence threshold or invariant-measure defect identity. Searches for the exact error-function term, DOI, stationary-measure aliases, and mean/variance formulations found no same-system prior result. The closest published-finding corpus analogue is a Rössler variance-gap theorem, which has a different vector field and does not imply this result. Quadratic jerk papers checked for broader coverage do not include the nonpolynomial \(z\operatorname{erf}(z)\) term.

## Value
PASS. The result converts the source’s forcing/equilibrium discriminant into an exact global threshold for compact recurrent dynamics and gives a sharp, quantitative stationary envelope in the hidden-attractor regime. These conclusions materially sharpen the source’s numerical bifurcation picture and are useful for checking future simulations or invariant-state computations.

## Closest literature and limitations
The primary comparison is Rasul–Salih (2024), DOI 10.22436/jmcs.035.03.05. Additional comparisons are Liu–Sang–Wang–Ahmad (2021), DOI 10.3390/axioms10030227, and Llibre–Makhlouf (2025), DOI 10.1007/s00010-025-01182-5. The proof does not certify the numerical hidden attractor’s existence or ergodicity and does not classify every possible nonrecurrent compact set at the critical parameter. A residual originality risk remains for unindexed or unpublished work.

Same-model review: passed. Independent audit: not yet performed.
