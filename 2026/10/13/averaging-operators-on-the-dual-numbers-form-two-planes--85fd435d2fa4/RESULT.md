# Averaging operators on the dual numbers form two planes

## Finding

Let \(K\) be any field and let
\[
A_K=K[\varepsilon]/(\varepsilon^2)
\]
be the algebra of dual numbers.

An averaging operator on \(A_K\) is a linear map \(T:A_K\to A_K\) satisfying
\[
T(x)T(y)=T(T(x)y)=T(xT(y))
\]
for all \(x,y\in A_K\).

Write
\[
T(1)=a+b\varepsilon,
\qquad
T(\varepsilon)=c+d\varepsilon.
\]
With the basis \(\{1,\varepsilon\}\), so that matrix columns record \(T(1)\) and \(T(\varepsilon)\), every averaging operator is exactly one of the matrices in
\[
\boxed{
\left\{
\begin{pmatrix}
a&c\\
0&0
\end{pmatrix}
:a,c\in K
\right\}
\ \cup\
\left\{
\begin{pmatrix}
a&0\\
b&a
\end{pmatrix}
:a,b\in K
\right\}.
}
\]

Thus the averaging-operator variety is the union of two affine planes meeting only at the zero operator.

Every algebra automorphism of \(A_K\) has the form
\[
\phi_s(1)=1,
\qquad
\phi_s(\varepsilon)=s\varepsilon,
\qquad
s\in K^\times.
\]
Conjugation acts on the two planes by
\[
\phi_s
\begin{pmatrix}
a&c\\
0&0
\end{pmatrix}
\phi_s^{-1}
=
\begin{pmatrix}
a&c/s\\
0&0
\end{pmatrix}
\]
and
\[
\phi_s
\begin{pmatrix}
a&0\\
b&a
\end{pmatrix}
\phi_s^{-1}
=
\begin{pmatrix}
a&0\\
sb&a
\end{pmatrix}.
\]

Therefore every automorphism orbit has a unique representative among the four one-parameter families
\[
\boxed{
E_a=
\begin{pmatrix}
a&0\\
0&0
\end{pmatrix},
\qquad
F_a=
\begin{pmatrix}
a&1\\
0&0
\end{pmatrix},
}
\]
\[
\boxed{
S_a=aI_2,
\qquad
J_a=
\begin{pmatrix}
a&0\\
1&a
\end{pmatrix},
\qquad
a\in K,
}
\]
with exactly one duplication:
\[
E_0=S_0=0.
\]

Over a finite field \(\mathbf F_q\),
\[
\boxed{
|\operatorname{Avg}(A_{\mathbf F_q})|=2q^2-1
}
\]
and
\[
\boxed{
|\operatorname{Avg}(A_{\mathbf F_q})/\operatorname{Aut}(A_{\mathbf F_q})|=4q-1.
}
\]

Exactly
\[
2q-1
\]
of these classes are singletons, namely the \(E_a\) and \(S_a\) classes with the zero class counted once. The remaining
\[
2q
\]
classes, represented by the \(F_a\) and \(J_a\), each have size
\[
q-1.
\]

## Assumptions and scope

The result is valid over an arbitrary field. No algebraic-closure or characteristic restriction is needed.

The operator identity is the ordinary associative specialization of the relative averaging identity used for Hom-associative algebras when the twisting map is the identity and the bimodule is the regular adjoint bimodule.

The finite-field statement concerns conjugacy of operators by algebra automorphisms of the fixed dual-number algebra. It does not classify arbitrary two-dimensional averaging algebras up to simultaneous change of both multiplication and operator.

The dual numbers are chosen because they are the smallest nonsemisimple unital local algebra and the first-order infinitesimal algebra \(K[\varepsilon]/(\varepsilon^2)\).

## Proof

Let
\[
x=x_0+x_1\varepsilon,
\qquad
y=y_0+y_1\varepsilon.
\]
Multiplication in \(A_K\) is
\[
(x_0+x_1\varepsilon)(y_0+y_1\varepsilon)
=
x_0y_0+(x_0y_1+x_1y_0)\varepsilon.
\]

Write
\[
T(1)=a+b\varepsilon,
\qquad
T(\varepsilon)=c+d\varepsilon.
\]

It is enough to impose the averaging identity on the four ordered pairs of basis vectors.

From the constant and \(\varepsilon\)-coefficients of
\[
T(1)T(1)=T(T(1))
\]
and
\[
T(1)T(\varepsilon)=T(T(1)\varepsilon),
\]
one obtains the four scalar equations
\[
bc=0,
\qquad
b(a-d)=0,
\qquad
cd=0,
\qquad
d(a-d)=0.
\]

The right averaging identity gives the same equations because \(A_K\) is commutative.

Now solve the system.

If
\[
d\ne0,
\]
then
\[
c=0
\]
from \(cd=0\), and
\[
a=d
\]
from \(d(a-d)=0\). Thus
\[
T=
\begin{pmatrix}
a&0\\
b&a
\end{pmatrix}.
\]

If
\[
d=0
\]
and \(b\ne0\), then \(b(a-d)=0\) and \(bc=0\) give
\[
a=c=0,
\]
which is again contained in the same lower-triangular plane.

Finally, if
\[
d=b=0,
\]
then \(a\) and \(c\) are arbitrary, giving
\[
T=
\begin{pmatrix}
a&c\\
0&0
\end{pmatrix}.
\]

Hence the complete solution set is exactly the union of the two displayed affine planes. Their intersection is the zero matrix.

For automorphisms, every algebra automorphism fixes the identity. The nilradical is the unique one-dimensional ideal
\[
K\varepsilon,
\]
so
\[
\phi(\varepsilon)=s\varepsilon
\]
with \(s\ne0\), and every such choice gives an automorphism. Thus
\[
\operatorname{Aut}(A_K)\cong K^\times.
\]

Conjugating the first plane rescales only \(c\) by \(s^{-1}\). Therefore for each fixed \(a\), the locus \(c=0\) is one orbit and all \(c\ne0\) form one orbit.

Conjugating the second plane rescales only \(b\) by \(s\). Therefore for each fixed \(a\), the locus \(b=0\) is one orbit and all \(b\ne0\) form one orbit.

The two planes meet only at zero, so there are no additional identifications. This proves the four normal-form families and their uniqueness.

Over \(\mathbf F_q\), each plane has \(q^2\) points and their intersection has one point. Hence
\[
|\operatorname{Avg}(A_{\mathbf F_q})|
=
q^2+q^2-1
=
2q^2-1.
\]

The zero-parameter loci \(c=0\) and \(b=0\) give \(q+q-1=2q-1\) singleton orbits. The nonzero loci contribute \(q+q=2q\) further orbits, each of size \(q-1\). Thus the number of orbits is
\[
(2q-1)+2q=4q-1.
\]

## Verification

The included checker `artifacts/verify.py` reconstructs the averaging equations symbolically from the multiplication
\[
\varepsilon^2=0.
\]

It confirms that the complete polynomial system reduces to
\[
bc=0,
\qquad
b(a-d)=0,
\qquad
cd=0,
\qquad
d(a-d)=0.
\]

It verifies directly that both affine-plane families satisfy the full two-sided averaging identity.

It also exhaustively checks the finite fields
\[
\mathbf F_2,\quad
\mathbf F_3,\quad
\mathbf F_5,\quad
\mathbf F_7.
\]
For each field it enumerates all linear maps, independently tests the averaging identity, enumerates all algebra automorphisms, and computes every conjugacy orbit.

The output agrees with
\[
2q^2-1
\]
operators and
\[
4q-1
\]
orbits in every tested field.

The checker returns `VERIFY_OK`.

Finite enumeration is not used to prove the arbitrary-field classification.

## Relationship to prior work

Braiek, Chtioui, Mabrouk, and Elhamdadi introduce relative averaging operators for Hom-associative algebras with representations. Their Definition 3.1 gives the left and right relative averaging identities, and they explicitly note that an ordinary averaging operator is a relative averaging operator on the adjoint bimodule. Their Theorem 3.9 shows that such an operator induces a Hom-associative dialgebra structure.

Earlier algebraic work of Cao studies averaging operators abstractly, including free averaging algebras and Lie structures induced by averaging operators. The inspected full text contains a general finite-dimensional section about induced Lie brackets and a two-dimensional real example on \(\mathbb C\), but no classification of averaging operators on the dual-number algebra.

Focused searches for dual numbers, \(K[\varepsilon]/(\varepsilon^2)\), two-dimensional associative algebras, and averaging-operator classifications did not locate the two-plane solution variety, the four normal-form families, or the finite-field count \(4q-1\).

The closest database result found during overlap checking concerns automorphism normal forms for averaging operators on a different two-dimensional nilpotent pre-Lie algebra. Its multiplication and averaging equation are different and it does not imply the present associative dual-number classification.

## Limitations

The theorem classifies averaging operators only on the fixed dual-number algebra. It does not classify averaging operators simultaneously over all two-dimensional associative algebras.

The quotient is by algebra automorphisms of \(A_K\); coarser equivalence notions that also alter the underlying multiplication are outside the claim.

A specialized or unindexed source may already contain the same concrete classification.

Failed searches do not prove novelty.

## References

1. S. Braiek, T. Chtioui, S. Mabrouk, and M. Elhamdadi, “Hom-associative algebras, Admissibility and Relative averaging operators,” arXiv:2311.08407v1, dated 20 August 2023. MSC 2020: 17B61, 17B60, 17C10, 17A32.
2. W. Cao, “An Algebraic Study of Averaging Operators,” arXiv:1401.7389v1, 29 January 2014.
