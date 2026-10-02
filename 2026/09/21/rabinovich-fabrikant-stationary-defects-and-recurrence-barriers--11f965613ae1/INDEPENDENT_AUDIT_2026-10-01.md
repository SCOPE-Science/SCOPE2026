# Mathematical audit — 2026-10-01

## Final claim assessed

Heightwise stationary laws for the Rabinovich–Fabrikant flow

## Correctness — PASS

PASS. The repaired claim is correct. Direct differentiation gives the displayed radial and energy balances. The sign decomposition is valid. For the positive compact invariant component, invariance applied to cutoff antiderivatives with derivative \(\varphi(z)\chi_\varepsilon(z)/z\) gives \(\int\varphi(z)(\alpha+xy)=0\) for every bounded continuous test function, hence the conditional law. The conditional radial identity is algebraic. A second cutoff applied to \(\log R\), together with \(|xy|/R\le1/2\), yields the logarithmic-radial identity. These are analytic statements and do not rely on the symbolic artifact.

## Originality — PASS

PASS to the best of current knowledge on the repaired claim. The original package overclaimed novelty for the global off-plane mean and mean-height defect: the complete 20 September 2026 published Rabinovich--Fabrikant result already proves those identities, sign selection, and periodic-orbit consequences. The repair removes those as contributions. The earlier result does not state a conditional-in-height law or the logarithmic-radial stationary identity, and its global averages do not imply them. Resultary searches for the conditional law returned the repaired record and related but different stationary-balance results, with no earlier exact coverage located.

### equivalent_formulations

Searches: Resultary: Rabinovich Fabrikant invariant measure conditional xy given z stationary moment barriers recurrence; complete 2026/9/20 SCOPE-rabinovich-fabrikant-recurrence-sign-selection--047ddc1ae9fc

Evidence: The 20 September theorem gives \(\int xy=-\alpha\) and the mean-height defect but no identity tested against arbitrary functions of height.

Reasoning: The repaired statement is equivalent to vanishing of \(\int\varphi(z)(\alpha+xy)\,d\nu\) for every bounded continuous \(\varphi\); one global average is strictly weaker.

### broader_coverage

Searches: complete 20 September Rabinovich--Fabrikant recurrence result; original 1979 Rabinovich--Fabrikant model reference

Evidence: The earlier published recurrence theorem covers global balance and sign selection, which are now expressly treated as prior work.

Reasoning: No inspected broader result supplies the arbitrary-height test-function identity or the cutoff \(\log R\) identity.

### exact_database_or_table

Searches: Resultary semantic search for conditional stationary Rabinovich--Fabrikant identities

Evidence: No numerical database is relevant and no earlier theorem-level exact match for the repaired conditional law was found.

Reasoning: The claim is an invariant-measure identity, not a tabulated invariant.

### claim_vs_prior_implication

Searches: 20 September global recurrence law versus repaired cutoff-generator proof

Evidence: The prior law fixes \(\int xy\) only. The repaired proof uses all test functions of \(z\), which is additional information not recoverable from that scalar equality.

Reasoning: The surviving conditional theorem is not mechanically implied by the earlier global balance.

## Scientific value — PASS

PASS. A heightwise conditional stationary law is a structural refinement of a global average: it constrains every occupied height of an arbitrary compact stationary state. The logarithmic-radial identity supplies a second independent exact stationary flux. These are natural diagnostics for a standard three-dimensional flow and are not merely a renamed global balance.

## Source inspections

- **Recurrence sign selection and mean-height law for the Rabinovich--Fabrikant system** — https://github.com/Resultary/2026/tree/main/2026/9/20/SCOPE-rabinovich-fabrikant-recurrence-sign-selection--047ddc1ae9fc. Material read: Complete published RESULT.md, including theorem, proof, prior-work discussion and limitations. Assessment: DECISIVE_PARTIAL_COVERAGE_REQUIRING_REPAIR. Evidence: It already proves the global off-plane balance, mean-height defect, sign selection and periodic consequences, but not the repaired conditional law.
- **Stochastic self-modulation of waves in nonequilibrium media** — https://www.jetp.ras.ru/cgi-bin/dn/e_050_02_0311.pdf. Material read: Bibliographic and model context from the assigned package; no whole-document noncoverage claim is based on this source in this audit. Assessment: BACKGROUND_RESIDUAL_RISK. Evidence: Original model provenance is prior art; originality of the repaired conditional law rests primarily on direct comparison with the stronger later recurrence theorem and targeted published-record search.

## Checked sources

- Complete assigned Git package and artifact tree at the frozen snapshot; current directory entries exactly matched the frozen tree.
- Independent Lie-derivative, cutoff-generator and logarithmic-radial proof reconstruction.
- Complete earlier 20 September Rabinovich--Fabrikant recurrence result.
- Resultary semantic search for conditional and global stationary-balance aliases.

## Limitations and residual risks

Requires \(\alpha,\gamma>0\) and compact support. The laws are stationary identities, not pointwise trajectory laws; existence or uniqueness of nontrivial invariant states is not asserted.

- Older Russian-language or model-specific work may contain an equivalent conditional stationary identity under different terminology.
- The repair deliberately makes no novelty claim for the previously published global mean-height or periodic-orbit barriers.

## Disposition

**repaired**
