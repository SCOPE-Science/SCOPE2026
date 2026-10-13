# Characteristic-three phase transition for anti-Rota–Baxter operators on the dual numbers

## Finding

Let
\[
D_K=K[\varepsilon]/(\varepsilon^2)
\]
with ordered basis
\[
(1,\varepsilon).
\]
An anti-Rota–Baxter operator is a linear map \(T:D_K\to D_K\) satisfying
\[
T(x)T(y)=-T\!\left(T(x)y+xT(y)\right)
\]
for all \(x,y\in D_K\).

Write
\[
T=
\begin{pmatrix}
a&b\\
c&d
\end{pmatrix},
\qquad
T(1)=a+c\varepsilon,\quad
T(\varepsilon)=b+d\varepsilon.
\]
Then \(T\) is anti-Rota–Baxter if and only if
\[
3a^2+2bc=0,\qquad
2c(2a+d)=0,
\]
\[
b(3a+d)=0,\qquad
2ad+2bc+d^2=0,
\]
\[
3b^2=0,\qquad
4bd=0.
\]

If
\[
\operatorname{char}K\ne3,
\]
these equations reduce to
\[
\boxed{
T=
\begin{pmatrix}
0&0\\
c&0
\end{pmatrix},
\qquad c\in K.
}
\]

If
\[
\operatorname{char}K=3,
\]
the solution set jumps to the union of two affine planes meeting only at the zero operator:
\[
\boxed{
\mathcal A=
\left\{
\begin{pmatrix}
a&b\\
0&0
\end{pmatrix}:a,b\in K
\right\},
}
\]
and
\[
\boxed{
\mathcal B=
\left\{
\begin{pmatrix}
a&0\\
c&a
\end{pmatrix}:a,c\in K
\right\}.
}
\]

Consequently, over a finite field \(\mathbf F_q\),
\[
\boxed{
|\operatorname{ARB}(D_{\mathbf F_q})|=
\begin{cases}
q,&3\nmid q,\\
2q^2-1,&3\mid q.
\end{cases}}
\]

In characteristic \(3\), the rank distribution is
\[
\boxed{
\#\{\operatorname{rank}T=0,1,2\}
=
\left(1,\ q^2+q-2,\ q(q-1)\right).
}
\]
Thus characteristic \(3\) is exactly the case in which invertible anti-Rota–Baxter operators occur on the dual numbers; there are
\[
\boxed{q(q-1)}
\]
of them.

The strong condition
\[
T(x)T(y)z=xT(y)T(z)
\]
has another sharp description. If \(3\nmid q\), every anti-Rota–Baxter operator is strong. If \(3\mid q\), the strong operators are exactly the plane \(\mathcal B\), so there are
\[
\boxed{q^2}
\]
strong operators.

The algebra automorphisms are
\[
\phi_u(1)=1,\qquad
\phi_u(\varepsilon)=u\varepsilon,
\qquad u\in K^\times.
\]
Conjugation acts by
\[
\phi_uT\phi_u^{-1}
=
\begin{pmatrix}
a&b/u\\
uc&d
\end{pmatrix}.
\]
Hence, over \(\mathbf F_q\), if \(3\nmid q\) there are exactly two conjugacy classes: the zero operator and the nonzero line. If \(3\mid q\), there are
\[
\boxed{4q-1}
\]
classes: \(2q-1\) singleton classes and \(2q\) classes of size \(q-1\).

Over every finite extension, the same characteristic dichotomy persists. Thus the Hasse–Weil zeta function of the anti-Rota–Baxter solution set is
\[
\boxed{
Z(T)=
\begin{cases}
\dfrac{1}{1-qT},&3\nmid q,\\[2mm]
\dfrac{1-T}{(1-q^2T)^2},&3\mid q.
\end{cases}}
\]

## Assumptions and scope

The anti-Rota–Baxter identity is the associative-algebra identity introduced by Gao, Liu, and Bai. Their paper works throughout over characteristic \(0\), whereas the calculation here is performed directly over an arbitrary field.

The algebra \(D_K\) is the two-dimensional unital local algebra of dual numbers. This is different from the two-dimensional complex algebra used in Example 2.20 of the source, whose nonzero products are \(e_1e_1=e_1\) and \(e_1e_2=e_2\).

The strong condition is the source's strong anti-Rota–Baxter identity. Equivalence means conjugation by unital algebra automorphisms of \(D_K\).

## Proof

For
\[
x=x_0+x_1\varepsilon,\qquad
y=y_0+y_1\varepsilon,
\]
multiplication is
\[
xy=x_0y_0+(x_0y_1+x_1y_0)\varepsilon.
\]

The anti-Rota–Baxter defect
\[
\Delta_T(x,y)
=
T(x)T(y)+T\!\left(T(x)y+xT(y)\right)
\]
is bilinear in \(x,y\). It therefore suffices to evaluate it on the four ordered pairs from \((1,\varepsilon)\).

For \((1,1)\), the two coordinates are
\[
3a^2+2bc,\qquad 2c(2a+d).
\]
For \((1,\varepsilon)\), and identically for \((\varepsilon,1)\), they are
\[
b(3a+d),\qquad 2ad+2bc+d^2.
\]
For \((\varepsilon,\varepsilon)\), they are
\[
3b^2,\qquad4bd.
\]
This proves the displayed defining system.

Suppose first that \(\operatorname{char}K\ne3\). If the characteristic is \(2\), the first, fourth, and fifth equations give
\[
a=d=b=0.
\]
If the characteristic is different from \(2\) and \(3\), the fifth equation gives \(b=0\), the first gives \(a=0\), and the fourth gives \(d=0\). In either case \(c\) is free, proving the one-dimensional family.

Now assume \(\operatorname{char}K=3\). The equations reduce to
\[
bc=0,\qquad c(d-a)=0,\qquad bd=0,\qquad d(d-a)-bc=0.
\]
If \(b\ne0\), then \(c=d=0\), while \(a\) is free; this lies in \(\mathcal A\). If \(b=0\), then either \(d=a\), giving \(\mathcal B\), or \(d=0\) and \(c=0\), which is already the \(b=0\) part of \(\mathcal A\). The two planes intersect only at zero.

The finite-field counts and rank distribution follow immediately. In \(\mathcal A\), every nonzero operator has rank \(1\). In \(\mathcal B\), an operator has determinant \(a^2\), so it has rank \(2\) exactly when \(a\ne0\).

For the strong condition, evaluation on basis triples reduces to
\[
b=0,\qquad a(a-d)=0
\]
within the anti-Rota–Baxter locus. Thus the characteristic-\(3\) strong locus is exactly \(\mathcal B\); outside characteristic \(3\), the entire one-dimensional anti-Rota–Baxter family is strong.

Every unital automorphism of \(D_K\) fixes \(1\) and preserves the radical \(K\varepsilon\), hence has the form
\[
\phi_u=\operatorname{diag}(1,u),\qquad u\ne0.
\]
The displayed conjugation formula follows by matrix multiplication.

When \(3\nmid q\), multiplication by \(u\) is transitive on nonzero \(c\), giving two classes. In characteristic \(3\), on \(\mathcal A\) the parameter \(a\) is fixed and nonzero \(b\)'s form one orbit for each \(a\); on \(\mathcal B\), \(a\) is fixed and nonzero \(c\)'s form one orbit for each \(a\). The \(b=0\) line of \(\mathcal A\) and the \(c=0\) line of \(\mathcal B\) consist of fixed points and intersect only at zero. Hence there are \(2q-1\) singleton classes and \(2q\) nontrivial classes.

The extension-field point counts are \(q^m\) outside characteristic \(3\) and \(2q^{2m}-1\) in characteristic \(3\). Substituting these into the defining exponential series for the Hasse–Weil zeta function gives the stated rational functions.

## Verification

The included program `artifacts/verify.py` reconstructs the six scalar anti-Rota–Baxter equations from multiplication in \(K[\varepsilon]/(\varepsilon^2)\).

It independently evaluates the strong identity and the algebra-automorphism conjugation action.

It exhaustively tests all \(q^4\) linear endomorphisms over
\[
\mathbf F_2,\quad\mathbf F_3,\quad\mathbf F_5,\quad\mathbf F_7.
\]
The resulting anti-Rota–Baxter counts are
\[
2,\quad17,\quad5,\quad7.
\]
For \(\mathbf F_3\), the rank profile is
\[
(1,10,6),
\]
the strong count is \(9\), and there are \(11\) automorphism classes. These agree with the closed formulas.

The checker returns `VERIFY_OK`.

Finite enumeration is a replay check. The arbitrary-field classification is proved by the exact equation split above.

## Relationship to prior work

Gao, Liu, and Bai introduced anti-Rota–Baxter operators on associative algebras as operators governing anti-dendriform structures. Their Definition 2.15 gives the exact operator identity and the strong condition used here. The paper explicitly assumes characteristic \(0\).

The same paper gives an explicit two-dimensional complex example, but its algebra has nonzero products
\[
e_1e_1=e_1,\qquad e_1e_2=e_2,
\]
rather than the dual-number multiplication. In that example all anti-Rota–Baxter operators form a single affine line and are strong.

The source also proves that invertible anti-O-operators are automatically strong. The characteristic-\(3\) dual-number family found here is consistent with that theorem: every invertible operator lies in the strong plane \(\mathcal B\).

Targeted searches for anti-Rota–Baxter operators on the dual numbers, \(K[\varepsilon]/(\varepsilon^2)\), characteristic \(3\), and finite-field anti-Rota–Baxter counts did not locate the two-plane phase transition, the finite-field formulas, or the automorphism quotient.

## Limitations

The theorem is specific to the dual-number algebra and the weightless anti-Rota–Baxter identity of the cited source.

The source literature was developed in characteristic \(0\); although the polynomial identity itself makes sense over every field, no claim is made that every structural theorem from that paper extends unchanged to positive characteristic.

A specialized or differently indexed positive-characteristic calculation may exist. Failed searches do not prove novelty.

## References

1. D. Gao, G. Liu, and C. Bai, “Anti-dendriform algebras, new splitting of operations and Novikov type algebras,” arXiv:2209.08962v1, first public 19 September 2022; *Journal of Algebraic Combinatorics* 59 (2024), 661–696, DOI `10.1007/s10801-024-01303-4`.
