# Review of Perfect Roman domination polynomial of complete multipartite graphs

## Correctness
PASS. A zero in part \(X_i\) sees exactly the \(2\)-labels outside that part, so the perfect Roman condition is precisely \(T-t_i=1\). Splitting by \(T=0\), \(T=1\), \(T=2\), and \(T\ge3\) gives disjoint exhaustive families. The polynomial terms count each family without overlap, and the minimum formula follows by minimizing the corresponding weights. Independent definition-level enumeration agrees for every complete multipartite type through order nine.

## Originality
PASS. The inspected 2019 full article gives polynomial-time and linear-time algorithms for the minimum perfect Roman domination number on several graph classes, including cographs, but does not state an arbitrary complete-multipartite all-function enumerator. The 2024 full article studies enumeration of pointwise-minimal perfect Roman dominating functions, not the weight distribution of all feasible functions. Targeted semantic and exact-phrase searches returned no complete-multipartite perfect Roman polynomial. The closest indexed findings concern other Roman-domination variants or unrelated complete-multipartite enumerators.

## Value
PASS. Perfect Roman domination is algorithmically nontrivial even on broad structured classes. The theorem converts the complete-multipartite subclass from minimum-only computation to an exact feasible-function description and weight census. The result also compresses the minimum on this family to a closed three-candidate formula and separates it cleanly from minimal-function enumeration.

Same-model review: passed. Independent audit: not yet performed.
