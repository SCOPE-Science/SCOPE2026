# Review of All paired-dominating sets of complete multipartite graphs

## Correctness
PASS. A selected complete multipartite subgraph of even order \(2t\) has a perfect matching exactly when no selected part exceeds \(t\); necessity is immediate and sufficiency follows by induction after matching vertices from two largest parts. That condition already forces at least two selected parts, which is exactly what domination needs. The bad half-majority events are disjoint, so the coefficient formula is exact. Any valid set contains a cross-part edge whose endpoints are themselves paired dominating, proving that the minimal sets are exactly the edges. The independent brute-force checker agrees through order nine.

## Originality
PASS. The inspected 2021 publisher source studies upper paired domination and its computational complexity but does not state a complete-multipartite all-set classification. Exact and semantic searches for paired domination, upper paired domination, complete multipartite graphs, and paired-dominating-set enumeration found no equivalent formula. The closest retrieved database results concern a paired-versus-total domination gap in trees and unrelated complete-multipartite domination variants.

## Value
PASS. Upper paired domination is difficult on broad graph classes, while this theorem identifies the precise reason it collapses on complete multipartite graphs and simultaneously retains the full nontrivial distribution of all feasible set sizes. The coefficient formula is an exact Hall-type enumeration, not just the routine observation that the minimum paired-domination number is two.

Same-model review: passed. Independent audit: not yet performed.
