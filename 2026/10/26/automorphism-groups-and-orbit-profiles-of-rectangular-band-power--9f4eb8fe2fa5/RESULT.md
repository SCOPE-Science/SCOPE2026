# Automorphism groups and orbit profiles of rectangular-band power semigroups

## Finding

Let \(I,J\) be finite sets of cardinalities \(a,b\ge 2\), and equip \(B=I\times J\) with rectangular-band multiplication \((i,j)(k,\ell)=(i,\ell)\). Let \(\mathcal P_+(B)\) be the semigroup of all **nonempty** subsets of \(B\) under setwise multiplication. Put
\[
F_{u,v}=\sum_{i=0}^{u}\sum_{j=0}^{v}(-1)^{i+j}\binom ui\binom vj 2^{(u-i)(v-j)}\qquad(1\le u\le a,\;1\le v\le b).
\]
These numbers count bipartite graphs on two fixed vertex sets of sizes \(u,v\) without isolated vertices. There is a (noncanonically split) isomorphism
\[
\operatorname{Aut}(\mathcal P_+(B))\cong
\left(\prod_{\varnothing\ne U\subseteq I\atop\varnothing\ne V\subseteq J}
S_{F_{|U|,|V|}-1}\right)
\rtimes\left(
\prod_{u=1}^{a} S_{\binom au}
\times\prod_{v=1}^{b}S_{\binom bv}\right).
\]
Here \(S_0\) and \(S_1\) denote trivial groups. The right factor acts by relabeling the row-support and column-support sets separately within each fixed cardinality; the left factor freely permutes nonrectangular subsets having any fixed pair of supports. In particular,
\[
|\operatorname{Aut}(\mathcal P_+(B))|=
\left(\prod_{u=1}^{a}\binom au!\right)
\left(\prod_{v=1}^{b}\binom bv!\right)
\prod_{u=1}^{a}\prod_{v=1}^{b}
\left((F_{u,v}-1)!\right)^{\binom au\binom bv}.
\]
The action has exactly \(ab+(a-1)(b-1)=2ab-a-b+1\) orbits on \(\mathcal P_+(B)\): one orbit of rectangular subsets for each pair of support sizes, and one orbit of nonrectangular subsets for each pair of sizes at least two.

For \(a=b=2\), the automorphism group is \(S_6\rtimes(S_2\times S_2)\), of order \(2880\); the original rectangular band's automorphism group has order \(4\). The latter embeds through taking images of subsets but does not exhaust the power-semigroup automorphisms.

If \(a=1\) or \(b=1\), the proper-band hypothesis is essential: every nonempty subset is a rectangle and the full automorphism group becomes \(S_{2^a-1}\times S_{2^b-1}\), acting without a cardinality restriction.

## Assumptions and scope

All sets are finite and nonempty. The power semigroup excludes the empty set; adding it changes its structure. An automorphism means a bijection preserving setwise multiplication. A rectangular subset means a Cartesian product \(U\times V\) with nonempty \(U\subseteq I\) and \(V\subseteq J\). Let \(r(X)=\{i:\exists j\ (i,j)\in X\}\) and \(c(X)=\{j:\exists i\ (i,j)\in X\}\) denote its nonempty row and column supports. Define \(\mathcal F_{U,V}=\{X:r(X)=U,\ c(X)=V\}\).

## Proof

**1. Intrinsic square and support fibers.** Directly from the defining product, for arbitrary nonempty \(X,Y\subseteq B\),
\[
XY=r(X)\times c(Y),\qquad X^2=r(X)\times c(X).
\]
Consequently the set \(E=\mathcal P_+(B)^2\) of all products is exactly the set of nonempty rectangles, and it coincides with the set of idempotents. The operation on \(E\) is the rectangular band
\[
(U,V)(U',V')=(U,V'),
\]
where the coordinates range over \(\mathcal U=2^I\setminus\{\varnothing\}\) and \(\mathcal V=2^J\setminus\{\varnothing\}\). Thus every automorphism \(\phi\) of \(\mathcal P_+(B)\) induces two bijections \(\sigma:\mathcal U\to\mathcal U\) and \(\tau:\mathcal V\to\mathcal V\) such that
\[
\phi(U\times V)=\sigma(U)\times\tau(V).
\]
For a general \(X\in\mathcal F_{U,V}\), the square identity and preservation of squares imply \(\phi(X)\in\mathcal F_{\sigma(U),\tau(V)}\). Conversely, any pair \(\sigma,\tau\) and arbitrary bijections between the corresponding fibers preserving the distinguished rectangle yield a multiplication-preserving bijection, because every product is the rectangle built from the first factor's row support and second factor's column support. Hence there are no further compatibility conditions.

**2. Fiber sizes and their rigidity.** Each \(X\in\mathcal F_{U,V}\) is the edge set of a bipartite graph on the labeled vertex parts \(U,V\), in which every vertex has positive degree. Applying inclusion–exclusion over isolated vertices gives \(|\mathcal F_{U,V}|=F_{|U|,|V|}\). If either support has size one then this fiber is a singleton: its only element is the rectangle. For \(u,v\ge2\), the fiber has at least seven elements (extend any full-support graph on two-by-two parts by attaching additional vertices), so it is not a singleton.

Assume \(a,b\ge2\). The row-support sets of cardinality one are intrinsically characterized by the property that **every** fiber above them has cardinality one. Thus \(\sigma\) permutes exactly the row singletons. Analogously, \(\tau\) permutes exactly the column singletons. For \(u\ge2\), the smallest fiber size across column supports of size at least two is
\[
\min_{2\le v\le b}F_{u,v}=F_{u,2}=3^u-2.
\]
Indeed each of the \(u\) rows must choose a nonempty subset of the two columns (three choices), while the two constant choices failing to cover both columns must be omitted. To see that \(F_{u,v}\) strictly increases with \(v\) for \(u\ge2\), adjoin a new column to each no-isolated-vertex graph and connect it either only to a fixed first row or only to a distinct second row, producing two distinct admissible extensions. These values strictly increase with \(u\). Since \(\tau\) maps nonsingleton column supports bijectively to nonsingleton column supports, it preserves this minimum as a function of \(U\), forcing \(|\sigma(U)|=|U|\) for every nonempty \(U\). By the transpose argument, \(|\tau(V)|=|V|\) for every nonempty \(V\).

Conversely, arbitrary cardinality-preserving \(\sigma,\tau\) match equal-size fibers and can be lifted to automorphisms by choosing bijections of their \(F_{u,v}-1\) nonrectangular members. This proves that the full induced group on \(E\) is
\[
H=\left(\prod_{u=1}^{a}S_{\binom au}\right)\times
\left(\prod_{v=1}^{b}S_{\binom bv}\right),
\]
and the kernel is \(K=\prod_{U,V}S_{F_{|U|,|V|}-1}\).

**3. Splitting and orbits.** For each ordered pair of sizes \((u,v)\), choose a standard labeling of the nonrectangle members of every fiber with those support sizes. Transporting these labels along \(H\) defines a group section \(H\to\operatorname{Aut}(\mathcal P_+(B))\), and conjugation simply permutes the \(K\)-factors for matched supports. This yields the claimed semidirect product and order formula. On rectangles, \(H\) acts transitively for each \((u,v)\). On nonrectangles, the kernel \(K\) is transitive within each fiber, and \(H\) connects all fibers with the same support sizes. These are exactly the claimed \(ab+(a-1)(b-1)\) orbits.

**4. Boundary when one side has size one.** If \(a=1\), every nonempty subset is of the form \(I\times V\), and product is right-zero multiplication. Its automorphism group is the full symmetric group on its \(2^b-1\) elements. The case \(b=1\) is dual. The unified expression \(S_{2^a-1}\times S_{2^b-1}\) follows, since one factor is trivial. This completes the proof.

## Verification

Run `python verify.py` using Python 3 and the standard library. The verifier computes all nonempty subsets, support fibers, and the setwise multiplication table independently for bands of shapes \((1,3),(2,2),(2,3),(3,3)\), checks the inclusion–exclusion fiber formula, and enumerates **all \(2880\) automorphisms in the proposed \((2,2)\)-family**, verifying bijectivity and every multiplication equation in each case. The resulting terminal message is `VERIFY_OK`. The finite tests do not establish universal validity; the preceding proof covers arbitrary finite \(a,b\) in scope.

## Relationship to prior work

Tringali's 2026 survey explicitly formulates the power-semigroup automorphism question in terms of the canonical inclusion \(\operatorname{Aut}(S)\hookrightarrow\operatorname{Aut}(\mathcal P_{\mathrm{fin}}(S))\), and discusses rigidity/nonrigidity across groups and numerical semigroups. The present result gives a complete, substantially nonrigid family of finite semigroups; finite sets make the finitary and full nonempty power constructions coincide.

Tamura and Shafer's 1967/1968 results (the published meeting abstract *Power semigroups. II*, Theorem 2) already establish the structural observation that the power semigroup of a rectangular band is a rectangular band of null semigroups. This **is prior knowledge**; the observation \(\mathcal P_+(B)^2=E\) is not asserted as a new discovery. The result here identifies the exact cardinality profile of its null fibers, proves that the cardinalities of both supports are intrinsic under automorphisms when both base dimensions exceed one, and derives the complete group and orbit census.

Yu and Zhao's 2019 theorem on the strong isomorphism property of bands implies that automorphisms of the power semigroup of a proper rectangular band preserve the original singleton copies. That conclusion is respected here but is strictly weaker than the complete determination of automorphisms; notably, nonrectangle fiber permutations fix **all** singleton copies while remaining nontrivial.

The exact group/order and orbit formulas have not been identified in the reviewed sources or the indexed mathematical-record search; no assertion of absolute priority is possible.

## Limitations

The semidirect-product splitting depends on arbitrary label choices for nonrectangles, so it is not canonical. The result concerns the multiplicative semigroup of **nonempty** subsets only, not the power-set semiring that also remembers union. In particular, permutations of nonrectangles need not preserve union and do not define semiring automorphisms. The classical 1967/1968 source was accessible in meeting-abstract form, not as a fully inspected original paper; an unindexed exact automorphism classification remains an originality risk. The statement does not cover more general bands, other Rees matrix semigroups, or infinite rectangular bands.

## References

1. Salvatore Tringali, *Power monoids and their arithmetic: a survey*, arXiv:2602.15754, first public 2026-02-17, https://arxiv.org/abs/2602.15754 . The relevant complete introduction and automorphism discussion are in the arXiv manuscript, pp. 1–5.
2. T. Tamura and J. Shafer, *Power semigroups*, Math. Japon. 12 (1967), 25–32, with erratum 1984; also *Power semigroups. II*, Notices Amer. Math. Soc., meeting abstract 68T-321 (1968), Theorem 2. Abstract indexed at https://www.ams.org/journals/notices/196802/196802FullIssue.pdf .
3. Baomin Yu and Xianzhong Zhao, *The bands satisfying the strong isomorphism property*, Semigroup Forum 98 (2019), 327–337, DOI:10.1007/s00233-019-09998-9, https://www.researchgate.net/publication/330610725_The_bands_satisfying_the_strong_isomorphism_property . See Lemma 2.4 and Theorem 3.5.
4. Salvatore Tringali and Kerou Wen, *On the automorphisms of the power semigroups of a numerical semigroup*, Transactions of the London Mathematical Society (2026), DOI:10.1112/tlm3.70030, https://arxiv.org/abs/2604.26901 .
