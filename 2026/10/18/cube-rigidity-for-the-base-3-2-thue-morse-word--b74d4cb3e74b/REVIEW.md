# Scientific review: coprime-period cube rigidity

## Correctness — PASS
The generating recurrence implies aligned blocks \(a_m(1-a_m)a_m\). An equal adjacent pair can occur only at a block boundary, while the even-sampled symbols \(a_m\) cannot have four alternating terms. These two exact constraints force any cube whose period is coprime to three to be alternating, with period two and length six. The no-ten-bit-alternation lemma proves the sharp \(9/2\) upper bound, which is attained at positions \(12\)–\(20\). The accompanying exact verifier independently checks the first 50,000 letters and the stated bounded period range, but finite observation is not used to establish the infinite theorem.

## Originality — PASS within checked evidence
The same-word primary source (Dekking, arXiv:2301.13563, 2023) proves the recurrence and presents an unrestricted critical-exponent conjecture. Dekking–Keane (2023) includes an alternating fourth-power example; the later Cassaigne–Espinoza–Rigo–Stipulanti manuscript (arXiv:2602.21895) concerns frequencies, morphic relations and recurrence. OEIS A357448 contains finite values and the defining substitution. None of those examined results states, or by its given conclusions establishes, the exact coprime-to-three cube classification or its sharp restricted exponent. An unindexed equivalent theorem remains possible.

## Mathematical value — PASS
The three-fold block boundaries make the divisibility of periods by three a mathematically intrinsic split, not a chosen numerical slice. The theorem identifies the complete cube spectrum on one side of that split and a sharp restricted critical exponent, giving a structural partial answer to the published critical-exponent problem.

## Limitations
The unrestricted critical exponent, and repetitions at periods divisible by \(3\), remain unresolved by this proof. Further specialist review may reveal equivalent literature. The finite executable checker is not a substitute for the universal argument.

Self-review: passed. Independent audit: not yet performed.
