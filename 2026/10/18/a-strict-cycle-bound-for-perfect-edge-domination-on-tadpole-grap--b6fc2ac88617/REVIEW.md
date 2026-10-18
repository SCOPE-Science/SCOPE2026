# Review of the cycle bound for tadpole perfect edge domination

## Correctness — PASS

Every perfect edge dominating set on a connected graph corresponds uniquely to the local three-color encoding. The six permitted ordered color pairs induce the displayed integer transfer matrix, and exact multiplication proves \(M^5=M^4+M^2\). A boundary matrix that checks the degree-three attachment vertex and its tail converts this identity into the recurrence with respect to cycle length. A reversible partition of the last three tail vertices proves the second recurrence. Direct base enumerations give the complete \(3\times3\) strictly positive deficit matrix. Strong induction in the cycle length followed by strong induction in the tail length proves strict positivity for every declared parameter. `verify.py` checks the matrix identity, base cases and separate brute-force edge-subset counts. No finite search is used as a substitute for the infinite proof.

## Originality — PASS

The closest source, Grippo–Lin–Moyano–Vera, *Counting perfect edge dominating sets: extremal results and linear-time algorithms*, arXiv:2607.03894v1, poses cycle-extremality for connected graphs as Conjecture 5.1, proves the tree comparison and gives path/cycle recurrences and generic series-parallel counting algorithms. It does not state the infinite tadpole inequality or its exactly determined bivariate deficit. Its Proposition 2.5 supplies the previously known tail-extension identity, which is explicitly credited. Grippo–Lin–Vera, arXiv:2509.04598v2, counts these structures algorithmically on \(P_6\)-free graphs, not for the unbounded tadpole family. Targeted searches for the named graph, equivalent lollipop terminology, unicyclic extremal counting, cycle maximization and the transfer recurrence did not reveal a covering theorem. Closest indexed items involved different edge/vertex invariants. Remaining risk: relevant work with different terminology or unavailable indexing could have been missed.

## Mathematical value — PASS

The 2026 paper specifically leaves the cycle upper bound open beyond the treated tree case. Tadpoles are a natural two-parameter first departure from cycles and trees within connected unicyclic graphs. The theorem settles this whole infinite class with strict inequality and supplies an **exact positive-deficit recurrence in two independent graph parameters**, not merely a fixed-order numerical instance or a generic dynamic-programming implementation. It provides a reusable boundary-transfer mechanism for extending the class, while making no claim to a solution for all unicyclic graphs.

## Limitations and external comparison

The proof does not cover multiple pendants, branched attached trees, general unicyclic graphs or unrestricted connected graphs. The symbolic calculations can be repeated with standard integer arithmetic. General counting algorithms from the motivating paper give counts instance-by-instance but do not assert the parametric extremal conclusion. The available database and literature comparisons support best-knowledge originality, not an absolute guarantee against unindexed material.

Self-review: passed. Independent audit: not yet performed.
