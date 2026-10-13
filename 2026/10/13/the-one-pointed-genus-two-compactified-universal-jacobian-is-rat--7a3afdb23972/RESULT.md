# The one-pointed genus-two compactified universal Jacobian is rationally product-indecomposable
## Finding
Let \(X=\overline{J}_{2,1}\) be a fine compactified universal Jacobian over \(\overline{\mathcal M}_{2,1}\). Fava computes Tate-type rational cohomology with Hodge--Euler polynomial
\[
L^6+5L^5+15L^4+20L^3+15L^2+5L+1.
\]
Because \(X\) is smooth and proper and its cohomology is Tate, its odd rational cohomology vanishes and
\[
\bigl(b_0,b_2,b_4,b_6,b_8,b_{10},b_{12}\bigr)=(1,5,15,20,15,5,1).
\]
Define the reduced even-degree Poincaré polynomial
\[
B_X(t)=\sum_{k=0}^6 b_{2k}t^k=1+5t+15t^2+20t^3+15t^4+5t^5+t^6.
\]
Then \(B_X(t)\) is irreducible in \(\mathbf Z[t]\). Consequently there is no nontrivial product decomposition \(X\simeq Y\times Z\) with \(Y,Z\) positive-dimensional connected smooth proper complex Deligne--Mumford stacks. More generally, the rational cohomology of \(X\) cannot be the Künneth tensor product of the rational cohomologies of two such positive-dimensional factors.

## Assumptions and scope
The statement concerns the complex fine compactified universal Jacobian of type \((2,1)\) considered in arXiv:2610.01829v1. It uses only the rational Betti numbers computed there and the Künneth theorem. The conclusion rules out genuine products of positive-dimensional connected smooth proper complex Deligne--Mumford stacks, and therefore also products of smooth proper complex varieties. It does not claim that \(X\) is indecomposable under birational maps, fibrations, correspondences, semiorthogonal decompositions, or motives.

## Proof
Reduce \(B_X\) modulo \(3\). Since \(5\equiv2\), \(15\equiv0\), and \(20\equiv2\pmod3\), we obtain
\[
\overline B(t)=t^6+2t^5+2t^3+2t+1\in\mathbf F_3[t].
\]
The accompanying exact checker applies the standard finite-field irreducibility criterion for a monic polynomial of degree \(6\): it verifies
\[
t^{3^6}\equiv t\pmod{\overline B},
\]
and, for the prime divisors \(2,3\) of \(6\),
\[
\gcd\bigl(\overline B,t^{3^3}-t\bigr)=1,
\qquad
\gcd\bigl(\overline B,t^{3^2}-t\bigr)=1.
\]
Hence \(\overline B\) is irreducible over \(\mathbf F_3\), so Gauss's lemma implies that \(B_X\) is irreducible over \(\mathbf Z\) and \(\mathbf Q\).

Suppose, toward a contradiction, that \(X\) had the rational cohomology of a product \(Y\times Z\), where \(Y\) and \(Z\) are connected smooth proper complex Deligne--Mumford stacks of positive dimension. By Künneth, the ordinary Poincaré polynomial factors as \(P_X(s)=P_Y(s)P_Z(s)\). Since \(P_X\) has no odd-degree terms and all Betti numbers are nonnegative, neither factor can have odd rational cohomology: any odd Betti number of one factor would already contribute a positive odd coefficient after multiplication by the other factor's \(b_0=1\). Thus
\[
P_Y(s)=B_Y(s^2),\qquad P_Z(s)=B_Z(s^2)
\]
for nonconstant polynomials \(B_Y,B_Z\in\mathbf Z_{\ge0}[t]\); nonconstancy follows from positive dimension and Poincaré duality. Therefore
\[
B_X(t)=B_Y(t)B_Z(t),
\]
contradicting irreducibility. This proves the claimed rational product-indecomposability.

## Verification
`verify.py` implements polynomial arithmetic over \(\mathbf F_3\) with the Python standard library only. It reconstructs \(\overline B\), checks the two required gcd conditions and the degree-six Frobenius condition, and independently checks that the source Betti vector produces the stated polynomial. The recorded output in `VERIFY.txt` ends with `VERIFY_OK`.

The scientific input from arXiv:2610.01829v1 is the exact Tate-type Hodge--Euler polynomial of \(\overline J_{2,1}\). The finite-field irreducibility proof and the Künneth obstruction are proved here.

## Relationship to prior work
Fava computes the rational cohomology and rational Chow groups of \(\overline J_2\) and \(\overline J_{2,1}\), and his Lemma 3.1 exhibits genuine relative product decompositions for compactified Jacobians over curves obtained by gluing along a separating node. The paper does not state an irreducibility result for the global Poincaré polynomial or a global product-indecomposability theorem; targeted full-text searches for “irreducible”, “Poincaré”, and product language reveal the cohomology calculation and stratum-wise product constructions but no implication-equivalent global statement.

Pagani--Tommasi compute genus-one fine compactified universal Jacobian cohomology, while Fava--Pagani--Viviani classify compactified universal Jacobians. These works supply surrounding geometry but do not determine the above genus-two one-pointed product obstruction. Targeted web and published-finding searches for the exact Betti polynomial, product decomposition, cohomological product, and irreducibility produced no covering statement.

## Limitations
Irreducibility of \(B_X\) is an obstruction only to products whose rational cohomology satisfies Künneth with nonnegative Betti numbers, as it does for the stated smooth proper factors. The argument does not rule out nontrivial fibrations, finite covers, birational product structures, or motivic factorizations. It also does not assert the analogous statement for \(\overline J_2\); its reduced even Poincaré polynomial is reducible.

## References
1. Marco Fava, *Cohomology of the fine compactified universal Jacobians \(\overline J_2\) and \(\overline J_{2,1}\)*, arXiv:2610.01829v1, 1 October 2026.
2. Nicola Pagani and Orsola Tommasi, *Geometry of Genus One Fine Compactified Universal Jacobians*, International Mathematics Research Notices 2023, no. 10, 8495--8543, DOI 10.1093/imrn/rnac094.
3. Marco Fava, Nicola Pagani, and Filippo Viviani, *A complete classification of modular compactifications of the universal Jacobian*, arXiv:2603.05455.
