# Scientific review: total-domination histories of subdivided cliques

## Correctness — PASS

The proof splits the open-neighborhood process into independent original-vertex and subdivision-vertex subsequences, proves there are exactly \(n!\) orders of the former, and bijectively enumerates the latter by a last-edge one-or-two-new-endpoint recurrence. It then counts order-preserving shuffles and obtains every exponent and both extreme coefficients. A standalone checker built directly from graph neighborhoods agrees at \(n=2,3,4,5\); the infinite theorem is proved, not extrapolated.

## Originality — PASS

Brešar, Henning, and Rall (2016), Theorem 8.4, already determine the maximum sequence length of general incidence graphs in terms of an underlying Grundy covering number. Bahadır, Gözüpek, and Doğan (2020/2021) study equality of extreme lengths. These strong precedents do not supply the claimed **full ordered-histories polynomial** or its per-length coefficients, based on the inspected relevant text. Ordinary complete-graph edge-cover tables enumerate unordered edge sets and are not the same invariant. A previously unindexed coefficient formula under an alternative name remains a priority risk.

## Mathematical value — PASS

The result completely enumerates legal finished greedy histories in a canonical growing graph family. The polynomial refines minimum and maximum total domination lengths and has exact factorial coefficients at both extremes; it also demonstrates that every intermediate length occurs. This distinguishes order-sensitive greedy behavior from ordinary edge-cover cardinality counts.

## Scientific scope and limitations

The theorem concerns \(S(K_n)\) for each integer \(n\ge2\), and no general subdivision theorem or asymptotic probabilistic limit is asserted. The maximum length alone is implied by known incidence-graph extremal theory. Independent publication-priority and mathematical audit are absent.

Self-review: passed. Independent audit: not yet performed.
