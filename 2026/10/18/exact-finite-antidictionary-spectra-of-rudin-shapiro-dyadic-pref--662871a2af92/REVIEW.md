# Scientific review of exact finite Rudin–Shapiro antidictionary spectra

## Correctness — PASS
The prefix generator is independently compared with the exact binary two-kernel recurrence at each of the ten levels. The candidate-reduction lemma proves that every minimal absent factor has its central core among positive adjacent suffix LCPs or the empty core. Exact left/right/bilateral extension sets enumerate all and only minimal absent factors. `verify.py` exhausts every finite input level \(7\le m\le16\) and checks the full sorted-result SHA-256 digests in `SPECTRUM.tsv` as well as every claimed bin and a direct all-factor verifier for the first two levels. The result is finite: it does not rely on a false inference from finite experiments to all \(m\).

## Originality — PASS against inspected sources
Full material of Allouche–Bousquet-Mélou (1994) studies infinite Rudin–Shapiro factor languages and their factor complexity, not exact minimal-absent-factor spectra of ten finite dyadic prefixes. Barton et al. (2014) provide general suffix-array enumeration methods, but do not report these exact specialized outputs. OEIS A005943 concerns a non-equivalent counting invariant. published-finding corpus similarity searches for antidictionary, minimal forbidden factor, minimal absent word, numeric data, and source aliases returned only non-covering related records; SCOPE079 is a string-attractor calculation and was viewed only by indexed summary. A broader or previously unindexed table remains a meaningful risk; nonhits do not prove absolute priority.

## Value — PASS
The theorem gives a full finite antidictionary classification for ten natural prefixes of a well-studied automatic sequence, reaching length \(65536\). The patterned length histogram, exact boundary maximum and stable increment of eight per doubling provide concrete benchmarks for minimal forbidden factors and further structural work. It is not a routine parameter substitution into the known infinite factor-complexity formula, and the classification does not claim an unproved extension.

## Limits and evidence
Scientific scope: strictly \(7\le m\le16\), linear rather than cyclic words, contiguous rather than scattered factors. Independent audit has not been conducted; earlier literature may contain unindexed special-case antidictionaries. Computation is reproducible from the embedded `verify.py` and `SPECTRUM.tsv`; the proof of exhaustiveness is written in `RESULT.md`.

Self-review: passed. Independent audit: not yet performed.
