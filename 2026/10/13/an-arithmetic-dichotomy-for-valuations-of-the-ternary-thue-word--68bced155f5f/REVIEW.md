# Scientific review

## Correctness — PASS

The published 2014 Lemma 8 and proof of Theorem 2 give the *exact*, parity-resolved Parikh spectrum of each factor length of the ternary Thue fixed point and the recurrences for the extremal number of ones. These are the nontrivial external premises. Equation (2) in the proof is direct integer algebra with integer-valued endpoints ensured by parity. The collision equation and parity split handle all five possible differences of the \(0\)-minus-\(2\) counts, including degenerate weights. The recurrence produces widths increasing by one along each \(4n-1\) step. In the failure cases, the proof either bounds additive complexity by three or exhibits a matching of many disjoint colliding Parikh-vector pairs, establishing divergence rather than just a single counterexample. The standalone checker passed for selected lengths and valuations. Its finite tests are not substituted for the infinite proof.

## Originality — PASS (residual priority risk)

The closest 2024 primary paper proves the preservation statement only for valuations \((0,1,\lambda)\) with \(\lambda\ge5\) (Theorem 31) and gives two examples of failure. The new statement classifies **all integer valuations** through an exact divisibility condition, and shows that every failure entails diverging loss of abelian classes; these are not covered by the cited one-parameter theorem. The 2014 exact Parikh-spectrum theorem is the main prior structural ingredient and logically permits the new derivation, but does not itself state a valuation criterion, collision classification, or quantitative weighted gap. The 2025 group-action result concerns a distinct quotient, and the 2018/2019 additive-complexity paper uses a different morphism. Targeted research-record, literature and prior-ledger searches found no matching criterion. Residual risk: an unindexed or implicit equivalent from the published spectral theorem might already be known.

## Value — PASS

This settles a natural all-integer-valuation version of the explicit 2024 question about preserving additive versus abelian distinguishability for a well-studied square-free ternary word. It yields a complete arithmetic phase diagram, not just a sufficient separation threshold; nearby strictly increasing valuations such as \((0,2,7)\) and \((0,2,8)\) lie on opposite sides. Its divergent-gap alternative quantifies the irreversibility of a bad valuation on arbitrarily long windows. No claim of new Parikh-spectrum machinery or of a result for all ternary words is made.

## Closest literature and limitations

The decisive inputs are Blanchet-Sadri et al., Integers 14 (2014), Lemma 8 and Theorem 2, and Popoli–Shallit–Stipulanti, arXiv:2410.02409v1, Section 4. The 2025 orbit study and Chen–Wen–Wu's distinct-substitution additive result were also compared. The 2014 general spectrum makes the classification accessible by additional arithmetic arguments, leaving a residual originality assessment risk; independent assessment is advisable before external priority claims. Finite checker output does not prove the infinite claim. Only integer scalar weights and the specified word are covered.

Self-review: passed. Independent audit: not yet performed.
