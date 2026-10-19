# Review of the endomorphism and retraction classification

## Correctness — PASS

Distinct basis elements have zero product, and bijectivity of the square-successor basis forces one nonzero entry per target row. Multiplicativity along each cycle forces a source cycle, a phase and a nonzero scalar whose `(2**ell-1)`-st power equals one. Counting these gives `(1+r*h)**r`, `h=ell*gcd(q-1,2**ell-1)`. Composition-idempotence precisely reduces nonzero arrows to identity-labelled roots; choosing `k` roots produces `comb(r,k)*(1+k*h)**(r-k)` maps of rank `k*ell`. Each step is proved without characteristic restrictions. Actual GF(2), GF(3), GF(4) exhaustive enumerations include an independent full-matrix test. The finite checks do not themselves establish the general theorem.

## Originality — PASS within compared coverage

Narkuziyev's permutation-cycle decomposition and element idempotents are distinguished from composition-idempotent algebra endomorphisms. Sriwongsa–Zou's full inspected automorphism-group analysis and Wei–Zou's full inspected isomorphism-class enumeration concern invertible maps and parameter orbits, respectively, not the noninvertible direct-sum endomorphism semigroup or its rank-refined retractions. Focused published-literature and published-finding corpus searches returned related but not covering claims, including prior cycle classification and a separate general wreath-product relative-rank result. Residual risk is an equivalent theorem in unindexed transformation-monoid literature or a generalization not identified here; absence from a search is not a uniqueness certificate.

## Value — PASS

The family is the natural repeated-simple-factor boundary of permutation evolution algebras. The structural monoid normal form classifies every homomorphism, and its exact rank spectrum determines all split retract images uniformly in dimension and finite-field characteristic. The nontrivial scalar-resonance factor `gcd(q-1,2**ell-1)` separates fields with equal characteristic but distinct available roots; for example two length-two cycles have 14 nonzero proper-rank retractions over GF(4), versus 6 over GF(2) or GF(3). This goes beyond the known single-cycle automorphism order and classification of idempotent algebra *elements*.

## Limitations and literature

No extension to mixed-length or arbitrary weighted cycles is asserted. Narkuziyev (arXiv:1803.11415), Sriwongsa–Zou (arXiv:2202.01333) and Wei–Zou (arXiv:2310.12368) are the closest object-level sources checked. The 2018 source was available only in public excerpts and a publisher abstract, not an inspectable full PDF during this comparison; the 2022 and 2023 PDFs were inspected directly. Broader unindexed literature remains a novelty risk.

Self-review: passed. Independent audit: not yet performed.
