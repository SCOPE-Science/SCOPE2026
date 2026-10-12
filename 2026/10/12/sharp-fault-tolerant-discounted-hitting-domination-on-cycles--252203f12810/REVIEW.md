# Scientific review: Sharp fault-tolerant discounted hitting domination on cycles

## Correctness — PASS

The underlying source potential is determined by the unique solution to a two-boundary discount recurrence. Every possible failure pattern merges original cyclic gaps into consecutive blocks of size at most \(f+1\), and every such maximal block can be realized by an adversarial choice. This proves the exact window condition, including the boundary with a single surviving source. Summing all windows proves the lower bound \(kL\ge(f+1)n\). A periodic balanced floor-difference construction realizes the lower bound at every permitted parameter choice. The transfer trace and root-count identity then count every labeled optimum set, including rotationally periodic patterns without overcounting.

Exact-rational tests solved 3,027 pinned potential systems, accounted for 57,345 adversarial failures, checked 948 threshold/failure profiles and 194,796 membership decisions, and independently verified all minimum counts. A separate transfer-matrix verifier checked 374 coefficient profiles. These finite calculations corroborate an all-orders analytic proof and are not treated as proof by extrapolation.

## Originality — PASS with residual risk

Allagan, Pereyra and Massey, arXiv:2609.31535v1, Lemma 5.5 already establishes the ordinary segment gap values and their monotone cutoff. This part is credited. The authors' Section 9 explicitly proposes robustness when sources fail as further research, whereas Sections 6–7 solve ordinary placement on spiders, stars and complete graphs. None supplies the cyclic adversarial-window criterion, closed all-f minimum, balanced construction, or labeled optimum enumerator. Searches of alternative names (penalized/group hitting, source resilience, fault tolerance, cyclic windows), published research results, and relevant mathematical comparisons did not identify a covering theorem. Search absence is not a novelty certificate; unindexed equivalent work remains a risk.

## Value — PASS

Fault tolerance is directly motivated by the origin of the discounted-hitting invariant. The result gives a sharp feasibility boundary \(\tau\le\psi_{f+1}\), an exact optimum for every graph order and failure budget, a constructive description of all feasible/optimal configurations, and an exact finite transfer-matrix enumerator of optimizers. This is a natural complete classification, not a selected small-parameter computation or a mere restatement of the ordinary two-boundary lemma. Its sharp parameter transitions and optimal configuration counts provide useful benchmarks for failure-resilient source placement.

## Scope and limitations

This theorem concerns cycles with homogeneous simple random walks and source-status loss, not edge/vertex destruction or heterogeneous attenuation. The dynamic count is exact but its matrix dimension may grow rapidly with the failure budget. External novelty remains subject to further literature indexing and independent specialist assessment.

Self-review: passed. Independent audit: not yet performed.
