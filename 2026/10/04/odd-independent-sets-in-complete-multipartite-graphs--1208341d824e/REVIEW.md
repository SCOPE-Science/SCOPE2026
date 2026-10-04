# Review: Odd independent sets in complete multipartite graphs

## Correctness
PASS. A nonempty independent set in a complete multipartite graph lies in one part. Vertices in that same part see zero selected vertices, while every vertex in every other part sees all selected vertices. Hence the odd-independence condition is equivalent to odd cardinality. The counting polynomial and the maximum-size formula follow immediately from this exact classification. The exhaustive verifier independently checks the defining condition for all complete-multipartite types through order \(11\).

## Originality
PASS. The initiating paper arXiv:2509.20763v1 defines \(\alpha_{\mathrm{od}}\), treats numerous classical classes, and explicitly asks for understanding of equality \(\alpha_{\mathrm{od}}(G)=\alpha(G)\). Its inspected full text has no “multipartite” occurrence. Its Proposition 2 covers bipartite graphs with all degrees odd, with exact equality only under an additional odd-regular hypothesis; that does not imply the arbitrary complete-bipartite or arbitrary complete-multipartite formula here. Targeted web searches and four semantic-index searches under odd independence, odd independent sets, complete bipartite, and complete multipartite terminology found no covering theorem. The closest indexed complete-multipartite record concerns ordinary odd chromatic number, a different invariant.

## Value
PASS. This is a complete structural classification, not an isolated parameter computation: it enumerates every odd independent set in every complete multipartite graph, yields a closed generating polynomial, and exactly resolves the initiating paper’s equality question \(\alpha_{\mathrm{od}}=\alpha\) on a broad classical graph family. The result includes irregular complete bipartite graphs not covered by the paper’s odd-regular equality proposition and gives reusable exact test cases for the new invariant.

## Closest literature and limitations
The closest primary source is Caro–Petruševski–Škrekovski–Tuza, arXiv:2509.20763v1. Its general odd-degree bipartite proposition is compatible with the present formula but strictly weaker on complete bipartite graphs. No inspected source or indexed result implied the full complete-multipartite classification or enumerator. The main residual risk is an older equivalent observation phrased before the invariant received its current name.

Same-model review: passed. Independent audit: not yet performed.
