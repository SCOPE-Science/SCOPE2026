# Review

## Correctness

PASS. Marking one \(r\)-cycle gives a bijection between a weighted permutation with a distinguished \(r\)-cycle and an Ewens permutation on the remaining \(n-r\) labels, with one additional cycle. This proves the Palm identity exactly. The covariance formula follows by taking the identity function and using the standard Ewens mean cycle count.

The sign bracket is strictly decreasing because increasing \(r\) adds one positive term to the harmonic tail. Its macroscopic limit is \(1+\theta\log(1-x)\), whose unique zero is \(1-e^{-1/\theta}\). The covariance profile combines this limit with the exact gamma-function mean of \(A_{n,r}\).

## Originality

PASS, with an explicit residual risk from older size-biased Ewens literature. Bakšajeva--Manstavičius was inspected in full public form at the cycle-structure formula, conditioned-Poisson representation, additive-function framework, and restricted-cycle results. The inspected text does not state covariance between total cycles and one cycle-size count or the sign threshold.

Lugo's full public text was inspected at its exact joint factorial-moment formulas and normalized long-cycle limits. It treats the same macroscopic size regime but not the total-cycle cross-covariance.

Hoppe's size-biased Poisson--Dirichlet paper is highly relevant by title and abstract, but only abstract-level material was accessible. It is therefore named as a residual risk rather than declared non-covering.

## Value

PASS. Total richness and the frequency spectrum are canonical summaries of Ewens samples in both random-permutation and population-genetic interpretations. The result gives a finite structural law and a qualitative phase transition: rare and moderate frequency classes move with richness, while sufficiently macroscopic classes move against it. The threshold fraction is explicit and parameter-dependent.

Same-model review: passed. Independent audit: not yet performed.


Exact replay: `VERIFY_OK permutation_parameter_evals=17736 mean_checks=81 palm_checks=660 covariance_checks=81 threshold_checks=18 asymptotic_checks=20`.
