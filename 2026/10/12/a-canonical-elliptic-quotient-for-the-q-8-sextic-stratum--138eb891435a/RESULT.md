# A canonical elliptic quotient for the \(Q_8\)-sextic stratum

## Finding
Let \(K\) be algebraically closed of characteristic \(0\) or \(p>21\). For a smooth Badr--Bars sextic
\[
C_{b,c}:\quad X^6+Y^5Z+YZ^5+bX^2(Z^4-Y^4)+cX^2Y^2Z^2=0,
\]
consider the displayed quaternion subgroup \(Q_8=\langle A,B\rangle\), where
\[
A=[X:iY:-iZ],\qquad B=[X:\zeta_8Z:-\zeta_8^{-1}Y],\qquad i=\zeta_8^2.
\]
The quotient map \(C_{b,c}\to C_{b,c}/Q_8\) has exactly six ramification points. They form three \(Q_8\)-orbits of size two, each with cyclic stabilizer \(C_4\). Hence
\[
g(C_{b,c}/Q_8)=1,
\]
and the quotient signature is
\[
[1;4,4,4].
\]
For members for which the displayed \(Q_8\) is the full automorphism group, this is the full automorphism quotient.

## Assumptions and scope
The characteristic hypothesis is the one used for the smooth plane-sextic classification and also makes the order-eight action tame. The statement concerns every smooth member carrying the displayed \(Q_8\)-action; it does not assert that every parameter pair \((b,c)\) has full automorphism group exactly \(Q_8\), because special parameters can acquire extra symmetry.

## Proof
The generators satisfy
\[
A^2=B^2=z=[X:-Y:-Z],
\]
where \(z\) is the central involution of \(Q_8\). Every nontrivial subgroup of \(Q_8\) contains \(z\). Therefore every point with nontrivial stabilizer is fixed by \(z\).

The fixed locus of \(z\) in \(\mathbb P^2\) is the line \(X=0\) together with \([1:0:0]\). The isolated fixed point is not on the sextic because \(F(1,0,0)=1\). On \(X=0\), the curve equation becomes
\[
YZ(Y^4+Z^4)=0.
\]
Thus \(z\) fixes exactly six points on the smooth curve.

Write \(t=Y/Z\) on the fixed line. Modulo the central involution, the two generators act by
\[
A:t\longmapsto -t,\qquad B:t\longmapsto -i/t.
\]
The pair \(\{0,\infty\}\) is fixed pointwise by the cyclic subgroup \(\langle A\rangle\) and interchanged by \(B\). The roots of \(t^2=-i\) form a pair fixed pointwise by \(\langle B\rangle\), while the roots of \(t^2=i\) form a pair fixed pointwise by \(\langle AB\rangle\). Hence the six fixed points split into exactly three \(Q_8\)-orbits of size two, and each stabilizer has order \(4\). There are no other ramification points because any nontrivial stabilizer must contain \(z\).

A smooth plane sextic has genus \(10\). Tame Riemann--Hurwitz for \(Y=C_{b,c}/Q_8\) gives
\[
2\cdot10-2=8(2g(Y)-2)+6(4-1).
\]
Both sides contribute \(18\) before the quotient term, so \(g(Y)=1\). The three ramification orbits give three branch points, each of index \(4\), proving the signature \([1;4,4,4]\).

## Verification
The accompanying checker verifies the matrix relations defining \(Q_8\), invariance of the family equation under both generators, the factorization on the central fixed line, the three stabilizer equations in the coordinate \(t\), and the Riemann--Hurwitz computation. These symbolic checks supplement, rather than replace, the group-theoretic proof above.

## Relationship to prior work
Badr and Bars classify smooth plane sextics by automorphism group and exhibit this quaternionic family explicitly. Their table and the detailed quaternion case provide the generators and invariant equation used here. The quotient genus, full ramification locus, and signature \([1;4,4,4]\) are not stated in the inspected portions of that source. Searches for the same conclusion using quaternion-group, plane-sextic, quotient-genus, and signature terminology did not locate a covering statement.

## Limitations
This result determines the quotient by the displayed quaternion subgroup, not the complete geometry of the resulting elliptic curve as a function of \((b,c)\). It does not compute a Weierstrass model or \(j\)-invariant. Older computational tables of higher-genus group actions may encode an abstract genus-ten \(Q_8\) action with the same signature under different notation; no such table was located in the sources inspected here.

## References
E. Badr and F. Bars, *The stratification by automorphism groups of smooth plane sextic curves*, arXiv:2208.12749v1 (2022); later published with DOI 10.1007/s10231-025-01558-z.

E. Badr, M. El-Guindy, and M. Kamel, *Automorphism groups and signatures of smooth septic curves*, Glasgow Mathematical Journal (2025), DOI 10.1017/S0017089525000126. This later degree-seven classification is relevant for comparison of signature methods but does not cover plane sextics.
