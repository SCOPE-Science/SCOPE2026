# Self-review

## Correctness — PASS

The final claim is the exact formula for the minimum domination number of the Sierpiński product of \(C_n\) and \(C_{3k+1}\), for every \(n\ge3\) and \(k\ge1\). A layer-capacity argument gives a universal lower bound \(kn\). Equality induces a unique hole and forced three-step internal tiling in every layer; all connecting edges must point coherently toward the holes. The resulting necessary-and-sufficient closed-walk condition has an explicitly classified length spectrum. The proof separately constructs a set of size \(kn+1\) in every parameter range, resolving every exceptional case. The executable checks 522 parameter pairs and enumerates normalized connecting maps for five small pairs; these are supporting tests, not an infinite proof.

## Originality — PASS

The closest primary result is Henning–Klavžar–Kleszcz–Pilśniak, *The Sierpiński Domination Number*, arXiv:2309.15409v1 (2023), published in *Ars Mathematica Contemporanea* 24 (2024), #P3.06. Its cycle theorem supplies only \(\{kn,kn+1\}\) for second-factor order \(3k+1\), with the \(4\mid n\) tightness condition and isolated extra examples. The new exact table implies those cases but is not implied by them; it settles the remaining infinite parameter ranges. A search-index excerpt of an earlier submitted draft displays a purported stronger but superseded expression; it is contradicted by a directly checked \(n=7,k=3\) example with \(21\) dominating vertices where that expression predicts \(22\). The revised and journal texts use the two-value range. The full earlier draft could not be retrieved and is a specific residual access risk. The original graph-product paper arXiv:1904.04180 addresses structure rather than this domination parameter. Searches for equivalent formulations and later coverage found no matching theorem. The principal residual risk is relevant earlier work concealed by terminology, indexing or inaccessible texts; absence from search is not novelty proof. The four structured implication comparisons and genuine source inspections are recorded in AUDIT.json.

## Value — PASS

The work closes a published quantitative gap for a natural graph domination invariant on a two-parameter classical graph-product family. The value lies in a necessary-and-sufficient structural criterion and complete classification, not in isolated small computations or repackaging previously proved instances. It explains the short-cycle exceptions through zero-sum walk obstructions and supplies constructions throughout the infinite family.

## Limits and verification status

The minimization is over all connecting maps. No statement is made about the domination number for each fixed map, enumeration of minimizing maps, or different congruence classes of second-factor length. Finite verification does not replace the proof, and independent external review has not taken place.

Self-review: passed. Independent audit: not yet performed.
