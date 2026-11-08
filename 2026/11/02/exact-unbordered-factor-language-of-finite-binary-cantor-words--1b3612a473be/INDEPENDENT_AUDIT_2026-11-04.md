# Independent mathematical audit

## correctness

PASS

The number of intervening zeros after the i-th 1 is g_i=3^{ν₂(i)}, proved by doubling the iteration and the central 3^m gap. For words beginning in 1 and ending in 0 with final run t, a border would require an earlier gap at least t; conversely, from the first such gap divisible by 2^m and the final gap index also divisible by 2^m, matching ν₂ modulo 2^m constructs an actual shorter equal prefix and suffix (including the r=0 case). Thus unbordered iff every earlier complete gap is shorter than t. Modular restriction forces the preceding gaps to be a suffix of C_m and terminal t∈T_m, and the construction occurs before the next central gap. The palindrome property yields reversed orientation; distinct t,m and different numbers of ones distinguish j. Summing 2+2[1+Σ 2^m(3^m−3^{m−1})] gives the formula; the unique maximal suffix at m=k−1 yields the two longest factors. Independently enumerated every substring and tested borders naively for k=1..4, with exact set equality; this is finite corroboration of the valuation argument.

## originality

PASS

Automatic-word unbordered-factor counting is established theory, but Goč–Mousavi–Shallit (2012) full primary paper studies Thue–Morse and period-doubling/Rudin–Shapiro, with no Cantor substitution classification in its inspected sections. Permutation-complexity studies treat precisely Cantor-like substitution but a different invariant; general string border algorithms give maximum-length computation without the all-rank explicit language. No equivalent full finite Cantor factor set was identified; a less indexed sequence-specific count remains plausible.

## value

PASS

The finite Cantor substitution is canonical and extremely nonuniformly recurrent. A complete structural classification of all distinct unbordered factors is more informative than an arbitrary numerical table: the 2-adic ruler-gap lemma explains which terminal runs generate border-free words and gives closed growth Θ(|C_k|^{log_3 6}) and exact longest factors. These explicit finite languages can serve as benchmarks for algorithmic word combinatorics.

The dated certificate retains the supplied scientific assessment, sources and limitations.
