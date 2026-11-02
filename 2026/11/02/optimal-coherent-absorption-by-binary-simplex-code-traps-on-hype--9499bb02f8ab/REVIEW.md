# Scientific review: optimal coherent absorption by binary simplex-code traps

## Correctness — PASS

The proof identifies energy-shell restriction ranks exactly with subset-XOR syndromes, then establishes a uniform upper bound using only the weight-zero, weight-one and weight-two shells. For the simplex code, the constant off-diagonal Gram kernel and its two eigenvalues are derived from the uniform pairwise distance. A binomial-ratio argument verifies strictly positive eigenvalues at all interior weights for \(m\ge3\). The direct-sum dark-mode characterization uses positivity of all trap rates. These are analytical steps for the whole family, not extrapolations from finite enumeration. The independent executable tests include full small-case matrix and Krylov rank calculations; see `VERIFICATION.md`.

## Originality — PASS on inspected evidence; historical priority remains provisional

Equivalences as binary subset-sum images, Fourier restriction/observability ranks, and non-Hermitian quantum-walk dark dimensions were compared. Moore–Russell's hypercube walks, Krovi–Brun's dark hitting-time modes, Varbanov–Krovi–Brun's continuous hitting times, and Krapivsky–Luck–Mallick's trap survival establish the surrounding formalism but do not imply the sharp bound for arbitrary affine absorber sets in the material examined. Published records on Fourier restriction to Hamming shells, a systematic simplex-LCD code, and a one-corner Cartesian walk have different mathematical objects. An earlier specialist coding/controllability formulation could conceivably subsume the claim, so this assessment is evidence-limited rather than a global assertion of novelty.

## Mathematical value — PASS

For a fixed trap budget of \(2^m\) points chosen as a natural affine code, the sharp all-placement bound is a meaningful optimization of eventual coherent absorption, with an explicit maximizer and energy-shell accessibility profile. It quantifies how code geometry interacts with extremely degenerate hypercube energy levels; the objective concerns an infinite natural physical family rather than an arbitrary finite slice. Maximizing capture does not establish fastest decay, and a general unrestricted trap optimum is not claimed.

## Scientific boundaries

Only binary hypercubes with uniform hopping, affine dimension-\(m\) traps, positive sink rates, and one-particle dynamics are covered. The source comparison and this review do not constitute an independent scientific audit.

Self-review: passed. Independent audit: not yet performed.
