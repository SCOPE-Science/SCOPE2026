# Review: parity-alternating initial rank compression in \(F_n\)

## Correctness
**PASS.** The proof uses only the stated transition maps. The collision letter \(a\) can reduce rank by at most one and is effective exactly when states \(2\) and \(n\) are both present. In a shortest target-rank word, \(a^2=a\) excludes adjacent \(a\)'s. Consecutive effective occurrences have separator lengths different from \(0\) and \(2\); a one-letter separator forces the next separator to have length at least \(3\). This yields the lower bounds by pairing separators. Explicit missing-state formulas for the two parity classes attain those bounds throughout \(1\le s\le(n+1)/2\). Exact power-automaton search for odd \(5\le n\le17\) and direct witness replay through odd \(n=301\) agree with the theorem.

## Originality
**PASS.** The defining source states the transition maps of \(F_n\) and proves only the reset threshold \(n^2-3n+3\). Its relevant subsection and theorem do not state prescribed-rank minima, and the inspected full text contains no occurrence of “rank.” Searches using the aliases “rank compression,” “deficiency,” “shortest word to rank,” the exact parity formulas, the source identifier, and the primitive-digraph \(V_n\) description found no statement implying the claimed profile. The closest indexed automata records concern different families or different invariants, so they do not dominate the claim. Residual risk remains that a differently named or unindexed note contains the same profile.

## Value
**PASS.** The family \(F_n\) is a classical slowly synchronizing series whose published endpoint behavior is quadratic. Prescribed-rank compression is a natural finer invariant of the same synchronization process. The theorem gives a complete initial half-profile rather than one isolated value, and its parity oscillation exposes a concrete local mechanism—alternating one-step and forced three-step opportunities for effective collisions—that is invisible from the reset threshold alone. The result therefore supplies a reusable structural description of how this slow family begins to compress.

## Closest literature and limitations
The closest primary source is Ananichev–Gusev–Volkov, arXiv:1302.5793, Section 4.4 and Theorem 7. An earlier paper by the same authors, arXiv:1005.0129, is a preliminary treatment of related slow families but does not define this \(F_n\) profile. The new theorem stops at \(s=(n+1)/2\); no statement is made for larger deficiencies.

Same-model review: passed. Independent audit: not yet performed.
