# Path extremality through eight vertices and an eight-vertex prime-core cutoff
## Finding
For every finite simple graph \(G\) on \(1\le n\le 8\) vertices and every \(0\le k\le n\), \(z(G;k)\le z(P_n;k)\), where \(z(G;k)\) is the number of zero-forcing sets of cardinality \(k\). Consequently, every connected graph whose canonical split decomposition has exactly one prime bag of size at most \(8\) is path-extremal.

For reference, the exact path coefficient vector at order eight is
\[
(z(P_8;0),\ldots,z(P_8;8))=(0,2,18,52,70,56,28,8,1).
\]

## Assumptions and scope
All graphs are finite, simple, and undirected. A zero-forcing process starts from a blue set \(S\); a blue vertex having exactly one white neighbor forces that neighbor blue. A set is zero forcing if repeated legal forces make every vertex blue. The coefficient \(z(G;k)\) counts zero-forcing sets \(S\subseteq V(G)\) with \(|S|=k\). A graph is path-extremal when \(z(G;k)\le z(P_n;k)\) for every \(k\), where \(n=|V(G)|\).

The finite statement covers all isomorphism classes, connected or disconnected, of orders one through eight. The split-decomposition consequence is for connected graphs in the class with exactly one prime bag, as in German's Corollary 4.

## Proof
For each graph in the finite census and for each subset \(S\subseteq V(G)\), the forcing closure is computed exactly. At each step, every currently blue vertex with exactly one white neighbor contributes that unique neighbor; the process stops only at a fixed point. Thus the test is equivalent to the definition of zero forcing, with no search heuristic or probabilistic step. Grouping successful sets by cardinality gives every coefficient \(z(G;k)\) exactly.

Orders at most seven use the complete unlabeled graph atlas. For order eight, begin with every unlabeled graph \(H\) on seven vertices and add one new vertex with each of its \(2^7\) possible neighborhoods. Every eight-vertex graph appears in this list: delete any vertex of an arbitrary eight-vertex graph, identify the remaining graph with its seven-vertex representative, and restore the deleted vertex by its neighborhood. Exact isomorphism testing removes duplicates and leaves 12,346 classes, matching the standard independent unlabeled-graph count at order eight.

Exhaustive forcing then gives \(z(G;k)\le z(P_n;k)\) for every census graph and every coefficient. Hence the finite claim follows.

German proves that if every induced subgraph of every split-prime graph on at most \(m\) vertices is path-extremal, then every connected graph whose canonical split decomposition has exactly one prime bag of size at most \(m\) is path-extremal. Taking \(m=8\), the premise holds because the finite verification covers every graph on at most eight vertices, including all such induced subgraphs. This proves the stated infinite-class consequence.

## Verification
`artifacts/verify.py` is a standard-library verifier for the embedded census `artifacts/graphs_upto8.g6`. It decodes every graph, enumerates all vertex subsets, recomputes the zero-forcing closure, checks every coefficient against the path coefficient vector, and checks the expected census counts. The replay covers 13,598 unlabeled graphs and 3,305,498 starting sets. It reports exactly one graph at each order with the full path coefficient vector and ends with `ALL CHECKS PASSED`.

The order-eight census construction is documented in `artifacts/generate_order8.py` and `artifacts/CENSUS_NOTES.md`. The generated order-eight graph6 data have SHA-256 `d6bba0a339f03ea5ae2a9035c09e73e9852e4d8e4614578f8ca82d113d9c96cc`.

## Relationship to prior work
Boyer, Brimkov, English, Ferrero, Keller, Kirsch, Phillips, Reff, and Smith formulated the coefficientwise path-extremal conjecture for the zero-forcing polynomial. Curtis, Gan, and Haddock restated the coefficient form and proved partial results under additional graph hypotheses.

German's 2026 preprint proves the conjecture for distance-hereditary graphs and gives a split-decomposition reduction. Its Corollary 4 explicitly reduces the one-prime-bag class to finite verification of bounded-order split-prime bases, but it does not supply a cutoff-eight verification. The result here executes that finite step through order eight and therefore converts the conditional reduction into an unconditional statement for prime bags of size at most eight.

A separate recent result on the zero-forcing polynomial proves that no universal second-best nonpath tree exists in the coefficientwise order. That statement concerns comparisons among trees and neither implies the all-graph order-eight verification nor the prime-bag consequence here.

## Limitations
The computation proves the conjecture only through order eight and does not imply the conjecture for arbitrary graphs. The infinite consequence uses German's stated split-decomposition reduction and is limited to connected graphs with exactly one prime bag of size at most eight. The order-eight census generation used exact isomorphism testing in NetworkX; the embedded verifier independently rechecks every forcing coefficient on the finalized census but does not itself reimplement graph isomorphism canonization.

## References
1. S. German, *The Path-Extremal Conjecture for Zero Forcing: Distance-Hereditary Graphs and a Split-Decomposition Reduction*, arXiv:2605.10836v1, 2026.
2. B. Boyer et al., *The zero forcing polynomial of a graph*, arXiv:1801.08910; Discrete Applied Mathematics 258 (2019), 35–48.
3. S. Curtis, L. Gan, and J. Haddock, *Zero Forcing with Random Sets*, arXiv:2208.12899.
4. B. McKay, standard graph6 census of unlabeled simple graphs; the order-eight census contains 12,346 graphs.
