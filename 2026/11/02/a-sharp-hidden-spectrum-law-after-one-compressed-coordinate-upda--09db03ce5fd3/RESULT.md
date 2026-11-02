# A sharp hidden-spectrum law after one compressed coordinate update

## Finding

A single exact coordinate-descent step, starting from the prescribed reference determinant and using entrywise compression of previously untouched matrix-vector entries, can produce an **identically zero stored gradient** while the true gradient is nonzero and the spectral-energy underestimate is strictly positive. In a natural two-active-coordinate plus unseen-leaves family, the largest possible hidden ground-state correction has an exact scalar characterization depending only on the compression threshold, the number of unseen coordinates, and a lower bound on the unseen block.

Fix \(0<s<1\), \(\gamma>0\), an integer \(m\ge1\), and threshold \(\tau>0\). Put \(A=1+s^2\) and
\[
H=\begin{pmatrix}-1&-s&0\\-s&-s^2&v^{\mathsf T}\\0&v&D\end{pmatrix},\qquad D=D^{\mathsf T}\succeq\gamma I_m,
\quad v\in\mathbb R^m,\quad |s v_j|\le\tau\ (1\le j\le m).
\]
For the objective \(f(c)=\|H+cc^{\mathsf T}\|_F^2\), initialize \(c^{(0)}=e_0\) and the **exact** stored vector \(b^{(0)}=He_0\). Select coordinate \(1\) by its nonzero initial gradient, perform exact line minimization, and drop updates \(\alpha H_{j1}\) to previously zero leaf entries whenever \(|\alpha H_{j1}|\le\tau\), preserving all entries on the active support. Then the unique step is \(\alpha=s\), and
\[
c^{(1)}=(1,s,0_m)^{\mathsf T},\quad
b^{(1)}=(-A,-sA,0_m)^{\mathsf T},\quad
4\bigl(b^{(1)}+\|c^{(1)}\|_2^2c^{(1)}\bigr)=0,
\]
although the actual gradient is \(4(0,0,s v)^{\mathsf T}\), with sharp size \(4s\|v\|_2\le4\sqrt m\tau\). The active-subspace Rayleigh energy is \(-A\).

If \(v\neq0\), write the full minimum eigenvalue as \(\lambda_{\min}(H)=-L\), \(L>A\), and its missing energy correction as \(\Delta=L-A\). Define \(L_*>A\) as the unique solution to
\[
\boxed{\frac{L_*(L_*-A)(\gamma+L_*)}{L_*-1}=\frac{m\tau^2}{s^2}.}
\]
Then the **sharp universal bound** is
\[
\boxed{0<\Delta\le L_*-A,}
\]
with equality for \(D=\gamma I_m\) and \(|v_j|=\tau/s\) for every leaf. Equivalently, for every prescribed energy tolerance \(\eta>0\), all such matrices satisfy \(\Delta\le\eta\) if and only if
\[
\boxed{m\tau^2\le\frac{s^2(A+\eta)\eta(\gamma+A+\eta)}{A+\eta-1}.}
\]
When \(v=0\), the correction is exactly zero, and the same upper bound remains valid.

In particular, with \(s=1/2\), \(\gamma=1\), \(m=r^2\), \(v_j=1/r\) and \(\tau=1/(2r)\), the stored gradient is zero after the legitimate first update for every integer \(r\ge1\), whereas \(\tau\to0\) and \(\Delta\) is a fixed positive constant. The active and ground energies are independent of \(r\), as is the operator norm of \(H\). Thus a dimension-independent spectral-error bound tending to zero with \(\tau\) is impossible for this family without a sparsity/decay or aggregate-tail hypothesis.

## Assumptions and scope

The matrix is an abstract real symmetric eigenproblem, not an assertion that every such matrix is a molecular Hamiltonian. The compression rule is applied only to **new** entries of the stored \(b\) vector; already stored nonzero/active entries remain exact. The theorem concerns the state after one exact coordinate line search, not a claim that a particular implementation's full multistep stopping rule must terminate there. The energy comparison concerns the smallest eigenvalue of \(H\) versus the Rayleigh quotient of \(c^{(1)}\).

The exclusion of \(s=0\) ensures the first gradient chooses the bridge, while \(s<1\) gives strict convexity of that coordinate line subproblem. Zero updates at the threshold are assumed discarded; choosing all inequalities strictly below \(\tau\) gives the corresponding arbitrarily close sharp supremum if an implementation keeps equality.

## Proof

1. Initially \(b^{(0)}=(-1,-s,0_m)^{\mathsf T}\), \(\|c^{(0)}\|_2^2=1\), so the stored and true objective gradients are \(4(0,-s,0_m)^{\mathsf T}\). Coordinate \(1\) is the unique nonzero-gradient eligible coordinate, connected to reference coordinate \(0\) by \(H_{01}=-s\).

2. On \(c=e_0+\alpha e_1\), the derivative is
\[
\tfrac14\frac{d}{d\alpha}f(e_0+\alpha e_1)=\alpha^3+(1-s^2)\alpha-s.
\]
Its derivative is \(3\alpha^2+1-s^2>0\); substitution shows \(\alpha=s\) is the unique global minimizer. Hence \(c^{(1)}=(1,s,0_m)^{\mathsf T}\), of squared norm \(A\).

3. The exact update on active entries is \((-A,-sA)\). Each untouched leaf would receive \(s v_j\), but is discarded because \(|s v_j|\le\tau\). Consequently the stored gradient is exactly zero. Direct multiplication by the uncompressed \(H\) gives the true gradient \(4(0,0,s v)\). Cauchy–Schwarz bounds its norm by \(4\sqrt m\tau\), attained at equal-magnitude saturated entries. Restricting \(H\) to the first two coordinates gives \(-uu^{\mathsf T}\), \(u=(1,s)\), with minimum eigenvalue \(-A\).

4. Suppose \(v\neq0\). Since the Rayleigh quotient of \(u\) in the active plane equals \(-A\) and it is coupled to a nonzero leaf vector, the minimum eigenvalue strictly lies below \(-A\) (take an arbitrarily small leaf perturbation with sign lowering the quotient). Therefore \(L>A\), and \(D+LI_m\) is positive definite. Eliminating the leaf variables in \((H+LI)x=0\) yields the two-by-two Schur matrix
\[
\begin{pmatrix}L-1&-s\\-s&L-s^2-v^{\mathsf T}(D+LI_m)^{-1}v\end{pmatrix}.
\]
Its determinant vanishes, giving the **exact secular equation**
\[
L(L-A)=(L-1)v^{\mathsf T}(D+LI_m)^{-1}v.
\]
The spectral assumption on \(D\) gives \(v^{\mathsf T}(D+LI_m)^{-1}v\le\|v\|_2^2/(\gamma+L)\le m\tau^2/[s^2(\gamma+L)]\).

5. The function \(\Phi(L)=L(L-A)(\gamma+L)/(L-1)\) increases strictly on \(L>A\): its logarithmic derivative is \(1/L+1/(L-A)+1/(\gamma+L)-1/(L-1)>0\) because \(A>1\). It increases continuously from zero to infinity, so \(L_*\) exists uniquely and \(L\le L_*\). If \(D=\gamma I_m\) and each \(|v_j|=\tau/s\), both inequalities become equality; conversely its secular equation identifies \(L=L_*\), proving attainment. Monotonicity yields the displayed necessary-and-sufficient tolerance condition by evaluating \(\Phi(A+\eta)\).

6. In the sequence \(m=r^2\), \(v_j=1/r\), the coupling has Euclidean norm one and only the normalized all-ones leaf mode is coupled to the active block. The nontrivial spectral block is always
\[
K=\begin{pmatrix}-1&-1/2&0\\-1/2&-1/4&1\\0&1&1\end{pmatrix},
\]
while the other \(m-1\) eigenvalues are \(1\). Its smallest eigenvalue is strictly below \(-5/4\), independently of \(r\); the remaining eigenvalues stay bounded. Thus \(\Delta>0\) and the full operator norm remain fixed as \(\tau=1/(2r)\) vanishes.

## Verification

`checker.py` directly constructs the full matrix and verifies exact first-step support, compressed and true gradients, the secular equation and extremal sharpness. It tests the scalar worst-case law for rational parameters, randomized symmetric \(D\succeq\gamma I\), and the fixed-norm family. The infinite-dimensional sequence is established by orthogonal block decomposition in the proof, not by finite sampling. The inequalities and monotonicity are analytic; the script is supporting evidence rather than a substitute for proof.

## Relationship to prior work

Li and Wu (arXiv:2607.24319v1, 2026) analyze compressed coordinate descent for FCI and give error estimates under decay assumptions. Wang, Li and Lu (arXiv:1902.04592, 2019) specify the reference-vector initialization, coordinate selection and compressed \(b\)-update which this construction respects. The 2025 parallel multicoordinate adaptation also explicitly explains that updates are discarded only on previously unselected coordinates, so the Rayleigh quotient stays exact on the retained subspace.

Small eigenpair residuals and missing extremality information are classical topics, as are Schur-complement eigenvalue bounds. This finding does **not** claim novelty for those identities alone; its claim is the exact reachable one-update compressed-gradient state, sharp finite-threshold energy frontier with dimension, and fixed-operator-norm vanishing-threshold obstruction. The previously published projected-eigenpair false-positive example concerns the opposite mechanism—an exact zero residual at a **nonextremal** stationary eigenvector—not an **inexact stored gradient** at a true nonstationary vector. Likewise, cover-transversal contamination in SM3 concerns compressed adaptive gradient history, not spectral truncation and extremal-eigenvalue bias.

## Limitations

The construction is adversarial and its star degree grows with \(m\). It does not refute results imposing decay, bounded degree, or control of the aggregate discarded residual. A full production CDFCI iteration can use additional stopping tests, recomputation, or later coordinate selection. The one-update result proves that zero **stored** gradient alone is not a certificate of full-space stationarity or spectral accuracy. The sharp energy law applies to the displayed matrix class, not all symmetric matrices. Historical uniqueness cannot be conclusively established; a prior specialized star-resolvent estimate may imply the scalar bound, though it would not automatically include the stated method-reachable compressed iterate.

## References

1. Y. Li and Q. Wu, *The Convergence and Error Analysis of Coordinate Descent Methods with Compression for Full Configuration Interaction*, arXiv:2607.24319v1 (first public July 27, 2026), https://arxiv.org/abs/2607.24319.
2. Z. Wang, Y. Li, and J. Lu, *Coordinate Descent Full Configuration Interaction*, arXiv:1902.04592 (2019), https://arxiv.org/abs/1902.04592.
3. *Parallel Multicoordinate Descent Methods for Full Configuration Interaction*, *J. Chem. Theory Comput.* 21 (2025), https://pubs.acs.org/jctcce/article/21/5/2325/3693048/Parallel-Multicoordinate-Descent-Methods-for-Full.
4. W. Gao, Y. Li, and H. Shen, *Weighted Trace-Penalty Minimization for Full Configuration Interaction*, *SIAM J. Sci. Comput.* 46 (2024), A179–A203, https://doi.org/10.1137/23M1547676.
