# Review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

The main argument separates the two biparts of the projective nonincidence graph. A point vertex can newly dominate only hyperplane vertices, so the legality of a point in an interleaved total dominating sequence is unaffected by previously selected hyperplane vertices. After points \(P_1,\ldots,P_i\) have been selected, the hyperplanes still undominated by points are exactly those containing \(P_1+\cdots+P_i\). Hence a new point is legal exactly when it increases this span, and the selected points dominate every hyperplane exactly when the span becomes all of \(V\). This forces exactly \(d\) point vertices.

The hyperplane argument is the dual statement. After hyperplanes \(H_1,\ldots,H_i\) have been selected, the undominated points are exactly the one-dimensional subspaces of \(H_1\cap\cdots\cap H_i\). A legal new hyperplane decreases the intersection dimension by exactly one, and total domination of the point side is equivalent to zero final intersection. This forces exactly \(d\) hyperplane vertices. Therefore every total dominating sequence has length \(2d\). A basis and dual basis supply an explicit sequence, so existence is not merely inferred from the forcing argument.

The degree count follows from the Gaussian counts \([d]_q-[d-1]_q=q^{d-1}\). Connectedness follows because any two projective points admit a common nonincident hyperplane, while every hyperplane has an outside point. The false-twin argument separates distinct points by a hyperplane containing exactly one, and dually for hyperplanes. The recursive deletion isomorphism follows from \(V=P\oplus H\) on every nonincidence edge and the bijection \(K\mapsto K\cap H\).

A finite verification independently reconstructs the graphs over several prime fields and exhaustively checks the span/legality equivalence for all point subsets in the stated small cases. These computations agree with the theorem and are corroborative rather than a substitute for the proof.

## Originality

Brešar--Henning--Rall introduced Grundy total domination and its hypergraph covering connection. Dravec--Jakovac--Kos--Marc characterized the bipartite total-4 case and regular bipartite total-6 graphs, with the latter tied to projective planes. Their projective-plane family agrees with the \(d=3\) specialization of the present construction. Bahadır--Gözüpek--Doğan proved that odd total-uniformity is impossible, supplied a connected total-8 example, and explicitly stated that they believed connected total \(k\)-uniform graphs exist for every larger even \(k\), leaving their construction as an open research direction.

Point-hyperplane nonincidence graphs of projective geometries are classical graph objects, so no novelty is claimed for the graphs themselves. Searches using total \(k\)-uniform graphs, equal total and Grundy total domination, total 10-/12-uniform graphs, point-hyperplane nonincidence/non-incidence graphs, finite projective geometry, and the hypergraph covering terminology did not locate the arbitrary-dimensional total-\(2d\) theorem or a completed connected existence spectrum. Subsequent literature located during current-status checking concerned other Grundy-total-domination bounds, products, or zero-forcing relations rather than this existence problem.

Originality is therefore assessed as PASS only to the best of our knowledge. The principal residual risk is a differently indexed finite-geometry, design-theory, thesis, or hypergraph-covering source that observes the same arbitrary-dimensional construction without using the term total \(k\)-uniform.

## Value

The result closes a concrete published existence question rather than adding one isolated parameter value. It gives a single uniform family for every even parameter, and the known nonexistence for odd parameters then yields the exact connected existence spectrum. The family is additionally regular, false-twin-free, explicit over every finite field, and recursively compatible with the standard two-step reduction for total-uniform graphs. Its \(d=2\) and \(d=3\) cases recover the known crown-graph and projective-plane phenomena, explaining them as the first members of one higher-dimensional mechanism.

## Limitations

The result does not classify all total \(k\)-uniform graphs, does not establish minimum order or minimum degree for a given \(k\), and does not claim novelty for projective nonincidence graphs as graph objects. The finite verification treats prime fields only, whereas the proof covers all prime powers. Originality remains subject to the indexing risk described above.
