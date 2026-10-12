# Review of Coprime rigidity and exact prime-base collisions for digit sums

## Correctness
PASS. The proof reduces a hypothetical collision between base-coprime multipliers to a proper repeated base-\(b^\ell\) block. Choosing \(n_m=(b^m-1)/a\) forces the \(a\)-ray to have maximal digit sum \((b-1)m\). On the \(c\)-ray, the Euclidean remainder of the coprime ratio produces a repeated block \(A\) with \(1\le A\le b^\ell-2\), hence a strict one-unit digit-sum deficit per block. Subtracting the fixed quotient term can alter only boundedly many low blocks, so it cannot cancel the linear deficit. Symmetry gives equality of the multipliers. The prime-base classification follows by removing powers of the base prime, which only append zero digits. The bundled checker independently exercises the block identity and bounded finite instances.

## Originality
PASS relative to the checked material. The 2021 source explicitly poses the digit-sum multiplier-ray question but supplies no solution. The 2023 related paper studies ordinary injectivity of \(H_b(n)=nS_b(n)\), which is statement-distinct and does not imply ray rigidity. Targeted semantic-database queries for the exact coprime formulation, the prime-base equivalence, power-of-base aliases, and the source's Question 20 returned no implication-equivalent result. The closest indexed quasi-injectivity record concerns compositions with the divisor-counting function and a different numbered question.

## Value
PASS. The result is directly motivated by an explicit published open question. It separates the obvious positional-shift obstruction from genuine multiplier ambiguity, proves a rigidity theorem in every base, and gives a complete if-and-only-if classification for all prime bases. This is a structural resolution rather than a bounded example or a renaming of the shift identity.

## Closest literature and limitations
The closest primary source is Pongsriiam's Question 20, which asks whether digit-sum equality on every multiplicative ray forces equality of multipliers and whether the question extends to arbitrary bases. The later Noppakaew--Pongsriiam paper includes \(S_b\) only inside the product \(nS_b(n)\). No claim is made here about a full collision classification for composite bases or about iterated digit sums.

Self-review: passed. Independent audit: not yet performed.
