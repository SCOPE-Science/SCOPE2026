# Rota–Baxter moduli of the two-dimensional square Zinbiel algebra

## Finding

Let \(K\) be a field and let \(Z_K\) be the two-dimensional Zinbiel algebra with basis
\[
\{e_1,e_2\}
\]
and sole nonzero product
\[
e_1e_1=e_2.
\]

A weight-zero Rota–Baxter operator is exactly
\[
\boxed{
R_{a,b,d}(e_1)=a e_1+b e_2,\qquad
R_{a,b,d}(e_2)=d e_2,\qquad
a(a-2d)=0.
}
\]

The full automorphism group is
\[
\boxed{
\operatorname{Aut}(Z_K)
=
\left\{
\phi_{s,t}:
\phi_{s,t}(e_1)=s e_1+t e_2,\quad
\phi_{s,t}(e_2)=s^2e_2,\quad
s\in K^\times,\ t\in K
\right\}.
}
\]
Conjugation sends
\[
\boxed{
b\longmapsto sb+\frac{a-d}{s}t
}
\]
and fixes \(a,d\).

If \(\operatorname{char}K\ne2\), every orbit has exactly one representative among
\[
\boxed{0,}
\]
\[
\boxed{
N:e_1\mapsto e_2,\qquad e_2\mapsto0,
}
\]
\[
\boxed{
P_d=\operatorname{diag}(0,d),\qquad d\in K^\times,
}
\]
and
\[
\boxed{
Q_d=\operatorname{diag}(2d,d),\qquad d\in K^\times.
}
\]

If \(\operatorname{char}K=2\), the second diagonal branch collapses, and every orbit has exactly one representative among
\[
\boxed{
0,\qquad N,\qquad P_d\ (d\in K^\times).
}
\]

Therefore
\[
\boxed{
|\operatorname{RB}_0(Z_{\mathbf F_q})|
=
\begin{cases}
2q^2-q,&q\text{ odd},\\
q^2,&q\text{ even},
\end{cases}
}
\]
and
\[
\boxed{
|\operatorname{RB}_0(Z_{\mathbf F_q})/\operatorname{Aut}(Z_{\mathbf F_q})|
=
\begin{cases}
2q,&q\text{ odd},\\
q+1,&q\text{ even}.
\end{cases}
}
\]

For odd \(q\), the orbit sizes are \(1\), \(q-1\), and \(q\) repeated \(2(q-1)\) times. For even \(q\), the orbit sizes are \(1\), \(q-1\), and \(q\) repeated \(q-1\) times; when \(q=2\), the first two sizes both equal \(1\).

## Assumptions and scope

The Rota–Baxter identity is the weight-zero identity
\[
R(x)R(y)=R\bigl(R(x)y+xR(y)\bigr).
\]

The result is valid over every field. The cited low-dimensional paper works over \(\mathbb C\); the arbitrary-field statement, the characteristic-\(2\) boundary, the automorphism quotient, and the finite-field counts are proved directly here.

The finite-field formulas count linear operators and their conjugacy classes under the algebra automorphism group.

## Proof

Write
\[
R(e_1)=a e_1+b e_2,\qquad
R(e_2)=c e_1+d e_2.
\]

For the pair \((e_1,e_1)\), the Rota–Baxter identity gives
\[
a^2e_2
=
R(2a e_2)
=
2ac\,e_1+2ad\,e_2,
\]
so
\[
2ac=0,\qquad a^2=2ad.
\]

For \((e_1,e_2)\), it gives
\[
ac\,e_2
=
R(c e_2)
=
c^2e_1+cd\,e_2.
\]
Thus
\[
c^2=0.
\]
Since \(K\) is a field,
\[
c=0.
\]
The remaining equation is
\[
\boxed{a(a-2d)=0.}
\]

For automorphisms, write
\[
\phi(e_1)=s e_1+t e_2.
\]
Since \(e_2=e_1^2\), multiplicativity forces
\[
\phi(e_2)=s^2e_2,
\]
and invertibility is exactly \(s\ne0\). Hence the displayed automorphism group is complete.

Matrix multiplication gives
\[
\phi_{s,t}
\begin{pmatrix}
a&0\\
b&d
\end{pmatrix}
\phi_{s,t}^{-1}
=
\begin{pmatrix}
a&0\\
sb+\dfrac{a-d}{s}t&d
\end{pmatrix}.
\]

Assume first that \(\operatorname{char}K\ne2\). On the branch \(a=0\), every point with \(d\ne0\) has \(a-d\ne0\), so a suitable \(t\) kills \(b\), giving \(P_d\). When \(a=d=0\), conjugation is \(b\mapsto sb\), producing the two orbits \(0\) and \(N\).

On the branch \(a=2d\), a point outside the first branch has \(d\ne0\), so \(a-d=d\ne0\) and again \(t\) kills \(b\), giving \(Q_d\). Since \(a,d\) are conjugacy invariants, all displayed representatives are unique.

If \(\operatorname{char}K=2\), the equation becomes
\[
a^2=0,
\]
hence \(a=0\), so only the \(0,N,P_d\) representatives remain.

For \(\mathbf F_q\),
\[
|\operatorname{Aut}(Z_{\mathbf F_q})|=q(q-1).
\]
If \(q\) is odd, the branch \(a=0\) contributes \(q^2\) operators and the branch \(a=2d\ne0\) contributes \(q(q-1)\), giving \(2q^2-q\). The representatives number
\[
2(q-1)+2=2q.
\]

If \(q\) is even, \(a=0\) for every operator, so there are \(q^2\) operators and
\[
(q-1)+2=q+1
\]
orbits.

The zero operator has full stabilizer. The stabilizer of \(N\) has \(s=1\) and arbitrary \(t\), so its orbit has size \(q-1\). Each nonzero diagonal representative has stabilizer \(t=0\) and arbitrary \(s\ne0\), so its orbit has size \(q\).

## Verification

The included checker exhaustively verifies
\[
\mathbf F_2,\quad
\mathbf F_3,\quad
\mathbf F_5,\quad
\mathbf F_7.
\]

For every \(2\times2\) linear map, it directly checks the Rota–Baxter identity on all ordered pairs of basis vectors and confirms the symbolic equations. It independently enumerates all algebra automorphisms, constructs all conjugacy orbits, and checks the normal-form representatives and orbit-size distributions.

It obtains:
\[
q=2:\ 4\text{ operators},\ 3\text{ orbits};
\]
\[
q=3:\ 15\text{ operators},\ 6\text{ orbits};
\]
\[
q=5:\ 45\text{ operators},\ 10\text{ orbits};
\]
\[
q=7:\ 91\text{ operators},\ 14\text{ orbits}.
\]

The checker returns `VERIFY_OK`. Finite enumeration is not used in the arbitrary-field proof.

## Relationship to prior work

Gao, Ni, and Yu classify Rota–Baxter operators on complex Zinbiel algebras of dimension at most three. For the nontrivial two-dimensional algebra
\[
e_1e_1=e_2,
\]
their Section 3 produces the two complex branches corresponding to
\[
a=0
\]
and
\[
a=2d.
\]

Their manuscript explicitly works over \(\mathbb C\) unless stated otherwise, and the inspected two-dimensional calculation presents raw matrix families rather than an automorphism quotient.

The present result computes that quotient, extends the equations to arbitrary fields, identifies the characteristic-\(2\) collapse of one branch, and gives exact finite-field operator and orbit counts.

A separate paper on finite-dimensional Zinbiel algebras identifies the same square algebra as the nontrivial two-dimensional Zinbiel type, but does not study Rota–Baxter operators.

Targeted semantic and literature searches for square-Zinbiel Rota–Baxter conjugacy, finite-field counts, and the characteristic-\(2\) boundary did not locate the displayed moduli theorem.

## Limitations

The theorem treats only the nontrivial two-dimensional Zinbiel algebra, not the three-dimensional families of the source.

The result concerns field-valued points. It does not determine the scheme structure of the Rota–Baxter equations in characteristic \(2\).

A specialized or unindexed source may contain the same automorphism-orbit classification.

Failed searches do not prove novelty.

## References

1. J. Gao, J. Ni, and J. Yu, “Some Results on Zinbiel Algebras and Rota–Baxter Operators,” *Axioms* 13 (2024), 314, DOI 10.3390/axioms13050314, published 10 May 2024. MSC 2020: 17A30, 17A32.
2. M. Ceballos, J. Núñez, and Á. F. Tenorio, “Finite-dimensional Zinbiel algebras and combinatorial structures,” *Analele Ştiinţifice ale Universităţii Ovidius Constanţa. Seria Matematică* 30 (2022), 67–96, DOI 10.2478/auom-2022-0035.
