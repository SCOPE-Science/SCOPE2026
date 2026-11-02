# Review of the generator and Poisson-limit theorem

## Correctness — PASS

The statement restricts to full powerset tense algebras under a fixed finite permutation, with ordered generators and a fixed cycle length in the limit. The proof explicitly establishes that full generation is equivalent to pairwise distinct two-sided colored itineraries; this is equivalent to each cycle's word being primitive and primitive necklaces on equal-length cycles being distinct. Möbius inversion then gives the exact falling-factorial product, including one-cycles, zero generators and insufficient necklace inventory. For the limit, every even-length cycle has nonprimitivity probability asymptotic to the reciprocal square root of the alphabet-word count, while odd lengths have smaller probability. Conditioned on primitivity, every necklace has exactly the same multiplicity; factorial moments for the birthday pairs give the second Poisson law and tightness of the number of discarded cycles yields asymptotic independence. This proof does not rely on finite computation. The attached checker confirms direct algebraic closure and the formula in 339 cases encompassing 10,999 assignments; it reports `ALL_CHECKS_OK`. The assumptions, quantifiers and limiting regime are explicitly specified.

## Originality — PASS within inspected sources

The full 2026 motivating paper develops the relevant tense Boolean algebra axioms and a completeness theorem but does not study algebra generation or cyclic coloring. The 2019 distinguishing-coloring paper is conceptually much closer to the finite normal form, and the 2019 oriented-graph paper discusses symmetry-breaking parameters: consequently the primitive-necklace and distinguishing-coloring ingredients are **not claimed as original**. OEIS A074650 records the exact primitive-necklace count. The assessed new mathematical statement is the **joint two-obstruction Poisson limit with an even-cycle correction and its generator-probability threshold**. Searches of mathematical research records, the relevant primary literature and exact sequence data did not identify this assertion or a strictly stronger theorem implying it. Important remaining risk: a more general Poisson theorem for distinguishing colorings of disjoint directed cycles or standard occupancy processes could already imply this consequence without tense-algebra terminology. This is a self-review, evidence-limited historical assessment, not independent priority verification.

## Mathematical value — PASS

The generator rank is a natural finite-algebraic invariant, not an arbitrarily selected statistic. The exact count yields the complete generating-tuple spectrum for a structurally motivated tense-algebra subclass, while the limiting theorem identifies the **two qualitatively different failure mechanisms** and a parity-dependent critical-window law. It also proves a logarithmic factor-two separation between the least possible generators and the number needed for success with high probability. This provides a precise typical-versus-existential comparison for the modal algebraic semantics, rather than only a small finite table.

## Limits and overlap caution

The result concerns permutation tense algebras, not arbitrary tense algebras, and treats fixed common orbit length in the random limit. The exact necklace factors and basic birthday asymptotics are classical inputs; the article does not assert novelty of these separately. A full third-party literature audit could discover a dominating general result. The computational checker is finite and cannot certify the Poisson theorem.

Self-review: passed. Independent audit: not yet performed.
