# Same-model scientific review

## Correctness
PASS. The core step is a bijection: under exchangeability and no ties, all calibration/future interleavings in the total score order are equally likely, and each interleaving determines exactly one weak composition of future scores among the calibration gaps. Aggregation by consecutive gaps gives the stated Dirichlet-multinomial law by stars-and-bars. The simultaneous-band recurrence counts the same compositions by prefix totals, with prefix sums reducing the cost to \(O(nm)\). Exact finite enumeration in `verify.py` independently checks representative instances of each step.

## Originality
PASS with a stated literature risk. The closest direct source, arXiv:2303.02770, proves the exact beta-binomial law for one empirical-coverage level. arXiv:2210.14735 develops tolerance-region and beta conditional-coverage guarantees, and arXiv:1910.10562 develops the nested-set formulation. Searches across conformal, Dirichlet-multinomial, order-statistic, uniform-composition, and simultaneous-band phrasings did not locate the full finite joint law or the exact coverage-band evaluator. The classical probability/combinatorial ingredients are not claimed as new.

## Value
PASS. Multiple nominal levels from the same calibration set are intrinsically dependent. Their exact coupling is needed for simultaneous calibration diagnostics, familywise coverage statements across levels, and exact coverage-curve bands. The full rank-grid theorem and \(O(nm)\) evaluator provide a reusable finite-sample tool rather than a one-off numerical fact.

## Closest literature and limitations
The direct predecessor is Marques, arXiv:2303.02770, whose one-level beta-binomial theorem appears as a marginal of the present vector law. Hulsman, arXiv:2210.14735, and Gupta--Kuchibhotla--Ramdas, arXiv:1910.10562, supply closely related tolerance-region and nested-set viewpoints. A residual risk remains that older multivariate tolerance-region or order-statistics literature contains an equivalent spacing formulation under different language. The theorem itself requires exchangeable, almost-surely tie-free scores.

Same-model review: passed. Independent audit: not yet performed.
