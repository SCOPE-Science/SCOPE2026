# Independent mathematical audit — 2026-10-01

Record: `SCOPE-20260918-4bfe5c340ddd`

## Correctness — PASS

The topology comparison is valid. Metric functionals on a normed space are convex and one-Lipschitz, so each sublevel set is norm-closed convex and therefore weakly closed by Hahn–Banach separation; every basic metric-functional superlevel neighborhood is weakly open, giving \(\tau_\diamond\subseteq\tau_w\). Walsh's singleton-Busemann characterization puts every extreme dual-ball functional, and its negative, in the metric-functional compactification; lower semicontinuity of both signs makes each extreme functional \(\tau_\diamond\)-continuous. If their algebraic span is the full dual, every continuous linear functional is continuous for \(\tau_\diamond\), yielding the reverse inclusion. Finite-dimensional dual balls satisfy the span condition by Krein–Milman, and strictly convex duals do so because every unit vector is extreme. The direct internal-functional separation proves the general \(T_1\) claim.

### Correctness sources

- Gutiérrez–Nevanlinna, arXiv:2609.19368
- Gutiérrez–Nevanlinna, DOI 10.4171/ZAA/1828
- Walsh, DOI 10.5802/aif.3198
- assigned RESULT.md

### Correctness risks

- The extreme-span condition is sufficient, not proved necessary.
- The strict C[0,1] example depends on the source's unbounded metric-functional convergent sequence.

## Originality — PASS

The new topology paper establishes its convergence theory, normed-space Hausdorffness, and an unbounded C[0,1] convergent sequence, while the earlier paper supplies sequence-level weak-convergence results. No inspected source states the full topology inclusion, the extreme-span equality criterion for arbitrary nets, or the finite-dimensional equality theorem.

### equivalent_formulations

Searches:
- arXiv:2609.19368 full text
- DOI 10.4171/ZAA/1828
- Walsh extreme dual/Busemann point theorem

Evidence:
- The source topology paper does not state the audited comparison with the classical weak topology.
- Walsh identifies extreme dual points as singleton Busemann points, supplying an ingredient rather than the final topology theorem.

Reasoning:
The sequence formulation and topology formulation were compared separately, because sequence equivalence does not in general imply equality of non-first-countable topologies.

### broader_coverage

Searches:
- Gutiérrez–Nevanlinna sequence result under strictly convex dual
- Kell co-convex topology

Evidence:
- Those results concern sequence convergence or a different weak topology.

Reasoning:
They do not imply the arbitrary-net equality criterion for this metric-functional topology.

### exact_database_or_table

Searches:
- functional-analysis topology tables and exact criterion searches

Evidence:
- No exact database/table entry for the extreme-span criterion was located.

Reasoning:
This result is theorem-level and not naturally table-driven.

### claim_vs_prior_implication

Searches:
- implication comparison with bounded-sequence weak equivalence

Evidence:
- Bounded-sequence equivalence cannot imply equality of the full topologies; the source itself exhibits unbounded metric-functional convergence in C[0,1].

Reasoning:
The audited result genuinely adds topology-level information.

### source_inspections
- **A Weak Topology on Metric Spaces** — https://arxiv.org/abs/2609.19368. Trigger: Immediate source defining the topology. Material read: Full accessible preprint, including topology definition, convergence theorem, normed-space separation discussion, and C[0,1] example. Method: Primary full-text statement comparison. Assessment: Does not state the extreme-span equality theorem. Evidence: It develops the new topology and supplies the strictness example used here.
- **Hilbert and Thompson geometries isometric to infinite-dimensional Banach spaces** — https://doi.org/10.5802/aif.3198. Trigger: Extreme dual points as metric/Busemann functionals. Material read: Corollary-level full-text material identifying singleton Busemann points with extreme dual-ball points. Method: Primary theorem comparison. Assessment: Supplies the key representation lemma, not the topology comparison. Evidence: Corollary 3.5 gives the extreme-point characterization.

### checked_sources

- https://arxiv.org/abs/2609.19368
- https://doi.org/10.4171/ZAA/1828
- https://doi.org/10.5802/aif.3198
- assigned RESULT.md

### residual_risks

- The topology preprint is very recent, so unindexed parallel observations remain possible.

## Scientific value — PASS

The theorem positions a newly introduced weak topology relative to the classical weak topology, gives exact recovery on broad natural classes including all finite-dimensional spaces and spaces with strictly convex dual, and identifies genuine strictness in C[0,1]. The arbitrary-net statement is stronger and more useful than a sequence-only observation.

### Value sources

- arXiv:2609.19368
- Walsh's extreme-dual characterization

### Value risks

- The condition is not a characterization of every space with equality.

## Limitations

- The extreme-span condition is sufficient, not necessary.
- No general characterization for C(K)-type spaces is claimed.
- Originality is best-of-knowledge for a very recent topology.

## Disposition

**PASSED**
