# Scientific review: matched three-tap STFT support

## Correctness — PASS

For each time shift, the STFT is a prime cyclic Fourier transform of a masked product with support size equal to the overlap multiplicity. The sharp prime Fourier row bound gives at most \(r-1\) zeros when this overlap has cardinality \(r\). Three-point difference geometry gives overlap lists \((3,2,2,1,1)\) or \((3,1,1,1,1,1,1)\), proving the respective lower bounds. The explicitly factored signal/window pair realizes every permitted four-hole progression pattern; nonprogressions attain any two central holes using nonvanishing Fourier minors. Multiplying the two side-row root identities proves the necessary resonance law. Exact cyclotomic checks through prime \(13\) independently corroborate all geometric and constructive cases. Risk: the finite checker alone cannot establish the universal prime statement; the supplied proof does.

## Originality — PASS, subject to bibliographic limits

Nicola's primary article proves equality classification at the universal support threshold but does not make the matched three-tap exact-minimum or four-hole statements. Tao supplies the prime Fourier minor lemma and uncertainty inequality, which govern one shift at a time; they do not imply simultaneous attainability of four zeros. A published two-sparse STFT classification does not cover three-point signal/window supports. Targeted searches for three-sparse cyclic STFT minima, equal-support windows, and the four-hole resonance identity did not uncover an equivalent formula. Risk: specialized Gabor or sparse-filter literature could express this finite-dimensional result under different terminology. The claim is not independently certified.

## Value — PASS

The distinction between progression and nonprogression supports is a complete infinite-prime classification of the sharp short-time Fourier support for the first matched three-tap problem beyond the two-tap case. Its exact zero-pattern enumeration adds information beyond generic uncertainty bounds. The product constraint coupling two side shifts to two central Fourier zeros is a structural consistency law, not a numerical recomputation or a single arbitrary example. The scope is deliberately limited to matched three-point supports.

## Closest literature and limits

Fabio Nicola, arXiv:2204.14176v1, Theorem 1.2 and Sections 2–4 (full text inspected); Terence Tao, arXiv:math/0308286, Theorem 1.1 and Lemma 1.3 (full text inspected); published two-sparse prime cyclic STFT support classification (summary inspected, full public page unavailable). The latter two furnish relevant context, not the claimed matched three-tap classification. The manuscript's exact algebraic construction and finite tests are included; an independent audit remains outstanding.

Self-review: passed. Independent audit: not yet performed.
