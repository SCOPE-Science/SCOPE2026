# Five relative cyclic subgroup commutativity degrees for \(C_r\rtimes C_{pq}\)

## Finding

Let \(p,q,r\) be distinct primes satisfying
\[
pq\mid r-1,
\]
and let
\[
G=C_r\rtimes C_{pq}
\]
be the faithful Frobenius semidirect product. For \(H\le G\), write
\[
\operatorname{csd}(H,G)
=
\frac{
|\{(H_1,G_1)\in L_1(H)\times L_1(G):H_1G_1=G_1H_1\}|
}{
|L_1(H)|\,|L_1(G)|
},
\]
where \(L_1(X)\) is the set of cyclic subgroups of \(X\).

Put
\[
L=3r+2.
\]
Then every subgroup of \(G\) is conjugate to exactly one of
\[
1,\quad C_r,\quad C_p,\quad C_q,\quad C_{pq},\quad
C_r\rtimes C_p,\quad C_r\rtimes C_q,\quad G.
\]

The corresponding relative cyclic subgroup commutativity degrees are
\[
\operatorname{csd}(1,G)=\operatorname{csd}(C_r,G)=1,
\]
\[
\operatorname{csd}(C_p,G)
=
\operatorname{csd}(C_q,G)
=
\frac{3r+7}{2L},
\]
\[
\operatorname{csd}(C_{pq},G)
=
\frac{3r+17}{4L},
\]
\[
\operatorname{csd}(C_r\rtimes C_p,G)
=
\operatorname{csd}(C_r\rtimes C_q,G)
=
\frac{11r+4}{(r+2)L},
\]
and
\[
\operatorname{csd}(G)
=
\frac{21r+4}{L^2}.
\]

These five numbers are pairwise distinct. In fact,
\[
1>
\frac{3r+7}{2L}>
\frac{3r+17}{4L}>
\frac{11r+4}{(r+2)L}>
\frac{21r+4}{L^2}.
\]
Therefore
\[
\boxed{|\operatorname{Im} f_1|=5.}
\]

This determines all relative cyclic subgroup commutativity degrees for the square-free Frobenius family
\[
C_r\rtimes C_{pq}
\]
that was explicitly singled out in the published literature as a difficult three-non-normal-class test family.

## Assumptions and scope

The action of \(C_{pq}\) on \(C_r\) is faithful. Since
\[
pq\mid r-1,
\]
such an action exists because
\[
\operatorname{Aut}(C_r)\cong C_{r-1}.
\]
Every nonidentity element of the complement acts fixed-point-freely on the nonidentity elements of \(C_r\), so the semidirect product is Frobenius.

The invariant is the relative cyclic subgroup commutativity degree, not the elementwise relative commutativity degree and not the relative subgroup commutativity degree using all subgroups.

The primes \(p\) and \(q\) play symmetric roles. The formulas depend on them only through the existence condition
\[
pq\mid r-1;
\]
once the Frobenius action exists, the relative degrees depend only on \(r\).

## Proof

Write
\[
A=C_r
\]
for the Frobenius kernel and
\[
B=C_{pq}
\]
for a fixed complement. Let \(P\) and \(Q\) denote the unique subgroups of \(B\) of orders \(p\) and \(q\).

First classify the subgroups.

The kernel \(A\) is the unique Sylow \(r\)-subgroup. If \(H\le G\) contains \(A\), then
\[
H/A\le G/A\cong C_{pq},
\]
so
\[
H\in\{A,\ A\rtimes P,\ A\rtimes Q,\ G\}.
\]

Now suppose
\[
H\cap A=1.
\]
Projection to \(G/A\) is injective on \(H\), so \(H\) is cyclic of order
\[
1,\quad p,\quad q,\quad\text{or}\quad pq.
\]
The complements of \(A\) in the relevant Hall subgroups are conjugate by \(A\). Since every nonidentity subgroup of \(B\) acts fixed-point-freely on \(A\),
\[
C_A(P)=C_A(Q)=C_A(B)=1.
\]
Hence
\[
N_G(P)=N_G(Q)=N_G(B)=B.
\]
It follows that the subgroups of orders \(p\), \(q\), and \(pq\) each form a conjugacy class of size \(r\). This gives exactly the eight subgroup-conjugacy types displayed above.

In particular, the cyclic subgroups of \(G\) are
\[
1,\quad A,
\]
together with \(r\) conjugates of each of
\[
P,\quad Q,\quad B.
\]
Therefore
\[
|L_1(G)|=2+3r=L.
\]

Next count cyclic-subgroup permuting partners.

Both \(1\) and \(A\) permute with every cyclic subgroup, so each has \(L\) partners.

Fix one complement \(B_i\). Its three nontrivial cyclic subgroups
\[
P_i,\quad Q_i,\quad B_i
\]
permute pairwise because \(B_i\) is cyclic. Together with \(1\) and \(A\), this gives five partners for each of \(P_i,Q_i,B_i\).

There are no further partners. Two distinct order-\(p\) subgroups cannot permute, because their product would be a subgroup of order \(p^2\), but
\[
p^2\nmid |G|.
\]
The same argument applies to distinct order-\(q\) subgroups. If \(P_i\) and \(Q_j\) permute, their product is a subgroup of order \(pq\), hence a complement. Such a complement normalizes \(P_i\), but
\[
N_G(P_i)=B_i,
\]
so it must be \(B_i\), forcing
\[
Q_j=Q_i.
\]
Likewise, a subgroup \(P_i\) or \(Q_i\) can permute with a complement only when it lies in that complement. Finally, distinct complements cannot permute: they have trivial intersection and their product would have order
\[
p^2q^2,
\]
which does not divide \(|G|\).

Thus every nonnormal cyclic subgroup has exactly five cyclic-subgroup partners.

We can now compute every relative degree.

For \(1\) and \(A\), all cyclic subgroups appearing in \(L_1(H)\) are universal partners, so
\[
\operatorname{csd}(1,G)
=
\operatorname{csd}(A,G)
=
1.
\]

For \(P\) or \(Q\),
\[
|L_1(P)|=|L_1(Q)|=2,
\]
and the two partner counts are \(L\) and \(5\). Hence
\[
\operatorname{csd}(P,G)
=
\operatorname{csd}(Q,G)
=
\frac{L+5}{2L}
=
\frac{3r+7}{2L}.
\]

The complement \(B\cong C_{pq}\) has four cyclic subgroups,
\[
1,\quad P,\quad Q,\quad B.
\]
Their partner counts are
\[
L,\quad 5,\quad 5,\quad 5,
\]
so
\[
\operatorname{csd}(B,G)
=
\frac{L+15}{4L}
=
\frac{3r+17}{4L}.
\]

The subgroup
\[
A\rtimes P
\]
has exactly
\[
r+2
\]
cyclic subgroups: \(1\), \(A\), and its \(r\) order-\(p\) complements. Therefore
\[
\operatorname{csd}(A\rtimes P,G)
=
\frac{2L+5r}{(r+2)L}
=
\frac{11r+4}{(r+2)L}.
\]
The same computation applies to
\[
A\rtimes Q.
\]

Finally,
\[
G
\]
has two universal cyclic subgroups and \(3r\) nonnormal cyclic subgroups, each with five partners. Thus
\[
\operatorname{csd}(G)
=
\frac{2L+15r}{L^2}
=
\frac{21r+4}{L^2}.
\]

It remains to compare the five values. Because \(p\) and \(q\) are distinct primes,
\[
pq\ge6.
\]
Since
\[
pq\mid r-1,
\]
we have
\[
r\ge7.
\]
The successive differences are
\[
1-\frac{3r+7}{2L}
=
\frac{3(r-1)}{2L},
\]
\[
\frac{3r+7}{2L}
-
\frac{3r+17}{4L}
=
\frac{3(r-1)}{4L},
\]
\[
\frac{3r+17}{4L}
-
\frac{11r+4}{(r+2)L}
=
\frac{3(r-1)(r-6)}{4(r+2)L},
\]
and
\[
\frac{11r+4}{(r+2)L}
-
\frac{21r+4}{L^2}
=
\frac{12r(r-1)}{(r+2)L^2}.
\]
All are positive. Therefore the image contains exactly five values.

## Verification

The included replay constructs the semidirect products directly as pairs
\[
(a,b)\in \mathbf Z/r\mathbf Z\times\mathbf Z/pq\mathbf Z
\]
with multiplication
\[
(a,b)(c,d)
=
(a+t^bc,\ b+d),
\]
where \(t\) has multiplicative order \(pq\) modulo \(r\).

For the cases
\[
(p,q,r)=(2,3,7),\quad(2,5,11),\quad(2,3,13),
\]
the replay:

- enumerates every cyclic subgroup from the group multiplication;
- checks that there are exactly \(3r+2\) cyclic subgroups;
- compares \(HK\) and \(KH\) for every ordered pair of cyclic subgroups;
- verifies that \(1\) and \(C_r\) have \(3r+2\) partners and every other cyclic subgroup has exactly five;
- computes each relative cyclic subgroup commutativity degree directly from its definition;
- verifies all five closed formulas and their distinctness.

The replay returns `VERIFY_OK`.

Finite enumeration is not used to prove the universal theorem.

## Relationship to prior work

The 2019 paper introducing relative cyclic subgroup commutativity degrees develops the invariant, determines several families with few values, and ends with a research program based on the number of conjugacy classes of nonnormal subgroups.

Its published final section explicitly identifies
\[
C_r\rtimes C_{pq},
\qquad
pq\mid r-1,
\]
as a Frobenius group with three nonnormal conjugacy classes of subgroups. It states that resolving
\[
|\operatorname{Im} f_1|
\]
for this family requires computing and comparing the six nontrivial relative degrees represented by
\[
G,\quad C_{pq},\quad C_p,\quad C_q,\quad C_r\rtimes C_p,\quad C_r\rtimes C_q.
\]
The theorem above performs exactly that calculation and shows that the six listed types collapse to four nontrivial values, with the two normal cyclic types contributing the fifth value \(1\).

A later paper classifies finite groups with five relative commutativity degrees, but its invariant is the elementwise relative commutativity degree
\[
d(H,G),
\]
not the cyclic-subgroup invariant
\[
\operatorname{csd}(H,G).
\]
It therefore does not cover this result.

Targeted searches using the Frobenius presentation, the three-nonnormal-class formulation, the invariant name, and the exact divisibility condition did not locate an equivalent arbitrary-\(p,q,r\) formula.

## Limitations

The theorem assumes the faithful Frobenius action of the full cyclic complement \(C_{pq}\). Semidirect products in which the action has a nontrivial kernel have different subgroup structure.

The result treats the square-free complement \(C_{pq}\). Complements with more prime factors introduce additional cyclic subgroup types and need a larger divisor-lattice count.

The theorem determines the relative cyclic subgroup commutativity function for this family, but it does not classify all groups with three or four nonnormal conjugacy classes of subgroups.

An equivalent calculation may exist under ZM-group notation or subgroup-permutability terminology that was not exposed by the indexed searches.

## References

1. M.-S. Lazorec, “Relative cyclic subgroup commutativity degrees of finite groups,” arXiv:1803.01149v1, first public version 3 March 2018; later published in *Filomat* 33(13) (2019), 4021–4032, DOI 10.2298/FIL1913021L.
2. M. Farrokhi Derakhshandeh Ghouchan, “Finite groups with five relative commutativity degrees,” arXiv:1912.04550v1, first public version 10 December 2019; later published in *Results in Mathematics* 77 (2022), article 56, DOI 10.1007/s00025-021-01591-3.
