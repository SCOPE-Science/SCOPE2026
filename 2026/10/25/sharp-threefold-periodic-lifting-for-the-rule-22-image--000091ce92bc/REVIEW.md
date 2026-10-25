# Scientific review: Rule 22 periodic lifting

## Correctness — PASS
The four-state labeled de Bruijn relation exactly encodes all local antecedents; a periodic image has an antecedent with spatial period dividing a multiple of its displayed period precisely when the corresponding relation power has a loop. The generated finite Boolean relation semigroup is exhaustively closed at 2375 elements, not truncated by output-word length. Every relation with a cycle has a return in one, two, or three steps; precisely the two powers of the one-symbol relation have first return in three steps. A separate finite-state flag excludes mixed words from these two relations. The all-one three-cycle and the `001` two-cycle give sharpness. `verify.py` independently checks all necessary exact integer assertions, including 2046 shorter cyclic words.

## Originality — PASS (best-knowledge, historical uncertainty)
Badii–Politi (1997) addresses Rule 22 spatial languages and entropy, not sharp periodic preimage periods. Gravner–Griffeath (2010) addresses finite-seed space-time dynamics. Mariot–Leporati (2015) gives periodic-preimage results for linear bipermutive CA, a hypothesis Rule 22 violates. Martínez et al. (2019) provides subset and de Bruijn methods without the specific uniform factor-three result or its sole exceptional output. Salo (2022) establishes general decidability and periodic lifting obstructions for related ECA but not this exact evaluated multiplier theorem. Accessible previous research claims and mathematical-record searches gave no equivalent or stronger explicit evaluated result. The semigroup method itself is classical and is not claimed as novel. An unindexed previous exact calculation remains possible.

## Mathematical value — PASS
Spatial period lifting is a natural question about surjectivity on finite cyclic quotients and obstructions to equivariant sections. The result is a complete, sharp classification of **all periods** for a classical nonlinear nonsurjective CA, not a finite-length census. It isolates two genuinely different nontrivial obstructions, proves a uniform preimage-period inflation bound, and identifies the unique family requiring tripling. This does not follow from image-language entropy or simply from Rule 22's local truth table without the finite-semigroup invariant.

## Limitations
The proof needs the supplied 2375-state finite exhaustive certificate. The earlier published subset machinery renders the problem algorithmically solvable in principle. Historical priority has not been independently certified. The complete set of outputs requiring doubling is not explicitly enumerated, and time-periodic dynamics are outside scope.

Self-review: passed. Independent audit: not yet performed.
