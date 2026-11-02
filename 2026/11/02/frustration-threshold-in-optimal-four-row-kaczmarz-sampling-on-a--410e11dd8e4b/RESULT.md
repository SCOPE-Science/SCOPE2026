# Frustration threshold in optimal four-row Kaczmarz sampling on a signed inverse-Gram cycle

## Finding

Consider an invertible real \(4\times4\) matrix \(A\) with unit Euclidean norm in each row. Put \(G=AA^{\mathsf T}\), \(C=G^{-1}\), and suppose, for some \(w>0\), \(t>0\), that
\[
C_{12}=C_{23}=C_{34}=w,\qquad C_{14}=-tw,\qquad C_{13}=C_{24}=0.
\]
There is no restriction on the four diagonal entries beyond the displayed Gram-inverse conditions. In particular, the signed off-diagonal support is a frustrated four-cycle.

For independent fixed row sampling with probabilities \(p_i\), the unique distribution minimizing the worst conditional expected *squared Euclidean error* after a single exact Kaczmarz projection is
\[
p_i^*=q_i/T,\quad T=\sum_{j=1}^4q_j,
\]
with
\[
(q_1,q_2,q_3,q_4)=
\begin{cases}
(C_{11}+w(1-t),\ C_{22}+2w,\ C_{33}+2w,\ C_{44}+w(1-t)),&0<t\le1/3,\\
(C_{11}+2twc,\ C_{22}+2wc,\ C_{33}+2wc,\ C_{44}+2twc),&t\ge1/3,
\end{cases}
\qquad c=\sqrt{\frac{t+1}{4t}}\ \ (t\ge1/3).
\]
Both expressions coincide at \(t=1/3\). The sharp maximal one-step expected energy-decrement eigenvalue is \(1/T\); the minimal worst expected squared-error contraction factor is therefore \(1-1/T\). Explicitly,
\[
T=\sum_i C_{ii}+w\begin{cases}
6-2t,&0<t\le1/3,\\
2(t+1)^{3/2}/\sqrt t,&t\ge1/3.
\end{cases}
\]
At \(t=1/3\), the optimal dual correlation certificate changes from collinear to planar. The threshold is independent of the diagonal entries, and the optimal probabilities remain unique across the transition.

## Assumptions and scope

The system \(Ax=b\) is square, real, invertible and consistent, and all rows of \(A\) have unit norm. One row \(i\) is selected independently with fixed distribution \(p\) at each step and the error \(e\) is updated by the orthogonal projection \(e\mapsto (I-a_i a_i^{\mathsf T})e\). This result optimizes the sharp bound \(\sup_{e\ne0}\mathbb E\|e^+\|_2^2/\|e\|_2^2\) **for a single step**, not the exact average MSE at later steps or an adaptive policy. Row signs can be changed without changing the Kaczmarz projections. The theorem uses a labelling in which the unique negative off-diagonal edge is \(\{1,4\}\) and three positive ones form the path \(1-2-3-4\).

The hypotheses describe a nonempty family: for any fixed \(t>0\), set \(C=\operatorname{diag}(a,b,b,a)+wH_t\), where \((H_t)_{12}=(H_t)_{23}=(H_t)_{34}=1\), \((H_t)_{14}=-t\), the matrix is symmetric, and all other entries of \(H_t\) vanish. At \(w=0\), \(a=b=1\) gives \(\operatorname{diag}(C^{-1})=\mathbf1\); the derivative of the two independent diagonal equations with respect to \((a,b)\) is \(-I_2\). The implicit-function theorem therefore gives positive-definite, unit-row Gram realizations for sufficiently small \(w>0\). An explicit example for \(t=1\) is \(C=aI+wH_1\), \(w=1/4\), \(a=(1+\sqrt{1+8w^2})/2\), for which \(H_1^2=2I\) and \(\operatorname{diag}(C^{-1})=\mathbf1\).

## Proof

**1. Exact optimization reformulation.** For a fixed error \(e\), the one-step mean squared norm is
\[
\mathbb E\|e^+\|_2^2=e^{\mathsf T}(I-A^{\mathsf T}\operatorname{diag}(p)A)e.
\]
Its sharp worst contraction is \(1-\lambda_{\min}(A^{\mathsf T}\operatorname{diag}(p)A)\). Since \(G=AA^{\mathsf T}\) is positive definite, the nonzero eigenvalues equal those of \(G^{1/2}\operatorname{diag}(p)G^{1/2}\). Thus \(\lambda_{\min}\ge\lambda\) exactly when \(\operatorname{diag}(p)\succeq\lambda C\). Writing \(q=p/\lambda\), optimizing over the simplex is equivalent to the diagonal-majorant semidefinite program
\[
T_* =\min_{q\in\mathbb R^4}\left\{\sum_i q_i:\operatorname{diag}(q)-C\succeq0\right\}.
\]
Its dual is \(\max\{\operatorname{tr}(CX):X\succeq0,\ \operatorname{diag}X=\mathbf1\}\). Strict primal feasibility gives equality of the optimal values. Every primal feasible \(q\) has \(q_i\ge C_{ii}>0\), and \(p=q/T_*\) is a valid positive probability vector when \(q\) is optimal.

**2. Collinear regime.** For \(0<t\le1/3\), choose the displayed \(q\) and \(X=\mathbf1\mathbf1^{\mathsf T}\). Write \(S=\operatorname{diag}(q)-C\). Reversal of the four-vertex path decomposes the matrix \(S/w\) into the two real symmetric \(2\times2\) blocks
\[
B_+=\begin{pmatrix}1&-1\\-1&1\end{pmatrix},\qquad
B_-=\begin{pmatrix}1-2t&-1\\-1&3\end{pmatrix}.
\]
The first is positive semidefinite; the second has positive diagonal and determinant \(2-6t\ge0\). Hence \(S\succeq0\). Moreover \(S\mathbf1=0\), so \(SX=0\), and
\(\sum_iq_i=\operatorname{tr}(CX)\). These are matching primal and dual certificates.

**3. Planar regime.** For \(t\ge1/3\), let \(c=\sqrt{(t+1)/(4t)}\in(1/2,1]\) and \(\theta=\arccos(c)\). Take the displayed \(q\) and set \(X_{ij}=\cos((i-j)\theta)\). As the Gram matrix of four planar unit vectors with successive angles \(\theta\), this \(X\) is positive semidefinite with unit diagonal. Now \(S/w\) decomposes under the same reversal into
\[
B_+=\begin{pmatrix}t(2c+1)&-1\\-1&2c-1\end{pmatrix},\qquad
B_-=\begin{pmatrix}t(2c-1)&-1\\-1&2c+1\end{pmatrix}.
\]
Both have nonnegative diagonal and determinant \(t(4c^2-1)-1=0\), hence \(S\succeq0\). The identities \(\cos3\theta=c(1-2t)/t\) and \(\sin\theta=t\sin3\theta\) imply \(SX=0\) (equivalently, \(S\) annihilates the cosine and sine coordinate vectors). Thus primal and dual objectives again agree. Summing the four components of \(q\) gives the stated value of \(T\).

**4. Uniqueness.** Let \(q'\) be any optimal majorant. For the exhibited optimal dual \(X\), complementary slackness gives \((\operatorname{diag}(q')-C)X=0\), because both matrices are positive semidefinite and their trace pairing vanishes. In the first regime \(X=\mathbf1\mathbf1^{\mathsf T}\); its diagonal entries give \(q'_i=\sum_j C_{ij}\), which is exactly the displayed \(q_i\). In the second regime, write \(X_{ij}=v_i\cdot v_j\) with unit planar vectors \(v_i\); taking the inner product of the \(i\)-th equation with \(v_i\) yields
\[
q'_i=\sum_j C_{ij}(v_i\cdot v_j),
\]
again giving the displayed values. The transition point belongs to either formula. Hence \(q\) and the derived \(p\) are unique.

## Verification

The self-contained source file `verify_signed_cycle.py` replays exact rational certificates for \(t=1/10,1/5,1/3,4/5,9/7,25/11\), checks primal-dual equality, every principal minor of both certificates, and complementary slackness. It also verifies an explicit normalized Gram instance and numerically constructs further normalized instances on both sides of the transition; it compares their predicted contraction eigenvalues with actual spectra and with randomly sampled competing distributions. Run `python verify_signed_cycle.py` with Python 3, NumPy, SymPy and SciPy installed. These finite checks corroborate, but do not replace, the parameter-uniform argument above.

## Relationship to prior work

Classical randomized Kaczmarz theory and weighted row-selection analysis are due to Strohmer–Vershynin and Needell–Srebro–Ward. Agaskar–Wang–Lu studied exact MSE and optimization of selection probabilities. Semidefinite correlation-matrix geometry, including low-rank elliptope representations and cycle elliptopes, has independent prior literature. The contribution stated here is the exact normalized four-row **inverse-Gram signed-cycle** probability law, its one-third frustration threshold and unconditional optimizer uniqueness. It is not a new general semidefinite-programming duality theorem nor a theorem about long-horizon annealed/quenched error exponents.

## Limitations

The theorem covers only square four-row systems with the specified inverse-Gram conditional-correlation support and ratio; it does not handle arbitrary weighted signed cycles, rectangular systems, finite-horizon multi-step MSE or adaptive policies. The 2014 exact-MSE paper was identified but its complete text was not accessible in this review. Prior cycle-elliptope geometry gives general structural context and could limit novelty of the dual construction; no independent mathematical audit has been performed.

## References

1. D. Needell, N. Srebro and R. Ward, *Stochastic Gradient Descent, Weighted Sampling, and the Randomized Kaczmarz algorithm*, first arXiv public version 21 October 2013, arXiv:1310.5715v1, https://arxiv.org/abs/1310.5715.
2. T. Strohmer and R. Vershynin, *A randomized Kaczmarz algorithm with exponential convergence*, Journal of Fourier Analysis and Applications 15 (2009), 262–278, https://doi.org/10.1007/s00041-008-9030-4.
3. A. Agaskar, C. Wang and Y. M. Lu, *Randomized Kaczmarz algorithms: Exact MSE analysis and optimal sampling probabilities*, GlobalSIP 2014, https://doi.org/10.1109/GlobalSIP.2014.7032145.
4. M. Nagy, M. Laurent and A. Varvitsiotis, *Forbidden minor characterizations for low-rank optimal solutions to semidefinite programs over the elliptope*, Journal of Combinatorial Theory B 108 (2014), 40–80, https://doi.org/10.1016/j.jctb.2014.02.011.
5. M. Laurent, F. M. Mascarin and S. Telen, *The Algebraic Boundary of Graph Elliptopes*, arXiv:2605.02484v1 (4 May 2026), https://arxiv.org/abs/2605.02484.
