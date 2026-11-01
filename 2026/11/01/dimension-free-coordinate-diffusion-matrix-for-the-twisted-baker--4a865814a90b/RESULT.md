# Dimension-free coordinate diffusion matrix for the twisted baker map

## Finding
For every integer \(M\ge 2\), the Saiki--Takahasi--Yorke twisted baker map has an **exact full spatial Green--Kubo covariance matrix** under stationary normalized Lebesgue measure. Define the centered coordinates \(u_1=x_1\) and \(u_j=x_j-1/2\) for \(2\le j\le M\), and their Birkhoff-sum vector \(S_N=\sum_{t=0}^{N-1}u\circ F^t\). Then
\[
\lim_{N\to\infty}N^{-1}\operatorname{Cov}(S_N)=V_M
=\frac1{12}\begin{pmatrix}4&-\mathbf 1^{\mathsf T}\\-\mathbf 1&I_{M-1}+\mathbf 1\mathbf 1^{\mathsf T}\end{pmatrix}.
\]
Moreover \(N^{-1/2}S_N\) converges in distribution to the centered multivariate Gaussian with covariance \(V_M\). For every \(M\), all passive-coordinate pairs have limiting Pearson correlation \(1/2\), while every first-to-passive coordinate pair has limiting correlation \(-1/(2\sqrt2)\); these values do not depend on either coordinate indices or dimension.

The \(M-2\) passive-coordinate difference modes all have diffusion eigenvalue \(1/12\). The remaining two eigenvalues are
\[
\lambda_\pm(M)=\frac{M+4\pm\sqrt{M^2-4M+12}}{24}.
\]
This positive-definite diffusion geometry exhibits an exchangeable passive block even though the map itself cycles passive coordinates in a fixed order. In particular, \(\lambda_+(M)\sim M/12\) and \(\lambda_-(M)\to1/4\).

## Assumptions and scope
The phase space is \(X_M=[-1,1]\times[0,1]^{M-1}\), and the map is exactly
\[
F(x_1,\ldots,x_M)=
\begin{cases}
(1+2x_1,x_2,\ldots,x_M),&x_1<0,\\
(1-2x_M,x_1,\ldots,x_{M-1}),&x_1\ge0.
\end{cases}
\]
The initial point is distributed according to the normalized product Lebesgue measure \(m\); thus \(u_1\) has variance \(1/3\), and each other \(u_j\) has variance \(1/12\). Components are initially independent. The map preserves \(m\) because every interior point has two full branches with Jacobian magnitude \(2\), and \((F,m)\) is mixing, indeed Bernoulli, by the source paper. All limits are for fixed \(M\) as \(N\to\infty\); the final eigenvalue comparisons separately take \(M\to\infty\).

## Proof
Write \(\mathcal P\) for the Perron--Frobenius operator with respect to \(m\). The two inverse branches, at an image point \(y\), are
\[
L(y)=((y_1-1)/2,y_2,\ldots,y_M),\quad
R(y)=(y_2,\ldots,y_M,(1-y_1)/2),
\]
and therefore \(\mathcal Pf=(f\circ L+f\circ R)/2\). The centered affine span is invariant, with
\[
\mathcal Pu_1=\tfrac14u_1+\tfrac12u_2,\qquad
\mathcal Pu_j=\tfrac12(u_j+u_{j+1})\quad(2\le j<M),\qquad
\mathcal Pu_M=\tfrac12u_M-\tfrac14u_1.
\]
Let \(B\) be the coefficient matrix of these relations, so that \(\mathcal Pu=Bu\). Since \(m\) is mixing, every matrix coefficient of \(B^n\) tends to zero: \(\langle\mathcal P^n u_i,u_j\rangle\to0\). In this finite-dimensional invariant space, \(\rho(B)<1\).

Define \(H=(I-B)^{-1}B=\sum_{n\ge1}B^n\). Its complete entries can be written without matrix inversion:
\[
H_{11}=0,\quad H_{1j}=1\ (j\ge2),\quad H_{i1}=-\tfrac12\ (i\ge2),\quad
H_{ij}=\begin{cases}-\tfrac12,&2\le j<i,\\\tfrac12,&j=i\ge2,\\\tfrac32,&i\ge2,\ j>i.\end{cases}
\]
A direct row-by-row multiplication verifies \((I-B)H=B\). Set the vector-valued bounded affine function \(h=Hu\), and \(d=u+h-h\circ F\). By the Poisson identity, \(\mathcal Pu+\mathcal Ph=h\), while \(\mathcal P(h\circ F)=h\). Hence \(\mathcal Pd=0\). The sequence \(d\circ F^t\) is a stationary reverse-martingale-difference sequence for the decreasing future filtration. Moreover,
\[
S_N=\sum_{t=0}^{N-1}d\circ F^t-h+h\circ F^N,
\]
so the difference of the Birkhoff sums is bounded, independently of \(N\). The bounded reverse-martingale central limit theorem (or the usual natural-extension formulation), together with mixing/ergodicity, gives a multivariate Gaussian limit with covariance \(\int dd^{\mathsf T}\,dm\).

For an entirely explicit coefficient calculation, put \(D=\int uu^{\mathsf T}\,dm=\operatorname{diag}(1/3,1/12,\ldots,1/12)\). The absolutely summable Green--Kubo series is
\[
V_M=D+\sum_{n\ge1}\bigl(B^nD+D(B^{\mathsf T})^n\bigr)=D+HD+DH^{\mathsf T}.
\]
Insertion of the displayed entries of \(H\) gives \((V_M)_{11}=1/3\), \((V_M)_{1j}=-1/12\) for \(j\ge2\), \((V_M)_{ii}=1/6\) for \(i\ge2\), and \((V_M)_{ij}=1/12\) for distinct \(i,j\ge2\). These four cases prove the block formula and the stated pairwise correlations.

On the \((M-2)\)-dimensional subspace \(\{(0,z):\sum_jz_j=0\}\), the matrix \(12V_M\) acts as identity. On its orthogonal complement, in the basis consisting of the first coordinate and the normalized passive sum, it is
\[
\begin{pmatrix}4&-\sqrt{M-1}\\-\sqrt{M-1}&M\end{pmatrix}.
\]
Its trace is \(M+4\) and determinant \(3M+1>0\), proving both remaining eigenvalue formulas and strict positive definiteness. Expansion of the square root proves the claimed large-dimension behavior.

## Verification
The standalone `verify.py` uses exact rational arithmetic and only the Python standard library. It checks the branch-transfer identities for all \(2\le M\le9\) at five rational points per dimension, and independently checks \((I-B)H=B\) and \(V_M=D+HD+DH^{\mathsf T}\) for every \(2\le M\le30\). It executed successfully. These finite checks are diagnostics; the row formulas, martingale argument, and eigenvalue calculation above establish the theorem for all dimensions.

## Relationship to prior work
Saiki, Takahasi and Yorke introduced this exact piecewise-affine family and proved Lebesgue invariance, Bernoulli mixing, and periodic-orbit properties. Those foundational facts are premises here, not new conclusions. A previously established calculation of the first-coordinate temporal covariance gives the \((1,1)\) entry, but a univariate law does not determine the mixed entries, passive-coordinate block, exchangeable diffusion geometry, or full multivariate central limit. Periodic-orbit real/complex eigenvalue distributions concern derivative cocycles and do not imply additive coordinate covariance. The contribution is the complete dimension-uniform joint fluctuation matrix, its correlations, and its diffusion spectrum.

## Limitations
This theorem concerns the specific centered coordinate observables and the stationary Lebesgue measure; it does not assert the same covariance for other invariant measures, higher-degree observables, nonstationary starts, or a joint limit when dimension grows simultaneously with observation time. The finite verification range is not an exhaustive infinity check. A differently named or unindexed prior computation of this full matrix could affect publication novelty; none was identified in the inspected sources.

## References
1. Y. Saiki, H. Takahasi, and J. A. Yorke, *The twisted baker map*, arXiv:2202.04304, first posted 2022-02-09, https://arxiv.org/abs/2202.04304; accessible complete author preprint https://arxiv.org/html/2202.04304v3; journal DOI https://doi.org/10.1088/1361-6544/acb4d3.
2. Standard bounded stationary martingale-difference central limit theorem (used after the explicitly derived Perron coboundary decomposition); no new general probabilistic limit theorem is claimed.
