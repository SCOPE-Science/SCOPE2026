# A non-smooth automorphism scheme for the characteristic-two Leibniz family \(L_8(\lambda)\)
## Finding
Let \(k\) be a field of characteristic \(2\), and let \(L=L_8(\lambda)\) have basis \(a_1,a_2,a_3\) with
\[
[a_1,a_1]=\lambda a_3,\qquad [a_1,a_2]=[a_2,a_1]=a_2,\qquad [a_2,a_2]=a_3,
\]
all other basis products being zero. The automorphism functor of \(L\), evaluated on commutative \(k\)-algebras, is represented by
\[
\mathcal A_\lambda=\operatorname{Spec} k[b,c,u,u^{-1}]/(b^2-\lambda(u^2-1)).
\]
For every commutative \(k\)-algebra \(R\), its \(R\)-points are exactly the matrices
\[
\begin{pmatrix}
1&0&0\\
b&u&0\\
c&bu&u^2
\end{pmatrix},
\qquad u\in R^\times,
\qquad b^2=\lambda(u^2-1).
\]
After adjoining an element \(s\) with \(s^2=\lambda\) and putting \(v=b+s(u-1)\), the equation becomes \(v^2=0\). Therefore the geometric automorphism scheme has dimension \(2\), is nonreduced at every geometric point, and is nowhere smooth. Its tangent space at the identity has dimension \(3\), with tangent matrices
\[
\begin{pmatrix}
0&0&0\\
q&p&0\\
r&q&0
\end{pmatrix},
\]
which is exactly the derivation algebra of \(L_8(\lambda)\). Thus there is one infinitesimal automorphism direction beyond the tangent space of the reduced geometric automorphism group.

## Assumptions and scope
The base is an arbitrary field \(k\) of characteristic \(2\), and \(\lambda\) is arbitrary. The statement concerns the affine automorphism group scheme of the fixed algebra \(L_8(\lambda)\), not merely its group of \(k\)-rational automorphisms. No perfection or algebraic-closedness hypothesis is used in the functorial matrix calculation. The geometric nonreducedness statement is made after scalar extension to a field containing a square root of \(\lambda\), in particular to an algebraic closure.

## Proof
For a commutative \(k\)-algebra \(R\), write a general \(R\)-linear automorphism candidate as
\[
f(a_1)=A a_1+B a_2+C a_3,\qquad
f(a_2)=D a_1+E a_2+F a_3,\qquad
f(a_3)=G a_1+H a_2+I a_3.
\]
For vectors \(x=(x_1,x_2,x_3)\) and \(y=(y_1,y_2,y_3)\), the bracket is
\[
[x,y]=(x_1y_2+x_2y_1)a_2+(\lambda x_1y_1+x_2y_2)a_3.
\]
Applying \(f([a_1,a_2])=[f(a_1),f(a_2)]\) gives \(D=0\), \((A-1)E=0\), and \(F=BE\). Applying \(f([a_2,a_2])=[f(a_2),f(a_2)]\) gives \(G=H=0\) and \(I=E^2\). The determinant is then \(AE^3\). Because it is a unit, both \(A\) and \(E\) are units, so \((A-1)E=0\) forces \(A=1\). Finally, \(f([a_1,a_1])=[f(a_1),f(a_1)]\) becomes
\[
B^2=\lambda(E^2-1).
\]
No further relation occurs, because \(a_3\) is central and the remaining defining products are already preserved. Renaming \(B=b\), \(C=c\), and \(E=u\) proves the functorial matrix description and the coordinate ring.

The ambient ring \(k[b,c,u,u^{-1}]\) has dimension \(3\), and the displayed nonzero equation cuts a hypersurface, so \(\dim \mathcal A_\lambda=2\). After adjoining \(s\) with \(s^2=\lambda\), characteristic \(2\) gives
\[
b^2-\lambda(u^2-1)=\bigl(b+s(u-1)\bigr)^2.
\]
Thus with \(v=b+s(u-1)\), the geometric coordinate ring is
\[
\overline{k}[c,u,u^{-1},v]/(v^2),
\]
so every geometric local ring contains the nonzero nilpotent class of \(v\). Hence the scheme is geometrically nonreduced and nowhere smooth.

For the tangent space, evaluate on \(k[\varepsilon]/(\varepsilon^2)\) at the identity by taking
\[
b=\varepsilon q,\qquad u=1+\varepsilon p,\qquad c=\varepsilon r.
\]
The defining equation imposes no first-order condition, because both sides are quadratic in \(\varepsilon\). The resulting tangent matrix is
\[
\begin{pmatrix}
0&0&0\\
q&p&0\\
r&q&0
\end{pmatrix},
\]
so the tangent space has dimension \(3\). Direct differentiation of the multiplication identities gives precisely the derivation rule, and the companion derivation classification records exactly this three-parameter matrix family.

## Verification
The accompanying `verify.py` checks the universal matrix identities symbolically in characteristic \(2\), reduces them modulo \(b^2-\lambda(u^2-1)\), verifies the full three-parameter derivation family, checks that adjoining \(s\) and substituting \(v=b+s(u-1)\) turns the relation into \(v^2=0\), and independently enumerates all invertible \(3\)-by-\(3\) matrices over \(\mathbb F_2\) for \(\lambda=0\). The finite enumeration finds exactly \(2\) ordinary automorphisms, as predicted by the reduced field-point formula. The checker output ends with `CHECK_OK`.

The finite enumeration is only a consistency check. The arbitrary-field and scheme-theoretic conclusions follow from the symbolic functorial calculation above.

## Relationship to prior work
Kurdachenko, Pypka, and Semko determine the ordinary automorphism groups of all three-dimensional non-Lie left Leibniz algebras over arbitrary fields in arXiv:2609.24320v1. For the characteristic-two family \(L_8(\lambda)\), their Theorem 4.2 gives the same field-point matrix equation \(b^2=\lambda(u^2-1)\), and Corollary 4.3 analyzes the resulting ordinary group according to whether \(\lambda\) is a square.

Their companion paper arXiv:2609.24323v1 determines derivation algebras. For \(L_8(\lambda)\), it gives the three-dimensional matrix family displayed above and notes that it is independent of \(\lambda\). The new point here is to treat the automorphisms functorially over arbitrary commutative base algebras, thereby exposing the nonreduced automorphism scheme and identifying the exact one-dimensional infinitesimal excess over the reduced geometric subgroup. The two source papers discuss ordinary automorphism groups and derivation algebras separately and do not formulate this group-scheme comparison.

The 2025 complex-field classification by Kaygorodov and Lopatin cannot cover this phenomenon because characteristic \(2\) is essential.

## Limitations
This result concerns only the family \(L_8(\lambda)\). It does not classify smoothness of the automorphism schemes for the other fifteen three-dimensional non-Lie Leibniz types. It also does not classify higher-order deformation functors beyond the explicitly determined automorphism group scheme. The originality search found no equivalent statement, but literature using different terminology for automorphism group schemes of nonassociative algebras may not be fully indexed.

## References
1. L. A. Kurdachenko, O. O. Pypka, M. M. Semko, *Automorphism Groups of Three-Dimensional Leibniz Algebras: A Complete Description*, arXiv:2609.24320v1, 2026.
2. L. A. Kurdachenko, O. O. Pypka, M. M. Semko, *Derivation Algebras of Three-Dimensional Leibniz Algebras: A Complete Description*, arXiv:2609.24323v1, 2026.
3. I. Kaygorodov, A. Lopatin, *Polynomial invariants for three-dimensional Leibniz algebras*, Canadian Mathematical Bulletin, published online 25 November 2025, DOI:10.4153/S0008439525101471.
