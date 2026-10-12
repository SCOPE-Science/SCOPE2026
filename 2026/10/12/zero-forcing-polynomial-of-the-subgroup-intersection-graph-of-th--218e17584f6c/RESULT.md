# Zero forcing polynomial of the subgroup-intersection graph of the exponent-\(p\) extraspecial group of order \(p^3\)

## Finding

Let \(p\) be an odd prime and let \(G\) be the extraspecial group of order \(p^3\) and exponent \(p\). For the intersection graph \(\Gamma(G)\) on the proper nontrivial subgroups of \(G\), \[\mathcal Z(\Gamma(G);u)=u^{p^2-1}(1+u)^{p+1}\big((1+u)(u+p)^{p+1}-p^{p+1}\big).\] Consequently \(Z(\Gamma(G))=p^2\), and the number of minimum zero forcing sets is \((2p+1)p^p\). Every minimum set is of exactly one of two types: either it contains the center, contains no maximal subgroup, and contains all but one of the \(p\) noncentral order-\(p\) subgroups inside each maximal subgroup; or it contains no center or maximal subgroup, contains all \(p\) such subgroups inside one maximal subgroup, and all but one inside every other maximal subgroup.

The graph has
\[
p^2+2p+2
\]
vertices, so every minimum zero forcing set leaves exactly \(2p+2\) vertices white.

## Assumptions and scope

Let \(p\) be an odd prime and let \(G\) be the extraspecial group of order \(p^3\) and exponent \(p\). Write
\[
Z=Z(G)=G'=\Phi(G),\qquad |Z|=p.
\]
Then \(G/Z\cong C_p^2\). Let \(M_1,\ldots,M_{p+1}\) be the maximal subgroups, the inverse images of the one-dimensional subspaces of \(G/Z\). Each has order \(p^2\), contains \(Z\), and is elementary abelian.

For each \(i\), let \(L_i\) be the set of noncentral subgroups of order \(p\) contained in \(M_i\). Since \(M_i\cong C_p^2\),
\[
|L_i|=p.
\]

## Proof

Because \(G\) has exponent \(p\), its nonidentity elements partition into order-\(p\) subgroups, giving
\[
\frac{p^3-1}{p-1}=p^2+p+1
\]
such subgroups. The \(p+1\) maximal subgroups pairwise intersect exactly in \(Z\).

Every noncentral order-\(p\) subgroup \(H\) lies in a unique maximal subgroup: \(HZ/Z\) is a one-dimensional subspace of \(G/Z\), whose inverse image is that maximal subgroup. Hence \(\Gamma(G)\) consists of a clique \(K_{p+2}\) on \(Z,M_1,\ldots,M_{p+1}\), together with \(p\) private leaves at each \(M_i\). Thus
\[
|V(\Gamma(G))|=(p+2)+p(p+1)=p^2+2p+2.
\tag{1}
\]

Let \(S\) be an initial blue set. In each \(L_i\), at most one vertex may be white. If two were white, their sole possible forcing source \(M_i\) would always see both.

Assume this necessary condition. If \(Z\) is blue, then any white \(M_i\) is forced by a blue leaf in \(L_i\); such a leaf exists because \(p\ge3\). Once all \(M_i\) are blue, each remaining white leaf is the unique white neighbor of its \(M_i\).

If \(Z\) is white, the same first stage colors all \(M_i\). Then \(M_i\) sees \(Z\) and its possible one white leaf. Thus forcing continues exactly when some \(L_i\) is entirely blue: its \(M_i\) forces \(Z\), after which all remaining white leaves are forced. Therefore \(S\) is zero forcing exactly when
\[
|L_i\setminus S|\le1
\quad\text{for every }i,
\tag{2}
\]
and, if \(Z\notin S\), at least one \(L_i\subseteq S\).

The colors of the \(p+1\) maximal subgroups are unrestricted, contributing \((1+u)^{p+1}\). A leaf block contributes
\[
u^p+pu^{p-1}=u^{p-1}(u+p).
\]
If \(Z\) is blue, the contribution is
\[
u(1+u)^{p+1}(u^p+pu^{p-1})^{p+1}.
\]
If \(Z\) is white, all allowed leaf profiles contribute except the profile with exactly one white leaf in every block:
\[
(1+u)^{p+1}
\left((u^p+pu^{p-1})^{p+1}-p^{p+1}u^{(p-1)(p+1)}\right).
\]
Adding gives
\[
\mathcal Z(\Gamma(G);u)
=
u^{p^2-1}(1+u)^{p+1}
\left((1+u)(u+p)^{p+1}-p^{p+1}\right).
\tag{3}
\]

The bracket in (3) has zero constant term and coefficient of \(u\)
\[
p^{p+1}+(p+1)p^p=(2p+1)p^p.
\]
Therefore
\[
Z(\Gamma(G))=p^2
\]
and the number of minimum zero forcing sets is
\[
(2p+1)p^p.
\tag{4}
\]

At minimum size all \(M_i\) are initially white. If \(Z\) is blue, each \(L_i\) has exactly one white leaf, giving \(p^{p+1}\) sets. If \(Z\) is white, exactly one \(L_i\) is entirely blue and each other block has one white leaf, giving \((p+1)p^p\) sets. These are exactly the two claimed types.

## Verification

The accompanying `verify.py` was read from its packaged path before replay.

For \(p=3\), it tests all \(2^{17}=131072\) initial blue sets and verifies the criterion (2) subset-by-subset, then reproduces the complete polynomial coefficient-by-coefficient. It obtains \(Z=9\) and \(189\) minimum sets.

It independently constructs the finite Heisenberg group
\[
\left\{
\begin{pmatrix}
1&a&c\\
0&1&b\\
0&0&1
\end{pmatrix}:a,b,c\in\mathbb F_p
\right\}
\]
for \(p=3,5\), enumerates every order-\(p\) subgroup and every projective-line maximal subgroup, and checks every pairwise subgroup intersection against the claimed clique-with-private-leaves graph.

It also expands (3) for \(p=3,5,7,11\) and checks the minimum exponent and coefficient.

Exact replay output:

```text
p=3 full polynomial: {9: 189, 10: 918, 11: 1848, 12: 2005, 13: 1286, 14: 508, 15: 124, 16: 17, 17: 1}
p=3 characterization checked on all 2^17 subsets
Heisenberg p=3: 17 proper nontrivial subgroups, graph pattern OK
Heisenberg p=5: 37 proper nontrivial subgroups, graph pattern OK
p=3: Z=9, min_count=189, polynomial_at_1=6896
p=5: Z=25, min_count=34375, polynomial_at_1=4971968
p=7: Z=49, min_count=12353145, polynomial_at_1=7114145536
p=11: Z=121, min_count=6562168424053, polynomial_at_1=60185692241063936
VERIFY_OK
```

The finite checks corroborate the arbitrary-prime proof; the theorem itself follows from the subgroup classification and the exact forcing criterion.

## Relationship to prior work

Classical work on finite \(p\)-groups treats extraspecial groups as a central nilpotent family. A 2010 classification article explicitly includes extraspecial \(p\)-groups and is classified under \(20D15\).

The subgroup-intersection literature defines the graph used here and studies structural properties such as planarity, connectivity, domination, and diameter. Those parameters do not determine the standard zero forcing sets.

The zero forcing polynomial literature supplies the counting invariant and closed forms for several graph families. Its full text was checked through the family-characterization section; no corona formula or subgroup-intersection specialization covering the graph in (1) was found.

## Limitations

The theorem is restricted to odd-prime extraspecial groups of order \(p^3\) and exponent \(p\).

Larger extraspecial groups and the exponent-\(p^2\) nonabelian group of order \(p^3\) are not covered.

No minimum-rank or maximum-nullity equality is asserted.

## References

1. Q. Zhang, L. Li, and M. Xu, “Finite \(p\)-Groups All of Whose Proper Quotient Groups are Abelian or Inner-Abelian,” *Communications in Algebra* 38 (2010), 2797–2807. DOI: 10.1080/00927870903074066. Published online 18 August 2010. Mathematics Subject Classification: \(20D15\).
2. S. Kayacan and E. Yaraneri, “Finite groups whose intersection graphs are planar,” *Journal of the Korean Mathematical Society* 52 (2015), 81–96. DOI: 10.4134/JKMS.2015.52.1.081. Public bibliographic date: 6 February 2015.
3. K. Boyer, B. Brimkov, S. English, D. Ferrero, A. Keller, R. Kirsch, M. Phillips, and C. Reinhart, “The zero forcing polynomial of a graph,” *Discrete Applied Mathematics* 258 (2019), 35–48. arXiv:1801.08910, first submitted 26 January 2018.
