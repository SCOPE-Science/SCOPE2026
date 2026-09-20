# A cyclic-Sylow obstruction to ψ-divisibility and the classification of Z-groups

Let
\[
\psi(G)=\sum_{g\in G}o(g)
\]
for a finite group \(G\). Recall that \(G\) is **\(\psi\)-divisible** if
\[
\psi(K)\mid \psi(G)
\qquad\text{for every subgroup }K\le G.
\]

## Theorem

Let
\[
G=P\rtimes H,
\]
where \(P\) is a nontrivial cyclic \(p\)-group, \((|P|,|H|)=1\), and the action of \(H\) on \(P\) is nontrivial. Then \(G\) is not \(\psi\)-divisible.

Equivalently, if a finite \(\psi\)-divisible group has a normal cyclic Sylow \(p\)-subgroup \(P\), then \(P\le Z(G)\).

## Proof

Put
\[
t=|P|,\qquad A=\psi(P),\qquad
C=C_H(P),\qquad h=\psi(H),\qquad c=\psi(C).
\]
Since the action is nontrivial, \(C<H\), hence \(h>c\).

For a normal cyclic Sylow subgroup and a complement, the standard sum-of-element-orders formula is
\[
\psi(G)=t\,h+(A-t)c.
\tag{1}
\]
This is Lemma 2.1(iii) in Lazorec's notation, ultimately the normal-cyclic-Sylow formula used throughout the literature on \(\psi\).

Assume for contradiction that \(G\) is \(\psi\)-divisible.

First, \(H\le G\), so \(h\mid\psi(G)\). From (1),
\[
h\mid (A-t)c.
\tag{2}
\]

Second, \(C\) centralizes \(P\), so \(PC=P\times C\). Since \((|P|,|C|)=1\),
\[
\psi(PC)=\psi(P)\psi(C)=Ac.
\]
Thus \(Ac\mid\psi(G)\). Subtracting \(Ac\) from (1) gives
\[
Ac\mid t(h-c).
\tag{3}
\]

Write
\[
d=(h,c),\qquad h=dx,\qquad c=dy,\qquad (x,y)=1.
\]
Because \(h>c\), we have \(x>y\).

From (2),
\[
x\mid (A-t)y,
\]
and therefore, since \((x,y)=1\),
\[
x\mid A-t.
\tag{4}
\]
Hence \(x\le A-t<A\).

From (3),
\[
Ay\mid t(x-y),
\]
so in particular
\[
A\mid t(x-y).
\tag{5}
\]
For a cyclic \(p\)-group \(P\),
\[
\psi(P)=\frac{p^{2a+1}+1}{p+1}\equiv1\pmod p
\qquad (|P|=p^a),
\]
and consequently \((A,t)=1\). Thus (5) yields
\[
A\mid x-y.
\tag{6}
\]
But
\[
0<x-y<x\le A-t<A,
\]
contradicting (6). Hence \(G\) is not \(\psi\)-divisible. \(\square\)

## Corollary 1: normal cyclic Sylow subgroups are central

If \(P\) is a normal cyclic Sylow \(p\)-subgroup of a finite \(\psi\)-divisible group \(G\), Schur--Zassenhaus gives a complement \(H\) with \(G=P\rtimes H\). The theorem rules out a nontrivial action, so \(P\le Z(G)\).

## Corollary 2: classification of \(\psi\)-divisible Z-groups

A finite **Z-group** is a finite group whose Sylow subgroups are cyclic. Then
\[
\boxed{\text{\(G\) is a \(\psi\)-divisible Z-group}
\iff
\text{\(G\) is cyclic of square-free order}.}
\]

Indeed, a nonnilpotent Z-group has a standard presentation
\[
ZM(m,n,r)=
\langle a,b\mid a^m=b^n=1,\ b^{-1}ab=a^r\rangle,
\]
with
\[
(m,n)=(m,r-1)=1,\qquad r^n\equiv1\pmod m,
\]
and \(m,n>1\). Choose any prime power \(p^a\Vert m\). The Sylow \(p\)-subgroup
of \(\langle a\rangle\) is cyclic and normal, and the condition
\((m,r-1)=1\) makes the action of \(b\) on it nontrivial. The theorem therefore
excludes every nonnilpotent Z-group.

A nilpotent Z-group is cyclic. Harrington--Jones--Lamarche proved that a finite
abelian group is \(\psi\)-divisible exactly when it is cyclic of square-free
order. This gives the classification.

## Corollary 3: the square-free-order open problem

Every finite group of square-free order is a Z-group. Therefore
\[
\boxed{\text{no nonnilpotent group of square-free order is \(\psi\)-divisible}.}
\]

This answers negatively the open problem stated by Lazorec after Proposition
2.4 of *On a divisibility property involving the sum of element orders*.
That paper had proved a partial ZM-group obstruction and computationally checked
all nonnilpotent square-free-order groups of order at most \(72000\).

## Relation to prior work

Harrington, Jones and Lamarche introduced the \(\psi\)-divisibility terminology
and classified the abelian case in 2014; they explicitly noted that they knew no
nonabelian examples.

Lazorec's 2020/2021 paper studied ZM-groups and proved, under an additional
arithmetic hypothesis, that certain \(ZM(p^\alpha,n,r)\) groups are not
\(\psi\)-divisible. It then asked whether any finite nonnilpotent group of
square-free order can be \(\psi\)-divisible. The proof above removes those
arithmetic restrictions for every semidirect product with a noncentral normal
cyclic Sylow subgroup, and consequently classifies all \(\psi\)-divisible
Z-groups.

Lazorec's 2023 paper on the \(\psi\)-divisibility graph still stated that the
only known examples were cyclic groups of square-free order and that existence
of nonabelian \(\psi\)-divisible groups remained open. The present result does
not settle that broader question: it excludes a large structural class, but a
hypothetical nonabelian \(\psi\)-divisible group could have no noncentral normal
cyclic Sylow subgroup.

## Limitations

The theorem does not classify all finite \(\psi\)-divisible groups and does not
exclude every possible nonabelian example. Its hypothesis requires a normal
cyclic Sylow subgroup with a nontrivial coprime complement action.

Originality is asserted only to the best of our knowledge. Searches through the
2020/2021 and 2023 \(\psi\)-divisibility papers and current literature did not
locate this two-subgroup divisibility argument, the resulting normal-cyclic-Sylow
obstruction, or the resulting classification of Z-groups. An unindexed or
differently phrased prior observation could still exist.

## References

1. J. Harrington, L. Jones, A. Lamarche, “Characterizing Finite Groups Using the Sum of the Orders of the Elements,” *International Journal of Combinatorics* (2014), Article ID 835125. https://doi.org/10.1155/2014/835125
2. M.-S. Lazorec, “On a Divisibility Property Involving the Sum of Element Orders,” *Bulletin of the Malaysian Mathematical Sciences Society* 44 (2021), 941–951. https://doi.org/10.1007/s40840-020-00987-8
3. M.-S. Lazorec, “A graph related to the sum of element orders of a finite group,” *Contributions to Discrete Mathematics* 18(2) (2023), 113–128. https://doi.org/10.55016/ojs/cdm.v18i2.73182
4. M. Herzog, P. Longobardi, M. Maj, “An exact upper bound for sums of element orders in non-cyclic finite groups,” *Journal of Pure and Applied Algebra* 222(7) (2018), 1628–1642. https://doi.org/10.1016/j.jpaa.2017.07.010
