# Universal sign-flip Floquet instability of dissipative gradient descent-ascent

## Finding

**Theorem.** Let \(d\ge1\), let \(A\in\mathbb R^{d\times d}\) be invertible, and fix \(0<\rho<1\) and \(\eta>0\). Apply the dissipative gradient descent-ascent (DGDA) update of Zheng, Loizou, You, and Mallada to the two-periodic unconstrained saddle functions
\[
f_k(x,y)=(-1)^k x^{\mathsf T}Ay,\qquad (x,y)\in\mathbb R^d\times\mathbb R^d,\quad k=0,1,\ldots.
\]
Initialize the auxiliary variables at their corresponding primary variables, \(\widehat x_0=x_0\) and \(\widehat y_0=y_0\). Every nonzero primary initialization \((x_0,y_0)\ne(0,0)\) produces a primary trajectory with \(\|(x_{2m},y_{2m})\|_2\to\infty\) geometrically. In particular, *arbitrarily small positive steps do not restore convergence*, despite all stage games having the same unique saddle \((0,0)\).

More precisely, write \(\sigma_1,\ldots,\sigma_d>0\) for the singular values of \(A\). The full real two-step Floquet matrix has, with algebraic multiplicities, the exact eigenvalues \(q_+(\eta\sigma_j)\) and \(q_-(\eta\sigma_j)\), **each repeated twice** for every \(j\), where
\[
T_\rho(t)=2\big((1-\rho)^2+\rho^2\big)+t^2,\qquad
D_\rho(t)=(1-2\rho)^2+(1-\rho)^2t^2,
\]
\[
q_\pm(t)=\frac{T_\rho(t)\pm\sqrt{T_\rho(t)^2-4D_\rho(t)}}2.
\]
For every \(t>0\), these multipliers are distinct and satisfy
\[
0<q_-(t)<1<1+\frac{t^2}{2}\le q_+(t).
\]
(The displayed strict comparison before \(1+t^2/2\) is a direct consequence of \(q_-<1\); equality in the final comparison is not needed.) Hence the full period map is a positive-definite symmetric matrix with both contracting and expanding eigenspaces. Nevertheless, none of the permitted synchronized nonzero initial states lies entirely in its stable eigenspace.

For example, in the scalar case \(A=[1]\) with \(\rho=\eta=1/2\), either static sign of the payoff gives a Schur-stable one-step DGDA matrix with spectral radius
\[
\sqrt{\frac{2+\sqrt3}{4}}<1,
\]
but alternating the signs yields the unstable two-step multiplier
\[
q_+=\frac{5+\sqrt{21}}8>1.
\]

## Assumptions and scope

The method uses simultaneous updates with one gradient evaluation and the same fixed parameters at every iteration:
\[
\begin{aligned}
x_{k+1}&=x_k-\eta\nabla_x f_k(x_k,y_k)-\rho(x_k-\widehat x_k),\\
\widehat x_{k+1}&=\widehat x_k-\rho(\widehat x_k-x_k),\\
y_{k+1}&=y_k+\eta\nabla_y f_k(x_k,y_k)-\rho(y_k-\widehat y_k),\\
\widehat y_{k+1}&=\widehat y_k-\rho(\widehat y_k-y_k).
\end{aligned}
\]
The payoff alternates exactly between \(A\) and \(-A\), beginning with \(A\). The common saddle point is \((0,0)\), because \(A\) is invertible. There are no constraints, projections, sampling, delayed gradients, or approximate solves. The auxiliary initialization is part of the theorem; no claim is made about *every* point in the unrestricted augmented state space.

## Proof

**1. A transposed period map.** Set \(z_k=(x_k,y_k)\), \(\widehat z_k=(\widehat x_k,\widehat y_k)\), \(c=1-\rho\), and
\[
K=\begin{pmatrix}0&A\\-A^{\mathsf T}&0\end{pmatrix},\qquad K^{\mathsf T}=-K.
\]
In the state order \(w_k=(z_k,\widehat z_k)\), the step using payoff sign \(s\in\{-1,1\}\) is \(w_{k+1}=B_s w_k\), with
\[
B_s=\begin{pmatrix}cI-s\eta K&\rho I\\\rho I&cI\end{pmatrix}.
\]
Since \(K\) is skew-symmetric, \(B_-=B_+^{\mathsf T}\). Consequently the exact two-step matrix, from even to even times, is
\[
P=B_-B_+=B_+^{\mathsf T}B_+.
\]
This identity is specific to the stated simultaneous update and exact sign reversal. It makes \(P\) symmetric positive semidefinite without requiring commutation of two arbitrary iteration matrices.

**2. Complete singular-mode spectrum.** The real singular-value decomposition of \(A\) decomposes \(K\) into independent two-dimensional skew planes with complex eigenvalues \(\pm i\sigma_j\). On the complex eigenline for \(+i\sigma_j\), and using \(t=\eta\sigma_j\), the step is
\[
H_+(t)=\begin{pmatrix}c-it&\rho\\\rho&c\end{pmatrix},
\]
and the reversed-sign step is \(H_+(t)^*\). Their period product is the Hermitian matrix \(Q(t)=H_+(t)^*H_+(t)\). Direct multiplication gives
\[
\operatorname{tr}Q(t)=T_\rho(t),\qquad \det Q(t)=D_\rho(t),
\]
and
\[
\det(I-Q(t))=1-T_\rho(t)+D_\rho(t)=-\rho(2-\rho)t^2<0.
\]
Moreover \(\det Q(t)=D_\rho(t)>0\), because \(0<\rho<1\) and \(t>0\). As \(Q(t)\) is Hermitian positive definite, its two eigenvalues must straddle \(1\). The quadratic formula yields exactly \(q_\pm(t)\), and conjugate skew planes give each eigenvalue twice in the real period spectrum.

**3. Every synchronized primary initialization excites expansion.** Let \(v\) be an arbitrary nonzero complex coefficient in one skew singular mode. The synchronized augmented initial vector is \((v,v)\). The first step obeys
\[
H_+(t)\binom vv=\binom{(1-it)v}{v}.
\]
Its period Rayleigh quotient is therefore
\[
\frac{(v,v)^*Q(t)(v,v)}{2|v|^2}=1+\frac{t^2}{2}>1.
\]
The spectral theorem now forces a nonzero projection of \((v,v)\) onto the \(q_+(t)\)-eigenspace: a vector in the \(q_-(t)\)-eigenspace alone would have Rayleigh quotient strictly below \(1\). In fact, with \(r_t=1+t^2/2\), the exact spectral weight of the expanding eigenspace is \((r_t-q_-(t))/(q_+(t)-q_-(t))>0\). This also proves \(q_+(t)\ge r_t\).

The primary component of an expanding eigenvector cannot vanish: the off-diagonal entry of \(Q(t)\) has modulus \(\rho\sqrt{4c^2+t^2}>0\), so neither coordinate axis is an eigenspace. Thus the primary coefficient in that mode grows like a nonzero multiple of \(q_+(t)^m\), while its contracting component decays as \(q_-(t)^m\). Orthogonal singular modes cannot cancel in the Euclidean norm. Since \((x_0,y_0)\ne0\), at least one mode has nonzero \(v\), proving geometrically diverging primary iterates at even times.

**4. The fixed-game comparison.** For \(d=1\), \(A=[1]\), and \(\rho=\eta=1/2\), the fixed-sign complex step eigenvalues are
\[
\frac12+\frac{i}{4}\pm\frac{\sqrt3}{4}.
\]
Both have modulus below \(1\), and the larger modulus is exactly \(\sqrt{(2+\sqrt3)/4}\). The period polynomial has \(T=5/4\) and \(D=1/16\), giving the two eigenvalues \((5\pm\sqrt{21})/8\). Hence two separately convergent fixed-game iterations alternate into an expanding one.

## Verification

Run `python verify.py` with the packages in `requirements.txt`. The verifier symbolically recomputes the singular-mode trace, determinant, \(\det(I-Q)\), synchronized-state Rayleigh quotient, the fixed-game example, and the leading small-step expansion. It also compares the complete eigenvalue multiset with \(240\) independently assembled real Floquet products of dimensions \(1\) through \(4\), checks the synchronized expanding projection, and verifies the reduction to OGDA when \(\rho=1/2\). The computation prints `VERIFY_OK` upon success. Only the analytic arguments above establish the universal statement; numerical samples alone are not proofs.

## Relationship to prior work

Zheng, Loizou, You, and Mallada introduced the exact DGDA iteration above and analyzed convergence for *static* bilinear problems. Their update and frozen-game stability theorem are starting points; neither implies stability under switching. Feng and collaborators proved that optimistic GDA can diverge in periodic zero-sum games, and Fiez and collaborators studied periodic games under continuous-time GDA. These establish that time variation can undermine static-game reasoning, so the general qualitative possibility of an instability is **not** presented as new.

There is an exact relationship that must not be obscured: when \(\rho=1/2\), eliminating the auxiliary variable gives, after its first update,
\[
z_{k+2}=\big(I-\eta K_{k+1}\big)z_{k+1}+\frac{\eta}{2}K_kz_k,
\]
which is optimistic GDA at step size \(\eta/2\) on the time-varying game. Thus the \(\rho=1/2\) qualitative instability connects directly to existing optimistic-method counterexamples. The contribution asserted here is instead the *all-damping-parameters* DGDA theorem, its explicit full Floquet spectrum for every invertible square coupling, and divergence for **every** nonzero synchronized primary initialization. The previously identified OGDA periodic example is rectangular and establishes divergence from certain initial conditions; the static DGDA theorem and continuous-time recurrence results cover neither the claimed full parameter set nor the stated all-initialization conclusion.

## Limitations

The theorem does not apply to arbitrary periodic sign patterns, arbitrary nonskew saddle operators, constraints, noisy gradients, noninvertible rectangular matrices, or adaptive parameters. The stable fixed-game example does not say every separate fixed game is stable for every \(\eta\). Some nonzero *unsynchronized* augmented initial states lie in the stable Floquet eigenspace, so their trajectories can converge even when the period map is unstable. The finding makes no independent-audit claim and no priority claim concerning the already-known OGDA periodic instability.

## References

1. T. Zheng, N. Loizou, P. You, E. Mallada, “Dissipative Gradient Descent Ascent Method: A Control Theory Inspired Algorithm for Min-max Optimization,” arXiv:2403.09090v1, first public 2024-03-14. https://arxiv.org/abs/2403.09090
2. Y. Feng, H. Fu, Q. Hu, P. Li, I. Panageas, B. Peng, X. Wang, “On the Last-iterate Convergence in Time-varying Zero-sum Games: Extra Gradient Succeeds where Optimism Fails,” arXiv:2310.02604, first public 2023-10-04. https://arxiv.org/abs/2310.02604
3. T. Fiez, R. Sim, S. Skoulakis, G. Piliouras, L. Ratliff, “Online Learning in Periodic Zero-Sum Games,” arXiv:2111.03377, first public 2021-11-05. https://arxiv.org/abs/2111.03377
