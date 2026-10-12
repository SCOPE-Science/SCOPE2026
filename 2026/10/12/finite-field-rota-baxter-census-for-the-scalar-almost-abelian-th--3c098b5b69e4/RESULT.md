# Finite-field Rota–Baxter census for the scalar almost-abelian three-dimensional Lie algebra

## Finding

Let \(K\) be any field, let \(V\) be a two-dimensional \(K\)-vector space, and let
\[
L=Kt\ltimes V
\]
be the Lie algebra defined by
\[
[t,v]=v
\qquad(v\in V),
\qquad
[V,V]=0.
\]

Every linear map \(R:L\to L\) can be written uniquely as
\[
R(t)=at+u,
\qquad
R(v)=f(v)t+Av,
\]
with
\[
a\in K,\qquad
u\in V,\qquad
f\in V^\ast,\qquad
A\in\operatorname{End}(V).
\]

Then \(R\) is a weight-zero Rota–Baxter operator,
\[
[R(x),R(y)]
=
R\!\left([R(x),y]+[x,R(y)]\right)
\qquad(x,y\in L),
\]
if and only if
\[
\boxed{
fA=-af,
\qquad
A^2=-u\otimes f.
}
\]

For every prime power \(q\), the corresponding algebra \(L_q\) over \(\mathbf F_q\) has exactly
\[
\boxed{
q^5+q^4-q^2
}
\]
weight-zero Rota–Baxter operators.

Their exact rank distribution is
\[
\boxed{
\#\{R:\operatorname{rank}R=0\}=1,
}
\]
\[
\boxed{
\#\{R:\operatorname{rank}R=1\}
=
q^4+2q^3-q^2-q-1,
}
\]
\[
\boxed{
\#\{R:\operatorname{rank}R=2\}
=
q(q^2-1)^2,
}
\]
and
\[
\boxed{
\#\{R:\operatorname{rank}R=3\}=0.
}
\]

Thus this nonabelian three-dimensional Lie algebra has no invertible weight-zero Rota–Baxter operator over any field.

The same count over every extension field is
\[
|\operatorname{RB}_0(L_q)(\mathbf F_{q^m})|
=
q^{5m}+q^{4m}-q^{2m}.
\]
Consequently its Rota–Baxter operator variety has Hasse–Weil zeta function
\[
\boxed{
Z(T)
=
\frac{1-q^2T}{(1-q^5T)(1-q^4T)}.
}
\]

## Assumptions and scope

The 2020 classification source studies the family
\[
[e_1,e_2]=e_1,
\qquad
[e_1,e_3]=0,
\qquad
[e_2,e_3]=ke_3.
\]
Its exceptional case \(k=-1\) is isomorphic over every field to the algebra above: take
\[
t=-e_2,
\qquad
V=\operatorname{span}\{e_1,e_3\}.
\]
Then
\[
[t,e_1]=e_1,
\qquad
[t,e_3]=e_3.
\]

The theorem is valid in every characteristic, including characteristic \(2\). It counts all linear weight-zero Rota–Baxter operators; no automorphism quotient is taken.

The source works over \(\mathbb C\). The finite-field theorem is obtained directly from the defining identity, not by counting the source's normalized complex parameter families.

## Proof

Write elements of \(L\) as pairs
\[
(s,x)\in K\oplus V.
\]
The bracket is
\[
[(s,x),(r,y)]
=
(0,sy-rx).
\]

Write
\[
R(s,x)
=
(as+f(x),\,su+Ax).
\]

First apply the Rota–Baxter identity to \(t=(1,0)\) and \(v=(0,x)\). We have
\[
R(t)=(a,u),
\qquad
R(v)=(f(x),Ax).
\]
The left side is
\[
[R(t),R(v)]
=
(0,aAx-f(x)u).
\]
The expression inside the outer \(R\) on the right is
\[
[R(t),v]+[t,R(v)]
=
(0,(aI+A)x).
\]
Hence the \(K t\)-component gives
\[
f(A+aI)=0,
\]
that is,
\[
fA=-af.
\]
The \(V\)-component gives
\[
aAx-f(x)u
=
A(aI+A)x,
\]
so
\[
A^2=-u\otimes f.
\]

Conversely, these two equations make the identity hold for \((t,v)\). For \(v,w\in V\),
\[
[R(v),R(w)]
=
f(v)Aw-f(w)Av,
\]
while
\[
[R(v),w]+[v,R(w)]
=
f(v)w-f(w)v.
\]
Applying \(R\) gives the same \(V\)-component, and the \(t\)-component is
\[
f(v)f(w)-f(w)f(v)=0.
\]
The pair \((t,t)\) is automatic. Bilinearity proves the criterion.

Now let \(K=\mathbf F_q\).

### The stratum \(f=0\)

The equations reduce to
\[
A^2=0,
\]
while \(a\) and \(u\) are arbitrary.

A \(2\times2\) square-zero matrix is either zero or a nonzero rank-one nilpotent. For a nonzero such matrix,
\[
\operatorname{im}A=\ker A
\]
is a line in \(V\). There are \(q+1\) choices of this line and \(q-1\) nonzero maps
\[
V/\ker A\longrightarrow\operatorname{im}A.
\]
Hence there are
\[
1+(q+1)(q-1)=q^2
\]
square-zero matrices.

This stratum therefore contains
\[
q\cdot q^2\cdot q^2=q^5
\]
operators.

For the rank count, when \(A=0\) there is one zero operator and
\[
q^3-1
\]
rank-one operators.

Fix a nonzero square-zero \(A\). If \(a\ne0\), the first column has a nonzero \(t\)-component and is independent of \(\operatorname{im}A\), so the operator has rank \(2\). If \(a=0\), the rank is \(1\) exactly when
\[
u\in\operatorname{im}A,
\]
which gives \(q\) choices of \(u\). Thus each nonzero \(A\) contributes
\[
q
\]
rank-one operators and
\[
q(q^2-1)
\]
rank-two operators.

The \(f=0\) stratum therefore contributes
\[
1
\]
operator of rank \(0\),
\[
2q^3-q-1
\]
of rank \(1\), and
\[
q(q^2-1)^2
\]
of rank \(2\).

### The stratum \(f\ne0\)

All nonzero covectors are equivalent under a change of basis of \(V\). Choose coordinates in which
\[
f=(1,0).
\]
The equation
\[
fA=-af
\]
forces
\[
A=
\begin{pmatrix}
-a&0\\
r&s
\end{pmatrix}.
\]
Then
\[
A^2
=
\begin{pmatrix}
a^2&0\\
r(s-a)&s^2
\end{pmatrix}.
\]
Comparing this with
\[
-u\otimes f
\]
gives
\[
s=0,
\qquad
u=
\begin{pmatrix}
-a^2\\
ar
\end{pmatrix}.
\]
Thus, for each nonzero \(f\), the parameters
\[
a,r\in\mathbf F_q
\]
are free and determine \(A\) and \(u\) uniquely.

There are therefore
\[
(q^2-1)q^2=q^4-q^2
\]
operators in this stratum.

In the chosen basis their matrix is
\[
\begin{pmatrix}
a&1&0\\
-a^2&-a&0\\
ar&r&0
\end{pmatrix}.
\]
Its first column is \(a\) times its second column, and its second column is nonzero. Hence every operator in this stratum has rank \(1\).

Adding the two strata gives
\[
1,
\qquad
q^4+2q^3-q^2-q-1,
\qquad
q(q^2-1)^2,
\qquad
0
\]
in ranks \(0,1,2,3\), respectively, and their sum is
\[
q^5+q^4-q^2.
\]

Replacing \(q\) by \(q^m\) gives
\[
q^{5m}+q^{4m}-q^{2m}
\]
points over \(\mathbf F_{q^m}\). Therefore
\[
\begin{aligned}
Z(T)
&=
\exp\!\left(
\sum_{m\ge1}
\frac{(q^{5m}+q^{4m}-q^{2m})T^m}{m}
\right)\\
&=
\frac{1-q^2T}{(1-q^5T)(1-q^4T)}.
\end{aligned}
\]

## Verification

The included program `artifacts/verify.py` reconstructs the Rota–Baxter defect directly from
\[
[t,v]=v.
\]

It symbolically verifies that the complete basis-pair system is exactly equivalent to
\[
fA=-af,
\qquad
A^2=-u\otimes f.
\]

It then exhaustively tests all
\[
2^9=512
\]
linear endomorphisms over \(\mathbf F_2\) and all
\[
3^9=19683
\]
endomorphisms over \(\mathbf F_3\).

The resulting rank distributions are
\[
(1,25,18,0)
\]
over \(\mathbf F_2\), and
\[
(1,122,192,0)
\]
over \(\mathbf F_3\).
These agree with the closed formulas and give totals
\[
44
\]
and
\[
315.
\]

The checker also verifies the symbolic rank-count identities over several further integer values of \(q\). It returns `VERIFY_OK`.

The finite searches are replay checks; the arbitrary-field criterion and arbitrary-prime-power counts are proved above.

## Relationship to prior work

Cheng, Wu, and Wang complete the complex weight-zero Rota–Baxter classification for the three-dimensional Lie-algebra family
\[
[e_1,e_2]=e_1,\qquad
[e_1,e_3]=0,\qquad
[e_2,e_3]=ke_3.
\]
For the exceptional value
\[
k=-1,
\]
their Theorem 2.1 lists fifty normalized matrix families. Their reduction to equations (2.4)–(2.12) is consistent with the defining identity used here, but the paper works over \(\mathbb C\) and does not give a finite-field census or rank enumerator.

The preceding 2017 paper of Wu, Wang, and Cheng treats the distinct algebra denoted \(g_5\) in the later paper. The 2020 source explicitly identifies the present \(g_6\) family as the remaining case needed to complete the three-dimensional complex classification.

Focused searches for finite-field counts, the formula
\[
q^5+q^4-q^2,
\]
the block conditions
\[
fA=-af,\qquad A^2=-u\otimes f,
\]
and rank distributions for this scalar almost-abelian algebra did not locate a covering result.

## Limitations

The finite-field count and rank distribution are for the scalar almost-abelian three-dimensional algebra, equivalently the \(k=-1\) member of the source's \(g_6\) family.

The theorem does not count automorphism-conjugacy classes.

The Hasse–Weil zeta function records rational-point counts; it does not assert that the operator variety is isomorphic to a disjoint union of affine spaces.

A specialized or differently indexed source may contain an equivalent finite-field calculation. Failed searches do not prove novelty.

## References

1. Y. Cheng, L. Wu, and P. Wang, “Rota-Baxter Operators on 3-Dimensional Lie Algebras and Solutions of the Classical Yang-Baxter Equation,” *Communications in Mathematical Research* 35(1), 81–96, DOI `10.13447/j.1674-5647.2019.01.09`. The publisher records public publication on 18 March 2020.
2. L. Wu, M. Wang, and Y. Cheng, “Rota-Baxter Operators on 3-Dimensional Lie Algebras and the Classical R-Matrices,” *Advances in Mathematical Physics* 2017, Article 6128102, DOI `10.1155/2017/6128102`.
