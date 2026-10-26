# Scientific review

## Correctness — PASS

The theorem is checked at the level of all binary patterns, not only an optimized subclass. Swapping an adjacent \((1,0)\) inversion reduces work below the critical overhead. An independent telescoping identity gives strictly positive work excess for every nonzero active decision at and above the critical overhead. The suffix cost differences have the exact sign of \(\theta_{k+1}-h\), where thresholds are strictly increasing. The two dimension regimes follow from convergent versus divergent partial sums. Boundary equalities and finite-depth ties are explicitly handled. Exact rational enumeration of 1,790 configurations for depths through eight reproduces these analytic deductions; it does not establish an infinite theorem by itself.

## Originality — PASS, subject to identified prior-art risks

The most relevant primary preprint (Hyman, arXiv:2610.15143v1) establishes the cost of an arbitrary *specified* multilevel schedule and the cell-count geometry. It does not determine the globally cheapest binary partial schedule for this assumed per-fine-update interface overhead. Its final section specifically identifies overhead-sensitive scheduling optimization as a question. The 2013 Nyx article describes existing automated schedule enumeration but no sharp geometric one-switch theorem. Targeted published-record and accessible-claim searches did not reveal a covering result. A separate Nyx optimal-subcycling manuscript cited as in preparation, and equivalent engineering-cost formulations, remain originality risks. Failure to find a match is not certification of novelty.

## Value — PASS

The exact one-switch property compresses \(2^L\) possible temporal patterns to a threshold-selected coarse locked prefix. The finite-depth switching points, exact tie cases, and qualitative distinction between \(\rho=1\) and \(\rho>1\) are concrete structural facts motivated by the contemporary AMR work model. The result does not promise numerical speedups in implementations without the assumed overhead function.

## Limitations

The cell counts are precisely geometric, the finest-level physical timestep is fixed, temporal ratios are binary choices \(1\) or \(r\), and overhead is additive proportional to the active fine-side cell work. Irregular geometries, nonlocal synchronization and measured wall-clock performance are not included. No independent evaluation has been performed.

Self-review: passed. Independent audit: not yet performed.
