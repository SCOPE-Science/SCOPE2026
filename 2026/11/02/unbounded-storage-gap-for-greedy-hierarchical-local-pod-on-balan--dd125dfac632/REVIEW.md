# Scientific review

## Correctness — PASS

For \(r=2^d\ge2\), the root and first children have the claimed orthogonal row directions. The local POD rank rule (identity Gram matrix, unit range, size-proportional positive NRMSE budget) forces retention of every nonzero singular direction at every relevant node. Substitution into the exact factor-storage formula gives a strictly loss-making first split. Below that split, every group-aligned nonleaf cut strictly lowers storage, and splitting a homogeneous group increases storage, proving that the fine cut is optimal in the prescribed tree. Its ratio to the greedy root diverges linearly. The algebra separately proves both outputs have exact zero reconstruction error and cost fewer entries than the raw matrix. Supplementary reproducibility: 3,550 integer/Fraction-based assertions using `verify.py`.

## Originality — PASS with disclosed access risk

The motivating arXiv manuscript [1] already states that its storage-decreasing greedy search is not globally optimal and that an unprofitable first split can hide valuable descendants. Neither that qualitative observation nor general nonoptimality of greedy selection is claimed to be new. The asserted advance is an explicit, infinitely parameterized, *unbounded* storage approximation ratio obeying all local NRMSE-rank conditions with positive tolerance, 1D connectivity, balanced partitions, and exact reconstruction. Compared to the related full-text clustering work [2], the objective, partition direction, ranks and selection rules are different. The abstract of the specialist hierarchical tensor article [3] did not settle this claim, but its complete text could not be obtained, so historical priority is not exhaustive.

## Mathematical value — PASS

The example establishes that a monotone-improvement stopping policy offers no dimension-independent guarantee even when its individual feasible reconstructions are exact and are already useful compressed representations. This strengthens the source's qualitative warning into a reproducible worst-case quantitative benchmark and motivates multilevel lookahead or dynamic programming on a fixed spatial hierarchy. It does not assume an arbitrarily weak numerical accuracy tolerance or artificial zero-rank approximations.

## Closest sources and limitations

[1] Nuca–Parsani–Dalcin, arXiv:2610.31375v1, particularly equations (25)–(26) and Section 4; [2] Shamrai, arXiv:2601.11626v2, clustering and algorithms; [3] Ehrlacher–Grigori–Lombardi–Song, DOI 10.1137/19M128689X, available abstract only. The result does not cover arbitrary partitioner trajectories, encode metadata costs, or certify exhaustive literature novelty.

Self-review: passed. Independent audit: not yet performed.
