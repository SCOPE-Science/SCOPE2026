# Review of Weight enumerator of all minus dominating functions on complete multipartite graphs

## Correctness
PASS. For \(v\in V_i\), the closed-neighborhood sum is exactly \(w-s_i+f(v)\). The condition over an entire part is therefore equivalent to checking the minimum label \(\mu_i\), giving \(w-s_i+\mu_i\ge1\). The three cases in \(P_{n,w}(y)\) partition all part-labelings according to whether the minimum label is \(-1\), \(0\), or \(+1\). Coefficient extraction then enforces the global weight. The proof that \(w>0\) is explicit. The verifier independently checks the literal definition and every coefficient through order \(9\).

## Originality
PASS, with residual bibliographic risk. Liang's arXiv:1205.0343v1 was read in full in the relevant section. The paper explicitly says its goal is to determine the three scalar parameters and Theorem 3 proves only the complete-multipartite value of \(\gamma^-(G)\). Zelinka's 2006 paper is a complete-bipartite scalar predecessor. Searches for “minus domination polynomial,” “minus dominating functions weight distribution complete multipartite,” and equivalent all-function language returned no source stating the present coefficient enumerator. Semantic-index searches likewise returned only different domination variants or unrelated complete-multipartite results. Failed search is not treated as proof of novelty; the residual risk is an older or poorly indexed equivalent census.

## Value
PASS. The published complete-multipartite result compresses the feasible family to one minimum number, while the present theorem classifies every feasible \(\{-1,0,1\}\)-labeling and provides every weight multiplicity. This is a natural complete census of a classical domination variant and can answer counting, random-labeling, and coefficient questions without re-solving the neighborhood constraints for each graph.

Same-model review: passed. Independent audit: not yet performed.
