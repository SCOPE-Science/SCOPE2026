# Coordinate-dependent stability obstruction and an exact aligned-gain phase transition in a discrete minimax controller

## Finding
For the *explicit parameter update* of Luo, Chen and Zhu's Controlled-Minimax Algorithm 1, consider the bilinear zero-sum game \(\ell(x,y)=x^{\mathsf T}Ky\), where \(K\) is a real square invertible matrix, and equal controller gains \(\lambda_x=\lambda_y=\lambda>0\). Let \(\delta=1-\lambda\), the learning rate be \(\eta>0\), and \(\beta\in\mathbb R\) be the cross-gradient gain. With the paper's leading-coordinate coupling \(A_c=I\), every **symmetric indefinite** \(K\) (having at least one positive and one negative eigenvalue) yields a non-Schur-stable iteration matrix for *every* choice of \(\beta,\lambda,\eta\). For \(K\) positive definite and \(\beta>0\), every nonzero initial state grows exponentially, whatever the positive learning rate. This is a strict limitation of the specified discrete update, not of the paper's continuous-time velocity feedback theorem.

This obstruction is **not invariant under orthogonal changes of the strategy coordinates**: the games \(\ell(x,y)=x^{\mathsf T}y\) and \(\ell(x,y)=x^{\mathsf T}\operatorname{diag}(1,-1)y\) are orthogonally equivalent, yet with the *same* default \(A_c=I\) and any \(\beta<0\), only the first can be made Schur stable.

A mathematically natural alternative is to align the controller with the actual bilinear interaction by choosing \(A_c=K\), rather than the default identity. For **any invertible real square** \(K\), \(\beta=-b<0\), \(b>0\), and equal damping gains, let its least and greatest singular values be \(0<\mu\le L\) and set \(T=\delta^2\). The iteration is Schur stable **if and only if**
\[
0<\eta<\frac{2b}{b^2L^2+T}.
\]
Its exact worst-case Euclidean one-step factor, also its asymptotic spectral radius, has the **unique globally minimizing positive learning rate**
\[
\eta_*=
\begin{cases}
\displaystyle\frac{2b}{T+b^2(\mu^2+L^2)},& T<b^2(L^2-\mu^2),\\[5pt]
\displaystyle\frac{b}{T+b^2\mu^2},&T\ge b^2(L^2-\mu^2).
\end{cases}
\]
The corresponding squared minimal factor is
\[
\rho_*^2=
\begin{cases}
\displaystyle 1-\frac{4b^4\mu^2L^2}{[T+b^2(\mu^2+L^2)]^2},&T<b^2(L^2-\mu^2),\\[5pt]
\displaystyle\frac{T}{T+b^2\mu^2},&T\ge b^2(L^2-\mu^2).
\end{cases}
\]
Both formulas agree at the transition. In the second regime the slowest singular mode alone determines the best rate; in the first the two endpoint modes balance. Choosing \(A_c=K\) is a known **consensus-type** correction, not a claimed new optimizer; the new assessed assertion is the explicit comparison with the precise 2026 update and the closed sharp phase transition for its gain family.

## Assumptions and scope
All claims concern exact arithmetic, synchronous simultaneous updates, the specified bilinear real-square game of arbitrary finite dimension \(d\ge1\), equal \(\lambda_x=\lambda_y>0\), and a fixed positive \(\eta\). The negative result requires \(d\ge2\) and symmetric invertible indefinite \(K\). The positive aligned result requires arbitrary invertible \(K\), not necessarily symmetric, \(\beta=-b<0\), and \(A_c=K\). For the strict uniqueness assertion, the pair \((b,\delta)\) and spectrum of \(K\) are fixed; only \(\eta>0\) varies. Schur stability means all eigenvalues lie strictly inside the unit disk. The norm is Euclidean, with no unreported coordinate scaling.

The exact Algorithm 1 updates are \(g_x=Ky\), \(g_y=K^{\mathsf T}x\), \(u_x=\lambda g_x+\beta A_cg_y\), \(u_y=\beta A_c^{\mathsf T}g_x-\lambda g_y\), followed by \(x^+=x-\eta g_x+\eta u_x\) and \(y^+=y+\eta g_y+\eta u_y\). Thus its real linear update matrix is
\[
M_{A_c}=\begin{pmatrix}
I+\eta\beta A_cK^{\mathsf T}&-\eta\delta K\\
\eta\delta K^{\mathsf T}&I+\eta\beta A_c^{\mathsf T}K
\end{pmatrix}.
\]

## Proof
**1. Default coupling and the sign obstruction.** If \(K=K^{\mathsf T}\), orthogonally diagonalize \(K\) with signed eigenvalues \(s_1,\ldots,s_d\). For \(A_c=I\), the corresponding invariant real two-dimensional block is
\[
B_s=\begin{pmatrix}1+\eta\beta s&-\eta\delta s\\\eta\delta s&1+\eta\beta s\end{pmatrix}.
\]
Its two eigenvalues are \(1+\eta\beta s\pm i\eta\delta s\), and its squared norm is exactly
\[
R_s^2=1+2\eta\beta s+\eta^2(\beta^2+\delta^2)s^2.
\]
For an indefinite spectrum and \(\beta>0\) choose a positive \(s\), and for \(\beta<0\) choose a negative \(s\). Either choice gives \(R_s>1\). When \(\beta=0\), every nonzero \(s\) has \(R_s\ge1\), with equality only if \(\delta=0\); hence strict Schur stability is impossible. When \(K\) is positive definite and \(\beta>0\), every mode has \(R_s>1\), proving exponential divergence for every nonzero initial state. For \(K=I\) and \(\beta<0\), all modes contract for sufficiently small \(\eta\). Replacing \(K=I\) by \(K=\operatorname{diag}(1,-1)\) is exactly the strategy substitution \(y\mapsto\operatorname{diag}(1,-1)y\), while keeping \(A_c=I\) creates the impossible-to-stabilize indefinite spectrum.

**2. Aligned coupling.** For \(A_c=K\) and \(\beta=-b\), the update is
\[
M_K=\begin{pmatrix}
I-\eta bKK^{\mathsf T}&-\eta\delta K\\
\eta\delta K^{\mathsf T}&I-\eta bK^{\mathsf T}K
\end{pmatrix}.
\]
Use a singular-value decomposition \(K=U\operatorname{diag}(s_1,\dots,s_d)V^{\mathsf T}\). The orthogonal change \(\operatorname{diag}(U,V)\) reduces this matrix to independent normal real blocks
\[
C_s=\begin{pmatrix}1-\eta b s^2&-\eta\delta s\\\eta\delta s&1-\eta b s^2\end{pmatrix},
\quad
r_s(\eta)^2=(1-\eta b s^2)^2+\eta^2\delta^2s^2.
\]
For each \(s>0\), \(r_s(\eta)^2<1\) is equivalent to \(0<\eta<2b/(b^2s^2+\delta^2)\). Taking all singular values gives the stated sharp stability interval. The SVD blocks are normal and orthogonal, so their largest modulus is simultaneously the operator 2-norm and spectral radius; there are no hidden nonnormal growth assumptions.

**3. Exact minimax phase transition.** For fixed \(\eta\), write \(z=s^2\) and
\[
f_\eta(z)=1-2b\eta z+\eta^2(b^2z^2+Tz).
\]
It is convex in \(z\), so over any spectrum within \([\mu^2,L^2]\) the maximum is attained at one of its actual endpoints; both endpoints are singular values. For \(\mu<L\), their difference is
\[
f_\eta(L^2)-f_\eta(\mu^2)
=(L^2-\mu^2)\eta\bigl[-2b+\eta\{T+b^2(L^2+\mu^2)\}\bigr].
\]
They cross at \(\eta_e=2b/[T+b^2(L^2+\mu^2)]\). For \(\eta<\eta_e\), the smaller singular value controls the maximum; for \(\eta>\eta_e\), the larger controls it. The unconstrained minimizer of the smaller-endpoint quadratic is \(\eta_\mu=b/(T+b^2\mu^2)\). If \(T\ge b^2(L^2-\mu^2)\), then \(\eta_\mu\le\eta_e\) and is globally optimal; otherwise, \(\eta_\mu>\eta_e\) and the upper envelope is minimized at its crossing \(\eta_e\). Every endpoint quadratic is strictly convex in \(\eta\), so the minimizer is unique, including at equality. Substitution yields the stated squared factors. For \(\mu=L\), there is only one endpoint; its unique minimizer is \(b/(T+b^2\mu^2)\), agreeing with the second formula.

## Verification
The complete standalone `check.py` (Python 3 with NumPy and SymPy) symbolically checks the signed-eigenmode identity and the exact balanced-rate formula, verifies all eigenmodes for 180 random positive-definite examples, tests the indefinite no-go for multiple signed spectra, and verifies the aligned SVD factor and piecewise global-optimum formula in 160 random invertible matrix examples. Execution produced the two lines: `PASS: symbolic identities and 180 arbitrary-SPD matrix cases, plus exact-rate stationary checks` and `PASS: indefinite-no-go, 160 aligned arbitrary-matrix SVD and optimal-step cases`. These finite computations corroborate, but do not substitute for, the universal exact argument above.

## Relationship to prior work
Luo, Chen and Zhu (2026), Algorithm 1 and Section 7, give the precise identity-like coupling update and explicitly reserve its discrete-time stability analysis for future work. Their Theorem 4.3 concerns a **different continuous-time velocity feedback system** and is not contradicted by the present discrete-map calculation. Mescheder, Nowozin and Geiger (2017) already introduce consensus optimization based on a Jacobian-transposed gradient, which motivates our aligned choice \(A_c=K\); no novelty in that correction mechanism is asserted. Azizian et al. (2020), Section 6.2, analyze and accelerate consensus optimization using spectral shapes and provide convergence-rate estimates, but do not explicitly give the fixed-gain sign obstruction for Luo et al.'s later identity-coupled update nor the stated exact two-regime minimizer over a finite singular-value interval. Zhang and Yu (2020) analyze bilinear games via other gradient methods; their results concern different iteration maps. The exact negative comparison and exact aligned-gain phase transition are the scoped claims.

## Limitations
The stability conclusions are for the printed parameter update in exact arithmetic, not for continuous-time velocity feedback, a different implementation, nonlinear games, stochastic gradients, nonsimultaneous updates, or arbitrary unequal damping gains. The aligned controller is a known consensus-type structure and requires knowledge of \(K\); it may not be computationally attractive in high dimensions. All rate formulas optimize only \(\eta\) with \(b,\lambda\) fixed and are not claims of an optimal algorithm among all solvers. Existing general spectral-shape theory could subsume the fixed-parameter minimax calculation as an implicit special case; an exhaustive historical bibliographic guarantee is not claimed. Strict boundaries have unit-modulus modes and are not Schur stable.

## References
1. T. Luo, J. Chen and J. Zhu, *Controlled-Minimax: Stabilizing Adversarial Optimization via Control Theory*, first posted 2026-10-09, arXiv:2610.12915, https://arxiv.org/abs/2610.12915; Algorithm 1, Section 4 and Section 7.
2. L. Mescheder, S. Nowozin and A. Geiger, *The Numerics of GANs*, arXiv:1705.10461, https://arxiv.org/abs/1705.10461; Sections on consensus optimization and iteration stability.
3. W. Azizian, D. Scieur, I. Mitliagkas, S. Lacoste-Julien and G. Gidel, *Accelerating Smooth Games by Manipulating Spectral Shapes*, AISTATS 2020, https://proceedings.mlr.press/v108/azizian20a.html; Sections 5–6.
4. G. Zhang and Y. Yu, *Convergence of Gradient Methods on Bilinear Zero-Sum Games*, arXiv:1908.05699, https://arxiv.org/abs/1908.05699; bilinear iterative dynamics.
