# Self-review

## Correctness (PASS)
The determinant reduction applies to every complex input: \(F\) is unchanged under a unimodular Schur mask, and the two singular values are determined by \(F\) and determinant modulus. The arithmetic–geometric mean inequality gives the entire admissible product domain. In the complex plane the feasible output determinant forms an ellipse with explicitly computed semiaxes. Its radial maximization has two regimes; differentiating the resulting weak singular-value ratio yields a single global maximum at the transition. The explicit balanced matrix has the claimed singular values and attains the bound for every phase. The phase-zero gauge case, the negative phase branch, and the Hadamard endpoint are covered. Numerical samples and exact boundary identities give additional checks but do not establish universal correctness.

## Originality (PASS, subject to historical-priority risk)
Tian's full primary text treats the same target norm and gives a general finiteness criterion and nonsharp two-sided comparison with column approximation; it does not compute this phase-dependent two-dimensional optimum. Davidson and Donsig's full accessible treatment concerns Schur multiplier norms on bounded operators, not the weak Schatten target, so its symmetric-symbol norm formulas do not imply this weak-norm value. Banks–Harcharras studies idempotents on strong \(S_p\), \(p>1\). Semantic database searches using the exact phase formula and its Lorentz/Schatten and Hadamard aliases found related Schatten-four and rank-one phase results but no equivalent weak-Schatten classification. Lack of a search match is not a uniqueness proof: unindexed early finite-dimensional estimates remain a historical risk.

## Value (PASS)
This determines a complete natural, gauge-invariant one-parameter finite model of the new weak \((1,1)\) Schur multiplier problem, with an exact attainment example for each complex phase. The norm is not merely a standard first-coordinate matrix norm: the second singular value drives the optimum. The sharp transition from an ellipse-boundary to an interior optimizer explains why the weak endpoint responds quadratically to phase, whereas the ordinary trace norm already incurs a linear distortion. The answer supplies a precise benchmark for endpoint inequalities without asserting any unproved higher-dimensional generalization.

## Scope and risks
Only complex 2-by-2 symbols with every entry unimodular are treated. The result makes no assertion about complete or amplified weak norms, nonunimodular masks, or uniqueness of extremizers. Potential older equivalent finite-dimensional calculations are not ruled out.

Self-review: passed. Independent audit: not yet performed.
