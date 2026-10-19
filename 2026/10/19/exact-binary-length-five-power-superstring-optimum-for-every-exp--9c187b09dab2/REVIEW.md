# Scientific review: fifth-root binary power-superstring spectrum

## Correctness

**PASS.** The statement quantifies over every integer exponent \(p\ge3\) with binary roots of length five and ordinary linear hosts. The shortest-common-superstring problem reduces exactly to a Hamiltonian overlap-path minimum for \(32\) distinct equal-length words. Distinct rotation-class roots can overlap in at most four positions, while transitions within a class have a power-independent minimum positive shift distance. Consequently, a path with eight or more class changes costs at least \(45p-9\), strictly above the exhibited \(40p+2\). For the remaining seven-transition paths the necklace blocks are contiguous and an integer subset dynamic program exhaustively evaluates all \(4096\) block/end states, giving a sharp cubic value of \(122\). The cost scaling by \(40\) per added repetition is exact, not a numerical extrapolation. The standalone package enumerates the local permutations, the complete grouped dynamic program and the explicit witness, and checks smaller cases against an unrestricted Hamiltonian-mask dynamic program. No outside solver status or unproved infinite computation is needed.

## Originality

**PASS against inspected sources, with residual risk.** Au's arXiv:0904.3997, Section 3, states a general lower bound which specializes to \(40p-8\) and a conjugate-cover construction giving relevant upper bounds. It does not establish the sharp matching lower bound, the cubic base optimum, or the all-optima class-block property. An available ten-symbol conjugate cover yields the upper value \(40p+2\) by Au's method, so the construction alone is not new; the certified lower bound and forced block structure are the contribution. OEIS A372435 concerns binary squares rather than higher powers, so that sequence does not cover this exponent range. Targeted mathematical-record and literature searches found no equivalent theorem; unseen computations, alternate formulations and incomplete indexing remain possible.

## Mathematical value

**PASS.** The result closes a ten-symbol gap between an established general lower bound and an attainable upper bound for a natural entire infinite exponent family. It supplies a sharp periodic-block superstring invariant, an unrestricted optimality proof, and a strong structural constraint on all optimal overlap orderings, not merely a short example or a known numerical table entry. It is deliberately restricted to the first useful unclassified five-symbol root class and makes no unsupported claim for other root lengths.

## Limits and closest literature

Yu Hin Au, *Generalized de Bruijn words for Primitive words and Powers*, arXiv:0904.3997 (v1 April 25, 2009; Section 3 of v5 read); OEIS A372435 (square superstrings). The finite dynamic program is exhaustively reconstructible from `verify.py` and `CERTIFICATE.json`. This is not a human-independent mathematical audit and does not exclude equivalences in presently unindexed publications. The statement does not address cyclic hosts, noninteger powers, nonbinary alphabets or all optimal host multiplicities.

Self-review: passed. Independent audit: not yet performed.
