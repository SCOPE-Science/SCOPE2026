# Review: idempotent centralizers in the finite directed-path monoid

## Correctness — PASS

The proof directly analyzes the commutation equation with an interval clamp: its restriction to the fixed interval is a binary-step path with prescribed endpoints, and both tails are either unconstrained or forced constant according to those endpoints. The resulting endpoint-weighted binomial sum gives the centralizer formula with correct degenerate boundaries (singleton clamp and identity). Summing over all interval positions gives the total commuting-pair count, and a direct interval-intersection argument yields all maximal idempotent semilattices and the clique polynomial. The standalone verifier independently enumerates all monoid maps and all idempotents through size ten and all cliques through size five. The unrestricted mathematical proof, not these finite tests, establishes the claim. Residual correctness risk: an undetected error in the symbolic finite-sum simplification, although every tested value agrees.

## Originality — PASS relative to inspected evidence

The 2021 Fernandes–Paulista primary paper, arXiv:2112.13427, establishes the monoid characterization and its idempotent census, not centralizers. Fernandes (2024), DOI 10.1007/s00233-024-10466-2, gives presentations of **the same monoid** under another name, again not the individual centralizer counts, idempotent commuting clique polynomial or ordered commuting-pair enumeration. The comparison therefore accounts for the strongest immediate alias. A 2012 symmetric inverse semigroup commuting-graph paper and a 2025 completely simple semigroup graph paper concern different monoids and do not directly imply these precise counts. Targeted literature searches for interval-image idempotent centralizers and directed-path commuting graph formulas, plus searches against accessible mathematical research records and earlier claim collections, found no dominating statement. Search failure does not prove priority. A detailed 2025 thesis on semigroup commuting graphs and any general chain-transformation centralizer classification remain residual priority risks.

## Mathematical value — PASS

The exact centralizer profile is a natural intrinsic statistic of an infinite family already studied by monoid presentations, rank and regularity. It yields a closed aggregate commuting-pair count and the quadratic decay \(32/n^2\) of the mixed idempotent commutativity probability. The idempotent-commuting graph is completely classified, including **every** maximal commuting semilattice and **all** clique coefficients, not just a small special case. The result has a motivated structural role in understanding commuting substructures within path endomorphism monoids, beyond the previously known idempotent count.

## Literature and limits

Closest source: Fernandes–Paulista, arXiv:2112.13427 (2021), Proposition 1.5 and Corollary 1.9; Fernandes, *Semigroup Forum* 109 (2024), Sections 1–4. General commuting-graph context: Araújo–Bentz–Konieczny, arXiv:1205.1664, and Paulista, *Communications in Algebra* 53 (2025). Only the idempotent part of the commuting relation is classified; this is not a complete full-monoid commuting graph. Independent mathematical audit remains unperformed.

Self-review: passed. Independent audit: not yet performed.
