# Scientific assessment

## Correctness

**PASS.** The universal VC formula has a mathematical upper bound obtained from a cyclic-gap obstruction and a constructive lower bound using step-two/step-three fillings. Each residue class of cycle order is addressed, including the unique short-gap case. The finite adaptive lower bound has a concrete full tree with distinct terminal witnesses, and the entropy bound of \(39<64\) independently excludes depth six. Complete exhaustive recursion verifies the first threshold for all cycles on three through thirteen vertices. The direct mask checker and independent cyclic-gap checker agree. The disjoint-union statement uses a proven product-additivity lemma for both dimensions, not an extrapolated finite pattern.

## Originality

**PASS with residual historical-priority risk.** Searches addressed maximal independent sets, independent domination, cycle membership shattering, VC dimension, Littlestone dimension, vertex-transitive regular examples and product reductions. Bhaskar (2017) and Walker (2022) give general tree-shattering theory, not this graph class. Drmota et al. (2019) enumerate maximal independent sets in graphs including cycles but do not analyze membership-query VC or Littlestone dimensions. Mofidi (2022) studies independent-set and neighborhood families under well-gradedness/extremality, not the specific maximal-independent-set cycle classification. The closest earlier path result shows a gap in linear forests but does not imply either the thirteen-cycle threshold or the vertex-transitive regular construction. An equivalent result in older graph-identification literature remains possible.

## Mathematical value

**PASS.** The exact static dimension of every connected cycle, and therefore every finite \(2\)-regular graph, is a natural complete classification. The thirteen-cycle is a sharp structural boundary: every smaller cycle has no adaptive excess, while its own complete depth-five witness produces a linearly growing gap in regular vertex-transitive graphs after taking isomorphic disjoint unions. The complete five-query trace statistic strengthens the isolated dimension claim and measures the failure of fixed shattering. The result does not require a general Littlestone formula for longer connected cycles to have this value.

## Limits and comparison

The all-width VC result has a direct proof; the first adaptive threshold is an exact finite theorem with fully specified checkers and witnesses. No statement determines the online dimension of arbitrary longer cycles. The cited papers concern enumerative cycle families, general shattering bounds, and related but different graph concept families; they do not provide equivalent complete coverage in the inspected material. Historical priority outside accessible sources is not excluded, and no independent audit is claimed.

Self-review: passed. Independent audit: not yet performed.
