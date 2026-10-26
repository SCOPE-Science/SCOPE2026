# Review

## Correctness

The lower bound follows by translating undirected adjacency to \(S(x,y)\lor S(y,x)\) without increasing quantifier rank. Rank one is immediate, and the rank-two boundary is verified directly. For ranks \(q\ge3\), the upper bound uses the order-preserving form of the cycle-cut gap strategy in Brown–Hoshino; its short-gap preservation maintains the orientation of every successor edge.

## Originality

The closest published result classifies quantifier-rank equivalence for undirected cycles, with cutoff \(2^{q-1}+3\) for \(q\ge3\). It does not state the corresponding equivalence for directed successor cycles. Searches of the research database found a directed-path threshold and cyclic-group EF results, but no direct successor-cycle threshold. These comparisons support a narrow orientation-invariance extension; they do not prove that no unindexed source exists.

## Value

The result identifies exactly when adding a coherent orientation to a finite cycle fails to improve quantifier-rank distinguishability. This is a natural, exact finite-model-theoretic boundary rather than a finite enumeration or a mere relabeling of the undirected theorem.

## Closest literature and limitations

Brown–Hoshino (2007) supplies the undirected cycle threshold and gap strategy. Gomaa (2010) studies quantifier-depth bounds for finite abelian groups in a different language. The result here is restricted to binary relational successor cycles of size at least three; a unary function language is outside scope.

Self-review: passed. Independent audit: not yet performed.
