# Scientific review

**Correctness — PASS.** The source's normalized half-edge infection probability and equal per-degree recruitment imply disease-free class sizes \(\Lambda/\mu\). Differentiating the quotient and incidence proves cancellation of that class-size factor. Constant positive clearance rates give an exact six-dimensional closed ODE; direct rational differentiation produces a Hurwitz Jacobian with spectrum \(\{-1,-1/6,-1/2,-1/2,-1/2,-1/2\}\), while the source's printed threshold is \(5/3>1\). The executable checks the complete Jacobian, not just a purported finite simulation of the infection-age model.

**Originality — PASS.** The primary paper's actual sections 2–3 and appendix were read, including its conflicting contact and reproduction formulas. A source-specific search and semantic comparisons with published related epidemic-threshold findings did not identify this exact normalization contradiction or this local-stability reversal. The same second-moment/first-moment factor is classical; no novelty for that generic factor is claimed. Residual risk: other normalizations in the literature could be implicitly intended, but would require changing the model's explicit definition; an undiscovered independent source may already have identified this conflict.

**Value — PASS.** A source theorem uses the printed quantity to distinguish local extinction from invasion. The admissible example flips that binary stability verdict, a substantive mathematical boundary relevant to interpreting bifurcation and control thresholds. The result is not a numerical rounding observation or a routine special-case corollary of the source's actual statement.

**Limitations.** Correctness of the *literal normalized-contact equations* does not resolve the authors' intended alternative variable convention, the nonlinear global outcomes, or the empirical simulations. No independent audit has been carried out.

Self-review: passed. Independent audit: not yet performed.
