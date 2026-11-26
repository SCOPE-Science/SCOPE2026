# Independent mathematical audit

## correctness

PASS

The frozen stability, label diagram, and closure argument are valid. A lifted path proves preservation of the reachability cap under onto bounded morphisms. On a generated component the radius cap makes the finitely many boxed clauses apply everywhere. Their unique labels encode exactly the successor-image condition, and back lifts paths from the labelled root to show surjectivity onto the target generated subframe. A finite union over the target roots and an onto map to the target complete the definability proof, using only depth h+1. The frozen terminal-loop/dead-end comparison proves the pointed sharpness claimed there but does not prove sharpness under frame validity. In the repair G is the disjoint union of the dead-end path of length h and (for h>=1) the loop-ended path of length h-1; F adds the loop-ended path of length h. Under every valuation the added root transfers at depth h to the dead-end root, and each nonroot transfers exactly to a suffix of the shorter loop-ended path. Thus the two frames have identical depth-at-most-h validity, also for h=0. G validates the single-variable depth-(h+1) separator since the long walk is absent on the dead-end component and walks of lengths h-1 and h coincide at the loop in the short component. F falsifies it at the added root with different values of p at the final two worlds. Box false handles h=0. Check 3 in /workspace/independent_checks.py made 2412 exhaustive tiny diagram/map comparisons, with a literal multi-label valuation enumeration, and checked the pointed witnesses for h=0..5. The replacement python3 /workspace/repairs/3/CHECK.py passed seven frame pairs with exact one-atom type enumeration and separator validity; full arbitrary-valuation equivalence comes from the proof.

## originality

PASS

Pass is for the repaired sharp bound on frame-validity axiomatizations; the diagram and relative closure argument supply the upper bound, not an unqualified novelty claim over prior finite definability machinery. The lower bound compares all worlds and valuations within the very same ambient class, and gives an explicit separator. The original pointed sharpness result does not imply this just by taking the negation of its diagram.

## value

PASS

This determines how much modal nesting a general relative axiomatization may actually require, not merely the depth of one diagram encoding. The matching pair shows that adding arbitrarily many shallower formulas cannot help, while the upper bound is independent of the number of worlds. The lower bound already uses one proposition in a single separator.

The dated certificate retains the supplied scientific assessment, sources and limitations.
