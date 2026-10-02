# Independent mathematical audit — Positive stresses certify infinitesimal jamming of Q5 and R5

Audit date: 2026-10-01 (UTC) UTC
Disposition: passed

## Correctness
exact reconstruction gives 40 points and 240 contacts for each of Q5 and R5. The published orbit representatives generate all contacts with positive weights in {4,5,6}; exact equilibrium is 30 times each vertex. An independent finite-field rank computation gives rigidity rank 190 on 200 velocity coordinates, while the points span five dimensions, so the 10-dimensional kernel is exactly infinitesimal rotation. Positive stress then forces every feasible first-order contact derivative to vanish.

## Originality
the closest primary preprint by Eric Self (arXiv:2609.12640, 11 September 2026) explicitly states that jamming of Q5 and R5 is open. Resultary searches found the present record but no earlier equivalent certificate or stronger theorem resolving these two configurations. Classical spherical-code rigidity papers provide the criterion, not these certificates.

### equivalent_formulations
The claimed positive-stress/rank certificate is equivalent to proving all feasible infinitesimal motions are rotations; no prior equivalent certificate for Q5 or R5 was located.

Searches: Resultary: Q5 R5 kissing configurations infinitesimal jammed positive stress spherical code rigidity; arXiv:2609.12640

Evidence: Self's primary full text says the jamming question for Q5 and R5 is open; Cohn–Jiao–Kumar–Torquato supplies the general infinitesimal-jamming framework, not these certificates.

### broader_coverage
No broader theorem inspected implies jamming of Q5 and R5 without the record's new configuration-specific computation.

Searches: arXiv:1102.5060; arXiv:2609.12640

Evidence: General spherical-code rigidity theory covers the criterion but does not cover these two configurations; the 2026 Q5/R5 source explicitly leaves them open.

### exact_database_or_table
The result is a proof/certificate rather than a database extraction.

Searches: Resultary semantic search for Q5/R5 rigidity certificates

Evidence: No database/table containing these exact stress weights or rank-190 certificates was located.

### claim_vs_prior_implication
The final claim is not a corollary of the inspected prior statements.

Searches: Self arXiv:2609.12640 conclusion; Cohn et al. arXiv:1102.5060

Evidence: Prior theory plus previously known coordinates does not itself establish the positive stress and rank facts; Self records the question as open.

### Source inspections
- **Eric Self, Non-convex unit-edge polytopes on kissing configurations in dimensions 5–7** — Primary full text inspected; its conclusion states that Q5 and R5 remained open. Assessment: Compared against the final statement and implication scope.
- **Cohn, Jiao, Kumar, Torquato, Rigidity of spherical codes** — Primary paper/abstract inspected for the spherical-code jamming framework. Assessment: Compared against the final statement and implication scope.
- **Resultary search** — Searched for Q5/R5 positive-stress jamming and equivalent rigidity certificates; no prior covering result was found. Assessment: Compared against the final statement and implication scope.

## Scientific value
resolving the two configurations explicitly singled out as open in the immediately preceding primary literature is a motivated rigidity result. The exact positive stresses and rank certificates are reusable structural data rather than an arbitrary finite computation.

## Reproducibility
Independent exact reconstruction: Q5=(40 points,240 contacts,orbit sizes 60/120/30/30,rank 190); R5=(40 points,240 contacts,13 stress orbits summing to 240,rank 190); both point spans have rank 5.

## Limitations and residual risks
The theorem concerns the specified Q5 and R5 configurations. It does not determine the five-dimensional kissing number, classify all 40-point configurations, prove local uniqueness among all spherical codes, or classify all equilibrium stresses. Residual originality risk remains from concurrent work after the recent open-problem statement.
- Very recent concurrent work may be incompletely indexed.
- The rank check is modular at a large prime; because a nonzero 190 by 190 minor modulo that prime implies the corresponding integer/rational minor is nonzero, it is a valid lower-rank certificate, while the rotation kernel supplies the matching upper bound.
