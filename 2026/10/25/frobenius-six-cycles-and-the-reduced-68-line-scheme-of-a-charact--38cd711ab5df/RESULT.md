# Frobenius six-cycles and the reduced 68-line scheme of a characteristic-two quartic

## Finding

Let \(X\subset\mathbb P^3_{\mathbb F_2}\) be the quartic
\[
X=V(F),\qquad
F=x_0x_1^2x_2+x_1^4+x_1x_2^3+x_0^3x_3+x_0x_2x_3^2.
\]
Its scheme \(F_1(X)\) parametrizing projective lines is **finite étale of degree \(68\)** over \(\mathbb F_2\). The geometric Frobenius permutation of its points has cycle type
\[
\boxed{1^4\,2^2\,3^2\,6^9}.
\]
The four lines of the distinguished plane section \(x_0=0\) form two rational lines and one conjugate pair. The other \(64\) lines have cycle type \(1^2\,2^1\,3^2\,6^9\). Consequently, every geometric line is defined over \(\mathbb F_{64}\), and this is the smallest finite extension of \(\mathbb F_2\) containing all of them. For each integer \(n\ge1\),
\[
\boxed{\#F_1(X)(\mathbb F_{2^n})=4+4\mathbf1_{2\mid n}+6\mathbf1_{3\mid n}+54\mathbf1_{6\mid n}}.
\]
The Hasse–Weil zeta function of the **line scheme**, not of the quartic surface, is
\[
\boxed{Z(F_1(X),T)=\frac1{(1-T)^4(1-T^2)^2(1-T^3)^2(1-T^6)^9}}.
\]

## Assumptions and scope

All assertions concern exactly the displayed \(\mathbb F_2\)-model, with \(x_0,x_1,x_2,x_3\) homogeneous coordinates and with its usual Grassmannian/Hilbert line scheme. They do not assert the same Frobenius class for other twists or members of the original one-parameter family. Frobenius is the map \(a\mapsto a^2\). The source of the underlying geometric maximum is Veniani's theorem for K3 quartics with rational double points; in this model the sole surface singularity is the \(A_3\) point \([0:0:0:1]\) (Veniani, Section 6).

The first derivatives in characteristic two are
\[
F_{x_0}=x_1^2x_2+x_0^2x_3+x_2x_3^2,\quad
F_{x_1}=x_2^3,\quad
F_{x_2}=x_0x_1^2+x_1x_2^2+x_0x_3^2,\quad
F_{x_3}=x_0^3.
\]
Thus any projective singularity has \(x_0=x_2=0\), and \(F=0\) then forces \(x_1=0\), confirming uniqueness of its support. The \(A_3\) analytic type is the published result cited above.

## Proof

**A finite-field certificate of all geometric lines.** Set \(K=\mathbb F_2[z]/(z^6+z+1)\). The polynomial is irreducible: Rabin's degree-six test yields \(z^{64}=z\) and
\[
\gcd(z^6+z+1,z^8-z)=\gcd(z^6+z+1,z^4-z)=1.
\]
Every projective line over \(K\) has a unique \(2\)-by-\(4\) reduced-row-echelon basis matrix with pivots \(p<q\). Write its rows as \(A,B\). The line lies on \(X\) exactly when the five binary-quartic coefficients of \(F(sA+tB)\) vanish. The accompanying certificate `lines.txt` specifies \(68\) pairwise distinct such matrices. Field elements are encoded by integers from \(0\) to \(63\), interpreted as binary coefficient vectors of polynomials in \(z\); a record contains its two pivots followed by both four-entry rows.

The direct polynomial verification in `verify.py` checks **all five coefficients**, not just isolated evaluations. Independently, `enumerate.cpp` enumerates all \(17,047,617\) Grassmannian chart matrices over \(K\) and finds exactly \(68\) solutions: \(48,16,0,0,3,1\) in pivot charts \((0,1),(0,2),(0,3),(1,2),(1,3),(2,3)\), respectively. Its test at five distinct projective parameter points is exhaustive for binary quartics because a nonzero homogeneous quartic has at most four distinct projective zeros. The two files reproduce exactly the same ordered \(68\)-line certificate.

By Veniani's sharp global upper bound, a characteristic-two K3 quartic has **at most 68** geometric lines. Since this quartic has the required \(A_3\) singularity and the certificate exhibits \(68\) distinct lines, there are no other geometric lines, even over a larger field. This geometric bound, not the finite-field search alone, proves completeness over an algebraic closure.

**Frobenius.** Squaring all entries of a reduced-row-echelon matrix again gives the unique reduced-row-echelon matrix for its Frobenius image. The \(68\) certified matrices are closed under this operation. Iterating it gives exactly four fixed points, two two-cycles, two three-cycles and nine six-cycles. Thus the full geometric splitting occurs over \(K\), and the six-cycles prevent splitting over any proper subextension of \(K\).

**Reducedness.** In any Grassmannian echelon chart, the five coefficients of \(F(sA+tB)\) are defining equations for the line scheme. For each of the \(68\) matrices, `verify.py` computes their \(5\)-by-\(d\) Jacobian in the chart's \(d\) free coordinates (\(0\le d\le4\)), using the characteristic-two first variation of \(F\). All \(68\) Jacobians have rank \(d\); equivalently, every Zariski tangent space is zero. There are no positive-dimensional geometric components by the geometric line bound. Every local Artin algebra is therefore a field, so the entire finite scheme is reduced and, over the perfect field \(\mathbb F_2\), étale.

**Cuspidal plane.** Restriction to \(x_0=0\) factors as
\[
F|_{x_0=0}=x_1(x_1+x_2)(x_1^2+x_1x_2+x_2^2).
\]
These are precisely the four distinct coplanar lines described as cuspidal by Veniani. Two are \(\mathbb F_2\)-rational and the other two are conjugate over \(\mathbb F_4\); subtracting their orbits from the total gives the claimed decomposition of the other \(64\).

Finally, an orbit of length \(d\) contributes \(d\) rational points over \(\mathbb F_{2^n}\) exactly when \(d\mid n\), and its zeta factor is \((1-T^d)^{-1}\). Multiplication of these factors gives the formulas.

## Verification

Run from the directory containing the three certificate files:

```sh
python3 verify.py
g++ -O3 -std=c++17 enumerate.cpp -o enumerate
./enumerate 64 0x43 > generated_lines.txt
cmp lines.txt generated_lines.txt
```

The Python checker verifies irreducibility, full polynomial restrictions, all tangent Jacobians, Frobenius closure, each orbit type and the plane-line refinement. It prints `VERIFY_OK`. The independent C++ chart census visits every \(K\)-rational line in all six echelon charts and prints the complete list in the same order. Both computations use exact arithmetic; no heuristic enumeration, floating point, or unbounded search enters the proof. The published geometric bound is still a necessary mathematical premise to extend the finite certificate to all geometric lines.

## Relationship to prior work

Rams and Schütt introduced the \(68\)-line characteristic-two K3 quartic family (arXiv:1512.01358, Remark 2.3, originally circulated in December 2015). Veniani proved the geometric upper bound and studied the explicit \(A_3\) family and its four cuspidal lines (arXiv:1606.02135, Theorem 1.1 and Section 6). Those facts are expressly used rather than claimed as new. The calculation here identifies the **prime-field Frobenius permutation** for the particular displayed model and verifies the full line-scheme reducedness, yielding arithmetic splitting and its zeta function. The inspected relevant sections do not state these model-specific data; that observation is not a certificate of uniqueness against all historical or unpublished computations.

## Limitations

The theorem does not determine the zeta function or Picard Frobenius action of the desingularized surface. It does not classify the Frobenius action for general nonzero parameters, for twists, or for other arithmetic models of the same geometric surface. Its geometric completeness relies on Veniani's proven bound, and independent validation of this new computation has not occurred. Further historical literature may contain an equivalent arithmetic computation.

## References

1. S. Rams and M. Schütt, *At most 64 lines on smooth quartic surfaces (characteristic 2)*, arXiv:1512.01358 (first publicly posted 2015-12-04), Remark 2.3. https://arxiv.org/abs/1512.01358
2. D. C. Veniani, *Lines on K3 quartic surfaces in characteristic 2*, arXiv:1606.02135 (first publicly posted 2016-06-07), Theorems 1.1–1.2 and Section 6. https://arxiv.org/abs/1606.02135
3. A. Degtyarev, *Lines in supersingular quartics*, arXiv:1604.05836 (2016); comparison concerns smooth quartics and line configurations, not this prime-field Galois action. https://arxiv.org/abs/1604.05836
