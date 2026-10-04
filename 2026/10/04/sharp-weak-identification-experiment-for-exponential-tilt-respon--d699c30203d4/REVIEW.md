# Same-model review

## Correctness
PASS. The proof starts from the exact target-input density after the response tilt. The fixed source mode mass makes the normalized gate perturbation centered exactly, so the first KL term cancels. A uniform logistic expansion gives the second moment \(3\eta^2+O(\eta^3)\), from which the KL, Fisher, and target-mean constants follow. The triangular-array likelihood-ratio increments are uniformly \(O(\eta)\), so the finite critical experiment follows from Lindeberg. Pinsker and Hoeffding establish the zero- and infinite-information regimes. The packaged deterministic checker reproduces the constants numerically for the source normalization used in the motivating paper.

## Originality
PASS. Choi (2026) owns the source model and the qualitative statement that every \(\eta>0\) is identified while \(\eta=0\) is not, and explicitly states that no general regression estimation rate is derived. Garg et al. (2020) provide broader fixed-model label-shift rates controlled by likelihood curvature, and Lee--Ma--Zhao provide semiparametric large-sample label-shift theory. The inspected statements do not contain the explicit logistic-gate density perturbation, its \(3/2\) KL coefficient, the Fisher constant, or the critical \(m\eta^2\) Gaussian experiment. Statement-level indexed searches also returned no equivalent claim.

## Value
PASS. The motivating paper reports sharp practical deterioration as its mode-signal parameter decreases. The theorem gives the exact statistical reason: information per target input is quadratic in that signal, so maintaining a fixed ability to distinguish response shifts requires target sample size of order \(\eta^{-2}\). The critical total-variation limit further quantifies the entire transition instead of merely restating identifiability.

## Closest literature and limitations
The closest direct source is arXiv:2609.30886v1. The closest broader label-shift comparison inspected in full is arXiv:2003.07554; its curvature-dependent bound is related but not the same statement. arXiv:2307.04250 is a plausible broader semiparametric comparison; only its abstract and accessible records were inspected because the checked full-text route was unavailable. The claim is restricted to a known-source, correctly specified separable binary-mode subexperiment and does not establish a rate for the implemented ExTRA estimator or a conformal-coverage guarantee.

Same-model review: passed. Independent audit: not yet performed.
