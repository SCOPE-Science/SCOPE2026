# Exact singular hyperplane in the \(321654\) regular-nilpotent Hessenberg–Schubert cell
## Finding
Let \(N\) be the principal nilpotent endomorphism of \(\mathbb C^6\), let \(h=(3,4,5,6,6,6)\), and let \(w=321654\). In the Hessenberg–Schubert cell \(C=\operatorname{Hess}(N,h)\cap X_w^\circ\cong\mathbb A^6\) with the coordinates used in Abe–Insko Example 4.10, \(z_{12},z_{45},z_{13},z_{46},z_{23},z_{56}\), the singular points are exactly \[C\cap\operatorname{Sing}(\operatorname{Hess}(N,h))=V_C(z_{12}-z_{23}-z_{45}+z_{56}).\] At every point of this hyperplane the local defining Jacobian has rank exactly \(5\), while off the hyperplane it has rank \(6\). Thus the source's displayed dense open smooth set is the full smooth locus inside this cell, and the cell contains non-permutation singular points.

## Assumptions and scope
Work over \(\mathbb C\). Let \(N\) be the \(6\times6\) principal nilpotent matrix with ones on the superdiagonal. Let \(h=(3,4,5,6,6,6)\) and \(w=321654\). Write \(P_w\) for the permutation matrix of \(w\), and let \(U=(u_{ij})\) be lower unitriangular. The standard affine chart \(wU^-\) is represented by \(g=P_wU\). The Hessenberg equations on this chart are the six entries of \(g^{-1}Ng\) in positions \( (4,1),(5,1),(6,1),(5,2),(6,2),(6,3)\), because these are exactly the pairs with row index larger than \(h\) of the column index.

The source's Schubert cell is obtained by setting all lower-unitriangular coordinates to zero except
\[
 u_{21}=z_{23},\quad u_{31}=z_{13},\quad u_{32}=z_{12},\quad
 u_{54}=z_{56},\quad u_{64}=z_{46},\quad u_{65}=z_{45}.
\]
Abe–Insko verify that this entire Schubert cell lies in \(\operatorname{Hess}(N,h)\), so it is an affine \(6\)-space with these free coordinates. Their local defining ideal is radical, and the ambient chart has dimension \(15\) while \(\operatorname{Hess}(N,h)\) has dimension \(9\); hence smoothness on the chart is equivalent to Jacobian rank \(6\).

## Proof
Let \(J_C\) be the Jacobian of the six local equations after restriction to the cell. All columns vanish except those indexed by
\[
(u_{41},u_{42},u_{43},u_{51},u_{52},u_{53},u_{62},u_{63}).
\]
In that column order, exact differentiation gives
\[
J_C=
\begin{pmatrix}
0&-1&z_{12}-z_{23}&0&0&0&0&0\\
1&z_{56}&z_{56}(-z_{12}+z_{23})&0&-1&z_{12}-z_{23}&0&0\\
-z_{45}&-z_{45}z_{56}+z_{46}&(z_{12}-z_{23})(z_{45}z_{56}-z_{46})&1&z_{45}&z_{45}(-z_{12}+z_{23})&-1&z_{12}-z_{23}\\
0&1&z_{56}&0&0&-1&0&0\\
0&-z_{45}&-z_{45}z_{56}+z_{46}&0&1&z_{45}&0&-1\\
0&0&-z_{45}&0&0&1&0&0
\end{pmatrix}.
\]
Set
\[
\Delta=z_{12}-z_{23}-z_{45}+z_{56}.
\]
Among the \(6\times6\) minors of \(J_C\), exactly seven are nonzero as polynomials. Their distinct values, up to sign, are \(\Delta\) and \((z_{12}-z_{23})\Delta\). In particular, one maximal minor is exactly \(\Delta\), while every maximal minor is divisible by \(\Delta\). Therefore \(\operatorname{rank}J_C=6\) if and only if \(\Delta\neq0\).

To rule out any further rank drop on \(\Delta=0\), take the first five equation rows and the columns \(u_{41},u_{42},u_{51},u_{52},u_{53}\). The determinant of this \(5\times5\) minor is identically \(1\). Hence \(\operatorname{rank}J_C\ge5\) everywhere, and on \(\Delta=0\) the rank is exactly \(5\). The Jacobian criterion now gives the asserted equality of the singular intersection with the hyperplane \(V_C(\Delta)\).

For an explicit non-permutation singular point, take \(z_{12}=z_{23}=1\) and \(z_{45}=z_{56}=z_{13}=z_{46}=0\). Then \(\Delta=0\), and the reconstructed Jacobian has rank \(5\).

## Verification
The bundled `verify.py` reconstructs \(g=P_wU\), forms \(g^{-1}Ng\) exactly, extracts the six Hessenberg equations, differentiates them symbolically, restricts to the source's six-dimensional Schubert cell, enumerates every potentially nonzero maximal minor, and checks the constant \(5\times5\) minor. It also checks one explicit singular point and one explicit smooth point. The script uses exact symbolic arithmetic and terminates with `VERIFY_OK`.

The proof does not infer an infinite statement from sampled points: the decisive steps are polynomial identities for all maximal minors and an identically constant lower-rank minor.

## Relationship to prior work
Abe–Insko, Example 4.10, introduces exactly this \(h\), \(w\), affine cell, and Jacobian. The displayed \(3\times3\) subdeterminant is \(\Delta\), so their argument proves that the open subset \(\Delta\neq0\) is smooth and concludes that generic points of the cell are nonsingular. The computation above supplies the missing converse: every point with \(\Delta=0\) is singular. Thus the exact singular intersection is an affine hyperplane \(\mathbb A^5\), not merely the permutation flag. The prose immediately before the example says “the rest of the points in the cell are nonsingular,” but the example's actual calculation and concluding sentence establish only generic nonsingularity; the maximal-minor calculation resolves that discrepancy.

Horiguchi–Shirato later give explicit singular loci for intersections of regular nilpotent Hessenberg varieties with the open opposite Schubert cell for the special family \(h_m=(m,n,\ldots,n)\). Their theorem does not apply to \(h=(3,4,5,6,6,6)\) or to the Schubert cell indexed by \(321654\).

## Limitations
The statement is only about the intersection of the global singular locus with this one named Hessenberg–Schubert cell. It does not classify the full singular locus of \(\operatorname{Hess}(N,h)\), its irreducible components, or the analytic singularity type transverse to the hyperplane. No claim is made for other Hessenberg functions or permutations. Literature searches cannot exclude an uncatalogued equivalent computation.

## References
- H. Abe and E. Insko, *On singularity and normality of regular nilpotent Hessenberg varieties*, arXiv:2212.13817v1, especially Proposition 3.3, Proposition 4.7, and Example 4.10; later published in *Journal of Algebra*, DOI:10.1016/j.jalgebra.2024.02.042.
- T. Horiguchi and T. Shirato, *Coordinate rings of regular nilpotent Hessenberg varieties in the open opposite Schubert cell*, arXiv:2302.06041v1; later published in *Forum of Mathematics, Sigma*, DOI:10.1017/fms.2024.142.
