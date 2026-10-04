# Review: All k-forcing sets of complete multipartite graphs

## Correctness
PASS. The proof fixes the first actual force. In a complete multipartite graph a black vertex in \(V_i\) sees exactly the white vertices outside \(V_i\), so the first force is possible exactly when \(1\le W-w_i\le k\) and the part contains an initial black vertex. That force clears every outside white vertex. The only remaining whites lie in \(V_i\), and they are forceable exactly when their number is at most \(k\). This proves both directions without assuming a particular later forcing order. Maximizing the two independent white capacities gives the minimum-size formula, and inclusion-exclusion over maximizing witness parts gives the minimum-set count. The packaged verifier agrees with the theorem on all tested complete multipartite profiles through order \(9\) and \(k\le4\).

## Originality
PASS with stated residual risk. The foundational \(k\)-forcing paper defines the parameter and proves general bounds, but its inspected full text does not state an arbitrary complete-multipartite classification. Boyer et al. prove the ordinary zero-forcing polynomial for complete multipartite graphs with all parts of size at least two; that \(k=1\) slice is explicitly excluded from the novelty claim. A 2024 paper on \(k\)-forcing automata treats complete bipartite graphs, including minimum-set behavior, but not arbitrary complete multipartite graphs and not the retained all-set criterion or minimum-set inclusion-exclusion count. Published-record searches for complete multipartite \(k\)-forcing and aliases found no stronger statement that implies the retained theorem.

## Value
PASS. Complete multipartite graphs are a canonical dense family and \(k\)-forcing is a standard irreversible propagation invariant. The theorem compresses the entire dynamics for every initial set to one witness-part condition, gives an exact closed formula for \(F_k\), and counts every minimum set even when several witness parts overlap. It unifies the ordinary zero-forcing and complete-bipartite cases while exposing the precise capacity mechanism governing arbitrary multipartite graphs.

## Closest literature and limitations
The closest exact same-object result located is the \(k=1\) complete-multipartite zero-forcing polynomial of Boyer et al. The closest \(k>1\) family result located is the complete-bipartite analysis in the 2024 automata paper. The retained theorem strictly changes the quantified domain to arbitrary numbers of parts and supplies a complete all-set characterization plus an exact overlap-corrected basis count. Residual risk remains from older literature indexed only under generalized-forcing terminology.

Same-model review: passed. Independent audit: not yet performed.
