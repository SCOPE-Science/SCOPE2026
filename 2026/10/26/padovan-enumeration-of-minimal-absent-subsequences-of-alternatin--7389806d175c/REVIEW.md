# Independent mathematical audit

## correctness

PASS

Greedy embedding of a word u of length L with r runs and initial-one indicator s uses c(u)=2L-r+s positions in the alternating infinite word; u is absent iff c(u)>2k. Deleting an interior singleton (or an initial zero singleton) does not lower cost, hence MAS structure excludes them. Allowed last-run>=2 words must have c=2k+1 or 2k+2; allowed last-singleton words require c=2k+1. Weighted-run generating series with Q=x^3/(1-x^2), P=x/(1-x^2) give rational A(x), B(x) and the stated even/odd coefficient extraction. Every length-k word embeds; length-(k+1) absent words are 0^(k+1),1^(k+1), and 1^i0^(k+1-i), i=1..k, exactly k+2. Independent brute-force candidate enumeration k=1..8 counted 3,5,9,16,28,49,86,151 MAS and k+2 SAS, checking deletions directly. Infinite recurrence follows algebraically, not by finite induction over checked host lengths.

## originality

PASS

Kosche et al. 2021/2023 introduce MAS/SAS and give a >=4-symbol exponential-polynomial separation, but the inspected full text does not present the alternating binary Padovan count. Adamson et al. 2024 bound length-specific absent words, not the total MAS of this host; Manea et al. 2025 give algorithms. The Padovan numbers are known OEIS A000931, but their identification with this natural MAS host and exact GF are the claimed result.

## value

PASS

The minimal-versus-shortest absent-subsequence gap is a core object of the literature. A simple 2-symbol periodic host exhibits exponential versus linear growth, improving the alphabet complexity of prior explicit separation and giving an exact generating function, growth constant and combinatorial interpretation of a classical sequence. This is a natural full infinite-family classification, not an unexplained table match.

The dated certificate retains the supplied scientific assessment, sources and limitations.
