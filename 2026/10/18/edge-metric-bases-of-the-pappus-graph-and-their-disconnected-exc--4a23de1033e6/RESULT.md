# Edge-metric bases of the Pappus graph and their disconnected exchange geometry

## Finding
Let \(P\) be the eighteen-vertex Pappus graph, realized as the point--nonvertical-line incidence graph over \(\mathbb F_3\). Its edge metric dimension is \(\operatorname{edim}(P)=4\), and exactly \(540\) four-vertex edge metric bases exist. All of them admit the complete affine-geometric characterization stated below. In the graph whose vertices are the bases and whose edges are one-vertex exchanges (token jumps), there are \(3672\) edges and exactly seven components: six copies of \(K_3\square K_3\), each of order \(9\) and diameter \(2\), and a connected component of order \(486\) with radius and diameter both \(5\). Under token slides along an original incidence edge, every one of the \(540\) bases is isolated.

## Assumptions and scope
All arithmetic is in \(\mathbb F_3\). There are points \(p_{x,y}\), for \(x,y\in\mathbb F_3\), and nonvertical lines \(\ell_{m,b}\), for \(m,b\in\mathbb F_3\). An incidence edge joins \(p_{x,y}\) to \(\ell_{m,b}\) if and only if \(y=mx+b\). The graph has \(18\) vertices and \(27\) edges. In the canonical labeling, \(p_{x,y}\) has index \(3x+y\) and \(\ell_{m,b}\) has index \(9+3m+b\), with representatives \(0,1,2\).

For a vertex \(s\) and an edge \(e=uv\), define \(d(s,e)=\min\{d(s,u),d(s,v)\}\) with graph shortest-path distance. A vertex set \(S\) is *edge resolving* if all \(27\) edge-distance vectors \((d(s,e))_{s\in S}\) are distinct, using any fixed order on \(S\). A basis is an edge-resolving set of smallest cardinality.

The four-vertex bases are **exactly** those in the following three mutually exclusive classes.

1. **Points only:** two points from each of two distinct vertical classes \(x=c\); no lines. There are \(27\).
2. **Lines only:** two lines from each of two distinct slope classes \(m=c\); no points. There are \(27\).
3. **Mixed:** points \(p,q\) with distinct first coordinates, together with nonparallel lines \(\ell,k\), such that the affine intersection \(\ell\cap k\) is not on the affine line through \(p,q\). There are \(486\).

A token jump replaces one chosen vertex with any previously unchosen vertex while remaining a basis. A token slide is a token jump in which the removed and added vertices are adjacent in \(P\). The claims concern exactly these minimum-cardinality bases and these two moves.

## Proof
**Distance formula.** Any two distinct points with different first coordinates share a nonvertical line and lie at graph distance \(2\). Two points on one vertical line, being nonidentical and having no common retained line, lie at distance \(4\). Dually, two distinct nonvertical lines of different slopes meet in an affine point and have distance \(2\), while parallel lines have distance \(4\). A point and a line have distance \(1\) when incident and \(3\) otherwise. Therefore, for an incidence edge \(e=(p_{x,y},\ell_{m,b})\) and a landmark \(s\), its distance is given by the following exhaustive cases:

* If \(s=p_{u,v}\): \(d(s,e)=0\) when \((u,v)=(x,y)\); otherwise \(1\) when \(v=mu+b\); otherwise \(2\) when \(u\ne x\); otherwise \(3\).
* If \(s=\ell_{n,c}\): \(d(s,e)=0\) when \((n,c)=(m,b)\); otherwise \(1\) when \(y=nx+c\); otherwise \(2\) when \(n\ne m\); otherwise \(3\).

These rules are independent of any search algorithm or graph library and determine all possible edge signatures.

**Finite exact classification.** For every cardinality \(k\in\{0,1,2,3,4\}\), enumerate every \(k\)-subset of the canonical \(18\)-vertex set and compare its \(27\) signatures obtained from the displayed formula. An edge-resolving set is detected precisely when the number of distinct signatures equals \(27\). The complete counts of resolving sets for \(k=0,1,2,3,4\) are, respectively, \(0,0,0,0,540\). On all \(\binom{18}{4}=3060\) four-subsets, the signature test agrees exactly with the three geometric predicates above. Thus the classification is necessary and sufficient, and the lower bound of four is exhaustive. For example, \(\{p_{0,0},p_{1,0},\ell_{0,1},\ell_{1,0}\}\) is a mixed basis, proving attainment independently of the count.

The class counts also follow geometrically. Each pure type has \(\binom{3}{2}\binom{3}{2}^2=27\) choices. There are \(\binom32\,3^2=27\) unordered pairs of points with distinct first coordinates. For any such pair, there are exactly \(18\) eligible unordered pairs of nonparallel lines whose intersection is off the determined affine line, giving \(27\cdot18=486\) mixed bases. Both geometric predicates and all counts are exhaustively verified by the provided independent algebraic checker.

**Exchange graph.** Index every basis by its ordered four-element canonical label set. Two bases are connected by a token jump exactly when their intersection has cardinality \(3\). Construct every such pair, giving precisely \(3672\) edges. No basis has \(1\) or \(3\) point landmarks, so one replacement cannot join pure and mixed types or the point-only and line-only types. For any fixed pair of distinct vertical point classes, the two-of-three choices in each class give \(3\times3\) point-only bases; two are adjacent exactly when one coordinate choice changes. Thus these nine vertices induce \(K_3\square K_3\). The three choices of the pair of vertical classes give three such components; slope-class duality gives three more. The remaining \(486\) mixed bases form one component, established by complete breadth-first search in the explicitly specified finite exchange graph. The search determines eccentricity \(5\) at each of the \(486\) vertices; each small component has eccentricity \(2\) at each vertex. Two different implementations produce the same sorted state list and undirected edge list, and independently reproduce every eccentricity. The complete lists of bases and token-jump edges are embedded in `state_transition_certificate.json`.

**Sliding obstruction.** Every incidence edge joins a point to a line. A slide along such an edge changes the number of selected points by exactly one. Every four-vertex basis, however, has an even number of selected points: \(0\), \(2\), or \(4\). Hence no slide of a basis can produce another basis. This is a structural proof, independent of enumeration of the exchange graph.

## Verification
Run `python verify_graph.py state_transition_certificate.json` and `python verify_geometry.py state_transition_certificate.json` in the same directory. The first independently generates graph distances through breadth-first search and performs all finite signature and exchange tests. The second derives signatures from the finite-field formulas, tests the geometric classification against each four-subset, constructs exchanges by common-triple indexing, and calculates shortest paths through bitset frontiers. Both validate the entire certificate, not just summary counts. Expected outputs appear in `verification_graph.json` and `verification_geometry.json`. The sorted basis list and edge list have SHA-256 digests `9c55045f90fe9a946ceec98c7caf4e7ce675c3c28bac63219649aabafb6ff74b` and `b4f09a77286c9916f88e733a5ddc10127e7109240af8774a1165f54ba92fd20d`, respectively, using compact JSON serialization. No probabilistic testing or unverified extrapolation is used.

## Relationship to prior work
Kelenc, Tratnik and Yero introduced edge metric dimension, gave its distance definition, basic family results, and computational complexity; the inspected full work does not classify minimum edge-resolving sets on the Pappus graph or their exchanges. Bartoli, Héger, Kiss and Takáts studied *ordinary vertex* metric dimension in affine and biaffine incidence graphs. Their results address a different family of signatures, and their main large-order arguments do not cover the present edge-metric exchange claim. No claim is made that the definition or the affine graph is new.

## Limitations
This is an exact finite theorem for the Pappus graph only; it does not establish an analogous formula for general biaffine planes. The component distance claim relies on exhaustive enumerations with included fully reproducible programs and a complete small finite certificate, not a hand-derived closed-form distance isomorphism for the \(486\)-vertex component. The originality comparison is limited to the cited and searched literature; unknown or unindexed equivalent work cannot be excluded. Independent validation has not been performed.

## References
1. A. Kelenc, N. Tratnik, I. G. Yero, *Uniquely identifying the edges of a graph: the edge metric dimension*, arXiv:1602.00291, first publicly posted 2016-01-31. https://arxiv.org/abs/1602.00291
2. D. Bartoli, T. Héger, G. Kiss, M. Takáts, *On the metric dimension of affine planes, biaffine planes and generalized quadrangles*, arXiv:1706.06583, first posted 2017-06-20. https://arxiv.org/abs/1706.06583
