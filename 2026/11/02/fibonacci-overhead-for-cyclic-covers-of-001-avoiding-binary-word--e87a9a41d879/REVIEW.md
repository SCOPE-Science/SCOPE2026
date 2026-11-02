# Scientific review

## Correctness — PASS

The result is an all-order theorem, not an extrapolation from finite data. The full de Bruijn graph makes the allowed-cover boundary explicit: forbidden windows may occur in a covering cycle. The required-edge graph has positive imbalance exactly at the \(F_{n-1}\) no-`00` vertices starting in `01`, and an equal total negative imbalance at vertices ending in `00`. Every extra source-to-sink path needs at least \(n-2\) edges because no overlap of two or more bits is possible. Paths of exactly that length exist by the shared final/initial zero, and the augmented graph is Eulerian and connected. The proof covers every integer \(n\ge3\). The Python verifier reconstructs matching finite examples through order eighteen and exhaustively excludes shorter circular words at the two smallest nontrivial orders. Its finite tests support but do not replace the proof.

## Originality — PASS, with historical-priority qualification

The closest fully inspected source is Moreno–Matamala, *Minimum de Bruijn Sequence in a Language with Forbidden Substrings* (arXiv:0711.1695v1). Its Sections 2–3 concern exact-once Eulerian cycles of an irreducible subshift's periodic language. The present finite-factor target includes transient `001`-avoiding words whose periodic repetitions are inadmissible; thus the required subgraph is unbalanced, and those Eulerian results do not yield this shortest *superset* covering length. The second primary source, Bernardini et al. (CPM 2022), studies shortest strings with an **exact** prescribed set of factors and general directed-postman algorithms; it neither provides nor implies the specific Fibonacci transfer count under unrestricted extra factors. Bibliographic searches for aliases, forbidden-pattern rotations and the proposed integer formula did not reveal a dominating theorem. The historical 2004 conference version of the first source and unindexed tables remain residual priority risks.

The nearest recovered related exact results concern covering all words avoiding `000` at finitely many orders and covering words avoiding `00` at all orders. The former forbids a constant three-bit pattern, while `001` lies in a different binary reversal/complement orbit. The latter targets an entirely different allowed set. Neither statement implies the theorem here. This comparison concerns mathematical statements and reductions, not just titles.

## Value — PASS

This solves a natural, infinite family of shortest cyclic superstring instances with a simple forbidden factor. The result is stronger than an upper-bound construction or a finite numeric table: it determines the exact optimum for every order and gives the sharp reason for the overhead. Its unusual \(\Theta(n)\) overhead relative to the number of admissible windows separates finite-factor coverage from ordinary restricted de Bruijn cycles and is useful as a closed-form benchmark for constrained-sequence assembly and postman augmentations. The chosen object and invariant are intrinsic, not an arbitrary parameter slice.

## Risks and limitations

The source-domain distinction (all finite factors versus periodically extendible factors) is essential. No statement is made about a cover that itself avoids `001`, about minimal linear rather than circular covers, or about other three-bit forbidden-pattern orbits. A 2020 paper on exact-once universal cycles under removal of a small number of words was available by abstract but not fully inspected; its stated parameter range differs, and it is not treated as exclusionary evidence. Historical publication indexing and the earlier conference version may contain uncatalogued special cases. No independent audit or historical-priority certification has been performed.

Self-review: passed. Independent audit: not yet performed.
