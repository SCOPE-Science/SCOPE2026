# Degree-one affine groups over finite fields have an exact realizability dichotomy

## Finding

Let
\[
q=p^f
\]
be a prime power. Then
\[
\operatorname{AGL}_1(\mathbf F_q)
=
(\mathbf F_q,+)\rtimes\mathbf F_q^\times
\]
is the unit group of a finite ring exactly in the following cases:
\[
\boxed{
\operatorname{AGL}_1(\mathbf F_q)\text{ is realizable by a finite ring}
\iff
q=3\text{ or }q\text{ is a power of }2.
}
\]

For every
\[
q=2^f,
\]
there is a uniform local realization of order \(q^2\). Let
\[
\sigma:\mathbf F_q\to\mathbf F_q,
\qquad
\sigma(a)=a^2,
\]
and define the twisted dual-number ring
\[
R_q
=
\mathbf F_q(\varepsilon;\sigma)
=
\mathbf F_q+\mathbf F_q\varepsilon
\]
by
\[
\varepsilon^2=0,
\qquad
\varepsilon a=a^2\varepsilon.
\]
Then
\[
\boxed{
R_q^\times\cong\operatorname{AGL}_1(\mathbf F_q).
}
\]

The only realizable odd-field case is
\[
\boxed{
\operatorname{AGL}_1(\mathbf F_3)
\cong
S_3
\cong
\operatorname{GL}_2(\mathbf F_2)
=
M_2(\mathbf F_2)^\times.
}
\]

Thus the degree-one affine groups over finite fields have a complete finite-ring realizability classification.

## Assumptions and scope

A finite group is called realizable here if it is isomorphic to the multiplicative unit group of a finite unital associative ring.

The affine group is written in the convention
\[
(b,a)(d,c)
=
(b+ad,ac),
\]
where
\[
b,d\in\mathbf F_q
\quad\text{and}\quad
a,c\in\mathbf F_q^\times.
\]

The theorem concerns finite realizing rings. It makes no assertion about realizability by infinite rings of characteristic zero.

The positive construction uses a noncommutative local ring when
\[
q>2.
\]

## Proof

First assume
\[
q=2^f.
\]
Let
\[
R_q=\mathbf F_q+\mathbf F_q\varepsilon
\]
with multiplication determined by
\[
\varepsilon^2=0
\]
and
\[
\varepsilon a=a^2\varepsilon.
\]
Equivalently,
\[
(a+b\varepsilon)(c+d\varepsilon)
=
ac+(ad+bc^2)\varepsilon.
\]

An element
\[
a+b\varepsilon
\]
is a unit exactly when
\[
a\ne0.
\]
Hence
\[
|R_q^\times|=q(q-1).
\]
The subgroup
\[
U=1+\mathbf F_q\varepsilon
\]
is isomorphic to the additive group of \(\mathbf F_q\), and the embedded field units
\[
\mathbf F_q^\times
\]
form a complement.

For
\[
a\in\mathbf F_q^\times
\]
and
\[
b\in\mathbf F_q,
\]
direct multiplication gives
\[
a(1+b\varepsilon)a^{-1}
=
1+ba^{-1}\varepsilon.
\]
Thus
\[
R_q^\times
\cong
(\mathbf F_q,+)\rtimes\mathbf F_q^\times
\]
where \(a\) acts on the additive factor by multiplication by \(a^{-1}\).

Since inversion
\[
a\longmapsto a^{-1}
\]
is an automorphism of the cyclic group
\[
\mathbf F_q^\times,
\]
reparameterizing the complement turns this inverse-scalar action into the usual scalar action. Therefore
\[
R_q^\times
\cong
\operatorname{AGL}_1(\mathbf F_q).
\]

The case
\[
q=3
\]
is also realizable because
\[
\operatorname{AGL}_1(\mathbf F_3)
\cong
S_3
\cong
\operatorname{GL}_2(\mathbf F_2)
=
M_2(\mathbf F_2)^\times.
\]

It remains to exclude odd
\[
q>3.
\]
Put
\[
G=\operatorname{AGL}_1(\mathbf F_q)
\]
and let
\[
K=(\mathbf F_q,+)
\]
be its translation subgroup.

The center of \(G\) is trivial. Indeed, any element centralizing every translation must have scalar part \(1\), so it lies in \(K\); a translation fixed by every nonzero scalar is zero because
\[
|\mathbf F_q^\times|>1.
\]

Suppose
\[
R^\times\cong G
\]
for a finite ring \(R\). The units of the characteristic subring lie in
\[
Z(R^\times)=1.
\]
For a nonzero finite ring this forces
\[
\operatorname{char}R=2.
\]

Let
\[
J=J(R)
\]
be the Jacobson radical. Since \(R\) has characteristic \(2\), the normal subgroup
\[
1+J
\]
has \(2\)-power order.

We claim that \(G\) has no nontrivial normal \(2\)-subgroup. If \(N\triangleleft G\) is a \(2\)-group, then, because \(K\) has odd order,
\[
N\cap K=1.
\]
Both \(N\) and \(K\) are normal, so
\[
[N,K]\le N\cap K=1.
\]
Thus \(N\) centralizes \(K\). But
\[
C_G(K)=K,
\]
so
\[
N\le K,
\]
and therefore \(N=1\).

Hence
\[
1+J=1,
\]
so
\[
J=0.
\]
The finite ring \(R\) is semisimple. By Artin--Wedderburn and Wedderburn's little theorem,
\[
R
\cong
\prod_i M_{n_i}(\mathbf F_{2^{e_i}}).
\]
Therefore
\[
G
\cong
R^\times
\cong
\prod_i
\operatorname{GL}_{n_i}(\mathbf F_{2^{e_i}}).
\]

The center of
\[
\operatorname{GL}_{n_i}(\mathbf F_{2^{e_i}})
\]
contains the scalar subgroup of order
\[
2^{e_i}-1.
\]
Since \(G\) has trivial center, every nontrivial unit-group factor must have
\[
e_i=1.
\]
Consequently,
\[
G
\cong
\prod_i\operatorname{GL}_{n_i}(\mathbf F_2),
\]
after discarding factors
\[
M_1(\mathbf F_2)
\]
whose unit group is trivial.

Now \(G\) is directly indecomposable. To see this, note first that \(K\) is a minimal normal subgroup: the complement
\[
\mathbf F_q^\times
\]
acts transitively on
\[
K\setminus\{0\}.
\]
If
\[
G=X\times Y
\]
with \(X,Y\triangleleft G\), then
\[
[K,X]\le K\cap X,
\qquad
[K,Y]\le K\cap Y.
\]
Minimality of \(K\) shows that if neither intersection equals \(K\), then both are trivial, forcing all of \(G\) to centralize \(K\), which is impossible. Thus, after exchanging \(X,Y\),
\[
K\le X.
\]
Then \(Y\) centralizes \(K\), so
\[
Y\le C_G(K)=K\le X.
\]
Since
\[
X\cap Y=1,
\]
we get \(Y=1\).

It follows that
\[
G\cong\operatorname{GL}_n(\mathbf F_2)
\]
for a single
\[
n\ge2.
\]
For
\[
n\ge3,
\]
the group
\[
\operatorname{GL}_n(\mathbf F_2)
=
\operatorname{PSL}_n(\mathbf F_2)
\]
is simple, whereas \(G\) has the proper nontrivial normal subgroup \(K\). Hence
\[
n=2.
\]
Therefore
\[
G\cong\operatorname{GL}_2(\mathbf F_2)\cong S_3,
\]
so
\[
|G|=6.
\]
Since
\[
|G|=q(q-1),
\]
we obtain
\[
q=3,
\]
contrary to \(q>3\).

This proves the classification.

## Verification

The included checker constructs the twisted dual-number rings directly for
\[
q=2,4,8,16.
\]
The nonprime fields use explicit irreducible binary polynomials.

For every test field, the checker:

- verifies the displayed twisted multiplication;
- checks an explicit inverse for every element with nonzero constant term;
- confirms that precisely \(q(q-1)\) elements are units;
- constructs the explicit bijection from
  \[
  \operatorname{AGL}_1(\mathbf F_q)
  \]
  to the unit group;
- verifies the homomorphism identity for every ordered pair of affine transformations.

It also checks the inverse-scalar conjugation action
\[
a(1+b\varepsilon)a^{-1}
=
1+ba^{-1}\varepsilon.
\]

The checker returns `VERIFY_OK`.

Finite computation is not used to prove the classification.

## Relationship to prior work

Lockridge and Terkel study Fuchs' realizability problem for linear groups. Their affine section explicitly restricts to
\[
\operatorname{AGL}_1(\mathbb Z/n\mathbb Z)
=
\operatorname{Hol}(C_n),
\]
where the additive group is cyclic, and gives a complete finite-ring classification in that setting. Their introduction also points out the distinct example
\[
\operatorname{AGL}_1(\mathbf F_4)\cong A_4
\]
while noting that
\[
\operatorname{Hol}((\mathbf F_4,+))\cong S_4.
\]
The inspected full text does not classify
\[
\operatorname{AGL}_1(\mathbf F_q)
\]
over arbitrary finite fields.

Blunck, Havlicek, and Zanella study the twisted dual-number ring
\[
K(\varepsilon;\sigma).
\]
They prove that its unit group is a semidirect product of
\[
K^\times
\]
with
\[
1+K\varepsilon.
\]
Taking
\[
K=\mathbf F_{2^f}
\]
and
\[
\sigma(a)=a^2
\]
supplies the positive construction used here. Their work is geometric and does not formulate or classify the associated groups in Fuchs' realizability problem.

Davis and Occhipinti prove that
\[
A_4
\]
is realizable, which covers the isolated case
\[
\operatorname{AGL}_1(\mathbf F_4).
\]
The theorem above places that example inside the full even-field family and supplies the complementary odd-field obstruction.

Targeted searches using affine-group, unit-group, finite-field, twisted-dual-number, and Fuchs-problem formulations did not locate the displayed all-\(q\) classification.

## Limitations

The theorem concerns degree-one affine groups. Higher-degree affine groups have noncyclic linear parts and require different normal-subgroup and semisimple-factor analysis.

Only finite realizing rings are classified. Characteristic-zero realizability is not addressed.

The twisted dual-number construction itself is prior ring theory; the new claim is the identification of the complete even-field family together with the proof that \(q=3\) is the only odd-field exception.

An equivalent classification may exist in older unit-group literature under a different description of the affine Frobenius groups.

Failed searches do not prove novelty.

## References

1. K. Lockridge and J. Terkel, “Fuchs' problem for linear groups,” arXiv:2401.11583v1, first public version 21 January 2024; *Communications in Algebra* 52 (2024), 2892–2902, DOI 10.1080/00927872.2024.2310166. Primary MSC 2020: 16U60, 20G40.
2. A. Blunck, H. Havlicek, and C. Zanella, “Divisible designs from twisted dual numbers,” *Designs, Codes and Cryptography* 47 (2008), 11–20, DOI 10.1007/s10623-007-9043-z.
3. C. Davis and T. Occhipinti, “Which alternating and symmetric groups are unit groups?”, *Journal of Algebra and Its Applications* 13 (2014), article 1350114, DOI 10.1142/S0219498813501144.
