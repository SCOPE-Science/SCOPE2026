# Review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

The proof reduces the near-minimum problem to a sharp width gap for defective sequences.

The key local lemma was checked directly in the difference triangle: if all anti-diagonal entries after \(e_i\), except the terminal \(1\), are zero, then row \(i\) has the form
\[
(1,e_i,e_i,\ldots,e_i),
\]
so the next left-edge entry is \(|e_i-1|=1\), forcing \(e_i\in\{0,2\}\).

For a defective sequence, choose the rightmost failure of Muney's interval-completeness inequality and let \(B\) be the anti-diagonal tail sum to its right. The suffix reverse tree is the complete even interval \(\{0,2,\ldots,B+1\}\). The zero-suffix lemma excludes \(B=1\), hence \(B\ge3\). Reversing the failing fold produces \(B+2\ge5\) positive distances. Earlier reverse steps cannot reduce cardinality. If zero never appears, the two-sided extension width is at least \(10\); if zero appears, its first appearance adds it to an injectively translated set of at least five positive values, giving at least six distances and width at least \(11\). This establishes the defective-width gap without computation.

The equivalence \(|K_S|\le9\iff A(S)\le7\) then follows from the candidate bound \(|K_S|\le A(S)+2\) and the interval-complete equality \(|K_S|=A(S)+2\). The explicit width-\(5,7,9\) anti-diagonal forms are obtained from parity, positivity of \(e_1\), the terminal value \(e_{n-1}=1\), and the same zero-suffix lemma.

A standalone exact-integer program enumerates all sequences through \(n=10\) and checks the theorem and the three structural forms. The resulting total counts agree with the published enumeration \(1,2,6,27,180,1786,26094,559127\) for \(n=3,\ldots,10\).

## Originality

Originality is assessed to the best of our knowledge.

The closest source inspected in full is Muney, arXiv:2606.23721v2. It proves the reverse-tree characterization and exact interval-completeness criterion, identifies the first defective sequence, and proves the unique minimum width \(5\). Section 16 then explicitly asks as Open Question (5):

“Stability classification near the minimum: characterize \(S\in\mathcal G_n\) with \(|K_S|\le9\).”

The present theorem answers that question by the invariant condition \(A(S)\le7\), proves that every defective sequence has width at least \(10\), and gives the corresponding anti-diagonal forms.

Searches covered exact and synonymous combinations involving Gilbreath sequences, valid-extension sets, extension width, anti-diagonal sums, near-minimum stability, width \(9\), and follow-up work citing or naming Muney's paper. OEIS entries linked from the paper were also checked for nearby finite-Gilbreath classifications. No matching theorem or later solution to the stated open question was located.

The main residual originality risk is the recency of the June/July 2026 source: a synchronous or very recent follow-up could be incompletely indexed. No inaccessible paper was identified whose metadata specifically suggests that it contains this classification.

## Value

The result closes an explicit open problem from the closest paper and reveals a genuine gap phenomenon:
\[
5,\ 7,\ 9,\ \text{then at least }10.
\]
More structurally, a single scalar invariant, the anti-diagonal sum \(A(S)\), completely controls the extension set throughout the entire near-minimum regime. The proof also isolates a reusable mechanism: the rightmost failed folding inequality creates at least five positive reverse branches, while the Gilbreath boundary condition rules out the only smaller tail.

## Limitations

The theorem classifies only the regime \(|K_S|\le9\). Widths \(10\) and above can be highly disconnected and are not classified here. The result concerns finite strictly increasing Gilbreath sequences and does not address the prime-sequence Gilbreath conjecture itself. No independent validation is asserted.
