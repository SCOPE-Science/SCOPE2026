# Review

## Correctness
PASS. In \(K_{n_1,\ldots,n_r}\), a vertex from a part of size \(b\) strongly dominates a vertex in a different part of size \(a\) exactly when \(b\le a\). This gives the strong domination number by a complete three-case analysis: singleton minimum, unique minimum of size at least two, or repeated minimum of size at least two. Applying the same classification after one or more deletions yields the stated stability formula. The only one-deletion-resistant repeated-minimum case is minimum size \(3\), for which two deletions create a singleton part. An independent brute-force replay for every noncomplete multipartite profile through order \(8\) agrees with both formulas.

## Originality
PASS. The initiating 2026 preprint studies the same stability parameter and treats complete bipartite and balanced complete multipartite graphs, but it does not give the arbitrary part-size classification stated here. Its balanced-family statements are not equivalent to the present formula. Semantic database searches for the exact invariant, the balanced and Turan aliases, the exceptional \(K_{3,3}\) case, and arbitrary complete multipartite profiles returned only different domination variants or unrelated multipartite results. Earlier strong-domination papers inspected during the comparison concern \(\gamma_{st}\) itself rather than its 2026 vertex-deletion stability.

## Value
PASS. This is a complete classification on a canonical graph family, not an isolated parameter evaluation. It reduces the stability to two elementary statistics, resolves the balanced multipartite family in a sharp two-valued form, and identifies a concrete exceptional minimum size \(3\) that is invisible in the more complicated bounds and cases stated in the initiating preprint.

Closest literature: arXiv:2601.03891v2 is the decisive comparator because it defines the same stability parameter and explicitly studies balanced complete multipartite graphs. The main limitation is the possibility of an older poorly indexed equivalent statement or a later revised version of that preprint.

Self-review: passed. Independent audit: not yet performed.
