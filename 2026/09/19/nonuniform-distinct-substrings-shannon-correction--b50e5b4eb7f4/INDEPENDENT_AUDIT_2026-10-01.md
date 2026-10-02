# Independent scientific audit — SCOPE-20260919-b50e5b4eb7f4

Audited at: 2026-10-01T14:19:47.879090Z

Disposition: **passed**

## Correctness — PASS

The renewal sandwich is valid, bounded surprisal overshoot gives the inverse-entropy renewal count, and the periodicity-class estimate makes overlapping-repeat corrections summable. The threshold split with bounded-increment Hoeffding estimates gives both one-sided L1 bounds. The Monte Carlo artifact is supplementary only.

## Originality — PASS

The classical all-length paper explicitly strengthens its general result only for unbiased memoryless sources, while fixed-length nonuniform papers address a different statistic. An earlier SCOPE concentration result gives stronger centered concentration once the mean is known, but does not supply the nonuniform inverse-Shannon-entropy expectation correction.

### Equivalent formulations

No equivalent theorem was located.

### Broader coverage

Broader concentration does not imply the mean asymptotic.

### Exact database or table

This is an asymptotic theorem, not table recomputation.

### Claim versus prior implication

The central expectation theorem is not mechanically implied.

## Value — PASS

The inverse-Shannon-entropy first correction for arbitrary fixed nonuniform iid sources is a natural exact extension of a classical all-length complexity problem and requires a genuine renewal-overlap argument.

## Sources inspected

- On average sequence complexity — https://www.cs.ucr.edu/~stelo/papers/tcs04.pdf. NOT_COVERING: The sharp first correction is stated for unbiased memoryless sources.
- Asymptotic Analysis of the kth Subword Complexity — https://doi.org/10.3390/e22020207. NOT_COVERING: Studies fixed-k rather than total all-length complexity.
- Exact approximation of average subword complexity of finite random words over finite alphabet — https://doi.org/10.5220/0002273000050009. NOT_COVERING_IN_MATERIAL_READ: Accessible formulation uses a uniform random-word model.

## Residual risks

- The full 2008 Ivanko article and Dębowski chapter were not inspected line by line.
- The separate L1 concentration consequence is less novel because prior SCOPE variance control is stronger once the mean asymptotic is known.

## Limitations

- Fixed finite iid sources only.
- No dependent-source, growing-alphabet, variance-asymptotic or limiting-fluctuation theorem is proved.
- Older Ivanko/Dębowski full-text overlap remains a residual risk.
