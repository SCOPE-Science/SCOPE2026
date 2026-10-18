# Scientific review

## Correctness

PASS. The exact cut process is reconstructed from uniform pairings; the transition probability of closing an exposed chord is \(h/(M-k)\). For two nested prefix cuts, the stated covariance follows from probabilities of one specified pair and two disjoint specified pairs. The positive innovation variances give the precision quadratic form and determinant. The limiting predictable quadratic variation is \(2t^2/(1-t)^2\); bounded jumps and endpoint reversal supply the full functional convergence. The limit's covariance and aggregate-span variance are obtained by Brownian time-change and integration. A standalone, exhaustive exact-arithmetic verifier passed 450 assertions up to twelve sites. This finite computation does not prove the infinite-sample limit.

## Originality

PASS with residual priority risk. Acan (arXiv:1501.01489v1, Sections 2 and 6) analyzes random-chord *degree* and separately whole-chord growth; it does not explicitly evaluate the joint prefix-cut covariance, its inverse and determinant, or the Gaussian limit. Berkooz, Narayan, and Simón (JHEP 2018, Section 3.1) develop open-chord transfer recursions for a different weighted problem. The history mechanism itself is not new, and this comparison assesses specifically the evaluated unweighted second-order kernel and functional limit. Search comparisons of alternative names (open chords, active arcs, pairing boundary process, height process, prefix cut) identified no direct encompassing claim in the consulted results. General recurrence machinery may implicitly encode the finite covariance, and a separate literature search could still uncover an earlier Gaussian profile theorem.

## Mathematical value

PASS. The open-chord height profile is an intrinsic observable of matching diagrams; its complete covariance controls every weighted linear scan statistic. The exactly sparse precision matrix gives a finite-size second-order local structure despite long-range covariance, and the limit identifies a non-Brownian pinned Gaussian Markov process with a simple explicit time-change. This adds whole-process fluctuation information not supplied by the published fixed-chord degree distribution. The aggregate-span normal law illustrates a natural global statistic, rather than an arbitrary parameter specialization.

## Closest sources and scientific limitations

Acan (2015), Sections 2 and 6, supplies the most closely related direct probabilistic analysis; Berkooz–Narayan–Simón (2018), Section 3.1, supplies a general transfer formulation for open-chord histories. The proofs and formulas here concern uniform unweighted matchings and do not extend automatically to crossing-weighted ensembles, nonuniform pairings, or stronger tail probabilities. The structural transition mechanism is classical; historical priority attaches only to the evaluated profile statements and their proof, and remains open to independent audit.

Self-review: passed. Independent audit: not yet performed.
