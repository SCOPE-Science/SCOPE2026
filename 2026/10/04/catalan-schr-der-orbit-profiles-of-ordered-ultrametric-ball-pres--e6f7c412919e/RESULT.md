# Catalan–Schröder orbit profiles of ordered ultrametric ball-preserving groups

## Finding

For each \(N\in\{2,3,\ldots\}\cup\{\infty\}\), let \(\mathbb U_N^\prec\) be Malicki's ordered rational \(N\)-ultrametric Urysohn space, and let
\[
G_N=\operatorname{BP}_\prec(\mathbb U_N^\prec)
\]
be its group of order-preserving ball-preserving automorphisms. Let \(t_{N,n}\) denote the number of plane rooted trees with \(n\) leaves in which every internal vertex has at least two children and at most \(N\) children; for \(N=\infty\), there is no upper bound.

Then the number \(a_{N,n}\) of \(G_N\)-orbits on injective ordered \(n\)-tuples is exactly
\[
\boxed{a_{N,n}=n!\,t_{N,n}}.
\]
The tree numbers are determined by \(t_{N,1}=1\) and the root decomposition
\[
t_{N,n}
=
\sum_{j=2}^{\min(N,n)}
\sum_{n_1+\cdots+n_j=n\atop n_i\ge1}
\prod_{i=1}^j t_{N,n_i},
\]
with the obvious unbounded interpretation for \(N=\infty\). Equivalently, if
\[
T_N(z)=\sum_{n\ge1}t_{N,n}z^n,
\]
then
\[
T_N(z)=z+\sum_{j=2}^N T_N(z)^j
\]
for finite \(N\), while
\[
T_\infty(z)=z+\frac{T_\infty(z)^2}{1-T_\infty(z)}.
\]

Two classical endpoints follow immediately:
\[
a_{2,n}=n!C_{n-1},
\]
where \(C_m\) is the Catalan number, and
\[
a_{\infty,n}=n!s_{n-1},
\]
where \(s_m\) is the little Schröder number. Thus the injective profiles begin
\[
1,2,12,120,1680,30240,\ldots \qquad(N=2)
\]
and
\[
1,2,18,264,5400,141840,\ldots \qquad(N=\infty).
\]

If repetitions are allowed and \(b_{N,n}\) is the number of orbits on all ordered \(n\)-tuples, then
\[
\boxed{b_{N,n}=\sum_{k=1}^n {n\brace k}a_{N,k}},
\]
so the exponential generating function is
\[
\boxed{\sum_{n\ge1}b_{N,n}\frac{z^n}{n!}=T_N(e^z-1)}.
\]
For example, the full profiles begin \(1,3,19,207,3211,64383,\ldots\) for \(N=2\), and \(1,3,25,387,8521,241683,\ldots\) for \(N=\infty\).

## Assumptions and scope

Malicki defines \(\mathcal K_N^\prec\) as the finite rational ultrametric spaces with a convex linear order and with every equilateral \(r\)-polygon of size at most \(N\). He notes that the same classes, with order-preserving ball-preserving injections as morphisms, are Fraïssé classes. Proposition 5.1 characterizes ball-preserving bijections by preservation of strict comparisons of pair distances, and Proposition 5.13 identifies the \(N=2\) case with ordered boron tree structures.

The statement concerns the ball-preserving group in this ordered sense: every group element preserves both the convex point order and the ball structure, but it need not preserve numerical distance values. The result is an orbit-profile theorem for these groups; it does not claim a new enumeration of Catalan or Schröder trees themselves.

## Proof

Fix a finite subset \(A\subseteq\mathbb U_N^\prec\). Form its reduced cluster tree as follows. The leaves are the points of \(A\). For every distance value occurring on \(A\), the corresponding equivalence classes under “distance strictly below this value” give the nontrivial clusters; order clusters by inclusion and suppress unary vertices. Ultrametricity makes this a rooted tree. Convexity of \(\prec\) orders the children of every internal vertex from left to right, so the result is a plane rooted tree.

Every internal vertex has at least two children by reduction. It has at most \(N\) children: choosing one leaf from each child produces an equilateral set at the radius of that cluster, hence an \(r\)-polygon, whose size is bounded by \(N\). Conversely, every finite plane rooted tree with these degree constraints can be realized by assigning strictly increasing rational radii along each root path and using the left-to-right leaf order. Thus precisely the stated plane trees occur as finite cluster shapes.

Now let \(f:A\to B\) be a bijection between finite subsets. By Malicki's Proposition 5.1, \(f\) is ball-preserving exactly when it preserves the strict distance comparisons
\[
d(x,y)<d(y,z).
\]
In a finite ultrametric, these comparisons are exactly the ancestor relations among the corresponding least common ancestors in the cluster tree. Hence \(f\) is ball-preserving if and only if it induces an isomorphism of the reduced cluster trees. Adding preservation of \(\prec\) says exactly that this is an isomorphism of plane trees.

Such finite order-preserving bp-isomorphisms extend to global elements of \(G_N\). This is the homogeneity supplied by the Fraïssé category with order-preserving bp-injections noted by Malicki; equivalently, one can run the usual back-and-forth directly in \(\mathbb U_N^\prec\). At a one-point extension, only a finite chain of strict distance inequalities and a finite left-right position must be realized. Rational distance levels can be inserted between the finitely many existing levels, and the matching cluster tree guarantees that a new branch is requested only where the bound \(N\) still permits one. The ordinary one-point extension property of the ordered rational \(N\)-ultrametric Urysohn space then supplies the new point. Repeating this in both directions yields the required global bp-automorphism.

Therefore injective ordered tuple orbits are exactly coordinate-labeled plane cluster trees. A plane tree with \(n\) leaves has a fixed left-to-right order on its leaf positions, and an ordered finite structure of this kind is rigid. The tuple coordinates \(1,\ldots,n\) may be assigned to those leaf positions in exactly \(n!\) ways. This proves
\[
a_{N,n}=n!t_{N,n}.
\]

Decomposing a plane tree at its root gives the recurrence and generating-function equations. For \(N=2\), these are full plane binary trees with \(n\) leaves, counted by \(C_{n-1}\). With no degree bound, these are plane rooted trees with no unary vertices and \(n\) leaves, counted by the little Schröder number \(s_{n-1}\).

Finally, an arbitrary ordered \(n\)-tuple determines a partition of its coordinate set into \(k\) equality classes and then an injective ordered \(k\)-tuple of distinct values. There are \({n\brace k}\) such set partitions, so
\[
b_{N,n}=\sum_{k=1}^n{n\brace k}a_{N,k}.
\]
Using
\[
\sum_{n\ge k}{n\brace k}\frac{z^n}{n!}=\frac{(e^z-1)^k}{k!},
\]
and \(a_{N,k}/k!=t_{N,k}\), gives the displayed composition \(T_N(e^z-1)\).

## Verification

A separate checker implements two independent descriptions of \(t_{N,n}\): direct recursive generation of canonical plane trees and the composition recurrence. They agree for \(N=2,3,4,\infty\) through \(n=8\). The checker also verifies the Catalan values for \(N=2\), the OEIS A001003 little Schröder values for \(N=\infty\), multiplies by \(n!\) to obtain the injective orbit sequences, and applies the Stirling transform to obtain the displayed full profiles. It ends with `VERIFY_OK`.

The finite computation verifies the enumerative layer, not the model-theoretic extension argument. That argument depends on Malicki's finite bp-morphism framework and the Fraïssé/back-and-forth extension property.

## Relationship to prior work

Malicki's 2019 preprint, later published in *Archive for Mathematical Logic*, introduces the groups \(\operatorname{BP}(\mathbb U_N^\prec)\), proves structural facts about partial bp-automorphisms, and establishes a comeager conjugacy class but no comeager 2-diagonal conjugacy class. It also identifies the \(N=2\) category with ordered boron trees. The paper does not state the finite tuple-orbit profile above.

Petrov proved earlier that two finite ultrametric spaces are related by a ball-preserving bijection exactly when their representing rooted trees are isomorphic. That result explains the unordered finite tree invariant, but it neither treats Malicki's ordered generic groups nor derives the Catalan-to-Schröder orbital profile or the Stirling-transform law.

The pure combinatorial fact that plane rooted trees with no outdegree-one vertex and \(n\) leaves are counted by \(s_{n-1}\) is classical and recorded as OEIS A001003. The claimed contribution is the object-specific orbit classification and its exact profile, not the Schröder sequence itself.

Targeted exact-phrase searches, broader web searches, the published-finding corpus semantic index, and the existing local ledger were checked. The closest indexed published-finding corpus records compute orbit profiles for random-poset, Rado-graph, and distributive-lattice groups, not for ordered ultrametric bp-groups. A prior local finding concerns a two-sorted distance-comparison automorphism group of an ultrametric Fraïssé limit and yields partition-lattice-chain counts; it is a different group, language, and profile.

## Limitations

The proof uses the ordered, order-preserving bp-group; dropping the convex order changes the finite automorphism quotient and therefore the count. The finite-degree interpolation \(t_{N,n}\) is standard plane-tree enumeration once the orbit classification is known, so no new combinatorics is claimed there. The literature search cannot exclude an unindexed or unpublished observation of the same orbit profile. No independent audit has been performed.

## References

1. Maciej Malicki, “Remarks on weak amalgamation and large conjugacy classes in non-archimedean groups,” arXiv:1908.09494 (2019); *Archive for Mathematical Logic* 61 (2022), 685–704, DOI 10.1007/s00153-021-00807-1.
2. E. Petrov, “Ball-preserving mappings of finite ultrametric spaces,” arXiv:1302.5896 (2013).
3. Aleksandra Kwiatkowska and Maciej Malicki, “Ordered structures and large conjugacy classes,” arXiv:1903.00936 (2019); *Journal of Algebra* 557 (2020), 67–96.
4. OEIS A001003, little Schröder numbers; in particular, the interpretation as ordered trees with no vertex of outdegree one and \(n+1\) leaves.
