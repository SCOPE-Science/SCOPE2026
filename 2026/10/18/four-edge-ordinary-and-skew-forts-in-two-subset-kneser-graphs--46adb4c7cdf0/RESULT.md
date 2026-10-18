# Four-edge ordinary and skew forts in two-subset Kneser graphs

## Finding

For every integer \(n\ge5\), let \(G_n=\mathrm{KG}(n,2)\) be the graph whose vertices are the two-element subsets of \([n]\), adjacent precisely when disjoint. An **ordinary fort** is a nonempty vertex set \(X\) such that every vertex outside \(X\) has either zero or at least two neighbors in \(X\). A **skew fort** requires the same condition at *every* vertex, including those inside \(X\). Both kinds of forts have minimum cardinality exactly four.

Identify four vertices of \(G_n\) with four distinct edges of \(K_n\). Every minimum **ordinary fort** has exactly one of these forms:

- the four edges of a star \(K_{1,4}\);
- the four edges of a cycle \(C_4\);
- four pairwise disjoint edges (a four-edge matching, possible only for \(n\ge8\));
- when \(n=6\) only, the three edges of a star \(K_{1,3}\) together with an edge disjoint from that star.

Every minimum **skew fort** is either a four-edge star or a four-edge matching; the cycle and the exceptional six-vertex configuration are ordinary forts only. The ordinary and skew minimum-fort counts are respectively

\[
B_n=n\binom{n-1}{4}+3\binom n4+105\binom n8+60\mathbf1_{\{n=6\}},
\qquad
B^-_n=n\binom{n-1}{4}+105\binom n8.
\]

Here a binomial coefficient is zero when its lower argument exceeds the upper argument. In particular, the difference is \(B_n-B^-_n=3\binom n4+60\mathbf1_{\{n=6\}}>0\). Ordinary and skew **failed zero forcing numbers** are nevertheless equal:

\[
F(G_n)=F^-(G_n)=\binom n2-4.
\]

The ordinary scalar equality was published previously; the new contribution assessed here is the complete comparative classification and the exact multiplicity formulas, especially for skew failure configurations.

## Assumptions and scope

All graphs are finite, simple, and labeled as above. The theorem covers every integer \(n\ge5\), including the Petersen graph at \(n=5\). A forcing process starts with a chosen set of black vertices. Under ordinary zero forcing, a black vertex having exactly one white neighbor forces it black. Under skew zero forcing, the forcing vertex may be black or white. An initial set is *failed* if the process cannot make every vertex black. The cardinality of a largest failed set is \(F\) or \(F^-\), respectively. A fort is called minimum when it has the smallest cardinality among nonempty forts; this is different from inclusion-minimality. No assertion is made for \(n<5\) or for \(\mathrm{KG}(n,r)\) with \(r>2\).

## Proof

**1. Reduction to an edge-degree condition.** Write a selected set \(X\subseteq V(G_n)\) as an edge set \(H\subseteq E(K_n)\), let \(k=|H|\), and put \(d(u)=\deg_H(u)\). For a two-element subset \(e=uv\), the number of selected vertices adjacent to \(e\) in \(G_n\) is exactly

\[
q_H(uv)=k-d(u)-d(v)+\mathbf1_{\{uv\in H\}}.
\]

This follows by subtracting the \(d(u)+d(v)\) selected edges incident with \(u\) or \(v\), adding back \(uv\) once if it was double-subtracted, and recognizing that adjacency in \(G_n\) means disjointness. Hence an ordinary fort satisfies \(q_H(uv)\ne1\) for all \(uv\notin H\), while a skew fort requires \(q_H(uv)\ne1\) for **all** two-element subsets \(uv\).

**2. No ordinary fort with fewer than four vertices.** A one-edge \(H\) fails because \(n\ge5\) permits an edge disjoint from it. For two edges, whether adjacent or disjoint, a third edge can be chosen to intersect exactly one selected edge; it is not selected and has \(q_H=1\). For three edges, every simple graph with three edges is, after deleting isolated vertices, one of the following: three disjoint edges, a three-edge star, a triangle, a four-vertex path, or a two-edge path plus a disjoint edge. Respectively, choose a test edge joining an endpoint of each of two matching edges; joining two leaves of a star; joining a triangle vertex to a vertex outside the triangle; joining the endpoints of a four-vertex path; or joining a leaf of the two-edge path to an endpoint of the disjoint edge. Each test edge lies outside \(H\) and is disjoint from **exactly one** selected edge. Cases requiring more than \(n\) vertices do not arise. Therefore no ordinary fort, and hence no skew fort, has cardinality below four.

**3. All ordinary four-edge forts.** Now \(k=4\). If \(\max d=4\), all four edges share a center and form \(K_{1,4}\), which satisfies the ordinary condition. If \(\max d=3\), write the three center edges as \(ca,cb,cd\), and examine the remaining edge. When it joins two of \(a,b,d\), there is an isolated original vertex and the nonselected pair joining that vertex to \(c\) has \(q_H=1\). When it joins one of \(a,b,d\) to an outside vertex, one obtains nonadjacent original vertices of degrees two and one, giving \(q_H=4-2-1=1\). When it is disjoint from \(\{c,a,b,d\}\), the six supported vertices form \(K_{1,3}\sqcup K_2\); if \(n\ge7\), an unused vertex again gives \(q_H=1\) with \(c\). At \(n=6\), direct substitution in the displayed degree identity shows that \(K_{1,3}\sqcup K_2\) **is** an ordinary fort. The disjoint last-edge case is impossible for \(n=5\).

Suppose instead \(\max d\le2\). If a degree-two vertex \(u\) and a degree-one vertex \(v\) are nonadjacent in \(H\), then \(q_H(uv)=4-2-1=1\), forbidden. Thus every degree-one vertex must be adjacent to every degree-two vertex. Since degree-one vertices have only one neighbor, there is then at most one degree-two vertex, and since that vertex has only two neighbors, at most two degree-one vertices. But the degree sum of four edges is eight, whereas one degree-two vertex and at most two degree-one vertices contribute at most four; contradiction. Therefore degrees one and two cannot coexist. The only possibilities are all positive degrees one, yielding four disjoint edges, or all positive degrees two, yielding a cycle \(C_4\). Both satisfy the ordinary condition by the degree identity: every unselected \(uv\) has \(d(u)+d(v)\) equal to zero, one, two, or four, never three. This exhausts the ordinary cases.

**4. Skew restriction.** A four-edge star is skew because a test edge incident with the center meets all four chosen edges, while a test edge missing the center meets at most two; thus \(q_H\) is zero or at least two. A four-edge matching is skew since every test edge intersects at most two chosen edges, so \(q_H\ge2\). A four-cycle is not skew: any selected cycle edge has exactly one disjoint selected edge, namely its opposite edge. The exceptional \(K_{1,3}\sqcup K_2\) is not skew because any selected star edge is disjoint from exactly the separate edge. Hence the stated list of skew forts is complete.

**5. Counts and failed forcing.** A four-edge star is specified by its center and four distinct leaves, yielding \(n\binom{n-1}{4}\) possibilities. A four-cycle is specified by four vertices and one of three cycles, yielding \(3\binom n4\). A four-edge matching is specified by eight vertices and one of \((8-1)!!=105\) pairings, yielding \(105\binom n8\). At \(n=6\), the claw-plus-edge structure has six center choices and \(\binom53\) leaf choices; its remaining two vertices form the disjoint edge, yielding \(60\). The types are mutually disjoint.

For either forcing rule, a failed initial black set has a nonempty terminal white set into which no further force is possible; that terminal set is an ordinary or skew fort respectively. Conversely, the complement of any fort is itself a failed initial black set. Thus maximum failed sets are precisely complements of minimum forts. Applying the established minimum size four yields both failed-forcing numbers and the stated numbers of maximum failed sets.

## Verification

The standalone `verify.py` independently constructs \(G_n\) from disjointness of two-subsets and tests all candidate forts of sizes one through four for every \(5\le n\le10\), covering 264,959 subsets. It compares membership with an independent graph-shape classifier and verifies each coefficient of the counting formulas. For \(5\le n\le8\), it separately simulates both forcing processes on complements of 34,028 white candidate sets, checking that terminal failure agrees with the static fort tests. Its recorded output is `verify_output.txt`.

## Relationship to prior work

Brešar, Kos and Torres determined the skew **successful** zero forcing number \(Z^-(\mathrm{KG}(n,r))=\binom nr-\binom{2r}{r}\) for \(r\ge2\), \(n\ge2r+1\) and investigated standard zero forcing. Their scalar optimum concerns the minimum **successful** seed, not the largest failed seed or the count of four-vertex forts. Johnson, Vick and Narayan studied failed skew forcing and characterized graphs with failed-skew number one, not the Kneser-family extremal configurations here. Afzali, Ghodrati and Maimani established the ordinary **failed** zero forcing scalar \(F(\mathrm{KG}(n,r))=\binom nr-(r+2)\) in the relevant range, which for \(r=2\) already gives \(F(G_n)=\binom n2-4\); this scalar is accordingly **not** claimed as new. Their abstract and accessible metadata did not establish the exact multiplicities of maximum failed sets or the skew/ordinary comparison. The complete text of that 2024 article could not be obtained for direct coverage comparison.

## Limitations

The result addresses minimum-cardinality forts only, not all inclusion-minimal forts or all failed sets. Its proof covers \(n\ge5\), not higher-order Kneser graphs. Exhaustive computation is supplementary to the infinite-family argument. The 2024 ordinary-failure article was available through metadata and abstract but not in full text; an unindexed equivalent classification could affect priority. This is a self-review, not independent validation.

## References

1. B. Brešar, T. Kos, P. D. Torres, *Grundy domination and zero forcing in Kneser graphs*, Ars Mathematica Contemporanea 17 (2019), 419–430; published online 6 November 2019; DOI: 10.26493/1855-3974.1881.384.
2. A. Johnson, A. E. Vick, D. A. Narayan, *Characterization of Graphs With Failed Skew Zero Forcing Number of 1*, arXiv:2209.09379 (first posted 19 September 2022); later Mathematics 10 (2022), 4463; DOI: 10.3390/math10234463.
3. F. Afzali, A. H. Ghodrati, H. R. Maimani, *Failed zero forcing numbers of Kneser graphs, Johnson graphs, and hypercubes*, J. Applied Mathematics and Computing 70 (2024), 2665–2675; DOI: 10.1007/s12190-024-02064-w.
