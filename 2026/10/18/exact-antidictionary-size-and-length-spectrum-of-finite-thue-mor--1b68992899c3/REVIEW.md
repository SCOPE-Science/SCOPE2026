# Review: exact finite Thue–Morse antidictionary

## Correctness — PASS

The proof uses the published classification of infinite bispecial Thue–Morse factors, and explicitly verifies how two-sided extensions transform under substitution. An independent parity-desubstitution induction establishes the exact factor-complexity cutoff at length \(2^{m-2}+1\). The five extra minimal absent factors are precisely the infinite factors missing at the next length, by a matching finite/infinite count. Exhaustion eliminates longer candidates. The standalone checker reproduces all minimal absent factors and their spectra for \(3\le m\le9\), and the context parity for multiple substitution levels. The infinite claim is proved symbolically; finite tests alone are not used as proof.

## Originality — PASS against the inspected work, with residual risk

The closest primary work, Radoszewski–Rytter (2012, DOI 10.1016/j.jda.2011.01.001), gives the infinite bispecial families and compacted factor graphs, but the inspected statements do not provide an exact finite antidictionary cardinality or its sharp length spectrum. Barton et al. (2014, DOI 10.1186/s12859-014-0388-9) give a general minimal-absent-word algorithm, not the evaluated substitution-family formula. Search comparisons included alternate names (minimal forbidden factors, antidictionaries, weak bispecials), fixed-length factors versus absent subsequences, and related published work on Thue–Morse string attractors. Earlier complete graph descriptions contain enough information from which related counts may be derivable; a prior published derivation remains possible.

## Value — PASS

Antidictionaries are compact descriptions of forbidden factors. The theorem determines a natural and complete invariant for every binary Thue–Morse iterate: exact logarithmic size, every permitted length, and the five maximal boundary exclusions. It separates hereditary infinite-language obstructions from finite-endpoint effects, a distinction useful when reasoning about bounded automatic-string languages.

## Limits

This review covers only the presented claim for dyadic iterates; no statement about arbitrary Thue–Morse prefixes or independent certification is made.

Self-review: passed. Independent audit: not yet performed.
