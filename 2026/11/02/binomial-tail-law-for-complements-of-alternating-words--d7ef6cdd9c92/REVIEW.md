# Review of the alternating-word complement classification

## Correctness (C): PASS

The statement quantifies over all nonnegative \(m,k\), distinct alphabet symbols, and distinct complement words. The proof separates necessity (balanced even residual prefixes and parity changes of the deleted alternating subsequence) from sufficiency (an explicit segment for each maximal reversed-block run), then counts runs through their boundaries. This establishes the full language equality, the exact minimum deletion count, and both binomial sums without extrapolation. The standalone checker compares exact sets by two independently formulated enumerators for 78 parameter pairs; its finite success corroborates but does not replace the proof.

## Originality (O): PASS, subject to publication-priority uncertainty

The 2026 foundational paper of Adamson, Fleischmann and Huch gives general algorithms and singleton/shuffle structure but leaves closed formulas in specified natural families open (Conclusion). Its Sections 3 and 4 were inspected, including the singleton perfect-shuffle Theorem 4.5. No formula or characterization by reversed-block runs for alternating source and deleted subsequence was found. Semantic database searches for the same objects, aliases, parameters, run characterization and binomial tail returned related deletion/shuffle results but not a statement implying this theorem. Recoverable prior claims include an alternating-word minimal-absent-subsequence result and shuffle variants, none of which imply the complement-language classification. This remains best-knowledge novelty, not proof of global uniqueness; an unindexed shuffle enumeration is plausible.

## Value (V): PASS

The primary source expressly identifies closed forms for special complement-scattered-factor sets as an unresolved direction. Alternating words are the canonical binary extremal test case, and the full two-parameter theorem gives not merely an isolated value but a structural normal form, a precise minimal deletion resource, a binomial-tail census, and a sharp phase boundary from full to incomplete residual coverage. This is nontrivial information not implicit in the raw embedding count (many embeddings share a residual).

## Limits

The theorem is not an optimal bound over arbitrary word pairs. No external independent mathematical audit or definitive priority certification has been performed.

Self-review: passed. Independent audit: not yet performed.
