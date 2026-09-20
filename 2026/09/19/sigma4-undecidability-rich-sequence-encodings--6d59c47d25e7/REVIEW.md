# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

The proof was checked against the explicit counter-machine reduction and rank-predicate definitions in Karimov--Nieuwveld--Ouaknine, arXiv:2609.20415. The source halting formula consists of existential sequence parameters, initial/final endpoint formulas, and a universally quantified local transition formula. The source definitions show that the rank-zero, equality, and successor conditions are universal at the first level, whereas fixed positive rank and exact-one increment conditions admit existential-witness/universal-exclusion definitions.

The only syntactic obstacle in the source presentation is permission to use negated fixed-rank predicates inside the transition formula. It is not semantically necessary for the two-counter-machine model used there: counters are positive, so the branch test `counter > 1` is equivalent to the existence of two distinct rank witnesses. Program-state dispatch can be written as a finite positive disjunction over instruction labels. This yields a Sigma_2 step relation. The endpoint formulas are then Sigma_3, the universal local condition is Pi_3, and the outer existential sequence parameters yield an effective Sigma_4 halting sentence.

The same classification was checked against the source's Section 4 LRS-function definitions. For the selected-permutation variant, the stated extension is deliberately restricted to quantifier-free selectors so that representative membership does not add hidden alternations.

A compact syntactic audit is included in `artifacts/prefix_audit.py`; its output is in `artifacts/prefix_audit.txt`. The script is a sanity check of the alternation bookkeeping, not a substitute for the semantic proof.

## Originality

The motivating preprint was inspected at its abstract/introduction, counter-machine definition, Theorem 2 proof, arbitrary-permutation construction, Section 4 LRS construction, and selected-permutation/least-prime-factor construction. It states undecidability of the full first-order theories in the new examples. Its introduction separately records the earlier Hieronymi--Schulz three-block result for two power predicates, but the inspected text does not state a finite quantifier-block bound for the new arbitrary-permutation, special-function, or LRS-function examples. Full-text searches for `quantifier alternation` returned no match; `fragment` occurrences concern background results rather than such a refinement.

Targeted web searches combined Euler totient, sum of divisors, least prime factor, linear recurrences, first-order theory, quantifier fragments, and Sigma-level terminology. They found the motivating preprint and background literature but no prior statement matching the four-block refinement. SCOPE archive searches by the motivating title, Euler totient/first-order terminology, and arbitrary-permutation/quantifier terminology returned no overlap.

The claim is therefore made only to the best of our knowledge. Priority risk is elevated because arXiv:2609.20415 is extremely recent and the quantifier bookkeeping is a natural refinement that could be observed independently or added in a subsequent revision.

## Value

The source paper introduces several first undecidability results for natural one-function arithmetic structures. Localising those reductions to the fixed prefix ∃*∀*∃*∀* is materially stronger than full first-order undecidability: it bounds the logical alternation needed for the pathology and enables sharper future questions about the Sigma_3/Sigma_4 boundary. The result applies uniformly to the totient and sum-of-divisors examples and to the source's two-dominant-root LRS function construction, with a quantifier-free-selector extension that includes least prime factor.

## Limitations

No optimality is claimed. The Sigma_3 fragment may also be undecidable by another encoding. The selected-permutation extension requires a quantifier-free selector. The result does not address the source paper's predicate-valued LRS structure with addition, whose particular implementation has a different syntactic profile, nor its square-free-number construction. Independent audit and independent validation have not been performed.
