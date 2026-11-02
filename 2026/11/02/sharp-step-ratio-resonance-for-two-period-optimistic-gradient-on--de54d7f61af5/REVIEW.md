# Scientific review

## Correctness — PASS
The complexification of the real two-dimensional bilinear operator yields a two-component recurrence with period matrices \(T(h)\). Multiplying the matrices gives trace \(1-4uv-i(u+v)\) and determinant \(-uv\). The quadratic Schur–Cohn criterion gives both the necessary \(uv<1\) condition and the exact positive margin \(\Delta(u,v)>0\). The proof also treats \(\Delta=0\), the constant-step limit, and the equality cases of the small-step ratio. Exact rational substitution and finite eigenvalue computations from the distributed Python checker corroborate these identities. No finite test is used to infer the universal or asymptotic conclusions.

## Originality — PASS (qualified)
The closest constant-step OGDA results are Anagnostides–Penna (arXiv:2010.03211, Theorem 3.1) and de Montbrun–Renault (arXiv:2208.03085, Section 2); neither states a stability set for two different alternating learning rates. Alacaoglu–Böhm–Malitsky (arXiv:2212.13955, Sections 2 and 4) establish fixed-step equivalence of OGDA with golden-ratio methods and analyze a *different* adaptive algorithm. The two-period Floquet boundary and the vanishing-scale \(2\pm\sqrt3\) step-ratio obstruction are not covered by the identified claims. Accessible public mathematical records were checked for alias formulations. A more general older variable-coefficient multistep theorem may imply the criterion; that is a remaining priority risk.

## Value — PASS
Variable learning rates are a natural change to a stabilizing optimistic-gradient solver. The result shows that individually stable, even arbitrarily small, steps do not ensure convergence of the naive step-scaled historical-gradient rule. A sharp necessary-and-sufficient two-period stability region and an exact nontrivial ratio threshold explain this genuinely structural failure and distinguish naive substitution from guarded adaptive algorithms. This is not asserted as a convergence analysis for those guarded algorithms.

## Limits and nearby work
The model is a single unconstrained bilinear saddle in exact arithmetic, with positive deterministic period-two steps. No nonperiodic, nonlinear, stochastic, or finite-precision extension is claimed. Classical Schur stability and fixed-step OGDA convergence are prior mathematical ingredients. Independent priority and proof validation have not been performed.

Self-review: passed. Independent audit: not yet performed.
