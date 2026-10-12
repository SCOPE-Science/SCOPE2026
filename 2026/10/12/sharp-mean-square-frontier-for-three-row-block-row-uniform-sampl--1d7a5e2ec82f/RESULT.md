# Sharp mean-square frontier for three-row block-row uniform sampling beyond its safe stepsize bound

## Finding

Let \(0\leq\mu<1\), \(G_\mu=(1-\mu)I_4+\mu\mathbf 1\mathbf 1^{\mathsf T}\), and \(A_\mu=G_\mu^{1/2}\). All four rows of \(A_\mu\) have unit Euclidean norm. For the consistent linear system \(A_\mu x=0\), independently select one of the four three-element subsets \(S_t\subset\{1,2,3,4\}\) uniformly at each iteration. Perform the *simultaneous unaveraged row-correction* update

\[
x_{t+1}=x_t-A_{\mu,S_t}^{\mathsf T}A_{\mu,S_t}x_t.
\]

This is **exactly the block-row uniform sampling (BRUS) update of Du and Sun** (arXiv:2011.10353, Section 2.1.2, Algorithm 1), at block width \(\ell=3\) and absorbed stepsize \(\alpha_{\mathrm r}=1\). It is the simultaneous unaveraged sum of three standard unit-row Kaczmarz corrections. It is also representable by the *pseudoinverse-free alternative*, not the projection Algorithm 1, of Zhang--Li (arXiv:2211.16682v1): equal weights \(w_i=1/3\) and relaxation \(\alpha=3\).

Define the sharp threshold

\[
\mu_* = \frac{\sqrt 7-1}{3}=0.548583770354863\ldots.
\]

Then, with independent choices at every iteration:

1. For \(0\leq\mu<\mu_*\), \(\mathbb E\|x_t\|_2^2\to0\) geometrically for **every** deterministic \(x_0\in\mathbb R^4\).
2. At \(\mu=\mu_*\), the initial error \(x_0=\mathbf 1\) has a strictly positive limiting expected squared norm.
3. For \(\mu_*<\mu<1\), the same \(x_0=\mathbf 1\) has exponentially divergent expected squared norm.

There is a **strict stochastic-stabilization window** \(1/2<\mu<\mu_*\): every fixed three-row update matrix already has an eigenvalue with modulus \(2\mu>1\), and some initial errors increase their *expected* squared norm after one random step, yet every initial error still converges geometrically in mean square under independent resampling. More precisely, the random one-step update is expected-squared-norm nonexpansive for all inputs exactly when \(0\leq\mu\leq1/2\). For \(\mu=13/25\), initial \(x_0=\mathbf 1\) has the one-step amplification factor \(673/625>1\), although mean-square convergence holds.

## Assumptions and scope

The matrix is real, symmetric and positive definite because its two eigenvalues are \(1-\mu\), of multiplicity three, and \(1+3\mu\), of multiplicity one. Thus \(A_\mu\) is the unique real positive-definite square root and has exact row Gram matrix \(A_\mu A_\mu^{\mathsf T}=G_\mu\). The row subset is sampled independently with replacement *across iterations*, uniformly among the four distinct three-row subsets. The block correction is the unweighted sum of row corrections, with no block pseudoinverse or spectral damping. Although an illustrative BRUS pseudocode initializes the iterate at zero, any deterministic error \(e_0\) is realized by that initialization with consistent right-hand side \(b=-A_\mu e_0\) and exact solution \(x_*=-e_0\); the homogeneous formulation above is its translated error recurrence. Only this four-row equicorrelated family and this update are classified; neither general RB-SKM with a pseudoinverse nor arbitrary block stepsizes are covered.

## Proof

Write \(D_S\) for the diagonal indicator of a selected three-row subset and \(B_S=I_4-A_\mu D_SA_\mu\). In row coordinates \(y=A_\mu x\), the same update becomes \(y\mapsto (I_4-G_\mu D_S)y\). Define the covariance-transfer map

\[
\mathcal T_\mu(Y)=\frac14\sum_{|S|=3}(I_4-G_\mu D_S)Y(I_4-D_SG_\mu).
\]

The permutation-invariant plane of matrices \(Y=uI_4+v(\mathbf 1\mathbf 1^{\mathsf T}-I_4)\) is invariant under \(\mathcal T_\mu\). Directly summing the four omitted-index choices, the diagonal and common off-diagonal coefficients obey

\[
\begin{pmatrix}u_{t+1}\\v_{t+1}\end{pmatrix}=
M(\mu)\begin{pmatrix}u_t\\v_t\end{pmatrix},\qquad
M(\mu)=\begin{pmatrix}
(1+9\mu^2)/4 & 3\mu^2-3\mu/2\\
3\mu^2/2 & 7\mu^2/2-\mu
\end{pmatrix}.
\]

This recursion governs *all initial errors*, not merely exchangeable random initializations. Indeed, let \(\mathcal U(X)=\mathbb E[B_SXB_S]\), a self-adjoint linear map for the Frobenius inner product, because every \(B_S\) is symmetric. Repeated conditioning yields

\[
\mathbb E\|x_t\|_2^2=x_0^{\mathsf T}\mathcal U^t(I_4)x_0.
\]

Conjugating \(\mathcal U\) by \(A_\mu\) converts it into \(\mathcal T_\mu\). Therefore

\[
\mathcal U^t(I_4)=A_\mu^{-1}\mathcal T_\mu^t(G_\mu)A_\mu^{-1},
\]

and the recursion starts at \((u_0,v_0)=(1,\mu)\). In particular, if the spectral radius of \(M(\mu)\) is less than one, \(\mathcal U^t(I_4)\to0\), giving geometric mean-square convergence for every initial vector.

The exact characteristic data are

\[
\begin{aligned}
\operatorname{tr}M&=(23\mu^2-4\mu+1)/4,\\
\det M&=\mu(27\mu^3+7\mu-2)/8,\\
\det(I_2-M)&=3(\mu-1)(3\mu+1)(3\mu^2+2\mu-2)/8,\\
\det(I_2+M)&=(27\mu^4+53\mu^2-10\mu+10)/8.
\end{aligned}
\]

For \(0\leq\mu<\mu_*\), the three real second-order Schur/Jury inequalities hold: \(1-\det M>0\), \(\det(I_2-M)>0\), and \(\det(I_2+M)>0\). For the first, \(\mu_*<3/5\), whence

\[
\det M\leq \frac{(3/5)\left(27(3/5)^3+7(3/5)\right)}8<1.
\]

For the third, \(53\mu^2-10\mu+10>0\) by its negative discriminant, and the quartic term is nonnegative. For the second, the displayed factorization is positive exactly below the positive zero of \(3\mu^2+2\mu-2\), namely \(\mu_*\), within \([0,1)\). Thus every initial vector contracts geometrically in mean square below \(\mu_*\).

For \(\mu\geq\mu_*\), all four entries of \(M(\mu)\) are strictly positive because \(\mu_*>1/2\). At equality, \(\det(I_2-M)=0\) so the Perron eigenvalue is one. Above equality, \(\det(I_2-M)<0\), so the Perron eigenvalue exceeds one. A strictly positive Perron left eigenvector pairs positively with \((u_0,v_0)=(1,\mu)\), and positive-matrix Perron--Frobenius convergence implies that \(u_t+3v_t\) has a positive limiting value at equality and grows exponentially above it. As an explicit divergent witness, at \(\mu=3/5\) the moment matrix is \(\frac1{50}\begin{pmatrix}53&9\\27&33\end{pmatrix}\), whose Perron eigenvalue is \((43+7\sqrt7)/50>1\). For the deterministic initialization \(x_0=\mathbf1\), one has exactly

\[
\mathbb E\|x_t\|_2^2=\frac{4(u_t+3v_t)}{1+3\mu}.
\]

This proves the asserted sharp mean-square stability boundary.

Finally, another direct four-subset calculation gives

\[
\mathbb E[B_S^2]=c_\mu I_4+d_\mu(\mathbf1\mathbf1^{\mathsf T}-I_4),
\]

with eigenvalues \((18\mu^2-3\mu+1)/4\) on \(\operatorname{span}\{\mathbf1\}\) and \((2\mu^2+\mu+1)/4\) on its orthogonal complement. The latter is strictly below one for \(0\leq\mu<1\); the former is at most one exactly for \(\mu\leq1/2\), since its difference from one is \(3(2\mu-1)(3\mu+1)/4\). For any individual selected block, the nonzero spectrum of \(A_\mu D_SA_\mu\) is the spectrum of the selected row Gram matrix, namely \(1+2\mu,1-\mu,1-\mu\). Consequently \(B_S\) has eigenvalue \(-2\mu\), which is expansive exactly when \(\mu>1/2\). This establishes the strict stabilization interval and all one-step assertions.

## Verification

The companion standard-library script `verify.py` independently forms all four subset updates with exact rational arithmetic. For twelve rational values of \(\mu\) it reconstructs the entire two-dimensional transfer matrix, its characteristic identities, and both one-step eigenvalue formulas from the underlying four-by-four row Gram matrix. It verifies the rational example \(\mu=13/25\) and the transfer matrix at \(\mu=3/5\). The exact thresholds and infinitely many iterations are established by the analytic argument above, **not** by this finite set of checks. Execute with `python verify.py`.

## Relationship to prior work

Du and Sun, *Pseudoinverse-free randomized block iterative algorithms for consistent and inconsistent linear systems* (arXiv:2011.10353, Section 2.1.2, Algorithm 1), give precisely the block-row uniform sampling method studied here. Theorem 5 is a sufficient mean-square convergence theorem requiring a stepsize smaller than twice the inverse largest selected-block eigenvalue. At the absorbed step \(1\) for this family it applies only for \(\mu<1/2\), whereas the exact moment recursion proves convergence throughout \(1/2<\mu<\mu_*\). Thus the published *sufficient* stepsize ceiling is not necessary even for uniform block sampling, and randomization can stabilize individually expansive maps. No part of the present result contradicts the sufficient convergence theorem.

Zhang and Li, *Randomized block subsampling Kaczmarz--Motzkin method* (arXiv:2211.16682v1, Remark 2), describe a pseudoinverse-free weighted correction family giving the same update with relaxation \(3\) and three weights \(1/3\); their main Algorithm 1 instead employs a Moore--Penrose block pseudoinverse, so its convergence theorem does not cover the present update.

Zhang and Li's earlier block-sampling Kaczmarz--Motzkin work (arXiv:2011.06688, Algorithm 2) uses a block pseudoinverse. Necoara's *Faster randomized block Kaczmarz algorithms* (arXiv:1902.09946, Section 2.2) analyzes weighted averages of row corrections with stepsize prescriptions, not this exact sharp equicorrelation frontier at the unaveraged step. Published results on maximal-residual selection and cyclic ordering concern different operators. The exact phase boundary \(\mu_*\), the separated one-step boundary \(1/2\), and stochastic stabilization of individually expansive three-row maps do not follow from the inspected convergence bounds. These comparisons do not exclude all unindexed specialized work.

## Limitations

The update is the BRUS algorithm of Du--Sun at the absorbed unit coefficient; it does not assert failure of their sufficient convergence theorem. In the distinct optional weighted Zhang--Li formulation, the equivalent relaxation \(3\) implements the unaveraged sum and is not covered by the guarantees for its main pseudoinverse algorithm. Only four equicorrelated unit rows and independent uniform three-subset selection are classified; arbitrary row configurations, varying relaxation, nonuniform sampling and time-correlated schedules may have different thresholds. The equality-case conclusion is for the specified nonzero initialization, not a characterization of every initial vector. The exact analytic proof does not rely on finite enumeration. Specialized results outside the literature inspected may affect priority.

## References

1. K. Du and X.-H. Sun, *Pseudoinverse-free randomized block iterative algorithms for consistent and inconsistent linear systems*, arXiv:2011.10353 (first posted 20 November 2020; method/theorem checked in v2, 21 October 2021), Section 2.1.2 (BRUS Algorithm 1) and Theorem 5. https://arxiv.org/abs/2011.10353
2. Y. Zhang and H. Li, *Randomized block subsampling Kaczmarz--Motzkin method*, arXiv:2211.16682v1, 30 November 2022, Algorithm 1, Remark 2 and Theorem 1. https://arxiv.org/abs/2211.16682
3. Y. Zhang and H. Li, *Block sampling Kaczmarz--Motzkin methods for consistent linear systems*, arXiv:2011.06688, Algorithm 2. https://arxiv.org/abs/2011.06688
4. I. Necoara, *Faster randomized block Kaczmarz algorithms*, arXiv:1902.09946, Section 2.2. https://arxiv.org/abs/1902.09946
