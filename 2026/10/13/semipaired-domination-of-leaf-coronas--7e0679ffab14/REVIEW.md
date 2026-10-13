# Review of Semipaired domination of leaf coronas

## Correctness
PASS. The lower bound is forced independently in every private leaf-support pair: a dominating set must contain the leaf or its unique neighbor, hence at least \(n\) vertices, and semipaired sets have even size. The upper bound uses a proved lemma that every tree square has a matching of size \(\lfloor n/2\rfloor\). A longest-path endpoint reduction always removes a pair at tree-distance at most \(2\) while leaving a tree, until at most one vertex remains. A spanning tree transfers these pairs to the base graph because graph distance can only decrease. Thus all original vertices form a semipaired dominating set for even \(n\), and for odd \(n\) one unmatched original vertex is paired with its private leaf. Exhaustive optimum computation on all connected labeled base graphs through order five agrees with the formula.

## Originality
PASS. The 2019 same-invariant full text treats complexity, interval graphs, trees, and approximation and contains no corona or product treatment. The 2020/2021 same-invariant full text treats split graphs, block graphs, and bounded-degree complexity; targeted full-text checks found no corona, product, or pendant occurrence. Semantic searches under corona-product, leaf-corona, pendant-leaf, and tree-square formulations returned no semipaired theorem covering the claim. A 2021 paper studies corona operations for semitotal domination, but that predicate lacks the required global pairing and therefore does not imply this formula. The nearest prior record on semipaired crown graphs is object-disjoint and gives no corona implication.

## Value
PASS. The theorem is not a one-family numerical exercise: it gives one exact formula for the leaf corona of every connected graph, independent of the base graph’s structure. It also exposes the precise mechanism behind that universality—private leaves impose the sharp transversal lower bound, while a near-perfect matching in every spanning-tree square supplies the parity-correct semipairing. This converts what is algorithmically nontrivial on general graphs into a closed form on an entire graph operation.

Self-review: passed. Independent audit: not yet performed.
