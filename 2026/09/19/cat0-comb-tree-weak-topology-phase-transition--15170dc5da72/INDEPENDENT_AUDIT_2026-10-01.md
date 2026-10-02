# Independent mathematical audit — 2026-10-01

Record: `SCOPE-20260919-15170dc5da72`

## Correctness — PASS

The proof reconstructs directly from tree geometry. The comb is proper because every bounded ball meets only finitely many attachment sites and compact subsegments. A pointwise limit of internal metric functionals either has attachment coordinate tending to infinity, in which case it is exactly the unique-end Busemann function \(b=r-p\), or has a bounded subnet and is internal by properness. For each fixed internal functional, \(h_w(x_n)=n+L_n-2p(w)\) eventually tends to \(+\infty\), while \(b(x_n)=L_n-n\); this gives the exact endpoint limit set. The compact-range net lemma is valid by passing a nonconvergent subnet to a metric cluster point and testing its internal functional. If \(L_n-n\to-\infty\), every Busemann superlevel neighborhood is bounded and the two topologies coincide; otherwise an escaping endpoint subsequence has at least two limits. At \(L_n=n\), every point is a limit, implying hyperconnectedness, while the internal-functional separation gives \(T_1\).

### Correctness sources

- assigned RESULT.md
- earlier published SCOPE precompact-rigidity/horoball theorem
- Gutiérrez–Nevanlinna metric-functional topology papers

### Correctness risks

- The phase criterion is only for the explicit one-ended comb family, not arbitrary CAT(0) trees.

## Originality — PASS

An earlier published SCOPE result already proves that totally bounded sets are rigid for this topology and constructs a proper binary CAT(0) tree with arbitrary Busemann-horoball limit sets, including a universal-limit sequence. Thus proper CAT(0) non-Hausdorffness and universal convergence are prior coverage. The surviving claim is the exact one-ended comb classification: the full compactification has one boundary functional, the endpoint limit set has threshold \(\liminf(L_n-n)\), and the whole topology is metric exactly when \(L_n-n\to-\infty\). The earlier branching-tree theorem does not imply that global iff criterion for this family.

### equivalent_formulations

Searches:
- Resultary semantic search for CAT(0) comb metric-functional weak topology and Hausdorff phase transition
- comparison with SCOPE-precompact-rigidity-horoball-d-weak-tree--1ccb209e76ce

Evidence:
- The earlier result has a binary tree and arbitrary horoball limit sets; the audited result has a one-ended comb and an exact sequence-parameter iff criterion.

Reasoning:
Equivalent formulations via Busemann heights, exact d-weak limit sets, and equality/non-Hausdorffness of the topology were compared.

### broader_coverage

Searches:
- SCOPE-precompact-rigidity-horoball-d-weak-tree--1ccb209e76ce
- Gutiérrez–Nevanlinna topology source

Evidence:
- The earlier theorem covers bounded/precompact rigidity and existence of CAT(0) pathologies, but not the comb phase boundary.

Reasoning:
This is substantial partial broader coverage, not domination of the final comb theorem.

### exact_database_or_table

Searches:
- current Resultary metric-functional topology records

Evidence:
- No table or database entry gives the comb threshold \(L_n-n\); theorem-level comparison is the relevant check.

Reasoning:
The claimed invariant is an infinite-family topological criterion, not a table lookup.

### claim_vs_prior_implication

Searches:
- statement implication from binary-tree horoball theorem to one-ended comb

Evidence:
- The binary-tree construction uses many boundary Busemann functions; the comb compactification has exactly one boundary function and needs a separate global bounded-superlevel argument.

Reasoning:
The earlier result does not mechanically imply the comb iff condition.

### source_inspections

- **Precompact rigidity and horoball limit sets for metric-functional weak convergence** — https://github.com/Resultary/2026/tree/main/2026/9/18/SCOPE-precompact-rigidity-horoball-d-weak-tree--1ccb209e76ce. Trigger: Closest prior SCOPE result on proper CAT(0) trees. Material read: Complete published RESULT.md. Method: Full theorem and proof implication comparison. Assessment: PARTIAL COVERAGE only. Evidence: It proves precompact rigidity and binary-tree horoball/universal-limit phenomena, but no one-ended comb phase transition.
- **A Weak Topology on Metric Spaces** — https://arxiv.org/abs/2609.19368. Trigger: Primary source defining the topology. Material read: Accessible abstract/scope material and the source statements quoted in the assigned package; full arXiv text was not available through the attempted route in this run. Method: Scope comparison with access limitation recorded. Assessment: Background source, not decisive coverage. Evidence: It introduces the topology and supplies non-Hausdorff examples outside the audited comb classification.

### checked_sources

- assigned RESULT.md
- SCOPE-precompact-rigidity-horoball-d-weak-tree--1ccb209e76ce
- arXiv:2609.19368
- DOI 10.4171/ZAA/1828
- Resultary semantic search

### residual_risks

- The motivating topology paper is extremely recent, so unindexed parallel work remains possible.

## Scientific value — PASS

The exact Hausdorff/metric threshold on a natural one-ended proper CAT(0) family is a meaningful structural boundary. Prior work already shows CAT(0) pathologies can occur, but this theorem identifies precisely when they disappear and when they become maximally non-Hausdorff inside a simple parameterized family.

### Value sources

- earlier CAT(0) horoball theorem
- assigned comb classification

### Value risks

- The result does not classify arbitrary or multi-ended trees.

## Limitations

- The global iff criterion is restricted to the one-ended comb family.
- Proper CAT(0) non-Hausdorffness and universal-limit sequences themselves are prior covered phenomena; the accepted originality is the exact comb phase classification.
- Originality is best-of-knowledge for a very recent topology.

## Disposition

**PASSED**
