# Fourth-band harmonic sampling on the 24-cell: exact spectrum and uniquely optimal weights

## Finding
Let \(X\) be the twenty-four unit vectors in \(\mathbb R^4\) consisting of \(\pm e_i\), \(1\le i\le4\), and all sixteen sign vectors \((\pm1,\pm1,\pm1,\pm1)/2\). Equip \(S^3\) with probability surface measure. For each integer \(L\ge0\), let \(\mathcal H_{\le L}\) be the complex Hilbert direct sum of spherical harmonics of degrees \(0,\ldots,L\). For strictly positive weights \(w_x\) with \(\sum_{x\in X}w_x=1\), define the restriction map
\[
R_{L,w}:\mathcal H_{\le L}\longrightarrow \ell^2(X,w),\qquad (R_{L,w}f)_x=f(x).
\]
Its ranks at the first five cutoffs are
\[
(\operatorname{rank}R_{0,w},\ldots,\operatorname{rank}R_{4,w})=(1,5,14,22,24).
\]
At \(L=4\), for the uniform weights \(w_x=1/24\), the complete positive squared singular spectrum of \(R_{4,w}\) is
\[
1\quad(5\text{ times}),\qquad 2\quad(8\text{ times}),\qquad
\frac83\quad(9\text{ times}),\qquad 5\quad(2\text{ times}).
\]
Thus \(\kappa(R_{4,w})=\sqrt5\). This is **the least possible condition number among all strictly positive node weights**, and equality requires every weight to equal \(1/24\). In particular, degree four is the smallest spherical-harmonic cutoff allowing arbitrary interpolation on the full vertex set.

## Assumptions and scope
The sampling nodes are exactly the vertices specified above, without identification of antipodal pairs. All complex harmonics use the sphere's probability measure, and node weights are strictly positive and normalized to sum to one. Condition number means the ratio of the largest to the smallest **positive** singular value; at cutoff four restriction is surjective and all twenty-four sample singular values are positive. Lower-cutoff ranks do not depend on the positive weights. No claim is made about arbitrary four-dimensional spherical codes or about higher cutoffs.

## Proof
**1. Addition kernel.** Write \(U_0(t)=1\), \(U_1(t)=2t\), and \(U_{j+1}(t)=2tU_j(t)-U_{j-1}(t)\). The addition formula on \(S^3\) gives the reproducing kernel
\[
K_L(x,y)=\sum_{j=0}^{L}(j+1)U_j(\langle x,y\rangle).
\]
This follows by the zonal addition theorem normalized by \(\dim\mathcal H_j=(j+1)^2\), since \(U_j(1)=j+1\). With the vertex ordering of the verification script, let \(K_L\) also denote the twenty-four by twenty-four evaluation Gram matrix. The nonzero squared singular values of \(R_{L,w}\) are the nonzero eigenvalues of \(W^{1/2}K_LW^{1/2}\), where \(W=\operatorname{diag}(w_x)\).

**2. The adjacency calculation.** Among distinct vertices the only inner products are \(-1\), \(-1/2\), \(0\), and \(1/2\). Let \(J\) interchange antipodal vertices; \(A\) join vertices whose dot product is \(1/2\); let \(A_0\) join those with dot product zero; and put \(F=\mathbf1\mathbf1^*\). Then
\[
F=I+J+A_0+A+JA.
\]
Indeed, replacing a vertex by its antipode turns the \(1/2\) relation into the \(-1/2\) relation. Inserting the five possible dot products into the degree-four kernel yields the exact values
\[
\begin{array}{c|rrrrr}
\langle x,y\rangle&1&-1&0&1/2&-1/2\\\hline
K_4(x,y)&55&15&3&-6&-2
\end{array}
\]
and hence
\[
K_4=52I+12J+3F-9A-5JA.
\]
In the \(J\)-even subspace this reduces to \(64I+3F-14A\), and in the \(J\)-odd subspace it reduces to \(40I-4A\). The latter has \(F=0\).

For completeness, diagonalize \(A\) directly. Partition the vertices into eight signed axes and sixteen binary sign corners. Then
\[
A=\begin{pmatrix}0&B\\B^*&Q_4\end{pmatrix},
\]
where \(Q_4\) is the adjacency of the four-cube and \(B_{(i,\varepsilon),s}=1\) exactly when \(s_i=\varepsilon\). The corner Walsh monomial indexed by \(S\subseteq[4]\) is an eigenvector of \(Q_4\) with eigenvalue \(4-2|S|\). The matrix \(B\) kills every degree-two-or-higher Walsh monomial. The coupled constant sector has adjacency matrix \(\left(\begin{smallmatrix}0&8\\4&4\end{smallmatrix}\right)\), with eigenvalues \(8,-4\); each of the four coupled degree-one sectors has matrix \(\left(\begin{smallmatrix}0&8\\1&2\end{smallmatrix}\right)\), with eigenvalues \(4,-2\). On the axis block, the three even coordinate-difference directions are zero modes. Corner Walsh degrees two, three and four contribute eigenvalues \(0,-2,-4\) with multiplicities \(6,4,1\). Tracking parity under antipodal sign reversal gives the exact joint spectrum
\[
\begin{array}{c|rrr}
J=+1&A=8\ (1)&A=0\ (9)&A=-4\ (2)\\
J=-1&A=4\ (4)&A=-2\ (8)&
\end{array}
\]
where parenthesized integers are multiplicities. Since \(F\) acts by \(24\) on the all-ones eigenvector, which has \(J=+1,A=8\), and vanishes on its orthogonal complement, the eigenvalues of \(G=K_4/24\) are \(1\) five times, \(2\) eight times, \(8/3\) nine times, and \(5\) twice. This proves the uniform spectral assertion and surjectivity.

**3. Sharp weighted conditioning and uniqueness.** Besides the constant vector \(v^{(1)}_x=1\), which satisfies \(Gv^{(1)}=v^{(1)}\), there is a unimodular eigenvector \(v^{(5)}\) with \(Gv^{(5)}=5v^{(5)}\). To exhibit it, choose any primitive cube root of unity \(\omega\), put \(v^{(5)}=1\) on the eight axes, and on a corner \(s/2\) put \(v^{(5)}=\omega\) if \(\prod_i s_i=1\), otherwise \(\omega^2\). This vector is antipodally even, has coordinate sum zero, and direct neighbor counting gives \(Av^{(5)}=-4v^{(5)}\): every axis sees four corners of each phase, while every corner sees four axes and four opposite-parity corners. The formula above for \(K_4\) then gives the claimed eigenvalue \(5\).

Set \(B_w=W^{1/2}K_4W^{1/2}\). For either of the two unimodular eigenvectors \(v^{(\lambda)}\), with \(\lambda\in\{1,5\}\), test the Rayleigh quotient of \(z^{(\lambda)}=W^{-1/2}v^{(\lambda)}\):
\[
\frac{(z^{(\lambda)})^* B_w z^{(\lambda)}}{\|z^{(\lambda)}\|^2}
=\frac{576\lambda}{\sum_x w_x^{-1}}=:c\lambda.
\]
Thus \(\lambda_{\max}(B_w)\ge5c\), while \(\lambda_{\min}(B_w)\le c\). Since \(B_w\) is positive definite, \(\kappa(R_{4,w})^2\ge5\). Equality requires both Rayleigh bounds to be attained, especially \(z^{(1)}\) to be an eigenvector for the smallest eigenvalue \(c\). But
\[
B_w z^{(1)}=24W^{1/2}\mathbf1,
\]
so the eigenvector equation forces \(24w_x=c\) at every vertex, and normalization forces \(w_x=1/24\). Conversely, the uniform weights attain \(\sqrt5\). This proves global optimality and uniqueness, without a perturbative assumption.

**4. Exact interpolation and earlier cutoffs.** The minimal polynomial of \(G\) divides \((t-1)(t-2)(t-8/3)(t-5)\), and Lagrange interpolation of the reciprocal function gives
\[
G^{-1}=-\frac3{80}G^3+\frac25G^2-\frac{23}{16}G+\frac{83}{40}I.
\]
For arbitrary target data \(y=(y_x)_{x\in X}\), the unique least-\(L^2(S^3)\)-norm interpolant in \(\mathcal H_{\le4}\) is therefore
\[
f_y(t)=\frac1{24}\sum_{x\in X} K_4(t,x)(G^{-1}y)_x.
\]
The formula evaluates to \(y\) on all twenty-four vertices; every other interpolant differs by a vector in the kernel of the restriction map.

Finally, the 24-cell is a spherical 5-design; consequently the unweighted Gram matrices for cutoffs \(L=0,1,2\) have nonzero normalized eigenvalues all equal to one, of total multiplicities \(1,5,14\) respectively, because products of harmonics up to degree two have degree at most four. For \(L=3\), the kernel values at dot products \(1,-1,0,1/2,-1/2\) are \(30,-10,-2,-1,3\), yielding
\[
K_3\big|_{J=+1}=24I-2F+6A,\qquad K_3\big|_{J=-1}=40I-4A.
\]
The joint adjacency spectrum above gives \(K_3/24\) eigenvalues \(1\) fourteen times, \(2\) eight times and \(0\) twice. Thus its rank is \(22\), establishing all five ranks.

## Verification
The standalone standard-library script `check_24cell.py` forms the twenty-four exact rational vertices, constructs the five addition kernels using rational Chebyshev recurrence, performs exact row-reduction for all ranks, verifies the full factor identity \((K_4-24I)(K_4-48I)(K_4-64I)(K_4-120I)=0\), confirms the trace moments and inverse polynomial, and checks both explicit unimodular endpoint eigenvectors over \(\mathbb Q(\omega)\). It passes locally. The infinite assertion here concerns **all positive weight vectors on this fixed finite sampling set**; that assertion is proved algebraically in Step 3, not inferred from finite sampling of weights.

## Relationship to prior work
The regular 24-cell and its spherical design strength are classical. Cohn, Conway, Elkies and Kumar establish its 5-design property in the setting of optimal spherical configurations. Hirao, Nozaki and Tasaka subsequently study harmonic strengths of finite quaternionic unit groups and related modular forms. General optimal-design results for harmonic regression, such as Haines's discussion of degree versus design strength on the two-sphere, furnish related criteria but do not directly give a twenty-four-node fourth-degree singular spectrum on the three-sphere: strength five guarantees exact quadrature for products only through combined degree five, whereas the present band contains degree-four functions and products of degree eight. The calculation above uses the antipodal and four-cube incidence geometry to determine the full fourth-band spectrum, a sharp global conditioning bound, and uniqueness under all positive diagonal weights.

## Limitations
This is an exact theorem for one fixed, natural sampling configuration, not a claim of optimality among all possible twenty-four-point subsets of \(S^3\). Non-uniform weights are required to be strictly positive; approaching a zero weight makes full-node sampling singular. The broad literature on spherical harmonic frames and preconditioning is extensive, so an unlocated general specialization could subsume parts of this result. The accompanying self-review does not replace independent bibliographic review. The numerical checker corroborates finite matrix identities but is not needed to establish the analytic weighted-optimality proof.

## References
1. H. Cohn, J. H. Conway, N. Elkies and A. Kumar, *The \(D_4\) root system is not universally optimal*, first arXiv posting July 19, 2006; arXiv:math/0607447, https://arxiv.org/abs/math/0607447 and full text https://arxiv.org/html/math/0607447v3.
2. M. Hirao, H. Nozaki and K. Tasaka, *Spherical designs for finite quaternionic unit groups and their applications to modular forms*, arXiv:2507.01358, https://arxiv.org/pdf/2507.01358 (2025).
3. L. M. Haines, *Optimal designs for spherical harmonic regression* (2024); https://doi.org/10.1007/s00362-024-01630-5.
4. Standard addition formula for spherical harmonics on \(S^3\), equivalently the Gegenbauer addition theorem with \(C_j^{(1)}=U_j\).
