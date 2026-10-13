# Symmetry loss in inclusion graphs of the two rank-two groups of order \(p^3\)

## Finding

Let \(p\) be an odd prime, \(A=C_{p^2}\times C_p\), and \(M=\langle a,b\mid a^{p^2}=b^p=1,\ bab^{-1}=a^{1+p}\rangle\). For the inclusion graph \(\mathcal I(H)\) on the nontrivial proper subgroups of \(H\), both \(\mathcal I(A)\) and \(\mathcal I(M)\) are the balanced double star with \(p\) leaves at each center, hence \[\operatorname{Aut}(\mathcal I(A))\cong\operatorname{Aut}(\mathcal I(M))\cong (S_p\times S_p)\rtimes C_2,\qquad |\operatorname{Aut}(\mathcal I)|=2(p!)^2.\] Under compatible leaf labels, the natural actions of both group automorphism groups have the same image \[H_p=\{(t\mapsto\alpha t+\beta,\ s\mapsto\alpha^{-1}s+\gamma):\alpha\in\mathbb F_p^\times,\ \beta,\gamma\in\mathbb F_p\},\] of order \(p^2(p-1)\). However the kernels have different orders: \(|\ker(\operatorname{Aut}(A)\to\operatorname{Aut}(\mathcal I(A)))|=p(p-1)\) while \(|\ker(\operatorname{Aut}(M)\to\operatorname{Aut}(\mathcal I(M)))|=p\). Thus the inclusion graphs and even their group-induced permutation images coincide, while the symmetry lost by passage from the group to the graph distinguishes the abelian and nonabelian groups.

The common group-induced image has index
\[
\frac{2(p!)^2}{p^2(p-1)}
\]
in the full graph automorphism group. For \(p=3\) this index is \(4\); for \(p=5\) it is \(288\).

## Assumptions and scope

Let \(p\) be an odd prime. Put
\[
A=C_{p^2}\times C_p
\]
and
\[
M=\langle a,b\mid a^{p^2}=b^p=1,\ bab^{-1}=a^{1+p}\rangle.
\]
The latter is the nonabelian modular group of order \(p^3\) and exponent \(p^2\).

For a finite group \(H\), \(\mathcal I(H)\) denotes the graph whose vertices are the nontrivial proper subgroups of \(H\), with two distinct vertices adjacent exactly when one is properly contained in the other.

## Proof

First consider \(A\). Write \(e\) for a generator of the \(C_{p^2}\)-factor and \(f\) for a generator of the \(C_p\)-factor. Let
\[
P=\langle pe\rangle,
\qquad
E=\langle pe,f\rangle.
\]
The proper nontrivial subgroups are
\[
P,\quad E,\quad C_t=\langle e+t f\rangle,\quad Q_s=\langle s pe+f\rangle
\qquad(t,s\in\mathbb F_p).
\]
Here each \(C_t\) is cyclic of order \(p^2\), each \(Q_s\) has order \(p\), and the only containments are
\[
P<E,\qquad P<C_t,\qquad Q_s<E.
\tag{1}
\]
Thus \(\mathcal I(A)\) is a balanced double star: the adjacent centers are \(P,E\), with the \(p\) vertices \(C_t\) pendant at \(P\) and the \(p\) vertices \(Q_s\) pendant at \(E\).

For \(M\), put \(P=\langle a^p\rangle\) and \(E=\langle a^p,b\rangle\). Its proper nontrivial subgroups are
\[
P,\quad E,\quad C_t=\langle ab^t\rangle,\quad Q_s=\langle a^{ps}b\rangle
\qquad(t,s\in\mathbb F_p),
\]
and the containments are again exactly (1). Hence the two inclusion graphs are isomorphic to the same balanced double star.

Any automorphism of this double star may independently permute the \(p\) leaves on each side, and it may also swap the two centers together with their leaf blocks. Therefore
\[
\operatorname{Aut}(\mathcal I(A))\cong\operatorname{Aut}(\mathcal I(M))
\cong (S_p\times S_p)\rtimes C_2
\]
and the common order is \(2(p!)^2\).

We next compute the automorphisms induced by automorphisms of the underlying groups.

Every automorphism of \(A\) has the form
\[
e\longmapsto a e+b f,
\qquad
f\longmapsto pc e+d f,
\tag{2}
\]
where \(a\) is a unit modulo \(p^2\), \(b,c\in\mathbb F_p\), and \(d\in\mathbb F_p^\times\). Consequently
\[
|\operatorname{Aut}(A)|=p^3(p-1)^2.
\tag{3}
\]
Writing \(\bar a\) for the reduction of \(a\) modulo \(p\), (2) sends the two leaf labels by
\[
t\longmapsto \frac{d}{\bar a}t+\frac{b}{\bar a},
\qquad
s\longmapsto \frac{\bar a}{d}s+\frac{c}{d}.
\tag{4}
\]
Thus its image is precisely
\[
H_p=\{(t\mapsto\alpha t+\beta,\ s\mapsto\alpha^{-1}s+\gamma):
\alpha\in\mathbb F_p^\times,\ \beta,\gamma\in\mathbb F_p\},
\tag{5}
\]
which has order \(p^2(p-1)\). The kernel of (4) consists of \(b=c=0\) and \(d\equiv a\pmod p\). There are \(p(p-1)\) such choices, proving
\[
|\ker(\operatorname{Aut}(A)\to\operatorname{Aut}(\mathcal I(A)))|=p(p-1).
\tag{6}
\]

For \(M\), an automorphism is uniquely of the form
\[
a\longmapsto a^i b^j,
\qquad
b\longmapsto a^{pk}b,
\tag{7}
\]
where \(i\) is a unit modulo \(p^2\) and \(j,k\in\mathbb F_p\). To see the restriction on the image of \(b\), note that an arbitrary order-\(p\) candidate has the form \(a^{pk}b^\ell\); applying the defining conjugation relation to the images of \(a,b\) forces \(\ell=1\). Conversely every choice in (7) respects the defining relations and generates \(M\). Hence
\[
|\operatorname{Aut}(M)|=p^3(p-1).
\tag{8}
\]
If \(\bar i=i\bmod p\), the induced leaf permutations are
\[
t\longmapsto \bar i^{-1}t+j\bar i^{-1},
\qquad
s\longmapsto \bar i s+k.
\tag{9}
\]
They again give exactly the subgroup \(H_p\) in (5). The kernel consists of \(j=k=0\) and \(i\equiv1\pmod p\), so it has order \(p\):
\[
|\ker(\operatorname{Aut}(M)\to\operatorname{Aut}(\mathcal I(M)))|=p.
\tag{10}
\]

Equations (5), (6), and (10) prove the claim. They also show that, after identifying the two double stars by the labels above, even the induced permutation subgroups coincide. What differs is exactly the subgroup of group automorphisms annihilated by passage to the inclusion graph.

## Verification

The accompanying `verify.py` was read from its packaged path before replay.

For \(p=3\) and \(p=5\), it constructs both groups directly, enumerates all one- and two-generator proper subgroups, and verifies that each has exactly \(2p+2\) nontrivial proper subgroups and \(2p+1\) inclusion edges with the balanced-double-star degree pattern.

For \(p=3,5,7\), it enumerates the automorphism parameters in (2) and (7), computes their permutations of both leaf blocks, and verifies that the two image sets are exactly the same subgroup \(H_p\). It also checks the two automorphism-group orders, the kernel orders, and the full graph-automorphism index.

Exact replay output:

```text
A direct subgroup census 3 (8, 7)
M direct subgroup census 3 (8, 7)
A direct subgroup census 5 (12, 11)
M direct subgroup census 5 (12, 11)
p=3: graph_aut=72, common_image=18, index=4, kernels=(6,3)
p=5: graph_aut=28800, common_image=100, index=288, kernels=(20,5)
p=7: graph_aut=50803200, common_image=294, index=172800, kernels=(42,7)
VERIFY_OK
```

The finite computations corroborate the symbolic argument. The formulas for arbitrary odd \(p\) are proved directly by the subgroup and automorphism parametrizations above.

## Relationship to prior work

The original inclusion-graph paper gives the subgroup-containment construction and explicitly records that the modular group \(M_{p^3}\) and \(C_{p^2}\times C_p\) have isomorphic subgroup lattices, hence the same inclusion graph. That graph is therefore prior structure, not part of the originality claim.

Later work on inclusion graphs of nilpotent groups determines diameters in the nilpotent case and, according to its abstract and first-page statement, characterizes automorphism groups specifically for inclusion graphs of cyclic groups. The checked source does not state the natural-action image or kernel for either group considered here.

The new point is the comparison between full graph symmetry and symmetry induced from the underlying groups: the full double-star automorphism group is much larger, the two induced permutation images coincide exactly, yet the kernels differ by a factor of \(p-1\).

## Limitations

The theorem is restricted to odd primes. The groups of order eight have different subgroup structures and are not included.

The inclusion graph alone still does not distinguish \(A\) from \(M\), and neither does the induced permutation subgroup after the compatible identification above. The distinction uses the kernel of the natural action, which depends on the underlying group automorphism group as well as the graph.

The 2020 nilpotent-inclusion-graph paper was available here through its abstract and first-page material rather than a complete inspected article; its stated automorphism-group result is for cyclic groups. This leaves a residual bibliographic risk that an interior remark treats these two order-\(p^3\) cases without advertising them in the abstract.

## References

1. Q. Zhang, L. Li, and M. Xu, “Finite \(p\)-Groups All of Whose Proper Quotient Groups are Abelian or Inner-Abelian,” *Communications in Algebra* 38 (2010), 2797–2807. DOI: 10.1080/00927870903074066. Published online 18 August 2010. Mathematics Subject Classification: \(20D15\).
2. P. Devi and R. Rajkumar, “Inclusion graph of subgroups of a group,” arXiv:1604.08259, first submitted 27 April 2016.
3. S. Ou, D. Wong, and Z. Wang, “Diameters and automorphism groups of inclusion graphs over nilpotent groups,” *Journal of Algebra and Its Applications* 19 (2020), 2050097. DOI: 10.1142/S0219498820500978. Published online 29 May 2019.
