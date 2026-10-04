# Same-model review

## Correctness
PASS. For a vertex outside \(D\) in part \(V_i\), the selected-neighbor count is exactly \(d-d_i\). Equality of these counts over all outside vertices is therefore equivalent to equality of \(d_i\) over all non-full parts, and positivity of \(d-t\) is exactly domination. The product formula partitions all proper fair dominating sets by their unique common partial occupancy \(t\); the only overcount is the full set and the only invalid product term is the empty set at \(t=0\). The scalar minimum follows from two explicit constructions and the dichotomy \(t=0\) versus \(t\ge1\).

## Originality
PASS. The 2011 foundational paper defines fair domination and records only the scalar complete-bipartite equality \(\operatorname{fd}(K_{m,n})=\gamma(K_{m,n})\). The 2021 counting paper defines the fair domination polynomial and treats the balanced complete-bipartite family \(K_{n,n}\), not arbitrary complete multipartite graphs. Searches using “fair domination,” “\([k,k]\)-dominating,” and “regular set” terminology did not locate an arbitrary-part all-set classification or polynomial. The balanced bipartite specialization is explicitly excluded from the novelty claim.

## Value
PASS. Fair domination is a natural exact-neighbor-count refinement of domination, and the 2021 enumerative work makes all-set counting an established object. The theorem extends the known balanced biclique enumeration to every complete multipartite graph, gives a compact structural classification, a closed polynomial, and the exact minimum \(\operatorname{fd}(G)=\min\{r,\min_i n_i\}\). This is a natural complete-family result rather than an arbitrary finite slice.

## Closest literature and limitations
The closest source is Alikhani–Safazadeh, arXiv:2107.10671v1, whose Section 2.2 counts fair dominating sets of \(K_{n,n}\). Caro–Hansberg–Henning, arXiv:1109.1150v1, supplies the definitions and the scalar \(K_{m,n}\) result. A terminology-equivalent connection to \([k,k]\)-domination appears in the \([1,2]\)-sets literature. A residual risk remains that an older or poorly indexed source states the arbitrary multipartite classification under another name.

Same-model review: passed. Independent audit: not yet performed.
