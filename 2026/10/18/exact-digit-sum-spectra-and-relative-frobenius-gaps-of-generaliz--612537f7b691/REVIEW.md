# Scientific assessment: generalized-repunit digit-sum spectra

## Correctness

PASS. Cyclic carrying preserves the multiple congruence modulo the repunit, strictly decreases positive multiset weight by one base carry decrement, and stops at a nonzero standard length-\(r\) numeral. Every terminal multiple is among the \(b-1\) constant-digit repdigits, fixing each residue class's smallest attainable weight. Inverse cyclic carrying and digit-exponent separation realize every weight in the claimed progressions. Coprime reduction modulo \((b-1)/d\) yields the exact gap count and conductor. The finite verifier checks independent residue reachability and constructs explicit witnesses, but is not cited as a universal proof.

## Originality

PASS within inspected literature. The 2020 sturdy/flimsy paper gives a general power-sum criterion, upward closure by \(b-1\), and a repunit sturdiness result, but not the complete weight progression thresholds. The 2023 directed-graph paper gives necessary congruence restrictions and poses exact-spectrum classification for failed-equality cases; its full text does not state the length-\(r\) answer. The 2009 digit-sum paper addresses fixed/equal digit sums and density of sturdy integers, rather than complete attainable weights of repunit multiples. The length-three case is already separately covered and excluded. Remaining risk: exact classified spectra could be elsewhere, or the 2020 methods may be recognized as yielding the result with little additional work; this assessment makes no independence claim.

## Value

PASS. An entire natural two-parameter family receives a complete, sharp digit-sum spectrum, including the exact number and maximal size of exceptional admissible weights. The result resolves the arithmetic-output-set question on generalized repunits of arbitrary length at least four, rather than recording a small computational table or a parameter-renaming exercise. Its cyclic-normal-form proof explains the phenomenon structurally and provides direct witnesses.

## Scope and limitations

Only the specified repunit family is classified. The relative invariants apply to multiples of \(d\), not all positive integers when \(d>1\). The work has not received an independent audit; the literature comparison is limited to sources materially inspected and searchable records.

Self-review: passed. Independent audit: not yet performed.
