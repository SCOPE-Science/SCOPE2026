# Scientific review

## Correctness (PASS)

The claim follows from four explicit and independent analytical steps: the closed one-particle equation for SEP occupations, the exact complement-symmetric three-bit Walsh expansion, the nonzero-spectrum variance identity that characterizes uniform hubs, and Fourier/Bessel heat-kernel limits. The canonical and grand-canonical normalizations are separately derived; strict inequalities hold at every positive sampling lag on the specified graphs. Finite-state and scaling assertions in `verify_sparse_cmi.py` independently check examples, but no finite computation substitutes for the proof of the infinite families.

## Originality (PASS, best-knowledge and qualified)

The closest primary work, Iadecola (2026), treats **full intermediate local measurement records**, their charge-conditioned memory and a discrete-time SEP. The exact three-sample joint law, a graph-theoretic iff criterion for zero memory, and the two exact theta profiles are not stated there. The October 26 paper of Wang, Liang and Yang studies the distinct full-intermediate-record protocol and its different Gaussian asymptotic. Standard SEP duality and finite-graph spectral theory are acknowledged; direct derivability of the component formulas does not amount to an identified published theorem encompassing the new classification. Close residual risk: a general binary-trace Markov/lumpability result or multitime duality theorem may subsume parts of the result. Publication priority has not been independently established.

## Value (PASS)

The amount of memory seen by an observer depends fundamentally on *which intermediate samples are included*, and on whether global particle number is known. An exact graph criterion identifies the exceptional geometries with no local memory; a sharp finite-size theta crossover quantifies the difference between the fixed-charge and charge-uncertain ensembles; and the infinite-chain \(t^{-1}\) coefficient enables quantitative sparse-sampling comparisons. These are natural observable and control-geometry distinctions for lattice transport, not arbitrary parameter slices.

## Closest literature and limitations

T. Iadecola, arXiv:2607.06689v1 (July 7, 2026), https://arxiv.org/html/2607.06689v1. S. Wang, C. Liang, Z.-C. Yang, arXiv:2610.36058v1 (October 26, 2026), https://arxiv.org/html/2610.36058v1; the latter is compared for originality only. Scope is symmetric, stationary, half-filled SEP, one observed site and exactly three observations. No quantum, asymmetric, nonstationary, or full-record claim is made. Independent audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
