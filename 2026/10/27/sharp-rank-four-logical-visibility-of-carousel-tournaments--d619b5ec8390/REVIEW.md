# Review of the rank-four carousel tournament theorem

## Correctness — PASS

The antipodal representation preserves the original directed edges; each played vertex contributes a paired original/gap mark. The inductive paired-interval strategy handles equality, orientation and alternating site parity with the sharp threshold \(T_r=2^{r+1}-2\). It yields the uniform infinite cutoff without extrapolating from finite computation. The bundled `verify_carousel.py` constructs exact quantifier-rank-four Hintikka types for all odd orders through \(19\), giving distinct representatives at \(1,3,5,7,9,11,13,15\) and equal types for \(15,17,19\). The infinite tail is proved separately.

## Originality — PASS

Coregliano (arXiv:1503.04124) defines the family and studies limit densities; Goodall–Nešetřil–Ossona de Mendez (2015) prove strongly polynomial homomorphism counts for the same sequence; Pikhurko–Verbitsky (arXiv:1003.4865) review bounded-rank EF methods. published-finding corpus searches under cyclic/carousel/locally transitive/antipodal aliases located no equal or stronger exact rank-four classification. Logical depth results for directed successor paths and Boolean algebras do not imply the assertion in the half-circle tournament language. A possible unknown general theorem on antipodal circular orders remains a literature risk.

## Value — PASS

The exact eight-theory classification makes the last visible order \(13\) and stable tail beginning at \(15\) mathematically explicit for a naturally canonical tournament family. The proof provides a general bounded-rank game strategy for this family, linking its geometric rotational symmetry with finite model-theoretic expressibility. Neither a routine rewrite of homomorphism polynomiality nor a finite-only enumeration yields this infinite theorem.

## Limitations and close comparisons

The rank-four lower boundary relies on a small exact exhaustive computation with supplied source, while the infinitely many tail cases are covered by a separate argument. The general \(q\) assertion is only an upper bound. No proof-assistant or independent human audit has been performed; searches are not exhaustive of every primary source. Related exact thresholds for finite directed paths concern a different relation. The reference descriptions and residual risks are itemized in AUDIT.json.

Self-review: passed. Independent audit: not yet performed.
