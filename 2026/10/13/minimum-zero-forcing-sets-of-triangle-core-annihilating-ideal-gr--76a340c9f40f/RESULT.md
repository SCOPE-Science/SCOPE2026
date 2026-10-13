# Minimum zero forcing sets of triangle-core annihilating-ideal graphs

## Finding

Let \(F_n(m)\) be the graph consisting of \(n\ge1\) triangles sharing exactly one center together with \(m\ge1\) pendant leaves attached to that center. If \(m\ge2\), then \[Z(F_n(m))=n+m-1\] and the minimum zero forcing sets are exactly the sets containing one vertex from each noncentral triangle pair and all but one pendant leaf; hence there are \(m2^n\) minimum sets. If \(m=1\), then \(Z(F_n(1))=n+1\), and the minimum sets are exactly: the center plus one vertex from every triangle pair; or the leaf plus one vertex from every pair; or both vertices of exactly one triangle pair plus one vertex from every other pair. Thus there are \(2^{n-1}(n+4)\) minimum sets. The remaining finite Yu–Wu triangle-core annihilating-ideal graph \(K_3(1,1,1)\) has zero forcing number \(2\) and exactly \(9\) minimum sets. Consequently every finite commutative ring whose annihilating-ideal graph has core consisting only of triangles has its zero forcing number and all minimum zero forcing sets determined explicitly by the Yu–Wu graph classification.

For the finite ring-realizable families classified by Yu and Wu, this gives the following closed forms. Here \(p\ge3\) is prime, \(k\ge1\), and \(r\ge1\):
\[
\begin{array}{c|c|c}
G&Z(G)&\#\{\text{minimum zero forcing sets}\}\\ \hline
K_3(1)&2&5\\
K_3(2)&2&4\\
K_3(3)&3&6\\
K_3(1,1,1)&2&9\\
F_{2r}(2)&2r+1&2^{2r+1}\\
F_{(p^k+1)/2}(1)&(p^k+3)/2&2^{(p^k-1)/2}(p^k+9)/2\\
F_{(p^k-1)/2}(3)&(p^k+3)/2&3\cdot2^{(p^k-1)/2}.
\end{array}
\]

In particular, the last two Yu–Wu families have the same zero forcing number for the same \(p^k\), but their numbers of minimum zero forcing sets are different.

## Assumptions and scope

All graphs are finite and simple. A zero forcing set is an initially blue vertex set from which the standard color-change rule colors every vertex: a blue vertex with exactly one white neighbor forces that neighbor blue.

Following Yu and Wu, \(F_n(m)\) consists of \(n\) triangles
\[
c a_i b_i c,
\qquad
1\le i\le n,
\]
sharing only the center \(c\), together with pendant leaves
\[
x_1,\ldots,x_m
\]
adjacent only to \(c\). Their notation extends to \(F_1(m)=K_3(m)\).

The graph \(K_3(1,1,1)\) is a triangle with one pendant leaf at each of its three core vertices.

Yu and Wu classify the annihilating-ideal graphs whose cores consist only of triangles. For finite rings, their list consists precisely of
\[
K_3(1),\ K_3(2),\ K_3(3),\ K_3(1,1,1),
\]
\[
F_{2r}(2),
\qquad
F_{(p^k+1)/2}(1),
\qquad
F_{(p^k-1)/2}(3),
\]
with the parameter ranges stated above.

## Proof

Fix \(F_n(m)\). For every \(i\), the two noncentral vertices \(a_i,b_i\) have the same closed neighborhood:
\[
N[a_i]=N[b_i]=\{a_i,b_i,c\}.
\]
If both were white at some stage, no force could be the first force that colors one of them: any possible forcing vertex adjacent to one is also adjacent to the other. Hence every zero forcing set contains at least one vertex from each pair
\[
\{a_i,b_i\}.
\tag{1}
\]

Similarly, all pendant leaves have the same open neighborhood \(\{c\}\). If two leaves are white at the same time, no force can ever color either one first. Therefore, when \(m\ge2\), every zero forcing set contains at least \(m-1\) leaves. Combining this with (1),
\[
Z(F_n(m))\ge n+m-1.
\tag{2}
\]

Choose one vertex from each triangle pair and all but one pendant leaf. Because \(m\ge2\), some chosen leaf is blue and forces the center \(c\). Each chosen triangle vertex then has its mate as its unique white neighbor and forces it. Finally \(c\) forces the last white leaf. Thus equality holds in (2).

If a set has the minimum size \(n+m-1\), the two lower bounds used in (2) must both be tight. It therefore contains exactly one vertex from each triangle pair, exactly \(m-1\) leaves, and not the center. Conversely every such set forces by the sequence just described. Hence the number of minimum sets is
\[
2^n\binom{m}{m-1}=m2^n.
\]

Now let \(m=1\), and write \(x\) for the sole leaf. Equation (1) still gives the lower bound \(n\). A set of size \(n\) satisfying (1) contains exactly one vertex from each triangle pair and neither \(c\) nor \(x\). Every chosen triangle vertex then has two white neighbors, its mate and \(c\), so no force is possible. Therefore
\[
Z(F_n(1))\ge n+1.
\]

At size \(n+1\), after selecting at least one vertex from each of the \(n\) triangle pairs, there is exactly one extra blue vertex. There are three exhaustive possibilities.

First, the extra vertex is \(c\). Each selected triangle vertex forces its mate, after which \(c\) forces \(x\).

Second, the extra vertex is \(x\). The leaf forces \(c\), and the selected triangle vertices then force their mates.

Third, the extra vertex is the unselected mate in exactly one triangle pair. One vertex of that fully blue pair forces \(c\); the other selected triangle vertices then force their mates, and finally \(c\) forces \(x\).

Thus all three types are zero forcing and every minimum set has one of these forms. The first two types each contribute \(2^n\) sets. In the third type, choose the doubled pair in \(n\) ways and one vertex from each remaining pair in \(2^{n-1}\) ways. Hence
\[
2^n+2^n+n2^{n-1}
=
2^{n-1}(n+4)
\]
minimum sets.

It remains to treat \(K_3(1,1,1)\). One blue vertex never forces the graph, so \(Z\ge2\). A pair of blue leaves forces: the leaves first force their incident core vertices, then the third core and its leaf are forced. A blue core vertex together with a leaf attached to a different core vertex also forces. There are
\[
\binom32=3
\]
pairs of the first type and
\[
3\cdot2=6
\]
of the second type. The other two pair types—two core vertices, or a core vertex with its own leaf—stall. Therefore
\[
Z(K_3(1,1,1))=2
\]
with exactly \(9\) minimum sets.

Substituting the finite Yu–Wu parameter families into these formulas yields the table in the finding.

## Verification

The accompanying `verify.py` constructs \(F_n(m)\) directly and exhaustively enumerates all vertex subsets for
\[
1\le n\le6,
\qquad
1\le m\le4.
\]
For every case it verifies the zero forcing number, the exact minimum-set count, and the structural classification of every minimum set.

It separately constructs \(K_3(1,1,1)\), checks that the minimum size is \(2\), and verifies that the \(9\) minimum pairs are exactly the two types in the proof.

Finally, it substitutes representative parameters into each infinite Yu–Wu family and checks the displayed closed forms.

Exact replay output:

```text
F_1(1): Z=2, minimum_sets=5
F_1(2): Z=2, minimum_sets=4
F_1(3): Z=3, minimum_sets=6
F_1(4): Z=4, minimum_sets=8
F_2(1): Z=3, minimum_sets=12
F_2(2): Z=3, minimum_sets=8
F_2(3): Z=4, minimum_sets=12
F_2(4): Z=5, minimum_sets=16
F_3(1): Z=4, minimum_sets=28
F_3(2): Z=4, minimum_sets=16
F_3(3): Z=5, minimum_sets=24
F_3(4): Z=6, minimum_sets=32
F_4(1): Z=5, minimum_sets=64
F_4(2): Z=5, minimum_sets=32
F_4(3): Z=6, minimum_sets=48
F_4(4): Z=7, minimum_sets=64
F_5(1): Z=6, minimum_sets=144
F_5(2): Z=6, minimum_sets=64
F_5(3): Z=7, minimum_sets=96
F_5(4): Z=8, minimum_sets=128
F_6(1): Z=7, minimum_sets=320
F_6(2): Z=7, minimum_sets=128
F_6(3): Z=8, minimum_sets=192
F_6(4): Z=9, minimum_sets=256
K3(1,1,1): Z=2, minimum_sets=9
YU_WU_SPECIALIZATIONS_OK
VERIFY_OK
```

The finite checks corroborate the proof but do not replace its arbitrary-\(n,m\) twin-class argument.

## Relationship to prior work

Yu and Wu determine exactly which triangle-core graphs occur as annihilating-ideal graphs. Their paper defines \(F_n(m)\), proves the ring-realizable classification, and gives a complete finite-ring realization theorem. Its title page lists 2010 Mathematics Subject Classification \(13A15\) first, followed by \(05C75\). Their work does not study zero forcing.

General zero forcing literature includes formulas for ordinary windmill and generalized windmill graphs and the general zero forcing polynomial framework. In particular, later generalized-windmill work gives the ordinary zero forcing number when all peripheral clique blocks have a common size. The graph \(F_n(m)\) used here has mixed peripheral blocks—\(n\) copies of \(K_2\) and \(m\) pendant \(K_1\) blocks—and the inspected generalized-windmill result does not give the minimum-set classification or count proved here.

Targeted searches under “annihilating-ideal graph,” “triangle with horns,” “friendship graph,” “windmill,” “fan with pendant vertices,” “zero forcing,” and “minimum zero forcing sets” did not locate the stated classification or the Yu–Wu specialization.

## Limitations

The ring application is restricted to finite commutative rings whose annihilating-ideal graph has core consisting only of triangles.

The theorem determines the zero forcing number and all minimum zero forcing sets, but not the complete zero forcing polynomial.

The graph result for \(F_n(m)\) is purely combinatorial once Yu and Wu's ring classification is invoked; it does not distinguish rings that realize the same graph.

Later generalized-windmill work covers some related ordinary zero forcing numbers, so originality is claimed for the mixed horn family classification, the exact minimum-set enumeration, and the complete finite Yu–Wu ring specialization rather than for zero forcing on windmills in general.

## References

1. H. Yu and T. Wu, “Commutative Rings \(R\) Whose \(C(AG(R))\) Consist of Only Triangles,” *Communications in Algebra* 43 (2015), 1076–1097. DOI: 10.1080/00927872.2013.847950. Published online 7 January 2015.
2. K. Boyer, B. Brimkov, S. English, D. Ferrero, A. Keller, R. Kirsch, M. Phillips, and C. Reinhart, “The zero forcing polynomial of a graph,” *Discrete Applied Mathematics* 258 (2019), 35–48. DOI: 10.1016/j.dam.2018.11.033.
3. “On the \(Z_q\)-forcing number: computational approach and exact values,” *Journal of Physics: Complexity*. DOI: 10.1088/2632-072X/ae1430.
4. AIM Minimum Rank — Special Graphs Work Group, “Zero forcing sets and the minimum rank of graphs,” *Linear Algebra and its Applications* 428 (2008), 1628–1648. DOI: 10.1016/j.laa.2007.10.009.
