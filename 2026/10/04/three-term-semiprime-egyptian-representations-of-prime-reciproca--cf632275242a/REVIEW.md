# Same-model review

## Correctness
**PASS.** The denominator convention is explicit: each denominator is a product of two distinct primes and all denominators are distinct. Encoding denominators by edges gives a finite simple graph. Multiplication by the product of all support primes and reduction modulo a non-target vertex proves that every such vertex has degree at least two. This rules out lengths one and two and forces a three-edge representation to be a triangle. The triangle equality is exactly equivalent to \((q-1)(r-1)=p+1\), and the converse is immediate. The residue-class corollary follows from parity modulo four. Li's theorem is used only to know that the minimum length is finite.

The exact-arithmetic verifier checks finite instances but is not used to infer the infinite theorem.

## Originality
**PASS.** The closest source, arXiv:2609.32140v1, proves unrestricted existence for all squarefree rational denominators and explicitly uses a prime graph, but its result is existential and its full text contains no minimum-length discussion. The predecessor arXiv:2606.15159v2 and Butler--Erdős--Graham's three-prime-denominator paper likewise do not imply the claim. Exact published-findings database searches for the three-term triangle, shifted-prime factorization, minimum length, and leaf obstruction returned no covering finding. Web searches for the exact identity and factorization found no scholarly statement of the classification. An informal puzzle page has a related modular relation for integer targets; it does not cover this theorem.

Residual risk remains that such an elementary classification could exist as unindexed folklore or a problem solution. The claim therefore does not assert novelty of the modular leaf lemma by itself; the reviewed claim is the complete three-term prime-reciprocal classification.

## Value
**PASS.** The result gives a natural exact boundary immediately adjacent to a new existence theorem: it determines when the shortest possible semiprime Egyptian representation of \(1/p\) has three terms. It also yields the clean consequence that for \(p\equiv1\pmod4\), three terms occur exactly when \(p+2\) is prime. This supplies structural information about representation length, not merely another existence construction.

## Closest literature and limitations
Li's September 2026 theorem supplies existence for all squarefree rational denominators but no quantitative minimum length. Li's June 2026 paper covers all natural numbers and rational targets above a threshold. Butler--Erdős--Graham concern products of three distinct primes. The present theorem does not determine the exact minimum when the three-term factorization fails; it proves only a lower bound of four in that case.

Same-model review: passed. Independent audit: not yet performed.
