# Three-regime optimal tuning for a three-inner-step stochastic Lyapunov solver

## Finding
For a mean-square-stable two-state stochastic Lyapunov equation whose linear part has symmetric error modes \(\pm r\), the best constant real tuning parameter for **three inner steps** of a Smith inner–outer iteration has two sharp phase transitions, at \(r=2/5\) and \(r=1/2\). It can outperform the unrelaxed three-step Smith error factor by an entire power of \(r\) in the small-coupling regime.

Let \(q_*(r)\) denote the optimal outer-iteration Frobenius contraction factor, and let \(\alpha_*(r)\) denote its unique global minimizer over \(\mathbb R\). Then
\[
\alpha_*(r)=
\begin{cases}
\dfrac{2}{1+\sqrt{1-4r^2}},&0<r\le2/5,\\[2mm]
\dfrac{1}{2r},&2/5\le r\le1/2,\\[2mm]
1,&1/2\le r<1,
\end{cases}
\qquad
q_*(r)=
\begin{cases}
r^2\alpha_*(r)(\alpha_*(r)-1),&0<r\le2/5,\\[2mm]
\dfrac{3r-1}{4},&2/5\le r\le1/2,\\[2mm]
r^3,&1/2\le r<1.
\end{cases}
\]
At both interfaces the adjacent formulas agree; the minimizer is unique. In particular, \(q_*(r)<r^3\) for all \(0<r<1/2\), and
\[
q_*(r)=r^4+O(r^6)\qquad (r\downarrow0).
\]

## Assumptions and scope
Fix any real \(r\) with \(0<r<1\) and the swapping involution
\[
J=\begin{pmatrix}0&1\\1&0\end{pmatrix},\qquad J^2=I=J^\top J.
\]
Consider the discrete-time stochastic system \(x_{t+1}=\sqrt r\,Jx_t\omega_t\), where the scalar noises \(\omega_t\) are centered, independent of prior states, and of variance one. Its second moment decays geometrically by the factor \(r\), so the system is mean-square stable. Its Lyapunov equation for any given symmetric \(Q\succ0\) is \(X=\mathcal L_r(X)+Q\), where \(\mathcal L_r(X)=rJXJ\). The exact symmetric positive-definite solution is \(X_*=(Q+rJQJ)/(1-r^2)\).

With any fixed real scalar \(\alpha\) and arbitrary symmetric initial matrix \(X_0\), use precisely three inner stages of the Smith inner–outer recurrence of He et al. [1]:
\[
X_{k,0}=X_k,\qquad
X_{k,j+1}=\alpha\mathcal L_r(X_{k,j})
 +(1-\alpha)\mathcal L_r(X_k)+Q,\qquad j=0,1,2;
\quad X_{k+1}=X_{k,3}.
\]
Here the global objective is the worst-case **single outer-cycle** error factor \(\sup_{E=E^\top\ne0}\|\mathcal R_{\alpha,3}E\|_F/\|E\|_F\), not an average error for a selected right-hand side. The stated optimum ranges over all \(\alpha\in\mathbb R\), without a stagewise-positivity constraint. Error factors also give asymptotic spectral radii because the operator is Frobenius-self-adjoint.

## Proof
**1. Polynomial and physical modes.** Subtract the exact fixed point from each inner stage. Three substitutions give the outer error polynomial
\[
g_3(z;\alpha)=(1-\alpha)z+\alpha(1-\alpha)z^2+\alpha^2z^3.
\]
Since \(E\mapsto JEJ\) is a Frobenius-self-adjoint involution on real symmetric two-by-two matrices, the orthogonal decomposition
\[
E_+=(E+JEJ)/2,\qquad E_-=(E-JEJ)/2
\]
satisfies \(\mathcal L_r(E_+)=rE_+\) and \(\mathcal L_r(E_-)=-rE_-\). Both eigenspaces are nonzero (take \(I\) and \(\operatorname{diag}(1,-1)\)), so the precise worst-case norm is
\[
q_r(\alpha)=\max\bigl\{|g_3(r;\alpha)|,|g_3(-r;\alpha)|\bigr\}.
\]
Set \(u(\alpha)=g_3(r;\alpha)\), \(v(\alpha)=g_3(-r;\alpha)\). Direct expansion gives the two key identities
\[
u+v=2r^2\alpha(1-\alpha),\qquad
u-v=2r(1-\alpha+r^2\alpha^2),
\]
and the derivatives
\[
u'(\alpha)=-r(1-r)(1+2r\alpha),\qquad
v'(\alpha)=r(1+r)(1-2r\alpha).
\]
In particular \(u(1)=r^3\), \(v(1)=-r^3\). For \(\alpha<0\), one has \(v(\alpha)<-r\), so no negative parameter is optimal. For \(0\le\alpha\le1\), \(u(\alpha)\ge r^3\), so no such parameter beats \(\alpha=1\).

**2. Strong-coupling regime \(r\ge1/2\).** For every \(\alpha\ge1\), \(v'(\alpha)\le0\) and hence \(v(\alpha)\le-r^3\), with equality only at \(\alpha=1\). The previous paragraph bounds all remaining real parameters by at least \(r^3\). Thus the unique optimum is \(\alpha_*=1\) and \(q_*=r^3\).

**3. Intermediate regime \(2/5\le r\le1/2\).** The concave quadratic \(v\) has its unique global maximum at \(\alpha_m=1/(2r)\), where
\[
v(\alpha_m)=-(3r-1)/4,
\qquad u(\alpha_m)=(7r-3)/4.
\]
In this regime the maximum is strictly negative. Therefore, for every real \(\alpha\), \(q_r(\alpha)\ge|v(\alpha)|\ge(3r-1)/4\). The inequality \(|7r-3|\le3r-1\) holds exactly for \(2/5\le r\le1/2\), so \(\alpha_m\) attains that lower bound. Strict concavity makes the optimizer unique.

**4. Weak-coupling regime \(0<r\le2/5\).** Define
\[
\alpha_c=\frac{2}{1+\sqrt{1-4r^2}},
\]
the smaller positive root of \(1-\alpha+r^2\alpha^2=0\). Elementary algebra gives \(1<\alpha_c\le1/(2r)\) exactly on this range. At \(\alpha_c\), the two eigenmode factors agree and are negative:
\[
u(\alpha_c)=v(\alpha_c)=r^2\alpha_c(1-\alpha_c)<0.
\]
Let \(q_c=r^2\alpha_c(\alpha_c-1)\). On \([1,\alpha_c]\), the negative factor \(v\) is increasing because \(\alpha_c\le\alpha_m\), hence \(|v(\alpha)|\ge q_c\). On \([\alpha_c,\infty)\), the negative factor \(u\) strictly decreases, hence \(|u(\alpha)|\ge q_c\). For all \(\alpha<1\), the earlier bounds give \(q_r(\alpha)\ge r^3>q_c\), where the final strict inequality follows from \(v(1)=-r^3\), strict increase of \(v\) on \([1,\alpha_c)\), and \(v(\alpha_c)=-q_c\). Therefore \(\alpha_c\) uniquely minimizes \(q_r\).

The optimality formulas match at \(r=2/5\), where \(\alpha_*=5/4\) and \(q_*=1/20\), and at \(r=1/2\), where \(\alpha_*=1\) and \(q_*=1/8\). Expanding \(\alpha_c=1+r^2+2r^4+O(r^6)\) gives \(q_c=r^4+O(r^6)\). In the middle regime, strict improvement over \(r^3\) follows from
\[
r^3-(3r-1)/4=\frac{(1+r)(2r-1)^2}{4}>0\quad(2/5\le r<1/2).
\]
The proof is complete.

## Verification
The standalone \(\texttt{check.py}\) verifies the two polynomial identities and derivatives symbolically, rational interface examples, the inequality factorization, numerical minimax comparisons, and direct three-inner-stage stochastic Lyapunov recurrences on 300 reproducible symmetric test matrices. Execute \(\texttt{python check.py}\) with Python, NumPy, SymPy and SciPy. Universal minimax statements follow from the proof above, not the finite checker. For example, at \(r=2/5\), the exact optimal factor is \(1/20\), versus \(8/125\) for \(\alpha=1\); at \(r=9/20\), it is \(7/80\), versus \(729/8000\).

## Relationship to prior work
He, Su, Wang and Chen [1] introduce the stochastic-Lyapunov inner–outer algorithm, derive its general iteration polynomial (their equations (12), (14), and (18)), and explicitly analyze the second inner step; their Remark 2 and Section 4 leave higher-degree parameter tuning open. Here the polynomial itself is prior work: the new conclusion is the globally optimal **third-inner-step** parameter and sharp three-regime rate for a physically realizable signed two-mode Lyapunov operator. Chen et al. [2] study a different one-parameter explicit stochastic-Lyapunov recurrence. Tian et al. [3] investigate multi-step Smith inner–outer iterations for *continuous* coupled Markovian jump Lyapunov equations; their complete text was not available for comparison. General polynomial accelerators may attain still smaller factors because they are not restricted to this particular single-parameter recurrence.

## Limitations
The theorem concerns a two-state, variance-one multiplicative-noise stochastic system with swapping coupling, symmetric initial matrices and exact arithmetic. It does not claim that this tuning is optimal for arbitrary stochastic Lyapunov operators, nonsymmetric matrix-error norms, positivity of intermediate matrices at \(\alpha>1\), finite-precision implementations, or total work-optimal choices when inner-stage cost is included. The inaccessible complete text of [3], and incomplete full-text access to [2], leave residual bibliographic uncertainty; no independent external audit has been performed.

## References
[1] D. He, X. Su, F. Wang, X. Chen, *An Inner-Outer Iteration Algorithm with Optimal Parameters for Stochastic Lyapunov Matrix Equation*, arXiv:2607.00451, initially public 2026-07-01, https://arxiv.org/abs/2607.00451.

[2] Z. Chen, H.-J. Sun, J. Zhang, X. Chen, *Explicit iterative algorithm with optimal tuning parameter for stochastic Lyapunov matrix equation*, Numerical Algorithms 101 (2026), 679–702, DOI:10.1007/s11075-025-02019-7; originally available online in 2025.

[3] Z. Tian, J. Wang, Y. Dong, Z. Liu, *A multi-step Smith-inner-outer iteration algorithm for solving coupled continuous Markovian jump Lyapunov matrix equations*, Journal of the Franklin Institute 357 (2020), 3656–3679, DOI:10.1016/j.jfranklin.2020.02.026.
