# Perfect Roman domination of crown graphs
## Finding
For every integer \(n\ge3\), let \(\operatorname{Cr}_n=K_{n,n}-M\) be the crown graph obtained from the complete bipartite graph with bipartition \(A=\{a_1,\ldots,a_n\}\), \(B=\{b_1,\ldots,b_n\}\) by deleting the perfect matching \(M=\{a_i b_i:1\le i\le n\}\). Then the perfect Roman domination number is \[\gamma_R^p(\operatorname{Cr}_n)=4.\] Moreover, the minimum perfect Roman dominating functions are exactly the \(n\) functions obtained by choosing one deleted matching pair \(a_i,b_i\), assigning both vertices value \(2\), and assigning value \(0\) to every other vertex. Thus every minimum function has no value-\(1\) vertices and the number of minimum functions is exactly \(n\).

## Assumptions and scope
All graphs are finite, simple, and undirected. For an integer \(n\ge3\), the crown graph \(\operatorname{Cr}_n\) has bipartition
\[
A=\{a_1,\ldots,a_n\},\qquad B=\{b_1,\ldots,b_n\},
\]
and edges \(a_i b_j\) exactly when \(i\ne j\). Equivalently,
\[
\operatorname{Cr}_n=K_{n,n}-\{a_i b_i:1\le i\le n\}.
\]

A perfect Roman dominating function is a map \(f:V(G)\to\{0,1,2\}\) such that every vertex assigned value \(0\) has exactly one neighbor assigned value \(2\). Its weight is \(w(f)=\sum_{v\in V(G)}f(v)\), and \(\gamma_R^p(G)\) is the minimum possible weight.

## Proof
Fix an index \(i\). Assign value \(2\) to \(a_i\) and \(b_i\), and value \(0\) to every other vertex. Since \(a_i\) and \(b_i\) are the unique nonadjacent cross-part pair, every vertex \(a_j\) with \(j\ne i\) is adjacent to \(b_i\), and every vertex \(b_j\) with \(j\ne i\) is adjacent to \(a_i\). No zero vertex sees the other value-\(2\) vertex because vertices inside one bipartition class are nonadjacent. Thus every zero vertex has exactly one value-\(2\) neighbor, so
\[
\gamma_R^p(\operatorname{Cr}_n)\le4.
\]

We prove that no perfect Roman dominating function has weight at most \(3\). Such a function contains at most one vertex of value \(2\). If it contains no value-\(2\) vertex, then every vertex must have positive value, so its weight is at least \(2n>3\).

Suppose exactly one vertex has value \(2\), say \(a_i\). Every vertex of \(A\setminus\{a_i\}\) has no value-\(2\) neighbor because all its neighbors lie in \(B\). Hence each such vertex must be positive, forcing weight at least \(2+(n-1)\ge4\). Therefore no weight at most \(3\) is feasible, and \(\gamma_R^p(\operatorname{Cr}_n)=4\).

Let \(f\) now be a minimum function of weight \(4\). If it had exactly one value-\(2\) vertex \(a_i\), then all \(n-1\) other vertices of \(A\) would have value at least \(1\). For \(n\ge4\), this already gives weight at least \(n+1\ge5\). For \(n=3\), equality with weight \(4\) would force all vertices of \(B\) to have value \(0\), but then \(b_i\), which is nonadjacent to \(a_i\), would have no value-\(2\) neighbor. Thus every minimum function contains exactly two value-\(2\) vertices and no value-\(1\) vertices.

The two value-\(2\) vertices cannot lie in the same bipartition class, because then every zero vertex in that class would have no value-\(2\) neighbor. Write them as \(a_i\) and \(b_j\). If \(i\ne j\), then the zero vertex \(a_j\) is nonadjacent to \(b_j\) and hence has no value-\(2\) neighbor, a contradiction. Therefore \(i=j\). Conversely, every deleted matched pair \(a_i,b_i\) gives the valid function constructed above. Hence there are exactly \(n\) minimum functions.

## Verification
The included verifier constructs \(\operatorname{Cr}_n\) directly and tests the perfect Roman condition from the adjacency relation for every labeling in \(\{0,1,2\}^{2n}\).

For each \(3\le n\le7\), it independently determines the true minimum weight, collects every minimum function, and compares the complete minimum set with the deleted-matching-pair classification.

## Relationship to prior work
The 2018 paper on perfect Roman domination in regular graphs develops general upper bounds for regular graphs using packings. Its general construction assigns value \(2\) to a packing, value \(0\) to its boundary, and value \(1\) farther away. In a crown graph, a deleted matched pair is a packing of size two whose boundary is every other vertex, so that construction immediately supplies the weight-\(4\) candidate. The cited paper does not provide the crown-graph lower bound or classify its minimum functions; targeted full-text searches found no occurrence of “crown” or “bipartite.”

The 2019 algorithmic paper on perfect Roman domination proves hardness for bipartite graphs and algorithms for several structured graph classes. Targeted searchable-text checks found no crown, deleted-matching, or complete-bipartite-minus-matching formula. Thus the present result identifies the exact optimum and every optimum on a standard dense regular bipartite family.

## Limitations
The theorem concerns the crown graph \(K_{n,n}-M\) for \(n\ge3\). It does not claim an analogous formula for arbitrary regular bipartite graphs or for complete bipartite graphs with a nonperfect matching deleted. The finite computation is corroborative only; the all-parameter statement follows from the proof. A differently named or non-indexed exact crown-graph treatment could have escaped the searches.

## References
1. M. A. Henning, W. F. Klostermeyer, “Perfect Roman domination in regular graphs,” Applicable Analysis and Discrete Mathematics 12(1) (2018), 143–152, DOI 10.2298/AADM1801143H.
2. S. Banerjee, J. Mark Keil, D. Pradhan, “Perfect Roman domination in graphs,” Theoretical Computer Science 796 (2019), 1–21, DOI 10.1016/j.tcs.2019.08.017.
