# Unique minimax Kaczmarz sampling on forest-precision systems and topology-invariant Gaussian trees

## Finding

For a nonsingular real \(N\times N\) system \(Bx=b\), suppose all rows of \(B\) have Euclidean norm one, and the **precision matrix** \(K=(BB^{\mathsf T})^{-1}\) has off-diagonal support contained in a forest. For every fixed independent row-sampling distribution \(p\), the exact worst-direction expected one-step squared-error decrement under randomized Kaczmarz is

\[
\gamma(p)=\lambda_{\min}\bigl(B^{\mathsf T}\operatorname{diag}(p)B\bigr).
\]

Put \(d_i=K_{ii}+\sum_{j\ne i}|K_{ij}|\), and let \(T=\sum_{i=1}^N d_i=\operatorname{tr}K+2\sum_{i<j}|K_{ij}|\). Then **the unique maximizer over the entire probability simplex** and its sharp optimal decrement are

\[
\boxed{p_i^*=d_i/T,\qquad \max_p\gamma(p)=1/T.}
\]

In particular, let \(\mathcal T=(V,E)\) be *any* labeled tree on \(N\ge4\) vertices. Give each edge \(e\) an arbitrary real correlation \(\rho_e\) with \(|\rho_e|<1\), and define the unit-diagonal Gram matrix

\[
G_{ij}=\prod_{e\in P(i,j)}\rho_e,
\]

where \(P(i,j)\) is the unique tree path and an empty product is one. Every real square row matrix \(B\) with \(BB^{\mathsf T}=G\) therefore admits the unique optimal weights

\[
\boxed{
 p_i^*=\frac{1+\sum_{e\ni i}|\rho_e|/(1-|\rho_e|)}{N+2\sum_{e\in E}|\rho_e|/(1-|\rho_e|)},
 \qquad
 \gamma_* = \left(N+2\sum_{e\in E}\frac{|\rho_e|}{1-|\rho_e|}\right)^{-1}.
}
\]

For the important equal-magnitude family \(|\rho_e|=r\in[0,1)\), this simplifies to

\[
\boxed{p_i^*=\frac{1-r+r\deg_{\mathcal T}(i)}{N+(N-2)r},\qquad
\gamma_* = \frac{1-r}{N+(N-2)r}.}
\]

Thus, with size and edge-correlation magnitude fixed, **every tree topology has exactly the same sharp optimal one-step contraction** \(1-\gamma_*\), even though the uniquely optimal node probabilities depend on degree. The result allows zero and negative edge correlations.

## Assumptions and scope

The matrix \(B\) is square, real, invertible, and has nonzero unit-norm rows. The target system is consistent, and the probabilities are fixed independently and identically at each Kaczmarz iteration (the objective is the **worst-direction conditional one-step expected squared-error decrease**, not the exact long-horizon mean-square exponent or an adaptive sampling objective). The forest-precision theorem applies for any \(N\ge1\), with possibly disconnected support and isolated vertices; its tree specialization is highlighted for \(N\ge4\) to distinguish general branching from earlier small-system and single-hub cases. All \(p_i\) are allowed to be zero a priori, although the optimum is strictly positive. The named matrix \(G\) is positive definite, because it is the covariance matrix of a standardized Gaussian autoregression on the tree, as shown below. The factors \(B\) having this Gram matrix differ by a right orthogonal transformation, which does not change the claimed criterion.

## Proof

**1. Exact spectral objective and diagonal domination.** Write the error before a step as \(z=x-x_*\). Projecting against row \(b_i^{\mathsf T}\) with \(\|b_i\|_2=1\) yields

\[
\|z_{\mathrm{new}}\|_2^2=\|z\|_2^2-|b_i^{\mathsf T}z|^2.
\]

Taking the expectation over \(i\) with probabilities \(p_i\) gives the quadratic decrement \(z^{\mathsf T}B^{\mathsf T}\operatorname{diag}(p)Bz\). Therefore the minimum over \(\|z\|_2=1\) is exactly \(\gamma(p)\). For each real \(\lambda\), invertible congruence by \(B^{-1}\) gives

\[
B^{\mathsf T}\operatorname{diag}(p)B\succeq\lambda I
\quad\Longleftrightarrow\quad
\operatorname{diag}(p)-\lambda K\succeq0,
\qquad K=(BB^{\mathsf T})^{-1}.
\]

**2. Forest sign vector and universal upper bound.** Since the graph of nonzero off-diagonal \(K_{ij}\) is a forest, orienting each component from a root allows signs \(s_i\in\{-1,1\}\) satisfying \(s_is_j=\operatorname{sgn}(K_{ij})\) on every supported edge. There are no cycle-consistency constraints. Accordingly

\[
s^{\mathsf T}Ks=\operatorname{tr}K+2\sum_{i<j}|K_{ij}|=T.
\]

If \(\gamma(p)=\lambda\), the diagonal-PSD formulation gives

\[
0\le s^{\mathsf T}\bigl(\operatorname{diag}(p)-\lambda K\bigr)s=1-\lambda T.
\]

Hence \(\gamma(p)\le1/T\) for **every** distribution, without any symmetry assumption.

**3. Explicit attainable PSD certificate.** Since \(K\succ0\), every \(K_{ii}>0\), so \(d_i>0\) and \(p_i^*=d_i/T\) are valid probabilities. Let \(e_i\) denote the standard basis. Direct multiplication shows

\[
\operatorname{diag}(d)-K
 =\sum_{\{i,j\}:K_{ij}\ne0}|K_{ij}|
 \left(e_i-\operatorname{sgn}(K_{ij})e_j\right)
 \left(e_i-\operatorname{sgn}(K_{ij})e_j\right)^{\mathsf T}
 \succeq0.
\]

Thus \(\operatorname{diag}(p^*)-K/T\succeq0\), which makes \(\gamma(p^*)\ge1/T\). Together with the upper bound this proves exact optimality.

**4. Global uniqueness.** If \(p\) is any optimal distribution, the matrix \(M=\operatorname{diag}(p)-K/T\) is positive semidefinite and satisfies \(s^{\mathsf T}Ms=0\). A positive semidefinite matrix with a zero quadratic form must annihilate that vector, so \(Ms=0\). Coordinate \(i\) gives

\[
p_i=\frac{(Ks)_i}{Ts_i}=\frac{K_{ii}+\sum_{j\ne i}|K_{ij}|}{T}=\frac{d_i}{T}.
\]

Hence every optimizer is the one constructed above, even in disconnected forests or when some edge entries vanish.

**5. Tree Gaussian precision.** Choose any root of \(\mathcal T\). Let independent standard Gaussian noises be \(\xi_v\) and define recursively \(X_{\mathrm{root}}=\xi_{\mathrm{root}}\), and \(X_v=\rho_{e_v}X_{\mathrm{parent}(v)}+\sqrt{1-\rho_{e_v}^2}\,\xi_v\). Every \(X_v\) has variance one. Conditioning successively along unique paths shows \(\operatorname{Cov}(X_i,X_j)=\prod_{e\in P(i,j)}\rho_e\), even for signed or zero correlations. Since the defining linear map from the independent noises is invertible, \(G\succ0\). Expanding the Gaussian negative log density

\[
\frac12 X_{\mathrm{root}}^2+\frac12\sum_{v\ne\mathrm{root}}
\frac{(X_v-\rho_{e_v}X_{\mathrm{parent}(v)})^2}{1-\rho_{e_v}^2}
\]

produces the root-independent entries

\[
K_{ii}=1+\sum_{e\ni i}\frac{\rho_e^2}{1-\rho_e^2},\qquad
K_{ij}=\begin{cases}-\rho_e/(1-\rho_e^2),&e=\{i,j\}\in E,\\0,&\text{otherwise.}\end{cases}
\]

Therefore

\[
d_i=1+\sum_{e\ni i}
\left(\frac{\rho_e^2}{1-\rho_e^2}+\frac{|\rho_e|}{1-\rho_e^2}\right)
=1+\sum_{e\ni i}\frac{|\rho_e|}{1-|\rho_e|}.
\]

Summing over vertices counts each edge twice. This proves the tree formula in the Finding. When every edge has common absolute correlation \(r\), \(\sum_i\deg_{\mathcal T}(i)=2(N-1)\) gives the degree formula and topology independence. All conclusions remain valid at \(r=0\); no division by \(r\) was used.

## Verification

The standalone standard-library file `verify.py` carries out exact rational computations for tree sizes \(2\) through \(10\), including path, star, randomly generated trees, negative correlations, zero correlations, and unequal edge magnitudes. It constructs \(G\) by path products and \(K\) independently by tree-edge contributions, checks \(GK=I\), reconstructs the signed Laplacian sum of squares, checks the kernel sign vector, and verifies the displayed probabilities and rates. Running `python3 verify.py` produced **51,565 exact rational assertions passed**. This is finite regression coverage, **not** a substitute for the preceding all-dimensional proof. In particular the proof, rather than those checks, establishes global optimality and uniqueness.

As an exact heterogeneous example on five vertices with edge correlations \(1/2,-1/3,1/4,2/5\) on edges \(\{0,1\},\{1,2\},\{1,3\},\{3,4\}\), respectively, the law gives

\[
(p_0,p_1,p_2,p_3,p_4)=\left(\tfrac15,\tfrac{17}{60},\tfrac3{20},\tfrac15,\tfrac16\right),
\qquad \gamma_*=\tfrac1{10}.
\]

## Relationship to prior work

Strohmer and Vershynin introduced norm-weighted randomized Kaczmarz and its exponential bound. Dai, Soltanalian, and Pelckmans formalized the optimization of the one-step worst-direction contraction through an eigenvalue/semidefinite formulation (arXiv:1402.2863, section II). Gower and Richtárik gave a comprehensive randomized iterative-method framework and the corresponding general probability-selection SDP (arXiv:1506.03296, section 5.1). Those frameworks specify what must be optimized; the present claim identifies **a particular complete structural domain** where the optimum, global uniqueness, and sharp rate are given in closed form by local precision-edge data without solving an SDP.

Prior specific three-row and one-hub equicorrelation analyses already contain special instances, including stars with appropriate Gram parameters. They do not imply the claimed arbitrary-tree result or the invariance across nonisomorphic tree shapes and independently varying edge signs. A published 2014 investigation by Agaskar, Wang, and Lu studies exact multi-step MSE and annealed/quenched exponents; those long-run criteria should not be conflated with the present sharp one-step minimax criterion.

## Limitations

The criterion is **one-step worst-direction squared-error contraction** for fixed iid independent row choices; it is not a claim about the exact optimal probability law for finite-horizon MSE, quenched exponents, matrix error norms, adaptive sampling, or block Kaczmarz. The system must have unit-norm square independent rows; for nonunit rows they must first be normalized, and underdetermined or rectangular extensions are not established here. The forest sign vector and the elementary globally sharp certificate need not exist for a precision matrix whose support contains a sign-frustrated cycle; no necessity or impossibility result for cyclic sparsity is asserted. Existing general SDP machinery may derive the result when additionally combined with these graph-specific arguments, and specialized uninspected historical literature may contain an equivalent formula. No independent external mathematical audit has been performed.

## References

1. T. Strohmer and R. Vershynin, *A randomized Kaczmarz algorithm with exponential convergence*, public arXiv preprint February 8, 2007, https://arxiv.org/abs/math/0702226 .
2. L. Dai, M. Soltanalian, and K. Pelckmans, *On the Randomized Kaczmarz Algorithm*, public arXiv preprint February 12, 2014, https://arxiv.org/abs/1402.2863 , especially section II.
3. R. M. Gower and P. Richtárik, *Randomized Iterative Methods for Linear Systems*, public arXiv preprint June 10, 2015, https://arxiv.org/abs/1506.03296 , especially section 5.1.
4. A. Agaskar, C. Wang, and Y. Lu, *Randomized Kaczmarz Algorithms: Exact MSE Analysis and Optimal Sampling Probabilities*, GlobalSIP 2014, https://dash.harvard.edu/entities/publication/73120379-2750-6bd4-e053-0100007fdf3b (the accessible abstract was examined; complete text not inspected).
