# Self-review

## Correctness — PASS

The domain and quantifiers are exact: integer \(q\ge2\); nonnegative weights on \(\Sigma^5\); every two-letter prefix has mass one; every **distinct** three-letter subsequence has capacity one. Necessity follows by multiplying individual-output inequalities by a nonnegative 5-type weight and checking all \(52\) equality patterns, with exact minima \(14\) or \(19\). The symbolic capacity comparison forces \(q\ge7\). Sufficiency uses an explicit three-orbit mixture over the last three symbols, whose prefix masses are one and whose five orbit loads are exactly \((1,1,4/5,1,5/(q-2))\). The script reconstructs the complete finite lemma and exact q=7,8,9 incidences. Neither numerical LP output nor finite samples are used as the general proof.

## Originality — PASS, residual priority risk

The closest motivating preprint (Grishin--Zabokritskiy, arXiv:2609.38259, full accessible HTML sections 1, 2, 8, 10 and 11 inspected) gives systematic constructions for sufficiently large alphabets and a **different adjacent-burst** fractional-cover converse. Its statements do not imply an exact length-five arbitrary-two-deletion fractional threshold at seven. An earlier weighted-shadow calculation already proves the necessary seven-letter bound for integral codes: this review does not count that converse as new. The exact **feasible fractional point at seven and above**, including all output-type loads, was not covered by the accessible comparisons. Related q-ary multi-deletion asymptotic coding constructions and exact one-deletion finite tables change either the block-length regime or deletion radius. Semantically targeted mathematical-record and web searches found no exact equivalent. Risks: an unindexed fractional orbit-LP computation or unpublished table could predate the point; priority is not independently certified.

## Value — PASS

The parameter is mathematically motivated by the first full-symbol systematic two-deletion case: two information symbols and the conjecturally minimal three exposed suffix symbols. The result exactly settles a natural complete fractional relaxation at **all** alphabet sizes, rather than recomputing an isolated optimum. More importantly, it demonstrates sharply that single-output deletion-shadow capacity inequalities cannot push the known lower alphabet bound beyond seven; work on the unresolved integral boundary must use stronger collision/integrality information. This distinguishes a genuine methodological limitation from a claim of constructing a real code.

## Limitations and closest literature

No length-five systematic encoder at \(q=7\) is claimed. Full arbitrary-two-deletion fractional packing differs from both genuine integer code existence and adjacent-burst deletion models. The 2026 primary work and a 2023 q-ary long-code paper were inspected for implication; incomplete indexing leaves residual priority uncertainty. Only the present new claim is assessed.

Self-review: passed. Independent audit: not yet performed.
