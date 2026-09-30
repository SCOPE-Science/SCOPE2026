# Strong upper geodetic number of complete bipartite graphs
## Finding
Let \(G=K_{a,b}\) with bipartition \(A\cup B\) and \(1\le a\le b\). Then the strong upper geodetic number is
\[
\operatorname{sg}^{+}(K_{a,b})=
\begin{cases}
2,&a=b=1,\\
b,&a=1<b,\\
b+1,&2\le a\le b.
\end{cases}
\]
For \(2\le a<b\), every maximum-cardinality minimal strong geodetic set contains exactly two vertices of \(A\) and exactly \(b-1\) vertices of \(B\). Hence there are exactly \(\binom{a}{2}b\) such maximum sets.

For the balanced graph \(K_{n,n}\), \(n\ge2\), write \((s,t)=(|S\cap A|,|S\cap B|)\). The possible pairs for maximum-cardinality minimal strong geodetic sets are
\[
\begin{array}{c|c}
n& (s,t)\\ \hline
2&(1,2),(2,1)\\
3&(2,2)\\
4&(2,3),(3,2)\\
5&(2,4),(3,3),(4,2)\\
n\ge6&(2,n-1),(n-1,2).
\end{array}
\]
Consequently the numbers of maximum sets are respectively \(4,9,48,200\), and \(n^2(n-1)\) for \(n\ge6\). For \(K_{1,b}\) with \(b>1\), the unique maximum set is the part of size \(b\).

## Assumptions and scope
Graphs are finite, simple, connected, and undirected. A strong geodetic set \(S\) is a vertex set for which one shortest path is fixed for each unordered pair of vertices of \(S\), with the union of those fixed paths covering every vertex. A strong geodetic set is minimal if none of its proper subsets is strong geodetic. The strong upper geodetic number \(\operatorname{sg}^{+}(G)\) is the maximum cardinality of a minimal strong geodetic set.

The result concerns complete bipartite graphs only. It uses the strong-upper parameter introduced in the cited 2021 work and is distinct from the ordinary strong geodetic number \(\operatorname{sg}(K_{a,b})\), which minimizes over all strong geodetic sets.

## Proof
Fix \(S\subseteq V(K_{a,b})\), and put
\[
s=|S\cap A|,\qquad t=|S\cap B|,\qquad q_A=a-s,\qquad q_B=b-t.
\]
A vertex omitted from \(A\) can occur internally only on a length-two geodesic joining two selected vertices of \(B\). Each selected pair in \(B\) supplies one fixed geodesic and therefore can cover at most one omitted vertex of \(A\). Conversely, distinct selected pairs in \(B\) may be assigned to distinct omitted vertices of \(A\). The same statement holds with the parts interchanged. Hence
\[
S\text{ is strong geodetic}\quad\Longleftrightarrow\quad
q_A\le \binom{t}{2}\text{ and }q_B\le\binom{s}{2}. \tag{1}
\]
The strong-geodetic property is upward closed: if \(S\) is strong geodetic, every superset of \(S\) is strong geodetic after retaining the old fixed paths and choosing arbitrary shortest paths for the new pairs. Therefore a strong geodetic set is minimal exactly when deleting any one of its vertices destroys property (1).

First suppose \(a=b=1\). The graph is \(K_2\), so both vertices are required and \(\operatorname{sg}^{+}(K_{1,1})=2\).

Now suppose \(a=1<b\). Taking all \(b\) vertices of \(B\) is strong geodetic: one selected pair can route through the unique vertex of \(A\), and deleting any selected vertex leaves an omitted vertex of \(B\) but no selected pair in \(A\) to cover it. Thus this set is minimal. The only larger set is all of \(V(G)\), which is not minimal because deleting the vertex of \(A\) leaves the preceding strong geodetic set. Hence \(\operatorname{sg}^{+}(K_{1,b})=b\).

Assume henceforth \(2\le a\le b\). For the lower bound choose two vertices of \(A\) and all but one vertex of \(B\). Then \(s=2\), \(t=b-1\), \(q_A=a-2\), and \(q_B=1\). Since
\[
a-2\le \binom{b-1}{2},\qquad 1=\binom{2}{2},
\]
condition (1) holds. If a selected vertex of \(A\) is deleted, only one selected vertex remains in \(A\), so the omitted vertex of \(B\) cannot be covered. If a selected vertex of \(B\) is deleted, then two vertices of \(B\) are omitted but the two selected vertices of \(A\) provide only one same-part pair. Thus the set is minimal and has size \(b+1\).

For the upper bound, suppose a minimal strong geodetic set satisfies \(|S|\ge b+2\). Then
\[
q_A+q_B=a+b-|S|\le a-2.
\]
Consequently
\[
s=a-q_A\ge q_B+2,\qquad t=b-q_B\ge q_A+2.
\]
Delete any selected vertex of \(A\). The new parameters are \(s-1,t,q_A+1,q_B\). Since
\[
q_A+1\le t-1\le\binom{t}{2},
\]
and, because \(s-1\ge q_B+1\),
\[
q_B\le\binom{q_B+1}{2}\le\binom{s-1}{2},
\]
condition (1) still holds, contradicting minimality. Therefore \(|S|\le b+1\), and the value formula follows.

It remains to classify the maximum sets for \(a\ge2\). If \(|S|=b+1\), put \(q=q_B\). Then
\[
s=q+1,\qquad t=b-q,\qquad q_A=a-1-q. \tag{2}
\]
For \(q=1\), both possible one-vertex deletions fail condition (1), so every set with the counts in (2) is minimal. If \(q=0\), minimality is possible only when \(a>\binom b2\), which under \(2\le a\le b\) occurs only at \((a,b)=(2,2)\). If \(q=2\), deletion from \(B\) is still strong exactly when \(a-3\le\binom{b-3}{2}\); hence minimality occurs only for \((a,b)=(4,4)\) or \((5,5)\). Finally let \(q\ge3\). Both deletion-side capacity inequalities become active. Feasibility together with failure after an \(A\)-deletion forces
\[
a-1-q=\binom{b-q}{2}.
\]
Since \(a\le b\), the left side is at most \(b-q-1\); therefore \(b-q\le2\). The case \(b-q=1\) cannot also fail after a \(B\)-deletion, so \(b-q=2\), which forces \(a=b\) and \(q=b-2\). This is possible for \(b\ge5\). Combining these cases gives exactly the displayed balanced patterns and the unique unbalanced pattern \((s,t)=(2,b-1)\). Counting choices inside the two parts gives the stated enumeration.

## Verification
The accompanying `verify.py` independently builds every labeled complete bipartite graph \(K_{a,b}\) with \(1\le a\le7\) and \(a\le b\le8\). It tests every vertex subset. Strong-geodetic feasibility is checked by explicit bipartite matching between omitted vertices and available selected same-part geodesic slots rather than by directly invoking formula (1). Minimality is then tested by all one-vertex deletions. The program checks the exact value, every maximum-set part-count pattern, and every maximum-set count. Its archived output is `VERIFY_OK types 35 subsets 108204 minimal_sets 14183 max_sets 1625`.

## Relationship to prior work
The 2021 paper *Strong Upper Geodetic Number of Graphs* introduces \(\operatorname{sg}^{+}\), proves general NP-completeness, and gives values or bounds for several graph families. Its full-text main-results section does not state the complete-bipartite formula above. Earlier work on complete bipartite graphs determines the ordinary strong geodetic number \(\operatorname{sg}(K_{a,b})\), a minimum parameter, rather than the maximum size of a minimal strong geodetic set. The present result therefore addresses the upper analogue on the same benchmark family and additionally classifies and counts all maximum minimal sets.

## Limitations
Originality is best-of-knowledge, not an independent literature audit. Searches covered the defining strong-upper paper, exact complete-bipartite terminology, notation variants, ordinary strong-geodetic results, and later strong-geodetic variants, but differently phrased or inaccessible work may exist. The computational verification is finite and corroborative; the theorem for arbitrary \(a,b\) rests on the proof above. No independent audit, formal proof-assistant verification, or expert attestation has been performed.

## References
1. L. G. Bino Infanta and D. Antony Xavier, *Strong Upper Geodetic Number of Graphs*, Communications in Mathematics and Applications 12(3) (2021), 737–748, DOI `10.26713/cma.v12i3.1597`.
2. V. Iršič, *Strong Geodetic Number of Complete Bipartite Graphs and of Graphs with Specified Diameter*, Graphs and Combinatorics 34(3) (2018), 443–456, arXiv `1708.02416`, DOI `10.1007/s00373-018-1885-9`.
3. V. Gledel and V. Iršič, *Strong geodetic number of complete bipartite graphs, crown graphs and hypercubes*, arXiv `1810.04004`.
