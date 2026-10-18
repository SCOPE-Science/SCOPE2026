# Self-review

## Correctness: PASS

The outer-product multiplication rule gives an if-and-only-if commutation condition for distinct nonzero idempotents, including the potentially problematic case where both products are nonzero. Each ground coordinate has exactly \(2^{k+1}+k-1\) possible patterns in an ordered \(k\)-clique; missing double-singleton patterns represent precisely failed idempotence, and the all-empty pattern represents precisely nonmaximality. Standard finite inclusion-exclusion proves both global formulas without extrapolation from experiments. Degree counts and the exact diameter follow directly from the same cross-annihilation criterion. The executable direct finite census supports, but does not substitute for, the uniform combinatorial argument.

## Originality: PASS, with residual risks

Known Boolean-idempotent rank-one counts (Butler–Markowsky and OEIS A363232) are distinguished from the claimed all-arity clique/facet enumeration. The relevant 2010 full-text treatment of semiring commuting graphs establishes diameter and girth results for different vertex sets, not the complete size-resolved clique and facet census here. Prior work on the aperiodic Brandt semigroup concerns singleton matrix units and does not imply the census for all rectangular Boolean rank-one idempotents. This is a scoped literature comparison, not a global proof of priority; full-text access to some older Boolean-relation-semigroup studies remains incomplete.

## Value: PASS

The selected rank-one idempotent stratum is canonical in the Boolean relation semigroup. Its commuting families are exactly partial mutually annihilating rectangular decompositions, a structural problem not captured by the known vertex totals. Every maximal size occurs, so the clique complex is sharply nonpure; the formulas resolve the entire facet profile and all degrees, including isolates and component diameter. These are motivated natural graph/semigroup invariants across all matrix dimensions.

## Limits

No assertion is made for arbitrary Boolean idempotents or for the standard whole-semiring commuting graph. Priority beyond inspected sources and independent mathematical validation remain unresolved.

Self-review: passed. Independent audit: not yet performed.
