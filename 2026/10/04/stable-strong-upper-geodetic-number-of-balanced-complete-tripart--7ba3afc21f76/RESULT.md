# Stable strong upper geodetic number of balanced complete tripartite graphs
## Finding
For every integer \(n\ge 12\),
\[
\operatorname{sg}^{+}(K_{n,n,n})=n+2.
\]
Moreover, a minimal strong geodetic set has cardinality \(n+2\) if and only if its intersections with the three partite classes have sizes given by a permutation of
\[
(2,2,n-2).
\]
Consequently the number of maximum-cardinality minimal strong geodetic sets is
\[
3\binom{n}{2}^{3}.
\]

## Assumptions and scope
Graphs are finite, simple, connected, and undirected. A strong geodetic set \(S\) is a vertex set for which one shortest path is fixed for every unordered pair of vertices of \(S\), with the union of the fixed paths covering all vertices. It is minimal if no proper subset is strong geodetic. The strong upper geodetic number \(\operatorname{sg}^{+}(G)\) is the maximum cardinality of a minimal strong geodetic set.

Let the partite classes of \(K_{n,n,n}\) be \(V_1,V_2,V_3\). For a set \(S\), write
\[
s_i=|S\cap V_i|,\qquad t_i=n-s_i,\qquad p_i=\binom{s_i}{2},
\]
and put \(T=t_1+t_2+t_3\) and \(P=p_1+p_2+p_3\).

The theorem is a stable-range statement for \(n\ge 12\). It does not claim the strong upper geodetic number for smaller balanced tripartite graphs or for arbitrary complete multipartite graphs.

## Proof
A selected pair lying in two different partite classes is adjacent, so its fixed geodesic has no internal vertex. A selected pair lying in one class \(V_j\) has distance two, and its fixed geodesic may use exactly one internal vertex from either of the two other classes. Thus each of the \(p_j\) selected pairs inside \(V_j\) is one slot that can cover at most one omitted vertex outside \(V_j\).

Therefore the omitted vertices and the same-class selected pairs form a capacitated matching problem with three demand classes. Hall's condition reduces to
\[
S\text{ is strong geodetic}
\quad\Longleftrightarrow\quad
T\le P
\quad\text{and}\quad
t_i\le P-p_i\ \text{ for }i=1,2,3. \tag{1}
\]
Indeed, a demand subset contained in one part has exactly the slots from the other two parts available, giving the three single-part inequalities. Any demand subset meeting at least two parts has all three slot classes available, so the total inequality is sufficient for every remaining Hall constraint.

We use two elementary inequalities. First, if \(1\le a\le b\le c\) and \(a+b+c\ge14\), then
\[
\binom a2+\binom b2+\binom c2
\ge 3a+2b+2c-6. \tag{2}
\]
For \(a\ge5\), the difference between the two sides is coordinatewise nondecreasing and is already \(1\) at \((5,5,5)\). For \(a=4,3,2,1\), the smallest admissible sums of \(b+c\) are respectively \(10,11,12,13\); convexity in \(b,c\) reduces the minima to \((b,c)=(5,5),(5,6),(6,6),(6,7)\), where the differences are respectively \(0,3,7,13\).

Second, if \(2\le b\le c\) and \(b+c\ge14\), then
\[
\binom{b-1}{2}+\binom c2\ge 2b+2c-5. \tag{3}
\]
For \(b=2,3,4\) this follows directly from \(c\ge12,11,10\), respectively. For \(b\ge5\), use
\[
\binom{b-1}{2}\ge2b-5,\qquad \binom c2\ge2c.
\]

For the lower bound, choose \(S\) with part counts \((2,2,n-2)\). Then
\[
(t_1,t_2,t_3)=(n-2,n-2,2),\qquad
(p_1,p_2,p_3)=\left(1,1,\binom{n-2}{2}\right),
\]
so (1) holds for \(n\ge12\). If one selected vertex is deleted from either two-vertex part, then the two omitted vertices in the large selected part have only one available pair-slot outside that part. If one selected vertex is deleted from the \((n-2)\)-vertex part, then that part has three omitted vertices but only two pair-slots outside it. Hence every one-vertex deletion fails (1), so \(S\) is minimal. Thus
\[
\operatorname{sg}^{+}(K_{n,n,n})\ge n+2. \tag{4}
\]

For the upper bound, suppose a strong geodetic set has at least \(n+3\) vertices. If it meets all three parts, order the counts as \(1\le a\le b\le c\). Then \(n\le a+b+c-3\). Delete one selected vertex from the \(a\)-part. The new demand in that part satisfies
\[
n-a+1\le b+c-2\le\binom b2+\binom c2.
\]
The new demand in the \(b\)-part satisfies
\[
n-b\le a+c-3\le\binom{a-1}{2}+\binom c2,
\]
and similarly for the \(c\)-part. For total demand, (2) gives
\[
\binom{a-1}{2}+\binom b2+\binom c2
\ge2a+2b+2c-5,
\]
whereas the new total number of omitted vertices is at most \(2a+2b+2c-8\). Thus (1) still holds after the deletion, so the original set was not minimal.

If one part is empty, write the other counts as \(0<b\le c\). From \(b+c\ge n+3\) and \(c\le n\), we have \(b\ge3\). Delete one selected vertex from the \(b\)-part. The new demands are bounded by
\[
n\le b+c-3,\qquad n-b+1\le c-2,\qquad n-c\le b-3.
\]
Inequality (3), together with the obvious one-part capacity bounds, verifies all four conditions in (1). Hence this set is also not minimal. Two empty parts are impossible because the set has more than \(n\) vertices. Therefore every minimal strong geodetic set has size at most \(n+2\). Together with (4), this proves the value.

It remains to classify equality. Let a minimal strong geodetic set have exactly \(n+2\) vertices. If one part is empty, its counts are \((0,b,c)\) with \(b+c=n+2\). Deleting one selected vertex from the \(b\)-part leaves total demand \(2b+2c-5\), which is at most the available pair capacity by (3); the three individual demands are also within capacity. Thus an equality set cannot have an empty part.

Now order its positive counts as \(1\le a\le b\le c\), so
\[
a+b+c=n+2\ge14.
\]
Delete one selected vertex from the \(a\)-part. Inequality (2) gives the total Hall condition exactly:
\[
\binom{a-1}{2}+\binom b2+\binom c2
\ge 2a+2b+2c-5,
\]
which equals the new total demand. The demands in the \(a\)- and \(b\)-parts are also within capacity. For the \(c\)-part the required inequality is
\[
a+b-2\le\binom{a-1}{2}+\binom b2. \tag{5}
\]
Under \(1\le a\le b\), (5) fails only for \((a,b)=(2,2)\): if \(a=1\), then \(\binom b2\ge b-1\); if \(a=2\), it holds for \(b\ge3\); if \(a=3\), it holds already at \(b=3\); and if \(a\ge4\), each term supplies the needed linear bound. Hence, unless \(a=b=2\), deleting from the smallest part preserves strong geodeticity and contradicts minimality.

Therefore every equality set has sorted counts \((2,2,n-2)\). The lower-bound construction already proved every such set is minimal. There are three choices for the large part and \(\binom n2\) choices of the two selected vertices in each small part, while choosing \(n-2\) vertices in the large part is equivalent to choosing its two omitted vertices. Hence the number of equality sets is \(3\binom n2^3\).

## Verification
The accompanying `verify.py` implements the coverage problem independently as a maximum-flow instance between omitted-vertex demand classes and selected-pair slot classes. It enumerates every possible part-count triple for each \(12\le n\le30\), tests strong-geodetic feasibility by flow, tests minimality by every one-vertex deletion, and confirms both the value \(n+2\) and the three permutations of \((2,2,n-2)\) as the only maximum patterns.

The archived output is:
`VERIFY_OK`
`checked n=12..30 by independent max-flow enumeration`
`the infinite theorem rests on the accompanying proof`

The finite computation corroborates the structural proof but is not used to infer the theorem for arbitrary \(n\).

## Relationship to prior work
The 2021 paper introducing the strong upper geodetic number develops the parameter and several graph families but does not state a complete-tripartite or complete-multipartite formula of this kind. A 2018/2019 paper on complete multipartite graphs treats the ordinary strong geodetic number, which minimizes the cardinality of a strong geodetic set and is therefore a different optimization problem.

The closest published published-finding corpus finding determines the strong upper geodetic number of complete bipartite graphs and classifies its maximum minimal sets. The present theorem is not a direct substitution into that rank-two result: with three partite classes, omitted vertices in one class can be assigned to pair-slots from either of two other classes, and the proof requires the three-class Hall system (1). The stable classification \((2,2,n-2)\) and its count are not contained in the bipartite statement.

## Limitations
Originality is a best-of-knowledge conclusion, not an independent literature audit. Exact and alias searches covered the defining strong-upper paper, strong-geodetic work on complete multipartite graphs, the published complete-bipartite strong-upper result, and nearby strong edge-geodetic literature. Differently phrased or inaccessible work could still contain an equivalent theorem.

The theorem is restricted to balanced complete tripartite graphs in the stable range \(n\ge12\). It makes no claim that \(12\) is the first possible threshold for every related structural property, and it does not classify smaller orders or arbitrary part sizes. No independent audit, formal proof-assistant verification, or expert attestation has been performed.

## References
1. L. G. Bino Infanta and D. Antony Xavier, *Strong Upper Geodetic Number of Graphs*, Communications in Mathematics and Applications 12(3) (2021), 737–748, DOI `10.26713/cma.v12i3.1597`.
2. V. Iršič and M. Konvalinka, *Strong geodetic problem on complete multipartite graphs*, Ars Mathematica Contemporanea 17 (2019), arXiv `1806.00302`, DOI `10.26493/1855-3974.1725.2e5`.
3. *Strong upper geodetic number of complete bipartite graphs*, published published-finding corpus finding `2026/9/30/SCOPE-strong-upper-geodetic-number-of-complete-bipartite-graphs--19a81b4f67a5`.
