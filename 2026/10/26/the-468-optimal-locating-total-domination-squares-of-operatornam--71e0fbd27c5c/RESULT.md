# The 468 optimal locating-total domination squares of \(\operatorname{PG}(2,3)\)

## Finding

Let \(\Gamma\) be the point–line incidence graph of the projective plane \(\operatorname{PG}(2,3)\), with 13 point vertices and 13 line vertices. A *locating-total dominating set* \(S\) is a set of vertices such that (i) every vertex has a neighbor in \(S\), and (ii) any two distinct vertices outside \(S\) have different sets of neighbors in \(S\). Let \(\mathcal R\) have all minimum such sets as vertices, with an edge when one selected vertex is replaced by one unselected vertex while retaining the property.

**Theorem.** The minimum cardinality is
\[
\gamma_t^L(\Gamma)=10.
\]
All 1,872 minimum sets are precisely the following geometrically parametrized configurations. Choose a projective line \(\ell\), a point \(q\notin\ell\), a point \(x\in\ell\), a point \(p\in(qx)\setminus\{q,x\}\), and a line \(t\) through \(x\), different from \(\ell\) and \(qx\). Here \(qx\) denotes the unique line through \(q\) and \(x\). Select the five point vertices consisting of all four points of \(\ell\) and \(p\); select the five line vertices consisting of all four lines through \(q\) and \(t\).

There are exactly 13 choices for \(\ell\), nine for \(q\), four for \(x\), two for \(p\), and two for \(t\). Moreover,
\[
\boxed{\mathcal R\cong \bigsqcup_{468} C_4.}
\]
Each component is indexed by its fixed triple \((\ell,q,x)\); its four vertices correspond to the independent two choices of \(p\) and \(t\). Thus the exchange graph has 1,872 vertices, 1,872 edges, and all degrees equal to two. Every two different components are exchange-inaccessible without using a larger set.

## Assumptions and scope

The projective plane has 13 points and 13 lines, four points per line and four lines per point, and unique lines through distinct points and unique intersections of distinct lines. Points and lines are treated as different graph vertices. The condition distinguishes **only vertices outside** the chosen set, and uses **open graph neighborhoods**, not closed neighborhoods or distance vectors. An exchange deletes precisely one selected graph vertex and inserts precisely one unselected graph vertex; it does not allow two simultaneous replacements or an intermediate nonminimum set. No statement about planes of other orders is asserted.

For clarity write \(A\) for the selected points and \(B\) for the selected lines. Total domination of the incidence graph is equivalent to requiring that \(A\) meet every projective line (a blocking set) and that \(B\) cover every point. Because the incidence graph is bipartite, distinguishing two nonselected point vertices depends only on \(B\), and distinguishing two nonselected line vertices depends only on \(A\). Distinguishing a nonselected point from a nonselected line is automatic: their nonempty signatures lie in disjoint selected bipartition classes.

## Proof

**1. Lower bound and structure of small blocking sets.** Every line contains four points; hence fewer than four selected points cannot meet all 13 lines. Dually fewer than four selected lines cannot cover all 13 points. The only four-point blocking sets are complete projective lines. To see this, for any blocking set of size four let \(a_i\) be the number of projective lines meeting it in exactly \(i\) points. Incidence and pair counting give
\[
\sum_{i=1}^4 a_i=13,\qquad \sum_{i=1}^4 i a_i=16,\qquad
\sum_{i=1}^4 \binom{i}{2}a_i=6.
\]
Consequently \(a_2+2a_3+3a_4=3\) and \(a_3+3a_4=3\). If \(a_4=0\), then \(a_3=3\) and \(a_2=-3\), impossible. Thus \(a_4=1\). By point–line duality, the four-line covers are precisely the full pencils through points.

If \(A\) consists of the four points of a line \(\ell\), then for each of its four points \(x\) the three other lines through \(x\) have the same signature \(\{x\}\) relative to \(A\). At least two of these three must belong to \(B\), or two unselected line vertices would be indistinguishable. These four triples of lines are disjoint, so \(|B|\ge8\). Dually, \(|B|=4\) forces \(|A|\ge8\). Hence any locating-total dominating set of size at most ten must have at least five points and five lines, and a fortiori the minimum is at least ten.

Every five-point blocking set contains a full line. Indeed incidence and pair counting now yield
\[
\sum_{i=1}^4 a_i=13,\quad \sum_{i=1}^4 i a_i=20,\quad
\sum_{i=1}^4 \binom{i}{2}a_i=10,
\]
so \(a_3+3a_4=3\). If \(a_4=0\), there would be three distinct three-secants to the five selected points. But two such three-secants already contain all five points (distinct projective lines share exactly one point); a third projective line can meet each of those two in only one point and hence contain at most two selected points. This is impossible. Thus a five-point blocker is exactly \(A=[\ell]\cup\{p\}\), where \(p\notin\ell\) and \([\ell]\) denotes the four points on \(\ell\). The line \(\ell\) is unique. Dually, every five-line cover is \(B=[q]\cup\{t\}\), with \([q]\) the full pencil of four lines through \(q\), and \(t\notin[q]\); its center \(q\) is unique.

**2. The necessary geometry of an optimum.** Consider these general five-plus-five forms. For each \(x\in\ell\), there are exactly two lines through \(x\) different from both \(\ell\) and \(px\). Both have signature \(\{x\}\) relative to the selected points \(A\). Thus at least one of the two must belong to \(B\). If \(q\in\ell\), the pencil through \(q\) contains none of these two lines for each of the three points \(x\in\ell\setminus\{q\}\), while the single extra line \(t\) can help at only one such \(x\). Hence \(q\notin\ell\). If \(q=p\), the pencil consists precisely of the lines \(px\) for all four \(x\in\ell\); then an extra line cannot address all four indistinguishable pairs. Therefore \(q\ne p\).

Write \(x_0=pq\cap\ell\). For each \(x\in\ell\setminus\{x_0\}\), the pencil line \(qx\) differs from \(px\), so it is already one of the two lines with signature \(\{x\}\). At \(x_0\), however, \(qx_0=px_0\), and neither of the two lines with signature \(\{x_0\}\) is in the pencil. Consequently the additional selected line \(t\) must be one of precisely these two: it passes through \(x_0\) and differs from \(\ell\) and \(qx_0\). This proves necessity of the announced parameters.

**3. Sufficiency.** Conversely, choose parameters as in the theorem and let \(A=[\ell]\cup\{p\}\) and \(B=[q]\cup\{t\}\). The selected point set meets every line and the pencil covers every point, giving total domination. Among unselected line vertices, \(\ell\) has the four-point signature \([\ell]\); a line \(px\ne\ell\) has the unique two-point signature \(\{p,x\}\); and the other two lines through each \(x\in\ell\) have signature \(\{x\}\), with at most one remaining unselected because of \(B\). All these line signatures are therefore distinct.

For unselected point vertices, \(q\) is distinguished by all four pencil lines through \(q\). Any other point \(r\ne q\) has the pencil-line signature \(qr\), plus the extra line \(t\) exactly when \(r\in t\). The point \(x\) and the chosen point \(p\) on \(qx\) are selected, leaving only one other unselected point on that line (apart from \(q\)). On each of the other three pencil lines \(qy\), the intersection with \(t\) is neither \(q\) nor \(y\in\ell\), and therefore singles out one of the two unselected off-line points. Thus the unselected point signatures are pairwise distinct. This establishes the converse and the minimum ten.

**4. Counting and exchange components.** There are \(13\cdot9\cdot4\cdot2\cdot2=1872\) distinct configurations because the complete line \(\ell\) and full pencil center \(q\) are unique in any optimum, and then \(x=pq\cap\ell\), \(p\), and \(t\) can be recovered.

In a one-vertex exchange between optima, the five-plus-five split cannot change. Within the point side, the full four-point line \(\ell\) cannot change: two distinct projective lines have seven points in their union, while the two five-sets differing by one element have only six points in their union. The same argument fixes the full four-line pencil center \(q\) under an exchange on the line side. The point \(x\) is determined by \(t\cap\ell\) when the point side changes and by \(pq\cap\ell\) when the line side changes. Hence \((\ell,q,x)\) is constant along every exchange path.

For a fixed triple, the two points \(p\in(qx)\setminus\{q,x\}\) differ by one allowed point exchange, and independently the two possible extra lines \(t\) differ by one allowed line exchange. No other one-vertex exchanges are possible. The four configurations are therefore a copy of \(K_2\square K_2\cong C_4\). Exactly \(13\cdot9\cdot4=468\) such triples occur, proving the claimed disjoint union.

## Verification

Two standalone verifiers use the homogeneous-coordinate model over \(\mathbb F_3\). Run `python3 verify.py`; it independently enumerates every blocking point set and covering line set with part sizes between four and six and combined size at most ten, checks open-neighborhood signatures, constructs the geometric parameterization, and reconstructs all one-vertex exchanges. The expected final line is `ALL_VERIFY_OK`. Run `g++ -O2 -std=c++17 verify_alt.cpp -o verify_alt && ./verify_alt` for a separately implemented exhaustive bitmask construction, counting the minimum, equality types, degrees and connected components. Both were executed successfully on the supplied source files. The symbolic arguments above, not enumeration, prove the structural theorem.

## Relationship to prior work

Héger and Takáts (arXiv:1207.5469, 2012) study metric resolving and semi-resolving sets in projective-plane incidence graphs. They report metric dimension eight for the order-three plane and give general incidence-signature criteria; their distinct distance-resolution invariant neither imposes total domination nor classifies locating-total minima or their exchange graph. Héger and Nagy (arXiv:1603.02933, 2016) classify small *ordinary dominating sets* in projective planes via blocking and covering sets. In particular their relevant structural theorems concern a different requirement and have order restrictions; they do not imply the order-three locating-total classification. Henning and Jafari Rad (2012, DOI:10.1016/j.dam.2012.04.004) provide general locating-total domination bounds and results for other graph families. Those bounds do not supply the exact ten, the 1,872 equality cases or the 468 four-cycles. The novelty claimed here is confined to the stated order-three locating-total equality and exchange classification; it does not claim the projective-plane incidence properties, metric dimension, ordinary domination or general locating-total definitions.

## Limitations

The result is specific to the order-three projective plane and to one-at-a-time *minimum-preserving* exchanges. It does not establish the corresponding locating-total domination number for larger projective planes, nor connectivity when additional selected vertices are permitted. Relevant historical articles may contain unindexed or inaccessible equivalent statements; the originality assessment is provisional pending independent literature audit. The source `Locating-total domination in graphs` (2012) was available in indexed article excerpts but its complete publisher file could not be read in this review; no claim that its inaccessible pages were inspected is made. Neither an exhaustive finite computation nor a unsuccessful literature search is treated as a priority certificate.

## References

1. T. Héger and M. Takáts, *Resolving sets and semi-resolving sets in finite projective planes*, Electronic Journal of Combinatorics 19(4), P30 (2012), first public arXiv version 23 July 2012. https://arxiv.org/abs/1207.5469 ; https://doi.org/10.37236/2582.
2. T. Héger and Z. L. Nagy, *Dominating sets in projective planes*, arXiv:1603.02933v1 (9 March 2016); Journal of Combinatorial Designs 25 (2017), 293–309. https://arxiv.org/abs/1603.02933.
3. M. A. Henning and N. Jafari Rad, *Locating-total domination in graphs*, Discrete Applied Mathematics 160 (2012), 1986–1993. https://doi.org/10.1016/j.dam.2012.04.004.
