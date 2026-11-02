# An exact mean-square stability window beyond one-step contraction for averaged two-row Kaczmarz

## Finding

Consider two nonparallel unit measurement vectors \(u,v\in\mathbb R^2\) with \(0<\rho=|u^\top v|<1\). For a consistent, full-rank two-row linear system, draw \(\eta\ge1\) rows independently and uniformly with replacement at each step and average their simultaneous Kaczmarz corrections, with a positive fixed relaxation \(\alpha\). The exact asymptotic expected squared-error contraction factor for **every nonzero deterministic initial error** is
\[
r_\eta(\alpha,\rho)=1-\alpha+\frac{\alpha^2(1+\rho^2)}4+\frac\alpha2\sqrt{\rho^2(\alpha-2)^2+\frac{\alpha^2(1-\rho^2)^2}{4\eta^2}}.
\]
It is strictly less than one exactly for
\[
0<\alpha<\alpha_{\rm ms}=\frac4{1+\sqrt{\rho^2+(1-\rho^2)/\eta^2}}.
\]
The strict uniform one-step expected squared-error contraction threshold is smaller:
\[
\alpha_{\rm step}=\frac4{1+\rho+(1-\rho)/\eta}.
\]
For each integer \(\eta\ge2\) and each \(0<\rho<1\), \(\alpha_{\rm step}<\alpha_{\rm ms}\). Between these frontiers, some starting errors have a first-step mean-square increase, but every starting error has asymptotically geometric mean-square decay. The strictly convex asymptotic-rate function has a unique minimizer \(\alpha_{\rm opt}\in(1,2)\). At the reflection step \(\alpha=2\), the rate is \(r_\eta(2,\rho)=\rho^2+(1-\rho^2)/\eta<1\) for \(\eta\ge2\).

## Assumptions and scope

Let \(A\in\mathbb R^{2\times2}\) have unit rows \(u^\top,v^\top\), with \(0<|u^\top v|<1\), and let \(b=Ax_\star\) for a unique exact solution \(x_\star\). From any deterministic \(x_0\ne x_\star\), choose independently across steps and within each batch indices \(I_{k,j}\in\{1,2\}\), each fair. The update is
\[
x_{k+1}=x_k-\frac\alpha\eta\sum_{j=1}^\eta u_{I_{k,j}}(u_{I_{k,j}}^\top x_k-b_{I_{k,j}}),\qquad \alpha>0,\quad \eta\in\mathbb N.
\]
Every correction is computed from the same \(x_k\), not sequentially. Mean-square geometric convergence means \(\mathbb E\|x_k-x_\star\|_2^2\to0\) with a geometric rate; the asymptotic rate denotes the limit of its \(k\)-th roots. One-step strict uniform contraction means \(\mathbb E[\|x_{k+1}-x_\star\|_2^2\mid x_k]<\|x_k-x_\star\|_2^2\) for every nonzero error vector.

## Proof

Flip a row sign and rotate orthogonally without changing projections, so the two normals are \(u=(\sqrt a,\sqrt d)\), \(v=(\sqrt a,-\sqrt d)\), where \(a=(1+\rho)/2\), \(d=(1-\rho)/2\), \(a+d=1\), and \(ad=(1-\rho^2)/4\). Write the rotated error as \((X_k,Y_k)\). Let \(T_k=(N_{u,k}-N_{v,k})/\eta\), the signed batch imbalance. Binomial symmetry gives \(\mathbb ET_k=0\) and \(\mathbb ET_k^2=1/\eta\). The exact error update is
\[
X_{k+1}=(1-\alpha a)X_k-\alpha\sqrt{ad}\,T_kY_k,\qquad
Y_{k+1}=(1-\alpha d)Y_k-\alpha\sqrt{ad}\,T_kX_k.
\]
The batch is independent of the past, so with \(w_k=(\mathbb E X_k^2,\mathbb E Y_k^2)^\top\), the moments obey the *exact*, not bounded, recursion
\[
w_{k+1}=B_\alpha w_k,\qquad B_\alpha=
\begin{pmatrix}
(1-\alpha a)^2&\alpha^2ad/\eta\\
\alpha^2ad/\eta&(1-\alpha d)^2
\end{pmatrix}.
\]
Consequently \(\mathbb E\|x_k-x_\star\|_2^2=(1,1)B_\alpha^k(X_0^2,Y_0^2)^\top\). For every \(\alpha>0\) the off-diagonal entries are positive. Its Perron eigenvalue \(r_\eta\) is simple, dominates the modulus of the other eigenvalue, and has strictly positive left and right eigenvectors. Every nonzero deterministic initial error has a nonzero nonnegative squared-coordinate vector, so Perron--Frobenius theory yields a strictly positive leading coefficient and the asserted exact asymptotic rate.

Taking the larger eigenvalue of \(B_\alpha\) gives the displayed radical expression. To determine its crossing of one, calculate
\[
\det(I-B_\alpha)=\alpha^2ad\bigl[4-2\alpha+\alpha^2ad(1-\eta^{-2})\bigr].
\]
The smaller positive solution for \(\eta>1\), or the unique positive solution for \(\eta=1\), is
\[
\alpha_{\rm ms}=\frac4{1+\sqrt{1-4ad(1-\eta^{-2})}}.
\]
Since \(r_\eta(0,\rho)=1\), its right derivative at zero is \(-(1-\rho)<0\), and the Perron eigenvalue is strictly convex (proved below), this is precisely the unique positive return of \(r_\eta\) to one. Below it, mean square decays geometrically; at equality it approaches a strictly positive finite limit; above it it grows exponentially for every nonzero deterministic initial error.

For conditional one-step squared norms, put \(H=(uu^\top+vv^\top)/2\), whose eigenvalues are \(a,d\). The sample-mean projector \(G=\eta^{-1}\sum_j u_{I_j}u_{I_j}^\top\) satisfies
\[
\mathbb EG=H,\qquad \mathbb EG^2=(1-\eta^{-1})H^2+\eta^{-1}H.
\]
Thus the conditional energy operator \(\mathbb E(I-\alpha G)^2\) has eigenvalues
\[
1-2\alpha\lambda+\alpha^2\lambda\bigl[(1-\eta^{-1})\lambda+\eta^{-1}\bigr],\qquad \lambda\in\{a,d\}.
\]
Both are below one exactly when \(0<\alpha<2/[a+(1-a)/\eta]=\alpha_{\rm step}\). Between \(\alpha_{\rm step}\) and \(\alpha_{\rm ms}\), choosing an error along the \(a\)-eigenvector makes the first-step expected squared error strictly increase. Strict separation follows from
\[
[\rho+(1-\rho)/\eta]^2-[\rho^2+(1-\rho^2)/\eta^2]
=2\rho(1-\rho)(\eta-1)/\eta^2>0.
\]

For uniqueness of the fastest relaxation, write \(B_\alpha=I-2\alpha\operatorname{diag}(a,d)+\alpha^2C\), where
\[
C=\begin{pmatrix}a^2&ad/\eta\\ad/\eta&d^2\end{pmatrix}\succeq0.
\]
For \(\eta>1\), \(C\) is positive definite. For \(\eta=1\), it is positive semidefinite but has strictly positive quadratic form on the positive Perron vector. The standard simple-eigenvalue second-derivative formula for the maximal eigenvalue of a symmetric matrix implies \(r_\eta''(\alpha)>0\) for all \(\alpha>0\): its first term is \(2z^\top Cz>0\), while its eigenvector-variation term is nonnegative. At \(\alpha=1\), \(B_1'=2ad\begin{pmatrix}-1&1/\eta\\1/\eta&-1\end{pmatrix}\) is negative definite for \(\eta>1\). For \(\eta=1\), direct differentiation gives \(r_1'(1)=-\rho^2(1-\rho^2)/(1+\rho^2)<0\). Directly, \(r_\eta'(2)=\rho^2+(1-\rho^2)/\eta>0\). Hence the unique global minimizer lies strictly in \((1,2)\). Substitution of \(\alpha=2\) yields the claimed reflection rate.

## Verification

The accompanying `verify.py` uses rational arithmetic to exhaustively enumerate all possible batch count outcomes for three successive iterations on three exact nonorthogonal unit-row systems, four batch sizes, five relaxations and three initial errors, comparing direct expectations of both squared coordinates with the closed two-by-two moment recursion. Its remaining checks compare the two analytic eigenvalue expressions, the exact binomial moments and the stability frontiers. Run with `python3 verify.py`; expected success line: `VERIFY_OK exact=1116 numerical=114`. This is supplementary finite checking. The all-iterate and sharp-boundary claims follow from the analytic matrix proof.

## Relationship to prior work

Moorman, Tu, Molitor and Needell introduced randomized Kaczmarz with averaging, including useful one-step conditional squared-error bounds and associated tuning rules. Tondji and Lorenz developed averaged sparse/block Kaczmarz and optimize guaranteed bounds. This result instead computes the *exact iterated annealed* squared-error dynamics for a nonorthogonal two-row system; the dominant spectral radius controls all deterministic initial errors. In particular, its asymptotic-stability endpoint differs strictly from the established uniform one-step contraction frontier when the batch size exceeds one. Agaskar, Wang and Lu previously used matrix/lifted methods for exact MSE of ordinary randomized Kaczmarz; their general approach is relevant antecedent, not claimed as a new technique. No assertion is made about general multirow or nonuniform-sampling systems.

## Limitations

This is a two-row, real, consistent, full-rank model with unit row norms, equal independent sampling with replacement, identical batch size each step, and a fixed real positive relaxation. Numerical floating-point rounding, stochastic noisy right-hand sides, inconsistent systems, sequential within-batch projection, and dimensions greater than two are not covered. The exact finite-time distribution of the error is not identified, only the complete expected squared-error recursion. Priority remains subject to independent inspection of additional sources that might contain the same two-dimensional special case.

## References

1. J. Moorman, T. Tu, D. Molitor and D. Needell, *Randomized Kaczmarz with Averaging*, arXiv:2002.04126 (2020), and 2019 conference version, `https://jacob.moorman.me/research/2019ita.pdf`.
2. L. Tondji and D. A. Lorenz, *Faster Randomized Block Sparse Kaczmarz by Averaging*, arXiv:2203.10838 (first public March 21, 2022), DOI `10.1007/s11075-022-01473-x`.
3. A. Agaskar, C. Wang and Y. M. Lu, *Randomized Kaczmarz Algorithms: Exact MSE Analysis and Optimal Sampling Probabilities* (2014), open 2014 manuscript (bibliographic URL omitted; independently verify edition).
