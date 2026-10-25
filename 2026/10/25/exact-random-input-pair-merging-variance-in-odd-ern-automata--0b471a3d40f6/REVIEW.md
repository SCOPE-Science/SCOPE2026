# Scientific review of the odd-state random-input Černý pair variance

## Correctness — PASS
The claimed observable is a first merger time for one designated pair under independent fair letters. The unordered-pair automaton has precisely \(n(n-1)/2\) transient states in the odd case. Its transitions are stated explicitly, and the first-step moment equations are uniquely solvable because a fixed finite word merges any designated pair. The displayed mean solution satisfies all ordinary and boundary transitions. Summation of the second-moment differences leads to a scalar discrete Poisson equation with an upper reflecting boundary; solving it gives the variance polynomial. The independent rational-arithmetic checker solves the original pair-chain linear equations for odd \(n\le11\), and a finite degree-bound algebra certificate checks the final polynomial identity. These finite computations do not replace the general proof.

## Originality — PASS, with priority uncertainty
Gusev (2014, arXiv:1404.6731) supplies the pair-automaton method and the cubic expected time. Inspection of its relevant full-text derivation finds an expectation calculation, not the second moment or limiting coefficient of variation. General deterministic reset-threshold and random-transition-function studies concern different observables. Related publicly indexed work on exact Černý deficiency thresholds concerns shortest deterministic words, not fair-input hitting-time variance. Searches for alternative variance, hitting-time, and random-input terminology identified no covering statement. The result is not proven historically unique; overlooked earlier second-moment analysis remains a risk.

## Value — PASS
The variance has the same order as the square of the known cubic mean, with the explicit nonzero relative dispersion limit \(\sqrt{2/3}\). This distinguishes typical reliability under stochastic input from the previously calculated expectation and supplies an exact infinite-family stochastic statistic in a canonical extremal automaton.

## Limits and closest work
The closest source is Gusev's 2014 expected-time theorem; the new conclusion is strictly stronger in a different moment, not a restatement of the expectation. Only odd state counts, the opposite pair, and fair independent inputs are proved. The even case, arbitrary pairs, and full merging-time law are not covered. A prior equivalent variance calculation cannot be ruled out purely by failed searches. All checks are internal to the present analysis.

Self-review: passed. Independent audit: not yet performed.
