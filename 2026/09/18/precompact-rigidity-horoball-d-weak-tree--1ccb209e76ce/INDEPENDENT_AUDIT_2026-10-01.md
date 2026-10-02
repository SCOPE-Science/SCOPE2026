# Independent audit — 2026-10-01

## Final claim

Precompact rigidity and horoball limit sets for metric-functional weak convergence

## Correctness — PASS

On a totally bounded set, a finite \(r/4\)-net of points outside \(B(x,r)\) supplies internal functionals whose values drop by more than \(r/2\) at every such point, so every metric neighborhood contains a relative metric-functional weak neighborhood. This proves equality of the two subspace topologies and the proper-space bounded-convergence corollary. For the locally finite binary \(\mathbb R\)-tree, every pointwise limit of internal functionals is either another internal functional or an end Busemann functional: properness handles bounded subnets and compactness of the end space handles escaping subnets. The explicit rays \(0^{n-1}1\ldots\) with radial length \(2(n-1)+C\) keep exactly one Busemann functional at level \(C\) while all others diverge, yielding precisely the horoball; radial length \(3n\) makes every metric functional diverge and hence gives every point as a d-weak limit.

## Originality — PASS

The motivating metric-functional topology paper proves the topology/convergence equivalence and gives non-Hausdorff every-point phenomena on a snowflaked real line, while earlier CAT(0) weak-topology work concerns a different projection/Delta notion. No inspected source or earlier published record states the total-boundedness rigidity theorem, exact Busemann-horoball realization, or an every-point sequence in a proper CAT(0) tree. Later published tree refinements postdate this record and therefore do not cover its originality at publication time.

### Equivalent formulations

Searches/sources: Gutiérrez Nevanlinna d-weak topology metric functionals; horofunction weak convergence CAT(0) tree.

Evidence: The source uses the same internal metric functionals and the same liminf definition of d-weak convergence.

Reasoning: The audited topology-rigidity and tree-horoball statements are direct statements in that same notion, not terminological variants of the established projection weak topology.

### Broader coverage

Searches/sources: A Weak Topology on Metric Spaces arXiv:2609.19368; Lytchak Petrunin Weak topology on CAT(0) spaces.

Evidence: The first source proves general topology facts and examples; the second studies a distinct CAT(0) weak convergence.

Reasoning: Neither broader theory determines the audited exact limit sets in the binary tree or the equality on every totally bounded subset.

### Exact database or table

Searches/sources: published SCOPE index: metric functional weak CAT(0) tree horoball; precompact rigidity d-weak.

Evidence: No earlier exact record was located; a sharper comb-tree phase-transition record appears only on 2026-09-19.

Reasoning: The later record cannot serve as prior coverage for this 2026-09-18 result.

### Claim versus prior implication

Searches/sources: Gutiérrez–Nevanlinna non-Hausdorff examples; proper CAT(0) weak topology literature.

Evidence: Known every-point examples occur in different spaces, and known CAT(0) weak topology is a different convergence notion.

Reasoning: Those results do not mechanically imply that a proper CAT(0) binary tree has every-point d-weak sequences or exact Busemann-horoball limit sets.

## Scientific value — PASS

The two theorems identify a sharp geometric mechanism: precompactness suppresses the weak/metric discrepancy, while escape to infinity can create maximal nonuniqueness even in a proper complete CAT(0) tree. Exact horoballs as limit sets provide a reusable model family, not merely a one-off pathology.

## Sources inspected

- **A. W. Gutiérrez and O. Nevanlinna, A Weak Topology on Metric Spaces** (https://arxiv.org/abs/2609.19368): FOUNDATIONAL_CONTEXT_NOT_EXACT_COVERAGE. The paper supplies the d-weak topology and examples but not the precompact equality theorem or the proper-tree horoball constructions.
- **A. Lytchak and A. Petrunin, Weak topology on CAT(0) spaces** (https://doi.org/10.1007/s11856-022-2420-5): DIFFERENT_NOTION. It concerns projection/Delta-type CAT(0) weak convergence, not the metric-functional liminf topology used in the audited result.

## Residual risks and limitations

- The universal-limit construction is proved for the regular binary tree, not for arbitrary proper CAT(0) spaces.
- The motivating topology preprint is recent, leaving a residual risk of unindexed parallel work.

## Disposition

**passed**
