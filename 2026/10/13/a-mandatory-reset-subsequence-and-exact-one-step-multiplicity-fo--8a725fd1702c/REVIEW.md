# Scientific review

## Correctness — PASS
The all-length proof follows each initial state through the rotation and collapsing input letters. Synchronization forces distinct modular counts of effective collapsing letters; one trajectory must cross the collapse edge at least \(n-1\) times, forcing the required scattered subsequence. The stated word resets, and the proof classifies every one-symbol insertion, including the sole forbidden interior \(b\) site per rotation block. Exact dynamic programming and an independent insertion simulation corroborate the formula at finite lengths. The proof covers all \(n\ge2\) without treating finite tests as infinite certification.

## Originality — PASS
The classical \((n-1)^2\) shortest reset length and standard Černý construction are not claimed as new. The checked 2013 open-access shortest-word-algorithm paper concerns finding lengths, the closely related published \(k\)-avoiding paper concerns worst-target avoidance thresholds, and the inspected 2022 complexity paper concerns different language intersection/subsequence problems. None of the inspected statements implies the mandatory scattered-subsequence property or the one-extra-letter enumeration. Older equivalent descriptions remain possible and require future bibliographic scrutiny.

## Value — PASS
The universal necessary scattered pattern describes the geometry of *all* resetting input words, not just a shortest witness. The exact first-excess multiplicity answers how much one-symbol input slack increases the design space: precisely \(n^2-4n+7\) choices, with a complete description of allowable insertions. This is a natural robustness and redundancy invariant of a canonical extremal automaton.

## Limitations
The subsequence criterion is necessary, not sufficient. No statement about words at larger excess lengths or different transition systems is made. The scientific proof has not been independently audited.

Self-review: passed. Independent audit: not yet performed.
