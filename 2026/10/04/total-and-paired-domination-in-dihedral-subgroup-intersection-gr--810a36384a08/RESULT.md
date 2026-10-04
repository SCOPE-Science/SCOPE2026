# Total and paired domination in dihedral subgroup intersection graphs

## Finding

Let \(D_{2n}=\langle a,b\mid a^n=b^2=1,\ bab=a^{-1}\rangle\) with \(n\ge3\), and let \(\Gamma(D_{2n})\) be the intersection graph on the proper nontrivial subgroups, where distinct vertices are adjacent exactly when their intersection is nontrivial. If \(n\) is prime, then \(\Gamma(D_{2n})\) is edgeless, so neither total nor paired domination exists. If \(n\) is composite and \(p\) is its smallest prime divisor, then \[\gamma_t(\Gamma(D_{2n}))=\begin{cases}p,&p^2\mid n,\\ p+1,&p^2\nmid n,\end{cases}\] and \[\gamma_{\mathrm{pr}}(\Gamma(D_{2n}))=2\left\lceil\frac{\gamma_t(\Gamma(D_{2n}))}{2}\right\rceil.\] Equivalently, for composite \(n\), paired domination equals \(2\) when \(4\mid n\), equals \(4\) when \(n\equiv2\pmod4\), and equals \(p+1\) when \(n\) is odd. In every composite case the ordinary minimum dominating construction can be chosen to induce a clique, so total domination has no extra cost over ordinary domination; paired domination adds exactly the parity correction.

The result completely separates the genuine obstruction from the matching obstruction: prime dihedral groups have an edgeless subgroup intersection graph, composite dihedral groups admit minimum total dominating sets at the ordinary domination bound, and paired domination changes that bound only when it is odd.

## Assumptions and scope

Let
\[
D_{2n}=\langle a,b\mid a^n=b^2=1,\ bab=a^{-1}\rangle,
\qquad n\ge3.
\]
The graph \(\Gamma(D_{2n})\) has as vertices all proper nontrivial subgroups of \(D_{2n}\), with distinct vertices adjacent when their intersection is nontrivial.

A total dominating set \(\mathcal D\) requires every vertex, including every member of \(\mathcal D\), to have a neighbor in \(\mathcal D\). A paired dominating set is a dominating set whose induced subgraph has a perfect matching.

For each divisor \(d\mid n\) and residue \(r\pmod d\), write
\[
H_{d,r}=\langle a^d,a^r b\rangle.
\]
When \(d>1\), this is a proper dihedral subgroup containing exactly \(n/d\) reflection subgroups. Let \(p\) be the smallest prime divisor of \(n\).

## Proof

Every reflection \(a^j b\) generates a subgroup
\[
R_j=\langle a^j b\rangle
\]
of order two. Since \(R_j\) has prime order, a subgroup vertex intersects \(R_j\) nontrivially exactly when it contains \(R_j\). Hence every dominating set must cover all \(n\) reflection subgroups by containment.

A proper subgroup containing a reflection is dihedral of the form \(H_{d,r}\) with \(d\mid n\) and \(d>1\). It contains exactly \(n/d\) reflections, and therefore at most \(n/p\) reflections. Consequently every dominating set, and hence every total dominating set, has at least \(p\) vertices.

Suppose first that \(n\) is prime. The proper nontrivial subgroups are \(\langle a\rangle\) and the \(n\) reflection subgroups. Any two of them intersect trivially, so the graph is edgeless. Total and paired dominating sets do not exist.

Now assume \(n\) is composite. For \(0\le r<p\), put
\[
P_r=H_{p,r}=\langle a^p,a^r b\rangle.
\]
The \(p\) subgroups \(P_0,\ldots,P_{p-1}\) partition the reflection subgroups: each contains exactly \(n/p\) of them. Moreover, because \(n/p>1\), any two distinct \(P_r,P_s\) have the nontrivial common subgroup \(\langle a^p\rangle\). Thus these \(p\) vertices induce a clique.

If \(p^2\mid n\), the cyclic subgroup \(\langle a^p\rangle\) contains the subgroup of order \(q\) for every prime \(q\mid n\), including \(q=p\). Hence the union of the \(P_r\) contains every minimal subgroup of \(D_{2n}\): all reflections and every prime-order rotation subgroup. Therefore
\[
\{P_0,\ldots,P_{p-1}\}
\]
is a dominating set. Since it induces a clique, it is total dominating, so
\[
\gamma_t(\Gamma(D_{2n}))=p.
\]

Suppose instead that \(p^2\nmid n\). Any collection of exactly \(p\) proper subgroups covering all \(n\) reflections must make every member attain the maximum \(n/p\) reflection count. Thus it is precisely the family
\[
P_0,\ldots,P_{p-1}.
\]
The order-\(p\) rotation subgroup
\[
L=\langle a^{n/p}\rangle
\]
has trivial intersection with \(\langle a^p\rangle\) because \(p^2\nmid n\). Hence none of the \(P_r\) dominates \(L\), proving the lower bound
\[
\gamma_t(\Gamma(D_{2n}))\ge p+1.
\]
Adding the rotation subgroup \(\langle a\rangle\) fixes this: it contains every prime-order rotation subgroup, and
\[
\langle a\rangle\cap P_r=\langle a^p\rangle\ne1.
\]
Thus
\[
\{P_0,\ldots,P_{p-1},\langle a\rangle\}
\]
is a clique and a total dominating set, giving
\[
\gamma_t(\Gamma(D_{2n}))=p+1.
\]

It remains to impose the perfect-matching condition. Every paired dominating set is total dominating and has even cardinality, so
\[
\gamma_{\mathrm{pr}}\ge
2\left\lceil\frac{\gamma_t}2\right\rceil.
\]
If the displayed total minimum has even size, it is a clique and hence has a perfect matching, giving equality immediately.

There are only two odd-size cases. If \(p^2\mid n\) and \(p\) is odd, append \(\langle a^p\rangle\) to the \(p\)-clique \(\{P_r\}\); the resulting clique has size \(p+1\). If \(p=2\) and \(4\nmid n\), the total minimum is the three-clique
\[
\{P_0,P_1,\langle a\rangle\}.
\]
Because \(n\) is composite, \(\langle a^2\rangle\) is nontrivial and is adjacent to all three, producing a four-clique. Therefore in every composite case
\[
\gamma_{\mathrm{pr}}(\Gamma(D_{2n}))
=2\left\lceil\frac{\gamma_t(\Gamma(D_{2n}))}2\right\rceil.
\]

## Verification

The accompanying `verify.py` constructs every proper nontrivial subgroup directly from the dihedral presentation. It builds the intersection graph from literal subgroup intersections, exhaustively searches total and paired dominating sets through the claimed minimum sizes, and separately checks the explicit clique witnesses.

For every \(3\le n\le20\), the replay agrees with the theorem. Exact output:

```text
n=3 prime p=3 vertices=4 total=none paired=none
n=4 composite p=2 vertices=8 gamma_t=2 gamma_pr=2 total_witness=['H_2,0', 'H_2,1'] paired_witness=['H_2,0', 'H_2,1']
n=5 prime p=5 vertices=6 total=none paired=none
n=6 composite p=2 vertices=14 gamma_t=3 gamma_pr=4 total_witness=['H_2,0', 'H_2,1', 'A_1'] paired_witness=['H_2,0', 'H_2,1', 'A_1', 'A_2']
n=7 prime p=7 vertices=8 total=none paired=none
n=8 composite p=2 vertices=17 gamma_t=2 gamma_pr=2 total_witness=['H_2,0', 'H_2,1'] paired_witness=['H_2,0', 'H_2,1']
n=9 composite p=3 vertices=14 gamma_t=3 gamma_pr=4 total_witness=['H_3,0', 'H_3,1', 'H_3,2'] paired_witness=['H_3,0', 'H_3,1', 'H_3,2', 'A_3']
n=10 composite p=2 vertices=20 gamma_t=3 gamma_pr=4 total_witness=['H_2,0', 'H_2,1', 'A_1'] paired_witness=['H_2,0', 'H_2,1', 'A_1', 'A_2']
n=11 prime p=11 vertices=12 total=none paired=none
n=12 composite p=2 vertices=32 gamma_t=2 gamma_pr=2 total_witness=['H_2,0', 'H_2,1'] paired_witness=['H_2,0', 'H_2,1']
n=13 prime p=13 vertices=14 total=none paired=none
n=14 composite p=2 vertices=26 gamma_t=3 gamma_pr=4 total_witness=['H_2,0', 'H_2,1', 'A_1'] paired_witness=['H_2,0', 'H_2,1', 'A_1', 'A_2']
n=15 composite p=3 vertices=26 gamma_t=4 gamma_pr=4 total_witness=['H_3,0', 'H_3,1', 'H_3,2', 'A_1'] paired_witness=['H_3,0', 'H_3,1', 'H_3,2', 'A_1']
n=16 composite p=2 vertices=34 gamma_t=2 gamma_pr=2 total_witness=['H_2,0', 'H_2,1'] paired_witness=['H_2,0', 'H_2,1']
n=17 prime p=17 vertices=18 total=none paired=none
n=18 composite p=2 vertices=43 gamma_t=3 gamma_pr=4 total_witness=['H_2,0', 'H_2,1', 'A_1'] paired_witness=['H_2,0', 'H_2,1', 'A_1', 'A_2']
n=19 prime p=19 vertices=20 total=none paired=none
n=20 composite p=2 vertices=46 gamma_t=2 gamma_pr=2 total_witness=['H_2,0', 'H_2,1'] paired_witness=['H_2,0', 'H_2,1']
VERIFY_OK
```

The finite computation is corroborative only. The arbitrary-\(n\) proof is the reflection-cover lower bound together with the explicit clique constructions above.

## Relationship to prior work

Kayacan's full treatment of dominating sets in subgroup intersection graphs proves the ordinary dihedral formula
\[
\gamma(\Gamma(D_{2n}))=
\begin{cases}
p,&p^2\mid n,\\
p+1,&p^2\nmid n,
\end{cases}
\]
where \(p\) is the smallest prime divisor of \(n\). The paper studies ordinary domination; full-text searches show no use of total domination or paired domination. The present result proves that, for composite \(n\), the ordinary lower bound is attained by a clique, so total domination is exactly the same parameter while paired domination is its least even majorant.

Rajkumar and Devi give a detailed full-text description of the proper subgroups of dihedral groups and compute degrees and clique number for the subgroup intersection graph. Their article does not study domination variants. Their convention includes the trivial proper subgroup, which is isolated; the theorem here uses the standard proper-nontrivial convention of Kayacan.

A later paper on the intersection graph of subgroups of a dihedral group of order \(2pq\) studies detour and eccentricity invariants rather than total or paired domination. Targeted searches under the dihedral, subgroup-intersection, total-domination, paired-domination, and perfect-matching formulations did not locate the stated classification.

## Limitations

The theorem concerns ordinary dihedral groups \(D_{2n}\) and the subgroup intersection graph on proper nontrivial subgroups. It does not assert an analogous formula for generalized quaternion, semidihedral, or arbitrary metacyclic groups.

The result determines the minimum cardinalities, not the number of all minimum total or paired dominating sets. Such enumeration is more delicate when \(p^2\nmid n\), because minimum reflection covers need not be unique once one allows one more subgroup than the reflection-cover lower bound.

The checker covers only \(3\le n\le20\) and is not used as an infinite proof.

## References

1. S. Kayacan, “Dominating Sets in Intersection Graphs of Finite Groups,” arXiv:1602.03537, first posted 10 February 2016; later published in *Rocky Mountain Journal of Mathematics* 48 (2018), 2311–2335. DOI: 10.1216/RMJ-2018-48-7-2311.
2. R. Rajkumar and P. Devi, “Intersection graph of subgroups of some non-abelian groups,” *Malaya Journal of Matematik* 4(2) (2016), 238–242. DOI: 10.26637/mjm402/007.
3. P. M. Khudhur, R. R. Haji, and S. M. S. Khasraw, “The Intersection Graph of Subgroups of the Dihedral Group of Order \(2pq\),” *Iraqi Journal of Science* 62(12) (2021), 4923–4929. DOI: 10.24996/ijs.2021.62.12.30.
