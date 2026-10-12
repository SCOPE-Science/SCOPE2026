# Scientific review: random-stage implicit RK2 stability

## Correctness — PASS

For the exact published implicit and semi-implicit update forms, both scalar updates reduce to the same rational amplification factor. The proof identifies mean-square stability with a strict inequality on the second moment of that factor under independent sampling. The global centered-stage obstruction follows from an exact nonnegative factorization and dominated convergence/Fatou at the stiff limit; a two-atom construction establishes sharpness of the constant. For the two-point family, an exact polynomial factorization proves strict stability throughout the open left half-plane at the limiting probability, and the stiff-limit argument proves failure immediately beyond it. The reproducibility program checks both defining polynomial identities by exact coefficients and 309 exact-rational instances. The universal theorem rests on the proof, not on those instances.

## Originality — PASS, residual priority risk

The closest directly motivating source, Bochacik–Przybyłowicz, arXiv:2404.19059v1, Section 3, fixes stages uniform on \([0,1]\) and establishes the corresponding mean-square instability. Its 2025 revision retains that stage law. It does not prove a general sharp variance penalty over all laws with mean \(1/2\), nor the complete two-point probability criterion allowing some stages below \(1/2\). Earlier randomized explicit RK2 literature uses a different polynomial multiplier. Eisenmann–Jans–Kruse–Podhajsky, arXiv:2607.18928, Section 5, establishes per-realization stability for another two-stage implicit tableau with the random parameter at least \(1/2\), which does not imply the mixed-stage threshold here. Searches across indexed mathematical findings and the inspected primary literature did not reveal the combined result. Absence of an indexed equivalent is not proof of global priority; specialized random-coefficient theta literature may contain an unlocated counterpart.

## Value — PASS

This theorem resolves a motivated stability-design question left by the uniform-random-stage result: is loss of mean-square A-stability a feature of randomization itself, or of stage-center preservation? The sharp \(12\)-variance penalty answers the first side for every centered stage law, and the exact \(p_*(a)\) frontier exhibits stabilizing randomization with occasional individually expansive stages. Both are structural statements useful for reasoning about accuracy/stability tradeoffs of the original solver, not a one-off computation. The boundary result is complete for the stated two-point family.

## Scope and outstanding limitations

Conclusions concern scalar-test mean-square A-stability only; no B-stability, nonlinear or high-dimensional result is claimed. Biased stage laws generally lose quadratic-order matching of the expected local amplification, so they are not advertised as drop-in higher-order methods. The publication-priority comparison is strongest for available full texts and remains subject to unindexed methods literature. The mathematical identities have been rechecked but have not undergone independent external audit.

Self-review: passed. Independent audit: not yet performed.
