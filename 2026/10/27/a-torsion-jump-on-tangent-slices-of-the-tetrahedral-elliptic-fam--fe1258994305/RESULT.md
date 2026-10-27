# A torsion jump on tangent slices of the tetrahedral elliptic family

## Finding

Let the tetrahedral invariant elliptic threefold over the parameter plane have equation
\[
S^2=-4R^3+P^2R^2+18PQ^2R-(4P^3+27Q^2)Q^2.
\]
In the Weierstrass coordinates \(X=4R\), \(Y=4iS\), the generic fiber is
\[
Y^2=X^3-P^2X^2-72PQ^2X+16(4P^3+27Q^2)Q^2.
\]
For every \(m\in\mathbb C^\times\), restrict to the tangent line \(P=mt+4/m^2\), \(Q=t\). Then
\[
\boxed{(X,Y)=\left(m^2t^2+\frac{16t}{m},0\right)}
\]
is a rational section of exact order two. The same family has the rational order-three section
\[
(X,Y)=\left(\frac{4P^2}{3},\frac{4(P^3-27Q^2)}{3\sqrt3}\right).
\]
The tangent slice therefore has Mordell--Weil group \(\mathbb Z/6\mathbb Z\) and rank zero. Away from the tangent boundary, the generic slice has Mordell--Weil group \(\mathbb Z\oplus\mathbb Z/3\mathbb Z\), with rank-one height lattice \(\langle1/6\rangle\).

## Assumptions and scope

Work over \(\mathbb C\), with the relatively minimal elliptic surface obtained by completing the indicated line slice. The generic-line statement assumes \(m,r\ne0\) and \(m^2r\ne4\); the tangent statement assumes \(m\ne0\) and \(r=4/m^2\). The claim concerns the Mordell--Weil group of the generic fiber over \(\mathbb C(t)\), not the group of points on each individual specialized fiber.

## Proof

Write \(a_2=-P^2\), \(a_4=-72PQ^2\), and \(a_6=16(4P^3+27Q^2)Q^2\). The third division polynomial is
\[
\psi_3(X)=3X^4+4a_2X^3+6a_4X^2+12a_6X+(4a_2a_6-a_4^2)
=-(4P^2-3X)(X^3-144PQ^2X+64P^3Q^2+1728Q^4).
\]
At \(X=4P^2/3\), the Weierstrass right-hand side is \(16(P^3-27Q^2)^2/27\). Thus the displayed \(Y\)-coordinate gives a rational point killed by multiplication by three. It is not the identity on the generic fiber, so its order is exactly three.

Now put \(P=mt+4/m^2\) and \(Q=t\). Direct polynomial factorization gives
\[
\begin{aligned}
Y^2={}&\frac{(-mX+m^3t^2+16t)}{m^6}\\
&\quad\cdot(-m^5X^2-8m^4Xt+16mX+64m^6t^3+176m^3t^2+256t).
\end{aligned}
\]
Consequently \(X=m^2t^2+16t/m\), \(Y=0\) lies on the curve. A finite point with \(Y=0\) on a nonsingular Weierstrass cubic is a nonidentity point of order two.

The discriminant factor in the source is proportional to \(Q^2(P^3-27Q^2)^3\). For \(P=mt+r\), the cubic factor has discriminant \(-19683r^3(m^2r-4)\). If \(m,r\ne0\) and \(m^2r\ne4\), its three roots are distinct, giving fibers \(I_2,I_3,I_3,I_3,I_1\). At \(r=4/m^2\),
\[
(mt+4/m^2)^3-27t^2=\frac{(m^3t-8)^2(m^3t+1)}{m^6},
\]
so the fibers are \(I_2,I_6,I_3,I_1\), in agreement with the published tangent-line table. In both cases the Weierstrass coefficients have fundamental line bundle of degree one, so the relatively minimal surface is rational and its Néron--Severi rank is ten.

For a generic line, the reducible fibers contribute root lattice \(A_1\oplus A_2^{\oplus3}\) of rank seven and determinant \(2\cdot3^3=54\). Shioda--Tate gives Mordell--Weil rank \(10-2-7=1\). The torsion subgroup injects into the product of component groups \(\mathbb Z/2\oplus(\mathbb Z/3)^3\). A two-torsion section would meet the identity component at every \(I_3\) fiber, so its height would be at least \(2-1/2>0\), contradicting torsion. For a nonzero three-torsion section, the height formula forces nonidentity components at all three \(I_3\) fibers; two independent three-torsion sections are impossible because each component map to \(\mathbb Z/3\) has a nonzero kernel on a two-dimensional \(\mathbb F_3\)-space. Thus the torsion is exactly \(\mathbb Z/3\). The height determinant is \(3^2/54=1/6\), giving \(\langle1/6\rangle\).

For the tangent line, the root lattice is \(A_1\oplus A_5\oplus A_2\), of rank eight and determinant \(2\cdot6\cdot3=36\). Shioda--Tate gives rank zero. The discriminant formula for a rational elliptic surface then gives torsion order six. The explicit order-two section and the inherited order-three section generate a subgroup of order six, so the full group is \(\mathbb Z/6\mathbb Z\).

## Verification

The division-polynomial factorization and the tangent-line Weierstrass factorization were checked by exact symbolic expansion. The parameter discriminant \(-19683r^3(m^2r-4)\) was computed exactly. The rank and height conclusions use the stated fiber configurations, the Shioda--Tate formula, the height formula, and the rational-elliptic-surface discriminant relation. No finite-field experiment or numerical approximation is used as proof.

## Relationship to prior work

Gegelia and van Straten give the tetrahedral discriminant and list both the generic affine-line fiber configuration and the tangent specialization \(m^2r=4\) in their discussion of other sections. Their table does not state the parameter-dependent order-two section above. The abstract Mordell--Weil groups and height lattices are consequences of the classical classification by reducible-fiber root lattices; this finding does not claim those abstract consequences alone as new. Its specific addition is the explicit section formula on the tangent locus and its role in realizing the torsion jump in this parameterized family.

## Limitations

The statement is over \(\mathbb C\) and concerns the generic elliptic curve over the line parameter. It does not classify all specializations of individual fibers, and it does not assert a new classification of rational elliptic surfaces. The classical Mordell--Weil classification already determines the abstract group from the root-lattice data; the priority risk is whether the displayed parameter-dependent section has appeared in a source not located in the searches. The official repository record for the older classification was available, but its full-text request was rate-limited during this check.

## References

1. N. Gegelia and D. van Straten, “The platonic elliptic surfaces,” arXiv:2608.25644 (2026), especially the tetrahedral discriminant and Table 8 on other line sections. \(\texttt{https://arxiv.org/abs/2608.25644}\).
2. K. Oguiso and T. Shioda, “The Mordell-Weil lattice of a rational elliptic surface,” Commentarii Mathematici Universitatis Sancti Pauli 40 (1991), 83--99, DOI: 10.14992/00009974. The official repository record is \(\texttt{https://rikkyo.repo.nii.ac.jp/records/10006}\).
