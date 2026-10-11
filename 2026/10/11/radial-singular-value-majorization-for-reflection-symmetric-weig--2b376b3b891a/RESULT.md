# Radial singular-value majorization for reflection-symmetric weighted integration

## Finding

Let \(w\in C^1([0,1];\mathbb R)\) be strictly positive and reflection-symmetric, \(w(t)=w(1-t)\). On complex \(L^2(0,1)\) define the weighted, rank-one-corrected Volterra operator
\[
(T_{\alpha,w}f)(x)=\int_0^x w(t)f(t)\,dt-\alpha\int_0^1w(t)f(t)\,dt,\qquad \alpha\in\mathbb C.
\]
Let \(s_1(T)\ge s_2(T)\ge\cdots\) denote singular values with multiplicities. **The entire singular-value sequence depends on \(\alpha\) only through \(r=|\alpha-\tfrac12|\).** Moreover, for any \(0\le r<R\), any \(\alpha,\beta\) with \(|\alpha-\tfrac12|=r\) and \(|\beta-\tfrac12|=R\), and each positive integer \(m\),
\[
\sum_{j=1}^{m}s_j(T_{\alpha,w})\ \le\ \sum_{j=1}^{m}s_j(T_{\beta,w}).
\]
Thus the singular-value sequences obey weak submajorization radially, simultaneously at every finite rank. For every \(1<p<\infty\), the Schatten norms satisfy the **strict** inequality
\[
\|T_{\alpha,w}\|_{S_p}<\|T_{\beta,w}\|_{S_p}\qquad(r<R).
\]
In particular the weighted half-correction \(T_{1/2,w}\) uniquely minimizes every such Schatten norm over the entire complex parameter plane; there is no claim of strictness in every finite Ky Fan inequality.

## Assumptions and scope

All operators act on complex \(L^2(0,1)\) with Lebesgue measure. The weight is real, positive, continuously differentiable and symmetric about \(\tfrac12\). Reflection symmetry is indispensable for the asserted *universal* circular invariance: for the nonsymmetric smooth weight \(w(t)=\sqrt{1+t}\), the parameters \(\alpha=0\) and \(\alpha=1\) have equal radius \(\tfrac12\), yet
\[
\|T_{0,w}\|_{S_2}^2=\frac23,\qquad \|T_{1,w}\|_{S_2}^2=\frac56.
\]
No finite-dimensional experiment is used to infer these infinite-dimensional statements.

## Proof

**1. Inversion and boundary conditions.** For any \(\alpha\), the operator \(T_{\alpha,w}\) maps \(L^2(0,1)\) bijectively onto the Sobolev hyperplane
\[
\mathcal D_\alpha=\{y\in H^1(0,1):(1-\alpha)y(0)+\alpha y(1)=0\}.
\]
Indeed \(y'=wf\) and the endpoint condition follows by substituting \(y(0)=-\alpha\int wf\) and \(y(1)=(1-\alpha)\int wf\). Conversely for \(y\in\mathcal D_\alpha\), \(f=y'/w\) recovers \(y=T_{\alpha,w}f\). Thus its inverse is \(D_\alpha y=y'/w\) on \(\mathcal D_\alpha\). The inverse is closed and densely defined, and the embedding \(H^1(0,1)\hookrightarrow L^2(0,1)\) is compact. Write \(p=w^{-2}\). The positive self-adjoint operator \(D_\alpha^*D_\alpha\), associated to the form \(\int_0^1 p|y'|^2\), has differential expression \(-(py')'\) and boundary conditions
\[
(1-\alpha)y(0)+\alpha y(1)=0,\qquad
\overline\alpha\,p(0)y'(0)+\overline{(1-\alpha)}\,p(1)y'(1)=0.
\]
Its eigenvalues are strictly positive, tend to infinity, and their reciprocal square roots are the singular values of \(T_{\alpha,w}\), with multiplicities.

**2. An exact parameter-dependent characteristic equation.** Let \(M_\lambda=\begin{pmatrix}A_\lambda&B_\lambda\\ C_\lambda&D_\lambda\end{pmatrix}\) carry the state \((y(0),p(0)y'(0))^{\mathsf T}\) to \((y(1),p(1)y'(1))^{\mathsf T}\) for \(-(py')'=\lambda y\). Constancy of the Wronskian gives \(\det M_\lambda=1\). Inserting the two boundary conditions and eliminating the initial state gives **exactly**
\[
F_\alpha(\lambda)=1+|\alpha|^2(A_\lambda-1)+|1-\alpha|^2(D_\lambda-1)=0.
\]
Every positive root is an eigenvalue, with its usual spectral multiplicity; no assertion that the roots admit an elementary closed form is needed. One can obtain the determinant directly from the boundary matrix
\[
\begin{pmatrix}
1-\alpha+\alpha A_\lambda&\alpha B_\lambda\\
\overline{1-\alpha}\,C_\lambda&\overline\alpha+\overline{1-\alpha}\,D_\lambda
\end{pmatrix}.
\]

**3. Reflection removes the complex phase.** When \(p(t)=p(1-t)\), reflection of solutions yields the transfer identity \(M_\lambda=R M_\lambda^{-1}R\), with \(R=\operatorname{diag}(1,-1)\). Hence \(A_\lambda=D_\lambda\). The characteristic equation reduces to
\[
F_\alpha(\lambda)=1+q_\alpha(A_\lambda-1),\qquad
q_\alpha=|\alpha|^2+|1-\alpha|^2=\tfrac12+2|\alpha-\tfrac12|^2.
\]
Thus equal radii give identical eigenvalue characteristic functions; standard multiplicity theory for regular self-adjoint Sturm–Liouville problems ensures identical eigenvalue multisets, hence identical singular-value multisets. The conclusion is for the entire sequence, not just its largest term.

**4. Radial majorization.** For each \(m\ge1\), \(K_m(T)=\sum_{j=1}^m s_j(T)\) is a convex norm of compact operators. The map \(\alpha\mapsto T_{\alpha,w}\) is affine, and Step 3 makes \(K_m(T_{\alpha,w})\) radial around \(\tfrac12\). Every radial convex function on the plane is nondecreasing in its radius: a point on an inner circle is the midpoint of two points on any chosen outer circle. This proves all displayed Ky Fan inequalities.

**5. Strict Schatten ordering.** The classical Volterra operator belongs to \(S_p\) for every \(p>1\), and multiplication by bounded \(w\) and adding a rank-one term preserve that membership. The \(S_p\) norm is strictly convex for \(1<p<\infty\). For distinct parameters \(\alpha\ne\beta\), the operators \(T_{\alpha,w}\) and \(T_{\beta,w}\) are not equal (their difference is a nonzero rank-one operator), and the midpoint inequality is strict. Choose two distinct points of radius \(R\) with midpoint any chosen point of radius \(r<R\); equality of their Schatten norms by Step 3 and strict convexity yield the strict radial inequality.

**6. Boundary of the symmetry assertion.** Directly integrating the square of the kernel gives for any positive \(w\):
\[
\|T_{\alpha,w}\|_{S_2}^2=
\int_0^1w(t)^2\bigl[t|\alpha|^2+(1-t)|1-\alpha|^2\bigr]dt.
\]
For \(w(t)=\sqrt{1+t}\), substituting \(\alpha=0\) and \(1\) yields respectively \(2/3\) and \(5/6\), proving that arbitrary asymmetric weighting can destroy the circular invariance.

## Verification

Run `python verify_weighted.py` after installing dependencies in `requirements.txt`. The standalone checker symbolically verifies the boundary determinant, verifies the exact asymmetric first moment, numerically compares transfer diagonals for symmetric and nonsymmetric weights, and compares discretized singular spectra at several radii and complex phases. It returned `WEIGHTED_VOLTERRA_TRANSFER_OK`. These finite tests verify representative identities only; Steps 1–6 prove the universal statements analytically.

## Relationship to prior work

The classical Volterra singular values and the full scalar-coefficient pencil \(z_1V+z_2V^*\) have been studied extensively. Khadkhuu and Tsedenbayar (2018, Theorem 1 and proof) derive the unweighted spectral root equation underlying the *constant-weight* special case, so neither the constant-weight singular spectrum nor its operator norm is asserted to be new here. Lyubich and Tsedenbayar (2010) treat polynomials in \(V\), not input-weighted rank-one-corrected integration. Fucci, Graham and Kirsten (arXiv:1311.0174, Sections 2–3) give a general spectral-determinant treatment of coupled regular Sturm–Liouville boundary problems. The present contribution is the **weighted integration identification, reflection-dependent isospectral circles, all-rank Ky Fan radial domination, strict Schatten hierarchy, and explicit asymmetric failure**; those conclusions are not established as a family in the inspected papers. Eveson (2004) studies iterates of Volterra convolution operators, rather than this spectral comparison.

## Limitations

The theorem requires a positive reflection-symmetric input weight for radial ordering; no conclusion is made for general nonsymmetric weights beyond the exact transfer equation and the explicit obstruction. It gives an implicit characteristic equation for general weights, not elementary eigenvalue formulas or individual singular-value monotonicity. Each fixed finite-rank Ky Fan sum is proved nondecreasing, not necessarily strictly increasing. The 2018 unweighted paper contains a spectral-root derivation that must not be misrepresented as novel. General Sturm–Liouville theory supplies part of the method; bibliographic searches cannot establish global uniqueness, and an equivalent weighted comparison in unindexed literature remains possible. Independent mathematical validation has not been conducted.

## References

- S. P. Eveson, *Asymptotic behaviour of iterates of Volterra operators on \(L^p(0,1)\)*, arXiv:math/0409516v1, public 27 September 2004.
- Y. Lyubich and D. Tsedenbayar, *The norms and singular numbers of polynomials of the classical Volterra operator in \(L^2(0,1)\)*, Studia Math. 199 (2010), 171–184, DOI:10.4064/sm199-2-3.
- L. Khadkhuu and D. Tsedenbayar, *A note about Volterra operator*, Mathematica Slovaca 68 (2018), 1117–1120, DOI:10.1515/ms-2017-0173.
- G. Fucci, C. Graham and K. Kirsten, *Spectral functions for regular Sturm–Liouville problems*, arXiv:1311.0174v1 (2013).
- V. K. Tuan and R. Gorenflo, *Asymptotics of singular values of Volterra integral operators*, Numer. Funct. Anal. Optim. 17 (1996), 453–461, DOI:10.1080/01630569608816704.
