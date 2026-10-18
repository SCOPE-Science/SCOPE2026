# Unimodular single-node reachability and equal controllability volume on every path

## Finding

For every integer \(n\ge2\), let \(L_n\) be the combinatorial Laplacian of the unweighted path \(P_n\), with vertices numbered consecutively from \(1\) to \(n\). For \(1\le j\le n\) define its ordered Kalman matrix
\[
K_{n,j}=[e_j,(-L_n)e_j,\ldots,(-L_n)^{n-1}e_j].
\]
Then the **exact integral-volume classification** is
\[
\boxed{\det K_{n,j}\in\{-1,0,1\},\qquad
 |\det K_{n,j}|=\begin{cases}1,&\gcd(2j-1,n)=1,\\0,&\gcd(2j-1,n)>1.\end{cases}}
\]
In particular, the full-rank Kalman matrices are unimodular over the integers; there are exactly \(\varphi(2n)\) such actuator locations, where \(\varphi\) is Euler's totient. For the integer-input discrete update \(x_{t+1}=-L_nx_t+e_ju_t\) starting from zero, an arbitrary integer state can be reached **exactly in \(n\) steps with integer inputs** if and only if this gcd equals one, because the input-to-terminal-state matrix is a column permutation of a unimodular integer matrix. For every real \(a\), every nonzero real \(b\), and every integer \(H\ge n\), the discrete-time controllability Gramian for \(A=aI-bL_n\),
\[
W^{\mathrm d}_{n,j}(H)=\sum_{t=0}^{H-1}A^te_je_j^{\mathsf T}A^t,
\]
has the **same positive determinant at every controllable vertex**, and determinant zero at every other vertex. At the minimum full-rank horizon,
\[
\boxed{\det W^{\mathrm d}_{n,j}(n)=
\begin{cases}b^{n(n-1)},&\gcd(2j-1,n)=1,\\0,&\text{otherwise}.\end{cases}}
\]
For \(H<n\), all of these Gramian determinants vanish.

The analogous result holds for every continuous-time horizon \(T>0\) and uniform damping \(\gamma\ge0\). Put
\[
W^{\mathrm c}_{n,j}(T,\gamma)=\int_0^T
 e^{-(L_n+\gamma I)t}e_je_j^{\mathsf T}e^{-(L_n+\gamma I)t}\,dt,
\quad \lambda_k=2-2\cos(k\pi/n),\quad 0\le k<n,
\]
and
\[
C_{k\ell}(T,\gamma)=\int_0^T
 e^{-(2\gamma+\lambda_k+\lambda_\ell)t}\,dt.
\]
For each \(T>0\), \(C\) is positive definite and
\[
\boxed{\det W^{\mathrm c}_{n,j}(T,\gamma)=
\begin{cases}(2n)^{-(n-1)}\det C(T,\gamma),&\gcd(2j-1,n)=1,\\0,&\text{otherwise}.\end{cases}}
\]
The common positive determinant is independent of actuator location and so gives the complete global D-optimal single-actuator set, uniformly in \(T\) and \(\gamma\). If \(\gamma>0\), the infinite-horizon expression is particularly simple:
\[
\boxed{\det W^{\mathrm c}_{n,j}(\infty,\gamma)=
\begin{cases}\displaystyle\prod_{k,\ell=0}^{n-1}
  (2\gamma+\lambda_k+\lambda_\ell)^{-1},&\gcd(2j-1,n)=1,\\0,&\text{otherwise}.\end{cases}}
\]

## Assumptions and scope

Each path edge has unit weight; vertices are indexed starting at one. The control is one unconstrained scalar input at one vertex, with unit actuator amplitude. The Gramian is on the **full** \(n\)-dimensional state space, including the consensus mode. The finite continuous-time horizon is strictly positive. Only for the infinite continuous-time horizon is \(\gamma>0\) required. The discrete horizon \(H\) counts the number of summands and its dynamics need not be stable for finite \(H\). No claim is made about multiple actuators, nonunit path weights, trace metrics, or equal Gramian matrices rather than equal **determinants**.

## Proof

**Step 1: path eigenvectors and their coordinate product.** The distinct eigenvalues of \(L_n\) are \(\lambda_k=2-2\cos(k\pi/n)\), \(0\le k<n\). An orthonormal eigenbasis \(u_k\) has entries
\[
u_0(j)=n^{-1/2},\qquad
u_k(j)=\sqrt{2/n}\cos\!\left(\frac{\pi k(2j-1)}{2n}\right)
\quad (1\le k<n).
\]
Write \(r=2j-1\). If \(g=\gcd(r,n)>1\), then \(g\) is odd and \(k=n/g\) belongs to \(\{1,\ldots,n-1\}\); \(\cos(\pi kr/(2n))=0\). Conversely, if \(\gcd(r,n)=1\), then \(r\) is invertible modulo \(2n\). Multiplication by \(r\) permutes the nonzero residue-pairs \(\{\pm k\}\) for \(1\le k<n\), and therefore permutes the absolute cosine values \(\left|\cos(\pi k/(2n))\right|\). The elementary product identity
\[
\prod_{k=1}^{n-1}\cos\left(\frac{\pi k}{2n}\right)=
\frac{\sqrt n}{2^{n-1}}
\]
then gives
\[
\boxed{\prod_{k=0}^{n-1}u_k(j)^2=
\begin{cases}(2n)^{-(n-1)},&\gcd(2j-1,n)=1,\\0,&\text{otherwise}.\end{cases}}
\tag{1}
\]
The cosine identity follows, for instance, from the standard product of \(2n\)-th roots of unity or the double-angle formula and the sine product. Since all numbers coprime to \(2n\) are odd, the count of \(j\) obeying the gcd condition is exactly \(\varphi(2n)\).

**Step 2: integer Kalman volume.** Let \(U\) have eigenvector columns \(u_k\). Spectral factorization of the Kalman matrix gives
\[
K_{n,j}=U\operatorname{diag}(u_0(j),\ldots,u_{n-1}(j))V,
\quad V_{k,t}=(-\lambda_k)^t,\quad 0\le k,t<n.
\]
The squared determinant is the product in (1) times the nonzero squared Vandermonde \(\prod_{k<\ell}(\lambda_\ell-\lambda_k)^2\). For the endpoint \(j=1\), the vector \((-L_n)^t e_1\) vanishes beyond row \(t+1\), and its component in row \(t+1\) equals \(1\). Thus \(K_{n,1}\) is triangular with every diagonal entry \(1\), so \(\det K_{n,1}=1\). Because \(j=1\) is coprime, the Vandermonde square must equal \((2n)^{n-1}\). Inserting (1) now proves every Kalman determinant has absolute value \(0\) or \(1\). It is an integer determinant, establishing the claimed unimodularity without numerical approximation.

**Step 3: discrete Gramian.** Replacing \(-L_n\) by \(A=aI-bL_n\) changes the squared Vandermonde by the factor \(b^{n(n-1)}\). Consequently, for the \(n\)-step Kalman matrix \(K_{n,j}(A)\),
\[
\det K_{n,j}(A)^2=\mathbf1_{\gcd(2j-1,n)=1}\,b^{n(n-1)}.
\]
The minimal-horizon Gramian is \(W^{\mathrm d}_{n,j}(n)=K_{n,j}(A)K_{n,j}(A)^{\mathsf T}\), yielding the stated determinant. For larger \(H\), orthogonal diagonalization gives \(U^{\mathsf T}W^{\mathrm d}U=D_j C_H D_j\) with \((D_j)_{kk}=u_k(j)\) and \((C_H)_{k\ell}=\sum_{t=0}^{H-1}(a-b\lambda_k)^t(a-b\lambda_\ell)^t\). For \(H\ge n\) the monomial feature vectors are linearly independent because the spectral nodes are distinct, making \(C_H\) positive definite and independent of \(j\); equation (1) completes the location classification. For \(H<n\), the Gramian has rank at most \(H\).

**Step 4: continuous Gramian.** With \(B=-L_n-\gamma I\), the same orthogonal diagonalization gives \(U^{\mathsf T}W^{\mathrm c}U=D_j C D_j\), where \(C\) is as above. Since distinct exponentials are linearly independent on every nonempty interval, \(z^{\mathsf T}Cz=\int_0^T |\sum_k z_k e^{-(\gamma+\lambda_k)t}|^2dt>0\) for every nonzero \(z\). Equation (1) therefore proves the finite-horizon statement. For \(\gamma>0\) and \(T=\infty\), the Cauchy matrix has entries \((2\gamma+\lambda_k+\lambda_\ell)^{-1}\) and determinant
\[
\det C(\infty,\gamma)=\frac{\prod_{k<\ell}(\lambda_\ell-\lambda_k)^2}{\prod_{k,\ell}(2\gamma+\lambda_k+\lambda_\ell)}.
\]
The Vandermonde identity from Step 2 cancels \((2n)^{-(n-1)}\), producing the exact product formula.

## Verification

`verify.py` reproduces exact-integer Bareiss determinants for every input location on paths from \(n=2\) to \(n=18\), exact minimal-horizon Gramian determinants for \(n\le8\), rational Lyapunov-equation solutions for \(n\le4\) with positive damping, and affine discrete-time matrices at multiple integer scalings. It prints a single `VERIFY_OK` line or raises an exception. This is supplementary finite corroboration, not the proof of a statement for all \(n\).

## Relationship to prior work

Parlangeli and Notarstefano [1, Theorem IV.4] give the arithmetic **rank-controllability** criterion for Laplacian dynamics on paths; that criterion is acknowledged prior knowledge. Fitch and Leonard [2, Theorem 2] factor a **reduced disagreement-space** reachable-volume objective into Laplacian eigenvector products. Dilip [3, Theorem 3 and Example 1] gives a general full-state spectral Gramian determinant comparison and observes a four-way optimality tie for a **six-vertex path**. The present result does **not** claim either general factorization or that example as new. Its evaluated statement is the all-size exact **unimodular Kalman determinant** and its consequence that all controllable nodes tie for **every finite horizon and damping**, with explicit common determinants and totient count. Existing formulas motivate this problem but, in the inspected material, do not evaluate this exact infinite-family identity. Adjacency-based path control cannot be used as a mere shift or rescaling: the path Laplacian differs from the shifted adjacency operator in its endpoint diagonal terms, and must be treated with its own eigenvectors.

## Limitations

The finding does not rank controllable positions by worst-case energy, trace, or numerical conditioning; equality of determinants allows strongly unequal spectra. The classical generic spectral factorization and qualitative reachability criterion are existing results. The six-node tie was explicitly reported before this proof. Although the inspected primary materials do not state this combined all-size theorem, independent priority and mathematical review remain necessary. Infinite-horizon continuous-time values require \(\gamma>0\), because the undamped consensus mode makes the infinite integral diverge.

## References

[1] G. Parlangeli and G. Notarstefano, *On the reachability and observability of path and cycle graphs*, arXiv:1109.3556v1, first public 2011-09-16. https://arxiv.org/abs/1109.3556

[2] K. Fitch and N. E. Leonard, *Optimal Leader Selection for Controllability and Robustness in Multi-agent Networks*, European Control Conference, 2016, Theorem 2. https://naomi.princeton.edu/wp-content/uploads/sites/744/2021/03/Fitch_Leonard_ECC_16_final.pdf

[3] A. S. A. Dilip, *The Controllability Gramian, the Hadamard Product, and the Optimal Actuator/Leader and Sensor Selection Problem*, IEEE Control Systems Letters 3 (2019), 883–888, DOI:10.1109/LCSYS.2019.2919278. Author's public full text: https://www.researchgate.net/publication/333408055_The_Controllability_Gramian_the_Hadamard_Product_and_the_Optimal_ActuatorLeader_and_Sensor_Selection_Problem

[4] T. H. Summers, F. L. Cortesi, and J. Lygeros, *On Submodularity and Controllability in Complex Dynamical Networks*, arXiv:1404.7665v1, 2014. https://arxiv.org/abs/1404.7665
