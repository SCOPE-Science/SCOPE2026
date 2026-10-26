# Review of the degree-sharp high-girth coalition theorem

## Correctness — PASS

The proof begins with a self-contained universal upper bound: two disjoint TOIDS cannot coexist, so the coalition graph of a partition has pairwise-intersecting edges and a universal hub. Each partner of the hub must meet one fixed neighborhood of size at most \(\Delta\), or one fixed two-vertex edge, giving at most \(\Delta\) partners. For the lower bound the chosen maximum-degree vertex \(v\) has independent \(N(v)\); the absence of triangles and four-cycles, together with minimum degree two, means only \(v\) is undominated by \(V\setminus N(v)\). Each singleton neighbor repairs exactly that deficiency, and its complement remains independent. These are unrestricted logical arguments, with no reliance on numerical extrapolation.

The standalone verifier checks every one of the \(72\) eligible labeled graphs on at most six vertices and several larger constructions against exact partition enumeration. The small girth-four boundary is checked on all \(203\) partitions of a six-vertex graph. Finite tests corroborate but are not substituted for the theorem's proof.

## Originality — PASS, subject to priority risk

The closest inspected primary source is Buntina–Golmohammadi, arXiv:2607.23623 (first public 26 July 2026). Its maximum-degree result is one-sided, and its exact-family theorem covers complete graphs, complete bipartite graphs, paths, and cycles. The cycle special cases are subsumed and are explicitly excluded from the originality claim. The present finding supplies the missing lower bound for the whole high-girth minimum-degree-two class and a local sufficient condition; this does not follow from the source's degree upper bound without the new neighborhood argument. Specific searches for the invariant combined with girth, radius-two neighborhoods, and degree equality did not locate a covering theorem in the inspected scientific records. Relevant published mathematical-record summaries dealt with different domination parameters. Unindexed exact results under another name remain possible.

## Value — PASS

The source paper explicitly raises degree-based bounds as an open research direction. The result identifies an extensive, structurally motivated infinite class on which the general maximum-degree bound is always sharp, even for disconnected and nonregular graphs. An explicit partition makes the extremal value constructive. A small bipartite example at girth four verifies that the girth hypothesis has genuine force, while ordinary small-cycle examples are not presented as novel results.

## Scope and residual risks

The theorem gives a sufficient condition and exact value, not an equality characterization for all graphs. The six-vertex boundary is an exhaustive finite result; source equivalence and bibliographic priority require external expert review. The code is a reproducibility check, not an independent formal verification.

Self-review: passed. Independent audit: not yet performed.
