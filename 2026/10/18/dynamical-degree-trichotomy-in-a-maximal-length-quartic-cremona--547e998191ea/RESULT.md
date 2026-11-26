# Dynamical-degree trichotomy in a quartic class of ordinary quadratic length seven

## Finding

Consider the quartic plane Cremona map
\[
\Psi([X:Y:Z])=[Z^2(XZ+Y^2):(XZ+Y^2)^2+YZ^3:Z^4].
\]
It has ordinary quadratic length seven, which is maximal **among quartics of Blanc–Furter length two**. Projective-linear postcomposition preserves both of these lengths and the degree. The first dynamical degree, in contrast, takes three distinct values under the following postcompositions. For \(a,b\in\mathbb C^*\), set \(D_{a,b}(x,y)=(ax,by)\) and \(S_{a,b}(x,y)=(ay,bx)\) on \(Z=1\). Then
\[
\lambda_1(D_{a,b}\circ\Psi)=4,\qquad
\lambda_1(S_{a,b}\circ\Psi)=
\begin{cases}
2,&a+b^2\ne0,\\
1,&a+b^2=0.
\end{cases}
\]
On \(a=-b^2\), the map has finite order if and only if \(-b^3\) is a root of unity. Its exact order is then twice the order of \(-b^3\), so this locus realizes every even finite order without changing the quartic degree or either length.

## Assumptions and scope

The base field is \(\mathbb C\). The first dynamical degree is \(\lambda_1(F)=\lim_{n\to\infty}(\deg F^{\circ n})^{1/n}\), with projective degree computed after common-factor cancellation. Ordinary quadratic length counts standard maps \([X:Y:Z]\dashmapsto[YZ:XZ:XY]\), with projective-linear maps allowed between them and at the ends without cost. Blanc–Furter length counts de Jonquières factors up to projective automorphisms. The maximality stated here is relative to the length-two quartics, not to quartic de Jonquières maps. The dynamical classification is for invertible diagonal and antidiagonal postcompositions only.

## Proof

**Degree and lengths.** Calabri–Giao, Theorem 1.3 and equation (3), give \(\Psi\) as the length-two quartic \(\psi_{1.1}\) of ordinary quadratic length seven and prove that no length-two quartic has greater ordinary quadratic length. Postcomposing with a projective automorphism preserves ordinary quadratic length, since such an automorphism or its inverse is allowed at the left end of a factorization. It likewise preserves Blanc–Furter length (left composition with a projective automorphism sends a de Jonquières map between pencils of lines to one of the same kind). Multiplication of a homogeneous triple by an invertible constant matrix preserves its degree and its common divisors. In particular every map under consideration is quartic.

**Diagonal case.** On \(Z=1\) write \(\psi=B\circ A\), where
\[
A(x,y)=(x+y^2,y),\qquad B(x,y)=(x,y+x^2).
\]
These are polynomial automorphisms, so their extensions are birational. For \(F=D_{a,b}\circ\psi\), with \((x_n,y_n)=F^{\circ n}(x,y)\), one has
\[
x_{n+1}=a(x_n+y_n^2),\qquad y_{n+1}=b\big(y_n+(x_n+y_n^2)^2\big).
\]
For \(n\ge1\), the coordinate degrees are \(2\cdot4^{n-1}\) and \(4^n\). This holds at \(n=1\); at each next step the squared term strictly dominates the other summand, first in \(x_n+y_n^2\) and then in \(y_n+(x_n+y_n^2)^2\). For a polynomial map the projective degree is the maximum coordinate degree: homogenize with last coordinate \(Z^d\) at that degree \(d\); at least one other leading component is not divisible by \(Z\). Thus \(\deg F^{\circ n}=4^n\).

**Antidiagonal case.** Let \(L(x,y)=(y,x)\). Then \(B=LAL\), \(S_{a,b}=D_{a,b}L\), and for \(G=S_{a,b}\circ\psi\) one computes
\[
A G A^{-1}=A D_{a,b} A L=H,\qquad H(x,y)=(ay+cx^2,bx),\quad c=a+b^2.
\]
If \(c\ne0\), the coordinate degrees of \(H^{\circ n}\) are \(2^n,2^{n-1}\) for \(n\ge1\). The initial degrees are \(2,1\), and the two recurrences use the square of the previous first coordinate and a nonzero multiple of that coordinate, respectively. Thus \(\deg H^{\circ n}=2^n\). Applying degree submultiplicativity to the conjugations in both directions yields \(2^n/4\le\deg G^{\circ n}\le4\cdot2^n\); taking \(n\)-th roots gives \(\lambda_1(G)=2\).

If \(c=0\), then \(H(x,y)=(ay,bx)\), so \(1\le\deg G^{\circ n}\le4\) for every \(n\) and \(\lambda_1(G)=1\). In this case \(H^2(x,y)=(tx,ty)\) with \(t=ab=-b^3\). The affine scalar map \(H^{2k}\) extends to \([t^kX:t^kY:Z]\), the identity exactly when \(t^k=1\). Odd powers exchange the axes, so none is the identity. Birational conjugacy preserves order. For any primitive root of order \(r\), choose \(b\ne0\) with \(-b^3\) equal to that root and set \(a=-b^2\). This yields exact order \(2r\). For example, \(a=-1,b=1\) yields order four; the square is \((x,y)\mapsto(-x-2y^2,-y)\), and the successive degrees through the fourth iterate are \(4,2,4,1\).

## Verification

The accompanying standard-library checker `verify.py` compares the shear decomposition and the antidiagonal conjugation by sparse polynomial arithmetic at selected parameter values. It also checks sample diagonal and Hénon degree growth and the exact order-four example. These are finite checks; the universal statements follow from the displayed conjugacy and degree inductions. The ordinary length assertion uses Calabri–Giao's theorem rather than the script.

## Relationship to prior work and limitations

Calabri–Giao give the representative, its length and the length-two quartic maximum. Their equivalence allows independent projective automorphisms at the two ends; it is not dynamical conjugacy. The affine/elementary versus Hénon dichotomy and multiplicative degree growth for reduced words are classical, as in Friedland–Milnor. Likewise the finite-order linear behavior is familiar up to birational conjugacy. The statement here concerns which values occur under one-sided monomial changes of a fixed length-seven presentation, the exact exceptional parameter curve, and the simultaneous realization of every even order in that class. It does not give new finite-order conjugacy types, classify all projective-linear postcompositions, or assert a maximality theorem outside the stated quartic stratum. The literature comparison is bounded.

## References

1. A. Calabri and N. T. N. Giao, *On plane Cremona maps of degree 4 and length 2*, [arXiv:2610.08416v1](https://arxiv.org/abs/2610.08416v1), especially Theorem 1.3, equation (3), and Section 7.
2. J. Blanc and J.-P. Furter, *Length in the Cremona group*, Annales Henri Lebesgue **2** (2019), 187–257, [DOI](https://doi.org/10.5802/ahl.18).
3. S. Friedland and J. Milnor, *Dynamical properties of plane polynomial automorphisms*, Ergodic Theory and Dynamical Systems **9** (1989), 67–99, [DOI](https://doi.org/10.1017/S014338570000482X).
4. I. Dolgachev and V. Iskovskikh, *Finite subgroups of the plane Cremona group*, [arXiv:math/0610595](https://arxiv.org/abs/math/0610595), Section 1.
