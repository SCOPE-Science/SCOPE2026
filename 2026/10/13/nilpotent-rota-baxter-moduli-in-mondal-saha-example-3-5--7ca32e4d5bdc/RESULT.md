# Nilpotent Rota–Baxter moduli in Mondal–Saha Example 3.5

## Finding

Let \(K\) be a field with
\[
\operatorname{char}K\ne2,
\]
and let \(L_K\) have basis
\[
\{e_1,e_2,e_3\}
\]
with nonzero left Leibniz brackets
\[
[e_3,e_2]=e_2,\qquad [e_3,e_1]=e_1+e_2.
\]

A weight-zero Rota–Baxter operator satisfies
\[
[T(x),T(y)]
=
T\bigl([T(x),y]+[x,T(y)]\bigr).
\]

The nilpotent weight-zero Rota–Baxter operators on \(L_K\) are exactly
\[
\boxed{\operatorname{RB}_{\mathrm{nil}}(L_K)=\mathcal N_1\cup\mathcal N_2,}
\]
where
\[
\mathcal N_1=
\left\{
\begin{pmatrix}
0&0&0\\
d&0&f\\
0&0&0
\end{pmatrix}
:d,f\in K
\right\},
\]
and
\[
\mathcal N_2=
\left\{
\begin{pmatrix}
0&0&c\\
0&0&f\\
0&0&0
\end{pmatrix}
:c,f\in K
\right\}.
\]
Thus the nilpotent locus is two affine \(2\)-planes meeting in
\[
\mathcal N_1\cap\mathcal N_2=K E_{23}.
\]

Every nonzero operator in this locus has rank \(1\) and satisfies
\[
T^2=0.
\]

The full automorphism group is
\[
\boxed{
\operatorname{Aut}(L_K)=
\left\{
G_{u,v}=
\begin{pmatrix}
u&0&0\\
v&u&0\\
0&0&1
\end{pmatrix}
:u\in K^\times,\ v\in K
\right\}.
}
\]

Under conjugation, every nilpotent Rota–Baxter operator is conjugate to exactly one member of
\[
\boxed{
\{dE_{21}:d\in K\}
\ \cup\
\{dE_{21}+E_{23}:d\in K\}
\ \cup\
\{E_{13}\}.
}
\]

Over every odd finite field \(\mathbf F_q\),
\[
\boxed{|\operatorname{RB}_{\mathrm{nil}}(L_{\mathbf F_q})|=2q^2-q}
\]
and
\[
\boxed{
|\operatorname{RB}_{\mathrm{nil}}(L_{\mathbf F_q})/\operatorname{Aut}(L_{\mathbf F_q})|
=
2q+1.
}
\]

For every extension field \(\mathbf F_{q^m}\), the nilpotent locus has
\[
2q^{2m}-q^m
\]
points, so
\[
\boxed{
Z(T)=\frac{1-qT}{(1-q^2T)^2}.
}
\]

## Assumptions and scope

Mondal and Saha study this algebra in Example 3.5 of their paper on Rota–Baxter Leibniz algebras. Their displayed family is precisely \(\mathcal N_2\). They define nilpotent Rota–Baxter operators immediately before the example.

The preprint first appeared on 1 August 2022. The journal article lists \(17A32\) first among its MSC 2020 codes.

Zhang's 2018 paper already classifies all complex weight-zero Rota–Baxter operators on every non-Lie solvable Leibniz algebra of dimension at most \(3\), including this algebra. No originality is claimed for the raw complex operator list. The result here isolates the complete nilpotent sublocus over fields of characteristic different from \(2\), determines its geometry, and computes its automorphism quotient.

## Proof

For
\[
x=(x_1,x_2,x_3)^T,\qquad
y=(y_1,y_2,y_3)^T,
\]
the bracket is
\[
[x,y]
=
x_3\bigl(y_1e_1+(y_1+y_2)e_2\bigr).
\]

Write
\[
T=
\begin{pmatrix}
a&b&c\\
d&e&f\\
g&h&i
\end{pmatrix}.
\]
Evaluating the Rota–Baxter defect
\[
[T(x),T(y)]-T([T(x),y]+[x,T(y)])
\]
on the nine ordered basis pairs yields, among the resulting equations,
\[
h^2=0,\qquad g(g+h)=0.
\]
Because \(K\) is a field,
\[
g=h=0.
\]

The remaining system contains
\[
b(a+b+e)=0,
\]
and
\[
a^2+ab+bd+bi=0,\qquad
a^2+ab+bd-bi=0.
\]

If \(b=0\), the equations force
\[
a=e=0,\qquad ci=0,\qquad fi=cd.
\]
If \(i\ne0\), then \(c=f=0\), so
\[
T=
\begin{pmatrix}
0&0&0\\
d&0&0\\
0&0&i
\end{pmatrix},
\]
which is nilpotent exactly when \(i=0\).

If \(i=0\), the remaining condition is
\[
cd=0.
\]
This gives exactly \(\mathcal N_1\cup\mathcal N_2\).

If \(b\ne0\), subtraction of the two displayed equations gives
\[
2bi=0.
\]
Since \(\operatorname{char}K\ne2\),
\[
i=0.
\]
The rest of the system gives
\[
e=-a-b,\qquad
d=-\frac{a(a+b)}{b},\qquad
f=-\frac{(a+b)c}{b}.
\]
The resulting matrix has rank \(1\) and trace
\[
a+e=-b\ne0,
\]
so it is not nilpotent.

Thus the nilpotent locus is exactly the two displayed planes. Every point on either plane has square zero; hence every nonzero point has rank \(1\).

For automorphisms, the derived ideal
\[
[L_K,L_K]=\langle e_1,e_2\rangle
\]
is characteristic. On this ideal, left multiplication by \(e_3\) is
\[
J=
\begin{pmatrix}
1&0\\
1&1
\end{pmatrix}.
\]
An automorphism has block form
\[
\begin{pmatrix}P&0\\0&s\end{pmatrix}
\]
after \([e_3,e_3]=0\) eliminates the translation part, and bracket preservation gives
\[
PJ=sJP.
\]
Because \(2\ne0\), trace comparison gives \(s=1\). The centralizer of \(J\) consists exactly of
\[
P=
\begin{pmatrix}
u&0\\
v&u
\end{pmatrix},
\qquad u\ne0,
\]
which proves the automorphism formula.

Conjugation gives
\[
G_{u,v}(dE_{21}+fE_{23})G_{u,v}^{-1}
=
dE_{21}+ufE_{23},
\]
and
\[
G_{u,v}(cE_{13}+fE_{23})G_{u,v}^{-1}
=
ucE_{13}+(vc+uf)E_{23}.
\]

On \(\mathcal N_1\), the parameter \(d\) is fixed and \(f\) has two orbits: zero and nonzero. On \(\mathcal N_2\), the \(c=0\) points are already in the intersection, while every point with \(c\ne0\) is conjugate to \(E_{13}\). This gives the unique normal forms.

Over \(\mathbf F_q\), each plane has \(q^2\) points and their intersection has \(q\), so the point count is \(2q^2-q\). The normal forms contribute \(q+q+1=2q+1\) conjugacy classes.

## Verification

The bundled program `artifacts/verify.py` reconstructs the Leibniz product and weight-zero Rota–Baxter defect symbolically.

It verifies that every point of \(\mathcal N_1\cup\mathcal N_2\) has zero Rota–Baxter defect and square zero.

Over \(\mathbf F_3\), it exhaustively checks all \(3^9\) endomorphisms and confirms that the nilpotent Rota–Baxter locus is exactly the two-plane union.

Over
\[
\mathbf F_3,\quad
\mathbf F_5,\quad
\mathbf F_7,
\]
it constructs the full automorphism group and computes every conjugacy orbit. The nilpotent-operator counts are
\[
15,\quad45,\quad91,
\]
and the orbit counts are
\[
7,\quad11,\quad15.
\]

The checker returns `VERIFY_OK`.

Finite-field enumeration is replay evidence. Completeness and the normal-form theorem are symbolic.

## Relationship to prior work

Mondal–Saha Example 3.5 gives exactly the component
\[
\mathcal N_2=
\left\{
\begin{pmatrix}
0&0&c\\
0&0&f\\
0&0&0
\end{pmatrix}
\right\}.
\]
The paper does not claim that this displayed family is exhaustive.

Zhang's 2018 classification is broader at the raw-operator level: it gives all complex weight-zero Rota–Baxter operators on every three-dimensional non-Lie nonnilpotent solvable Leibniz algebra, including the multiplication
\[
[c,a]=a+b,\qquad[c,b]=b,
\]
which is the same algebra after renaming the basis. Thus the existence of the second nilpotent component is already implicit in that raw classification.

The new statement is the exact nilpotent moduli theorem: the two-plane geometry over arbitrary characteristic different from \(2\), square-zero rigidity, the full automorphism group, unique conjugacy normal forms, finite-field orbit count, and zeta function.

Targeted searches for the exact algebra together with nilpotent Rota–Baxter conjugacy, automorphism orbits, the count \(2q+1\), and the zeta function did not locate a covering statement.

## Limitations

Characteristic \(2\) is excluded.

The theorem treats nilpotent weight-zero Rota–Baxter operators on one three-dimensional solvable Leibniz algebra. It does not reclassify all Rota–Baxter operators.

Failed searches do not prove absolute historical novelty.

## References

1. B. Mondal and R. Saha, “Cohomology, deformations and extensions of Rota-Baxter Leibniz algebras,” *Communications in Mathematics* 30 (2022), 93–117, DOI `10.46298/cm.10295`, arXiv:2208.00560.
2. L. Zhang, “Rota-Baxter Leibniz Algebras and Their Constructions,” *Advances in Mathematical Physics* 2018, Article ID 8540674, DOI `10.1155/2018/8540674`.
