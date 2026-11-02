# Scientific review

## Correctness — PASS

The source's hypergraph dynamics reduce exactly to the scalar cubic recurrence for the specified unit-sum interactions. Under the strict step bound the recurrence is increasing, preserves \((r,1]\), and approaches the endemic double root from above at rate \(1/(h\kappa rt)\). A factored Vandermonde identity proves finite-time full rank and the universal determinant asymptotic. Centered rows and the nonzero cross product \(v(r)\times v'(r)\) prove the second singular-value asymptotic; the determinant gives the third. Exact rational checks reproduce the determinant identity and model-parameter recovery. The decimal trajectory is a sanity check, not an infinity proof.

## Originality — PASS with residual risk

The direct motivating full text (Liang--Cui--Liu, arXiv:2408.08602v1, Section 4) states its three-parameter least-squares design and the ordinary full-column-rank requirement, but no critical-fold determinant or sharp condition-number decay. Kiss--Simon, arXiv:2208.07543v1, studies continuous SIR/pairwise-model identification from growth and final size; Landry--Restrepo, arXiv:2006.15453v2, studies higher-order contagion folds without the proposed sampling-design theorem. Mathematical-record comparisons found different SIS convergence/bifurcation, SIR identification, and critical dynamics claims but none implies the three-rate time-window asymptotics. The Vandermonde factor itself is classical; existing specialized numerical-analysis or unindexed epidemic-inference literature might implicitly cover this specialization, so priority remains uncertain.

## Mathematical value — PASS

The originating parameter-learning framework explicitly requires a rank condition, but it does not quantify how the observation horizon affects reliable inference. This theorem identifies a natural and biologically motivated difficult regime, an endemic fold where prevalence stabilizes algebraically, and simultaneously establishes strict noiseless identifiability and the exact sixth- and fourth-power losses of numerical stability. The determinant leading factor is universal across step sizes, pairwise rates, and initial conditions. The result informs choice of measurement windows, without asserting statistical confidence bounds.

## Scientific limitations

Only a homogeneous three-agent diagonal invariant subsystem and three consecutive regression rows are treated. The unscaled three-rate design does not characterize constrained fold-aware or noisy-data estimators. Independent validation of mathematics, novelty, or publication priority has not occurred.

Self-review: passed. Independent audit: not yet performed.
