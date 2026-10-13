# Maximal abelian quotients of three icosahedral Galois-point plane curves

## Finding
Let \(C_d\subset\mathbf P^2_{\mathbf C}\), for \(d\in\{12,20,30\}\), be the three smooth icosahedral plane curves
\[
C_d:\quad Z^d+F_d(X,Y)=0,
\]
where \(F_{12},F_{20},F_{30}\) are the binary-icosahedral invariant forms used by Harui, Miura and Ohbuchi. Write \(G_d=\operatorname{Aut}(C_d)\) and \(D_d=[G_d,G_d]\). Then
\[
D_d\cong\operatorname{SL}(2,5)
\]
for all three degrees. Consequently the maximal abelian quotient curves \(Y_d=C_d/D_d\) have
\[
(g(Y_{12}),g(Y_{20}),g(Y_{30}))=(1,2,4).
\]
More precisely, \(G_d/D_d\cong C_{d/2}\), and the induced cyclic maps \(Y_d\to C_d/G_d\cong\mathbf P^1\) have exactly three branch points with ramification indices
\[
(2,3,6),\qquad(2,5,10),\qquad(3,5,15)
\]
for \(d=12,20,30\), respectively.

## Assumptions and scope
The ground field is \(\mathbf C\). The curves and invariant forms are exactly those in Theorem 5 of Harui--Miura--Ohbuchi. The claim concerns the coarse smooth quotient curves by the abstract commutator subgroup of the full automorphism group. It does not identify explicit affine equations for \(Y_d\), nor does it claim a complete isogeny decomposition of \(\operatorname{Jac}(C_d)\).

## Proof
Harui--Miura--Ohbuchi determine
\[
G_{30}\cong C_{15}\times\operatorname{SL}(2,5),
\]
\[
G_{20}\cong C_5\times(\operatorname{SL}(2,5)\rtimes C_2),\qquad
G_{12}\cong C_3\times(\operatorname{SL}(2,5)\rtimes C_2).
\]
Because \(\operatorname{SL}(2,5)\) is perfect, the commutator subgroup in every case is exactly its normal \(\operatorname{SL}(2,5)\) factor. Hence
\[
G_{12}/D_{12}\cong C_6,\qquad G_{20}/D_{20}\cong C_{10},\qquad G_{30}/D_{30}\cong C_{15}.
\]

The outer-Galois-point subgroup \(N_d\cong C_d\) is normal and the reduced group is \(G_d/N_d\cong A_5\). The zeros of \(F_d\) are one of the three exceptional \(A_5\)-orbits on \(\mathbf P^1\): their sizes are \(12,20,30\), so their point stabilizers have orders \(5,3,2\), respectively. Obus--Shaska's treatment of the same binary-icosahedral superelliptic forms confirms that the full quotient has exactly three branch values. At the branch value coming from the zeros of \(F_d\), the inertia group contains \(N_d\) and has order
\[
d\cdot(60/d)=60.
\]
The two other branch values lie over the other two exceptional orbit types of \(A_5\).

It remains to determine their full inertia orders. Since \(C_d\) is a smooth plane curve, \(g(C_d)=(d-1)(d-2)/2\), namely \(55,171,406\). The full quotient has degree \(|G_d|=60d\). Riemann--Hurwitz, with one inertia order already equal to \(60\), forces the remaining two orders to be \(2,3\) for \(d=12\), \(2,5\) for \(d=20\), and \(3,5\) for \(d=30\); these are also the only possibilities dividing the two remaining \(A_5\)-stabilizer orders.

Now factor the full quotient through \(Y_d=C_d/D_d\). Since \(D_d\cong\operatorname{SL}(2,5)\) maps onto \(A_5\) with central kernel of order \(2\),
\[
|N_d\cap D_d|=2.
\]
Thus the image of \(N_d\) in \(G_d/D_d\) has order \(d/2\), so the order-\(60\) full inertia group maps onto the entire residual cyclic group. The other two inertia images have orders dividing the coprime pairs \( (2,3)\), \( (2,5)\), or \( (3,5)\). Their product with a generator from the special inertia is the identity. In a cyclic group of order equal to the product of those two coprime integers, this forces the two remaining images to have their full respective orders. Hence the residual signatures are exactly
\[
(2,3,6),\quad(2,5,10),\quad(3,5,15).
\]
A final Riemann--Hurwitz computation gives \(2g(Y_d)-2=0,2,6\), hence genera \(1,2,4\).

## Verification
The accompanying checker verifies all numerical steps exactly with rational arithmetic: the plane-curve genera and full group orders, uniqueness of the two nonspecial full inertia orders from Riemann--Hurwitz, the coprime-order forcing in the residual cyclic quotient, and the three quotient genera. The non-numerical inputs are the published group structures, normal cyclic outer-Galois-point subgroup, reduced \(A_5\) action, and three-branch property described in the cited sources.

## Relationship to prior work
Harui--Miura--Ohbuchi determine the three full automorphism groups and their cyclic outer-Galois-point kernels, but do not state the quotient by the commutator subgroup or its genus. Obus--Shaska place the same degree-\(12\), degree-\(20\) and degree-\(30\) binary-icosahedral superelliptic forms among the three-branch curves with many automorphisms; that supplies a direct literature check on the three-branch geometry, but they do not identify the maximal abelian quotient curves above. Harui--Kato--Komeda--Ohbuchi study cyclic quotients \(C/\langle\sigma\rangle\) of smooth plane curves; their results do not cover the noncyclic commutator subgroup \(\operatorname{SL}(2,5)\). The later classification of Badr--Harui recovers the same \(A_5\)-reduced automorphism setting without stating these commutator quotients.

## Limitations
No explicit equations for the genus-\(1\), genus-\(2\) or genus-\(4\) quotient curves are supplied. The argument is over \(\mathbf C\) and uses the exact characteristic-zero automorphism groups from the source. A residual originality risk is that older subgroup-signature tables for icosahedral curves may encode these three intermediate quotients in different notation.

## References
1. T. Harui, K. Miura, A. Ohbuchi, *Automorphism group of plane curve computed by Galois points, II*, arXiv:1709.05025; Proc. Japan Acad. Ser. A Math. Sci. 94 (2018), 59--63.
2. A. Obus, T. Shaska, *Superelliptic curves with many automorphisms and CM Jacobians*, arXiv:2006.12685; Math. Comp. 90 (2021), 2951--2975.
3. T. Harui, T. Kato, J. Komeda, A. Ohbuchi, *Quotient curves of smooth plane curves with automorphisms*, Kodai Math. J. 33 (2010), 164--172, doi:10.2996/kmj/1270559164.
4. E. Badr, T. Harui, *Smooth plane curves with a unique outer Galois point and their automorphism groups*, arXiv:2603.26180.
