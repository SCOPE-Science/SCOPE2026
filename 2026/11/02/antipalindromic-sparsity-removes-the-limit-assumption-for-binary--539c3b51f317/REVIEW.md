# Scientific review

## Correctness (C): PASS
The proof treats every non-ultimately-periodic binary infinite word. XOR differencing preserves non-ultimate periodicity: an eventually \(h\)-periodic derivative forces the source to be eventually \(2h\)-periodic. Every antipalindromic length-\(n\) factor maps to an ordinary palindromic length-\(n-1\) factor, with at most two inverse lifts. The derivative factor count is at most the original factor count at the shifted length. The cited Shallit theorem applies to the derivative and yields the strong logarithmic antipalindromic-sparsity limit. Its application to the source gives ordinary palindrome sparsity. Finally, Burnside's lemma for the four group elements, with zero nonempty complement fixed points, gives the unconditional \(1/4\) ratio. Edge cases \(n=1\) and zero palindrome counts do not alter the asymptotic conclusion. Exact finite tests were replayed from the embedded checker, not used as an infinite proof.

## Originality (O): PASS with residual priority risk
Blažek–Dvořáková–Pelantová, arXiv:2610.14637v1, Theorem 36 is conditional on existence of the ratio limit. Their Remark 37 explicitly notes that an antipalindromic analogue of Shallit's sparsity theorem would remove the condition. The claimed unconditional result is not implied by their displayed inequalities alone. Shallit's arXiv:2606.08127v3 addresses ordinary palindromes; the new binary XOR-derivative reduction supplies the missing comparison for antipalindromes. The earlier Pelantová–Starosta symmetry theory provides adjacent-length inequalities and Burnside context, not the proposed unconditional limit. published-finding corpus searches by exact topic and alternate terminology and accessible earlier claims found no stronger covering result. A previously unindexed argument using the same derivative map remains possible; no definitive uniqueness is claimed.

## Value (V): PASS
This resolves a specific hypothesis gap explicitly isolated by the 2026 authors. It proves convergence, rather than just identifying a possible limit, for all aperiodic \(H\)-invariant binary languages, even when complexity growth oscillates and no recurrence is assumed. The strong antipalindromic estimate is itself useful for bounding generalized-palindrome statistics across binary symbolic systems, not simply a numerical special case.

## Closest literature and limits
The closest source is Blažek–Dvořáková–Pelantová (2026), Theorem 36 and Remark 37; Shallit (2026) supplies the ordinary-palindrome theorem, with a distinct object and hypothesis. Binary alphabets, the four-element symmetry group, and language invariance delimit the scope. There is no claimed finite convergence rate or independent mathematical validation.

Self-review: passed. Independent audit: not yet performed.
