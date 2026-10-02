# Mathematical audit — 2026-10-01

## Final claim assessed

Binary classification of even exactly k-deficient-perfect numbers with two prime factors

## Correctness — PASS

PASS. Writing the deficiency \(\Delta=2n-\sigma(n)\) gives the exact base-\(p\) expansion with first digit \(t=p-(2^{a+1}-1)\) and all later digits \(t-1\). Positivity forces \(p>2^{a+1}-1\), while \(\Delta<p^b\) excludes divisors from the top \(p^b\)-layer. Every selected lower layer has a binary coefficient at most \(2^{a+1}-1<p\), so uniqueness of base-\(p\) expansion forces those digits exactly; binary uniqueness then gives the unique divisor set and its Hamming-weight cardinality. Independent sample calculations reproduce the stated examples, and the repository exact subset-sum scan is consistent supporting evidence.

## Originality — PASS

PASS to the best of current knowledge. Chen's primary 2019 paper was inspected at its abstract and main classification theorem: it treats odd exactly two-deficient-perfect numbers with two distinct prime divisors, not the arbitrary-\(k\) even family. The 2021 exactly-three paper likewise concerns the odd case, while Tang--Ren--Li supply the known \(k=1\) deficient-perfect slice recovered as a specialization. Resultary searches for the arbitrary-\(k\) even two-prime classification returned only the assigned record. No inspected source gives the short prime interval, unique divisor representation, or binary-weight formula.


### equivalent_formulations

Searches: Resultary: exactly k-deficient-perfect even two prime factors binary Hamming weight classification; web: \(2^a p^b\) exactly k deficient perfect

Evidence: The exact semantic search returned only the assigned arbitrary-\(k\) record. Primary sources found for \(k=2\) and \(k=3\) concern odd integers.

Reasoning: Subset-sum, deficiency and exact-\(k\) formulations were compared; none inspected is equivalent to the full even two-prime theorem.
### broader_coverage

Searches: Chen 2019 exactly k-deficient-perfect PDF; Aursukaree--Pongsriiam 2021 exactly 3-deficient-perfect; Tang--Ren--Li 2013 deficient-perfect

Evidence: Chen's main theorem classifies the odd exactly-two two-prime case; later work classifies an odd exactly-three slice; Tang--Ren--Li give the \(k=1\) predecessor.

Reasoning: These are neighboring fixed-\(k\) results and do not dominate the arbitrary-\(k\) even classification.
### exact_database_or_table

Searches: OEIS A331627; OEIS A331628; OEIS A331629; Resultary exact theorem search

Evidence: The sequence resources record examples and fixed-\(k\) references, not the binary prime-interval theorem.

Reasoning: Example tables cannot imply the quantified uniqueness and all-\(b\) classification.
### claim_vs_prior_implication

Searches: Chen 2019 main theorem; Tang--Ren--Li \(k=1\) classification; assigned base-\(p\) digit proof

Evidence: The predecessor theorems cover special fixed-\(k\) cases only.

Reasoning: The base-\(p\) digit uniqueness argument supplies a new all-\(k\) structural implication not mechanically present in those special cases.

## Scientific value — PASS

PASS. This is a natural complete classification across every exponent pair and every \(k\) in a standard divisor-sum family. It unifies the known \(k=1\) even slice, determines all even two-prime cases at once, proves uniqueness of the deficient-divisor set, and yields explicit low-\(k\) corollaries.

## Source inspections

- **On exactly k-deficient-perfect numbers** — https://math.colgate.edu/~integers/t37/t37.pdf. Material read: Primary PDF abstract and main theorem pages defining the problem and classifying the odd exactly-two two-prime cases. Assessment: CLOSEST_FIXED_K_PRIOR_NOT_EVEN_ARBITRARY_K. Evidence: The theorem concerns odd exactly two-deficient-perfect integers with two distinct prime divisors.
- **On Exactly 3-Deficient-Perfect Numbers** — https://doi.org/10.1080/00150517.2021.12427539. Material read: Primary bibliographic and abstract-level statement identifying the odd exactly-three result. Assessment: NEIGHBORING_ODD_FIXED_K_RESULT. Evidence: It does not state an arbitrary-\(k\) classification for even \(2^a p^b\).

## Limitations and residual risks

The classification is for even integers with exactly two distinct prime factors. It does not classify odd cases or support size at least three, and it does not settle infinitude for a prescribed fixed value of \(k\).

- Poorly indexed divisor-partition literature could contain the same even two-prime classification under different terminology; no such theorem was located.

## Disposition

**passed**
