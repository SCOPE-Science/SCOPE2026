# Exact stationary feasibility risk and penalty tuning for scalar stochastic MALM

## Finding

For the scalar stochastic momentum augmented-Lagrangian (MALM) recurrence below, put \(t=\beta/\eta\). A finite limiting feasibility second moment exists precisely for \(0<t<4/3\), in which case
\[
\lim_{r\to\infty}\mathbb E[x_r^2]=\frac{\sigma^2}{\eta^2}\frac{2\alpha^2[2-\alpha-(1-\alpha)t]}{t(2-\alpha)(4-3t)[\alpha^2+(1-\alpha^2)t]}.
\]
At and beyond \(t=4/3\), nondegenerate gradient noise makes \(\mathbb E[x_r^2]\) diverge to infinity. For fixed \(\eta,\sigma^2\) and \(0<\alpha<1\), the stationary risk has exactly one minimizing penalty ratio, the unique zero in \((2/3,1)\) of
\[
-\frac{1-\alpha}{2-\alpha-(1-\alpha)t}-\frac1t+\frac3{4-3t}-\frac{1-\alpha^2}{\alpha^2+(1-\alpha^2)t}=0.
\]
The minimizer tends to \(1\) as \(\alpha\downarrow0\), and to \(2/3\) as \(\alpha\uparrow1\). The value \(4/3\) is inherited from the deterministic scalar primal–dual iteration; the result concerns the forced second moment and its penalty optimum.

## Assumptions and scope

Minimize \(f(x)=0\) for \(x\in\mathbb R\), subject to \(x=0\). Let \(\eta,\beta>0\) and \(0<\alpha<1\) be constant. The oracle noises \(\xi_{r+1}\), \(r\ge0\), are independent and identically distributed with mean zero and variance \(\sigma^2\in(0,\infty)\), independent of the initial state, which has finite second moment. The updates are
\[
\begin{split}
x_{r+1}&=x_r-\eta^{-1}(m_r+\lambda_r+\beta x_r),\\
\lambda_{r+1}&=\lambda_r+\beta x_{r+1},\\
m_{r+1}&=(1-\alpha)m_r+\alpha\xi_{r+1}.
\end{split}
\]
These are Eqs. (5)–(7) of Qiu, Maithripala, and Lin with constraint operator 1, right-hand side 0, and an additive gradient oracle. Their Algorithm 1 is fixed-parameter within a run; their finite-horizon convergence theorem selects parameters as functions of the planned horizon. Here the parameters are held fixed as the number of iterations tends to infinity. The analysis measures feasibility, not KKT iteration complexity.

## Proof

Set \(a=\alpha\), \(e=1-a\), \(d=2-a\), \(u_r=\lambda_r/\eta\), \(v_r=m_r/\eta\), and \(z_r=(x_r,u_r,v_r)^{\mathsf T}\). Then \(z_{r+1}=Mz_r+a\eta^{-1}\xi_{r+1}e_3\), where \(e_i\) denotes a standard basis vector and
\[
M=\begin{pmatrix}1-t&-1&-1\\t(1-t)&1-t&-t\\0&0&e\end{pmatrix}.
\]
Its characteristic polynomial at \(z\) is \((z-e)Q_t(z)\), where \(Q_t(z)=z^2-2(1-t)z+(1-t)\). The real quadratic Schur conditions are \(t>0\), \(4-3t>0\), and \(|1-t|<1\), jointly equivalent to \(0<t<4/3\). Since \(0<e<1\), this is the strict stability interval for \(M\).

In the stable interval the mean tends to zero, and the stationary covariance, normalized by \(\sigma^2/\eta^2\), solves \(C=MCM^{\mathsf T}+a^2 e_3e_3^{\mathsf T}\). This solution is unique: iteration sums the covariance contributions of independent noise increments, the sum converges because \(M\) is Schur stable, and the propagated initial covariance tends to zero.

Write \(D=a^2+(1-a^2)t\) and \(X=C_{11}\). The scalar momentum variance satisfies \(C_{33}=e^2C_{33}+a^2\), so \(C_{33}=a/d\). Let \(A_0\) be the upper-left two-by-two block of \(M\). The normalized cross-covariances \((C_{13},C_{23})^{\mathsf T}\) solve a system with coefficient \(I-eA_0\) and right side \(-e(1,t)^{\mathsf T}C_{33}\). Its determinant is \(D\), and solution is
\[
C_{13}=-a^2e/(dD),\qquad C_{23}=-ate/(dD).
\]
For the remaining entries use \(u'=u+tx'\), with primes denoting next-step variables. Stationarity of the variance of \(u\) gives the normalized covariance of \(u\) and \(x'\) as \(-tX/2\), so \(C_{12}=tX/2\). Evaluating the same covariance from \(x'=(1-t)x-u-v\) gives \(C_{22}=t(2-t)X/2-C_{23}\). Expanding the variance of \(x'\) gives \(C_{22}=t(3-2t)X-C_{33}+2(1-t)C_{13}-2C_{23}\). Thus
\[
\frac{t(4-3t)}{2}X=C_{33}-2(1-t)C_{13}+C_{23}=\frac{a^2(d-et)}{dD}.
\]
Rescaling \(X\) yields the stated feasibility risk.

For \(t=4/3\), the roots of \(Q_t\) are \(-1,1/3\); for \(t>4/3\), \(Q_t(-1)<0\) and \(Q_t(0)<0<Q_t(1)\), so the roots are one less than \(-1\) and the other in \((0,1)\). Hence at or beyond the frontier there is a simple dominant eigenvalue \(\lambda_-\le-1\); all other eigenvalues have modulus below one. The controllability determinant \(\det[e_3,Me_3,M^2e_3]=t\) is nonzero, as is the observability determinant \(\det[e_1^{\mathsf T};e_1^{\mathsf T}M;e_1^{\mathsf T}M^2]=-a\). In particular, the left eigenvector for \(\lambda_-\) is not orthogonal to the forcing vector \(e_3\), and its right eigenvector is not orthogonal to the observed coordinate \(e_1\). The impulse coefficients \(e_1^{\mathsf T}M^j e_3\) therefore have a nonzero leading term proportional to \(\lambda_-^j\), plus a term that tends to zero. Independence of the increments gives a variance contribution \((a^2\sigma^2/\eta^2)\sum_{j=0}^{r-1}(e_1^{\mathsf T}M^j e_3)^2\) after \(r\) steps, which diverges even at the boundary. The independent initial contribution cannot cancel it.

For fixed \(a\), log differentiation of \(X\) gives the displayed optimizer equation. The log second derivative is
\[
-\frac{e^2}{(d-et)^2}+\frac1{t^2}+\frac9{(4-3t)^2}+\frac{(1-a^2)^2}{D^2}>0.
\]
Indeed \(d-et>0\) there and \(3/(4-3t)>e/(d-et)\), as \(3d-4e=2+a>0\). The risk diverges at both stable endpoints for every fixed \(a>0\). The log derivative at \(2/3\) is \(-9(1-a)(a+2)/[(4-a)(a^2+2)]<0\), and at \(1\) it is \(a(a+1)>0\). Thus there is exactly one critical point in \((2/3,1)\), the global minimum. On \([2/3,1]\) the log derivative extends continuously to \(a=0\) and \(a=1\), since all its denominators stay positive. At \(a=0\) its only root there is 1, and at \(a=1\) its only root is \(2/3\), as follows by substitution and the same strict derivative inequality. Every subsequential limit of the minimizing ratios solves the corresponding endpoint equation, proving the two asserted limits.

## Verification

Run `python verify.py` with Python 3 and its standard library. The checker solves the six Lyapunov equations by exact rational elimination on a grid and compares the risk and selected other entries. It also tests derivative signs and brackets, and compares four seeded empirical second moments with the formula. The frozen record reports 1716 checks. These are finite corroboration; the all-parameter conclusion follows from the analytical proof.

## Relationship to prior work and limitations

The deterministic primal–dual block is already covered by the scalar bilinear Chambolle–Pock calculation of Banert, Upadhyaya, and Giselsson, §7 of arXiv:2309.03998v2. In fact let \(y_r=\lambda_r+\beta x_r\), \(\tau=1/\eta\), and \(\rho=\beta\). With zero momentum forcing, the updates are \(x_{r+1}=x_r-\tau y_r\) and \(y_{r+1}=y_r+\rho(2x_{r+1}-x_r)\). These are precisely their scalar bilinear updates with extrapolation parameter 1 and step product \(\tau\rho=t\). The \(-1\) crossing at \(4/3\) is not an independent novelty claim. The stochastic result concerns the same primal–dual block with the additive momentum state acting as a filter: its forcing is visible in the feasibility coordinate, the stationary second moment is explicit, and its penalty optimum is unique. Deterministic convergence does not determine that stationary risk or its minimizing ratio.

Qiu, Maithripala, and Lin, arXiv:2604.13272v1, Lemma 7 and Theorem 1, choose parameters by horizon to obtain approximate stationarity. Their result is different from an infinite run with one fixed triple \((\eta,\beta,\alpha)\). Related constant-template STORM covariance calculations concern corrected momentum without this dual state. No claim is made that this scalar classification gives a tuning rule for nonlinear constraints, state-dependent noise, or general nonconvex MALM. Equivalent stationary calculations outside the inspected literature cannot be excluded.
