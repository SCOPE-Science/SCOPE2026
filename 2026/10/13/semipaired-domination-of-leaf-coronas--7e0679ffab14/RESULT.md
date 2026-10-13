# Semipaired domination of leaf coronas
## Finding
Let \(G\) be any connected graph of order \(n\ge2\). Form the leaf corona \(G\circ K_1\) by adjoining to every vertex \(v\in V(G)\) a private leaf \(v^\prime\) adjacent only to \(v\).

Then
\[
\gamma_{pr2}(G\circ K_1)=2\left\lceil\frac n2\right\rceil.
\]
Equivalently,
\[
\gamma_{pr2}(G\circ K_1)=
\begin{cases}
n,&n\text{ even},\\
n+1,&n\text{ odd}.
\end{cases}
\]

The result is constructive. Choose any spanning tree \(T\) of \(G\). The square \(T^2\) has a matching saturating every vertex when \(n\) is even and all but one vertex when \(n\) is odd. For even \(n\), the original vertex set \(V(G)\) itself is therefore semipaired. For odd \(n\), if \(u\) is the unmatched original vertex, then
\[
V(G)\cup\{u^\prime\}
\]
is semipaired by pairing \(u\) with \(u^\prime\).

## Assumptions and scope
A semipaired dominating set of an isolate-free graph is a dominating set \(D\) of even cardinality that can be partitioned into pairs \(\{x,y\}\) satisfying
\[
d(x,y)\le2.
\]
The semipaired domination number \(\gamma_{pr2}\) is the minimum cardinality of such a set.

The theorem assumes only that \(G\) is finite, simple, connected, and has at least two vertices. No degree, planarity, chordality, or matching hypothesis on \(G\) is required.

## Proof
For each \(v\in V(G)\), let \(v^\prime\) denote its private leaf in \(G\circ K_1\). Since \(v^\prime\) has the unique neighbor \(v\), every dominating set \(D\) of the corona must contain at least one vertex from the pair
\[
\{v,v^\prime\}.
\]
These \(n\) pairs are disjoint, so
\[
|D|\ge n.
\]
Every semipaired dominating set has even cardinality, because it is partitioned into two-element blocks. Hence
\[
\gamma_{pr2}(G\circ K_1)\ge 2\left\lceil\frac n2\right\rceil.
\tag{1}
\]

It remains to construct a semipaired dominating set attaining the lower bound.

We use the following matching lemma.

**Lemma.** If \(T\) is a tree of order \(n\ge2\), then \(T^2\) has a matching of size \(\lfloor n/2\rfloor\).

To prove the lemma, repeatedly choose an endpoint \(x\) of a longest path in the current tree, and let \(y\) be its neighbor. Every neighbor of \(y\) except possibly the neighbor toward the interior of the longest path is a leaf. If \(y\) has at least two leaf neighbors, choose two of them and match them; their distance in the tree is \(2\). Delete those two leaves. If \(y\) has exactly one leaf neighbor, match that leaf with \(y\); their distance is \(1\). Delete both. In either case, the undeleted vertices induce a tree, unless no vertices remain. Iterating produces disjoint pairs at tree-distance at most \(2\) and leaves at most one vertex unmatched. Thus the pairs form a matching of size \(\lfloor n/2\rfloor\) in \(T^2\).

Now choose a spanning tree \(T\) of \(G\). Distances in \(G\) are no larger than the corresponding distances in \(T\), so every pair supplied by the lemma also has distance at most \(2\) in \(G\), and hence in the corona.

If \(n\) is even, the lemma partitions \(V(G)\) into \(n/2\) pairs at distance at most \(2\). The set \(V(G)\) dominates the corona, so it is a semipaired dominating set of size \(n\).

If \(n\) is odd, the lemma pairs all original vertices except one, say \(u\). Add the private leaf \(u^\prime\). Pair \(u\) with \(u^\prime\), which are adjacent, and retain all pairs from the lemma. Thus
\[
V(G)\cup\{u^\prime\}
\]
is a semipaired dominating set of size \(n+1\).

Both cases attain (1), proving the formula.

## Verification
The included verifier independently implements the semipaired definition, the spanning-tree construction, and the tree-square matching procedure.

It exhaustively checks every connected labeled simple graph of orders \(2,3,4,5\). For each of the \(771\) connected graphs, it constructs the leaf corona, enumerates all even vertex subsets until the true optimum is found, and confirms the theorem exactly.

It also checks the constructive matching argument on all \(18{,}248\) Prüfer-coded labeled trees of orders \(2\) through \(7\), and on deterministic connected graphs through order \(50\).

## Relationship to prior work
Semipaired domination was introduced as a relaxation of paired domination: a dominating set may pair vertices at distance \(1\) or \(2\), rather than requiring the pairs to be edges. The accessible algorithmic full text from 2019 studies complexity, interval graphs, trees, and approximation, and contains no corona-product treatment. The later 2020/2021 full text studies split graphs, block graphs, and bounded-degree complexity; targeted inspection found no occurrence of “corona”, “product”, or “pendant”.

A separate 2021 paper on **semitotal** domination does study corona and other graph products. That invariant requires each selected vertex merely to have another selected vertex within distance \(2\); it does not require a global partition into pairs. Its corona results therefore do not imply the semipaired formula proved here.

The lower bound in the theorem comes from the private-leaf transversal forced by domination, while the upper bound uses a matching theorem for squares of spanning trees. This mechanism is different from general-purpose tree algorithms for semipaired domination and gives an exact closed formula for every connected base graph simultaneously.

## Limitations
The theorem treats the one-leaf corona \(G\circ K_1\). It does not claim the same formula for \(G\circ H\) when the attached graph \(H\) has more than one vertex, nor for nonuniform numbers of pendant leaves.

Connectedness is used to obtain a spanning tree whose square supplies the pairing. Disconnected base graphs may require a componentwise parity analysis and are outside the claim.

The computation is finite corroboration only. The arbitrary-order result follows from the private-leaf lower bound and the tree-square matching lemma.

Search coverage cannot exclude a differently phrased or non-indexed treatment of the same corona family.

## References
1. M. A. Henning, A. Pandey, V. Tripathi, “Complexity and Algorithms for Semipaired Domination in Graphs,” arXiv:1904.00964v1, first public version 1 April 2019; later published in Theory of Computing Systems 64 (2020), 1225–1241.
2. M. A. Henning, A. Pandey, V. Tripathi, “Semipaired Domination in Some Subclasses of Chordal Graphs,” arXiv:2008.13491v1, first public version 31 August 2020; Discrete Mathematics & Theoretical Computer Science 23(1) (2021), Article 19, DOI 10.46298/dmtcs.6782.
3. T. W. Haynes, M. A. Henning, “Semipaired Domination in Graphs,” Journal of Combinatorial Mathematics and Combinatorial Computing 104 (2018), 93–109. This is the introducing article; no day-resolved public preprint date was verified for use as the first-public-date field.
4. Z. Kartal Yıldız, A. Aytaç, “Semitotal domination number of some graph operations,” first published online 20 January 2021, later Numerical Methods for Partial Differential Equations 39 (2023), 1841–1850.
