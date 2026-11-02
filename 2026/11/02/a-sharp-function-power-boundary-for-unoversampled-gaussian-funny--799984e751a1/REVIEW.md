# Scientific review

## Correctness — PASS

The stated Nyström matrix is the original subspace-iteration form. Positivity follows by the projector factorization and the Löwner--Heinz inequality. The sole nonzero eigenvalue and the exact error are direct linear-algebra identities. The normal-to-chi-square ratio has the displayed beta-prime density. Substitution yields the finite-parameter integral, with a dominating integrable function independent of \(L\), and a beta-integral proves the leading constant without approximation. The exponent controls all regimes. The probability-vs-expectation discrepancy follows from almost-sure fixed-sketch convergence with the exact expected limit. The executable checks matrix identities and explicit finite-parameter specializations, not an infinite theorem.

## Originality — PASS, qualified best-knowledge

The motivating work (Persson–Kressner, arXiv:2209.11023) defines funNyström and establishes general bounds conditional on at least two oversampling columns. The 2023 preprint of Persson–Meyer–Musco (arXiv:2311.14023) gives a general transfer principle; its subspace-iteration expectation result also assumes at least two oversampling columns. Neither inspected primary full text states the exact unoversampled single-spike power-function error asymptotics or the critical \(\beta=1/2\) expectation boundary. Existing randomized Nyström preconditioning analyses target different quantities. Exact ratio identities are standard and cannot alone support originality; the distinct contribution is the sharp algorithmic asymptotic and regime change. Semantic published-result searches found no dominating claim. An earlier uncatalogued special-case derivation remains a priority risk.

## Value — PASS

An operator-monotone matrix function can be approximated by funNyström without expensive function-vector products, but zero oversampling is not covered by common expected-error bounds. The exact exponent determines when one column of Gaussian subspace iteration is expectation-competitive, reveals a persistent rare-event bias at the square-root boundary, and shows why one additional power iteration eliminates it in the fixed-dimensional spike model. This is a natural, clearly quantified reliability threshold rather than an arbitrary finite-parameter computation.

## Limitations

Fixed finite dimension, diagonal one-spike spectra, powers \(0<\beta\le1\), Gaussian real sketches, integer power iteration, exact arithmetic, no oversampling. Extending to growing dimensions or general spectra is not claimed. Independent validation and definitive publication-priority checks are outstanding.

Self-review: passed. Independent audit: not yet performed.
