# Scientific review

## Correctness — PASS

All real parameters and the two-vertex case are covered. Exact Laplacian-power identities yield the hub-to-leaf cubic and leaf-to-leaf quadratic. An explicitly positive discriminant certificate makes all leaf-to-leaf entries positive and orders the hub-to-leaf cubics strictly by conductance. A separate exact normalized-polynomial certificate proves every cubic decreases strictly; a spectral argument handles all diagonal entries. The proof identifies the first and only loss of matrix positivity, including tied heaviest spokes. Exact symbolic and rational direct-matrix checks were replayed from `verify.py`; sampled tests are not used as infinite proofs.

## Originality — PASS, with risk

The closest inspected primary preprint, Ketcheson–Gottlieb–Macdonald, arXiv:1106.3626v1, develops general SSP theory for two-step Runge–Kutta formulas, whereas this result concerns the sharp endpoint positivity of the **classical four-stage RK4 stability polynomial** on every positively weighted star. General SSP sufficiency does not imply the necessary-and-sufficient cubic threshold, strict ordering by maximum edge weight, or strict improvement over forward Euler. Related archived findings concern third-order explicit RK on unweighted trees, fourth-order Gauss Padé on weighted stars, and Radau on unweighted stars; their formulas do not imply this one. Searches for weighted-star RK4, Taylor-polynomial alias, completed heat step, and maximum-spoke threshold found no covering theorem. Incompletely indexed specialized sources remain an originality risk; negative search results do not prove uniqueness.

## Value — PASS

A non-SSP fourth-order integrator can still have a sharp problem-specific nonnegativity horizon. The theorem gives a complete, non-asymptotic CFL criterion for every positive weighted star, shows that arbitrary heterogeneity never causes a leaf-to-leaf negativity or multiple separated timestep windows, and determines precisely which edges first fail using only the maximum conductance and three global power sums. This is a natural reusable numerical-safety result, not a table of isolated small cases.

## Limitations

The classification applies to the completed classical RK4 linear diffusion step on positively weighted stars. It does not certify intermediate stages, other Runge–Kutta formulas, arbitrary graphs, or historical uniqueness.

Self-review: passed. Independent audit: not yet performed.
