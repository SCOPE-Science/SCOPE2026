# Same-model review

## Correctness
PASS. Let \(r_i\) be reduced wins and \(q_i\) wins over the deleted player. Strict reduced reversal forces \(r_{i+1}-r_i\ge1\), while strict full reversal forces \(w_i-w_{i+1}\ge1\). Since \(w_i=r_i+q_i\), the adjacent inequalities force \(q_i-q_{i+1}\ge2\). This gives both the total-match lower bound and the deleted player's match-load lower bound. The displayed construction realizes equality. The \(n=3\) maximum-load exception is handled separately and sharply. The verifier replays all formulas on \(3\le n\le100\).

## Originality
PASS. The closest source proves existence of Borda inversion and explicitly raises the “few matches” issue, but its sparse construction is then developed for Massey and Colley; its Borda remark says that the particular sparse family fails to yield an inversion. Exact-source, alias, extremal-count, and published-finding corpus searches did not locate the two sharp Borda match-sparsity formulas. Fishburn's positional-voting inversion theorem and Kondratev–Ianovski–Nesterov's deletion-independence analysis use different input objects and do not imply these finite-tournament match extrema.

## Value
PASS. The motivating paper identifies excessive match counts as a realism limitation and asks for sparse inversions. The result supplies exact sharp complexity thresholds for Borda in two natural measures: total matches and the maximum number played by one participant. At \(n=5\), it reduces the displayed Borda example from \(110\) total matches to the sharp \(18\), and reduces the general example's \(44\)-match per-player load to the sharp maximum \(12\).

## Closest literature and limitations
The closest full-text source is Chèze–Fieux, arXiv:2503.02429, especially the Borda section, Example 20, Section 3, and the Borda remark in Section 3.3. Fishburn (1981) is the closest older reversal result but is formulated for voting profiles and positional scores. Kondratev–Ianovski–Nesterov study removal consistency for scoring rules on ranked-event data. Search failure is not a proof of novelty; a residual risk is that an equivalent extremal statement may exist under different terminology in sports-ranking or social-choice literature. The mathematical claim itself is limited to the explicitly stated tournament model.

Same-model review: passed. Independent audit: not yet performed.
