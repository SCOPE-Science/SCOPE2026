# Rank-one TCP cores detect toroidal correlations exactly
## Finding
For every integer \(d\ge 2\) and every \(d\times d\) complex correlation matrix \(Z\),
\[
\left(J_d/d,\,J_d/d,\,Z/d\right)\in\mathrm{TCP}_d
\quad\Longleftrightarrow\quad
Z\text{ is toroidal}.
\]
Here \(J_d\) is the all-ones matrix, and toroidal means that
\[
Z=\sum_k p_k u_k u_k^*,\qquad p_k\ge 0,\qquad \sum_k p_k=1,\qquad |(u_k)_j|=1.
\]
For the four-dimensional DOC family \(\Phi_{a,Z}\) introduced in arXiv:2609.32979v1, the endpoint \(a=1\) therefore satisfies
\[
\Phi_{1,Z}\text{ is entanglement breaking}
\quad\Longleftrightarrow\quad
Z\text{ is toroidal}.
\]
Thus the endpoint is not uniformly entanglement breaking and not uniformly non-entanglement-breaking; it splits exactly along the toroidal correlation set.

An explicit non-toroidal endpoint witness is
\[
Z_*=
\begin{pmatrix}
1&0&1/\sqrt2&1/\sqrt2\\
0&1&1/\sqrt2&i/\sqrt2\\
1/\sqrt2&1/\sqrt2&1&(1+i)/2\\
1/\sqrt2&-i/\sqrt2&(1-i)/2&1
\end{pmatrix}.
\]
It has rank \(2\), is an extreme point of the four-dimensional correlation set, and hence is not toroidal. Therefore \(\Phi_{1,Z_*}\) is bistochastic and PPT but not entanglement breaking.

## Assumptions and scope
A complex correlation matrix is positive semidefinite with unit diagonal. A toroidal correlation matrix is a convex combination of rank-one correlation matrices \(u u^*\) with all coordinates of \(u\) unimodular. Triplewise complete positivity uses the convention
\[
A=(V\odot\overline V)(W\odot\overline W)^*,\qquad
B=(V\odot W)(V\odot W)^*,\qquad
C=(V\odot\overline W)(V\odot\overline W)^*.
\]
The TCP cone is homogeneous, so multiplying all three matrices by the same positive scalar does not change membership after the corresponding rescaling of \(V\) and \(W\). The DOC entanglement-breaking/TCP equivalence and the parametrization of \(\Phi_{a,Z}\) are those used in arXiv:2609.32979v1.

## Proof
It is enough to prove
\[
(J_d,J_d,Z)\in\mathrm{TCP}_d
\quad\Longleftrightarrow\quad
Z\text{ is toroidal}.
\]
Suppose first that \(Z\) is toroidal. The all-ones matrix \(J_d\) is itself a rank-one toroidal correlation matrix. Applying the toroidal TCP-core construction with \(p=(1,\ldots,1)^T\), \(R=J_d\), and \(S=Z\) yields \((J_d,J_d,Z)\in\mathrm{TCP}_d\).

Conversely, assume that \((J_d,J_d,Z)\) has a TCP factorization with column pairs \(v_k,w_k\). Put
\[
z_k=v_k\odot w_k,\qquad y_k=v_k\odot\overline{w_k}.
\]
Then
\[
J_d=\sum_k z_k z_k^*,\qquad Z=\sum_k y_k y_k^*.
\]
Because \(J_d\) has rank one, each \(z_k\) lies in \(\operatorname{span}\{\mathbf 1\}\). Indeed, if \(x\perp\mathbf 1\), then
\[
0=x^*J_dx=\sum_k |x^*z_k|^2,
\]
so \(x^*z_k=0\) for every \(k\). Hence \(z_k=c_k\mathbf 1\) for scalars \(c_k\). Coordinatewise,
\[
|(y_k)_j|=|(v_k)_j|\,|(w_k)_j|=|(z_k)_j|=|c_k|.
\]
If \(c_k=0\), then \(y_k=0\). Otherwise write \(y_k=|c_k|u_k\), where every coordinate of \(u_k\) has modulus one. Since \(Z\) has unit diagonal,
\[
1=Z_{jj}=\sum_k |c_k|^2
\]
for every \(j\). Consequently
\[
Z=\sum_k |c_k|^2u_ku_k^*
\]
is a toroidal decomposition. This proves the equivalence for every \(d\ge2\).

At \(a=1\), the source family has \(r_1=1\), \(s_1=4\), and \(M_1=J_4\). Therefore
\[
(A_1,B_1,C_{1,Z})=(J_4/4,J_4/4,Z/4).
\]
The source establishes that every member of this family is trace preserving, unital, and PPT, and that DOC entanglement breaking is equivalent to TCP. The general equivalence above therefore gives the endpoint criterion.

It remains to certify that the displayed \(Z_*\) is genuinely non-toroidal. Let the columns of
\[
U=\begin{pmatrix}
1&0&1/\sqrt2&1/\sqrt2\\
0&1&1/\sqrt2&i/\sqrt2
\end{pmatrix}
\]
be \(u_1,\ldots,u_4\). Then \(Z_*=U^*U\), so \(Z_*\) is a correlation matrix of rank \(2\). To prove extremality directly, suppose \(Z_*=(P+Q)/2\) with correlation matrices \(P,Q\), and put \(H=(P-Q)/2\). Then \(Z_*\pm H\succeq0\) and \(\operatorname{diag}H=0\). If \(\xi\in\ker Z_*\), positivity gives \(P\xi=Q\xi=0\), hence \(H\xi=0\). Thus \(H\) is supported on the range of \(Z_*\), so \(H=U^*XU\) for a Hermitian \(2\times2\) matrix \(X\). Writing
\[
X=\begin{pmatrix}a&x+iy\\x-iy&b\end{pmatrix},
\]
the four zero-diagonal conditions \(u_j^*Xu_j=0\) give successively
\[
a=0,\qquad b=0,\qquad x=0,\qquad y=0.
\]
Hence \(H=0\), proving that \(Z_*\) is extreme. A toroidal decomposition would express this extreme correlation matrix as a convex combination of rank-one correlation matrices; extremality would force every positive-weight summand to equal \(Z_*\), impossible because \(\operatorname{rank}Z_*=2\). Thus \(Z_*\) is not toroidal.

## Verification
The proof is analytic and does not depend on finite enumeration. The standalone checker `artifacts/verify.py` reconstructs \(Z_*=U^*U\), verifies exact rank \(2\), nonnegative eigenvalues, the nonsingular four-equation extremality system, and the endpoint identities \(r_1=1\), \(s_1=4\), and \(M_1=J_4\). Replaying it from its packaged path returns `VERIFY_OK`. The checker corroborates the displayed algebra; the all-\(d\) TCP equivalence is proved symbolically above rather than inferred from computation.

## Relationship to prior work
Márquez González, arXiv:2609.32979v1, introduces the four-dimensional family \(\Phi_{a,Z}\), proves it is bistochastic and PPT for every \(a>0\) and every correlation matrix \(Z\), and proves non-entanglement-breaking only for \(a\ne1\). Its toroidal-core lemma supplies the sufficient implication at \(a=1\) when \(Z\) is toroidal, but it does not state the converse or classify the excluded endpoint.

Singh and Nechita, arXiv:2010.07898v2, establish the TCP/separability correspondence for LDOI objects and note that \(X^{(3)}_{(J_d,B,C)}\) is separable when both \(B\) and \(C\) lie in the convex hull of rank-one correlation matrices. They also record that dimensions at least four admit higher-rank extreme correlation matrices. Those results give the same sufficient direction but not the rank-one-core converse proved here.

Kribs, Levick, Pereira, and Rahaman, arXiv:2306.04077v1, characterize the convex hull of rank-one correlation matrices in mixed-unitary Schur theory and prove general mixing results around the identity. That work concerns the correlation-matrix/mixed-unitary side and does not supply the TCP necessity at the DOC endpoint.

Targeted searches for the equivalent formulations \((J_d,J_d,Z)\in\mathrm{TCP}_d\), separability of \(X^{(3)}_{(J_d,J_d,Z)}\), a rank-one TCP coherence core, and the \(a=1\) endpoint did not locate a prior statement of the iff criterion. The closest sources above were inspected at the level of their relevant definitions and results rather than by title alone.

## Limitations
The result classifies only the rank-one all-ones TCP core and, as an application, the \(a=1\) endpoint of the cited DOC family. It does not characterize general TCP triples, all four-dimensional PPT DOC channels, or the PPT-squared conjecture. The literature comparison cannot exclude an equivalent older statement under different LDOI or Schur-channel terminology that is absent from the searched indexes. The explicit \(Z_*\) witness is used only to show that the endpoint classification has both EB and non-EB cases; no claim is made that it is unique or extremal for another optimization problem.

## References
1. S. A. Márquez González, *Toroidal-Core Certificates for PPT-Squared Diagonal Orthogonal Covariant Channels*, arXiv:2609.32979v1 (2026).
2. S. Singh and I. Nechita, *Diagonal unitary and orthogonal symmetries in quantum theory*, Quantum 5, 519 (2021), arXiv:2010.07898v2.
3. D. W. Kribs, J. Levick, R. Pereira, and M. Rahaman, *Operator Algebra Generalization of a Theorem of Watrous and Mixed Unitary Quantum Channels*, J. Phys. A 57, 115303 (2024), arXiv:2306.04077v1.
