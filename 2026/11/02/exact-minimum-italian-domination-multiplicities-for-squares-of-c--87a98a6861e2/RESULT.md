# Exact minimum Italian-domination multiplicities for squares of cycles

## Finding

For every integer \(n\ge5\), let \(G_n=C_n^2\) be the square of the simple cycle, on the vertex set \(\mathbb Z/n\mathbb Z\); its four neighbours at each vertex are the positions differing by one or two. An Italian dominating function is \(f:V(G_n)\to\{0,1,2\}\) such that every \(v\) with \(f(v)=0\) satisfies \(\sum_{u\sim v}f(u)\ge2\). Write \(\omega(f)=\sum_v f(v)\), \(\gamma_I(G_n)=\min_f\omega(f)\), and let \(a_n\) be the number of minimum-weight functions.

The minimum weight \(\gamma_I(G_n)=\lceil n/3\rceil\) was established in earlier work on web graphs [2]. The **new** assertion is the full extremizer count

\[
a_n=
\begin{cases}
3,&n\equiv0\pmod3,\\
n+10\mathbf1_{n=5},&n\equiv2\pmod3,\\
\dfrac{n(n+5)}6+10\mathbf1_{n=10},&n\equiv1\pmod3.
\end{cases}
\]

The indicator \(\mathbf1_{n=k}\) equals one when \(n=k\) and zero otherwise. All counts refer to the graph with explicitly labelled cyclic positions; configurations related by rotation are counted separately. A complete structural classification follows.

Every minimum function is \(\{0,1\}\)-valued except when \(n=5\) or \(n=10\). The five additional minimum functions on \(G_5\) consist of a single vertex labelled \(2\) and all remaining vertices labelled \(0\). The five additional minimum functions on \(G_{10}\) consist of two vertices at cyclic separation five, both labelled \(2\), with all other labels \(0\).

For a binary function, list its positive vertices in increasing clockwise order and write the cyclic positive-to-positive gaps, each gap including the clockwise distance between consecutive positive vertices. Precisely the following cyclic gap multisets/words occur among binary minimum functions:

* \(n\equiv0\pmod3\): every gap is \(3\).
* \(n\equiv2\pmod3\): one gap is \(2\), all others are \(3\); at \(n=5\), the word \((1,4)\) is an additional possibility.
* \(n\equiv1\pmod3\): either one gap is \(1\) and all others are \(3\), or two gaps are \(2\) and all others are \(3\); at \(n=10\), the alternating cyclic word \((1,4,1,4)\) is an additional possibility.

For example, \((a_5,a_6,a_7,a_8,a_9,a_{10})=(15,3,14,8,3,35)\).

## Assumptions and scope

All cycles are finite, undirected, simple, and labelled by \(\mathbb Z/n\mathbb Z\), with \(n\ge5\). The graph power is ordinary distance-two adjacency, not a graph product. The Italian rule is imposed only on zero-labelled vertices and uses their **open** neighbourhoods; it is not ordinary domination, a closed-neighbourhood \(2\)-domination condition, or perfect Italian domination. There is no quotient by dihedral symmetries. The claim concerns the coefficient of minimum degree in the Italian domination polynomial, not its higher coefficients.

## Proof

**1. A deficit identity and a sharp lower bound.** Fix any Italian dominating function and let \(t\) be the number of vertices labelled \(2\), \(p\) the number with positive labels, and \(W=\omega(f)\). Thus \(p=W-t\). Define
\[
A=\sum_{v:f(v)>0}\ \sum_{u\sim v}f(u)\ \ge0,\qquad
B=\sum_{v:f(v)=0}\Big(\sum_{u\sim v}f(u)-2\Big)\ge0.
\]
Every vertex has four neighbours, so double-counting the neighbour-label sums gives \(4W=A+2(n-p)+B\). Consequently
\[
2(3W-n)=2t+A+B.\tag{1}
\]
This shows \(W\ge\lceil n/3\rceil\). This value is attained by binary configurations whose clockwise positive-vertex gaps are all \(3\), except for one gap of \(2\) when \(n\equiv2\pmod3\), or two gaps of \(2\) when \(n\equiv1\pmod3\). Every zero in those configurations has at least two positive neighbours. Thus the minimum weight is \(w=\lceil n/3\rceil\) (also previously known [2]). For a minimizer put \(d=3w-n\in\{0,1,2\}\); (1) becomes
\[
2d=2t+A+B.\tag{2}
\]

**2. The double-label exceptions.** Equation (2) gives \(t\le d\le2\). In the case \(d=0\) there is no label \(2\). If \(d=1\) and \(t=1\), then \(A=B=0\). The lone positive vertex must be the single \(2\): otherwise its nearest positive vertex clockwise, necessarily a \(1\), would have to be at distance at least three from the \(2\) because \(A=0\). At clockwise separation three, the zeros at distances one and two from the \(2\) each have neighbour-weight at least three, forcing \(B\ge2\). At separation four, the zero at distance two has neighbour-weight at least three, forcing \(B\ge1\). At separation at least five, the zero three steps from the \(2\) cannot be defended by the next \(1\). All contradict \(B=0\). With no \(1\)-labels, a single \(2\) can defend every other vertex only if \(n=5\). The five singleton-\(2\) functions are all valid.

If \(d=2\) and \(t=2\), then \(A=B=0\), and no positive vertices can be adjacent in \(G_n\). From each \(2\), its next clockwise positive vertex must be exactly five steps away and also labelled \(2\): separations three and four create positive slack \(B\), and a separation at least six leaves the vertex three steps ahead undefended. Therefore \(n=10\), with the two \(2\)-labels five apart. There are precisely five such configurations, and they are valid.

It remains to exclude \(d=2,t=1\). In this case \(A+B=2\). A \(1\)-labelled neighbour of the unique \(2\) would contribute at least three to \(A\) (the two directed terms sum to \(2+1\)), so all \(1\)'s are at cyclic distance at least three from that \(2\). There is at least one \(1\), since \(n\ge7\) when \(d=2\). Take the closest positive clockwise after the \(2\), at distance \(g\ge3\), and note that it is labelled \(1\). If \(g\ge5\), the zero three steps after the \(2\) has neighbour-weight at most one and is not defended. If \(g=4\), the zero at distance two has excess neighbour-weight at least one, while defending the zero at distance three requires a further \(1\) at position five: these adjacent \(1\)'s contribute at least two to \(A\). Thus \(A+B\ge3\). Hence \(g=3\). The same argument in the anticlockwise direction forces the closest positive on that side also to be at distance three. The four zeros at cyclic distances \(1,2\) clockwise and anticlockwise from the \(2\) are distinct since \(n\ge7\), and each has neighbour-weight at least three. Therefore \(B\ge4\), a contradiction. All nonbinary minimizers have been classified.

**3. Cyclic gap criterion for binary labels.** Suppose the minimizer uses only zero and one. Its \(w\) positive vertices determine a cyclic gap word \((g_1,\ldots,g_w)\), where the gaps are positive integers summing to \(n\). A gap of length at least five is impossible: the zero at distance two after its left endpoint has only that endpoint among its four neighbours in the selected set. Gaps of lengths \(2\) and \(3\) are always harmless: each of their interior zeros sees both endpoints. A gap of length \(1\) has no interior zero. A gap of length \(4\) is permissible precisely if each immediately preceding and immediately following gap has length \(1\); these two neighbouring positive vertices supply the second defender of the zeros one step from either endpoint. All other zeros are then defended. This is a necessary and sufficient criterion for a binary function.

Let \(a,b,c\) be the numbers of gaps of length \(1,2,4\), respectively (all remaining gaps have length \(3\)). Since the gaps sum to \(n\) and their number is \(w\),
\[
d=3w-n=2a+b-c.\tag{3}
\]
Every length-four gap has a distinct preceding length-one gap, so \(c\le a\) and hence \(d\ge a+b\). Since \(d\in\{0,1,2\}\), this restricts all minima.

When \(d=0\), all gaps have length \(3\). When \(d=1\), either one length-two gap occurs or \(a=c=1,b=0\). The latter demands that the unique length-four gap be flanked on both sides by the same unique length-one gap; hence there are just two gaps, with cyclic word \((1,4)\) and \(n=5\). When \(d=2\), either there is one length-one gap, or two length-two gaps, or some length-four gap. The latter initially permits either \(a=c=1,b=1\) or \(a=c=2,b=0\). The first is impossible: with three or more gaps, a length-four gap cannot have a unique length-one gap on both sides. In the second case, the two length-four gaps must each be flanked by both length-one gaps; this is only possible for the four-gap cyclic word \((1,4,1,4)\), with \(n=10\). These cases yield exactly the gap-word classification stated above.

**4. Exact labelled counts.** A cyclic gap word of length \(w\), with \(s\) ordered gap sequences of the specified form, yields precisely \(ns/w\) binary assignments on the explicitly labelled cycle; it accounts for the \(w\) choices of the starting positive vertex. All gaps equal to \(3\) give \(n/w=3\) functions. One gap equal to \(2\) gives \(n\) functions. In the residue-one case, one gap equal to \(1\) gives \(n\), and two gaps equal to \(2\) give \(n(w-1)/2\), so the general count is \(n(w+1)/2=n(n+5)/6\). The exceptional binary word \((1,4)\) at \(n=5\) adds five; \((1,4,1,4)\) at \(n=10\) adds five. The nonbinary functions from Step 2 add five at each of those two orders. These give the exact displayed formula for every \(n\ge5\). \(\square\)

## Verification

The standard-library Python script `verify.py`, packaged alongside this document, contains two independently formulated checks: direct enumeration of all \(\{0,1,2\}\)-assignments of weight \(\lceil n/3\rceil\) for every \(5\le n\le18\), and an independently constructed cyclic four-memory minimum-weight transfer for every \(5\le n\le60\). It compares optimal weights and counts with the theorem and counts minima containing a \(2\). Running `python3 verify.py` prints `FINITE_VERIFICATION_OK` if every assertion passes. Both checks completed successfully on the packaged source. The proof above, rather than finite verification, supports all orders.

## Relationship to prior work

Ferrari, Leoni, and López Pujato [2, Proposition 2.7 and Corollary 2.8] determine the Italian and \(2\)-domination **numbers** for the broader class of web graphs; their result already implies \(\gamma_I(C_n^2)=\lceil n/3\rceil\). That minimum-weight equality is a cited premise/check here, not a novelty assertion. The new result counts and classifies *all* minimizers, including the sporadic weight-two vertices. Shao and Zhao [1] introduce and enumerate Italian domination polynomial coefficients for ordinary cycles and develop algorithms for paths, trees, and cycles, but their graph class is \(C_n\), not \(C_n^2\). The related integer \(\{k\}\)-domination work [3] has different local conditions and concerns optimal values, not this coefficient. The present theorem supplies the previously absent explicit coefficient \([z^{\lceil n/3\rceil}]D_I(C_n^2,z)\), conditional on the priority comparisons described in REVIEW.md.

## Limitations

This is a self-reviewed mathematical claim, not an independent assessment. The proof concerns the minimum Italian-domination coefficient only; it does not give all coefficients of the polynomial or characterize analogous minimizers for arbitrary higher powers of cycles. Historical priority is not exhaustively certified; a differently worded minimum \(2\)-dominating-set count for the web graph could potentially cover the binary subcases. The exact total includes nonbinary minimum functions at \(n=5,10\), which cannot be obtained from binary \(2\)-domination alone.

## References

[1] P. Shao and C. Zhao, *Counting Weight-\(k\) Italian Dominating Sets on Trees and Cycles*, first publicly submitted 2026-09-09, arXiv:2610.00108, https://arxiv.org/abs/2610.00108.

[2] V. Ferrari, V. Leoni, and M. I. López Pujato, *Characterizations of Italian graphs and Sicilian graphs*, RAIRO Operations Research 59 (2025), 239–249, DOI:10.1051/ro/2024218; author-accessible version https://ri.conicet.gov.ar/handle/11336/253057.

[3] Cheng, Fu, and Liu, *The integer \(\{k\}\)-domination number of circulant graphs*, Discrete Mathematics, Algorithms and Applications (2020), DOI:10.1142/S179383092050055X.
