# Independent mathematical audit

## correctness

PASS

A selected vertex is essential exactly when its closed neighborhood contains a real vertex whose own closed neighborhood meets the selection in just that vertex. Five masks suffice for this test and domination at the center; the last two real columns are validated by padding twice, with absent and unselected columns treated distinctly. At a fixed four-mask suffix a suboptimal prefix cannot catch up. An independently written closed-neighborhood bitset recurrence reproduced at height three the equal supports of size 1285 at lengths 16, 20 and 24, weight increments 6 on every state, and zero count second differences. It reproduced terminal pairs (24,4), (27,4), (30,4), (33,4) at lengths 16,18,20,22 and the stated even base counts; it also matched the frozen height-two certificate. A coordinate-wide additive weight shift preserves all maximizing transitions, so four steps act on counts by the same integer linear map throughout the orbit. The verified second difference yields affine count evolution; two identical terminal counts in each even residue class set its slope to zero. This proves every even length, not just the test orders. Both checkerboards and both full-column patterns have the requisite size, domination and private witnesses, and are distinct also at n=2, so the count proves exhaustiveness.

## originality

PASS

Only the exhaustive even-length three-row pattern classification and the corresponding count are claimed in the repair. The two-row duplicate, known scalar formula, odd-length uniqueness, and earlier ladder automaton framework are credited and are not independent novelty claims.

## value

PASS

The next open strip after the ladder is a natural setting to test whether the known extremal size hides further patterns. The even three-row result shows that rows drop out but the checkerboards and two full-column types exhaust all maxima, including nonindependent ones. This supplies a useful top coefficient and structural list not implied by the size theorem, with an exact all-order certificate rather than a small grid census or a restatement of the ladder result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
