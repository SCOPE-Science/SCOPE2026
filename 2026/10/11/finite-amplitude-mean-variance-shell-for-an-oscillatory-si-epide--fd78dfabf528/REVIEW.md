# Same-model review

## Correctness
PASS. The proof uses three generator identities valid for compactly supported invariant measures inside the strict positive region: stationarity of \(Y\), stationarity of \(Y^2/2\), and stationarity of \(\log X\). These give \(n\bar Y+\bar X=m\), \(\operatorname{Cov}(X,Y)=-n\operatorname{Var}(Y)\), and the exact finite-amplitude mean–variance law. Factoring the endemic-equilibrium quadratic gives the variance-gap shell. The equality case is rigid because simultaneous zero variance in \(X\) and \(Y\) makes the invariant measure an equilibrium atom. The packaged symbolic checker reproduces the algebra and the exact source-example roots.

Risk: the invariant-measure argument requires support compactly contained in \(X>0\); it does not cover measures charging the infection-free boundary.

## Originality
PASS. The complete Zeng–Yu source was inspected at the model, equilibrium, Hopf, and numerical-example sections. It develops the bifurcation diagram and limit cycles but does not state a stationary mean–variance identity, a factorized variance gap, or a finite-amplitude mean trap between endemic infective coordinates. Searches using the exact vector field, nonlinear-incidence terminology, periodic-orbit averages, invariant measures, variance defects, and the two-endemic-equilibrium formulation returned no statement implying the claim. The closest indexed research records concern unrelated epidemic, Rössler, or generic recurrence systems.

Risk: the 2007 introducing article for the same epidemic model was accessible only at abstract level, so a differently phrased equivalent finite-amplitude average identity there cannot be completely excluded.

## Value
PASS. The source's central phenomena are Hopf cycles and bistability. The new law supplies a global finite-amplitude constraint on every compact recurrent state in the same bistable regime: the cycle's mean infective coordinate cannot drift beyond either endemic branch, and its distance from the branches exactly measures the combined variance \(V_X+nV_Y\). This is useful for interpreting simulations and data because it links an observable mean directly to oscillation amplitude without a small-cycle approximation.

Risk: the result is diagnostic rather than an existence theorem; it does not determine cycle period or stability.

Same-model review: passed. Independent audit: not yet performed.
