# Two Frobenius-splitting types and a maximal Weddle K3 surface over sixteen elements

## Finding

Over \(k=\mathbb F_{16}=\mathbb F_2[\theta]/(\theta^4+\theta+1)\), the two characteristic-two Weddle quartics specified below have six rational nodes and a seventh rational singularity of type \(D_4\), yet their smooth K3 resolutions have different point counts:
\[
\#X_{-}(k)=545,\qquad \#X_{+}(k)=609.
\]
The second is maximal, since \(609=16^2+22\cdot16+1\). The local distinction is arithmetic: the three outer curves in the \(D_4\) resolution form one rational component plus a conjugate pair in the first example, but all three are rational in the second.

## Assumptions and scope

Use homogeneous coordinates \([x:y:z:w]\) and define, for \(\mathbf a=(a,b,c,d)\),
\[
 W_{\mathbf a}=V\left(\det\begin{pmatrix}ayzw&x&1&a\\bxzw&y&1&b\\cxyw&z&1&c\\dxyz&w&1&d\end{pmatrix}\right)\subset\mathbb P^3_k.
\]
The field elements are represented by integers from \(0\) to \(15\), with bit \(i\) denoting the coefficient of \(\theta^i\); multiplication is reduced modulo \(\theta^4+\theta+1\). The two parameter vectors in this encoding are \((1,8,2,7)\) and \((3,11,1,15)\). Their entries are nonzero and pairwise distinct. The six marked points are the four coordinate vertices, \([1:1:1:1]\), and \([a:b:c:d]\); every four are linearly independent, as checked in the accompanying exact verifier. The minimal desingularizations are K3 surfaces by the characteristic-two Weddle theorem of Dolgachev [2]. This is an explicit existence and arithmetic-splitting result, not a complete family classification or determination of all zeta factors.

## Proof

**Singularities.** The determinantal Weddle model with six points in linear general position has six ordinary double points at the marked vertices and an additional \(D_4\) rational double point at
\[P=[\sqrt a:\sqrt b:\sqrt c:\sqrt d].\]
These geometric identifications are established for characteristic two in [2, Section 2]. Since \(k\) is perfect, all seven singular points are \(k\)-rational. The six node exceptional fibers are smooth projective conics over a finite field, hence each has \(17\) rational points and changes the point count by \(16\).

**Local splitting of the \(D_4\).** Write the affine expansion at \(P\), holding the fourth coordinate constant, in local parameters \(u,v,r\). The degree-two piece is the square of a linear form \(L\). For the first surface, the coefficients of \(L\) in the above field encoding are \((11,11,14)\); for the second they are \((9,2,2)\). On \(L=0\), use \(v=s,r=t\) and solve for \(u\). The degree-three homogeneous piece restricts to the binary cubics
\[
B_-(s,t)=2s^3+4s^2t+3st^2+9t^3,
\qquad B_+(s,t)=4s^2t+2st^2,
\]
where integer coefficients denote field elements, not ordinary integers in characteristic zero. In this notation,
\[
B_-=(t+15s)(9t^2+13st+3s^2),\qquad
B_+=2st(2s+t).
\]
The quadratic factor of \(B_-\) has no root in \(k\) and is separable; the three roots of \(B_+\) are \([1:0]\), \([1:2]\) and \([0:1]\). Thus the first cubic has exactly one rational geometric root and the second has three, and both cubics are squarefree over an algebraic closure.

For a \(D_4\) double-plane tangent cone in characteristic two, write the local equation as \(L^2+B_3+B_4=0\). In the blow-up of its singular point, near the reduced exceptional line the strict transform has equation \(Z^2+\rho B_3|_{L=0}+O(\rho^2)=0\). Each simple projective root of \(B_3|_{L=0}\) gives one ordinary node on the first blow-up, whose resolution adds one outer exceptional \(\mathbb P^1\). The reduced exceptional line becomes the central exceptional \(\mathbb P^1\). Frobenius permutes the three arms as it permutes the binary cubic roots. If \(n\) arms are rational, the fiber over the original \(D_4\) point has exactly \((16+1)+16n\) rational points: the central line gives \(17\), and each rational outer line contributes \(16\) new points after its intersection with the central line is counted. Nonrational conjugate arms do not contribute additional rational points.

**Exact projective enumeration.** The accompanying Python program expands the displayed determinant coefficientwise over \(k\). It independently evaluates the original determinant and the expanded quartic at every point of \(\mathbb P^3(k)\), enumerating each of its \(16^3+16^2+16+1=4369\) points exactly once by normalizing the first nonzero homogeneous coordinate to \(1\). Both methods give
\[
\#W_-(k)=417,\qquad\#W_+(k)=449.
\]
With \(n_-=1\) and \(n_+=3\), the resolution correction is \(6\cdot16+(1+n)\cdot16\), hence
\[
\#X_-(k)=417+96+32=545,
\qquad \#X_+(k)=449+96+64=609.
\]
For a smooth K3 surface over \(\mathbb F_{16}\), \(H^1\) and \(H^3\) vanish and the 22 eigenvalues on \(H^2\) have complex absolute value 16; therefore \(\#X(k)\le16^2+1+22\cdot16=609\). The second example attains this bound.

## Verification

Run `python verify_weddle16.py` with Python 3 and no external packages. The program tests general linear position for all fifteen four-point subsets, expands the quartic determinant, reproduces all \(4369\) evaluations by two algebraically independent representations (matrix determinant and expanded polynomial), checks the local tangent square and two binary cubics, counts their rational roots, and prints the two resolution totals. All field calculations use exact four-bit polynomial arithmetic. The script does not by itself prove the standard geometric fact about \(D_4\) exceptional configurations; that fact is used in the preceding local blow-up argument and [2].

## Relationship to prior work

Bolognesi [1] develops classical Weddle surfaces and their moduli interpretation. Dolgachev [2, Section 2] gives precisely the determinantal equation, characteristic-two exceptional \(D_4\) singularity, and K3 resolution; these are premises, not new discoveries. The new information here is an explicit pair of finite-field forms with different Frobenius splitting of the exceptional arms and distinct exact rational-point counts, including one maximal K3 surface. The earlier same-object computation of the local Jacobian scheme at the Cremona-fixed point determines a length-eight local algebra but does not determine the Frobenius action on the resolution or either rational-point count. The specific arithmetic comparison was not established in inspected primary texts or the actual mathematical-record searches; this is not an unconditional historical uniqueness claim.

## Limitations

The argument is for the two specified vectors over \(\mathbb F_{16}\). It does not classify all point counts or splitting types of the Weddle family. The point count alone does not determine the full zeta function of the nonmaximal surface. Historical descriptions under alternative names or in unavailable full texts could overlap; no independent audit has been performed.

## References

[1] M. Bolognesi, *On Weddle Surfaces and Their Moduli*, arXiv:math/0601251, initially public 2006-01-11; subsequently *Advances in Geometry* 7 (2007), DOI 10.1515/ADVGEOM.2007.008.

[2] I. Dolgachev, *K3 surfaces of Kummer type in characteristic two*, *Bulletin of the London Mathematical Society* (2024), DOI 10.1112/blms.13033, especially Section 2.
