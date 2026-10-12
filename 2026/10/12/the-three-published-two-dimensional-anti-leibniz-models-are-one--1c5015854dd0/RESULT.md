# The three published two-dimensional anti-Leibniz models are one algebra

## Finding

Let \(K\) be a field, and let \(C\) be the two-dimensional algebra with basis
\[
\{u,v\}
\]
and multiplication
\[
u^2=v,
\qquad
uv=vu=v^2=0.
\]

The three nontrivial two-dimensional anti-Leibniz models displayed in Theorem 2.3(2) of Braiek--Chtioui--Mabrouk are all isomorphic to \(C\).

The source lists
\[
A_2:\quad e_2^2=e_1
\]
and
\[
A_3:\quad e_1^2=e_2.
\]
These are isomorphic by interchanging the basis vectors.

Its parameter family \(A_1(a,b)\), with \(ab\ne0\), is given by
\[
e_1^2=-a e_1-\frac{a^2}{b}e_2,
\]
\[
e_1e_2=e_2e_1=b e_1+a e_2,
\]
and
\[
e_2^2=-\frac{b^2}{a}e_1-b e_2.
\]
Define
\[
f_1=e_1,
\qquad
f_2=-a e_1-\frac{a^2}{b}e_2=e_1^2.
\]
Then \((f_1,f_2)\) is a basis and
\[
f_1^2=f_2,
\qquad
f_1f_2=f_2f_1=f_2^2=0.
\]
Hence
\[
\boxed{A_1(a,b)\cong A_2\cong A_3\cong C.}
\]

Thus the published three-model list contains only one nontrivial isomorphism type.

A later anti-Leibniz bialgebra paper already merges the original \(A_2\) and \(A_3\) into one displayed model, but it still lists the \(A_1(a,b)\) family separately. The same basis change above identifies that remaining family with the first model as well.

The canonical model also has explicit symmetry and infinitesimal symmetry:
\[
\boxed{
\operatorname{Aut}(C)
=
\left\{
\begin{pmatrix}
s&0\\
t&s^2
\end{pmatrix}
:
s\in K^\times,\ t\in K
\right\}.
}
\]
Writing
\[
\phi_{s,\tau}(u)=s(u+\tau v),
\qquad
\phi_{s,\tau}(v)=s^2v,
\]
composition is
\[
\phi_{s,\tau}\phi_{r,\sigma}
=
\phi_{sr,\tau+s\sigma},
\]
so
\[
\operatorname{Aut}(C)\cong \mathbf G_a\rtimes\mathbf G_m.
\]

In characteristic zero,
\[
\boxed{
\operatorname{Der}(C)
=
\left\{
\begin{pmatrix}
r&0\\
w&2r
\end{pmatrix}
:
r,w\in K
\right\},
}
\]
and this is the two-dimensional affine Lie algebra.

## Assumptions and scope

The correction concerns the three displayed nontrivial models in Theorem 2.3(2). It does not require trusting the completeness of that theorem: the isomorphisms are verified directly from the displayed multiplication tables.

The source works in characteristic zero. The isomorphism \(A_1(a,b)\cong C\) itself only requires \(a\) and \(b\) to be nonzero.

The derivation-algebra identification is stated in characteristic zero so that the coefficient \(2\) has its ordinary meaning.

No claim is made here about higher-dimensional anti-Leibniz classifications.

## Proof

For \(A_2\) and \(A_3\), swapping the two basis vectors sends the unique nonzero square in one table to the unique nonzero square in the other.

Now consider \(A_1(a,b)\). Put
\[
v_0=b e_1+a e_2.
\]
The multiplication table rewrites as
\[
e_1^2=-\frac ab\,v_0,
\qquad
e_1e_2=v_0,
\qquad
e_2^2=-\frac ba\,v_0.
\]

A direct calculation gives
\[
e_1v_0
=
b e_1^2+a e_1e_2
=
-a v_0+a v_0
=
0,
\]
and similarly
\[
e_2v_0=0.
\]
Therefore \(v_0\) annihilates the entire algebra and
\[
v_0^2=0.
\]

Set
\[
f_1=e_1,
\qquad
f_2=-\frac ab\,v_0
=
-ae_1-\frac{a^2}{b}e_2.
\]
The change-of-basis determinant is
\[
-\frac{a^2}{b},
\]
which is nonzero. Hence \((f_1,f_2)\) is a basis. By construction,
\[
f_1^2=f_2,
\]
while the annihilator calculation gives
\[
f_1f_2=f_2f_1=f_2^2=0.
\]
Thus \(A_1(a,b)\cong C\).

For the automorphism group, write
\[
\phi(u)=p u+q v,
\qquad
\phi(v)=r u+s v.
\]
Since
\[
v=u^2,
\]
multiplicativity forces
\[
\phi(v)=\phi(u)^2=p^2v.
\]
Therefore
\[
r=0,\qquad s=p^2.
\]
Invertibility is equivalent to
\[
p\ne0.
\]
This gives the displayed automorphism group.

For derivations, write
\[
D(u)=r u+w v,
\qquad
D(v)=x u+y v.
\]
Using \(v=u^2\),
\[
D(v)
=
D(u)u+uD(u)
=
2r\,v.
\]
Hence
\[
x=0,\qquad y=2r.
\]
The remaining zero products impose no further conditions.

If
\[
H=
\begin{pmatrix}
1&0\\
0&2
\end{pmatrix},
\qquad
E=
\begin{pmatrix}
0&0\\
1&0
\end{pmatrix},
\]
then
\[
[H,E]=E.
\]
Thus the derivation Lie algebra is the standard two-dimensional affine Lie algebra.

## Verification

The included checker performs symbolic verification.

It rewrites the full \(A_1(a,b)\) multiplication table in the basis
\[
f_1=e_1,
\qquad
f_2=-a e_1-\frac{a^2}{b}e_2,
\]
and confirms exactly
\[
f_1^2=f_2,
\qquad
f_1f_2=f_2f_1=f_2^2=0.
\]

It verifies that the basis determinant is nonzero whenever \(ab\ne0\).

It also checks the general automorphism and derivation equations for the canonical algebra and verifies
\[
[H,E]=E.
\]

The checker returns `VERIFY_OK`.

## Relationship to prior work

Braiek, Chtioui, and Mabrouk introduce anti-Leibniz algebras and state that every two-dimensional example is isomorphic to one of three displayed models \(A_1,A_2,A_3\). The displayed \(A_1\) family carries two nonzero parameters, while \(A_2\) and \(A_3\) each have a single nonzero square.

A later paper by Hou and Cui recalls two displayed nontrivial two-dimensional forms: the square algebra \(e_1^2=e_2\) and the same parameter family that appeared as \(A_1\). Thus that later source already removes the obvious duplication between the original \(A_2\) and \(A_3\), but it still retains the parameter family as a separate form.

The basis change above shows that this remaining family is also the square algebra.

Focused searches for the exact parameter family, the two-dimensional anti-Leibniz classification, and explicit isomorphisms between the displayed forms did not locate this final collapse.

## Limitations

The result is a correction and normalization of the displayed two-dimensional models, not a new general classification theorem in higher dimension.

The original source does not explicitly say that the three displayed models are pairwise nonisomorphic, so the mathematically precise conclusion is that its displayed list is redundant. The later source does explicitly retain two forms, and those are likewise isomorphic.

An author note or unindexed correction may exist.

Failed searches do not prove novelty.

## References

1. S. Braiek, T. Chtioui, and S. Mabrouk, “Anti-Leibniz algebras: A non-commutative version of mock-Lie algebra,” arXiv:2409.17184v1, first public version 24 September 2024. MSC 2020: 16W10, 17A60, 17A01, 17A32, 17A36.
2. B. Hou and Z. Cui, “A bialgebra theory of anti-Leibniz algebras,” arXiv:2412.20028v1, first public version 28 December 2024.
