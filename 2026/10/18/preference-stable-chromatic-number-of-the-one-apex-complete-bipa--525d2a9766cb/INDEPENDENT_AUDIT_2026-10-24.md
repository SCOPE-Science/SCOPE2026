# Independent mathematical audit

## correctness

PASS

PASS: Fix a>=b>=1 and palette k=b+2. Greedily color universal vertex u with its favorite; process b vertices of side B assigning favorite of remaining colors; color all of A with the sole remaining color. Every envy arc points to an earlier colored vertex, including the full-arc definition in the pinned text; in Koana-Oh-Yoneda’s adjacency-only envy graph this is only easier. For k=b+1 when b>=2, choose b indexed vertices on each side whose favorite i (1<=i<=b) and second favorite k produce, after excluding ANY one color used on u, a complete set of favorite remaining colors in both sides. Every proper coloring has disjoint nonempty color sets S_A,S_B. For each s in S_A a B vertex assigned f(s) in S_B prefers s; for each t in S_B an A vertex assigned g(t) in S_A prefers t. A cycle of g∘f on the finite S_A gives a directed alternating envy cycle; every arc joins A and B, so is an actual edge also under the paper’s stricter official definition. Distinct colors on that orbit force distinct witness vertices. If b=1 the graph contains a triangle, giving 3. Fresh exhaustively enumerated all proper (b+1)-colorings for (a,b)=(2,2),(3,2),(3,3): respectively 6,6,168 proper, zero stable, corroborating the construction without proving all parameters. Potential wording difference: pinned RESULT defines envy arcs between any two vertices whereas original arXiv defines only between adjacent vertices; both bounds actually hold under adjacency-restricted definition, so the asserted numerical invariant survives.

## originality

PASS

PASS (qualified): Original Koana-Oh-Yoneda arXiv:2609.00569 full lawful HTML was read anew, including the graph-edge envy definition, Proposition 3.7 chi_stable(K_{a,b})=b+1 and general reachability/Grundy bounds. Its graph-class table lists complete bipartite, paths and cycles but no K_{a,b,1} formula; full-text find for tripartite and universal vertex found none. The special K_{2,2,1} overlaps other finite graph results; a separate Resultary result for K_{2,3,3} is a different non-singleton tripartite type. Subgraph monotonicity chi_stable(K_{a,b,1})>=b+1 plus upper bound b+2 leaves the apex increment unresolved, which the robust favorite profile proves. Qualified by possible unpublished general join/complete multipartite results, not an institutional access failure because arXiv HTML full text was accessible despite a VPN attempt failing.

## value

PASS

PASS: Adding a single universal apex to all complete bipartite K_{a,b} is the natural next family after the established exact bipartite result, and its one-unit increase in stable color requirement is a sharp infinite two-parameter classification, not a tiny finite instance. The robust one-deletion favorite profile is a structural lower-bound method and the exact answer is not implied by ordinary chromatic number or the general orientation upper bound alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
