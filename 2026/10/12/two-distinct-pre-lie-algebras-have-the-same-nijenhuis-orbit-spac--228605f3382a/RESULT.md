# Two distinct pre-Lie algebras have the same Nijenhuis orbit space

## Finding

Let \(k\) be any field. Consider the two nonisomorphic two-dimensional pre-Lie algebras
\[
A_2:\quad
e_1\cdot e_1=e_1,\qquad
e_1\cdot e_2=e_2\cdot e_1=e_2,
\]
and
\[
A_3:\quad
e_1\cdot e_1=e_1,
\]
with all omitted products zero.

For either algebra, the Nijenhuis operators are exactly
\[
\boxed{
N_{a,b,d}(e_1)=a e_1+b e_2,\qquad
N_{a,b,d}(e_2)=d e_2,\qquad
b(a-d)=0.
}
\]

The automorphism group is the same for both:
\[
\boxed{
\operatorname{Aut}(A_i)
=
\{\phi_s:\phi_s(e_1)=e_1,\ \phi_s(e_2)=s e_2,\ s\in k^\times\}.
}
\]
Conjugation satisfies
\[
\phi_sN_{a,b,d}\phi_s^{-1}=N_{a,sb,d}.
\]

Consequently every orbit contains exactly one representative of one of the forms
\[
\boxed{
D_{a,d}:
e_1\mapsto a e_1,\qquad
e_2\mapsto d e_2,
\qquad
(a,d)\in k^2,
}
\]
or
\[
\boxed{
J_a:
e_1\mapsto a e_1+e_2,\qquad
e_2\mapsto a e_2,
\qquad
a\in k.
}
\]

Thus the automorphism-orbit sets for the nonisomorphic algebras \(A_2\) and \(A_3\) are both canonically parameterized by
\[
\boxed{k^2\sqcup k.}
\]

Over a finite field \(\mathbf F_q\), each algebra has
\[
\boxed{2q^2-q}
\]
Nijenhuis operators and
\[
\boxed{q^2+q}
\]
automorphism-conjugacy classes. The \(q^2\) diagonal classes are singleton orbits. The \(q\) classes represented by \(J_a\) have orbit size \(q-1\).

There are exactly
\[
\boxed{q}
\]
square-zero Nijenhuis operators, forming exactly two automorphism orbits: the zero operator and the unique nonzero square-zero orbit represented by
\[
J_0.
\]
There are exactly
\[
\boxed{4}
\]
idempotent Nijenhuis operators, namely
\[
D_{0,0},\quad D_{1,0},\quad D_{0,1},\quad D_{1,1}.
\]

The coincidence is structurally nontrivial: \(A_2\) is unital, whereas \(A_3\) has no identity, yet their entire Nijenhuis orbit stratifications agree.

## Assumptions and scope

The theorem holds over every field, including characteristics \(2\) and \(3\).

The term “orbit” means conjugacy by the pre-Lie algebra automorphism group.

The source classifies Nijenhuis operators over \(\mathbf C\). The proof below rederives the two relevant families directly and therefore establishes the same classification over arbitrary fields before taking automorphism orbits.

The statement concerns \(A_2\) and \(A_3\) only. No claim is made that the remaining two-dimensional pre-Lie algebras have the same orbit space.

## Proof

Write a general linear map as
\[
N(e_1)=a e_1+b e_2,\qquad
N(e_2)=c e_1+d e_2.
\]

For a pre-Lie algebra, the Nijenhuis identity is
\[
N(x)\cdot N(y)
=
N\bigl(N(x)\cdot y+x\cdot N(y)-N(x\cdot y)\bigr)
\]
for all \(x,y\).

For \(A_2\), evaluation on the four ordered basis pairs reduces the identity to
\[
bc=0,\qquad
b(a-d)=0,\qquad
c^2=0.
\]
For \(A_3\), the same computation gives the same vanishing conditions, up to irrelevant signs:
\[
bc=0,\qquad
b(a-d)=0,\qquad
c^2=0.
\]
Because \(k\) is a field,
\[
c^2=0
\quad\Longrightarrow\quad
c=0.
\]
Hence in both algebras
\[
N(e_1)=a e_1+b e_2,\qquad
N(e_2)=d e_2,\qquad
b(a-d)=0.
\]

Now determine the automorphisms.

For \(A_2\), \(e_1\) is the identity, so every algebra automorphism fixes \(e_1\). The square-zero radical is \(k e_2\), so
\[
e_2\mapsto s e_2
\]
with \(s\ne0\).

For \(A_3\), let
\[
\phi(e_1)=u e_1+v e_2,\qquad
\phi(e_2)=r e_1+s e_2.
\]
The relation
\[
\phi(e_1)^2=\phi(e_1)
\]
forces
\[
u=1,\qquad v=0
\]
for an invertible \(\phi\). The relation
\[
\phi(e_1)\phi(e_2)=0
\]
then forces
\[
r=0.
\]
Thus again
\[
\phi=\phi_s,\qquad
\phi_s(e_1)=e_1,\quad
\phi_s(e_2)=s e_2,\quad s\in k^\times.
\]

A direct conjugation gives
\[
\phi_sN_{a,b,d}\phi_s^{-1}=N_{a,sb,d}.
\]

If
\[
b=0,
\]
the orbit is the singleton \(D_{a,d}\).

If
\[
b\ne0,
\]
the Nijenhuis condition gives
\[
d=a.
\]
Taking
\[
s=b^{-1}
\]
normalizes the coefficient of \(e_2\) in \(N(e_1)\) to \(1\), yielding \(J_a\). The parameter \(a\) is unchanged by conjugation, so distinct \(J_a\) are not conjugate.

This proves the arbitrary-field orbit classification.

Over \(\mathbf F_q\), there are \(q^2\) diagonal operators. The shear stratum has \(q\) choices of \(a\) and \(q-1\) choices of nonzero \(b\), hence
\[
q(q-1)
\]
operators. Therefore the total number is
\[
q^2+q(q-1)=2q^2-q.
\]

Each diagonal operator is fixed by all \(q-1\) automorphisms. Each shear operator has trivial stabilizer, so every shear orbit has size \(q-1\). Therefore the orbit count is
\[
q^2+\frac{q(q-1)}{q-1}=q^2+q.
\]

For square-zero operators, the diagonal stratum contributes only \(D_{0,0}\). In the shear stratum,
\[
N^2=0
\]
forces \(a=0\), while any nonzero \(b\) is allowed. Thus there are
\[
1+(q-1)=q
\]
square-zero operators in two orbits.

For idempotence, a diagonal operator is idempotent exactly when
\[
a,d\in\{0,1\},
\]
giving four operators. A shear operator has the form
\[
aI+bE,\qquad E^2=0,\quad b\ne0.
\]
The condition
\[
(aI+bE)^2=aI+bE
\]
requires simultaneously
\[
a^2=a,\qquad
(2a-1)b=0.
\]
No field element satisfies both with \(b\ne0\), so there are no idempotents in the shear stratum.

## Verification

The included checker exhaustively treats
\[
q\in\{2,3,5,7\}.
\]

For both \(A_2\) and \(A_3\), it enumerates every \(2\times2\) linear map and verifies directly that the Nijenhuis identity is equivalent to
\[
c=0,\qquad b(a-d)=0.
\]

It independently enumerates every invertible linear map preserving the algebra product and verifies
\[
\operatorname{Aut}(A_i)
=
\{\operatorname{diag}(1,s):s\in\mathbf F_q^\times\}.
\]

It then constructs all automorphism-conjugacy orbits and checks:
\[
|\operatorname{Nij}(A_i)|=2q^2-q,
\qquad
|\operatorname{Nij}(A_i)/\operatorname{Aut}(A_i)|=q^2+q.
\]

For \(q=5\), for example, each algebra has
\[
45
\]
Nijenhuis operators and
\[
30
\]
orbits: \(25\) singleton diagonal orbits and \(5\) shear orbits of size \(4\).

The checker also verifies the square-zero and idempotent counts and returns `VERIFY_OK`.

Finite enumeration is not used to prove the arbitrary-field theorem.

## Relationship to prior work

Gao, Kang, Lü, and collaborators classify all Nijenhuis operators on the two-dimensional complex pre-Lie algebras. For the algebras denoted \(A_2\) and \(A_3\), their theorem gives exactly two parametric families: diagonal operators and repeated-eigenvalue triangular operators with nonzero off-diagonal parameter.

The current full version explicitly states that a complete orbit analysis under \(\operatorname{Aut}(A)\) is beyond its scope. It illustrates the reduction only for \(A_5\), where a nonzero parameter can be normalized by automorphism conjugation, and says that similar reductions can be applied to other families.

The result here carries out that missing orbit analysis simultaneously for \(A_2\) and \(A_3\), extends the classification from \(\mathbf C\) to arbitrary fields by direct verification of the Nijenhuis equations, and gives exact finite-field orbit and stabilizer counts.

Targeted semantic and literature searches under \(A_2\), \(A_3\), dual-number, automorphism-orbit, conjugacy, and Nijenhuis-normal-form formulations did not locate this two-algebra orbit classification. The closest database result concerns averaging operators on the different nilpotent algebra \(A_5\), not Nijenhuis operators on \(A_2\) or \(A_3\).

## Limitations

The theorem does not provide the full orbit classification for all two-dimensional pre-Lie algebras.

The orbit calculation is elementary once the source's parametric families are known; its value is the exact completion of an explicitly deferred conjugacy problem for two natural nonisomorphic algebras, together with the characteristic-free and finite-field forms.

A later or unindexed source may contain equivalent normal forms.

Failed searches do not prove novelty.

## References

1. X. Gao, C. Kang, J. Lü, and collaborators, “Nijenhuis operators on low dimensional pre-Lie algebras and solutions of CYBE,” arXiv:2308.12121v1, first public version 23 August 2023; current arXiv version titled “Nijenhuis operators on 2D pre-Lie algebras and 3D associative algebras.” Current version MSC 2020: 17A36, 17B60, 16T25, 17B81.
2. Q. Wang, C. Bai, J. Liu, and Y. Sheng, “Nijenhuis operators on pre-Lie algebras,” arXiv:1710.03749v1, first public version 9 October 2017.
