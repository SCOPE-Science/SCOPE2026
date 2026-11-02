# Review of one-letter slack rigidity in the Černý reset language

## Correctness — PASS
The exact claim is for every integer \(n\ge2\), the labeled classical Černý automaton, and distinct input words. Reverse preimages preserve inclusion. Ignoring nonexpanding inverse \(b\)-steps yields a cyclic interval whose strict growth occurs only with the boundary at \(n-1\to0\). Each of \(n-1\) growth steps costs a \(b\), and at least \(n-1\) inverse \(a\)-rotations are forced between growths. Equality identifies the unique minimum reset word. At one extra letter, an additional \(a\) can only occur after inverse growth is complete, whereas an additional \(b\) must be an identity insertion. The full analysis of these positions excludes the sole shrink position in each internal gap and gives \((n-2)^2+1\) first-final-letter resets. The two words extending the unique optimal reset word account for the difference between first resets and arbitrary resets. A separate bit-mask DP verified all cases \(2\le n\le11\) and the distinct explicit words, returning `VERIFY_OK`. These finite checks are corroboration only; the universal assertion follows from the proof.

## Originality — PASS, with limits
The closest literature is the classical minimal reset threshold, Kisielewicz–Kowalski–Szykuła's 2013 online article on algorithms for shortest reset words, and Stoner's 2014 cyclic-merger analysis. The examined full texts establish length or algorithmic properties, but not the exact second-length first-reset multiplicity and complete list. Published records for Černý intermediate-rank deficiency and \(k\)-avoiding thresholds were read in full: extremal rank/avoidance lengths do not imply enumeration of words first resetting the whole state set with one unit of slack. Related prior work on pair synchronization concerns two starting states, not simultaneous full-set synchronization. Search results and inaccessible primary literature leave a historical-priority risk, and no independent assessment has been performed.

## Value — PASS
The result answers a natural rigidity question immediately above a sharp extremal synchronization threshold. The new parameter counts exact language coefficients, not just the known minimum length. Its complete classification identifies each allowed one-letter edit and excludes otherwise plausible insertions by a congruence boundary, giving a structural fact about near-optimal reset words for a canonical family. It does not resolve general reset-length conjectures.

## Scope and limitations
The proof concerns the specified automaton over \(\{a,b\}\), its first-reset language at exactly \((n-1)^2+1\) symbols, and the corresponding total reset count. It does not classify larger slack, synchronizing-word deletion minimality, or other automata. Potential historical equivalents in material not inspected remain unresolved. No independent scientific audit has been completed.

Self-review: passed. Independent audit: not yet performed.
