# Same-model review

Correctness: **PASS.** The proof exhaustively classifies maximal cliques and maximal stable sets in \(K_{a,b}-M_t\), then counts exactly the surviving edges disjoint from each deleted matching pair. Edge cases with isolated vertices are included. The standalone verifier independently enumerates all subsets for \(1\le a,b\le5\) and all legal \(t\), and checks the crown specialization through \(n=6\).

Originality: **PASS.** The closest literature defines CIS/non-CIS pairs, gives general CIS structure, and completely characterizes the unique-pair (almost-CIS) case. Those results imply the P4 defect-one consequence and some zero/nonzero recognition facts, but no inspected source or targeted semantic search supplied the all-parameter count \(t((a-1)(b-1)-t+1)\). The 2026 recognition preprint's full text was inaccessible through the available primary/OA routes, so residual overlap risk is explicitly retained rather than converted into a noncoverage claim.

Value: **PASS.** Exact certificate counts on a canonical perturbation of complete bipartite CIS graphs complement the recent general coNP-completeness result. The theorem gives both a sharp stability boundary and a compact crown-graph formula, so it is more than a routine yes/no special case.

Closest literature and limitations: Wu–Zang–Zhang (2009) already covers the almost-CIS implication globally; Andrade–Boros–Gurvich (2006) gives foundational structural conditions; Tao–Yang–Zang (2026) gives general recognition complexity. The claim is restricted to matching deletions from complete bipartite graphs, and the finite checker is not an infinite proof.

Same-model review: passed. Independent audit: not yet performed.
