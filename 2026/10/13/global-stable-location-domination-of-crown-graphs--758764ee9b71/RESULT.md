# Global stable location-domination of crown graphs
## Finding
Let
\[
\operatorname{Cr}_n=K_{n,n}-M,
\qquad n\ge3,
\]
be the crown graph with bipartition
\[
A=\{a_1,\ldots,a_n\},\qquad B=\{b_1,\ldots,b_n\},
\]
and deleted perfect matching
\[
M=\{a_i b_i:1\le i\le n\}.
\]
For a set \(S\subseteq V(\operatorname{Cr}_n)\), define its omitted-index sets by
\[
U=\{i:a_i\notin S\},\qquad V=\{i:b_i\notin S\}.
\]

Then \(S\) is a global stable locating-dominating set if and only if exactly one of the following holds.

1. There is an index \(i\) such that
\[
U=V=\{i\}.
\]
2. The omitted-index sets are disjoint,
\[
U\cap V=\varnothing,
\]
and they satisfy the boundary conditions
\[
U=\varnothing\Longrightarrow |V|\le n-2,
\]
\[
V=\varnothing\Longrightarrow |U|\le n-2,
\]
and, when both are nonempty,
\[
|U|\le n-3,
\qquad
|V|\le n-3.
\]

Consequently, if
\[
F_n(z)=\sum_S z^{|S|}
\]
is the cardinality enumerator over all global stable locating-dominating sets of \(\operatorname{Cr}_n\), then
\[
\begin{aligned}
F_n(z)={}&z^{2n}
+2\sum_{r=1}^{n-2}\binom nr z^{2n-r}
+n z^{2n-2}\\
&+\sum_{x=1}^{n-3}\sum_{y=1}^{\min\{n-3,n-x\}}
\binom nx\binom{n-x}{y}z^{2n-x-y}.
\end{aligned}
\]

The global stable locating-domination number is
\[
\lambda^s_{gl}(\operatorname{Cr}_n)=
\begin{cases}
4,&n=3,\\
6,&n=4,5,\\
n,&n\ge6.
\end{cases}
\]
The exact numbers of minimum sets are
\[
3,\quad 28,\quad 30
\]
for \(n=3,4,5\), respectively, and
\[
2^n-2\left(1+n+\binom n2\right)
\]
for every \(n\ge6\).

For \(n\ge6\), the minimum sets have an especially simple form: they choose exactly one endpoint of every deleted matching pair and contain at least three vertices from each bipartition class.

## Assumptions and scope
A locating-dominating set \(S\) in a graph \(G\) dominates every vertex outside \(S\) and gives distinct traces
\[
N_G(x)\cap S
\]
to distinct vertices outside \(S\). It is stable locating-dominating when
\[
S\setminus\{s\}
\]
remains locating-dominating for every \(s\in S\). It is global stable locating-dominating when the same stability property holds in both \(G\) and its complement.

The theorem covers \(n\ge3\). The boundary \(\operatorname{Cr}_2=C_4\) is not part of the new claim: the introducing paper already proves that a connected graph of order four has global stable locating-domination number four exactly for \(C_4\) and \(P_4\).

## Proof
Write
\[
p=n-|U|,
\qquad
q=n-|V|,
\]
for the numbers of selected vertices in \(A\) and \(B\), respectively.

We first derive the omitted-index structure.

Suppose \(|U|\ge2\), and choose distinct \(i,j\in U\). If both \(i,j\in V\), then the two outside vertices \(a_i,a_j\) have the same neighborhood trace in \(S\), so \(S\) is not locating. If \(i\in V\) but \(j\notin V\), then \(b_j\in S\). After deleting \(b_j\), both \(a_i\) and \(a_j\) have the same trace into \(S\setminus\{b_j\}\). Thus stability fails. Hence
\[
|U|\ge2\Longrightarrow U\cap V=\varnothing.
\]
By symmetry,
\[
|V|\ge2\Longrightarrow U\cap V=\varnothing.
\]
Therefore, if \(U\cap V\ne\varnothing\), then necessarily
\[
U=V=\{i\}
\]
for one index \(i\).

Now assume \(U\cap V=\varnothing\). If \(U\ne\varnothing\), choose \(i\in U\). Its deleted partner \(b_i\) is selected, and
\[
|N(a_i)\cap S|=q-1.
\]
Because deletion of any one selected neighbor must still leave \(a_i\) dominated, this trace must contain at least two vertices. Hence
\[
q\ge3,
\]
which is equivalent to
\[
|V|\le n-3.
\]
Similarly,
\[
V\ne\varnothing\Longrightarrow |U|\le n-3.
\]

If \(U=\varnothing\), every vertex of \(A\) is selected. The set cannot have \(q=0\), because a deleted selected vertex of \(A\) would then be undominated. It also cannot have \(q=1\): if \(b_t\) is the unique selected vertex of \(B\), then after deleting \(a_t\), the removed vertex \(a_t\) has no selected neighbor. Thus
\[
q\ge2,
\]
or equivalently
\[
|V|\le n-2.
\]
The symmetric argument gives the condition when \(V=\varnothing\).

These conditions are also sufficient. First take \(U\cap V=\varnothing\) and assume the stated size bounds. Fix \(s\in S\) and put
\[
D=S\setminus\{s\}.
\]
In the crown graph, every outside vertex \(a_i\) has trace
\[
N(a_i)\cap D=D_B\setminus\{b_i\},
\]
and every outside vertex \(b_j\) has trace
\[
N(b_j)\cap D=D_A\setminus\{a_j\},
\]
where \(D_A=D\cap A\) and \(D_B=D\cap B\). Disjointness of \(U\) and \(V\), together with the deletion of only one sensor, implies that on either side at most one outside vertex can have its matched partner absent from \(D\). Hence same-side traces are pairwise distinct. The numerical bounds ensure all of these traces are nonempty. Opposite-side traces lie in different bipartition classes, so they cannot agree.

In the complement, each side of the crown becomes a clique and the deleted matching becomes a perfect matching. Thus an outside vertex \(a_i\) has trace
\[
D_A\cup\bigl(\{b_i\}\cap D\bigr),
\]
and an outside vertex \(b_j\) has trace
\[
D_B\cup\bigl(\{a_j\}\cap D\bigr).
\]
Again, disjointness gives a unique optional matched partner on each side, so same-side traces are distinct. If both omission sets are nonempty, the bounds give at least two surviving selected vertices in each relevant clique part after one deletion. If one omission set is empty, the full selected side supplies the same separation. Consequently opposite-side traces cannot coincide, and all traces are nonempty. Therefore \(D\) is locating-dominating in both the crown and its complement.

Finally, if \(U=V=\{i\}\), then
\[
S=V(\operatorname{Cr}_n)\setminus\{a_i,b_i\}.
\]
For \(n\ge3\), deleting one further selected vertex leaves the two originally omitted vertices and the removed sensor with nonempty, pairwise distinct traces in both the crown and its complement. Thus this exceptional family is global stable locating-dominating.

The classification is proved.

To count all sets, the exceptional common-singleton case contributes
\[
nz^{2n-2}.
\]
For disjoint omitted sets with one side empty, choosing \(r\) omitted indices contributes
\[
2\binom nr z^{2n-r},
\qquad 1\le r\le n-2.
\]
For nonempty disjoint omitted sets of sizes \(x,y\), one first chooses \(U\) and then \(V\) from its complement, giving
\[
\binom nx\binom{n-x}{y}
\]
sets of size \(2n-x-y\). This yields the displayed polynomial.

The minimum cardinality follows by maximizing \(|U|+|V|\) under the classification. For \(n=3\), only the common-singleton family attains size four. For \(n=4\), the maximum number of omissions is two, so the minimum size is six. For \(n=5\), the disjoint choice \(|U|=|V|=2\) gives size six. For \(n\ge6\), one can take disjoint sets with
\[
|U|+|V|=n,
\qquad
|U|,|V|\ge3,
\]
so the minimum size is \(n\). Equality then forces \(U,V\) to partition the matching indices, which is exactly the stated transversal description. The number of such minima is
\[
\sum_{r=3}^{n-3}\binom nr
=2^n-2\left(1+n+\binom n2\right).
\]
The small minimum counts follow from the same classification.

## Verification
The included checker constructs \(\operatorname{Cr}_n\) and its complement directly from adjacency sets. It tests the definition literally: a set must be locating-dominating before and after deletion of every selected vertex in both graphs.

For every \(3\le n\le8\), the checker examines every vertex subset and compares direct feasibility with the stated omitted-index classification. It also checks the \(C_4\) boundary and independently scans every subset through the claimed minimum size for \(n=9\). The run performs \(242{,}758\) direct subset checks, including \(87{,}360\) all-set equivalence checks, and matches every classification and minimum count.

## Relationship to prior work
The 2023 paper introducing global stable location-domination defines exactly the invariant used here, gives the general existence criterion and the universal order bound, and treats joins, edge coronas, coronas, and lexicographic products. Its inspected full text contains no crown-graph or complete-multipartite specialization, and its conclusion explicitly recommends studying graph families not treated there.

The 2021 predecessor introduces stable locating-domination without the global complement requirement. Its inspected full text contains no crown or bipartite specialization.

Earlier work on locating domination in bipartite graphs and their complements studies ordinary locating-domination and the relation between a graph and its complement. It includes standard families such as complete bipartite graphs but not crown graphs in the inspected text, and it does not impose one-sensor deletion stability.

Related results for solid, self, distance-based, total, and other locating variants on crown graphs do not imply the present theorem: their feasibility rules are different, and none requires every one-vertex deletion to remain locating-dominating simultaneously in the graph and its complement.

## Limitations
The theorem concerns only crown graphs and does not give a general classification for arbitrary matching-deleted bipartite graphs.

The finite checker is corroborative. The proof for arbitrary \(n\) comes from the exact omitted-index trace analysis.

A differently phrased or non-indexed treatment of global stable location-domination on crown graphs may exist; the literature comparison therefore supports, but cannot logically certify, bibliographic uniqueness.

## References
1. M. M. Ortega, G. A. Malacas, S. R. Canoy, Jr., “Global Stable Location-Domination in Graphs,” European Journal of Pure and Applied Mathematics 16(3) (2023), 1685–1694, DOI 10.29020/nybg.ejpam.v16i3.4748; published 30 July 2023.
2. E. C. Ahmad, G. A. Malacas, S. R. Canoy, Jr., “Stable Locating-Dominating Sets in Graphs,” European Journal of Pure and Applied Mathematics 14(3) (2021), 638–649, DOI 10.29020/nybg.ejpam.v14i3.3998.
3. C. Hernando, M. Mora, I. M. Pelayo, “Locating domination in bipartite graphs and their complements,” arXiv:1711.01951; later published in Discrete Applied Mathematics.
