# Review

## Correctness

PASS. For propositional \(\varphi\), its truth set is unchanged because the contraction update changes only accessibility. Hence each successor row \(S\) follows the exact set map \(c_P(S)\). Idempotence is immediate after separating the cases \(S\subseteq P\) and \(S\not\subseteq P\).

For two contents, if the truth sets are equal, idempotence gives commutation; if they cover the carrier, the four possible subset relations of \(S\) to the two truth sets give the same final row in both orders. Conversely, if the truth sets are unequal and fail to cover the carrier, the empty row yields the two distinct complements in opposite orders. The propositional tautology criterion follows by assembling the required truth assignments into a two-world countermodel. The checker exhaustively confirms the row theorem through six worlds.

## Originality

PASS. The primary paper defines the update and develops preservation, success, AGM-style principles, reduction axioms, and a generalized event-model semantics. It does not state propositional idempotence or characterize when two hedged contractions commute. Full-text searches for idempotence and commutation terminology found no matching theorem.

Candidate-specific indexed searches for repeated contraction, idempotence, commuting hedged announcements, and propositional order effects found no equivalent published finding. A separate 2026 KR paper on dynamic belief contraction is a plausible related source, but only metadata and program information were accessible; it is retained as a residual risk rather than treated as non-covering.

## Value

PASS. Repetition and order are basic structural questions for any dynamic belief-change operation. Here the answers are unexpectedly sharp for factual contents: one contraction is already saturated, and two contractions are universally order-independent under exactly two simple classical conditions. The failure case needs only two worlds, so the theorem provides both a usable simplification law and a minimal obstruction pattern for reasoning about sequences of hedged announcements.

## Closest literature and limitations

Belardinelli--Zhang (2026) is the direct source of the operator. Their Proposition 6.3 specifically exploits propositional invariance, making the propositional restriction mathematically and semantically natural. Their conclusion discusses iterative questions for the broader generalized system but does not give the special-case algebra proved here.

Baltag--Fiutek--Smets (2026) studies dynamic belief contraction independently. Its full text was not available for statement-level comparison, so analogous iteration results under that different semantics remain possible.

The theorem does not extend automatically to modal contraction contents, because adding arrows can change their truth sets.

Same-model review: passed. Independent audit: not yet performed.
