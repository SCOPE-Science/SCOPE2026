# Scientific review: dyadic separation periodicity

## Correctness — PASS

The theorem specifies all positive window lengths and every admissible separation. The substitution yields exact even/odd decimations; infinite recurrence of each finite factor justifies empty-window bases. The one-by-one separation spectrum is proved for all gaps, and strong induction on the maximum of the two lengths reduces any claim to strictly shorter windows, with divisibility of dyadic periods. The two-letter table follows by direct substitution and certifies its least period. The accompanying script checks independent sequence constructions and 34,031 bounded assertions. No finite-prefix exhaustion is used as an infinite proof.

## Originality — PASS, with residual risk

The principal accessible primary source is Rigo–Stipulanti–Whiteland, arXiv:2206.15319 (2022); its definition exactly matches the equal-length specialization, but its general automaticity theorem does not imply pure periodicity. The relevant source text, introduction, definitions, theorem discussion and the boundary examples were inspected. Searches for the period-doubling boundary spectrum, its aliases, mixed-window correlations, dyadic separation laws and existing research records did not reveal a statement implying this theorem. Huang–Wen, arXiv:1703.07157 (2017), concerns return-word occurrence spectra; the full text was inaccessible, so latent equivalent statements are possible. Searches do not prove uniqueness.

## Value — PASS

The original boundary-sequence problem asks which prefix/suffix combinations can coexist at a specified distance. This theorem upgrades automaticity to an explicit purely periodic law for every window length, even for unequal windows, and resolves the two-letter spectrum exactly. It supplies an infinite constructive compression from infinitely many distance values to at most \(2^{1+\lceil\log_2\max(a,b)\rceil}\) residue classes. The result does not claim a general law for all automatic words or universal optimality of the period bound.

## Source and verification limitations

Primary source: https://arxiv.org/pdf/2206.15319. Supporting fixed-point identity: https://oeis.org/A096268. Plausible related inaccessible full text: https://arxiv.org/abs/1703.07157. Finite experiments support but do not establish the infinite theorem. Bibliographic coverage is necessarily incomplete.

Self-review: passed. Independent audit: not yet performed.
