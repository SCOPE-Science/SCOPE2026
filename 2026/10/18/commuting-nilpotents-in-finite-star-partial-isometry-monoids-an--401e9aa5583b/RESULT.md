# Commuting nilpotents in finite star partial-isometry monoids: an exact hub correction

## Finding

Let \(n\ge1\), put \(m=n-1\), and let \(D_n=\operatorname{DP}(S_n)\) be the monoid of partial isometries of the star \(S_n\) with hub \(0\) and leaves \(L=\{1,\ldots,m\}\). Let \(I_m\le D_n\) be the symmetric inverse monoid on \(L\), embedded by leaving \(0\) undefined. For a finite monoid of partial maps, a map is *nilpotent* if one of its positive powers is the empty map. Include the empty map among nilpotents.

Write \(C_n\) for the number of **ordered** pairs of commuting nilpotent maps in \(D_n\) and \(B_m\) for the corresponding count in \(I_m\). For each integer partition \(\lambda\vdash m\), let \(a_j(\lambda)\) be the number of parts equal to \(j\), and set \(\ell(\lambda)=\sum_j a_j(\lambda)\). Then

\[
\boxed{C_n-B_m=3m^2-m+2\sum_{\lambda\vdash m}\frac{m!}{\prod_{j\ge1}a_j(\lambda)!}\left(\ell(\lambda)^2+2\ell(\lambda)-a_1(\lambda)\right).}
\]

This difference counts precisely the ordered commuting nilpotent pairs with at least one component outside \(I_m\). The empty partition contributes zero when \(m=0\). An equivalent exponential-generating-function form, with \(s=z/(1-z)\), is

\[
C_n-B_m=3m^2-m+2m![z^m]\exp(s)(s^2+3s-z).
\]

## Assumptions and scope

All maps are partial **injective** self-maps; multiplication is partial-map composition. The star metric has distance \(1\) between the hub and a leaf, distance \(2\) between distinct leaves, and distance \(0\) on the diagonal. Each element of \(D_n\) preserves this metric on its domain. No field, parity, or asymptotic hypothesis is imposed. The assertion holds for every integer \(n\ge1\), including the one- and two-vertex cases.

For each leaf \(j\), let \(A_j\) denote the map \(0\mapsto j\) with singleton domain; for each leaf \(i\), let \(B_i\) denote \(i\mapsto0\). For distinct leaves \(i,j\), let \(H_{ij}\) denote the two-arrow map \(i\mapsto0\mapsto j\). Every nilpotent leaf-only map decomposes uniquely into vertex-disjoint directed paths, including isolated leaves. Its number of paths is \(c\), and the number of isolated paths is \(a_1\). Call a vertex a *source* if no arrow enters it and a *terminal* if no arrow leaves it. A one-vertex path is both.

## Proof

**Step 1: classify nilpotents involving the hub.** A partial isometry with domain of size at most one is any singleton arrow (or the empty map). For a partial isometry of domain size two, either both domain vertices and image vertices are leaves, or the hub occurs in both domain and image. When domain size is at least three, the hub occurs in the domain exactly when it occurs in the image, and then it must map to itself; otherwise the map is leaf-only. These observations follow directly from the three possible star distances, and agree with the element decomposition in Fernandes--Paulista, Proposition 2.1 and equation (1). Consequently the elements of \(D_n\) fall into leaf-only maps, maps fixing \(0\), and the singleton hub arrows and two-arrow hub maps just defined. Any map fixing \(0\) is not nilpotent. The two-arrow map with \(i=j\) is a two-cycle and is not nilpotent, whereas \(H_{ij}\), with \(i\ne j\), is nilpotent of index \(3\). Each \(A_j\) and \(B_i\) is square-zero. Thus the **entire** nilpotent set outside \(I_m\) is

\[
\{A_j:j\in L\}\ \sqcup\ \{B_i:i\in L\}\ \sqcup\ \{H_{ij}:i,j\in L,\ i\ne j\}.
\]

This also covers \(m=0\): the three displayed families are empty.

**Step 2: commuting with a fixed leaf-only nilpotent.** Fix a nilpotent \(\xi\in I_m\) with \(c\) directed-path components and \(a_1\) singleton components. Directly composing arrows gives

\[
A_j\xi=\xi A_j\iff j\notin\operatorname{dom}\xi,
\qquad
B_i\xi=\xi B_i\iff i\notin\operatorname{im}\xi.
\]

For distinct \(i,j\), it also gives

\[
H_{ij}\xi=\xi H_{ij}\iff i\notin\operatorname{im}\xi\ \text{and}\ j\notin\operatorname{dom}\xi.
\]

Each directed path has one source and one terminal; a singleton contributes an identical source-terminal pair. Hence exactly \(2c\) of the \(A_j,B_i\) and \(c^2-a_1\) of the \(H_{ij}\) commute with \(\xi\). Because either factor of an **ordered** pair may be the leaf-only map, this contributes \(4c+2(c^2-a_1)\) ordered commuting pairs with precisely one factor in \(I_m\).

**Step 3: pairs of hub-involving nilpotents.** Any two maps of type \(A\) commute, as do any two of type \(B\), giving \(m^2+m^2\) ordered pairs. A map \(H_{ij}\) commutes with another \(H_{kl}\) precisely when \((i,j)=(k,l)\): composing the two maps produces the arrow \(i\mapsto l\) in one order and \(k\mapsto j\) in the other. Every cross-type pair fails to commute: the compositions differ by at least one forced arrow. There are \(m(m-1)\) maps of type \(H\). Thus the number of ordered pairs with both factors outside \(I_m\) is exactly

\[
2m^2+m(m-1)=3m^2-m.
\]

**Step 4: sum over all leaf-only nilpotents.** A nilpotent partial bijection of \(m\) leaves is exactly a disjoint union of directed paths (cycles would prevent nilpotence). If the path-size multiset is a partition \(\lambda\vdash m\), the number of such labeled directed-path configurations is

\[
w(\lambda)=\frac{m!}{\prod_{j\ge1}a_j(\lambda)!},
\]

because arranging labels within each path fixes its arrows, and equal-sized path components may be permuted. For this configuration, \(c=\ell(\lambda)\) and \(a_1=a_1(\lambda)\). Summing Step 2 over the configurations and adding Step 3 proves the boxed formula.

For the generating function, the exponential formula for a set of directed paths gives the marking series \(\exp(tz/(1-z))\), where \(t\) marks components. At \(t=1\), first and second applications of \(t\partial_t\) yield \(s\exp(s)\) and \((s+s^2)\exp(s)\). Marking singleton components subtracts \(z\exp(s)\). Combining \(c^2+2c-a_1\) gives \(\exp(s)(s^2+3s-z)\). Multiplication by \(2m!\) and addition of \(3m^2-m\) gives the equivalent expression.

## Verification

The accompanying standalone file `checks/verify.py` constructs partial isometries by **checking pairwise star distances for each partial injection**, independently of the proof decomposition. It determines nilpotence by orbit traversal, tests commutation by explicit partial-map composition, and compares the resulting correction with the integer-partition formula. Exhaustive results for \(n=1,2,3,4,5,6\) give respectively the correction values \(0,6,34,168,1068,8530\). The corresponding ordered commuting-nilpotent counts \((B_m,C_n)\) are \((1,1),(1,7),(7,41),(61,229),(685,1753),(9361,17891)\). These finite tests are independent checks, not a substitute for the all-size proof above.

To reproduce: with Python 3, run `python checks/verify.py`; it requires only the standard library.

## Relationship to prior work

Fernandes and Paulista [1] classify the elements of the star partial-isometry monoid and determine its Green relations, order, rank, and presentation; its exact structural decomposition is used in Step 1. Their paper does not state the commuting-nilpotent-pair correction or the source/terminal criterion derived in Steps 2--4. Laradji and Umar [2] study the **number of individual** nilpotent partial bijections, a different statistic confined to the leaf-only baseline. The present result determines the additional ordered commuting-pair statistic contributed by the star hub, without assuming a closed form for the leaf-only commuting-pair count. Neither published source, by itself, supplies this cross-stratum compatibility enumeration.

## Limitations

The formula determines the exact difference \(C_n-B_m\), not a standalone closed form for \(B_m\). It does not classify all pairs of commuting leaf-only nilpotents, and it makes no claim about non-nilpotent elements, other graph families, or independent external certification. The characterization and formula are mathematically proved here; checks through \(n=6\) are corroborative only. Literature searches cannot exclude every unindexed or inaccessible earlier derivation.

## References

[1] V. H. Fernandes and T. Paulista, *On the monoid of partial isometries of a finite star graph*, arXiv:2203.05504v1 (first posted March 10, 2022), later *Communications in Algebra* 51 (2023), 1028--1048, doi:10.1080/00927872.2022.2121404. Open full text: https://run.unl.pt/bitstream/10362/148645/1/partialisometriesonstarsCA2.pdf .

[2] A. Laradji and A. Umar, *On the Number of Nilpotents in the Partial Symmetric Semigroup*, *Communications in Algebra* 32 (2004), 3017--3023, doi:10.1081/AGB-120038637.
