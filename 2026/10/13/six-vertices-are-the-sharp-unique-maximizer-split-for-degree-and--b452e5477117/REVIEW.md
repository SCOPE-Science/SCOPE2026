# Self-review

## Correctness
**PASS.** The complete connected labeled graph domain through six vertices is enumerated. Independent distance computations agree exactly; two independent exact Freeman-betweenness implementations agree on every connected graph; and the six-vertex conflict set is quotient-checked under all vertex relabelings. The unique class has a full \(6!\)-element orbit, and direct exact evaluation reproduces the representative's degree, closeness, and betweenness vectors.

Risk: the exhaustive statement stops at six vertices, as stated.

## Originality
**PASS.** Classical and modern network literature establishes that degree, closeness, and betweenness encode different notions of importance, and exact betweenness formulas are known for many graph families. That qualitative separation is not claimed as new. The accepted claim is instead the sharp finite unique-maximizer boundary and its complete first layer: universal coincidence through five vertices when both leaders are unique, exactly \(720\) six-vertex conflicts, and one asymmetric isomorphism class. Searches by aliases, exact counts, order, and representative structure did not locate a covering theorem or table.

Risk: search failure is not a proof of bibliographic uniqueness. An unindexed finite-graph census or software table could contain the same small-order classification.

## Value
**PASS.** Degree and betweenness answer different substantive network questions—local popularity versus brokerage on shortest routes—but many applications reduce either measure to a single “most central” actor. The exact smallest connected network where those two unambiguous choices conflict is therefore a natural structural invariant. The fact that the entire first obstruction is one asymmetric graph type, and that closeness uniformly sides with degree there, gives a compact benchmark for understanding the first possible leadership split.

Self-review: passed. Independent audit: not yet performed.
