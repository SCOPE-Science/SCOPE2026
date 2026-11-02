# Scientific review: fixed-content multiletter rotation spectra

## Correctness — PASS

The claim follows from four explicit steps: the concatenation identity for scattered ordered-pair counts; the proportional-Parikh criterion for equal profiles of two rotations; the gcd lower bound and its periodic equality case; and the sharp multiletter grouped-word upper endpoint together with an adjacent-exchange intermediate-value argument. The moving-prefix coordinates \(\mathbf H_i=N\mathbf P_i-i\mathbf c\) preserve exactly the same equality relation as the full \(2\)-binomial signatures. Under a linear adjacent exchange, exactly one of the \(N\) moving-prefix coordinates changes. The grouped-word argument crucially uses at least three occurring letters, because a proper circular interval cannot partially meet three monochromatic runs. Boundary cases with content gcd one, with exactly three letters, or with repeated rotations are explicitly accounted for. `checker.py` independently agrees with direct subsequence signatures over 18,666 fixed-content labeled words across eight compositions; this is corroboration, not a proof for all lengths.

## Originality — PASS, with residual historical-priority risk

Rigo–Salimov's 2013/2015 work introduces \(m\)-binomial equivalence and studies factor complexity of infinite words; its 2015 proof of rational symbol frequencies uses cyclic shifts but does not present an all-content spectrum of equivalence classes within one conjugacy orbit. Rao–Rigo–Salimov (2013) studies avoidance of binomial powers rather than cyclic-orbit spectra. Poovanandran–Simpson–Teh (2021) counts *averaged* subsequence occurrences over conjugates of a circular word and studies ambiguity between circular words, not the count of distinct pair-subsequence signatures of individual conjugates. The binary two-letter case behaves differently (for content \((2,2)\), its four rotations yield at most three profiles), which neither implies the grouped-word upper endpoint \(N\) for three or more letters nor classifies the new alphabet regime. Statement-level comparisons, checks for alternate terminology and exact tables, and available mathematical-result searches did not reveal stronger covering results. An undiscovered general multinomial-conjugacy theorem remains possible; absence from searches is not novelty certification.

## Value — PASS

The theorem gives a natural and exact all-parameters answer, not a modest numerical increment: for every positive multiletter composition it characterizes the entire attainable class-count spectrum, both sharp endpoints, and collisions via balanced circular segments. The abrupt change from the binary upper endpoint to the full \(N\)-rotation endpoint as soon as three letters occur is structurally explained by the geometry of runs on a circle. The result supplies constructive fixed-composition witnesses for every intermediate complexity and a direct criterion for maximal distinguishability of rotation signatures. No downstream conjecture is required for this complete classification to be useful.

## Closest literature and limits

The most relevant sources are Rigo and Salimov's available WORDS 2013 preprint and 2015 extended article, Rao–Rigo–Salimov (2013), and Poovanandran–Simpson–Teh (2021). The definition of binomial equivalence, general concatenation identities, and the elementary idea of tracking statistics under cyclic shifts are not new. The accepted claim is specifically the full-spectrum multiletter theorem. The work does not address higher-order binomial equivalence, words with fewer than three occurring letters, or counts of maximizers. It has not been independently audited.

Self-review: passed. Independent audit: not yet performed.
