# Scientific review

## Correctness — PASS

For the stated exact quadratic and projector-oracle algorithms, expand the one-sided finite differences into the residual-linear term and the Gaussian cubic noise term. Wick moments give the exact coupled moment recurrences displayed in `RESULT.md`; their spectral coefficients are \(s=(1-\alpha)^2\) and \(r=1-2\alpha+(q+2)\alpha^2\). The nonzero finite-radius noise makes the boundary \(r=1\) genuinely unbounded, while \(r<1\) yields the explicit positive fixed points. Strict floor separation follows from \(C_d>C_q\); the \(d^3\) ratio follows by algebra for fixed \(q\). Standalone exact Gaussian-polynomial tests for three configurations and deterministic 20,000-path seeded diagnostics independently support the calculations. Correctness is established by algebra rather than by finite numerical experiments.

## Originality — PASS, with residual risk

The benchmark one-sided control-variate estimator and its qualitative cubic smoothing bound already appear in Ryabchenko–Qian–Mou (arXiv:2609.08277v1, §3.1 and Appendix C). The sharp Gaussian residual contraction threshold also appears in partial-gradient stochastic optimization literature, including Chayti–Mirrokni–Jaggi (arXiv:2610.13871v1, Appendix B, Lemma 5). Accordingly, originality here is restricted to the **exact finite-\(\tau\) stationary second-moment formulas and equal-query full-versus-complement support ratio** for the specified oracle-projection quadratic dynamics. The first paper treats ambient Gaussian control variates and general nonconvex guarantees; the second uses a distinct residual-tracking method and central finite differences. Comparing their mathematical assertions and inspected derivations did not identify the exact combined statement. Indexed mathematical research-record searches with exact estimator aliases and formulas found related stochastic subspace and momentum results but no covering item. A specialized older estimator calculation outside the inspected sources could still imply the formulas, so this assessment is not a certificate of unprecedented publication.

## Mathematical value — PASS

The source estimator deliberately uses an exact projection-based reference to remove stochastic residual-gradient variance, but its finite-difference perturbation still ranges over all ambient coordinates. The result identifies the exact stationary consequence and shows that a fixed \(q\)-dimensional unknown gradient can coexist with a cubically growing ambient-dimension error penalty at the same one-perturbed-evaluation budget, while an elementary change of probe support avoids that penalty. The floor ratio and sharp stability window permit quantitative smoothing-radius/stepsize design; this is a complete small-model phase calculation, not a renaming of an estimator or a routine qualitative variance bound.

## Boundaries and sources

The result assumes a globally unbounded-gradient quadratic and thus is not a counterexample to [1]'s bounded-gradient theorem. It makes no assertion for arbitrary nonquadratics, adaptive references, changing projectors, or central differences. Source [2] explicitly covers the standard Gaussian contraction mechanism; that mechanism is not presented as new. The comparison depends on holding the coordinate scale \(\tau\) fixed; matched expected probe norms would define another optimization problem. Residual bibliographic risk concerns potential earlier moment identities and variance-reduced finite-difference algorithms not indexed by the searches.

Self-review: passed. Independent audit: not yet performed.
