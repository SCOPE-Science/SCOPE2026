# Scientific review

## Correctness — PASS

The short-relation lemma reduces a hypothetical multiple with at most \(b\) digits counted with multiplicity to an integer relation \(\sum_i c_i b^i\equiv0\pmod{b^r+1}\) having \(\ell^1\)-weight at most \(b\). The two boundary cases \(\max|c_i|=b\) and \(\max|c_i|\le b-1\) are separately ruled out unless the coefficients vanish; vanishing forces even total digit sum. The explicit \(b+1\)-digit witness and ordinary two-digit modulus are multiples, and carry-free concatenation realizes the entire positive semigroup they generate. All quantifiers are handled for even \(b\ge2\), \(r\ge2\), and all positive multipliers. The executable finite-state checks agree for 35 test settings; they do not establish the infinite theorem.

## Originality — PASS within inspected evidence

[1, Theorems 1–3] proves cofiniteness and guarantees multiples of a known digit sum, but neither determines the exact excluded odd values nor the Frobenius number for the present family. [2, Theorems 3–4] gives generic reachability/construction principles without the sharp signed short-relation obstruction. The accessible prior spectrum for multiples of \(b+1\) covers \(r=1\), which is explicitly excluded. The even-exponent family \(b^{2h}+1\) is coprime to \(b+1\) for even \(b\), so that prior modulus does not dominate it by divisibility. Targeted literature, database, and mathematical-result searches identified no statement implying the new full family; unindexed overlapping sources remain a risk.

## Mathematical value — PASS

This is a complete natural infinite-family classification of the digit-sum output sets sought in [1, Question 4]. For even bases it sharpens an existence/cofiniteness criterion into an exact conductor \(b\), Frobenius number \(b-1\), and a finite exceptional set of cardinality \(b/2\). The unusual independence from arbitrarily large exponent \(r\) supplies a benchmark for automata-based computation of digit-sum spectra. It is not a purely negative or normalization check.

## Closest literature and limits

The 2023 directed-arc paper [1] states the motivating Frobenius-number question (Question 4); Question 2 concerns the distinct non-coprime regime, and this theorem does not answer it. The 2020 sturdy/flimsy paper [2] contains the strongest inspected general digit-sum attainability machinery. The classification does not count representations, determine shortest witness size, or handle other cyclotomic moduli. Earlier unindexed coverage is not excluded by keyword searches. Computer checks and this review are not independent validation.

Self-review: passed. Independent audit: not yet performed.

## References

[1] Phunphayap–Noppakaew–Pongsriiam, arXiv:2303.13017v1 (2023).

[2] Clokie–Lidbetter–Molina Lovett–Shallit–Witzman, arXiv:2002.02731v1 (2020).
