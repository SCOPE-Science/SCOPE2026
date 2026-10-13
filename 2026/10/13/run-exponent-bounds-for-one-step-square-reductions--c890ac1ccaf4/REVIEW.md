# Self-review

## Correctness
PASS. For each root length \(p\), distinct one-step reductions are exactly the maximal length-at-least-\(p\) runs of matches \(W_t=W_{t+p}\). The associated factor is maximal with period \(p\). Fine--Wilf implies that its minimum period divides \(p\), and divisibility transfers maximality to the minimum period, so the factor is a standard run. Each run contributes at most \(\lfloor e(R)/2\rfloor\) possible root labels. Published run-exponent bounds then give the constants \(23/20\) and \(11/10\). The bundled checker exhaustively verifies the local correspondence on all binary words through length \(11\) and all ternary words through length \(7\).

## Originality
PASS. The direct source leaves \(\deg_k^+(n)\le n\) conjectural. The closest distinct-square theorem concerns a different invariant, and the closest run-exponent theorem supplies aggregate bounds without connecting runs to square-reduction outputs. Targeted searches found no statement implying the charging inequality or its two explicit consequences.

Residual risk remains from unindexed notes or theses using equivalent periodicity language.

## Value
PASS. The theorem gives a universal coefficient \(23/20\), and \(11/10\) in the binary case, toward the explicit coefficient-\(1\) conjecture. The run-charging lemma is reusable: any stronger bound for total run exponent immediately improves the square-reduction bound.

Self-review: passed. Independent audit: not yet performed.
