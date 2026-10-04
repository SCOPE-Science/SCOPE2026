# Exactly \(p\) fixed points for automorphisms of rank-two abelian \(p\)-groups

## Finding

Let \(p\) be a prime and let
\[
A=C_{p^a}\oplus C_{p^b},
\qquad
1\le a<b.
\]
For a divisor \(d\) of \(|A|\), let
\[
\theta(A,d)
=
\#\{\varphi\in\operatorname{Aut}(A):|\operatorname{Fix}(\varphi)|=d\}.
\]

Then the complete rank-two distinct-exponent formula for exactly \(p\) fixed points is
\[
\boxed{
\theta(A,p)=
\begin{cases}
p(2p^3-4p^2+1),&(a,b)=(1,2),\\[2mm]
p^b(p-2)(2p-1),&a=1,\ b\ge3,\\[2mm]
p^{4a-3}(p-1)(2p^2-3p-1),&a\ge2,\ b=a+1,\\[2mm]
2p^{3a+b-3}(p-1)(p-2),&a\ge2,\ b\ge a+2.
\end{cases}}
\]

The formula recovers the previously known cases
\[
C_p\oplus C_{p^2},\qquad
C_p\oplus C_{p^3},\qquad
C_{p^2}\oplus C_{p^3},
\]
and gives every remaining pair of distinct exponents.

For \(p=2\), a sharp exponent-gap transition follows:
\[
\theta(C_{2^a}\oplus C_{2^b},2)>0
\quad\Longleftrightarrow\quad
b=a+1.
\]
More precisely,
\[
\theta(C_2\oplus C_4,2)=2
\]
and, for \(a\ge2\),
\[
\theta(C_{2^a}\oplus C_{2^{a+1}},2)=2^{4a-3}.
\]

## Assumptions and scope

All groups are written additively.

The automorphism-counting function \(\theta(A,d)\) records automorphisms with exactly \(d\) fixed elements, not merely whether \(d\) occurs as a possible fixed-point number.

For \(1\le a<b\), every automorphism of
\[
A=C_{p^a}\oplus C_{p^b}
\]
has a unique matrix form
\[
\varphi=
\begin{pmatrix}
\alpha&\beta\\
p^{b-a}\gamma&\delta
\end{pmatrix},
\]
where
\[
\alpha\in(\mathbb Z/p^a\mathbb Z)^\times,
\quad
\beta,\gamma\in\mathbb Z/p^a\mathbb Z,
\quad
\delta\in(\mathbb Z/p^b\mathbb Z)^\times.
\]
This is the same matrix model used in the 2018 source for the arbitrary distinct-exponent rank-two family.

The primary classification is MSC2020 \(20K30\), which covers automorphisms, homomorphisms, and endomorphisms of abelian groups.

## Proof

Put
\[
d=b-a,
\qquad
u=\alpha-1,
\qquad
v=\delta-1.
\]
A fixed point \((x,y)\in C_{p^a}\oplus C_{p^b}\) satisfies
\[
ux+\beta y\equiv0\pmod{p^a},
\]
\[
p^d\gamma x+vy\equiv0\pmod{p^b}.
\]

We partition the automorphisms according to whether \(u\) and \(v\) are units modulo \(p\).

If both \(u\) and \(v\) are units modulo \(p\), then \(\varphi-I\) is an automorphism of the finite \(p\)-group, so the identity is the only fixed point. This case contributes nothing to \(\theta(A,p)\).

Suppose first that \(u\) is a unit and \(p\mid v\). The first congruence uniquely determines \(x\) from \(y\), and substitution into the second congruence gives
\[
\left(v-p^d\gamma u^{-1}\beta\right)y\equiv0\pmod{p^b}.
\]
There are exactly \(p\) solutions precisely when
\[
\nu_p\!\left(v-p^d\gamma u^{-1}\beta\right)=1.
\]
For each choice of \(\alpha,\beta,\gamma\), exactly
\[
(p-1)p^{b-2}
\]
choices of \(\delta\equiv1\pmod p\) satisfy this condition. Since there are
\[
p^{a-1}(p-2)
\]
choices of \(\alpha\) for which \(u\) is a unit, this case contributes
\[
N_1=p^{3a+b-3}(p-1)(p-2).
\]

Now suppose \(p\mid u\) and \(v\) is a unit. The second congruence uniquely determines \(y\) from \(x\), and substitution into the first gives
\[
\left(u-\beta v^{-1}p^d\gamma\right)x\equiv0\pmod{p^a}.
\]

If \(a=1\), the coefficient vanishes modulo \(p\), so every \(x\in C_p\) occurs and the fixed-point group has order \(p\). Hence this case contributes
\[
N_2=p^{b+1}(p-2).
\]

If \(a\ge2\), exact order \(p\) is equivalent to
\[
\nu_p\!\left(u-\beta v^{-1}p^d\gamma\right)=1.
\]
For each fixed \(\beta,\gamma,\delta\), exactly
\[
(p-1)p^{a-2}
\]
choices of \(\alpha\equiv1\pmod p\) satisfy this condition. Thus
\[
N_2=p^{3a+b-3}(p-1)(p-2)
\]
for \(a\ge2\).

It remains to consider
\[
p\mid u,
\qquad
p\mid v.
\]

If \(p\mid\beta\), then \((\varphi-I)(A)\subseteq pA\). Therefore the cokernel of \(\varphi-I\) surjects onto
\[
A/pA\cong C_p^2,
\]
so its order is at least \(p^2\). Since an endomorphism of a finite group has kernel and cokernel of equal cardinality, there cannot be exactly \(p\) fixed points.

Assume therefore that \(\beta\) is a unit.

If \(d\ge2\), choose a lift \(t\) satisfying
\[
t\beta\equiv v\pmod{p^2}.
\]
Because \(p\mid v\), also \(p\mid t\). The map
\[
\lambda:A\longrightarrow C_{p^2},
\qquad
\lambda(x,y)=y-tx\pmod{p^2},
\]
is well defined and surjective. Moreover,
\[
\lambda\bigl((\varphi-I)(x,y)\bigr)
=
p^d\gamma x+vy-t(ux+\beta y)
\equiv0\pmod{p^2}.
\]
Thus the cokernel of \(\varphi-I\) again has order at least \(p^2\). Consequently this double-unipotent case contributes nothing when
\[
b-a\ge2.
\]

Now let
\[
d=1.
\]
If \(p\mid\gamma\), the same map \(\lambda\) works because
\[
p\gamma\equiv0\pmod{p^2},
\]
so again there are at least \(p^2\) fixed points.

Finally assume that both \(\beta\) and \(\gamma\) are units. The first fixed-point congruence gives
\[
y\equiv-\beta^{-1}ux\pmod{p^a},
\]
so write
\[
y=-\beta^{-1}ux+p^az,
\qquad
z\in C_p.
\]
The second congruence becomes
\[
\left(p\gamma-v\beta^{-1}u\right)x\equiv0\pmod{p^{a+1}},
\]
because \(vp^az\) is divisible by \(p^{a+1}\). The coefficient has \(p\)-adic valuation exactly \(1\): its first term has valuation \(1\), whereas its second term has valuation at least \(2\). Hence
\[
x=0
\]
in \(C_{p^a}\), while \(z\) is arbitrary. There are exactly \(p\) fixed points.

The number of automorphisms in this final case is
\[
N_3
=
p^{a-1}\cdot p^a\cdot
p^{a-1}(p-1)\cdot p^{a-1}(p-1)
=
p^{4a-3}(p-1)^2.
\]

We now add the disjoint contributions.

For \((a,b)=(1,2)\),
\[
N_1+N_2+N_3
=
p(2p^3-4p^2+1).
\]

For \(a=1\) and \(b\ge3\),
\[
N_1+N_2
=
p^b(p-2)(2p-1).
\]

For \(a\ge2\) and \(b=a+1\),
\[
2N_1+N_3
=
p^{4a-3}(p-1)(2p^2-3p-1).
\]

For \(a\ge2\) and \(b\ge a+2\),
\[
N_1+N_2
=
2p^{3a+b-3}(p-1)(p-2).
\]

These are exactly the four cases in the theorem.

## Verification

The included replay enumerates the matrix model of the full automorphism group and directly solves the two fixed-point congruences for several primes and exponent pairs.

It verifies the theorem in all four structural regimes, including the characteristic-two transition. In particular, it checks:
\[
(p,a,b)\in
\{
(2,1,2),(2,1,3),(2,2,3),(2,2,4),
(3,1,2),(3,1,3),(3,2,3),(3,2,4),
(5,1,2),(5,1,3)
\}.
\]

The replay also checks that the three previously published special cases agree exactly with the corresponding branches of the formula:
\[
C_p\oplus C_{p^2},
\qquad
C_p\oplus C_{p^3},
\qquad
C_{p^2}\oplus C_{p^3}.
\]

It returns `VERIFY_OK`.

The finite enumeration is a replay only. The proof above establishes the formula for every prime and every pair \(1\le a<b\).

## Relationship to prior work

Hayat, López-Aguayo, and Abbas introduced the notation \(\theta(G,d)\) in the present setting, proved all \(\theta\)-values for \(C_p\oplus C_{p^2}\), and obtained
\[
\theta(C_{p^a}\oplus C_{p^b},1)
=
p^{3a+b-2}(p-2)^2
\]
for arbitrary \(1\le a<b\). Their 2018 paper ends by asking for exact formulas for \(\theta\) on direct sums of cyclic \(p\)-groups with distinct exponents. The theorem here gives the complete \(d=p\) slice for rank two.

Two further small exponent pairs were already known. Hayat and Ali computed all \(\theta\)-values for \(C_p\oplus C_{p^3}\) in 2016, and Ali, Hayat, and Li computed all \(\theta\)-values for \(C_{p^2}\oplus C_{p^3}\) in 2019. Their \(d=p\) expressions simplify respectively to the \(a=1,b=3\) and \(a=2,b=3\) cases of the theorem above.

Senden later determined the Reidemeister spectrum of every finite abelian group. For a finite abelian group, the Reidemeister number of an automorphism equals its number of fixed points. That result determines which powers of \(p\) can occur as fixed-point counts, but not how many automorphisms realize a given count. Thus it does not imply the multiplicity formula \(\theta(A,p)\).

The primary MSC classification \(20K30\) is independently confirmed by the published Reidemeister-spectrum paper for this same automorphism/fixed-point subject.

## Limitations

The theorem gives one natural nontrivial slice, \(d=p\), of the general \(\theta\)-value problem. It does not determine \(\theta(A,p^j)\) for arbitrary \(j\ge2\), nor does it treat rank at least three.

The proof uses the distinct-exponent rank-two matrix model. Equal exponents require a different analysis because the automorphism group is a full general linear group over a finite local ring.

The literature search inspected the 2018 open-problem source, the 2019 \(C_{p^2}\oplus C_{p^3}\) computation, the 2016 \(C_p\oplus C_{p^3}\) statement, and the 2023 Reidemeister-spectrum result. Targeted searches found no arbitrary-\((a,b)\) multiplicity formula for exactly \(p\) fixed points. An equivalent formula could nevertheless exist under different notation or in unindexed literature.

## References

1. U. Hayat, D. López-Aguayo, and A. Abbas, “Fixed Points of Automorphisms of Certain Non-Cyclic p-Groups and the Dihedral Group,” *Symmetry* 10 (2018), 238, DOI 10.3390/sym10070238.
2. U. Hayat and F. Ali, “Fixed points of automorphisms of \(C_p\times C_{p^3}\),” *Journal of Mathematical Analysis* 7(6) (2016), 91–101.
3. F. Ali, U. Hayat, and Y. Li, “Fixed points of automorphisms of certain finite groups,” *International Journal of Algebra* 13(4) (2019), 167–183, DOI 10.12988/ija.2019.9618.
4. P. Senden, “The Reidemeister spectrum of finite abelian groups,” *Proceedings of the Edinburgh Mathematical Society* 66 (2023), 940–959, DOI 10.1017/S0013091523000500, arXiv:2205.15740.
