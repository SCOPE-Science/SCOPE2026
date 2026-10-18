# Review of complete two-variable theories of colored equivalence relations

## Correctness: PASS

The defining local observations are expressible in the two-variable language, including two different elements of one unary color in one equivalence class: the required quantifier deliberately rebinds the first variable. Existence of one and two distinct classes of each local vector is also expressible with two variables, proving necessity. For sufficiency, the invariant in the two-pebble back-and-forth game tracks both atomic information and the full truncated local vector of every currently occupied class. The one-versus-two classes distinction supplies precisely the external witness needed when one pebble remains fixed. Induction on the number of moves covers all quantifier ranks, including infinite structures. The finite induced representative and all possible global profiles are constructed explicitly; summing local vector coordinates proves the upper bound, and a single finite conjunction of two-class existence formulas proves sharpness. The independent small-instance checker agrees with the predicted invariants, but the all-cardinality conclusion rests on the symbolic proof.

## Originality: PASS, subject to historical-priority uncertainty

The precise statement is a classification of complete *sentence theories* and a sharp *induced finite substructure* bound, simultaneously and for every number of unary predicates. Fiuk (2026) proves finite-model and complexity theorems for much more expressive equality-free fragments with an equivalence relation; the relevant sections inspected do not state an exact two-variable monadic theory count or induced-core extremum. Kieroński--Otto (2005), especially the introduction and Section 4, proves an exponential model property for two-variable logic with one equivalence and arbitrary extra relations, but no sharp cardinality-uniform core theorem in this restricted signature was located. Pratt-Hartmann (2015) adds unrestricted counting quantifiers and analyzes complexity; arbitrary counting can distinguish multiplicities beyond the double truncation used here. Searches for double-truncated class profiles, the number 6560, and the formula \(2q3^q\) did not produce an equivalent statement in accessible published sources. The use of two-pebble games itself is classical. An old or differently named monadic-equivalence classification might still subsume the explicit formulas; no independence or definitive priority is claimed.

## Value: PASS

The result gives a complete, finite, computable normal form for elementary equivalence in the smallest natural signature combining unary colors and an equivalence relation. Unlike generic satisfiability bounds, it counts every complete sentence theory and gives the least possible size of an actual *induced* truth-preserving substructure, with a matching single-sentence lower bound. The exact one-unary-predicate case (6560 theories; sharp 36-element core) makes the invariant concrete and supplies an independently checkable finite benchmark. This is an exact structural classification rather than merely a check of a normalization convention.

## Scope and residual risks

Only standard first-order quantifiers, equality, one equivalence symbol, and unary predicates are allowed. The theorem does not claim to extend to counting quantifiers or to multiple independently interpreted binary relations. Uninspected older formulations, including presentations through colored partitions and modal S5 types, may encode the same classification. Finite computations do not certify the infinite or all-arity portions. Independent scientific audit remains outstanding.

Self-review: passed. Independent audit: not yet performed.
