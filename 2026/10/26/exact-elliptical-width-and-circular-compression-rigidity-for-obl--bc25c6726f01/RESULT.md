# Exact elliptical width and circular-compression rigidity for oblique four-point normal spectra

## Finding
Let \(u,v,z_0\in\mathbb C\) with \(\operatorname{Im}(\overline u v)\ne0\), and let the normal matrix \(N\in M_4(\mathbb C)\) have eigenvalues \(z_0+u+v,z_0+u-v,z_0-u+v,z_0-u-v\), in that order. Put
\[
A=|u|^2+|v|^2,\quad B=\operatorname{Re}(\overline u v),\quad D=\operatorname{Im}(\overline u v),\quad h=\sqrt{A^2-4B^2},\quad \kappa=-\frac{2B}{A+h}.
\]
For a matrix \(T\), let \(W(T)=\{\langle Tx,x\rangle:\|x\|=1\}\) and let \(\delta(T)\) be the diameter of the largest closed Euclidean disk contained in \(W(T)\). Write \(\delta_2(N)=\max_{\dim S=2}\delta(N_S)\), where \(N_S\) is the orthogonal compression to \(S\). **Then**
\[
\boxed{\delta_2(N)^2=\frac{8D^2}{A+h}.}
\]
Every maximizing compression has numerical range **exactly** the closed disk of center \(z_0\) and radius \(\frac12\sqrt{8D^2/(A+h)}\). In the stated eigenbasis, all maximizing planes are obtained by selecting a unit vector \(x\) with four coordinate moduli squared, in order,
\[
\boxed{\left(\frac{1+\kappa}{4},\frac{1-\kappa}{4},\frac{1-\kappa}{4},\frac{1+\kappa}{4}\right),}
\]
allowing arbitrary coordinate phases, and adjoining the unique (up to phase) unit vector \(y\) described in the proof. Equivalently, all maximizing subspaces form one orbit of the diagonal-unitary commutant of \(N\).

As a consequence of the previously established finite-dimensional positive-block identity \(\Phi(X)=\delta_2(X)\), the optimal norm excess over all positive semidefinite block matrices with this fixed off-diagonal block is
\[
\boxed{\Phi(N)=\sqrt{\frac{8D^2}{A+h}}.}
\]
For example, \(u=1,v=e^{i\pi/3}\) gives \(\delta_2(N)^2=6/(2+\sqrt3)\), strictly greater than the equal-probability value \(3/2\). The square-root formula therefore detects a nontrivial optimal correlation in an oblique parallelogram, rather than a rotation of the rectangular case.

## Assumptions and scope
The matrix is complex normal, exactly four-dimensional, with four distinct eigenvalues forming a nondegenerate parallelogram. All maximizations are over complex two-dimensional *orthogonal* compressions. The scalar \(h>0\) because \(|2B|<A\) under real-linear independence of \(u,v\). The norm \(\Phi\) is the supremum of \(\|\begin{psmallmatrix}P&N\\N^*&Q\end{psmallmatrix}\|-\|P+Q\|\) over Hermitian \(P,Q\in M_4(\mathbb C)\) with the displayed block positive semidefinite. The asserted formula does not address non-parallelogram spectra or higher compression ranks.

## Proof
**1. Two-dimensional compression/covariance identity.** Translation by \(z_0 I\) does not change disk diameters, so assume \(z_0=0\). For an arbitrary unit vector \(x\in\mathbb C^4\), put \(p_j=|x_j|^2\), \(m=\sum_jp_jz_j\), \(V=\sum_jp_j|z_j-m|^2\), and \(c=\sum_jp_j(z_j-m)^2\). Suppose \(V>0\). The squared norm of the component of \(N^*x\) orthogonal to \(\operatorname{span}\{x,Nx\}\) is
\[
V-\frac{|c|^2}{V}.
\]
Indeed, \(\|(N^*-\overline m)x\|^2=V\), \(\|(N-m)x\|^2=V\), and the absolute inner product of the two centered vectors is \(|c|\). For a two-dimensional compression, choose a Schur eigenvector \(x\) followed by an orthogonal \(y\); the off-diagonal Schur entry is \(|\langle Ny,x\rangle|\), exactly the minor-axis length of its numerical-range ellipse. For fixed \(x\), maximizing over admissible \(y\perp x,Nx\) gives the displayed projection norm. Conversely every compression has a Schur eigenvector. If \(V=0\), the contribution is zero. Consequently
\[
\delta_2(N)^2=\max_{p_j\ge0,\,\sum p_j=1}\frac{V^2-|c|^2}{V},
\]
with the fraction zero for \(V=0\). If \(C\) is the \(2\times2\) real covariance matrix of the planar random point \(z_j\) with probabilities \(p_j\), then \(V=\operatorname{tr}C\) and \(V^2-|c|^2=4\det C\). Thus the objective is \(F(C)=4\det C/\operatorname{tr}C\).

**2. The optimal law is centered and centrally symmetric.** The four points are paired by central reflection. For any probability law \(p\), replace it by its average with the reflected law. The new law has the same second-moment matrix, mean zero, and covariance \(\widetilde C=C+mm^{\mathsf T}\), with \(m\) now interpreted as the two real coordinates of the original mean. On positive definite covariance matrices \(F(C)=4\lambda_1\lambda_2/(\lambda_1+\lambda_2)\) is strictly increasing under every nonzero positive-semidefinite increment: each eigenvalue is nondecreasing, at least one strictly increases, and the scalar expression is strictly increasing in each positive eigenvalue. Degenerate covariance has zero objective and is not a maximizer because the four eigenvalues are not collinear. Hence every optimal law has mean zero. Since \(u,v\) are real-linearly independent, zero mean means that the expected signs of \(u\) and \(v\) vanish, forcing the opposite-vertex weights to match. There is therefore one \(\kappa\in[-1,1]\) such that the four probabilities are \(((1+\kappa)/4,(1-\kappa)/4,(1-\kappa)/4,(1+\kappa)/4)\).

**3. Exact one-variable optimization.** Writing \(u,v\) as real planar vectors and \(L=[u\ v]\), the centered covariance is \(C=L\begin{psmallmatrix}1&\kappa\\\kappa&1\end{psmallmatrix}L^{\mathsf T}\). Therefore
\[
\det C=D^2(1-\kappa^2),\qquad \operatorname{tr}C=A+2B\kappa,
\]
and hence
\[
F(\kappa)=\frac{4D^2(1-\kappa^2)}{A+2B\kappa}.
\]
The denominator is strictly positive on \([-1,1]\). The endpoint values vanish and every interior value is positive. The derivative has the sign of \(-[B\kappa^2+A\kappa+B]\), whose strictly increasing derivative \(A+2B\kappa\) is positive. Its unique zero in \((-1,1)\) is \(\kappa_*=-2B/(A+h)\), also valid for \(B=0\) by continuity. At this point \(A+2B\kappa_*=h\) and \(1-\kappa_*^2=2h/(A+h)\). Thus the maximum is \(8D^2/(A+h)\), uniquely attained by the asserted weights.

**4. Explicit maximizer and rigidity.** Put \(\Delta=\sqrt{8D^2/(A+h)}\), let \(x\) be any unit vector with those four weights, and let \(c=\sum_jp_j z_j^2\), \(V=\sum_jp_j|z_j|^2=h\). Define the second unit vector by
\[
\boxed{y=\Delta^{-1}\bigl(N^*x-(\overline c/V)Nx\bigr).}
\]
The projection identity gives \(\|y\|=1\) and \(y\perp x,Nx\). Therefore the compression to \(\operatorname{span}\{x,y\}\), expressed in the orthonormal basis \((x,y)\), is \(\begin{psmallmatrix}0&\Delta\\0&0\end{psmallmatrix}\): the off-diagonal entry is \(\Delta\); the first diagonal entry vanishes because the weights are centrally symmetric; and the second vanishes because \(|y_j|^2\) is unchanged under replacing \(z_j\) by \(-z_j\), so their weighted signed sum is zero. Its numerical range is the closed disk centered at zero of radius \(\Delta/2\).

Conversely a maximizing plane has a Schur eigenvector \(x\). Equality in the chain of inequalities from part 1 forces its coordinate moduli squared to be the unique optimal probabilities from part 3 and forces the orthogonal Schur companion \(y\) to lie in the one-dimensional direction of the nonzero projection of \(N^*x\) onto \(\{x,Nx\}^\perp\). Thus its plane is exactly the one constructed above. Arbitrary phases of the coordinates of \(x\) commute with diagonal \(N\), establishing the full diagonal-unitary orbit classification. Translation restores disk center \(z_0\). Finally, Sababheh's Theorem 3.2 identifies the optimal positive-block norm defect with \(\delta_2(N)\), proving the last displayed formula without claiming that external theorem as new.

## Verification
The bundled standard-library script `verify_oblique.py` evaluates the closed formula, the unique optimal weights, the direct covariance functional for competing distributions, and the orthonormal Schur witness for five noncollinear configurations. It checks \(24000\) deterministic competing probability vectors per configuration, plus exact special-case reductions. The proof above does not depend on finite tests. As an exact normalization check, the orthogonal-vector case \(B=0\) yields \(\Delta^2=4D^2/A\), agreeing with the previously computed rectangular spectrum. For \(u=1,v=e^{i\pi/3}\) the correlation is \(\kappa_*=-(2-\sqrt3)\), and the exact squared width is \(6/(2+\sqrt3)\).

## Relationship to prior work
Sababheh (2026, Theorem 3.2) proved the general bridge \(\Phi(X)=\delta_2(X)\), but does not optimize its right side for oblique four-point normal spectra. Bourin and Lee (2021) introduced the elliptical-width bound without an exact parallelogram evaluation. Gau and Wu (2004, *Numerical range of a normal compression II*, especially Theorems 2.3 and 3.1) describe edge tangencies and normal-compression geometry, but not the present covariance minimax or its sharp full spectral formula. The published *Sharp elliptical width and complete compression rigidity for four-corner normal matrices* (2026) establishes the \(B=0\) rectangular subfamily. Its norm result, upper-bound proof and orbit classification assume real and imaginary half-sides of an axis-aligned rectangle; an oblique parallelogram with \(B\ne0\) cannot be brought into that family by complex unitary or scalar affine invariance, and the optimizing correlation is nonzero. The three-point spectral-triangle incircle result treats only three spectral vertices and likewise does not imply a four-point parallelogram norm formula. The general covariance projection step is related to classical Ritz-value/numerical-range methods, but the explicit optimization and full oblique four-spectrum classification are the contribution here.

## Limitations
The four spectral points must form a nondegenerate parallelogram; there is no claim for arbitrary quadrilaterals. The positive-block consequence depends on the cited general theorem, not a newly supplied constructive block-family proof. The optimal block excess is a supremum and need not be attained by a finite positive block. The literature search cannot rule out an unindexed equivalent formula under covariance or binary-observable compatibility terminology. Finite numerical checks alone do not establish the universal theorem. Independent scientific audit is not performed.

## References
1. Mohammad Sababheh, *An Extremal Formula for Elliptical Width and the Bourin–Lee Conjecture*, arXiv:2610.04377v1, first public 2026-10-03, https://arxiv.org/html/2610.04377v1.
2. Jean-Christophe Bourin and Eun-Young Lee, *Eigenvalue inequalities for positive block matrices with the inradius of the numerical range*, arXiv:2111.15180v1 (2021), https://arxiv.org/abs/2111.15180.
3. Hwa-Long Gau and Pei Yuan Wu, *Numerical range of a normal compression II*, Linear Algebra and its Applications 390 (2004), 121–136, doi:10.1016/j.laa.2004.04.013.
4. *Sharp elliptical width and complete compression rigidity for four-corner normal matrices*, public mathematical research record dated 2026-10-11, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-sharp-elliptical-width-and-complete-compression-rigidity-for-fou--c714a536b540.
5. *The incircle is the unique maximal numerical range of a two-dimensional compression of a three-point normal operator*, public mathematical research record dated 2026-10-11, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-the-incircle-is-the-unique-maximal-numerical-range-of-a-two-dime--9f87930b22d4.
