# Scientific assessment: bridge-linked clique Hilbert distortion

## Correctness — PASS

The claim is the exact least real-Hilbert metric distortion of two complete cliques of sizes \(m+1\) and \(n+1\) linked by a single bridge, for all integers \(m,n\ge2\), together with congruence rigidity and sharp size dependence. The lower bound applies to *every* Hilbert embedding: the within-class centroid variances have exact lower bounds, and the bridge and own-hub upper bounds impose a monotone upper envelope on cross-class squared distances. The unique root is forced by the graph distance three between leaves in opposite cliques. The proposed coordinates attain this root. The critical extra check is the strict inequality \(Q_A,Q_B>4\), verified analytically by comparing the defining root to \(2/\sqrt{4-a}\) and \(2/\sqrt{4-b}\); without it, the construction would not be valid. Equality in all lower-bound steps determines all distances, the orthogonal simplex arrangement and affine dimension. High-precision finite tests confirm the eight orbit inequalities and explicit coordinates but are not the proof for arbitrary clique sizes.

## Originality — PASS, with residual bibliographic risk

The closest inspected work is Robertson (2023), arXiv:2309.16070, giving an unrestricted semidefinite criterion for Hilbert distortion and examples on bipartite graphs and cubes; that criterion does not provide the explicit barbell root or rigidity classification. Duda–Wong (2024), arXiv:2408.08244, studies the same bridge-barbell graph but with quantum-walk Hamiltonians, not metric-embedding distortion. Baskoro–Obata (2023), arXiv:2311.03342, computes quadratic embedding constants for graphs with two *overlapping* maximal cliques, not the present bridge graph or its bi-Lipschitz Hilbert distortion. Accessible historical claims on double-star trees, two equilateral clusters, and one-hub clique bouquets were compared by their actual objects and implications: none states the new result. A double-star has leaf-pair graph distance two, whereas the present graph has distance one; its exact theorem cannot be applied by metric relabeling, and the opposite-hub constraints here require a separate sharp feasibility argument. Search absence cannot establish global priority; older metric-embedding classifications or graph-distance matrices may contain an equivalent expression.

## Mathematical value — PASS

The bridge-linked clique is a canonical dense network with a one-edge bottleneck and three graph-distance levels. The theorem gives an exact, nontrivial metric invariant for every pair of clique sizes; it classifies every optimal embedding, including its precise affine dimension; and it gives a sharp finite-size monotonicity and limiting extremum. The construction is not a mere substitution in a known result because, beyond deriving a lower envelope, its two-hop distances must be proved feasible uniformly across the entire parameter range. This distinguishes the bridge case from longer connecting paths, for which intermediate-hop constraints can become active. No downstream theorem is needed for the usefulness of a sharp structural classification.

## Limitations

The theorem is restricted to unweighted cliques connected by one bridge, integer \(m,n\ge2\), and real Hilbert targets of unrestricted dimension. It gives no claim for longer paths, weighted bridges, general clique trees or prescribed target dimensions. Numerical testing is finite. Historical priority remains conditional on the inspected literature, and no independent mathematical audit has been performed.

Self-review: passed. Independent audit: not yet performed.
