# Power-domination polynomial and minimal-set dichotomy of two-subset Kneser graphs

## Finding
Let \(n\ge5\), \(N=\binom{n}{2}\), and \(G_n=KG(n,2)\). Its vertices are the two-element subsets of \([n]\), and two vertices are adjacent precisely when those subsets are disjoint. We call a selected family of pairs a **star** if all its pairs contain a single common point. For families with at least three pairs this center is unique.

**Theorem.** A vertex subset \(S\) is power dominating in \(G_n\) if and only if one of the following mutually exclusive, parameter-dependent conditions holds:

1. \(n=5\): \(|S|\ge3\), or \(|S|=2\) and the two selected pairs intersect.
2. \(n\in\{6,7\}\): \(|S|\ge3\).
3. \(n\ge8\): \(|S|\ge3\) and either \(S\) is not a star or \(|S|\ge n-4\).

Consequently the **complete power-domination polynomial** \(\mathcal P_n(z)=\sum_{S\text{ power dominating}}z^{|S|}\) is
\[
\mathcal P_n(z)=
\begin{cases}
30z^2+\displaystyle\sum_{k=3}^{10}\binom{10}{k}z^k,&n=5,\\[4pt]
\displaystyle\sum_{k=3}^{N}\binom Nk z^k,&n=6,7,\\[4pt]
\displaystyle\sum_{k=3}^{N}\binom Nk z^k-n\sum_{k=3}^{n-5}\binom{n-1}{k}z^k,&n\ge8.
\end{cases}
\]
Every inclusion-minimal power-dominating set is characterized as follows: for \(n=5\), an intersecting pair of graph vertices; for \(n=6,7\), an arbitrary triple of graph vertices; for \(n\ge8\), either a three-pair family that is not a star or a star containing exactly \(n-4\) pairs. For \(n\ge8\), the counts in these latter two classes respectively are
\[
\binom N3-n\binom{n-1}{3}
\quad\text{and}\quad
n\binom{n-1}{3}.
\]
Thus the **total** number of inclusion-minimal sets for every \(n\ge6\) is exactly \(\binom N3\). In particular, the minimum and upper (largest inclusion-minimal) power-domination numbers are
\[
\gamma_P(G_n)=\begin{cases}2,&n=5,\\3,&n\ge6,\end{cases}
\qquad
\Gamma_P(G_n)=\begin{cases}2,&n=5,\\3,&n=6,7,\\n-4,&n\ge8.\end{cases}
\]
The general upper bound on the minimum \(\gamma_P(G_n)\) is not by itself asserted to be new; the theorem's substantive content is the full feasibility criterion, enumerator, all minimal sets and the unbounded minimal-size gap.

## Assumptions and scope
All graphs are finite, simple and undirected. The notation \(G_n=KG(n,2)\) denotes the Kneser **disjointness** graph, not its complement, the triangular or Johnson graph. Given a selected set \(S\), the power-domination process first observes the **closed neighborhood** \(N[S]\). It then repeatedly applies the zero-forcing rule: any observed vertex with exactly one unobserved neighbor observes that neighbor. Successful observation of all vertices defines a power-dominating set. The empty set is never successful. Inclusion-minimal means that no proper subset is successful. The upper parameter \(\Gamma_P\) is the largest cardinality of such a minimal set.

We view each selected Kneser vertex as an edge of \(K_n\). A pair in the ground set is initially *white* precisely when it is not selected and intersects every selected pair. Since power domination is monotone under adding selected vertices, it is enough to understand families of two and three edges and larger stars.

## Proof
**Step 1 (at most two selections).** One selected pair, say \(12\), leaves the \(2(n-2)\) pairs \(1x,2x\) (with \(x\notin\{1,2\}\)) unobserved. Every observed vertex of the form \(xy\), \(x,y\notin\{1,2\}\), has \(2(n-4)\ge2\) unobserved neighbors, and the selected pair has none. Hence propagation never starts.

For two disjoint selected pairs \(12,34\), the four unobserved vertices are \(13,14,23,24\). An observed pair has an even number of neighbors in this four-cycle of candidates: zero, two or four; thus no force occurs. For two intersecting selections \(12,13\), the unobserved pairs are \(23\) and \(1x\) for \(x=4,\dots,n\). Any observed vertex not selected is a pair avoiding \(1\), and it has exactly \(n-4\) unobserved neighbors (whether it meets \(23\) or not); the selected vertices have none. Hence this set stalls for \(n\ge6\). When \(n=5\), the observed vertex \(24\) forces \(15\), then \(25\) forces \(14\), and then \(45\) forces \(23\). Thus precisely the intersecting pairs of selected vertices succeed among all two-element sets when \(n=5\). Their number is \(n\binom{n-1}{2}=30\).

**Step 2 (nonstar triples).** Let \(S\) consist of three ground-set edges without a common endpoint. Up to isolated ground-set points, the three-edge graph \(([n],S)\) is a triangle, a three-edge path, a path of length two together with a disjoint edge, or a matching of three edges. A white pair is a *two-vertex cover* of this three-edge graph that is not itself a selected edge. In the four cases respectively there are \(0,2,2,0\) such white pairs: in a three-edge path \(ab,bc,cd\) they are \(ac,bd\), and in a path-plus-edge \(ab,bc,de\) they are \(bd,be\). (For the triangle, its three two-vertex covers are the three selected edges.)

If there are two white vertices \(e\ne f\), choose a ground-set point \(x\in f\setminus e\) and a point \(y\notin e\cup f\), possible because \(n\ge5\) and \(|e\cup f|\le4\). The Kneser vertex \(xy\) is disjoint from \(e\) but meets \(f\). Because \(e,f\) exhaust the white vertices, \(xy\) is observed; it has exactly one white neighbor, \(e\), and forces it. Once a single vertex remains white, any one of its observed neighbors can force it, since \(KG(n,2)\) has positive degree \(\binom{n-2}{2}\). Consequently **every nonstar three-element family is power dominating**.

**Step 3 (stars).** Let \(S\) be a star of size \(k\ge3\) with center \(c\). Its initially unobserved vertices are exactly the \(r=n-1-k\) unselected spokes \(cx\). Indeed any nonspoke \(uv\) is disjoint from some selected spoke \(ct\), because among at least three selected leaves at least one lies outside \(\{u,v\}\). Any observed nonspoke \(uv\) has precisely \(r-|\{u,v\}\cap U|\) white neighbors, where \(U\) is the set of \(r\) missing leaves. Selected spokes have none. If \(r\ge4\), every observed vertex has either zero or at least two white neighbors; the process is stuck. If \(r=3\), a nonspoke containing two missing leaves forces the third missing spoke. With two missing leaves, a nonspoke pairing one missing leaf and one selected leaf forces the other missing spoke. With one missing leaf, a nonspoke joining two selected leaves forces it. The indicated nonspoke vertices are all already observed, and the latter constructions are available because \(k\ge3\). Thus every such star succeeds exactly when \(r\le3\), equivalently \(k\ge n-4\).

**Step 4 (all set sizes).** A family containing a nonstar triple succeeds by Step 2 and monotonicity. Conversely, any family of at least three edges that is not a star contains a nonstar triple: if two edges are disjoint, choose any third; otherwise pairwise-intersecting edges have either a common center or form a triangle, and a nonstar triple appears whenever there is no common center for the whole family. Therefore Step 3 accounts for every remaining family of size at least three. For \(n=5\), every triple of edges of \(K_5\) contains two intersecting edges (three disjoint edges would use six vertices), so monotonicity of the successful intersecting pairs from Step 1 proves that all families of size at least three succeed. For \(n=6,7\), every three-element family succeeds, because the star case has \(r\le3\). For \(n\ge8\) the characterization in the theorem follows directly.

**Step 5 (polynomial and inclusion minimality).** The number of three-element or larger selections is \(\sum_{k=3}^N\binom Nkz^k\). For \(n\ge8\), the only unsuccessful families among them are stars with \(3\le k\le n-5\). Such a star has a unique center, so there are \(n\binom{n-1}{k}\) of size \(k\). Subtraction gives the polynomial; Step 1 supplies the exceptional size-two term for \(n=5\).

For \(n\ge8\), every nonstar triple is minimal because no one- or two-element set succeeds. Every successful star of size \(n-4\) is minimal because removing one spoke leaves a stalled star with four missing spokes. All larger successful stars contain a smaller successful star, and every other successful set contains a nonstar triple; thus there are no further minimal sets. For \(n=6,7\), all triples are minimal; for \(n=5\), precisely the intersecting selected pairs are minimal. The two classes of minimal sets for \(n\ge8\) number \(\binom N3-n\binom{n-1}{3}\) and \(n\binom{n-1}{3}\); they sum to \(\binom N3\). Taking their smallest and largest sizes proves the formulas for \(\gamma_P\) and \(\Gamma_P\), completing the proof.

## Verification
The standalone `verify_power_kneser.py` independently constructs the Kneser disjointness adjacency masks, begins each trial from the union of closed neighborhoods of its selected vertices, and repeatedly performs the original one-white-neighbor forcing rule. It compares that result against the theorem's structural criterion and polynomial coefficients. It exhaustively examines all \(2^{10}+2^{15}+2^{21}\) selected subsets for \(n=5,6,7\); all subsets through size four for \(n=8,9\); all subsets through size three for \(n=10,11\); every predicted large inclusion-minimal star for \(8\le n\le13\), including every deletion; and 1,000 reproducibly seeded random selections for each \(8\le n\le13\). This totals **2,278,600** tested selections or minimality configurations, all passing. Execute `python verify_power_kneser.py` using only the Python standard library; its JSON output is included as `verify_power_kneser_output.json`. Finite verification supplements and does not replace the proof.

## Relationship to prior work
Brimkov et al., *Power domination polynomials of graphs* (public preprint 28 May 2018, arXiv:1805.10984), develops the polynomial framework and formulas for several families, but the inspected work does not derive the two-subset Kneser-graph classification. Cornet and Torres, *k-tuple domination on Kneser graphs* (public preprint 29 August 2023, arXiv:2308.15603), studies **static** domination in the same Kneser family, including the known three-vertex ordinary dominating sets. Consequently the upper bound \(\gamma_P(G_n)\le3\) by itself is already implicit in the literature; the power-forcing structural dichotomy and counts do not follow from that static minimum. Brešar, Kos and Torres, *Grundy domination and zero forcing in Kneser graphs* (DOI 10.26493/1855-3974.1881.384), studies **zero forcing**, with a different initial-state condition from power domination, and does not supply the all-set power-domination enumerator. Bjorkman et al., *Power Domination Reconfiguration* (DOI 10.1007/s44007-025-00187-5), defines and studies the upper power-domination parameter in general, not this Kneser classification.

## Limitations
The domain is precisely \(KG(n,2)\) for \(n\ge5\); higher-subset Kneser graphs and generalized power domination are not covered. No claim is made that the bound \(\gamma_P(G_n)\le3\) is independently new. Although closely relevant primary texts and indexed research records were searched and compared, an unindexed or differently named equivalent result cannot be ruled out. Independent mathematical auditing has not been performed.

## References
- Brimkov et al., *Power domination polynomials of graphs*, arXiv:1805.10984, https://arxiv.org/abs/1805.10984 (first publicly posted 2018-05-28).
- Cornet and Torres, *k-tuple domination on Kneser graphs*, arXiv:2308.15603, https://arxiv.org/abs/2308.15603 (first publicly posted 2023-08-29).
- Brešar, Kos and Torres, *Grundy domination and zero forcing in Kneser graphs*, DOI:10.26493/1855-3974.1881.384.
- Bjorkman et al., *Power Domination Reconfiguration*, DOI:10.1007/s44007-025-00187-5.
