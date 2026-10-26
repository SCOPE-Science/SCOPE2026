# A rank-nine Ramanujan matrix with ten annihilator classes at Loewy length three

## Finding
For the finite local ring
\[
R=\mathbb F_2[x,y,z]/(xy,xz,yz,x^3,y^3,z^3,z^2+x^2+y^2),
\]
its generalized Ramanujan matrix \(C_R\), indexed by the associate classes of elements of \(R\), has size \(15\times15\) and rational rank **exactly \(9\)**. Yet its elements have **ten distinct annihilator ideals**. Thus the rank is strictly smaller than the annihilator-type count, with a nontrivial relation beyond the equal-row relations caused by coinciding annihilators. Moreover \(\mathfrak m^3=0\ne\mathfrak m^2\); the phenomenon is absent from the square-zero-radical rank formula.

## Assumptions and scope
The ground field is \(\mathbb F_2\). Put \(u=x^2\), \(v=y^2\), and \(W=\langle u,v\rangle_{\mathbb F_2}\); multiplication satisfies \(z^2=u+v\), all mixed products of \(x,y,z\) vanish, and \(W\mathfrak m=0\). The basis \(1,x,y,z,u,v\) has six vectors, so \(|R|=64\); its maximal ideal is \(\mathfrak m=\langle x,y,z,u,v\rangle\), with \(\mathfrak m^2=W\), \(\mathfrak m^3=0\), and socle \(W\).

For any finite commutative ring and associate-class representatives \(a,b\), define the generalized Ramanujan entry, exactly as in Nguyen--Tân--Treviño, by
\[
C_R(a,b)=\frac{\varphi(R/\operatorname{Ann}(a))}{\varphi(R/\operatorname{Ann}(ab))}\,\mu(R/\operatorname{Ann}(ab)).
\]
Here \(\varphi(S)=|S^\times|\), and the ring Möbius value \(\mu(S)\) is the product of \(-1\) over field factors when \(S\) is a product of fields, and zero otherwise (the zero ring contributes \(1\)). Over this local ring, the value of \(\mu(R/\operatorname{Ann}(t))\) equals \(1\) for \(t=0\), \(-1\) for \(t\in W\setminus\{0\}\), and \(0\) for \(t\notin W\).

## Proof
There are 32 units, each in one associate class. There are three separate nonzero socle classes and one zero class. For an element with nonzero image \(v_0\) in \(V=\langle x,y,z\rangle\), multiplying by \(1+\mathfrak m\) changes its \(W\)-coordinate by \(B(v_0,V)\), where \(B\colon V\times V\to W\) is multiplication. The three directions \(x,y,z\) have \(\operatorname{rank}B(v_0,-)=1\), hence two classes per direction; the remaining four nonzero directions have rank two, hence one class each. There are therefore \(1+1+3+3(2)+4=15\) classes.

The annihilator of a unit is zero, the annihilator of zero is \(R\), and all nonzero elements of \(W\) have annihilator \(\mathfrak m\). For \(v_0+w\) with \(v_0\in V\setminus\{0\}\) and \(w\in W\), the annihilator is \(W\oplus\ker B(v_0,-)\). The seven kernels are distinct: the three coordinate hyperplanes for \(x,y,z\), the coordinate lines for \(x+y,x+z,y+z\), and the diagonal line \(\langle x+y+z\rangle\). Thus there are \(3+7=10\) distinct annihilator ideals.

Let a column indexed by a radical element \(b\) have \(V\)-coordinates \((a,b_0,c)\in\mathbb F_2^3\), and put \(A=(-1)^a\), \(B=(-1)^{b_0}\), \(C=(-1)^c\). For a nonzero non-socle row represented by \(v_0\in V\), the entry is zero on unit columns and on radical columns is
\[
2^{\operatorname{rank}B(v_0,-)}\bigl(2\mathbf1_{B(v_0,(a,b_0,c))=0}-1\bigr).
\]
This uses the three Möbius cases above and \(\varphi(R/\operatorname{Ann}(v_0))=2^{\operatorname{rank}B(v_0,-)}\). The seven distinct row functions, restricted to radical columns, are respectively
\[
\begin{aligned}
&2A,\ 2B,\ 2C,\\
&2(A+B+AB-1),\\
&2(A+C+AC-1),\\
&2(B+C+BC-1),\\
&2(AB+AC+BC-1).
\end{aligned}
\]
Walsh functions on \(V\) are independent. The last four rows have coefficient determinant \(-2\cdot 2^4\ne0\) in the basis \((1,AB,AC,BC)\); together with \(A,B,C\), the seven rows span exactly \(\langle1,A,B,C,AB,AC,BC\rangle\), of dimension seven. All rows for elements with the same nonzero \(V\)-direction coincide.

The zero row is \(1\) on every column. Any nonzero socle row is \(-1\) on unit columns and \(+1\) on radical columns; its sum with the zero row is the radical-only constant \(2\), already in the seven-dimensional span. The two rows together add exactly one new direction, supported on unit columns. Finally the unit row takes \(+32\) at a zero column and \(-32\) at any nonzero socle column, whereas all eight previous directions depend only on the \(V\)-projection within radical columns; it contributes one further independent direction. Therefore \(\operatorname{rank}_{\mathbb Q}C_R=7+1+1=9\).

The additional linear dependence can be displayed explicitly, with \(r_t\) denoting the row for the associate class of \(t\):
\[
r_{x+y}+r_{x+z}+r_{y+z}-r_{x+y+z}-2r_x-2r_y-2r_z+2r_0+2r_u=0.
\]
It is not a relation between two identical annihilator rows because it involves seven distinct nonzero \(V\)-directions.

## Verification
Run `python3 verify.py` using only the Python standard library. The script constructs the complete 64-element multiplication table, checks associativity on basis triples, verifies the radical and socle properties, enumerates all unit orbits and annihilator sets, evaluates all 225 matrix entries by the defining quotient formula, obtains rank nine by exact rational elimination, and checks the displayed row relation. Expected output: `VERIFY_OK order=64 classes=15 annihilator_types=10 rank=9 relation=zero`. The human proof is independent of the finite checker.

## Relationship to prior work
Nguyen, Tân and Treviño (2026), Section 3, introduce this matrix for arbitrary finite commutative rings; their Theorem 3.3 characterizes its nonsingularity by the Frobenius property and Question 3.4 asks about its rank. Those statements do not determine the rank in this non-Frobenius example. The reported square-zero-radical rank formula in the related published research record treats \(\mathfrak m^2=0\); the present example has \(\mathfrak m^2\ne0\), and exhibits rank below the number of annihilator types.

## Limitations
The calculation concerns one explicitly specified ring and is not a rank formula for all rings with cube-zero radical. The ring has 64 elements, but minimality among all smaller rings is not claimed. The possible occurrence of an equivalent computation in unindexed literature is a bibliographic limitation, and independent mathematical audit has not been performed.

## References
1. Tung T. Nguyen, Nguyen Duy Tân, Enrique Treviño, *Supercharacter theory and applications to Ramanujan sums over a finite Frobenius ring*, arXiv:2609.30407v1 (first posted 2026-09-24), Section 3, especially equation (3.1), Theorem 3.3, Question 3.4. https://arxiv.org/html/2609.30407v1
2. *Rank formula for Ramanujan matrices with square-zero radical*, published research record dated 2026-10-04, indexed summary: https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-rank-formula-for-ramanujan-matrices-with-square-zero-radical--5cc1344198a0 (full text not inspected).
