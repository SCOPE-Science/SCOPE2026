# Automorphism normal forms for Nijenhuis operators on the commutative three-dimensional nilpotent algebra

## Finding

Let \(K\) be a field with
\[
\operatorname{char}K\ne2,
\]
and let \(A_K\) have basis
\[
\{e_1,e_2,e_3\}
\]
with sole nonzero products
\[
e_1e_2=e_2e_1=e_3.
\]
This is the algebra \(A_1\) in the three-dimensional nilpotent associative list used by Abdujabborov, Karimjanov, and Kodirova.

Write endomorphism matrices in the standard column convention. Then the complete Nijenhuis locus is
\[
\boxed{\operatorname{Nij}(A_K)=\mathcal C_1\cup\mathcal C_2,}
\]
where
\[
\mathcal C_1=
\left\{
\begin{pmatrix}
a&0&0\\
b&d&0\\
u&v&a
\end{pmatrix}
:a,b,d,u,v\in K
\right\}
\]
and
\[
\mathcal C_2=
\left\{
\begin{pmatrix}
a&c&0\\
0&d&0\\
u&v&d
\end{pmatrix}
:a,c,d,u,v\in K
\right\}.
\]
Each component is an affine \(5\)-space. Their intersection is
\[
\mathcal C_1\cap\mathcal C_2=
\left\{
\begin{pmatrix}
a&0&0\\
0&a&0\\
u&v&a
\end{pmatrix}
:a,u,v\in K
\right\}
\cong\mathbf A^3.
\]

Assume now that \(K=\mathbf F_q\) with \(q\) odd. The full automorphism group consists of two families:
\[
\mathcal G_0=
\left\{
\begin{pmatrix}
s&0&0\\
0&t&0\\
r&w&st
\end{pmatrix}
:s,t\in\mathbf F_q^\times,\ r,w\in\mathbf F_q
\right\}
\]
and
\[
\mathcal G_1=
\left\{
\begin{pmatrix}
0&s&0\\
t&0&0\\
r&w&st
\end{pmatrix}
:s,t\in\mathbf F_q^\times,\ r,w\in\mathbf F_q
\right\}.
\]
Hence
\[
\boxed{|\operatorname{Aut}(A_{\mathbf F_q})|=2q^2(q-1)^2.}
\]

The automorphism-conjugacy classes of Nijenhuis operators admit explicit normal forms.

For every ordered pair
\[
a\ne d,
\]
there are exactly four classes:
\[
\boxed{
\operatorname{diag}(a,d,a),\quad
\operatorname{diag}(a,d,a)+E_{31},\quad
\operatorname{diag}(a,d,a)+E_{21},\quad
\operatorname{diag}(a,d,a)+E_{21}+E_{32}.
}
\]

For every
\[
a\in\mathbf F_q,
\]
the repeated-eigenvalue fiber has exactly five classes:
\[
\boxed{
aI,\quad
aI+E_{31},\quad
aI+E_{31}+E_{32},\quad
aI+E_{21},\quad
aI+E_{21}+E_{32}.
}
\]

Therefore
\[
\boxed{
|\operatorname{Nij}(A_{\mathbf F_q})/\operatorname{Aut}(A_{\mathbf F_q})|
=
4q(q-1)+5q
=
q(4q+1).
}
\]

The raw Nijenhuis variety has
\[
\boxed{2q^5-q^3}
\]
points. Its exact rank distribution in ranks \(0,1,2,3\) is
\[
\boxed{
\left(
1,\,
(q-1)(q+1)(2q+1),\,
2q(q-1)(2q^2-1),\,
q^2(q-1)(2q^2-2q-1)
\right).
}
\]

Over every extension field \(\mathbf F_{q^m}\),
\[
|\operatorname{Nij}(A_{\mathbf F_q})(\mathbf F_{q^m})|
=
2q^{5m}-q^{3m}.
\]
Thus the Hasse--Weil zeta function of the reduced Nijenhuis variety is
\[
\boxed{
Z(T)=\frac{1-q^3T}{(1-q^5T)^2}.
}
\]

## Assumptions and scope

The 2021 source works over \(\mathbb C\) and gives all Nijenhuis operators on the five three-dimensional nilpotent associative algebras. Its Theorem 5 treats precisely the algebra above. In the source's row-vector display convention, its three listed families combine into the two irreducible affine components written here in the standard column convention.

The extension to arbitrary fields of characteristic different from \(2\) is proved directly below. Characteristic \(2\) is excluded because two torsion equations used to force the component decomposition lose their factor \(2\).

A 2026 complete classification covers all three-dimensional complex associative algebras and explicitly states that a full automorphism-orbit analysis is beyond its scope. The new statement here is the conjugacy classification and exact finite-field orbit count for this algebra, together with the arithmetic of the raw variety.

## Proof

For
\[
x=(x_1,x_2,x_3)^T,\qquad
y=(y_1,y_2,y_3)^T,
\]
the product is
\[
xy=(0,0,x_1y_2+x_2y_1)^T.
\]

Let
\[
N=
\begin{pmatrix}
a&c&p\\
b&d&q\\
u&v&f
\end{pmatrix}.
\]
The Nijenhuis torsion is
\[
T_N(x,y)=N(x)N(y)-N\!\left(N(x)y+xN(y)-N(xy)\right).
\]
Evaluation on ordered basis pairs first gives
\[
p^2=q^2=pq=0.
\]
Since \(K\) is a field,
\[
p=q=0.
\]
The remaining equations are
\[
b(a-f)=0,
\qquad
c(d-f)=0,
\qquad
bc+(a-f)(d-f)=0.
\]
The first two equations arise with a factor \(2\), which is why characteristic \(2\) is excluded.

If \(c=0\), then the equations imply either \(f=a\), producing \(\mathcal C_1\), or a point already contained in the overlap of the two displayed components. Symmetrically, if \(b=0\), they give \(\mathcal C_2\). If both \(b\) and \(c\) were nonzero, the first two equations would force
\[
f=a=d,
\]
and the third would give
\[
bc=0,
\]
a contradiction. This proves the two-component decomposition.

To find automorphisms, note that
\[
A_K^2=Ke_3
\]
is characteristic. Modulo \(Ke_3\), multiplication is the symmetric bilinear form
\[
B((x_1,x_2),(y_1,y_2))=x_1y_2+x_2y_1.
\]
If the induced \(2\times2\) matrix is \(P\) and
\[
g(e_3)=\mu e_3,
\]
then
\[
P^T
\begin{pmatrix}0&1\\1&0\end{pmatrix}
P
=
\mu
\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\]
Because \(2\ne0\), this forces \(P\) to be diagonal or anti-diagonal. The arbitrary \(e_3\)-components in \(g(e_1)\) and \(g(e_2)\) give exactly \(\mathcal G_0\) and \(\mathcal G_1\).

It remains to reduce conjugacy. Take
\[
N=
\begin{pmatrix}
a&0&0\\
b&d&0\\
u&v&a
\end{pmatrix}
\in\mathcal C_1
\]
and
\[
g=
\begin{pmatrix}
s&0&0\\
0&t&0\\
r&w&st
\end{pmatrix}
\in\mathcal G_0.
\]
A direct multiplication gives
\[
b'=\frac ts\,b,
\qquad
u'=tu+\frac ws\,b,
\qquad
v'=sv+\frac{d-a}{t}w.
\]
Put
\[
\lambda=\frac ts,\qquad \eta=\frac wt.
\]
Then
\[
b'=\lambda b,\qquad
u'=tu+\lambda b\eta,\qquad
v'=\frac t\lambda v+(d-a)\eta.
\]

Suppose first that
\[
a\ne d.
\]
If \(b=0\), choose \(\eta\) to kill \(v\), and then \(t\) distinguishes only \(u=0\) from \(u\ne0\). This gives the first two normal forms.

If \(b\ne0\), choose \(\lambda\) so that \(b'=1\), then choose \(\eta\) so that \(u'=0\). The remaining coordinate is zero or nonzero according as
\[
bv-(d-a)u
\]
is zero or nonzero; \(t\) normalizes a nonzero value to \(1\). This gives the other two normal forms.

An anti-diagonal automorphism exchanges the two affine components but preserves the repeated eigenvalue and the simple eigenvalue. Thus the ordered pair \((a,d)\), with \(a\) the repeated eigenvalue, remains the orbit label.

Now suppose
\[
a=d.
\]
If \(b=0\), the point lies in the component intersection. Diagonal scaling and the anti-diagonal swap leave exactly three possibilities for \((u,v)\): both zero, exactly one nonzero, or both nonzero. These give
\[
aI,\qquad aI+E_{31},\qquad aI+E_{31}+E_{32}.
\]
If \(b\ne0\), normalize \(b=1\), use \(w\) to kill \(u\), and distinguish \(v=0\) from \(v\ne0\). These give
\[
aI+E_{21},\qquad aI+E_{21}+E_{32}.
\]
Hence there are four classes for every \(a\ne d\) and five for every \(a=d\).

For point counting,
\[
|\mathcal C_1|=|\mathcal C_2|=q^5,
\qquad
|\mathcal C_1\cap\mathcal C_2|=q^3,
\]
so inclusion--exclusion gives
\[
2q^5-q^3.
\]

For ranks, on \(\mathcal C_1\) the determinant is
\[
a^2d.
\]
The rank-one matrices in \(\mathcal C_1\) require \(a=0\) and are exactly the nonzero rank-one \(2\times2\) matrices in the variables \((b,d;u,v)\), giving
\[
(q-1)(q+1)^2.
\]
The intersection contributes \(q^2-1\) rank-one points. Rankwise inclusion--exclusion gives
\[
(q-1)(q+1)(2q+1)
\]
rank-one operators. The rank-three count is
\[
2q^3(q-1)^2-q^2(q-1)
=
q^2(q-1)(2q^2-2q-1).
\]
The rank-two formula follows by subtraction.

## Verification

The included program `artifacts/verify.py` reconstructs the algebra and Nijenhuis torsion symbolically.

It verifies the component decomposition and the full automorphism group formula.

Over
\[
\mathbf F_3
\quad\text{and}\quad
\mathbf F_5,
\]
it constructs every Nijenhuis operator and every automorphism, computes every conjugacy orbit, and confirms that each orbit contains exactly one of the displayed canonical representatives. The orbit totals are
\[
39
\quad\text{and}\quad
105,
\]
matching
\[
q(4q+1).
\]

It also verifies the raw point and rank formulas over
\[
\mathbf F_3,\quad
\mathbf F_5,\quad
\mathbf F_7.
\]
The raw totals are
\[
459,\quad6125,\quad33271.
\]

The checker returns `VERIFY_OK`.

Finite enumeration is replay evidence. The arbitrary-field component theorem and the odd-finite-field normal-form proof are symbolic.

## Relationship to prior work

Abdujabborov, Karimjanov, and Kodirova classify Nijenhuis operators on all three-dimensional complex nilpotent associative algebras. Their Theorem 5 gives three parametric families for this algebra. Those families are exactly the two affine components above after converting from their row display to the standard column convention. They do not quotient the operators by algebra automorphisms or give finite-field orbit counts.

Zou, Gao, Kang, and Lü later give a complete classification of Nijenhuis operators on all three-dimensional complex associative algebras. Their paper explicitly says that a full orbit analysis under \(\operatorname{Aut}(A)\) is beyond its scope and is left for future conjugacy classification. Thus the complex parameter list is prior coverage, while the automorphism normal forms and finite-field orbit theorem are not implied by that list.

A separate existing calculation for the null-filiform algebra
\[
e_1^2=e_2,\qquad e_1e_2=e_2e_1=e_3
\]
uses the same 2021 source but concerns a different associative algebra with a different automorphism action and Nijenhuis variety.

Focused searches for this exact multiplication, automorphism conjugacy, the orbit formula
\[
q(4q+1),
\]
and the raw count
\[
2q^5-q^3
\]
did not locate a covering statement.

## Limitations

Characteristic \(2\) is excluded from the component and orbit theorem.

The result treats one of the five three-dimensional nilpotent associative algebras, not the full list.

The raw complex Nijenhuis families are already classified in prior work; originality is the automorphism quotient, finite-field normal forms, orbit count, and arithmetic consequences.

Failed searches do not prove absolute novelty.

## References

1. N. G. Abdujabborov, I. A. Karimjanov, and M. A. Kodirova, “Rota-type operators on 3-dimensional nilpotent associative algebras,” *Communications in Mathematics* 29 (2021), 227–241, DOI `10.2478/cm-2021-0020`.
2. X. Zou, X. Gao, C. Kang, and J. Lü, “Nijenhuis Operators on 2D Pre-Lie Algebras and 3D Associative Algebras,” *Axioms* 15 (2026), 80, DOI `10.3390/axioms15010080`.
