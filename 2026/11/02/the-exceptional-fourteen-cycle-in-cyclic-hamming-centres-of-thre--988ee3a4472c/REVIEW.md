# Scientific review: cyclic-Hamming three-one necklace centres

## Correctness — PASS

The statement explicitly confines centres and targets to rotation orbits of binary words of weight exactly three, using minimum-over-shifts Hamming distance. A pairwise-separation lemma reduces distance \(2\) to overlapping cyclic pair-distance profiles; distinct classes with disjoint profiles have distance \(4\). The proof constructs radius-two centres for lengths 5–12 and 14, uses Cauchy–Davenport to rule out a triangle-free allowed-difference circulant at prime length 13, and uses the exact Mantel edge threshold to rule out radius two for all \(n\ge15\). Equality in Mantel at length 14 forces the parity bipartition; direct cyclic-gap classification gives precisely two centres. Burnside counts the universal radius-four centres. Exhaustive independent shifts and symbolic separation profiles agree through length 17, and full finite census runs through length 26. No finite experiment substitutes for the infinite proof.

## Originality — PASS, with residual priority risk

The 2020/2023 Adamson–Deligkas–Gusev–Potapov necklace-centre papers use subword-multiset *overlap distance*, not minimum-rotation Hamming distance (see 2023 open-access text, §3.1–3.2, especially overlap definition and its optimization objective). The 2021 multidimensional necklace full text treats fixed-content enumeration and overlaps, but it does not imply the fixed-weight-three Hamming radius theorem. Searches for rotational Hamming, cyclic triangle triples, exact length-13/14 thresholds, and nearest aliases in published mathematical records did not reveal the same theorem. A general graph extremal theorem proves part of this result only after the new reduction; merely citing Mantel does not by itself give the classification. Residual risk: a specialized cyclic-difference-family classification or another indexing of cyclic Hamming centres may already contain an equivalent statement.

## Mathematical value — PASS

Weight three is the first constrained binary necklace layer where a single centre can have both distance-two and distance-four targets. The all-length phase diagram has a sharp nonmonotone exception (the radius jumps at 13, drops at 14, and then rises permanently), and the two distinct optimal centre orbits at 14 have a natural parity and extremal-graph explanation. The result is a complete, motivated classification of a natural covering invariant, not an arbitrary finite slice or a routine reproduction of a table.

## Scope, checks and limitations

The result makes no assertions about multiple centres, other weights, unrestricted binary centres, other quotient groups, or alternate metrics. The small-size multiplicities are checked exhaustively by the packaged verifier. All-length conclusions are analytic. The primary papers were compared at the level of metrics, quantified objects, and implications rather than title similarity. The priority comparison is based on the checked sources and semantic research search, not a universal uniqueness certification.

Self-review: passed. Independent audit: not yet performed.
