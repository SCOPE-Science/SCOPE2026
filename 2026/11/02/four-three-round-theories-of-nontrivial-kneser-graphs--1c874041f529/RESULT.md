# Four three-round theories of nontrivial Kneser graphs

## Finding
For integers \(k\ge2\) and \(n\ge2k\), let \(\mathrm{KG}(n,k)\) be the finite simple undirected graph whose vertices are the \(k\)-subsets of \([n]\), with adjacency given by disjointness. In first-order logic with equality and adjacency, two such graphs are equivalent through quantifier rank three **if and only if** their parameter pairs belong to the same one of the following four classes:

| Class | Exact parameter condition | Least representative | Number of vertices |
| --- | --- | --- | ---: |
| Matching | \(n=2k\) | \(\mathrm{KG}(4,2)\) | \(6\) |
| Low-intersection range | \(2k+1\le n\le3k-2\) | \(\mathrm{KG}(7,3)\) | \(35\) |
| Triangle-free boundary | \(n=3k-1\) | \(\mathrm{KG}(5,2)\) | \(10\) |
| Stable range | \(n\ge3k\) | \(\mathrm{KG}(6,2)\) | \(15\) |

The low-intersection range is nonempty only when \(k\ge3\). Therefore there are exactly four rank-three theories, and every graph has a rank-three equivalent representative of at most \(35\) vertices, with the bound sharp *within this Kneser family*.

An additional consequence is that the triangle-free graphs \(\mathrm{KG}(3k-1,k)\), for all \(k\ge2\), are indistinguishable at rank three from the Petersen graph \(\mathrm{KG}(5,2)\), although their chromatic numbers equal \(k+1\) and are unbounded. Thus first-order sentences of quantifier rank at most three cannot impose a finite upper bound on chromatic number, even among this explicit triangle-free family.

## Assumptions and scope
All graphs are finite, nonempty, simple, undirected, with no named vertices or extra relations. Quantifier rank is the largest nested depth of first-order quantifiers. Repeated assignments of variables to a vertex are allowed; there are no counting quantifiers. The parameters range over **all** integers \(k\ge2\), \(n\ge2k\). The relation \(G\equiv_3H\) means that every first-order sentence of rank at most three has the same truth value on both graphs.

## Proof
**1. A three-move invariant for vertex-transitive graphs.** Both the symmetric group on \([n]\) and its natural action on \(k\)-subsets act transitively on the vertices of \(\mathrm{KG}(n,k)\). For a pair of distinct vertices \(x,y\), record whether \(x\sim y\) and which of the four possibilities
\[
(\mathbf1_{x\sim z},\mathbf1_{y\sim z})\in\{(0,0),(1,0),(0,1),(1,1)\}
\]
can be realized by a *fresh* third vertex \(z\notin\{x,y\}\). The set of these pair profiles, together with the universal repeated-choice profiles \(y=x\) and \(z\in\{x,y\}\), exactly determines the three-round Ehrenfeucht–Fraïssé theory of a vertex-transitive graph. Indeed, after a first vertex is chosen, transitivity removes dependence on that choice. At the second move the duplicator matches the recorded pair profile; at the last move they match equality and one of the available adjacency bits. Conversely, any missing pair profile or missing extension bit gives the spoiler a winning move within three rounds. This is the ordinary three-move, not a counting, game.

For clarity encode a pair profile as \((e,B)\), where \(e\in\{0,1\}\) is its adjacency bit and \(B\) is the set of fresh-third-vertex bit-pairs. Write
\[
B_0=\{(0,0),(1,0),(0,1)\},\qquad
B_1=B_0\cup\{(1,1)\},\qquad
B_M=\{(0,0)\}.
\]

**2. The matching boundary.** When \(n=2k\), each vertex has exactly its complementary \(k\)-subset as a neighbor. There are at least three disjoint edges because \(k\ge2\). For an adjacent pair, a fresh third vertex must be nonadjacent to both; its profile is \((1,B_M)\). For a nonadjacent pair, the respective two partners supply the single-neighbor choices and a vertex on another edge supplies the double-nonneighbor choice; its profile is \((0,B_0)\). Thus the full pair-profile spectrum is
\[
\mathcal S_M=\{(1,B_M),(0,B_0)\}.
\]

**3. Fresh extension patterns for \(n\ge2k+1\).** Let \(x,y\) be distinct \(k\)-subsets with \(t=|x\cap y|\), where \(0\le t\le k-1\). They are adjacent exactly when \(t=0\). Each of the three patterns in \(B_0\) is available:

For \((0,0)\), if \(t=0\), take one point of \(y\) and \(k-1\) points of \(x\); if \(t\ge1\), take a common point, a point outside \(x\cup y\), and \(k-2\) further points of \(x\). These choices give a fresh vertex intersecting both sets. For \((1,0)\), choose a \(k\)-subset disjoint from \(x\) that intersects \(y\). If \(x,y\) are disjoint, replace one point of \(y\) by a point outside their union; if they meet, choose a point of \(y\setminus x\) and complete within \([n]\setminus x\). The symmetric construction gives \((0,1)\). All requisite outside points exist because \(n\ge2k+1\) and \(k\ge2\).

A fresh common neighbor \(z\) of \(x,y\) is precisely a \(k\)-subset of \([n]\setminus(x\cup y)\). The latter has size \(n-2k+t\). Consequently,
\[
(1,1)\in B(x,y)
\quad\Longleftrightarrow\quad
n-2k+t\ge k
\quad\Longleftrightarrow\quad
 t\ge3k-n.
\]
No computation or asymptotic approximation is used here.

**4. Exhausting all pair types.** Every integer \(t\in\{0,1,\ldots,k-1\}\) occurs as the intersection of two distinct \(k\)-sets because \(n\ge2k+1\). Applying the last criterion gives:
\[
\begin{array}{c|l}
2k+1\le n\le3k-2&\mathcal S_L=\{(1,B_0),(0,B_0),(0,B_1)\}\\
 n=3k-1&\mathcal S_T=\{(1,B_0),(0,B_1)\}\\
 n\ge3k&\mathcal S_S=\{(1,B_1),(0,B_1)\}.
\end{array}
\]
In the first line, \(3k-n\ge2\), so intersections \(t=1\) and \(t=k-1\) realize both nonadjacent profiles; \(k-1\ge3k-n\) follows from \(n\ge2k+1\). In the middle line, exactly \(t=0\) fails the common-neighbor test. In the last line, all \(t\) pass. These three spectra and the matching spectrum are pairwise different. Step 1 therefore proves both directions of the claimed equivalence classification.

For additional direct separating sentences, the matching class lacks a vertex with two distinct neighbors; the stable class admits a triangle, whereas the other nonmatching classes do not; and the low-intersection class, unlike the triangle-free boundary class, admits two distinct nonadjacent vertices with no common neighbor. Each is expressible with at most three nested quantifiers.

**5. Sharp representative size and chromatic consequence.** For fixed \(k\), \(\binom nk\) is strictly increasing with \(n\ge k\). Across \(k\ge2\), the least instances of the matching, triangle-free-boundary, and stable regimes occur at \((n,k)=(4,2),(5,2),(6,2)\); the low-intersection regime first exists at \((7,3)\). The resulting vertex counts are \(6,10,15,35\), respectively; the maximum is \(35\). Finally, the classical Kneser–Lovász theorem gives \(\chi(\mathrm{KG}(n,k))=n-2k+2\), and disjoint triples of \(k\)-sets exist only when \(n\ge3k\). Setting \(n=3k-1\) yields triangle-free graphs in the same logical class, with chromatic numbers \(k+1\) tending to infinity.

## Verification
Two standalone Python programs accompany this result. `verify_kneser.py` constructs Kneser graphs directly from all \(k\)-subsets and enumerates the actual fresh-third-vertex pair spectra; it checks the symbolic profiles and four-class prediction on \(28\) parameter pairs with graphs as large as \(924\) vertices. `verify_ef3.py` independently builds depth-three Hintikka types by enumerating *all* ordered triples, including repeated vertices, on nine graphs representing all four classes; it finds exactly four distinct theories. Run both using `python3 verify_kneser.py` and `python3 verify_ef3.py` from the extracted file directory. The stored outputs are `verify_kneser.out` and `verify_ef3.out`. The proof above—not finite enumeration—establishes the infinite-range assertions.

## Relationship to prior work
Matoušek and Ziegler (2002) develop topological lower bounds for Kneser chromatic numbers, and specifically discuss the triangle-free, high-chromatic regime \(n=3k-1\). Their treatment supplies the chromatic context, not a classification of Ehrenfeucht–Fraïssé theories. Pikhurko and Verbitsky (2010) survey first-order distinguishability and its game interpretation, including unrestricted finite graphs, but provide no parameter-specific three-round Kneser classification. The present result adds a complete two-parameter first-order classification and the corresponding logical invisibility of unbounded triangle-free chromatic number. Special-subfamily logical analyses for fixed set size and odd graphs do not by themselves determine the other parameter regimes or cross-family equivalences.

## Limitations
The theorem is restricted to \(n\ge2k\ge4\), ordinary disjointness adjacency, and quantifier rank at most three. It does not cover edgeless Kneser graphs, singleton-subset complete graphs, counting extensions, or rank four and above. Historical priority outside the inspected literature is not exhaustively established. The verification programs are finite corroborations, not independent proof of the quantified theorem, and no independent mathematical audit has been performed.

## References
1. J. Matoušek and G. M. Ziegler, *Topological lower bounds for the chromatic number: a hierarchy*, arXiv:math/0208072, first posted 2002-08-09; relevant material: Introduction and Sections 3–5. https://arxiv.org/abs/math/0208072
2. O. Pikhurko and O. Verbitsky, *Logical complexity of graphs: a survey*, arXiv:1003.4865, first posted 2010-03-25; relevant material: Sections 1 and 3 on graph logic and Ehrenfeucht games. https://arxiv.org/html/1003.4865v4
