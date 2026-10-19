# Self-review

**Correctness — PASS.** The finite theorem is established by an exhaustive root--partition enumeration with a complete-word scan, not by extrapolating measurements. For \(n\le10\), the included executable enumerates all \(2^n\binom{2n}{n}\) root--partition pairs, deduplicates roots by bitsets, and checks all binary length-\(2n\) output words. Independent direct-partition enumeration agrees through \(n=6\), the nonempty-word totals agree with \(\binom{2n}{n}\), and \(170\) distinct root witnesses certify the length-\(20\) lower bound.

**Originality — PASS (provisional).** He--Huang--Nam--Thaper establish reverse-shuffle membership and large-alphabet output counts; Grytczuk--Pawlik--Pleszczyński discuss generalized shuffle squares; Datko--Pawlik tabulate *ordinary* shuffle roots, whose length-\(20\) maximum is \(19\), not the reverse-shuffle maximum \(170\). Relevant semantic database searches did not return this precise profile. A pre-existing unindexed reverse-root census cannot be excluded; this is a self-review, not a priority certification.

**Mathematical value — PASS.** The result determines a natural sharp inverse-counting invariant for all binary source words of length at most \(20\), including all eight length-\(20\) extremizers, complementing existing work on ordinary shuffle-root multiplicities. The separation between \(170\) reverse roots and \(19\) ordinary roots for the same length is mathematically informative. No infinite recurrence or general asymptotic assertion is made.

**Limits:** The sharp claim is confined to \(1\le n\le10\); the complete C++ upper-bound search at \(n=7,8,9,10\) was not independently reimplemented at those sizes. Relevant primary works were inspected as specified in `AUDIT.json`. Remaining originality risk: an unindexed equivalent enumeration. No independent external mathematical audit has occurred.

Self-review: passed. Independent audit: not yet performed.
