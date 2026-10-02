# Mathematical audit — 2026-10-01

## Final claim assessed

A heightwise stationary-flux law for the Rössler system

## Correctness — PASS

PASS on the repaired claim. For every smooth compactly supported \(\psi\), invariance gives \(\int\psi'(z)[b+z(x-c)]\,d\mu=0\). Conditioning on height defines a compactly supported signed measure with zero distributional derivative, so it must vanish. This forces zero mass at \(z=0\) and \(\mathbb E[x\mid z]=c-b/z\) almost surely. Compact support makes the conditional mean bounded, which also justifies the integrated reciprocal-height consequence.

## Originality — PASS

PASS to the best of current knowledge on the repaired claim. The original package substantially overlapped a published 20 September 2026 Rössler theorem: that earlier complete result already contains the mean/variance parabola, covariance identities, compact-recurrence threshold, harmonic-height identity, endpoint rigidity, and critical unique invariant probability. The repair removes all of those as contributions. The earlier theorem does not state the conditional law \(\mathbb E[x\mid z]=c-b/z\), and its single integrated harmonic identity does not imply the family of test-function identities that determine the conditional mean.

### equivalent_formulations

Searches: Resultary: Rossler invariant measure stationary moment parabola conditional x given z critical rigidity; complete 2026/9/20 SCOPE-rossler-compact-recurrence-threshold-and-measure-laws--6e87f2d3c811

Evidence: The earlier complete theorem contains the integrated harmonic identity but no arbitrary-test-function or conditional-expectation statement.

Reasoning: The repaired conditional law is equivalent to vanishing stationary flux against every height test function, which is strictly stronger than one integrated reciprocal-height equation.

### broader_coverage

Searches: 20 September Rössler compact-recurrence theorem; Bramburger--Fantuzzi invariant-measure Rössler context

Evidence: The broader earlier Rössler result is expressly attributed for all global moment and threshold claims.

Reasoning: No inspected broader statement determines the full conditional mean at almost every height.

### exact_database_or_table

Searches: Resultary semantic search for Rössler conditional stationary flux

Evidence: No table is relevant and no earlier theorem-level match for the conditional law was found.

Reasoning: This is an analytic invariant-measure identity.

### claim_vs_prior_implication

Searches: earlier harmonic identity versus distributional stationary-flux proof

Evidence: A single value of \(\int 1/z\) does not determine \(\mathbb E[x\mid z]\). The repair uses all test functions \(\psi'(z)\).

Reasoning: The surviving statement is not a mechanical corollary of the prior global moment parabola.

## Scientific value — PASS

PASS. The conditional law is a natural structural refinement of the stationary moment equations for a canonical chaotic flow. It identifies the mean horizontal coordinate at every occupied height of any compact stationary state and can be used as a height-resolved diagnostic rather than only a global moment check.

## Source inspections

- **Exact compact-recurrence threshold and invariant-measure laws for the Rössler system** — https://github.com/Resultary/2026/tree/main/2026/9/20/SCOPE-rossler-compact-recurrence-threshold-and-measure-laws--6e87f2d3c811. Material read: Complete published RESULT.md, including proof, prior-work discussion and limitations. Assessment: DECISIVE_PARTIAL_COVERAGE_REQUIRING_REPAIR. Evidence: It already proves the global moment parabola, covariances, recurrence threshold, harmonic identity and critical rigidity, but not the conditional flux law.
- **Data-driven discovery of invariant measures** — https://doi.org/10.1098/rspa.2023.0627. Material read: The Rössler invariant-measure context as identified by the assigned package and indexed primary source; no whole-document noncoverage claim is made from snippets. Assessment: BACKGROUND_RESIDUAL_RISK. Evidence: The repaired novelty judgment rests chiefly on the complete earlier Rössler theorem and direct search for the conditional law.

## Checked sources

- Complete assigned Git package and exact symbolic identity artifacts.
- Independent distributional stationary-flux proof.
- Complete earlier 20 September Rössler theorem.
- Resultary and relevant invariant-measure literature searches.

## Limitations and residual risks

Assumes \(a,b,c>0\) and compact support. It does not classify stationary measures or imply pointwise trajectory relations.

- Older model-specific invariant-measure literature could contain an equivalent conditional flux identity under different terminology.
- The repair makes no novelty claim for the previously published moment parabola, recurrence threshold or harmonic identity.

## Disposition

**repaired**
