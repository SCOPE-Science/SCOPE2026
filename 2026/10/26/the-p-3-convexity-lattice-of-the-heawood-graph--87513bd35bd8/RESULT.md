# The \(P_3\)-convexity lattice of the Heawood graph

## Finding
Let \(H\) be the point–line incidence graph of the Fano plane \(\mathrm{PG}(2,2)\). Define a vertex set \(S\subseteq V(H)\) to be \(P_3\)-convex when each vertex outside \(S\) has at most one neighbor in \(S\). Write \(P\) for the seven point-vertices and \(L\) for the seven line-vertices, and define the bivariate convex-set enumerator
\[
C_H(x,y)=\sum_{S\text{ is }P_3\text{-convex}}x^{|S\cap P|}y^{|S\cap L|}.
\]
Then exactly
\[
\begin{aligned}
C_H(x,y)={}&1+7y+7x(1+7y+3y^2+y^3)\\
&+21x^2(y+4y^2+2y^3)\\
&+7x^3(y+6y^2+3y^3)+28x^3y^3\\
&+28x^4y^4+x^7y^7.
\end{aligned}
\]
Thus
\[
C_H(z,z)=1+14z+49z^2+42z^3+98z^4+84z^5+49z^6+28z^8+z^{14},
\qquad C_H(1,1)=366.
\]
There are exactly \(49\) inclusion-maximal **proper** \(P_3\)-convex sets, in two geometrically defined classes: \(21\) sets with three points and three lines (one entire line of points together with a complete pencil at one of its points), and \(28\) sets with four points and four lines (one entire line of points, one exterior point, and all four lines joining these points). Every proper convex set has cardinality at most eight; equality occurs exactly for the latter \(28\) sets. In particular no convex set has cardinality \(7\) or \(9,10,11,12,13\).

## Assumptions and scope
The Fano plane has point set \(P=\mathbb F_2^3\setminus\{0\}\) and seven lines \(\{u,v,u+v\}\) for distinct nonzero vectors \(u,v\). Two distinct points determine one line; two distinct lines meet at one point; each line contains three points; each point lies on three lines. The graph \(H\) has a vertex for each point and each line, with adjacency meaning incidence. All counted subsets are distinct labeled subsets of this fixed 14-vertex graph. No claim is made for larger projective planes, for other notions of graph convexity, or for arbitrary Steiner triple systems.

For a selected set \(S\), put \(X=S\cap P\) and \(Y=S\cap L\). Because the graph is bipartite, convexity is equivalent to the pair of closure rules: the unique line through any two distinct members of \(X\) lies in \(Y\), and the unique intersection point of any two distinct members of \(Y\) lies in \(X\). These rules concern **all** length-two paths, not only induced or shortest paths; in this bipartite graph they agree on three-vertex paths.

## Proof
**Geometric closure and classification.** The two closure rules follow because every line-vertex outside \(S\) sees the selected points incident with it, and every point-vertex outside \(S\) sees the selected lines through it. Both inequalities are necessary and sufficient. Classify possible \(X\), and for each type list the polynomial of all permitted \(Y\), with a variable \(y\) marking the number of lines:

| Geometry of \(X\) | Number of such \(X\) | \(\sum_{Y\text{ permitted}}y^{|Y|}\) |
| --- | ---: | --- |
| No points | 1 | \(1+7y\) |
| One point | 7 | \(1+7y+3y^2+y^3\) |
| Two points | 21 | \(y+4y^2+2y^3\) |
| Three collinear points | 7 | \(y+6y^2+3y^3\) |
| Three noncollinear points | 28 | \(y^3\) |
| Four points: one full line plus an exterior point | 28 | \(y^4\) |
| Five or six points, or four points with no collinear triple | 0 admissible | \(0\) |
| All seven points | 1 | \(y^7\) |

Here is a verification of every nontrivial row, using only the projective-plane axioms.

* With \(X=\varnothing\), no two lines may be selected, as they meet outside \(X\). With \(X=\{p\}\), any two chosen lines must meet at \(p\); therefore sets of at least two chosen lines are subsets of the three-line pencil at \(p\), while any of the seven singleton lines is allowed.
* For \(X=\{p,q\}\), the joining line \(\ell=pq\) is mandatory. Every extra chosen line must pass through \(p\) or through \(q\). Choosing extras of both kinds is impossible, as such lines meet off \(\ell\). Hence one may choose a subset of the two non-\(\ell\) lines through exactly one of \(p,q\): one option with no extra line, four with one extra, and two with both extras.
* If \(X\) is the three points of a line \(\ell\), then \(\ell\) is mandatory. Two additional selected lines not equal to \(\ell\) must meet on \(\ell\), hence belong to one of its three pencils. This gives six choices of one extra line or three choices of two extras.
* If \(X\) consists of three noncollinear points, its three joining sides are mandatory and mutually meet at the selected vertices. A fourth selected line would meet at least one side outside \(X\), so is forbidden; thus the three sides are the unique possible \(Y\).
* A four-point set containing a full line \(\ell\) consists of its three points and a point \(p\notin\ell\). Its four joining lines are \(\ell\) and the three distinct lines from \(p\) to the three points on \(\ell\); these lines are pairwise concurrent or meet at selected points, so the set is convex. No fifth line can be chosen: if it goes through \(p\), it equals one of those three, and otherwise it would have to contain all three points of \(\ell\), hence equal \(\ell\).
* A four-point set with no collinear triple is a quadrangle. Its two lines joining disjoint pairs of its points intersect at a diagonal point outside the four chosen points, contradicting the closure rule. Every five- or six-point set contains a quadrangle: select a line containing all omitted points (at most two), and its four-point complement is a quadrangle contained in the selected set. With seven selected points all seven lines are forced. Thus no omitted cases remain.

The possible three-point sets split into seven lines and \(\binom73-7=28\) noncollinear triples; the four-point sets that contain a full line number \(7\cdot4=28\). Multiplying each row polynomial by \(x^{|X|}\) and its class multiplicity proves the stated bivariate and univariate polynomials.

**Maximal proper convex sets.** The 28 four-point–four-line configurations are maximal proper, since no larger proper convex set may have at least four selected points (the case table leaves only the whole plane). The \(7\cdot3=21\) configurations consisting of an entire line \(\ell\), its three points, and all three lines of the pencil at a chosen point \(p\in\ell\) are likewise maximal proper. They cannot be extended to a four-point configuration: the latter has its three non-\(\ell\) lines concurrent at a point outside \(\ell\), whereas the former has two non-\(\ell\) lines through \(p\in\ell\). Every other proper row extends to one of these families. A noncollinear triple extends by completing one of its sides to a full line and adding the fourth joining line. A collinear triple extends by completing the selected pencil. With two selected points, their joining line is forced and any further selected lines lie in a pencil at one of those points, so again they extend to a full line-and-pencil configuration. With one selected point, zero or two or three selected lines extend to a flag (the two- or three-line case is necessarily a pencil); if exactly one selected line is nonincident with that point, they extend instead to a four-point–four-line configuration based on that line and the external point. With zero selected points there is at most one selected line, and the set extends to a flag. Thus precisely 49 configurations are maximal proper.

## Verification
The independent script `verify_heawood_convex.py` constructs all seven Fano triples from nonzero binary vectors, computes the incidence graph, checks each of \(2^{14}=16{,}384\) vertex subsets directly by outside-vertex neighbor counts, and independently checks agreement with point-pair join and line-pair meet closure. It compares all 64 bivariate coefficients with the displayed polynomial and tests inclusion-maximality over all 365 proper convex sets. Running `python3 verify_heawood_convex.py` printed `VERIFY_OK`, total 366, and maximal proper types \((3,3):21\) and \((4,4):28\). The script is a finite corroboration; the proof above establishes the exact claim without relying on experimental extrapolation.

## Relationship to prior work
Dourado, Grippo, Lin, and Protti [1] introduced a systematic 2026 investigation of the number of \(P_3\)-convex sets, proving general complexity results and exact algorithms for all input graphs, with formulas for trees and threshold graphs. Their full paper does not state the Heawood/Fano bivariate polynomial, the 49 maximal proper configurations, or these cardinality gaps. Their general algorithms could calculate the scalar number after applying them to this graph, but no structural classification follows merely from the algorithmic running-time statements. Brešar and Valencia-Pabon [2] examine \(P_3\)-hull numbers of Cartesian products of complete graphs, a different parameter and graph class. The Heawood graph's identification with the Fano plane incidence graph is standard [3]. Existing results on other Heawood graph invariants or \(P_3\)-convex sets in prism graphs do not imply the classification proved here. This is a finite, exact structural example motivated by [1], not a new general counting algorithm or a complexity improvement.

## Limitations
The result is restricted to a fixed 14-vertex graph; no enumeration for higher-order projective planes is claimed. The literature and database comparison is finite and cannot establish absolute historical uniqueness. General counting algorithms apply to the same graph but do not explicitly assert the polynomial or maximal-set classification.

## References
[1] M. C. Dourado, L. N. Grippo, M. C. Lin, and F. Protti, *Counting \(P_3\)-convex sets in graphs*, arXiv:2603.04706v1, first posted 2026-03-05. https://arxiv.org/abs/2603.04706

[2] B. Brešar and M. Valencia-Pabon, *On the \(P_3\)-hull number of Hamming graphs*, 2019 manuscript. https://lipn.univ-paris13.fr/~valenciapabon/papers/P_3-convexity-RV2.pdf

[3] *Heawood Graph*, Wolfram MathWorld (graph identity and standard properties). https://mathworld.wolfram.com/HeawoodGraph.html
