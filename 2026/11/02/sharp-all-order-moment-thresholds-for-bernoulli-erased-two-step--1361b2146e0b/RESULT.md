# Sharp all-order moment thresholds for Bernoulli-erased two-step deadbeat control

## Finding

The following exact moment classification holds for a natural class of two-dimensional randomly switched control systems. Let \(D,N\) be real \(2\)-by-\(2\) matrices satisfying
\[
D^2=N^2=0,\qquad N\ne0,\qquad \gamma=\operatorname{tr}(ND)\ne0,
\]
and put \(A=I+D\). Let \(0<q<1\), take independent matrices \(B_n\) with \(\Pr(B_n=A)=q\) (erasure) and \(\Pr(B_n=N)=1-q\) (successful control), and evolve \(Z_{n+1}=B_nZ_n\) from any deterministic \(Z_0=z\ne0\).

For **every real moment order** \(p>0\), there is exactly one \(\lambda_p(q)>q\) solving
\[
\boxed{\quad (1-q)|\gamma|^p
 \sum_{k=1}^{\infty}\frac{k^p q^k}{\lambda_p(q)^{k+1}}=1.\quad}
\tag{1}
\]
There are positive, finite constants \(c_p,C_p\), independent of \(n\) and \(z\), for which
\[
\boxed{\quad c_p\lambda_p(q)^n\|z\|_2^p
 \le \mathbb E\|Z_n\|_2^p
 \le C_p\lambda_p(q)^n\|z\|_2^p,
 \qquad n=0,1,2,\ldots .\quad}
\tag{2}
\]
At the same time, \(Z_n=0\) for all sufficiently large \(n\), almost surely, because two consecutive successful controls annihilate every state.

The exact transition between exponential decay and exponential growth of the order-\(p\) moment is the unique \(q_p\in(0,1)\) satisfying
\[
(1-q_p)|\gamma|^p\sum_{k=1}^{\infty}k^p q_p^k=1.
\tag{3}
\]
For \(q<q_p\), every order-\(p\) moment decays exponentially; for \(q=q_p\), it is uniformly bounded above and away from zero for every nonzero fixed initial state; for \(q>q_p\), it grows exponentially. These conclusions concern the moments at each **deterministic** time \(n\), not merely moments indexed by successful transmissions.

A concrete sampled double-integrator model is
\[
y_{n+2}-2y_{n+1}+y_n=u_n,
\qquad u_n=
\begin{cases}
-2y_{n+1}+y_n,&\text{packet received},\\
0,&\text{packet erased}.
\end{cases}
\tag{4}
\]
For \(Z_n=(y_{n+1},y_n)^{\mathsf T}\), the two state matrices are
\[
A=\begin{pmatrix}2&-1\\1&0\end{pmatrix},
\qquad N=\begin{pmatrix}0&0\\1&0\end{pmatrix},
\qquad \gamma=-1.
\tag{5}
\]
The exact first-moment rate is
\[
\lambda_1(q)=q+\sqrt{q(1-q)},
\tag{6}
\]
and the second-moment rate is the unique real \(\lambda>q\) satisfying
\[
(\lambda-q)^3=q(1-q)(\lambda+q).
\tag{7}
\]
Thus the first- and second-moment thresholds are **\(q_1=1/2\)** and **\(q_2=1/3\)**. In the interval \(1/3<q<1/2\), the state is almost surely zero after finite time, its expected Euclidean norm decays exponentially, but its expected squared Euclidean norm grows exponentially. For example, at \(q=2/5\) the two rates are \(0.889897948557\ldots\) and \(1.113507624413\ldots\), respectively. At \(q=1/3\),
\[
Q=\begin{pmatrix}6&-3\\-3&2\end{pmatrix}\succ0,
\qquad \mathbb E[Z_n^{\mathsf T}QZ_n]=z^{\mathsf T}Qz
\quad\text{for every }n\ge0.
\tag{8}
\]
For this model \(q_p\) strictly decreases as \(p\) increases, giving a continuum of distinct sharp moment-stability thresholds.

## Assumptions and scope

The state space is \(\mathbb R^2\). The initial state is deterministic; the update modes are independent and identically distributed and independent of the initial state. The parameter \(q\) is the probability of **erasure**; \(1-q\) is the probability of successful actuation. An erased packet causes zero control for that step, rather than holding the previous input. There is no additive process or measurement noise. The control update \(N\) is nonzero and nilpotent, and the uncontrolled propagation is a nontrivial unipotent Jordan step \(A=I+D\). The nondegeneracy \(\gamma\ne0\) excludes uncoupled cases and is invariant under changes of state coordinates and rank-one factorizations of \(N\).

The Euclidean norm in (2) can be replaced by any norm on \(\mathbb R^2\), at the cost of changing positive comparison constants. The theorem is for every fixed finite real \(p>0\); neither the endpoints \(q=0,1\) nor limits involving \(p=\infty\) are part of (1)--(3). At \(q=0\), two deterministic successful steps give extinction. At \(q=1\), the unipotent open-loop map has polynomial (not geometric) growth on generic initial states.

## Proof

**1. Nilpotent algebra and absorption.** Since \(N\ne0\) and \(N^2=0\) in dimension two, factor \(N=r\ell^{\mathsf T}\), where \(r,\ell\in\mathbb R^2\) are nonzero and \(\ell^{\mathsf T}r=0\). In this notation
\[
\gamma=\operatorname{tr}(ND)=\ell^{\mathsf T}Dr.
\]
Because \(D^2=0\),
\[
A^k=(I+D)^k=I+kD,
\quad \ell^{\mathsf T}A^kr=k\gamma,
\quad NA^kN=k\gamma N\quad(k\ge0).
\tag{9}
\]
In particular \(N^2=0\): two consecutive successful transmissions set \(Z_n\) to zero, after which the homogeneous dynamics stays there. Let \(\tau\) be the index of the first completed adjacent-success pair. Considering disjoint pairs of update slots gives
\[
\Pr(\tau>2m)\le [1-(1-q)^2]^m\quad(m\ge0),
\tag{10}
\]
so \(\tau<\infty\) almost surely and has a finite mean (indeed the mean waiting time in steps is \([2-q]/(1-q)^2\)). This holds for every deterministic initial state.

**2. Existence of the exact moment rate.** For \(\lambda>q\) define
\[
F_p(\lambda)= (1-q)|\gamma|^p
\sum_{k=1}^{\infty} \frac{k^pq^k}{\lambda^{k+1}}.
\]
Each summand is positive; the series converges because \(q/\lambda<1\). The function is continuous and strictly decreasing, with \(F_p(\lambda)\to\infty\) as \(\lambda\downarrow q\) and \(F_p(\lambda)\to0\) as \(\lambda\to\infty\). The first limit follows from divergence of \(\sum k^p\), since \(p>0\). Hence the equation \(F_p(\lambda)=1\) has a unique root \(\lambda_p(q)>q\).

**3. An explicit positive homogeneous eigen-energy.** Fix \(p>0\), \(q\in(0,1)\), and this root \(\lambda=\lambda_p(q)\). Set
\[
V_p(x)=\sum_{k=0}^{\infty}
\frac{q^k}{\lambda^{k+1}}|\ell^{\mathsf T}A^kx|^p.
\tag{11}
\]
This converges uniformly on bounded subsets of \(\mathbb R^2\) because \(A^k=I+kD\) and \(q/\lambda<1\). It is continuous, nonnegative, and positively homogeneous of degree \(p\). It is strictly positive for every \(x\ne0\). Indeed, if it vanished, its \(k=0\) and \(k=1\) terms would give \(\ell^{\mathsf T}x=0\) and \(\ell^{\mathsf T}Dx=0\). The rows \(\ell^{\mathsf T}\) and \(\ell^{\mathsf T}D\) are linearly independent: the first annihilates \(r\), but the second takes value \(\gamma\ne0\) on \(r\). Thus \(x=0\), a contradiction. Continuity and compactness of the unit circle furnish constants \(0<m_p\le M_p<\infty\) such that
\[
m_p\|x\|_2^p\le V_p(x)\le M_p\|x\|_2^p
\quad\text{for every }x\in\mathbb R^2.
\tag{12}
\]
The shift in (11) gives the exact identity
\[
qV_p(Ax)=\lambda V_p(x)-|\ell^{\mathsf T}x|^p.
\tag{13}
\]
The rank-one representation yields
\[
V_p(Nx)=|\ell^{\mathsf T}x|^pV_p(r),
\quad
(1-q)V_p(r)=(1-q)|\gamma|^p
 \sum_{k=1}^{\infty}\frac{k^pq^k}{\lambda^{k+1}}=1.
\tag{14}
\]
Combining (13) and (14), for every \(x\in\mathbb R^2\),
\[
qV_p(Ax)+(1-q)V_p(Nx)=\lambda V_p(x).
\tag{15}
\]
Condition on \(Z_n\) and iterate (15). Independence of the update mode gives the **exact** identity
\[
\mathbb E V_p(Z_n)=\lambda^nV_p(z)
\quad(n=0,1,2,\ldots).
\tag{16}
\]
With (12), this proves (2), taking \(c_p=m_p/M_p\) and \(C_p=M_p/m_p\). The proof is valid for every real \(p>0\), including non-integer orders; it does not rely on differentiability of \(V_p\) or on finite-dimensional polynomial moment closure.

**4. Sharp erasure transition.** Evaluating \(F_p\) at \(\lambda=1\) gives
\[
G_p(q)=(1-q)|\gamma|^p\sum_{k=1}^{\infty}k^pq^k.
\tag{17}
\]
Let \(K_q\) be the number of erasures before one success, so \(\Pr(K_q=k)=(1-q)q^k\) for \(k=0,1,\ldots\). Then \(G_p(q)=\mathbb E(|\gamma|K_q)^p\). The geometric family \(K_q\) is strictly increasing in stochastic order as \(q\) increases; the positive function \(k\mapsto(|\gamma|k)^p\) is strictly increasing for \(k\ge0\). Thus \(G_p(q)\) is continuous and strictly increasing in \(q\). It tends to zero as \(q\downarrow0\), and to infinity as \(q\uparrow1\) (for example by comparing with the geometric mean length, or by the asymptotic \(G_p(q)\sim |\gamma|^p\Gamma(p+1)(1-q)^{-p}\)). Therefore (3) has exactly one root \(q_p\). Since \(F_p(\lambda)\) is strictly decreasing, \(\lambda_p(q)\) is below, at, or above one exactly when \(G_p(q)\) is below, at, or above one. With (2), this proves every phase claim, including the boundary's two-sided bounds.

**5. Exact canonical values and a strict moment gap.** For (4), direct substitution gives (5). Since \(|\gamma|=1\), the geometric-series identities
\[
\sum_{k=1}^{\infty}kr^k=\frac{r}{(1-r)^2},
\qquad
\sum_{k=1}^{\infty}k^2r^k=\frac{r(1+r)}{(1-r)^3}
\quad(0<r<1)
\tag{18}
\]
reduce (1) respectively to
\[
(\lambda-q)^2=q(1-q)
\quad(p=1)
\tag{19}
\]
and (7) for \(p=2\). The admissible \(\lambda>q\) root of (19) is (6). Substitution of \(\lambda=1\) gives \(q_1=1/2\), \(q_2=1/3\), and proves the exponential first-/second-moment separation for every \(1/3<q<1/2\). At \(q=1/3\), direct multiplication verifies
\[
\tfrac13A^{\mathsf T}QA+\tfrac23N^{\mathsf T}QN=Q,
\tag{20}
\]
while the leading principal minors of \(Q\) are \(6\) and \(3\), so \(Q\) is positive definite. This proves (8). Finally, at fixed \(q\in(0,1)\) and for this unit-coupling example, \(\mathbb E K_q^p\) increases strictly with \(p\), because \(K_q\) is integer-valued and has positive probability of being at least two. Hence the unique thresholds \(q_p\) strictly decrease as \(p\) increases.

## Verification

The accompanying standalone `verify.py` uses only the Python standard library. It checks the exact algebra \(NA^kN=k\gamma N\) on a range of integer powers; verifies (20), positive definiteness of (8), and exact rational expectation conservation for every binary mode sequence through seven steps from four distinct starts; checks the defining root equations for \(p=1,2\); and numerically tests the positive homogeneous eigenfunction (15), including noninteger \(p\), under independent mode selection. It also tests coupling magnitudes other than one and all finite binary mode sequences through four updates.

Command: `python3 verify.py`. The extracted verifier returned `VERIFY_OK checks= 1165` and the numerical rates \(\lambda_1(2/5)=0.889897948557\), \(\lambda_2(2/5)=1.113507624413\), and \(\lambda_2(1/2)=1.260689853402\). Exact algebra checks and finite enumeration are corroboration, not a substitute for the all-order, all-time proof given above.

## Relationship to prior work

The motivating full-text paper by Su, Li and Lu (arXiv:2108.12795v1, released 2021-08-29) gives frequency-domain mean-square input-output stability and stabilizability criteria for communication channels exhibiting random delays and dropouts. Lu, Li and Su (arXiv:2204.13083) develop a state-space and input-output treatment of mean-square control with random transmission delays. Sykora and collaborators (DOI:10.1002/rnc.5218) determine first- and second-moment dynamics of stochastically delayed linear control systems. Li, Lu and Su (arXiv:2402.04074) give more general MIMO mean-square stability criteria. These sources provide broad frameworks for second-order stability; their inspected mathematical statements do not specify the complete all-real-moment spectrum (1)--(3) for the nilpotent/unipotent erasure family, nor its exact almost-sure-extinction versus moment-growth example. This is a statement-and-implication comparison, not a claim that the general framework could never be specialized to obtain a second-moment bound.

Xu, Zhang, Gu and Tang (DOI:10.1137/22M1496062) analyze mean-square stabilizability under packet drops and random delays using a predictor-like controller and an algebraic Riccati equation. Only publisher and repository descriptions were accessible for this paper; its full technical content could not be compared. Accordingly publication priority is qualified, especially for the isolated second-moment special case. The continuous range of real moment orders and the explicit homogeneous eigen-energy are the principal distinguishing mathematical components.

## Limitations

This is a two-dimensional, homogeneous, independently switched, zero-input-on-erasure model, not a statement about all network protocols or actuator policies. In particular, holding a prior control input on loss changes the transition matrix and invalidates the theorem. Independent process noise also destroys exact finite-time absorption. The positive eigen-energy depends on the chosen real \(p>0\); no single Euclidean contraction coefficient applies across all moments. The comparison constants in (2) are not supplied in optimal closed form, although the constructive series (11) determines them by minimization and maximization on the unit circle. At criticality, the result proves uniform upper and positive lower bounds for moment expectations, not convergence of those moments to a common limit. Source comparisons are limited to the specifically inspected primary literature and accessible research records; they do not certify exhaustive publication priority. There is no independent validation of the mathematical result.

## References

1. W. Su, J. Li and J. Lu, *Mean-Square Input-Output Stability and Stabilizability of a Networked Control System with Random Channel Induced Delays*, arXiv:2108.12795v1 (2021-08-29). https://arxiv.org/html/2108.12795v1
2. J. Lu, J. Li and W. Su, *Mean-square stability of linear systems over channels with random transmission delays*, arXiv:2204.13083 (2022). https://arxiv.org/abs/2204.13083
3. H. T. Sykora et al., *On the moment dynamics of stochastically delayed linear control systems*, International Journal of Robust and Nonlinear Control (2020). https://doi.org/10.1002/rnc.5218
4. J. Li, J. Lu and W. Su, *Mean-Square Stability and Stabilizability for LTI and Stochastic Systems Connected in Feedback*, arXiv:2402.04074 (2024). https://arxiv.org/abs/2402.04074
5. J. Xu, H. Zhang, G. Gu and Y. Tang, *Stabilization of Discrete-Time Systems with Random Delays and Packet Drops: A Predictor-Like Controller*, SIAM Journal on Control and Optimization 61 (2023), 1737--1759. https://doi.org/10.1137/22M1496062
