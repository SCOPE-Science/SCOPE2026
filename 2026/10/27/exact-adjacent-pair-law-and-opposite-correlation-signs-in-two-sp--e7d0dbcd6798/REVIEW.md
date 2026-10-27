# Scientific review

## Correctness — PASS

The one-sided nonblocking system follows directly from one-attempt earliest-deposition conditioning, and the unique hyperbolic solution has explicit initial data. Independence across the two exterior half-lines after fixing equal neighboring species yields the \(AA\) and \(BB\) pair probabilities; opposite accepted species cannot be adjacent. The published one-site marginals are independently reconstructed as \(p\int h_A^2\) and \(q\int h_B^2\), and the derivative identity \(R_A+R_B=a+b-ab\) closes the full nine-entry law. An exact factorization with \(0<a<pt\) and \(0<b<qt\) establishes all strict signs, including boundary cases. `CHECK.py` passed 147 diagnostic assertions, among them direct deposition simulations and full small-ring arrival-order enumeration. These are checks, not substitutes for the proof. No critical lemma rests solely on computation.

## Originality — PASS, with priority risk

The motivating arXiv:2306.09786v1 full text (Sections 1–6) calculates one-point densities, but not the displayed adjacent law or the opposing covariance signs. arXiv:2210.05627v1 computes pair correlations for single-species nearest-neighbor exclusion, which has a different allowed-configuration space. arXiv:2211.04622v1 uses repeated deposition attempts, and its one-dimensional results are mainly approximate density calculations. Semantic published-record queries for AB adsorption, adjacent pairs, and aliases returned no exact matching two-species one-shot law; the closest visible results concerned other types of occupancy and covariance. A relevant cavity-event decomposition is already present in the motivating paper, and a broad general RSA correlation identity or an overlooked subsequent work could imply the formulas; absence in searches is not a proof of novelty. Independent scholarly assessment remains necessary.

## Scientific value — PASS

Two-site probabilities are the first natural spatial statistics beyond the known one-site density in the same antagonistic deposition model. The exact \(AA,BB,XX\) laws quantify like-type clustering and empty-site spacing, which densities cannot determine. The universal sign contrast—positive equal-species correlation simultaneously with negative aggregate occupation correlation—identifies a concrete and potentially misleading inference from species-resolved versus unlabeled imaging. The result is parameter-wide and transient, not an arbitrary numerical slice or routine restatement of a known density.

## Limitations

Only neighboring sites of the infinite one-dimensional single-attempt process, \(0<p<1\), and \(0<t\le1\) are included in the strict sign theorem. Finite-ring numerical checks cannot prove infinite-volume results. The full-text literature inspected was the 2023 model source, 2022 single-species RSA correlation source, and 2022 repeated-attempt antagonistic source; uninspected general RSA correlation literature remains a scholarly priority risk.

Self-review: passed. Independent audit: not yet performed.
