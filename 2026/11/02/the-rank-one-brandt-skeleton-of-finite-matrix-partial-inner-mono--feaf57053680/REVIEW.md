# Scientific review: rank-one Brandt skeleton

## Correctness — PASS

For each matrix pair \(g,h\), the domain is exactly \(\mathcal R(\ker(gh-I),\operatorname{im}(gh-I))\). The crucial nonscalar lemma is that every composition still has rectangular domain and range and is induced by invertible maps on its two tensor factors; preimages of intersections of rectangles retain rectangular form. This makes the \(q\)-element domains precisely the nonzero rank-one matrix lines. The idempotent and square-zero types are mutually exclusive and exhaustive, both are preserved by semigroup partial isomorphisms, and explicit choices of \(g,h\) realize every permitted inter-line isomorphism. The Brandt multiplication follows by matching source and target lines, and the ideal classification follows by restricting every nonzero rectangle to a rank-one line. A rank-two projection exhibits properness in every \(n\ge3\). Direct enumeration over \(\mathbb F_2\) and \(\mathbb F_3\) supports, but is not used to prove, the universal result.

## Originality — PASS, qualified

The closest primary source, Araújo et al., arXiv:2605.00041v1, Definition 3.8 and Problem 7.9, defines the inverse monoid and explicitly leaves matrix endomorphism monoids to future work. Its accessible full text treats transformation monoids, completely simple semigroups and certain equivariant endomorphism monoids; it does not state the two rank-one Brandt ideals or their counts. Prior two-by-two matrix enumeration covers only \(n=2\), whereas the present statement requires a uniform all-higher-dimensional rectangular-composition proof. Targeted searches using line domains, matrix partial inner maps, and Brandt matrix-unit language found no equivalent or dominating theorem. Since the 2026 article was originally part of the 2023 precursor arXiv:2301.04252, the underlying construction and motivation are **not** claimed as first published in 2026. A complete historical search of older partial automorphism monoid theory is not established; this remains a priority risk.

## Value — PASS

The full matrix-endomorphism partial-inner monoid is the subject of the concrete Problem 7.9 of the motivating paper. Even without classifying its higher-rank elements, identifying **all** its minimal nonzero ideals, their local groups, their matrix-unit indexing sets and the exact size of the canonical submonoid gives a structurally complete first layer in every matrix dimension. The idempotent and nilpotent layers behave differently (trivial versus multiplicative-field local groups); their comparison is an intrinsic feature of the monoid, rather than an arbitrary numerical slice. The properness witness explains why this is not a full solution to the stated open problem.

## Closest sources and limits

- Araújo et al., *The Inverse Monoid of Partial Inner Automorphisms of a Semigroup*, arXiv:2605.00041v1, §§3, 7, especially Problem 7.9 (primary full text inspected).
- Araújo et al., *Conjugacy in abstract semigroups, transformation and diagram monoids, and conjugacy growth*, arXiv:2301.04252 (earlier precursor, acknowledged; no novel-framework claim).
- An existing exact \(2\)-by-\(2\) calculation covers that boundary and is excluded from the novelty claim.

The result does not determine all of \(\operatorname{Inn}(M_n(\mathbb F_q))\) for \(n\ge3\). The finite checker directly tests single-generator line maps at three parameter pairs, not the infinite family or every composition. No external independent audit or priority certification is asserted.

Self-review: passed. Independent audit: not yet performed.
