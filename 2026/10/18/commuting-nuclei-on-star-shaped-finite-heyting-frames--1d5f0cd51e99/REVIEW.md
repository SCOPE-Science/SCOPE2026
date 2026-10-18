# Review of the star-frame nucleus commutation classification

## Correctness

**PASS.** The proof first reconstructs all nuclei on the \((2^n+1)\)-element upset Heyting algebra from their leafwise outputs and a principal-filter test for whether the root enters the image. It derives a unique parameter pair \((a,A)\), including the boundary cases \(A=\varnothing\) and \(A=L\). Direct composition on proper upsets proves the mixed-flag subset-inclusion condition. Maximality is checked in both directions, and a per-leaf forbidden-pattern count proves the entire ordered-tuple formula, including \(k=0\). No probabilistic convergence stronger than the exact pair formula is claimed.

The standalone `verify.py` obtains the same commutation predicate by pointwise evaluation of subset-generated nuclei, independently confirms all nucleus axioms and their small-carrier exhaustiveness, enumerates maximal cliques, and verifies small ordered tuples. The analytic proof, rather than finite tests, covers every \(n\ge1\) and \(k\ge0\).

## Originality

**PASS on the inspected evidence, with nonzero literature risk.** Lindenhovius's Artinian-poset theorem already supplies subset parameterization of all nuclei, and Ochs's 2021 note supplies an explicit inverse; neither result is claimed as new. The contribution is the pairwise composition criterion specifically for rooted stars, the complete maximal commuting-family classification, the arbitrary-length tuple enumerator, and the nonzero asymptotic limiting commuting probability. The closest known chain and diamond modality classifications concern non-isomorphic carriers or a different class of operators; neither implies the present non-chain Heyting-star spectrum through its stated theorem.

Semantic searches of published mathematical results included exact objects, aliases, and pair-count formulas. They did not expose a covering statement. The inspected primary sources address individual nuclei, congruences, and Grothendieck topologies rather than mutual commutation spectra. A more general, uncatalogued result in semigroup theory, locale theory, or categorical topology could still subsume this calculation; search silence does not certify priority.

## Mathematical value

**PASS.** Independent nuclei encode alternative sublocale/closure semantics; order-independent composition is therefore a natural compatibility condition. On an infinite family of genuinely non-chain finite Heyting algebras, the theorem gives not merely a count but a complete classification of maximal compatible systems and all finite commuting-collection statistics. The limiting commuting probability \(1/2\) is a structural consequence of the root flag, rather than an arbitrary finite numerical slice. The maximal family-size profile identifies the extrema of compatible modal collections.

## Limitations

The classification is restricted to finite rooted stars with labelled leaves and meet-preserving idempotent operators. It does not extend to all finite posets, arbitrary closure operators, or infinite frames. Earlier subset/nucleus duality is credited. Finite verifications are independent computations within this package, not proofs of the infinite parameter claims. Remaining originality risk concerns synonymous results outside indexed literature and uninspected portions of very long background treatments.

Self-review: passed. Independent audit: not yet performed.
