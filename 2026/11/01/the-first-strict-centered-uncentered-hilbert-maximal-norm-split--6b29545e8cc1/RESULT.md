# The first strict centered–uncentered Hilbert maximal-norm split occurs on the four-vertex path

## Finding
Let \(G\) be a finite connected simple graph, with counting measure on its vertices and graph-distance balls. Write \(M_c\) for centered and \(M_u\) for uncentered maximal averages of \(|f|\), and \(\|T\|_{2\to2}:=\sup_{f\ne0}\|Tf\|_2/\|f\|_2\). On every connected graph with at most three vertices their strong \(\ell^2\) norms agree.

On the four-vertex path \(P_4=0-1-2-3\), let \(\lambda_u\) be the unique real root in \((1.632,1.633)\) of
\[
324z^4-702z^3+308z^2-42z+1=0,
\]
and let \(\lambda_c\) be the unique real root in \((1.603,1.604)\) of
\[
36z^3-78z^2+35z-4=0.
\]
Then the exact, attained strong norms satisfy
\[
\boxed{\|M_u\|_{2\to2}=\sqrt{\lambda_u}\approx1.2775761248040804
\quad>\quad
\|M_c\|_{2\to2}=\sqrt{\lambda_c}\approx1.266333300268983.}
\]
Thus order four is the smallest graph order permitting a strict centered–uncentered *norm* separation.

Both sets of nonzero extremizers are classified up to path reflection, positive multiplication, and independent coordinate signs. Write \(A_u\) and \(A_c\) as below, and let \(v_u\) and \(v_c\) be their unique positive right top singular vectors, normalized by coordinate \(1\) equal to one. The absolute values of all extremizers for \(M_u\) are positive multiples of either \(v_u\) or its reversal; the analogous statement holds for \(M_c\) and \(v_c\). Explicitly,
\[
A_u=\begin{pmatrix}1/2&1/2&0&0\\0&1&0&0\\1/3&1/3&1/3&0\\0&1/3&1/3&1/3\end{pmatrix},\qquad
A_c=\begin{pmatrix}1/2&1/2&0&0\\0&1&0&0\\0&1/3&1/3&1/3\\0&1/3&1/3&1/3\end{pmatrix}.
\]
The normalized positive vectors have exact coordinates
\[
v_u=(\frac{117\lambda_u^2-31\lambda_u+1}{Q},1,
\frac{\lambda_u(72\lambda_u-17)}{Q},
\frac{(4\lambda_u-1)(9\lambda_u-1)}{Q}),
\quad Q=324\lambda_u^3-225\lambda_u^2+39\lambda_u-1,
\]
\[
v_c=(\frac1{4\lambda_c-1},1,\frac2{9\lambda_c-4},\frac2{9\lambda_c-4}).
\]
All coordinates are strictly positive. In particular, the uncentered norming profile is asymmetric, beyond mere reflection.

## Assumptions and scope
Vertices are indexed in path order and carry unit masses; an edge is present precisely between consecutive indices. A ball is \(B(a,r)=\{j:d_G(a,j)\le r\}\) for a vertex center \(a\) and radius \(r\ge0\). Only distinct vertex subsets matter. In \(M_c\), the center is the evaluation vertex; in \(M_u\), the ball may have any center but must contain the evaluation vertex. Averages use \(|f|\). Input and output use unnormalized counting \(\ell^2\), equivalent for the operator ratio to normalized counting on the same vertex set. Graphs are connected and nonempty, and there are no extra intervals or weighted masses.

For \(P_4\), the complete list of distinct balls is
\[
\{0\},\{1\},\{2\},\{3\},\{0,1\},\{2,3\},\{0,1,2\},\{1,2,3\},\{0,1,2,3\}.
\]
The interval \(\{1,2\}\) is **not** a graph-metric ball. This distinction is essential.

## Proof
**Finite positive linearization.** At each vertex choose one eligible ball, independently, and form a matrix whose row is that ball's normalized indicator. For the finite family \(\mathcal A\) of such nonnegative matrices, and any nonnegative vector \(x\),
\[
\|Mx\|_2^2=\max_{A\in\mathcal A}\|Ax\|_2^2.
\]
For any nonnegative matrix \(A\), replacing a real test vector by its absolute values does not decrease \(\|Ax\|_2\). Therefore
\[
\boxed{\|M\|_{2\to2}^2=\max_{A\in\mathcal A}\lambda_{\max}(A^{\mathsf T}A).}
\]
This identity reduces the nonlinear norm problem exactly to finitely many rational symmetric matrices; it is not an approximation.

**Exhaustive rational spectral bound.** For \(P_4\), centered ball choices at the four vertices have respective counts \(4,3,3,4\), giving \(144\) matrices. Uncentered choices have counts \(4,5,5,4\), giving \(400\) matrices. Among the uncentered matrices, the only two whose largest squared singular value exceeds \(13/8\) are \(A_u\) and its simultaneous row/column reflection; for each of the other \(398\), the four leading principal minors of \((13/8)I-A^{\mathsf T}A\) are strictly positive. Among the centered matrices, the only two exceeding \(8/5\) are \(A_c\) and its reflected matrix; the other \(142\) matrices have all four leading principal minors of \((8/5)I-A^{\mathsf T}A\) strictly positive. By Sylvester's criterion these inequalities bound *all* excluded squared norms strictly below the corresponding rational thresholds.

For the two exceptional pairs, direct rational determinant expansion gives
\[
\det(zI-A_u^{\mathsf T}A_u)=\frac{324z^4-702z^3+308z^2-42z+1}{324},
\]
\[
\det(zI-A_c^{\mathsf T}A_c)=\frac{z(36z^3-78z^2+35z-4)}{36}.
\]
Exact Sturm root counts show precisely one root above \(13/8\) in the first case and precisely one above \(8/5\) in the second. Rational Rayleigh test vectors, respectively \((3/10,1,19/100,9/100)\) and \((19/100,1,19/100,19/100)\), certify that their top squared singular values exceed these thresholds. The same root count isolates them in the stated disjoint rational intervals. Hence \(\|M_u\|^2=\lambda_u\) and \(\|M_c\|^2=\lambda_c\), and the strict gap follows immediately.

**All extremizers.** Each winning Gram matrix is irreducible and entrywise nonnegative, so its Perron top eigenvalue is simple and has a unique positive eigenvector up to scale. Solving three of the four linear eigenvector equations yields the displayed formulas; the fourth reduces exactly to the defining characteristic polynomial. If \(f\) is an extremizer, select at each vertex a ball that realizes \(M|f|\). Equality in the preceding spectral estimate forces that selection to be one of the two exceptional matrices and \(|f|\) to be its positive top eigenvector. Conversely the positive top eigenvector of a winning matrix attains the nonlinear norm, because \(M|f|\ge A|f|\) componentwise and no matrix has a larger norm. Signs of \(f\) are unrestricted because the operator depends on \(|f|\).

**Minimality in graph order.** On one or two vertices the centered and uncentered families coincide pointwise. Up to isomorphism, the connected three-vertex graphs are the triangle and the path. The triangle again has identical ball families. On the three-vertex path, the uncentered and centered families give respectively \(36\) and \(18\) rational selection matrices. In both families the sole matrix whose squared norm exceeds \(3/2\) has rows averaging \(\{0,1\},\{1\},\{1,2\}\). For all other matrices \((3/2)I-A^{\mathsf T}A\) is rational positive definite by the same principal-minor test. Its characteristic polynomial is \((4z-1)(4z^2-7z+1)/16\), proving
\[
\|M_{u,P_3}\|_{2\to2}^2=\|M_{c,P_3}\|_{2\to2}^2=\frac{7+\sqrt{33}}8.
\]
Thus no smaller connected graph can separate these operator norms.

## Verification
The attached standalone program `checker.py` constructs ball sets directly from shortest-path distances, enumerates all \(36+18+400+144=598\) row-selection matrices without omission, checks every claimed strict principal-minor inequality using exact rational arithmetic, calculates both exceptional characteristic polynomials, verifies rational Rayleigh witnesses, and isolates the roots by exact Sturm counts. It outputs `CERTIFICATE_OK`. The executable proof is finite and exhaustive because the mathematical domains are finite; no sampled inputs or numerical eigenvalues are used in the certificate. A separate numeric diagonalization is only for the displayed decimal approximations.

## Relationship to prior work
Soria and Tradacete (arXiv:1410.6204, originally posted October 22, 2014), Example 2.6(i), calculate the \(\ell^1\) norm of the centered operator on the four-vertex path, denoted \(L_4\) there. Their result is not a strong \(\ell^2\) calculation, and their other four-vertex graph called \(P_4\) is not the four-vertex path in the present notation. González-Riquelme and Madrid (arXiv:2005.03146, originally posted May 6, 2020), §3, obtain sharp strong \(\ell^2\) constants for centered operators on complete graphs and stars, not for the path of four vertices or its uncentered operator. Their §1 explicitly defines the uncentered graph-ball variant. These known results motivate the question but do not imply either new path constant or the first-order separation. Closely related previously established centered cycle and biclique norms also concern different metric-ball families. The searches reported in REVIEW.md and AUDIT.json found no published equivalent statement, but non-indexed calculations cannot be excluded.

## Limitations
This theorem is restricted to unweighted connected simple graphs, counting measure, four-vertex-path sharp constants, and the proof of minimal *vertex order* of a strict norm split. It does not classify all four-vertex graphs showing a split, weighted graph norms, longer paths, uncentered maximal operators defined over arbitrary intervals, or \(\ell^p\) exponents other than two. Independent audit is not performed; priority relative to unindexed sources remains uncertain.

## References
1. J. Soria and P. Tradacete, *Best constants for the Hardy–Littlewood maximal operator on finite graphs*, arXiv:1410.6204v1 (2014-10-22), https://arxiv.org/abs/1410.6204.
2. C. González-Riquelme and J. Madrid, *Sharp inequalities for maximal operators on finite graphs*, arXiv:2005.03146v1 (2020-05-06), https://arxiv.org/abs/2005.03146.
