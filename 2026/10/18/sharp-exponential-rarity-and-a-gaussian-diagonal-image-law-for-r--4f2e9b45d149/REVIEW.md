# Self-review

## Correctness — PASS

Under the explicitly fixed uniform binary-table model, the map from binary operations to flip-equivariant square transformations is a bijective monoid description. The existence of an equivariant inner inverse is proved equivalent to fixed outputs admitting fixed preimages. Conditioning on the independent diagonal image gives the exact occupancy law, agreeing with Baiduk–Kozerenko's known count. The new limit uses a correctly normalized zero-truncated-Poisson coefficient representation, uniform interior span-one local CLT, expansion of the off-diagonal factor through order one, a uniquely strictly concave saddle point, uniform endpoint coefficient upper bounds, and the discrete Laplace method. The leading constant retains the full \(\exp((1-x_*^2)/4)\) correction. The packaged finite verifier checks the exact count, directly checks the existence of monoid inner inverses at order two, and numerically checks both the sharp probability and conditional variance through \(n=640\). The infinite theorem relies on the proof, not these checks.

## Originality — PASS, with residual risks

The nearest direct source is Baiduk–Kozerenko, arXiv:2607.13746v1, Proposition 24 and Theorem 25: it supplies the regularity criterion and exact formula, so **neither is claimed as new**. Full-text inspection of its regularity/counting material identifies no sharp exponential equivalent or conditional Gaussian diagonal-image theorem. Rafieipour's thesis (regularity section) discusses structural questions and low orders; López-Permouth's 2026 full-text article treats idempotents rather than regular elements. Targeted published-web and published-finding corpus claim/alias searches found no formula matching the constants or conditional law; these negative search results are not a uniqueness guarantee. An unindexed saddle-point refinement or an implied result in a related equivariant-transformation literature remains possible.

## Value — PASS

The exact regularity enumeration counts an enormous finite monoid but leaves open its global random-element behavior. The theorem determines the exponential rarity *and leading coefficient*, and a nontrivial conditional Gaussian law; the conditioning pushes the typical diagonal-image fraction from \(1-e^{-1}\) to approximately \(0.680016\). This is a natural probabilistic algebra invariant with a structural interpretation, not a routine re-expression of the exact sum. The results resolve the dominant-diagonal-support mechanism quantitatively while explicitly preserving credit for earlier exact counts.

## Scope and residual limitations

The proof holds for a uniform labeled magma monoid, not for random associative semigroups or nonuniform binary tables. The Gaussian law is conditional on regularity, and no independent validation or certification is claimed. Finite code is corroboration, not an infinite proof. Bibliographic uncertainty remains for unindexed or inaccessible equivalent results.

Self-review: passed. Independent audit: not yet performed.
