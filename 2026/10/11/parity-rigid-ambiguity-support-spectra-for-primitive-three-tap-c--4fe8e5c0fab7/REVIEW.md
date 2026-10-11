# Scientific review: primitive three-tap self-ambiguity spectra

## Correctness — PASS
The five possible time-delay rows are disjoint for every cyclic order at least five, and a unit-step change of coordinates permutes sampled frequencies. The two outer rows cannot vanish, the two two-term rows have conjugate root parameters and therefore synchronized zero counts, and the positive real quadratic in the central row has exactly the stated sampled-root trichotomy. The proof handles the repeated root at \(-1\) as one distinct zero, proves the all-orders formula, and supplies explicit witnesses for every asserted parity-dependent support size. The extracted standalone checker corroborates 560 examples, not a universal theorem.

## Originality — PASS, with limitations
Nicola's 2022 paper gives the global support bound and equality characterization, not the five coupled Fourier-row spectrum for primitive three-tap self-windows. Krahmer–Pfander–Rashkov, Proposition 4.4, already implies the prime-order lower bound \(5p-4\) for support-three pairs, and that known numerical consequence is explicitly excluded from the novelty claim. Their Table/Figure data do not classify self-ambiguity coefficient strata or parity gaps across all orders. The inspected public two-sparse STFT trichotomy is restricted to two-point signal/window supports. No indexed equivalent of the full three-tap self-spectrum was found; an unindexed treatment remains possible.

## Value — PASS
The result is a complete natural first three-tap ambiguity-support classification (rather than a single artificial coefficient evaluation): it gives the full spectrum and every minimum-attaining coefficient triple across infinitely many cyclic orders, identifies phase-sensitive paired row cancellations, and exhibits two parity-forbidden levels despite an identical sharp minimum. Such exact support information distinguishes attainable localization patterns and makes the prime/composite and odd/even sampling boundaries explicit; it is not merely a restatement of the already known prime-order lower bound.

## Closest literature and limits
F. Nicola, arXiv:2204.14176, §§1–4; F. Krahmer, G. Pfander, P. Rashkov, arXiv:math/0611493, Proposition 4.4 and Figure 6; public result `2026/10/4/SCOPE-exact-support-trichotomy-for-two-sparse-prime-cyclic-stfts--5b84852d543c`, RESULT.md. The exact claim is restricted to three consecutive sites up to primitive affine change, and has only same-model scientific review. No independent audit or universal computer certificate has been performed.

Same-model review: passed. Independent audit: not yet performed.
