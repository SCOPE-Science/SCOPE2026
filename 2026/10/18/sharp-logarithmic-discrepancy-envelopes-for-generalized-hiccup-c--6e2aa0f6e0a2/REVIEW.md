# Scientific review

## Correctness
**PASS.** The exact symbol word in Cloitre, Proposition 4.3, identifies missing indices with zeros. With zero-weight \(+1\) and one-weight \(-(k-1)\), induction on complete \(k\)-ary tree words proves the total and exact prefix maxima and minima. A full hierarchical stage then has an explicit maximum and endpoint minimum; logarithmic comparison between stage index and stage length proves the two sharp infinite limits. The standalone finite verifier checks direct recurrence against the symbolic model across 24 parameter pairs, but is not substituted for the induction. Boundary cases \(q=1\) and negative stage drift are addressed.

## Originality
**PASS, with residual risk.** The closest published sources are Cloitre's Proposition 4.3 and Fokkink--Joshi's Lemma 5 (word/morphism), Ruskey--Deugau's exact shifted-tree inverse-position formulas (Theorems 25/27), together with their density asymptotic, and the OEIS A045412 entry. Relevant primary full text was examined; none of these inspected statements identifies the uniform two-parameter exact finite-stage extrema or both logarithmic slopes. The 2009 inverse-position formulas may imply the special \(x=k+1\) case, but Sections 6--7 do not state the full \(x\)-varying characteristic-word extremum theorem; this implication risk is explicitly retained. A previously recorded normal-limit claim for uniformly sampled indices is neither an implication of, nor an implication for, the present pointwise extremal classification; the common word representation is acknowledged. An unindexed equivalent consequence of the morphism remains possible.

## Mathematical value
**PASS.** The natural arithmetic invariant is the discrepancy of a self-referential integer sequence's missing-value counting function from its positive-density main term. The theorem gives **complete finite-stage extrema** and sharp infinite upper and lower slopes for every fixed pair of parameters, detecting positive, vanishing, and negative lower-envelope regimes. Those deterministic extremal features are not controlled by first-order density or the probabilistic central-limit description and are useful for studying uniform error terms and worst-case prefix behavior in morphic and meta-Fibonacci counting sequences.

## Closest literature and limits
The proof legitimately uses Cloitre's published tree-word theorem; novelty attaches only to the weighted-prefix extrema and their consequence. The conclusions exclude the finite-complement case \(x=2\) and varying parameters. The older exact inverse-position identities in the special \(x=k+1\) case may imply portions of the result, and earlier unindexed calculations using the same word may exist; no independent audit has been performed.

Self-review: passed. Independent audit: not yet performed.
