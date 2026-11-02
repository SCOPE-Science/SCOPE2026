# Review of the four-candidate, three-seat reciprocal-JR frontier

## Correctness

PASS. The reciprocal-JR definition reduces exactly to testing singleton ballots for the one unselected candidate. A top-three failure forces the fourth quality above the support-dependent floor. If the least valuable incumbent is safe to omit, an immediate normalized-loss bound applies; if that incumbent is unsafe, the exclusive-support counting inequality rules out three unsafe incumbents and gives a stronger harmonic bound for omitting the second-least-valuable incumbent. The boundary case where all four qualities equal one is treated separately. A fully specified family attains the claimed factor for every integer support parameter in the loss regime. The bundled exact checker passed 206077 finite profile checks and 520 sharp witnesses. Numerical tests are not taken as universal proof.

## Originality

PASS, subject to residual priority risk. The principal motivating paper, Boehmer et al. (arXiv:2609.08830), establishes the general 3/4 bound and an asymptotic two-seat obstruction; the present exact three-seat/four-candidate support-dependent frontier is not implied by those results. Earlier standard-JR welfare-price work by Elkind et al. (arXiv:2112.05994) concerns a distinct objective. An accessible earlier two-seat minimum-support result covers a different seat count and lacks the extra unsafe-incumbent case crucial here. Statement-level, parameter, alias and stronger-coverage queries did not surface equivalent coverage; unindexed or otherwise inaccessible proofs remain possible.

## Value

PASS. The four-candidate, three-seat case is the smallest candidate surplus where reciprocal representation can force a quality sacrifice at three seats. The result quantifies that sacrifice sharply as a function of candidate popularity and identifies the exact two-thirds population-support boundary beyond which proportionality costs nothing. A nontrivial second-obstruction argument is needed beyond the two-seat case, and the theorem provides a structural baseline for larger committees.

## Scope and limitations

Exactly four candidates, three committee seats, positive qualities bounded by one, reciprocal JR rather than more demanding axioms. All instances have a positive integer minimum supporter floor. Research literature inspection does not establish absolute novelty. Independent audit is not performed.

Self-review: passed. Independent audit: not yet performed.
