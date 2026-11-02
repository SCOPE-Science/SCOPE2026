# Exact moment-instability gap for alternating directed shear diffusion

## Finding
Let \(a,b,D,q>0\). An isotropically noise-driven planar particle alternates at symmetric Poisson rate \(q\) between two **individually Hurwitz-stable** triangular drifts, one coupling coordinate \(2\) into coordinate \(1\) and the other coupling coordinate \(1\) into coordinate \(2\). If \(b>2a\), its sharp second-moment stability threshold is
\[
q_2=\frac{4a^3}{b^2-4a^2},
\]
whereas its sharp first-moment stability threshold is
\[
q_1=\frac{a^2}{b-2a},\qquad
q_1-q_2=\frac{a^2}{b+2a}>0.
\]
Consequently, throughout the nonempty interval \(q_2\le q<q_1\), every finite first moment decays exponentially, but the positional second moment driven by arbitrarily weak independent Brownian noise grows without bound: linearly at \(q=q_2\) and exponentially for \(q_2<q<q_1\). For \(b\le2a\) both first and second moments are stable for every finite \(q>0\). These are complete sharp classifications, including their boundaries, not merely sufficient stability criteria.

For \(4a^2(a+q)>b^2q\), the process has a unique finite-second-moment stationary law, whose covariance is exactly
\[
\operatorname{Cov}(X)=\frac{D}{4a^2(a+q)-b^2q}
\begin{pmatrix}
4a(a+q)+b^2 & 2b(a+q)\\
2b(a+q) & 4a(a+q)+b^2
\end{pmatrix}.
\]
The divergence is not a perfectly synchronized fluctuation: on approaching the second-moment threshold from the stable side, and also along the critical long-time growth,
\[
\lim_{q\uparrow q_2}\frac{\operatorname{Cov}(X_1,X_2)}{\operatorname{Var}(X_1)}
=\lim_{t\to\infty}\frac{\mathbb E[X_{1,t}X_{2,t}]}{\mathbb E[X_{1,t}^2]}\bigg|_{q=q_2}
=\frac{2a}{b}\in(0,1),
\]
with \(X_0=0\) and stationary environment in the time-limit statement. The two sharp thresholds, the covariance formula, and this critical correlation together constitute the single assessed result: a complete moment phase diagram for a minimal nonreciprocal system with temporally reversing directed couplings.

## Assumptions and scope
Let \(S_t\) be a stationary continuous-time Markov chain with state space \(\{+,-\}\) and transitions in each direction at rate \(q>0\). Let \(W_t\) be standard two-dimensional Brownian motion independent of \(S\). Define the unique continuous solution to
\[
dX_t=A_{S_t}X_t\,dt+\sqrt{2D}\,dW_t,
\qquad
A_+=\begin{pmatrix}-a&b\\0&-a\end{pmatrix},\qquad
A_-=\begin{pmatrix}-a&0\\b&-a\end{pmatrix}.
\]
All parameters \(a,b,D,q\) are finite and strictly positive. Both instantaneous matrices have eigenvalue \(-a\) of multiplicity two. The first-moment classification concerns exponential decay of \(\mathbb E X_t\) for every integrable initial state and every initial environment law, with the usual independent driving assumption. The second-moment classification concerns the homogeneous linear switched flow and, with additive Brownian forcing, finiteness of asymptotic second moments. For the explicit finite-time covariance expressions and the divergence assertions, take \(X_0=0\) with \(S_0\) stationary. The process may have a stationary probability distribution with *infinite* variance outside the finite-variance regime; no nonexistence of such a distribution is claimed.

## Proof
**First moments.** Introduce the unnormalized environment-conditioned means \(m_\pm(t)=\mathbb E[X_t\mathbf1_{\{S_t=\pm\}}]\). The two-state generator gives
\[
\dot m_+=(A_+-qI)m_++q m_-,\qquad
\dot m_-=(A_--qI)m_-+q m_+.
\]
Coordinate swap combined with environment swap decomposes this four-dimensional system into two invariant two-dimensional blocks,
\[
N_+=\begin{pmatrix}-a-q&b+q\\q&-a-q\end{pmatrix},
\qquad
N_-=\begin{pmatrix}-a-q&b-q\\-q&-a-q\end{pmatrix}.
\]
The dominant eigenvalue of \(N_+\) is \(-a-q+\sqrt{q(q+b)}\). The real parts of the eigenvalues of \(N_-\) are strictly smaller: if \(q<b\) they equal \(-a-q\), while if \(q\ge b\) the larger is \(-a-q+\sqrt{q(q-b)}\). Thus all first moments decay exponentially exactly when
\[
q(b-2a)<a^2.
\]
For \(b>2a\) this gives \(q<q_1=a^2/(b-2a)\); at equality a simple neutral mode exists, and above it a growing mode exists. For \(b\le2a\) the inequality holds for all finite \(q\).

**Second moments and exact covariance.** For \(X_0=0\) and stationary \(S_0\), symmetry under simultaneous coordinate/environment interchange persists. Set
\[
u(t)=\mathbb E[X_{1,t}^2\mathbf1_{\{S_t=+\}}],\qquad
v(t)=\mathbb E[X_{2,t}^2\mathbf1_{\{S_t=+\}}],\qquad
w(t)=\mathbb E[X_{1,t}X_{2,t}\mathbf1_{\{S_t=+\}}].
\]
The opposite-environment conditional second moments are \(v,u,w\). Itô's formula and the switching generator yield the *exact* finite-time affine system
\[
\frac{d}{dt}\begin{pmatrix}u\\v\\w\end{pmatrix}
=M_+\begin{pmatrix}u\\v\\w\end{pmatrix}
+\begin{pmatrix}D\\D\\0\end{pmatrix},\qquad
M_+=\begin{pmatrix}-2a-q&q&2b\\q&-2a-q&0\\0&b&-2a\end{pmatrix}.
\]
With zero initial state, its solution is \(z(t)=\int_0^t e^{M_+(t-s)}(D,D,0)^\mathsf T\,ds\), and the full covariance has diagonal entry \(u(t)+v(t)\) and off-diagonal entry \(2w(t)\). The characteristic polynomial of \(M_+\) is
\[
p_+(\lambda)=\lambda^3+2(3a+q)\lambda^2+4a(3a+2q)\lambda
+2\bigl[4a^2(a+q)-b^2q\bigr].
\]
Its cubic Routh–Hurwitz determinant is
\[
2(3a+q)\,4a(3a+2q)
-2[4a^2(a+q)-b^2q]
=2(32a^3+32a^2q+8aq^2+b^2q)>0.
\]
The other relevant coefficients are always strictly positive except possibly the constant. Hence \(M_+\) is Hurwitz **if and only if** \(h=4a^2(a+q)-b^2q>0\). If \(h=0\), the cubic has one simple zero root and the other two roots have negative real parts. If \(h<0\), it has a positive real root. Moreover, \(M_+\) is irreducible Metzler. Its dominant right and left eigenvectors may be chosen strictly positive, so the positive forcing vector has strictly positive projection onto its Perron eigenspace. The integral formula then implies linear growth of \(u+v\) at \(h=0\), exponential growth at \(h<0\), and finite convergence at \(h>0\).

To check that an unsymmetrized initial condition cannot introduce an earlier unstable second-moment mode, the coordinate/environment antisymmetric sector has matrix
\[
M_-=\begin{pmatrix}-2a-q&-q&2b\\-q&-2a-q&0\\0&b&-2a-2q\end{pmatrix}.
\]
Its characteristic polynomial coefficients, from highest to lowest, are
\[
1,\quad 2(3a+2q),\quad 4(a+q)(3a+q),\quad 2[4a(a+q)^2+b^2q].
\]
The associated Routh–Hurwitz determinant is
\[
2(32a^3+64a^2q+40aq^2+8q^3-b^2q).
\]
Whenever \(h\ge0\), the estimate \(b^2q\le4a^2(a+q)\) makes this strictly positive. Thus the antisymmetric sector is Hurwitz at and below the positive-sector threshold. This verifies sharp mean-square stability of the entire homogeneous switched flow, not only of one symmetric initial law.

Solving \(M_+z+(D,D,0)^\mathsf T=0\) at \(h>0\) gives
\[
u_*=\frac{D[2a(a+q)+b^2]}h,\quad
v_*=\frac{2Da(a+q)}h,\quad
w_*=\frac{Db(a+q)}h.
\]
The stated covariance follows by reflection symmetry. At the critical boundary, substitution of \(q_2=4a^3/(b^2-4a^2)\) into the ratio of the off-diagonal and diagonal expressions yields exactly \(2a/b\). Since at this boundary the critical moment trajectory grows along the simple positive null eigenvector of \(M_+\), the same ratio is obtained from its leading linear-in-time moments. Exponential mean-square stability constructs a two-sided stationary stochastic convolution with finite second moment; contraction also establishes its uniqueness among stationary solutions with finite second moment. Conversely, if a finite-second-moment stationary solution existed for \(h\le0\), its reflection symmetrization would satisfy the stationary moment equation with positive forcing, contradicting the irreducible Metzler stability boundary. Thus \(h>0\) is also necessary for finite stationary covariance.

Finally, \(h=4a^3+(4a^2-b^2)q\). When \(b\le2a\) it is strictly positive for every finite \(q>0\). When \(b>2a\), its unique zero occurs at \(q_2=4a^3/(b^2-4a^2)\). Direct subtraction gives
\[
q_1-q_2=\frac{a^2}{b+2a}>0,
\]
which completes the sharp three-regime classification.

## Verification
The self-contained Python-standard-library checker in `artifacts/verify.py` verifies exact rational stationary moment balances, the cubic characteristic polynomial, positive-definiteness in the stable regime, strict ordering and distance of the two critical rates, and finite-time numerical diagnostics for stable, critical and unstable regimes. It reports `VERIFY_OK 3269` on the included parameter grid. These calculations are independently reproducible but do not replace the algebraic Routh–Hurwitz proof or the Perron projection argument for all positive parameters.

For the concrete parameters \(a=D=1\), \(b=3\), the second-moment and first-moment boundaries are respectively \(q_2=4/5\) and \(q_1=1\). At \(q=1/2\), the stationary covariance equals \(\begin{psmallmatrix}10&6\\6&10\end{psmallmatrix}\); at \(q=9/10\), all first moments decay but the noise-forced second moments grow exponentially. At \(q=4/5\) they grow linearly.

## Relationship to prior work
Ferraro, Grilletta, Maritan, Suweis and Azaele (2024) obtain a time-correlated annealed-interaction phase diagram and stationary variance for a large-dimensional Gaussian-disorder linear system in a dynamical mean-field limit. Their Figure 6 already exhibits a regime where the mean remains finite while variance diverges; that qualitative moment separation is **prior work**, not claimed here. Here the interactions are *two-state, common, directional and mutually exclusive*, with exactly two components; their Gaussian large-system results neither give the displayed Markov-switching matrices nor yield the two explicit moment thresholds.

Ogura and Preciado (2015) establish general moment-stability spectral criteria for Markov-regenerative switched linear systems, encompassing the present switching mechanism. The general criterion is prior knowledge and is not claimed as new. Its spectral test alone does not provide the closed algebraic critical rates, the strict mean-versus-variance interval, the finite stationary covariance or its Brownian-forcing divergence for these shears; deriving those requires the explicit invariant-sector reductions and characteristic polynomials above. Sturman and Thiffeault (2019) analyze related random products of two shears and provide bounds for Lyapunov and generalized Lyapunov exponents, but use discrete independent shear factors rather than continuously driven Poisson-alternating damped diffusions with additive noise. Their conclusions do not state this exact moment phase diagram. In this sense the new claim is a specific model-level exact phase classification, not a new general jump-linear stability theory.

## Limitations
All results assume symmetric two-state exponential switching, identical damping \(a\), identical positive coupling amplitude \(b\), isotropic independent additive Brownian noise and exactly two coordinates. The claim about exponential growth concerns ensemble second moments, not almost-sure sample-path growth or nonexistence of an invariant law without finite variance. Critical linear growth is a long-time statement; finite integrations cannot establish it. The result does not claim a threshold for general unequal shears, non-Markov dwell laws, nonlinear interactions or large-dimensional Gaussian annealed disorder. More general literature on Markov-jump moment criteria could contain an equivalent explicit two-shear example under other notation; this remains a priority-comparison risk.

## References
1. F. Ferraro, C. Grilletta, A. Maritan, S. Suweis and S. Azaele, “Exact solution of Dynamical Mean-Field Theory for a linear system with annealed disorder,” arXiv:2405.05183v1, 8 May 2024, https://arxiv.org/abs/2405.05183.
2. M. Ogura and V. M. Preciado, “Stability of Markov regenerative switched linear systems,” arXiv:1501.03474, 2015, https://arxiv.org/abs/1501.03474.
3. R. Sturman and J.-L. Thiffeault, “Lyapunov Exponents for the Random Product of Two Shears,” *Journal of Nonlinear Science* **29** (2019), 593–620, https://doi.org/10.1007/s00332-018-9497-3.
