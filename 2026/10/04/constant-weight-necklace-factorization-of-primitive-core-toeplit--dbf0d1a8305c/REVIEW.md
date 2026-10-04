# Review of Constant-weight necklace factorization of primitive-core Toeplitz recurrence polynomials

## Correctness
**PASS.** The proof reconstructs the canonical roots from arXiv:2609.27268, uses primitivity to make all subset-product exponents distinct modulo \(Q^d-1\), and identifies Frobenius with cyclic rotation. The necklace count is standard Möbius inversion on the exact period. The supplied checker confirms orbit counts and several exact finite-field factorizations, while the arbitrary-parameter theorem is proved symbolically rather than inferred from finite experiments.

## Originality
**PASS.** The closest 2026 Toeplitz sources define the exterior-degree root-product/compound recurrence but do not inspect primitive finite-field cores or Frobenius factorization. General finite-field sources explain cyclotomic cosets and necklaces, but the inspected material does not connect them to this canonical Toeplitz recurrence family or state the complete factor-degree law and irreducibility boundary. Semantic-database and targeted web searches for the equivalent exterior-power, compound-matrix, cyclotomic-coset, and constant-weight-necklace formulations found no stronger covering statement. Residual risk remains that an equivalent compound-matrix result exists under older terminology.

## Value
**PASS.** The theorem gives an exact arithmetic decomposition of a newly introduced recurrence profile: the factor degrees and counts are completely determined by constant-weight necklace periods, and primitive input is shown not to imply irreducibility except at the edge exterior degrees. This provides a natural finite-field structural boundary relevant to recurrence decomposition and symbolic computation.

## Closest literature and limitations
Alekseyev--Khomovsky, arXiv:2609.27268, supplies the canonical polynomial and the crucial canonical-versus-minimal distinction. Their companion arXiv:2609.13674 supplies the underlying compound recurrence picture. Rebenich's 2016 finite-field dissertation supplies background on Frobenius cyclotomic cosets and necklaces. The result here assumes a primitive core and does not classify specialized scalar minimal recurrences or nonprimitive irreducible cores.

Same-model review: passed. Independent audit: not yet performed.
