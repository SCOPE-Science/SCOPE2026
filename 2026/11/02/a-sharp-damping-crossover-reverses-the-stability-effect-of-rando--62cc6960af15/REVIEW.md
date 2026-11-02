# Review: randomized order versus frozen order for planar Lie–Trotter splitting

## Correctness

PASS. The exponential of each shear generator is a scalar damping times a first-degree nilpotent shear. Directly multiplied step matrices have average Gram matrix \(e^{-4ah}(1+s^4/2)I\), so independent fair order choices yield the exact squared-energy law by conditional expectation, without distributional assumptions on current state direction. Both fixed matrices have determinant \(e^{-4ah}\) and identical normalized trace \(2-s^2\), giving the spectral threshold. The comparison reduces to a cubic polynomial whose second derivative is positive above the critical elliptic–hyperbolic boundary. The cubic has exactly one root above that boundary; explicit exact parameters witness both stability reversals. The packaged finite-arithmetic verifier passed 193 checks. No finite check is used to infer an infinite statement.

## Originality

PASS, subject to publication-priority risk. The primary random splitting source evolves individual vector fields for independent random durations rather than randomly reversing a complete two-factor step. The relevant two-shear random matrix literature studies independent individual shears and generalized Lyapunov-exponent bounds rather than a fair sequence of reversed complete pairs with an exact mean-square identity. Randomized quantum product formulas compose unitary factors, whose norms cannot realize the present instability. The newer order-selection analysis of higher-order split solvers treats fixed-order linear stability, and even remarks that reversing one Lie–Trotter pair leaves its spectrum unchanged; it does not derive an interleaved random-order second-moment stability frontier. A published-record similarity search for aliases, swapped factors, mean-square exponents, cubic crossover and isospectral stability reversal returned adjacent but not implication-equivalent results. The closest accessible sources were materially inspected; one plausible randomized operator-splitting paper could only be checked at the abstract level, leaving residual priority uncertainty.

## Value

PASS. A basic numerical-design question is whether randomizing an operator order is harmless, protective or dangerous for long-time stability. The answer is sharply nonmonotone, even though the exact continuous system is exponentially stable and the two deterministic orders have identical spectra. The theorem supplies a unique dimensionless transition and exact witness problems on both sides, distinguishing spectral stability, mean-square stability and continuous-time decay. It is a natural counterexample to importing frozen-order stability conclusions into iid operator-order selection.

## Closest literature and limitations

- Agazzi, Mattingly and Melikechi (2022), random subflow durations and ergodicity, https://arxiv.org/abs/2201.06643.
- Sturman and Thiffeault (2019), individual random shears and generalized exponents, https://link.springer.com/article/10.1007/s00332-018-9497-3.
- Eisenmann and Stillfjord (2022), randomized operator-subset splitting, https://arxiv.org/abs/2210.05375; full manuscript was not accessible in the material inspected.
- Wei, Guenter and Spiteri (2025), fixed-order stability and design, https://arxiv.org/abs/2501.02310.

The proof covers only exact two-stage subflows of a specified damped planar linear system with iid fair order choices and their mean-square norm. It does not determine almost-sure Lyapunov stability or arbitrary matrix splitting.

Self-review: passed. Independent audit: not yet performed.
