# Rota–Baxter moduli of \(J_4\) have a characteristic-two jump

## Finding

Let \(K\) be a field and let \(J_K\) be the two-dimensional Jordan algebra with basis \(\{e_1,e_2\}\) and multiplication
\[
e_1\circ e_1=2e_1,\qquad
e_1\circ e_2=e_2\circ e_1=e_2,\qquad
e_2\circ e_2=0.
\]
This is the integral model whose complex specialization is the algebra denoted \(J_4\) in the cited low-dimensional classification.

Write a linear map as
\[
R=
\begin{pmatrix}
a&b\\
c&d
\end{pmatrix},
\]
where the columns are the coordinates of \(R(e_1)\) and \(R(e_2)\).

If
\[
\operatorname{char}K\ne2,
\]
then \(R\) is a weight-zero Rota–Baxter operator exactly when
\[
\boxed{d=-a,\qquad a^2+bc=0.}
\]
Equivalently,
\[
\boxed{R^2=0.}
\]
Thus the Rota–Baxter variety is exactly the square-zero cone in \(M_2(K)\).

The full automorphism group is
\[
\boxed{
\operatorname{Aut}(J_K)=
\left\{
P_{t,s}=
\begin{pmatrix}
1&0\\
t&s
\end{pmatrix}:t\in K,\ s\in K^\times
\right\}.
}
\]
For \(\operatorname{char}K\ne2\), it has exactly three conjugacy orbits on the Rota–Baxter cone, represented by
\[
\boxed{
0,\qquad
U=\begin{pmatrix}0&1\\0&0\end{pmatrix},\qquad
L=\begin{pmatrix}0&0\\1&0\end{pmatrix}.
}
\]
The two nonzero classes are intrinsically distinct: \(L\) preserves the characteristic line \(K e_2\), while \(U\) does not.

Characteristic \(2\) changes the answer. In that case the complete Rota–Baxter equations are
\[
\boxed{b(a+d)=0,\qquad bc+d^2=0.}
\]
The conjugacy classes are exactly
\[
\boxed{
0,\qquad U,\qquad L,\qquad
D_a=\begin{pmatrix}a&0\\0&0\end{pmatrix}\ (a\in K^\times).
}
\]
Hence a one-parameter semisimple branch appears only in characteristic \(2\).

For every finite field \(\mathbf F_q\), the exact counts are
\[
\boxed{
|\operatorname{RB}_0(J_{\mathbf F_q})|=
\begin{cases}
q^2,&q\text{ odd},\\
2q^2-q,&q\text{ even},
\end{cases}
}
\]
and
\[
\boxed{
|\operatorname{RB}_0(J_{\mathbf F_q})/\operatorname{Aut}(J_{\mathbf F_q})|=
\begin{cases}
3,&q\text{ odd},\\
q+2,&q\text{ even}.
\end{cases}
}
\]
For odd \(q\), the orbit sizes are
\[
1,\qquad q-1,\qquad q(q-1).
\]
For even \(q\), they are
\[
1,\qquad q-1,\qquad q(q-1),
\]
together with \(q\) repeated \(q-1\) times.

## Assumptions and scope

The Rota–Baxter identity used here is the weight-zero Jordan identity
\[
R(x)\circ R(y)=R\bigl(R(x)\circ y+x\circ R(y)\bigr).
\]

The source works over \(\mathbb C\). The arbitrary-field equations, automorphism quotient, characteristic-two boundary, and finite-field counts are established directly here.

The multiplication above is a Jordan multiplication over every field. In characteristic \(2\), its square map vanishes, so its Jordan identity is immediate; outside characteristic \(2\), the identity can also be checked directly from the displayed multiplication.

The quotient considered here is conjugation by automorphisms of the fixed Jordan algebra. It is not a classification of all two-dimensional Jordan algebras together with operators.

## Proof

For basis vectors, direct substitution into the Rota–Baxter identity gives the scalar equations
\[
2(a^2+bc)=0,
\qquad
2c(a+d)=0,
\qquad
b(a+d)=0,
\qquad
bc+d^2=0.
\]
The remaining basis equations repeat these or vanish.

Suppose first that \(\operatorname{char}K\ne2\). Then
\[
a^2+bc=0,
\qquad
c(a+d)=0,
\qquad
b(a+d)=0,
\qquad
bc+d^2=0.
\]
If \(b=c=0\), the first and last equations force \(a=d=0\). Otherwise, at least one of \(b,c\) is nonzero and hence
\[
d=-a.
\]
The remaining equation is
\[
a^2+bc=0.
\]
Conversely these two equations visibly satisfy the full system. Moreover
\[
\begin{pmatrix}a&b\\c&-a\end{pmatrix}^2
=(a^2+bc)I_2,
\]
which proves the square-zero characterization.

Now compute the automorphisms. Write
\[
\phi(e_1)=p e_1+t e_2,
\qquad
\phi(e_2)=r e_1+s e_2.
\]
The relation \(e_1\circ e_2=e_2\), together with invertibility, forces
\[
r=0,\qquad p=1,\qquad s\ne0.
\]
The other products are then automatically preserved. This gives the displayed automorphism group in every characteristic.

For
\[
P_{t,s}=\begin{pmatrix}1&0\\t&s\end{pmatrix},
\]
direct conjugation of a general matrix gives
\[
P_{t,s}
\begin{pmatrix}a&b\\c&d\end{pmatrix}
P_{t,s}^{-1}
=
\begin{pmatrix}
a-bt/s&b/s\\
at-bt^2/s+cs-dt&bt/s+d
\end{pmatrix}.
\]

Assume again that \(\operatorname{char}K\ne2\). For a nonzero Rota–Baxter operator with \(b\ne0\), take
\[
s=b,\qquad t=a.
\]
The conjugate is \(U\). If \(b=0\), then \(a=0\); a nonzero operator has \(c\ne0\), and taking \(s=c^{-1}\) gives \(L\). Since conjugation sends \(b\) to \(b/s\), the conditions \(b=0\) and \(b\ne0\) cannot mix. Thus the three representatives are unique.

Now let \(\operatorname{char}K=2\). The basis equations reduce to
\[
b(a+d)=0,
\qquad
bc+d^2=0.
\]
If \(b\ne0\), then
\[
d=a,
\qquad
c=a^2/b.
\]
Taking \(s=b\) and \(t=a\) conjugates the operator to \(U\).

If \(b=0\), then \(d=0\). The remaining matrices are
\[
\begin{pmatrix}a&0\\c&0\end{pmatrix}.
\]
For \(a=0\), one obtains either \(0\) or, after scaling \(c\), the class \(L\). For \(a\ne0\), the scalar \(a\) is invariant under conjugation, while choosing \(t\) kills \(c\); hence the unique representative is \(D_a\). This proves the characteristic-two list.

For odd \(q\), the square-zero cone has \(q^2\) points: for each \(b\ne0\), \(a,b\) determine \(c\), giving \(q(q-1)\) points, and the \(b=0\) line contributes \(q\) points. The \(U\)-orbit has size \(q(q-1)\), the \(L\)-orbit has size \(q-1\), and zero is fixed.

For even \(q\), the \(b\ne0\) branch has \(q(q-1)\) points. The \(b=0\) branch has \(q^2\) points, so the total is
\[
q(q-1)+q^2=2q^2-q.
\]
The \(U\)-orbit has size \(q(q-1)\), the \(L\)-orbit has size \(q-1\), and each \(D_a\)-orbit has size \(q\). Together with zero this gives \(q+2\) classes.

## Verification

The included checker `artifacts/verify.py` independently reconstructs the Jordan identity, the Rota–Baxter equations, the automorphism form, and the conjugation action symbolically.

It then exhaustively enumerates every \(2\times2\) linear map over
\[
\mathbf F_2,\quad\mathbf F_3,\quad\mathbf F_5,\quad\mathbf F_7
\]
and tests the Rota–Baxter identity on all ordered basis pairs. It separately enumerates all algebra automorphisms and all conjugacy orbits.

The outputs are
\[
q=2:\quad6\text{ operators},\ 4\text{ classes};
\]
\[
q=3:\quad9\text{ operators},\ 3\text{ classes};
\]
\[
q=5:\quad25\text{ operators},\ 3\text{ classes};
\]
\[
q=7:\quad49\text{ operators},\ 3\text{ classes}.
\]

The checker returns `VERIFY_OK`.

Finite enumeration is not used to prove the arbitrary-field theorem or the formulas for arbitrary prime powers.

## Relationship to prior work

Sun, Huang, Zhao, and Tian classify all weight-zero Rota–Baxter operators on complex Jordan algebras of dimension at most three. Their two-dimensional list includes the algebra \(J_4\) with the multiplication used here. Proposition 5.50 parametrizes its complex Rota–Baxter operators as
\[
\begin{pmatrix}
\lambda\mu&-\lambda^2\\
\mu^2&-\lambda\mu
\end{pmatrix}.
\]
It separates the cases \(\lambda\ne0\), \(\lambda=0,\mu\ne0\), and \(\lambda=\mu=0\) according to the induced pre-Jordan algebra.

The complex parametrization is a parametrization of the square-zero cone; over a general field it need not be field-surjective because it uses squares. The field-independent equations above remove that artifact and permit the full automorphism quotient and finite-field census.

The inspected source develops automorphism-orbit methods for compatible pre-Jordan structures, but its Rota–Baxter section presents raw operator matrices and induced pre-Jordan types. Searches of the full text found no operator-conjugacy classification and no finite-field treatment.

Benito, Gubarev, and Pozhidaev study Rota–Baxter operators on several quadratic, matrix, and simple Jordan-type algebras. The publicly accessible article scope concerns different algebra classes and does not supply the two-dimensional \(J_4\) quotient above.

Targeted semantic and literature searches for the \(J_4\) multiplication, Rota–Baxter conjugacy, the square-zero characterization, and finite-field counts did not locate the displayed theorem.

## Limitations

The theorem concerns one distinguished two-dimensional Jordan algebra and weight zero.

The characteristic-two algebra is the base change of the same integral multiplication table; it is not one of the source's complex isomorphism classes considered over \(\mathbb C\).

The result does not classify Rota–Baxter operators on the other five two-dimensional Jordan types over arbitrary fields.

A specialized or unindexed source may contain the same concrete quotient.

Failed searches do not prove novelty.

## References

1. Y. Sun, Z. Huang, S. Zhao, and Z. Tian, “Classification of pre-Jordan Algebras and Rota-Baxter Operators on Jordan Algebras in Low Dimensions,” arXiv:2111.02035v1, first public 3 November 2021. First-listed AMS classification: 16T25; additional classifications 16W10, 17C50, 17C55.
2. P. Benito, V. Gubarev, and A. Pozhidaev, “Rota–Baxter Operators on Quadratic Algebras,” *Mediterranean Journal of Mathematics* 15 (2018), 189, DOI 10.1007/s00009-018-1234-5.
