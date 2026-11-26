# Square-flip components in small hypercubes and a frozen family in every dimension at least four

## Finding

Let \(Q_d\) be the graph on \(\{0,1\}^d\) with edges at Hamming distance one. Let \(\mathcal F_d\) be the graph on the perfect matchings of \(Q_d\), where two states are adjacent if one is obtained from the other by replacing a matched opposite edge pair of a coordinate square by the other opposite pair. A matching is *frozen* if it is isolated in \(\mathcal F_d\).

The graph \(\mathcal F_2\) is \(K_2\), and \(\mathcal F_3\) is connected with nine vertices and twelve edges. For \(d=4\),
\[
\mathcal F_4=G_{264}\sqcup 8K_1,
\qquad |V(\mathcal F_4)|=272,\qquad |E(\mathcal F_4)|=768.
\]
The connected component \(G_{264}\) has radius seven and diameter eight; 252 vertices have eccentricity seven and twelve have eccentricity eight. The eight isolates form one orbit under coordinate permutations and bit translations, the 384 automorphisms of \(Q_4\). The full degree distribution of \(\mathcal F_4\), written as (degree : count), is
\[
(0:8),\ (3:32),\ (4:12),\ (5:96),\ (6:48),\ (8:72),\ (12:4).
\]
For every integer \(d\ge4\) there are at least \(2^{2^{d-4}}\) frozen perfect matchings of \(Q_d\). In particular, **among dimensions \(d\ge2\)** the first with a frozen matching is four. At \(d=1\) the unique perfect matching is vacuously frozen; \(Q_0\), if included, has no perfect matching.

## Assumptions and scope

The vertices of \(Q_d\) are labelled and a matching is an unordered set of unoriented edges covering each vertex once. There is no quotient by symmetry. A square varies exactly two coordinate bits, with all other bits fixed. Every four-cycle in \(Q_d\) has this form: each coordinate flipped along the cycle is flipped an even number of times, and avoiding repetition of vertices forces the flips to alternate between two coordinates. Longer cycle moves and whole-cube automorphisms are not moves. The detailed census is in dimensions two through four; the higher-dimensional result is only a lower bound on the number of isolated states, not a classification of all states or connected components.

## Proof

**Finite census.** Encode vertices by binary integers. Enumerate all perfect matchings in dimensions two, three and four by matching the even-parity vertices bijectively to the odd-parity vertices and retaining exactly those bijections whose pairs differ in one bit. Each perfect matching determines exactly one such bijection. A second enumeration pairs the least uncovered vertex with each uncovered neighbor and recurses. This is exhaustive and duplicate-free because the chosen vertex is determined by the partial matching and has a unique partner in any completion. Both enumerations give the same sets. In dimension one, the single edge is the only matching and there are no squares; in dimension zero there is a single vertex.

For every unordered coordinate pair, fix all other bits to enumerate its squares. For each matching test whether either opposite pair in each square is present. Replace it by the other opposite pair if present; this gives all and only flip neighbors. Check that these edges are symmetric and that every reached state occurs in the matching census. Enumerate components of this finite graph by breadth-first search; compute the eccentricities in its non-singleton four-dimensional component by breadth-first search from each vertex. Apply all \(2^4\cdot4!\) bit translations and coordinate permutations to one isolate and check the resulting set against the full list of isolates. The exact computation gives:

| \(d\) | Matchings | Flip edges | Component sizes | Degree counts |
|---|---:|---:|---|---|
| 2 | 2 | 1 | 2 | \(1:2\) |
| 3 | 9 | 12 | 9 | \(2:6,4:3\) |
| 4 | 272 | 768 | 264 and eight singletons | \(0:8,3:32,4:12,5:96,6:48,8:72,12:4\) |

The set obtained from the orbit check has size eight and equals the isolate set. The eccentricity counts within the component of size 264 are precisely \(7:252,8:12\).

**Frozen base states.** In the integer labels 0 through 15 use these four perfect matchings:

- \(A\): \((0,1),(2,6),(3,11),(4,12),(5,7),(8,10),(9,13),(14,15)\).
- \(B\): \((0,2),(1,9),(3,7),(4,5),(6,14),(8,12),(10,11),(13,15)\).
- \(C\): \((0,4),(1,3),(2,10),(5,13),(6,7),(8,9),(11,15),(12,14)\).
- \(D\): \((0,8),(1,5),(2,3),(4,6),(7,15),(9,11),(10,14),(12,13)\).

Each list covers all sixteen vertices once and its pairs differ in one bit. Testing both opposite pairs in each of the 24 squares finds no matched opposite pair in any of the four states. The four matchings are pairwise edge-disjoint, as is seen by comparing the four partners of every vertex; only cross-disjointness between \(\{A,B\}\) and \(\{C,D\}\) is needed.

**Construction in all dimensions.** In \(Q_d=Q_4\mathbin\square Q_{d-4}\), index the copies of \(Q_4\) by their outer word \(t\in\{0,1\}^{d-4}\). In every even-parity slice independently choose \(A\) or \(B\); in every odd-parity slice independently choose \(C\) or \(D\). Match only within slices. The choices produce distinct perfect matchings because the restriction to each slice recovers its chosen state. A square using two inner coordinates lies in one slice, so does not flip. A square using two outer coordinates contains no matched edges. In a mixed square the only candidate opposite matched pair would consist of the same inner edge in two adjacent slices. These slices have opposite parity, so cross-disjointness rules out that pair. Thus every constructed matching is frozen. There are \(2^{d-4}\) slices with two choices each, giving the bound.

## Verification

In the source package, `python3 verify_hypercube_flips.py` uses two matching recursions and two equivalent flip tests, builds all three finite graphs, checks components, degrees, distances and the isolate orbit, and verifies the explicit seeds and the four parity-slice examples for \(Q_5\). The finite census can also be reproduced by testing all \(8!\) bipartite bijections for \(Q_4\), generating the 24 coordinate squares and traversing the resulting flip graph. The proof for unbounded dimension is the three-case argument above, not an extrapolation from a finite run.

## Relationship to prior work

OEIS A005271 gives the raw matching totals \(1,2,9,272,\ldots\) starting at \(d=1\), not their square-flip graphs. Fink's matching graph uses adjacency when the union of two matchings is a spanning Hamiltonian cycle, not a single square flip. Milet and Saldanha study flips and other local moves for three-dimensional cubiculated regions with two floors, a different geometry. Hartarsky, Lichev and Toninelli's \(D_2(Q_d)\) is exactly this square-flip graph. Their Theorem 5 treats \(D_{d-1}(Q_d)\), which in dimension four includes hexagon moves, and their Theorem 6 uses \(D_{2d-2}(Q_d)\); neither gives the square-only classification in dimension four.

Other indexed treatments of the same graph include the exact geodesic profile (Resultary `84ee7ca2c7ef`), which reports the same component and eccentricities, and the all-coordinate-planes case of the directional classification (`a5a5b150160d`). The frozen-sector census in `db180e339d90` gives the same \(Q_4\) component census and the same four mutually disjoint seeds. That treatment uses one versus three choices on the two slice parities, then varies the fixed even-slice state to obtain \(8\cdot 3^{2^{d-5}}\) for \(d\ge5\). Its seed disjointness also allows the two-versus-two construction here; the two displayed estimates themselves are not identical, and the two-versus-two estimate is larger for \(d\ge8\). These are mathematical overlaps rather than claims of separate novelty or priority on identical statements.

## References

1. J. Fink, *Connectivity of matching graph of hypercube*, SIAM J. Discrete Math. (2009), https://kam.mff.cuni.cz/~fink/publications/kreweras2.pdf.
2. I. Hartarsky, L. Lichev and F. Toninelli, *Local dimer dynamics in higher dimensions*, https://arxiv.org/abs/2304.10930.
3. P. H. Milet and N. C. Saldanha, *Flip invariance for domino tilings of three-dimensional regions with two floors*, https://arxiv.org/abs/1404.6509.
4. OEIS A005271, https://oeis.org/A005271.
