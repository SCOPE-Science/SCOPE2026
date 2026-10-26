# Scientific review: exact first collisions in the period-doubling word

## Correctness — PASS

The exact substitution identities \(p_{2a}=0\), \(p_{2a+1}=1-p_a\) imply that no length-four all-zero factor exists and that factor sets originating at opposite starting parities are disjoint for length at least four. Each same-parity factor is an injective encoding of a shorter source factor. Comparing earliest repeated start positions therefore proves \(I(n)=2I(\lfloor n/2\rfloor)\) for all \(n\ge4\). The three direct base cases give both the closed formula and the unique previous collision position. The proof covers every positive integer length; the finite reproduction is corroboration only.

## Originality — PASS against inspected literature, with residual risk

Nicholson and Rampersad, arXiv:1507.08206 (2015), define this complexity measure and determine it for Thue–Morse, Fibonacci and Tribonacci, not the period-doubling fixed point. OEIS A366462 and A367184 supply the maximal **anywhere** unique-factor window and the first position attaining it; for dyadic lengths their zero-position observation already implies the dyadic slice of the present first-collision count. They do not supply the complete all-length initial profile or the explicit predecessor of the first collision. Shallit's slides on grouped factors give an existence criterion for complete distinct-factor windows somewhere in the word, not the first collision of the origin-anchored sequence. Searches of mathematical research records for period-doubling initial non-repetitive complexity, first-collision positions, desubstitution recurrence and grouped-factor equivalences found no stronger covering claim. Undiscovered or unpublished computations remain a historical-priority risk.

## Mathematical value — PASS

Initial non-repetitive complexity is a named, independently motivated orbit-complexity invariant. A complete evaluation for the canonical period-doubling word fills a natural missing example alongside the 2015 computations for other substitution words. The result is not a selected finite parameter: it determines every length and also which earlier substring causes the first repetition. Its two binary-leading-digit regimes and sharp lower/upper normalized accumulation values give interpretable structural information about scanning prefixes of a self-similar word.

## Boundaries

No assertion is made about arbitrary shifts, other substitutions, all later collisions, or priority beyond the inspected sources. The derivation uses the exact one-sided fixed point and zero-based positions. Finite checks are not substituted for the proof.

Self-review: passed. Independent audit: not yet performed.
