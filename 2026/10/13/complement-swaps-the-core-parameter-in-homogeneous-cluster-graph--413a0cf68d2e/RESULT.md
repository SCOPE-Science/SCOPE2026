# Complement swaps the core parameter in homogeneous cluster graphs
## Finding
For \(m,n\in\{2,3,\ldots,\aleph_0\}\), with at least one of \(m,n\) equal to \(\aleph_0\), let \(C_{m,n}\) be the disjoint union of \(m\) copies of the complete graph \(K_n\), and let \(D_{m,n}=\overline{C_{m,n}}\). These are the complementary homogeneous cluster/multipartite graphs.

The two structures have exactly the same automorphism group as a permutation group on their common vertex set:
\[
\operatorname{Aut}(C_{m,n})=\operatorname{Aut}(D_{m,n}).
\]
Nevertheless, complementation swaps the parameter controlling the model-complete core:
\[
\operatorname{core}(C_{m,n})\cong K_n,\qquad
\operatorname{core}(D_{m,n})\cong K_m,
\]
where \(K_{\aleph_0}\) denotes the countable complete graph. Thus when exactly one of \(m,n\) is finite, two homogeneous structures with the same oligomorphic permutation group have model-complete cores of different cardinality, one finite and one countably infinite.

The same swap is visible in the endomorphism image-cardinality spectrum. For \(C_{m,n}\), finite-image endomorphisms exist exactly when \(n<\aleph_0\). If \(m=\aleph_0\) and \(n<\aleph_0\), their finite image sizes are precisely
\[
n,2n,3n,\ldots.
\]
For \(D_{m,n}\), finite-image endomorphisms exist exactly when \(m<\aleph_0\). If \(m<\aleph_0\) and \(n=\aleph_0\), their finite image sizes are precisely
\[
m,m+1,m+2,\ldots.
\]
If \(m=n=\aleph_0\), every endomorphism of either graph has countably infinite image.

The common injective ordered-\(k\)-tuple orbit count is the number of set partitions of \([k]\) into at most \(m\) blocks, each of size at most \(n\). Consequently the entire automorphism-orbit profile is shared even though the core and finite-rank endomorphism behavior can differ maximally.

## Assumptions and scope
Graphs are simple and loopless. A graph homomorphism preserves edges but need not preserve nonedges. The parameters \(m,n\) are either integers at least \(2\) or \(\aleph_0\), and at least one is \(\aleph_0\), so the structures are countably infinite. The word core refers to the unique model-complete core in the sense of countably categorical structures.

For the orbit statement, an injective ordered \(k\)-tuple is classified by the partition of its coordinate positions according to which clique of \(C_{m,n}\), equivalently which part of \(D_{m,n}\), contains them. The constraints are at most \(m\) blocks and block size at most \(n\), with the corresponding condition omitted when a parameter is \(\aleph_0\).

## Proof
Complementation does not change which permutations preserve a graph, so
\[
\operatorname{Aut}(C_{m,n})=\operatorname{Aut}(D_{m,n}).
\]
Equivalently, both groups permute the \(m\) blocks and independently permute the \(n\) vertices inside each block. Therefore their tuple orbits coincide. For an injective ordered \(k\)-tuple, the orbit invariant is exactly the coordinate partition by blocks, and homogeneity within and between blocks realizes every partition allowed by the two cardinality bounds.

Consider an endomorphism \(f\) of \(C_{m,n}\). The restriction of \(f\) to any source clique \(K_n\) is injective, because adjacent vertices cannot be identified in a loopless target. Its image lies in a single target clique. If \(n<\aleph_0\), that restriction is therefore a bijection onto an entire target \(K_n\). Hence a finite image is a union of \(r\) target cliques and has size \(rn\). When \(m=\aleph_0\), every positive finite \(r\) can be realized by routing all source cliques onto exactly \(r\) target cliques, while using infinitely many target cliques gives countably infinite image. If \(n=\aleph_0\), already the image of one source clique is countably infinite, so every endomorphism has image size \(\aleph_0\).

Now consider an endomorphism \(g\) of \(D_{m,n}\). Vertices belonging to distinct source parts are adjacent, so their images must be distinct and lie in distinct target parts. Thus the sets of target parts used by two distinct source parts are disjoint. If \(m=\aleph_0\), countably many nonempty source parts force countably many distinct image vertices, so every endomorphism has image size \(\aleph_0\). If \(m<\aleph_0\) and \(n=\aleph_0\), the \(m\) nonempty, pairwise disjoint target-part supports must each contain exactly one target part. Inside a source part there are no edges, so its image can have any prescribed positive finite cardinality, or countably infinite cardinality, within its assigned target part. Therefore every finite image size at least \(m\) occurs, and no smaller one can occur.

Finally, \(C_{m,n}\) is homomorphically equivalent to \(K_n\): map every component into one fixed component and embed one component back. Similarly, \(D_{m,n}\) is homomorphically equivalent to \(K_m\): collapse each part to one vertex and embed \(K_m\) by choosing one vertex from each part. Complete graphs have only injective endomorphisms, hence are cores. Bodirsky's uniqueness theorem for model-complete cores of countably categorical structures identifies these representatives as the model-complete cores.

## Verification
The accompanying verifier performs exact finite checks on the approximants \(mK_n\) and their complements for \((m,n)=(2,2),(2,3),(3,2)\). It exhaustively enumerates all self-maps, checks the predicted image-rank spectra, constructs the full wreath-product automorphism groups, verifies automorphism preservation for both a graph and its complement, and compares brute-force injective tuple-orbit counts with the restricted set-partition count through arity \(4\). It reports:
\[
\texttt{VERIFY\_OK 3717 exact assertions}.
\]
These finite computations check the combinatorial mechanisms used in the proof; the infinite statements themselves follow from the structural arguments above rather than from extrapolation.

## Relationship to prior work
Coleman's 2018 classification determines the homomorphism-homogeneity behavior of the countable homogeneous undirected graphs and explicitly treats disjoint unions of equal cliques and their complements. In particular, its Section 5 separates the maximal homomorphism-homogeneity classes of these complementary families. The present result asks a different invariant question: what information about endomorphism image ranks and the model-complete core survives after the automorphism group is fixed?

Bodirsky proved that every countably categorical structure is homomorphically equivalent to a unique model-complete core, finite or countably categorical. Applying that framework here turns the elementary homomorphisms between the cluster and complete graphs into an exact core identification.

Targeted searches located the homogeneous-graph classifications, general work on homomorphism-homogeneity and endomorphism monoids, and the general model-complete-core theorem, but did not locate the parameter-swap statement, the complete finite-image spectra above, or the combined same-automorphism-group/core-cardinality contrast. The derivation is short, so an uncatalogued-folklore risk remains.

## Limitations
The result concerns the equal-block homogeneous cluster family and its complements; it does not classify endomorphism monoids of arbitrary homogeneous graphs. It records image cardinalities, not the full algebraic structure of the endomorphism monoids. When \(m=n=\aleph_0\), the core and image-cardinality invariants considered here do not distinguish the complementary pair. The originality assessment is literature-search based and cannot rule out an equivalent observation stated in different terminology.

## References
1. Thomas D. H. Coleman, “Two Fraïssé-style theorems for homomorphism-homogeneous relational structures,” arXiv:1812.01934, first submitted 5 December 2018.
2. Manuel Bodirsky, “Cores of Countably Categorical Structures,” arXiv:cs/0612069; Logical Methods in Computer Science 3(1), 2007.
3. A. H. Lachlan and R. E. Woodrow, “Countable ultrahomogeneous undirected graphs,” Transactions of the American Mathematical Society 262 (1980), 51–94.
4. Peter J. Cameron and Jaroslav Nešetřil, “Homomorphism-homogeneous relational structures,” Combinatorics, Probability and Computing 15 (2006), 91–103.
