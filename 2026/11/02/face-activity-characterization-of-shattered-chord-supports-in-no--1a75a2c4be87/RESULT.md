# Face-activity characterization of shattered chord supports in noncrossing perfect matchings

## Finding
Let \(n\geq1\), and let \(V=\{0,\ldots,2n-1\}\) label points in clockwise cyclic order in strictly convex position. Let \(\mathcal N_n\) be all straight-line noncrossing perfect matchings of \(V\), regarded as Boolean concepts on unordered-pair queries: a queried chord is positive exactly when it belongs to the matching.

**Face-activity theorem.** An arbitrary finite set of chords \(S\subseteq\binom V2\) is VC-shattered by \(\mathcal N_n\) if and only if all three conditions hold:

1. Its chords have distinct endpoints and no two cross.
2. Every face of the closed disk cut by the chords of \(S\) has an even number of *free* boundary vertices (vertices not incident with \(S\)).
3. Every chord of \(S\) borders at least one face containing a free vertex (necessarily at least two, by condition 2).

The disk boundary is the circle through the points; even an adjacent-vertex chord cuts off a small circular segment, counted as a face. The faces are the connected open regions obtained after cutting along all selected chords. A free point on the circle belongs to the closure of exactly one face. Thus the conditions are purely combinatorial and do not depend on distances or angles.

Moreover, for every \(n\ge1\),
\[
\operatorname{VCdim}(\mathcal N_n)=\operatorname{Ldim}(\mathcal N_n)=n-1.
\]
The maximum shattered supports have exactly \(n-1\) chords. There are precisely \(n^2\) such supports. They are in bijection with the \(n^2\) choices of two free vertices of opposite parity: remove those two vertices and match consecutive vertices along each of the two circular arcs between them.

## Assumptions and scope
All point sets are in strictly convex position; points are distinct, and noncrossing means chords do not meet in their interiors. Chords of the concept class are unordered vertex pairs; a query that cannot occur in a concept is always negative and cannot belong to a shattered nonempty support. A face includes every circular cap separated by an outer polygon side, as specified above. The theorem treats all integers \(n\ge1\), including the one-matching case \(n=1\). Shattering is simultaneous realization of every labeling of a *fixed* chord support; Littlestone dimension means shattering by a complete adaptive Boolean query tree. Nothing is claimed for arbitrary nonconvex point sets, bichromatic constraints, or non-perfect matchings.

## Proof
**Step 1: extendibility.** Suppose \(S\) consists of disjoint noncrossing chords. The selected chords subdivide the disk into convex faces (intersections of the disk with half-planes specified by the chords). An unpaired vertex belongs to exactly one face. If a noncrossing perfect matching contains \(S\), each face must contain an even number of unpaired vertices, because no completion chord can cross \(S\). Conversely, if each face has an even number, pair its unpaired boundary vertices consecutively in their cyclic order. These completion edges lie in that convex face, do not cross, and together with \(S\) form a noncrossing perfect matching. Therefore conditions 1 and 2 are exactly the all-positive-labeling feasibility condition.

**Step 2: an edge-disjoint rotation lemma.** Given \(2t\ge4\) points in cyclic order and any noncrossing perfect matching \(M\) on them, cyclically shift all endpoint indices forward by one. The resulting matching \(M^+\) remains noncrossing and shares no edge with \(M\). Indeed, if an edge \(e\) occurred in both, then \(M\) would contain both \(e\) and its one-step predecessor. Those chords either share a vertex (if their endpoints are cyclically adjacent) or cross (if not), contradicting the matching and noncrossing properties. Cyclic order rather than equal spacing is the only ingredient. The statement is deliberately restricted to \(2t\ge4\); for two vertices, the sole edge is unavoidable.

**Step 3: necessity of face activity.** Assume \(S\) is shattered, so Steps 1's conditions hold. Suppose some selected chord \(e\) has no free vertices in either of its neighboring faces. Force every chord of \(S\setminus\{e\}\) to be positive. Deleting \(e\) merges exactly its two adjacent faces and makes its two endpoints free. Since neither old face held a free vertex, the merged face now contains exactly two free vertices, the endpoints of \(e\); its unique matching edge is \(e\). Every noncrossing completion must therefore contain \(e\), contradicting the labeling in which \(e\) is negative and all other selected chords are positive. Condition 3 is necessary.

**Step 4: sufficiency of face activity.** Let all three conditions hold, and fix a completion \(M\supseteq S\) provided by Step 1. Choose an arbitrary positive-labeled subcollection \(P\subseteq S\); put \(N=S\setminus P\). The chords of \(P\) dissect the disk into convex faces. The restriction of \(M\) to the vertices free of \(P\) forms a noncrossing perfect matching within each such face, and each face has an even number of those vertices. A face with none needs no matching. A face with exactly two has a unique completion edge, and that edge cannot lie in \(N\): otherwise it would be a selected chord \(e\) whose two endpoints are the only vertices free of \(P\) in the face. Every chord of \(N\setminus\{e\}\) then lies outside this face, and restoring it cannot alter this face. After cutting by all of \(S\), the two faces adjoining \(e\) would contain no originally free vertices, contrary to condition 3.

In a face with at least four vertices free of \(P\), replace its restriction of \(M\) by the cyclically shifted matching of Step 2. All new chords remain inside the face by convexity and avoid *every* edge of the old matching in that face. In particular, they avoid all chords of \(N\), because \(N\subseteq M\). Combining the positive chords \(P\), the unique two-vertex completions, and the rotated completions yields a noncrossing perfect matching meeting \(S\) in exactly \(P\). As \(P\) was arbitrary, \(S\) is shattered.

**Step 5: dimensions.** Every perfect matching contains exactly \(n\) pairwise vertex-disjoint edges. If a query support of size \(n\) were shattered, its all-positive assignment would force one complete matching, and the assignment with all but one query positive would force the last edge as well, a contradiction. Thus \(\operatorname{VCdim}\le n-1\). A matching of \(n-1\) consecutive boundary chords leaving two circularly adjacent vertices unpaired meets all three conditions; thus \(\operatorname{VCdim}=n-1\).

For the online upper bound, predict every query negative until \(n-1\) distinct positive matching edges are identified; thereafter the remaining two unmatched vertices are known and every query can be answered without error. A realizable target can cause at most \(n-1\) mistakes. The standard complete-tree adversary makes one mistake per level against any deterministic predictor, so \(\operatorname{Ldim}\le n-1\). The general inequality \(\operatorname{VCdim}\le\operatorname{Ldim}\) gives equality. Repeated queries and queries for impossible chords do not change the argument.

**Step 6: maximum supports.** With \(n-1\) selected chords, there are exactly two free vertices, lying in one common face by condition 2. This is the only face with free vertices. Form the plane dual of the chord subdivision: each face is a vertex and each chosen chord an edge. This dual is a tree because adding each disjoint chord subdivides one face into two. Condition 3 says every dual edge touches the unique active face, so the dual is a star. Every other face is a leaf with no free vertices; its unique incident chord consequently cuts off a circular arc containing no other vertex. Hence every chord of the selected support joins neighboring original vertices on the circle. If the two free vertices are \(u,v\), the two arcs of remaining vertices between them must each have even cardinality; equivalently, \(u,v\) have opposite parity in the fixed cyclic labeling. Along each arc the unique matching using polygon-side edges pairs its vertices consecutively. Conversely, these pairs for every odd-even pair \(u,v\) produce one shattered support, since the face containing \(u,v\) touches all its chords. There are \(n\) even and \(n\) odd vertices, giving exactly \(n^2\) maximum supports.

## Verification
The attached `verify_noncrossing.py` independently enumerates all Catalan noncrossing perfect matchings, tests each candidate chord support by directly computing its projected labeling set, and compares with the theorem's face test. For \(1\le n\le6\), every support compatible with an all-positive completion is included, at every cardinality; this is 4,786 supports. The numbers of shattered supports, listed by support size \(0,1,\ldots,n\), are:

- \(n=1\): \((1,0)\).
- \(n=2\): \((1,4,0)\).
- \(n=3\): \((1,9,9,0)\).
- \(n=4\): \((1,16,48,16,0)\).
- \(n=5\): \((1,25,140,185,25,0)\).
- \(n=6\): \((1,36,318,860,567,36,0)\).

The verifier separately checks the edge-disjoint rotation property for all 624 noncrossing perfect matchings on 4, 6, 8, 10, 12, and 14 points, and computes exact Littlestone dimensions through 10 points, obtaining \((0,1,2,3,4)\). The unrestricted theorem is proved above and does not depend on finite enumerations. Run `python3 verify_noncrossing.py`; the expected output is in `verification_output.txt`.

## Relationship to prior work
Milich, Mütze, and Pergel (arXiv:2002.02290, public February 6, 2020) study flips and connectivity of noncrossing perfect matchings of the same circular point set. Their complete available text establishes flip-graph results, not the fixed-support positive-and-negative shattering criterion, the total count of maximum shattered supports, or the adaptive dimension. Mantas, Savić, and Schrezenmaier (arXiv:2001.03252, public January 9, 2020) study geometric optimization variants; their feasible-single-chord lemma anticipates the parity restrictions, but single-chord feasibility is insufficient to infer simultaneous shattering. Aichholzer, Asinowski, and Miltzow (arXiv:1403.5546; Electronic Journal of Combinatorics 2015) classify components of a disjoint-compatibility graph of matchings; their global pairing compatibility differs from the facewise prescribed-positive/prescribed-negative problem. The known structural equality for matroid basis concepts does not imply this result: distinct perfect matchings fail single-element matroid basis exchange, so their incidence family is not a matroid-basis family once it contains two matchings.

## Limitations
Novelty is assessed against the primary texts and indexed results inspected, not guaranteed against all historical literature. The 2015 disjoint-compatibility study has a substantial body of combinatorial material, and older matching-reconfiguration work might contain a separately phrased equivalent of part of the face criterion. No exact closed expression is claimed for the number of *all* shattered supports of each intermediate size for general \(n\); the displayed finite distributions are checks, not extrapolated theorems. The mistake-bound argument is specific to matching-edge membership and does not extend to unrestricted partial matchings without modification.

## References
1. I. Mantas, M. Savić, H. Schrezenmaier, *New variants of Perfect Non-crossing Matchings*, arXiv:2001.03252 (first submitted 2020-01-09), https://arxiv.org/html/2001.03252v3 .
2. M. Milich, T. Mütze, M. Pergel, *On flips in planar matchings*, arXiv:2002.02290 (first submitted 2020-02-06), https://arxiv.org/abs/2002.02290 .
3. O. Aichholzer, A. Asinowski, T. Miltzow, *Disjoint compatibility graph of non-crossing matchings of points in convex position*, Electron. J. Combin. 22(1) (2015), P1.65, https://doi.org/10.37236/4403 .
