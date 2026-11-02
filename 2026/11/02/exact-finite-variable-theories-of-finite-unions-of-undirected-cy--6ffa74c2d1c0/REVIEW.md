# Scientific review: exact finite-variable theories of cycle unions

## Correctness — PASS

Every nonempty finite simple degree-two graph is a disjoint union of cycles. Recursive walk-distance formulas can be written with only three reusable variable names. Their exact-distance layers define membership in each \(C_n\), including the even singleton-antipode and odd two-farthest-vertex cases. A width-\(k\) sentence detects every number of same-length components below or equal to \(k\). An indefinite \(k\)-pebble component-matching invariant proves the converse. The separate width-one and width-two classifications and all claimed strict boundaries have explicit witnesses. Three Python scripts test finite predicates and fixed-point tuple-type refinements, with no reliance on finite search for the infinite proof.

## Originality — PASS, with historical-priority qualification

The closest located primary source is Brown–Hoshino (2007), treating paths and cycles under a fixed quantifier-rank bound, while the present theorem fixes variable width and allows arbitrarily large rank across disconnected unions. Grohe–Otto (2012) supplies general game methods; Kotek–Makowsky (2013) proves rank-sensitive disjoint-union smoothness. Comparison of these statements, accessible research records, and a separate finite-rank cycle classification did not identify an already covering exact classification. Because general composition machinery may have a stronger implication in uninspected literature, this conclusion is qualified; searches alone do not establish historical priority.

## Mathematical value — PASS

The theorem supplies a natural, complete, exact family-wide invariant: all individual cycle lengths remain observable at width three, whereas multiplicities become invisible exactly after the number of available variables. It gives smallest representatives and a strict unbounded variable hierarchy. The contrast with bounded-rank cycle indistinguishability is structurally informative rather than an arbitrary computed instance.

## Independent status and limitations

The conclusion applies only to nonempty simple undirected 2-regular graphs in counting-free pure adjacency logic. The finite test suite corroborates but does not establish the general case. A broad literature search and independent mathematical audit have not been completed.

Self-review: passed. Independent audit: not yet performed.
