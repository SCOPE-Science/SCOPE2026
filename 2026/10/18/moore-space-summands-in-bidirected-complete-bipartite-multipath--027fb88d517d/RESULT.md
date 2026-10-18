# Moore-space summands in bidirected complete-bipartite multipath complexes

## Finding

Let \(G_n\) be the bidirected complete bipartite digraph on the vertex set \(\{u,v,w_0,\ldots,w_{n-1}\}\): for each \(i\) it has all four arcs \(u\to w_i\), \(w_i\to u\), \(v\to w_i\), and \(w_i\to v\), and no others. Let \(X_n=X(G_n)\) be its multipath complex, whose simplices are arc subsets forming a disjoint union of directed paths. Define the mod-two Moore space \(M(\mathbb Z/2,2)=S^2\cup_{\deg 2}e^3\). The following are integral homotopy equivalences:

\[
\begin{aligned}
X_3&\simeq S^1\vee\bigvee^{6}S^2,\\
X_4&\simeq \bigvee^{7}S^2\vee M(\mathbb Z/2,2),\\
X_5&\simeq M(\mathbb Z/2,2)\vee\bigvee^{31}S^3,\\
X_6&\simeq\bigvee^{169}S^3.
\end{aligned}
\]

In particular, \(\widetilde H_2(X_4;\mathbb Z)\cong\mathbb Z^7\oplus\mathbb Z/2\), and \(\widetilde H_2(X_5;\mathbb Z)\cong\mathbb Z/2\). These supply explicit unstable dynamical modules with torsion: \(G_4\) and \(G_5\) are themselves unstable dynamical modules, contrary to the torsion-implies-stability conjecture stated in the introduction to Caputi–Collari–Di Trani–Smith (2022). No assertion is made for \(n\) outside the four stated values.

## Assumptions and scope

The graph is finite, simple as a digraph (opposite arcs are permitted), and has precisely the specified arcs. A set of arcs is a multipath exactly when each vertex has indegree and outdegree at most one *within that set* and there is no directed cycle. The empty arc set is included as the augmented empty simplex. Homology is over \(\mathbb Z\) unless explicitly marked otherwise. The calculation is exhaustive for \(n\in\{3,4,5,6\}\), and depends neither on a guessed periodicity nor on extrapolation from sampled parameters. The principal classification is in combinatorial algebraic topology, MSC 55U10.

## Proof

**1. Exhaustive face construction.** Each of the two vertices \(u,v\) supports at most one selected incoming and one selected outgoing arc. Every graph arc meets one of these vertices, so a multipath contains at most four arcs. Index the arcs in the order
\[
( u\to w_i,\ w_i\to u,\ v\to w_i,\ w_i\to v ),\qquad 0\le i<n.
\]
Enumerating all arc subsets of size at most four and checking the indegree, outdegree and acyclicity predicates therefore enumerates *every* simplex, not only a truncation. The total face counts including the empty simplex are respectively \(115,313,711,1417\), and the nonempty face vectors by dimensions \(0,1,2,3\) are

```
n=3  (12, 42,  48,  12)
n=4  (16, 80, 144,  72)
n=5  (20,130, 320, 240)
n=6  (24,192, 600, 600)
```

**2. An explicit acyclic discrete-Morse matching.** Start with the augmented face poset. For each of the four arc-types in order, and within each type for the leaves in increasing order, pair every still-unpaired face lacking that arc with its still-unpaired coface formed by adding the arc. Remove each paired pair before continuing to the next stage. Each pair differs in exactly one arc, and no face appears in more than one pair. The verifier constructs the complete face-cover Hasse graph, directs matched incidences upward and all others downward, and performs an exhaustive directed topological sort. Every face is processed, proving no directed cycle exists. The four cases have, respectively, \(54,152,339,624\) augmented matching pairs and \(288,896,2200,4608\) Hasse incidences. The residual critical cells, with dimensions as exponents, are
\[
\begin{array}{c|c}
n&\text{augmented critical cells}\\\hline
3&1\text{ of dimension }1,\ 6\text{ of dimension }2\\
4&8\text{ of dimension }2,\ 1\text{ of dimension }3\\
5&1\text{ of dimension }2,\ 32\text{ of dimension }3\\
6&169\text{ of dimension }3.
\end{array}
\]
Exactly one augmented pair has the empty face as its lower member. Omitting that pair yields an ordinary Morse matching with exactly one additional critical vertex and no other changes. The finite acyclicity and counting assertions are verified by the bundled standalone scripts.

**3. Integral attaching maps, not just Betti numbers.** Orient each simplex by its increasing list of arc indices, so deleting the \(j\)-th element contributes \((-1)^j\) to its boundary. Successive integral cancellation of all matched face pairs has unit incidence coefficient at each pivot. Equivalently, recursively project lower cells through the other facets of their matched upper cells along the acyclic gradient graph. Both algorithms compute the same integral Morse boundary. In increasing critical-face order, the only potentially nonzero boundary is:

- \(n=3\): the \(1\)-by-\(6\) matrix is zero;
- \(n=4\): the \(8\)-by-\(1\) column is \((2,-2,0,2,2,-2,-2,0)^{\mathsf T}\), with content (gcd) \(2\);
- \(n=5\): the \(1\)-by-\(32\) row has content \(2\), with \(26\) nonzero entries;
- \(n=6\): the zero \(0\)-by-\(169\) matrix.

The full \(n=5\) row, independently obtainable using `verify_integer_cancellation.py`, is

```
[0,-2,2,-2,0,2,2,-2,-2,2,-2,2,-2,4,4,6,
 -2,2,4,-4,4,0,0,-4,-2,4,-2,0,4,2,2,0]
```

These computations are exact integer arithmetic, not a floating-point or finite-field approximation. The two programs implement separately the signed gradient projection and integral cellular chain cancellation; a third field-rank calculation independently corroborated the mod-two versus odd-prime torsion distinction.

**4. Recover the homotopy types.** The ordinary Morse CW complexes are connected with one \(0\)-cell and the higher-dimensional cells listed above. For \(n=3\), the unique \(1\)-cell gives \(S^1\); each \(2\)-cell attaches by a map \(S^1\to S^1\) of degree zero, hence null-homotopically. For \(n=4\), there are eight \(2\)-cells and one \(3\)-cell. The attaching map represents the displayed vector in \(\pi_2(\bigvee^8S^2)\cong\mathbb Z^8\). A unimodular change of basis turns it into \((2,0,\ldots,0)\), so the cofiber splits as the asserted Moore space and seven \(2\)-spheres. For \(n=5\), the \(32\) three-cell attaching maps into the single two-sphere have degrees given by the displayed row; a unimodular change of basis in the attaching spheres similarly reduces them to one map of degree \(2\) and \(31\) null maps. For \(n=6\) there are no positive-dimensional cells below dimension three, so the complex is a wedge of \(169\) three-spheres. Unimodular changes are realized by homotopy equivalences of wedges of simply connected spheres; the corresponding cofiber types are preserved.

**5. Unstable-module consequence.** In the terminology of Caputi–Collari–Di Trani–Smith (2022), a dynamical region must contain *every* directed cycle that contains one of its edges. Start with any arc of \(G_n\). By graph symmetries assume it is \(u\to w_i\). The oriented two-cycle forces \(w_i\to u\). For each \(j\ne i\), the oriented four-cycle \(u\to w_i\to v\to w_j\to u\) forces \(w_i\to v\), \(v\to w_j\), and \(w_j\to u\); the corresponding two-cycles force \(w_j\to v\) and \(u\to w_j\). Finally a four-cycle through \(u\to w_j\) and \(w_i\) forces \(v\to w_i\). Hence any nonempty dynamical region contains every arc of \(G_n\), and the full digraph is its sole dynamical module. All vertices have positive indegree and outdegree, so that module is unstable. The two torsion cases therefore violate the specific conjectured implication that torsion forces a dynamical module to be stable.

## Verification

Run the two bundled standard-library Python scripts independently:

```
python3 verify_bidirected_k2n.py
python3 verify_integer_cancellation.py
```

The first checks the exhaustive face predicates and face closure, all matching pairs, all directed Hasse edges and acyclicity, integral gradient-path boundary content, and exact reduced mod-two Betti ranks. The second independently rebuilds faces and performs direct signed integral unit-pivot chain cancellations. Both complete successfully with outputs ending in `VERIFY_OK` and `CANCEL_OK` for each of the four widths. Their reported integral boundary matrix shapes and contents are respectively \((1,6;0)\), \((8,1;2)\), \((1,32;2)\), and \((0,169;0)\). The above finite exhaustiveness argument justifies treating the computations as proof of each stated finite case. The graph-cycle argument in Step 5 is uniform for every \(n\ge2\), but the homotopy calculations are not.

## Relationship to prior work

Caputi, Collari, and Smith (2026) develop the topology and homology of bidirected *paths and polygons* and explicitly leave their polygonal wedge-of-spheres question open; these are different host graphs from \(G_n\). Caputi, Collari, Di Trani, and Smith (2022) study the one-way complete bipartite digraph, whose directed edges go only from one bipartition class to the other, and derive chessboard-complex Euler characteristics; this does not include the bidirected digraph here. Their earlier proposed torsion-implies-stability statement is contradicted by the specified examples, since those graphs are unstable modules. Caputi, Collari, and Ramos (2024) prove general bounded-genus torsion bounds and match multipath with matching complexes when the digraph has **no oriented cycles**; neither theorem determines the present integral homotopy types for strongly connected bidirected graphs. Previously documented graph Morse complexes of complete bipartite graphs concern complexes of discrete gradient fields, which are not multipath complexes. Other multipath complexes were already known to possess torsion; no first-ever-torsion claim is made.

## Limitations

The four classifications do not determine \(X_n\) for \(n\ge7\) or prove any periodic pattern; no general finite or infinite parameter formula is asserted. The full homotopy equivalences rely on the exact oriented cellular boundary and homotopy-group arguments, not just on the mod-two Betti numbers. A search of accessible literature and mathematical indexes identified no matching calculation, but literature coverage is not a proof of absolute novelty; unindexed, later or unpublished equivalent results remain possible. The only conjecture addressed is the explicit torsion/stability implication in the 2022 paper; the 2026 bidirectional-polygon conjecture is neither confirmed nor refuted by these nonpolygonal graphs.

## References

1. L. Caputi, C. Collari, J. P. Smith, *Multipath complexes of bidirectional polygonal digraphs*, arXiv:2601.05670v1, first posted 2026-01-09. https://arxiv.org/abs/2601.05670
2. L. Caputi, C. Collari, S. Di Trani, J. P. Smith, *On the homotopy type of multipath complexes*, arXiv:2208.04656v1, first posted 2022-08-09; published in *Mathematika* 70 (2024), e12235. https://arxiv.org/abs/2208.04656
3. L. Caputi, C. Collari, E. Ramos, *The weak categorical quiver minor theorem and its applications: matchings, multipaths, and magnitude cohomology*, arXiv:2401.01248v1, first posted 2024-01-02. https://arxiv.org/abs/2401.01248
