# Same-model review

## Correctness
PASS. Kummer's theorem reduces the gcd valuation to the minimum borrow count. For \(N=p^s+p^t\), the only no-borrow subdigit selections are \(0,p^s,p^t,N\); the proper nonzero selections are not divisible by \(m\) because \(p>m\) makes \(p\) a unit modulo \(m\). The explicit admissible index \(k=mp^{t-1}\) creates exactly one borrow because \(m<p\). These two steps prove the exact valuation \(1\). The standalone verifier independently checks the borrow argument over a broad deterministic grid, exhaustively minimizes admissible borrow counts in bounded cases, and directly checks integer gcds in small cases.

## Originality
PASS with residual bibliographic risk. McTague's theorem covers \(p\equiv1\pmod m\), and his corrected weakening requires all selected powers to have the same residue modulo \(m\). Fairfax-Ball extends the theory to \(p\equiv-1\pmod m\) and explicitly describes the remaining relation to Wu. The present sparse theorem applies whenever two powers are additive inverses modulo \(m\), including non-\(\pm1\) prime residue classes; the explicit \(m=5\), \(p\equiv2,3\pmod5\) family is outside the stated coverage of those theorems. Targeted semantic-database and web searches did not locate an equivalent sparse-row theorem.

## Value
PASS. The theorem extends a very recent exact valuation program to a natural family in residue classes not handled by the \(\pm1\) formulas. It isolates a reusable mechanism—minimal two-digit zero-sums plus a universal one-borrow witness—and supplies an infinite exact family for each of the two previously untreated invertible residue classes modulo \(5\). This is a structural lemma, not a routine recomputation of a table.

## Closest literature and limitations
The closest sources are McTague's arXiv:1510.06696v5, Fairfax-Ball's arXiv:2609.37754v1, and Wu's arXiv:2606.20940v2. The result is limited to two unit digits in the base-\(p\) row and does not give a complete arbitrary-residue classification. Search cannot certify absolute historical priority; unindexed or differently phrased prior work remains a residual risk.

Same-model review: passed. Independent audit: not yet performed.
