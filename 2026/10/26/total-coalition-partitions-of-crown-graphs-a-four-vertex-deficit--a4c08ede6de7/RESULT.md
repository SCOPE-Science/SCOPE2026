# Total coalition partitions of crown graphs: a four-vertex deficit and an exact optimum census

## Finding

Let \(\operatorname{Cr}_n\) be the crown graph obtained from \(K_{n,n}\) by removing a perfect matching, with \(n\ge 3\). A total coalition partition is a partition into nonempty vertex classes, none of which totally dominates the graph, in which every class can be united with some *other* class to form a total dominating set. Write \(TC(G)\) for the largest number of classes in such a partition, and \(M(G)\) for the number of optimal **unlabelled-block partitions** of the labelled vertices of \(G\).

**Theorem.** For every integer \(n\ge3\),
\[
TC(\operatorname{Cr}_n)=
\begin{cases}
3,&n=3,\\
2n-4,&n\ge4,
\end{cases}
\qquad
M(\operatorname{Cr}_n)=
\begin{cases}
48,&n=3,\\
857,&n=4,\\
\bigl(n(n-1)(n-2)/2\bigr)^2,&n\ge5.
\end{cases}
\]
For every \(n\ge5\), every optimal partition consists of exactly one three-vertex block meeting the two bipartition classes in \((1,2)\) vertices, exactly one three-vertex block of profile \((2,1)\), and the remaining \(2n-6\) vertices as singleton blocks. Conversely, each such choice is optimal. Thus the optimum has a unique profile for \(n\ge5\), even though its labelled realizations vary.

## Assumptions and scope

Write the bipartition as \(U=\{u_1,\ldots,u_n\}\) and \(V=\{v_1,\ldots,v_n\}\), with \(u_i v_j\in E(\operatorname{Cr}_n)\) exactly when \(i\ne j\). Graphs are finite, simple and undirected. A set \(D\) is **total dominating** when every vertex, including every member of \(D\), has a neighbor in \(D\). A total coalition consists of disjoint sets \(A,B\) that are each not total dominating but for which \(A\cup B\) is total dominating. Classes of partitions have no names: permuting classes does not create a new partition.

For any class \(B\), its **profile** is \((a(B),b(B))=(|B\cap U|,|B\cap V|)\). The profile criterion below is particular to the deleted-perfect-matching graph and must not be used for arbitrary bipartite graphs.

## Proof

**1. Profile criterion.** A subset \(D\) totally dominates \(\operatorname{Cr}_n\) if and only if \(|D\cap U|\ge2\) and \(|D\cap V|\ge2\). Indeed, a selected single \(u_i\) has no edge to \(v_i\), so a set with at most one selected \(U\)-vertex cannot totally dominate all of \(V\). Conversely, any two distinct selected vertices of \(U\) include a neighbor of each vertex of \(V\), and symmetrically for the other side. Hence, each legal partition class has either its first or its second profile coordinate at most one, and two distinct legal classes with profiles \((a,b)\) and \((c,d)\) form a coalition exactly when \(a+c\ge2\) and \(b+d\ge2\).

**2. The deficit and its small values.** For a partition \(\Pi\), define \(\varepsilon(\Pi)=\sum_{B\in\Pi}(|B|-1)=2n-|\Pi|\). If \(\varepsilon\le t\), the number of nonsingleton blocks is at most \(t\), and altogether they use at most \(2t\) vertices. A singleton of profile \((1,0)\) must partner a class of profile \((1,b)\) with \(b\ge2\), which costs at least two units of deficit; analogously a \((0,1)\) singleton needs a distinct class of profile \((a,1)\) with \(a\ge2\), also costing at least two. Therefore the simultaneous presence of singleton classes on both sides forces \(\varepsilon\ge4\).

Suppose instead that there is no singleton from \(U\). Whenever \(2n>2\varepsilon\), there must then be a singleton from \(V\), since otherwise all vertices would lie in nonsingleton classes. Any such \(V\)-singleton needs a partner of profile \((h,1)\), where \(h\ge2\); this partner costs \(h\) units of deficit. Every other \(U\)-vertex must also lie in a nonsingleton class.

If \(n\ge4\) and \(\varepsilon\le3\), then \(2n>2\varepsilon\). If \(h\ge3\), the partner uses all available deficit but still contains fewer than \(n\) of the \(U\)-vertices. If \(h=2\), the remaining deficit is at most one, and the at least two remaining \(U\)-vertices can fit only in one pure-\(U\) pair \((2,0)\); that pair has no partner with two \(V\)-vertices. Both cases contradict the coalition requirement. By symmetry, there must be singletons from both sides. Consequently \(\varepsilon\ge4\) for every \(n\ge4\).

For \(n=3\), the analogous argument with \(\varepsilon\le2\) also excludes the absence of either type of singleton: a \(V\)-singleton would require \((2,1)\), already using both deficit units, forcing the last \(U\)-vertex to be another singleton with no suitable partner. Both singleton types together would require deficit at least four. Thus \(\varepsilon\ge3\) when \(n=3\).

**3. Rigidity when \(n\ge5\) and \(\varepsilon\le4\).** Assume no \(U\)-singleton. Since \(2n\ge10>8\), at least one \(V\)-singleton exists. Its necessary partner has profile \((h,1)\), with \(2\le h\le4\) and deficit \(h\). If \(h=4\), no other nonsingleton can contain the missing \(U\)-vertices. If \(h=3\), at least two more \(U\)-vertices require a pure-\(U\) pair, consuming the last deficit unit, but that pair has no partner with two \(V\)-vertices. If \(h=2\), at least three further \(U\)-vertices must occupy nonsingleton classes within two remaining deficit units. At least one of these classes must be pure-\(U\), since a mixed class consumes at least one deficit unit per \(U\)-vertex it contains. A pure-\(U\) class needs a *different* class containing at least two \(V\)-vertices; such a class uses at least one of the two remaining deficit units. The one residual unit can then accommodate at most two additional \(U\)-vertices, again too few. This contradiction proves that a \(U\)-singleton exists, and symmetry gives a \(V\)-singleton.

Their respective partners are distinct and each costs at least two deficit units. Because the total deficit is at most four, the only possible nonsingleton classes have profiles \((1,2)\) and \((2,1)\). All other classes are singleton classes. This also proves \(\varepsilon\ge4\). Conversely, for \(n\ge5\) choose disjoint classes with the two stated profiles and leave everything else singleton. Each singleton can partner the appropriate triple, and the two triples can partner each other, so this is a total coalition partition. It has \(2n-4\) classes and is optimal.

For \(n=4\), the four classes \(\{u_i,v_i\}\), \(i=1,2,3,4\), each have profile \((1,1)\). Any two unite to a total dominating set, giving four classes, matching the upper bound. For \(n=3\), the analogous three classes give a feasible three-class partition, matching its upper bound.

**4. Number of optimal partitions.** For \(n\ge5\), choose the vertices in the unique profile-\((1,2)\) class and then the disjoint profile-\((2,1)\) class. There are
\[
\binom n1\binom n2\binom{n-1}2\binom{n-2}1
=\left(\frac{n(n-1)(n-2)}2\right)^2
\]
choices; all other vertices must be singleton classes. The two exceptional classes have different profiles, so no division by two is required.

For the two small orders, the complete block-profile census is finite and can be evaluated exactly. If a profile multiset \(\mathcal P\) has \(m_{a,b}\) blocks of profile \((a,b)\), with total first and second coordinates both equal to \(n\), it contributes precisely
\[
W(\mathcal P)=\frac{(n!)^2}{\displaystyle\prod_{a,b}(a!b!)^{m_{a,b}}m_{a,b}!}
\]
unlabelled-block partitions of the labelled vertices. It is admissible exactly when no profile has both coordinates at least two, and every profile has a *distinct occurrence* whose coordinatewise sum has both coordinates at least two. For \(n=3\), the only three-class profiles, up to swapping \(U\) and \(V\), contribute \(6\), \(2\cdot18\), and \(2\cdot3\), totaling \(48\). For \(n=4\), the complete four-class profile census, grouped under swapping the two sides, contributes
\[
144+2(144)+2(72)+72+2(48)+2(36)+24+9+2(4)=857.
\]
The standalone checker `verify_coalitions.py` lists all profile multisets by exhaustive generation from the above profile criterion and computes each \(W(\mathcal P)\) exactly. It also independently enumerates all vertex set partitions and tests total domination using the actual graph edges for \(n=3,4,5\); the results agree. These are exhaustive *finite* verifications for the exceptional orders, whereas the general \(n\ge5\) statement follows from Steps 1--3.

## Verification

Run `python verify_coalitions.py` with Python 3.9 or newer. Its profile calculation checks the extremal count for \(3\le n\le9\), producing \(48,857,900,3600,11025,28224,63504\). An independent graph-adjacency enumeration gives the same extremal values and counts for \(n=3,4,5\). The checker is not used as an oracle for the unbounded-\(n\) theorem: Step 3 handles those quantifiers symbolically.

## Relationship to prior work

Alikhani, Bakhshesh and Golmohammadi introduced total coalitions and proved general bounds, including \(TC(G)\ge\delta(G)+1\) for isolate-free graphs without a universal vertex, and determined \(TC(C_m)\) for cycles. Since \(\operatorname{Cr}_3\cong C_6\), the scalar value \(TC(\operatorname{Cr}_3)=3\) is already covered by their cycle theorem; it is **not** claimed as original. For \(n\ge5\), their general lower bound gives only \(TC(\operatorname{Cr}_n)\ge n\), whereas the classification here yields \(2n-4\) and every attaining partition. Barát and Blázsik established general maximum-degree upper bounds and constraints on total-coalition graphs, without the specific crown-graph optimal profiles or census in the inspected text. The novelty claimed here concerns the entire \(n\ge5\) classification and exact counts, together with the finite optimal-profile census at the first non-cycle boundary \(n=4\).

Ordinary coalition partitions, total restrained coalitions, and other domination-related partitions have different requirements and do not automatically entail the statement here.

## Limitations

The proof treats the exact crown family \(K_{n,n}-M\) with \(n\ge3\) and does not cover deletion of an incomplete matching or arbitrary near-complete bipartite graphs. The two small-order census values depend on exhaustive but fully specified finite profile summation, independently checked against actual adjacency. Prior published work covers the cycle case's scalar extremal number. Literature priority beyond the inspected sources, including unindexed treatments of total coalitions in crown graphs or the three-cube, cannot be ruled out. No independent mathematical audit has been performed.

## References

1. S. Alikhani, D. Bakhshesh and H. Golmohammadi, *Introduction to total coalitions in graphs*, arXiv:2211.11590, first submitted 21 November 2022, version 2 (10 December 2022), https://arxiv.org/html/2211.11590v2 .
2. J. Barát and Z. L. Blázsik, *General sharp upper bounds on the total coalition number*, arXiv:2301.09979, first submitted 24 January 2023, https://arxiv.org/abs/2301.09979 .
3. T. W. Haynes, J. T. Hedetniemi, S. T. Hedetniemi, A. A. McRae and R. Mohan, *Introduction to coalitions in graphs*, AKCE International Journal of Graphs and Combinatorics 17 (2020), 653--659, https://doi.org/10.1080/09728600.2020.1832874 .
