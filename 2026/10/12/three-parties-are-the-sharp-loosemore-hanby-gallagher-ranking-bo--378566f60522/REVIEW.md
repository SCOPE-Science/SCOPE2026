# Self-review

## Correctness
**PASS.** The two-party identity follows from the zero-sum discrepancy vector \((x,-x)\). For three parties, sign and permutation reduction to \((a,b,-a-b)\) gives the exact formula \(G^2=(3L^2+h^2)/4\), from which the sharp band and reversal criterion follow. The integer-grid statement is a complete exact enumeration of every positive vote and seat composition through denominator \(11\); the packaged verifier returns `VERIFY_OK` and classifies all first-layer reversals by symmetry.

Risk: the denominator threshold is specific to the common positive grid and is not asserted for unequal vote and seat denominators.

## Originality
**PASS.** Gallagher's primary paper already states that the two indices coincide with two parties, explains their different sensitivity to concentrated discrepancies, and reports that disproportionality measures can alter empirical rankings. Later literature proves the general inequality \(G\le L\) and characterizes equality. Those results do not supply the exact three-party geometry, the necessary-and-sufficient existence threshold \(L_A/L_B>\sqrt3/2\), or the positive-grid denominator-\(11\) first layer. Targeted published-result and literature searches did not locate those statements.

Risk: because the proof reduces to elementary norm geometry in three dimensions, an unindexed exercise or software test may contain an equivalent construction. Search failure is not proof of bibliographic uniqueness.

## Value
**PASS.** Loosemore–Hanby and Gallagher are standard electoral-disproportionality summaries, and Gallagher explicitly motivates his index by its different treatment of concentrated versus diffuse vote-seat discrepancies. The sharp party-count boundary identifies the first political setting in which that design choice can change an election comparison. The closed-form three-party band explains the mechanism rather than merely exhibiting a numerical example, while the integer-grid layer supplies a reproducible finite benchmark.

Self-review: passed. Independent audit: not yet performed.
