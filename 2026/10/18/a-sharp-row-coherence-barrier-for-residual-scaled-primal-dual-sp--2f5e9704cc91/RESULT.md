# A sharp row-coherence barrier for residual-scaled primal-dual splitting

## Finding
For an invertible real \(n\times n\) matrix \(A\), \(n\ge2\), consider the unique-solution equality-constrained linear program \(\min_{x\in\mathbb R^n}c^{\mathsf T}x\) subject to \(Ax=b\). The standard extrapolated primal-dual hybrid-gradient (PDHG) fixed-point map admits a diagonal **poststep residual** scaling that terminates exactly in two steps on row-orthogonal problems, but whose stability has the sharp normalized row-Gram threshold \(4/3\).

Set \(D=\operatorname{diag}(AA^{\mathsf T})\) and \(G=D^{-1/2}AA^{\mathsf T}D^{-1/2}\). Under the assumptions below, the fixed scaled iteration converges to the unique saddle from **every** starting pair if and only if \(\lambda_{\max}(G)<4/3\). At equality some nonzero initial errors do not decay, and above the threshold some grow exponentially. For two normalized rows of correlation \(\rho\in(-1,1)\), its exact spectral radius is
\[
\rho_{\mathrm{sp}}=|\rho|+\sqrt{|\rho|(1+|\rho|)},
\]
so the sharp two-row stability frontier is \(|\rho|<1/3\), whereas the ordinary PDHG map remains convergent under the ordinary step-size condition. The scaled iteration terminates for **all** initial states within two updates if and only if \(AA^{\mathsf T}\) is diagonal. This two-step property fixes the primal and dual positive coordinate scalings uniquely.

## Assumptions and scope
Fix a real invertible \(A\in\mathbb R^{n\times n}\) with \(n\ge2\), \(b,c\in\mathbb R^n\), and \(\tau,\sigma>0\) satisfying \(\tau\sigma\|A\|_2^2<1\). The equality-constrained problem has the unique saddle \(x_*=A^{-1}b\) and \(y_*=A^{-\mathsf T}c\) for Lagrangian \(L(x,y)=c^{\mathsf T}x+y^{\mathsf T}(b-Ax)\).

Given \(z=(x,y)\), define the ordinary extrapolated primal-dual map \(T(z)=(x^+,y^+)\) by
\[
x^+=x-\tau(c-A^{\mathsf T}y),\qquad
y^+=y+\sigma\{b-A(2x^+-x)\}.
\]
Write \(P=\operatorname{diag}(I,(\tau\sigma)^{-1}D^{-1})\), with all diagonal entries strictly positive. The object studied here is the **unguarded, fixed poststep-residual update** \(S(z)=z-P\{z-T(z)\}\), which is distinct from changing the metric inside the proximal subproblem or choosing trial steps through a safeguard. All conclusions use exact real arithmetic.

## Proof
**1. Exact iteration matrix.** Put \(X=x-x_*\), \(Y=y-y_*\), and write \(z-z_*=(X,Y)\). Direct substitution in \(T\), using \(Ax_*=b\) and \(A^{\mathsf T}y_*=c\), yields
\[
X^+=X+\tau A^{\mathsf T}Y,\quad
Y^+=Y-\sigma AX-2\tau\sigma AA^{\mathsf T}Y.
\]
The scaled error update has matrix
\[
K=\begin{pmatrix}
I&\tau A^{\mathsf T}\\
-\tau^{-1}D^{-1}A&I-2D^{-1}AA^{\mathsf T}
\end{pmatrix}.
\]
Define \(B=D^{-1/2}A\), and change variables to \(u=X\), \(v=\tau D^{1/2}Y\). In these variables \(K\) is similar to
\[
\widetilde K=\begin{pmatrix}I&B^{\mathsf T}\\-B&I-2BB^{\mathsf T}\end{pmatrix}.
\]
Every diagonal entry of \(G=BB^{\mathsf T}\) equals one. Since \(A\) is invertible, every eigenvalue \(g_j\) of \(G\) is strictly positive.

**2. Exact spectrum and boundary.** Apply a real singular-value decomposition \(B=U\operatorname{diag}(\sqrt{g_j})V^{\mathsf T}\) and orthogonally change the primal and dual coordinates. The map separates into \(n\) independent blocks
\[
M_g=\begin{pmatrix}1&\sqrt g\\-\sqrt g&1-2g\end{pmatrix},\qquad
\det(\lambda I-M_g)=\lambda^2-2(1-g)\lambda+(1-g).
\]
The eigenvalues are \(1-g\pm\sqrt{g(g-1)}\). For \(0<g<1\) they are conjugates of modulus \(\sqrt{1-g}<1\); at \(g=1\), \(M_1^2=0\). For \(g>1\), the largest modulus is \(g-1+\sqrt{g(g-1)}\). This is less than one exactly when \(g<4/3\), equals one when \(g=4/3\) (the corresponding eigenvalue is \(-1\)), and exceeds one above \(4/3\). The spectral radius criterion for finite-dimensional linear iterations proves the all-initial-state convergence assertion and both boundary counterexamples. At equality there is a nondecaying eigenvector, not necessarily divergence for every initial state. The ordinary PDHG map, by the same singular-value reduction, has characteristic roots \(1-h\pm i\sqrt{h(1-h)}\) where \(h=\tau\sigma s^2\in(0,1)\) for each singular value \(s\) of \(A\), and thus has spectral radius below one.

**3. Two-row coherence.** For two normalized rows write \(G=\begin{psmallmatrix}1&\rho\\\rho&1\end{psmallmatrix}\) with \(|\rho|<1\). Its eigenvalues are \(1\pm|\rho|\). The above block formula gives radius \(|\rho|+\sqrt{|\rho|(1+|\rho|)}\); this dominates the other block's \(\sqrt{|\rho|}\) and is below one precisely when \(|\rho|<1/3\). For example, take \(A=\begin{psmallmatrix}1&0\\1/2&\sqrt3/2\end{psmallmatrix}\) and \(\tau=\sigma=1/2\). The base PDHG step-size product is \(3/8<1\), yet the fixed scaled map has radius \((1+\sqrt3)/2>1\). The source algorithm's safeguard is not asserted to accept such a trial.

**4. Deadbeat characterization and uniqueness.** If \(AA^{\mathsf T}=D\), then \(G=I\), every \(M_g=M_1\), and \(K^2=0\). Conversely, if the full scaled method reaches the saddle in at most two steps for every initial state, then \(K^2=0\). Every spectral block must have both eigenvalues zero, forcing \(g_j=1\) for all \(j\), so \(G=I\) and \(AA^{\mathsf T}=D\).

More strongly, let the fixed scaling have arbitrary positive diagonal primal and dual blocks \(P_x,P_y\). Its error matrix is
\[
K_P=\begin{pmatrix}
I&\tau P_xA^{\mathsf T}\\
-\sigma P_yA&I-2\tau\sigma P_yAA^{\mathsf T}
\end{pmatrix}.
\]
The upper-right block of \(K_P^2\) is \(2\tau P_xA^{\mathsf T}(I-\tau\sigma P_yAA^{\mathsf T})\). The factors \(P_x\) and \(A\) are invertible, hence \(K_P^2=0\) forces \(P_yAA^{\mathsf T}=(\tau\sigma)^{-1}I\). A positive diagonal \(P_y\) can satisfy this only if \(AA^{\mathsf T}\) itself is diagonal; necessarily \(P_y=(\tau\sigma)^{-1}D^{-1}\). Then the upper-left block of \(K_P^2\) is \(I-P_x\), so \(P_x=I\). These conditions also suffice.

**5. Nonnegative-program interior basin.** Replace the primal step by \(x^+=[x-\tau(c-A^{\mathsf T}y)]_+\) for the nonnegative LP, assume \(x_*=A^{-1}b\) is strictly componentwise positive and \(AA^{\mathsf T}\) diagonal, and retain the same fixed scaling. Any starting pair satisfying \(x+\tau A^{\mathsf T}(y-y_*)\ge0\) componentwise has its first primal projection inactive. The initial update is therefore the affine \(K\)-step. Since \(K^2=0\), the next unprojected primal input is exactly \(x_*>0\); the second projection is inactive too. Thus the second scaled step reaches \((x_*,y_*)\) exactly. This is a sufficient half-space intersection for finite termination; no global claim is made for arbitrary projected starts.

## Verification
The accompanying standalone `verify.py` numerically constructs the original primal-dual map, the scaled residual update and the full linearized matrix; checks its spectrum on multiple two-row correlations and deterministic random invertible matrices; checks the analytic spectral transition, nilpotent cases, a specific instability despite base PDHG stability, and direct two-step termination on the stated nonnegative interior basin. The checks are finite and supplement, rather than establish, the universal proof. Run with `python verify.py` using Python 3 and NumPy.

## Relationship to prior work
Zhang, Gao and Udell (2026) introduce poststep fixed-point residual scaling and online adaptation in operator-splitting methods, concentrating their main paper on FBS, DRS and ADMM. Zhang's September 10 scientific exposition supplies the PDHG linear-program map and a safeguarded block-feedback extension. Neither the displayed online-learning safeguards nor classical diagonal metric changes are the fixed unguarded row-normalized dual correction analyzed here. Pock and Chambolle (2011) study diagonal preconditioning **inside** primal-dual steps, which is a different operator. The contribution assessed here is the exact row-Gram spectral phase diagram, the sharp two-row coherence frontier, the unique two-step diagonal correction, and the interior projected basin. It does not claim to invent PDHG, diagonal scaling, or the fixed-point residual template.

## Limitations
The global spectral claims assume a square invertible real constraint matrix and the exact fixed, unsafeguarded residual update with a specific positive diagonal scaling. Ill-conditioned or coherent rows may destabilize the scaled trial even when base PDHG converges; this does not contradict safeguarded adaptive algorithms. The projected nonnegative-LP result is restricted to a stated interior basin; noninterior starting states or noninvertible rectangular matrices are not classified. Exact arithmetic is assumed, and no improved implementation runtime is claimed. A generic older spectral theorem could yield an equivalent specialized calculation; the literature search is not a proof of absolute novelty.

## References
1. Wanyu Zhang, Wenzhi Gao and Madeleine Udell, *Operator Splitting Methods with Online Scaling*, arXiv:2609.10732, first publicly available September 9, 2026. https://arxiv.org/abs/2609.10732
2. Wanyu Zhang, *Online Scaling for Operator Splitting without a Smooth Envelope*, September 10, 2026. https://zwyhahaha.github.io/2026/09/10/online-scaling-without-a-smooth-envelope/
3. Thomas Pock and Antonin Chambolle, *Diagonal Preconditioning for First Order Primal-Dual Algorithms in Convex Optimization*, ICCV (2011), doi:10.1109/ICCV.2011.6126441.
