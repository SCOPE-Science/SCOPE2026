# Review

## Correctness
PASS. The proof translates equality of every deletion magnitude into exact Fourier-autocorrelation equations. For a nonzero shift \(r\), the difference variables satisfy \(T=d_\ell+d_{\ell-r}\). On odd-order \(r\)-cycles this recurrence has the stated form, and summing all cycles forces \(T=T(n-1)/2\); hence \(T=0\) for odd \(n\ge5\). The zero-shift equations then recover every Fourier magnitude, so all entries of the rank-one Fourier Gram matrix agree. The even-order and small-order failures are explicit and directly checked. The packaged verifier independently replays the derived finite linear systems over \(\mathbb Q\).

## Originality
PASS. The closest primary source is Bartusel--Führ--Oussa, arXiv:2109.07123. Its Remark 6.12 proves the deletion observation in the prime-field setting and explicitly says that it is unclear whether the observation extends to general cyclic groups. The present statement gives a complete cyclic classification, including all odd composite orders and explicit failure at every even order. Focused searches using the deletion, Pauli-pair, cyclic-group, and Fourier-projection formulations found no equivalent or stronger indexed result. The main residual risk is an equivalent theorem under different terminology in literature not surfaced by those searches.

## Value
PASS. This is a sharp answer to an explicit finite-Fourier-analysis question in the primary source. It exposes a structural parity mechanism: odd additive cycles force the autocorrelation-difference system to collapse, while the order-two character creates a universal obstruction in even cyclic groups. The result is a complete infinite-family classification rather than a finite census or a parameter-only refinement.

Same-model review: passed. Independent audit: not yet performed.

## Closest literature and limitations
The primary comparison is Remark 6.12 of arXiv:2109.07123. The theorem here does not address noisy measurements, optimal conditioning, sparse subsets of deletion operators, or noncyclic finite abelian groups. Those remain outside the claim.
