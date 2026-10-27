# Sharp stability and critical-damping tuning for two-component cyclic aggregated gradient

## Finding
Consider cyclic incremental aggregated gradient (IAG) for the average of two centered quadratic losses,
\[
f(x)=\tfrac12(f_1(x)+f_2(x)),\qquad f_1(x)=\tfrac12 x^{\mathsf T}Ax,\quad f_2(x)=\tfrac12x^{\mathsf T}Bx.
\]
At each iteration evaluate the component due in the alternating order \(1,2,1,2,\ldots\), retain the other component's latest gradient, and subtract \(\alpha\) times their average. Let \(A,B\) be commuting real symmetric positive-definite matrices, and let
\[
L=\max\{\lambda_{\max}(A),\lambda_{\max}(B)\}>0.
\]
After the initial pair of stored gradients is available, the IAG lifted error converges to zero from **every** two-step initial history exactly for
\[
\boxed{0<\alpha<2/L.}
\]
At \(\alpha=2/L\), at least one two-step Floquet eigenvalue equals \(-1\). For \(\alpha>2/L\), at least one mode has spectral radius greater than one.

For scalar curvatures \(a,b>0\), define
\[
S=a+b+\sqrt{ab},\qquad h_*=(S+\sqrt{S^2-ab})^{-1}.
\]
Among **all** constant steps \(\alpha>0\), the unique minimizer of the asymptotic two-step spectral radius is
\[
\boxed{\alpha_*=2h_*,\qquad \rho_*=\sqrt{ab}\,h_*.}
\]
The optimal period map has a nonsemisimple double eigenvalue \(\rho_*\). Consequently, at the optimal step its matrix powers have norm \(\Theta(m\rho_*^m)\) over \(m\) cycles; the optimality claim is for the root-asymptotic spectral rate, **not** a fixed finite-horizon norm.

## Assumptions and scope
Matrices \(A,B\) are finite-dimensional, real, symmetric, strictly positive definite, and commute. The iteration is deterministic and uses exact arithmetic, a fixed \(\alpha>0\), and one fresh gradient at each substep. No projection, proximal term, stochastic refresh, or momentum is present. We analyze convergence of the full initialized two-step linear state, not solely one specified warm start. The scalar optimization assumes \(a,b>0\) and has no dimensional dependence.

Set \(h=\alpha/2\). For the scalar mode, denote the even-cycle iterate by \(u=x_{2j}\) and its immediately preceding iterate by \(v=x_{2j-1}\). The refresh of component one and then component two yields
\[
x_{2j+1}=(1-ah)x_{2j}-bhx_{2j-1},\qquad
x_{2j+2}=(1-bh)x_{2j+1}-ahx_{2j}.
\]
This recurrence applies after the first cycle regardless of the policy for initializing the original gradient memory.

## Proof
For the state vector \((x_k,x_{k-1})^{\mathsf T}\), the scalar one-step matrices are
\[
M_a=\begin{pmatrix}1-ah&-bh\\1&0\end{pmatrix},\quad
M_b=\begin{pmatrix}1-bh&-ah\\1&0\end{pmatrix}.
\]
The two-step monodromy is \(T=M_bM_a\). Direct multiplication gives
\[
T=\begin{pmatrix}
(1-bh)(1-ah)-ah&-bh(1-bh)\\
1-ah&-bh
\end{pmatrix}.
\]
Its characteristic polynomial is \(z^2-t(h)z+d(h)\), where
\[
t(h)=1-2(a+b)h+ab h^2,\qquad d(h)=ab h^2.
\]
The strict Schur/Jury criterion for a real monic quadratic is exactly
\[
1-d(h)>0,\quad 1-t(h)+d(h)>0,\quad 1+t(h)+d(h)>0.
\]
Here these three quantities are respectively
\[
1-ab h^2,\qquad 2(a+b)h,\qquad 2(1-ah)(1-bh).
\]
For \(0<h<1/\max\{a,b\}\) all are positive. At the first endpoint the characteristic polynomial vanishes at \(z=-1\). If \(a\ne b\) and \(1/\max\{a,b\}<h<1/\min\{a,b\}\), the last Jury quantity is negative, forcing a real eigenvalue below \(-1\); above the second endpoint \(d(h)>1\). For \(a=b\), immediately beyond the sole endpoint \(d(h)>1\). This proves the scalar sharp stability threshold, including nonconvergence at equality.

For the rate optimum put \(g=\sqrt{ab}\) and \(S=a+b+g\). The smaller positive root of
\[
1-2Sh+g^2h^2=0
\]
is \(h_*=(S+\sqrt{S^2-g^2})^{-1}\), and \(0<h_*<1/S<1/\max\{a,b\}\). For \(0<h<h_*\), we have \(t(h)>2gh>0\); the two eigenvalues are positive and distinct. With \(\Delta=t^2-4g^2h^2\) and \(\lambda_+=(t+\sqrt\Delta)/2\), differentiation yields
\[
\lambda_+'(h)=\frac{t'(h)\lambda_+(h)-2g^2h}{\sqrt\Delta}<0,
\]
because \(t'(h)=-2(a+b)+2g^2h<0\) throughout this interval. At \(h=h_*\) the eigenvalues coalesce at \(gh_*\). For **every** \(h>h_*\), the eigenvalue product gives \(\rho(T(h))\ge\sqrt{d(h)}=gh>gh_*\), even outside the stable range. This proves existence and uniqueness of the global minimizer. At \(h_*\), the upper-right entry \(-bh_*(1-bh_*)\) is nonzero, so \(T(h_*)\) is not scalar and its repeated eigenvalue has a nontrivial Jordan block; the standard Jordan-power identity yields \(\Theta(m\rho_*^m)\) in operator norm.

Finally, commuting real symmetric matrices are simultaneously orthogonally diagonalizable. In the common eigenbasis the lifted period map splits as a direct sum of the scalar matrices \(T(h;a_j,b_j)\), with \(a_j,b_j>0\). The full state decays for every initialization iff each scalar block is Schur stable, equivalently
\[
0<h<\min_j\frac1{\max\{a_j,b_j\}}=\frac1L.
\]
The same scalar boundary modes prove necessity, completing the claim.

## Verification
The accompanying standard-library script `check.py` computes the monodromy from its one-step factors; checks trace, determinant, and both Jury-factor identities with exact rational arithmetic in 80 cases; and checks the stability frontier, critical-damping rate, and competing steps across 25 curvature pairs numerically. Run `python3 check.py` from the unpacked package directory. Its expected success marker is `CHECK_OK`. These finite checks are consistency tests: the proof above, not numerical enumeration, establishes the all-curvature and all-dimension statements.

For \(a=b=1\) the exact optimum is \(h_*=3-2\sqrt2\), giving \(\alpha_*=6-4\sqrt2\) and \(\rho_*=3-2\sqrt2\). The source's sufficient IAG step \(\alpha=1/(16L\tau)\) with one-step staleness \(\tau=1\) is therefore conservative on this natural test problem. The sharp stable upper limit, by contrast, is \(2/L\), a factor of \(32\) larger than that sufficient step (within the source's \(\alpha<1\) convention whenever \(L\ge2\)).

## Relationship to prior work
Zhu, Heath, and Mitra (2026), Section 4 and Theorem 4.1, give an improved **sufficient** convergence rate for IAG with bounded delay \(\tau\), using \(\alpha=1/(16L\tau)\); they do not present the sharp two-component spectral interval or its unique rate-optimal step. Gürbüzbalaban, Özdaglar, and Parrilo (2015/2017), Theorem 3.3, give a different Lyapunov-based sufficient step bound for cyclic IAG. Their introduction notes that the original Blatt–Hero–Gauchman quadratic analysis established small-step convergence without an explicit upper step bound. Mokhtari, Gürbüzbalaban, and Ribeiro (2016/2018) study the different DIAG algorithm, which averages iterates as well as gradients. The present exact period-map classification is specific to the minimal cyclic **IAG** setup and is not a claim of a new general stability theorem for all delayed-gradient algorithms.

## Limitations
No sharp statement is made for noncommuting component Hessians, nonquadratic objectives, arbitrary sampling patterns, stochastic gradients, or finite precision. The unique scalar step optimizes spectral asymptotics, not a prescribed finite iteration budget. At the optimum the monodromy is defective. An older author-hosted full-text copy of the original 2007 IAG paper could not be opened during the literature comparison; possible unindexed exact specializations remain a bibliographic risk, despite the later 2015 full-text description of its scope. Independent mathematical validation has not been performed.

## References
1. F. Zhu, R. W. Heath Jr., A. Mitra, *A Short and Unified Convergence Analysis of the SAG, SAGA, and IAG Algorithms*, arXiv:2602.05304 (first posted 2026-02-05), https://arxiv.org/abs/2602.05304.
2. M. Gürbüzbalaban, A. Özdaglar, P. A. Parrilo, *On the Convergence Rate of Incremental Aggregated Gradient Algorithms*, arXiv:1506.02081, SIAM Journal on Optimization 27 (2017), 1035–1048, https://arxiv.org/abs/1506.02081.
3. D. Blatt, A. O. Hero, H. Gauchman, *A Convergent Incremental Gradient Method with a Constant Step Size*, SIAM Journal on Optimization 18 (2007), 29–51, https://doi.org/10.1137/040615961.
4. A. Mokhtari, M. Gürbüzbalaban, A. Ribeiro, *Surpassing Gradient Descent Provably: A Cyclic Incremental Method with Linear Convergence Rate*, arXiv:1611.00347, https://arxiv.org/abs/1611.00347.
