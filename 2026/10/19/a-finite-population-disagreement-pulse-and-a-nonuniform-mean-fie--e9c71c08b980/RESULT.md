# A finite-population disagreement pulse and a nonuniform mean-field limit in symmetric persuasion

## Finding

In the symmetric finite-agent persuasion rule of Cao and Cortez, with initially neutral opinions, the expected empirical opinion variance rises from zero to a unique maximum at a logarithmic time, then decays to zero on a population-size timescale. This is an exact finite-population statement, not an asymptotic closure. Its two-exponential representation is

\[
\mathbb E S_N(t)=\frac{\mu^2(N-1)}{2N(r_{s,N}-r_{f,N})}\left(e^{r_{s,N}t}-e^{r_{f,N}t}\right),\qquad t\ge0.
\]

The decay exponents \(r_{f,N}<r_{s,N}<0\) are specified explicitly below. For every fixed \(0<\mu<1\),

\[
t_{\mathrm{peak}}(N,\mu)=\frac{2}{\mu(2-\mu)}\left[\log N+\log\left(\frac{(2-\mu)^2}{2\mu}\right)\right]+o(1),
\]

\[
\lim_{N\to\infty}\mathbb E S_N(Ns)=\frac{\mu}{2-\mu}\exp\left(-\frac{\mu^2}{2-\mu}s\right)\quad(s>0),
\]

and the maximum height converges to \(\mu/(2-\mu)\). By contrast, first taking the population limit and then the long-time limit gives this strictly positive Bernoulli-convolution variance, while taking the long-time limit at each finite population gives zero. Indeed the finitely many opinions converge almost surely to unanimity at either extreme, each with probability one half. Consequently, the infinite-population approximation does not converge uniformly in time, even at the level of a one-agent Wasserstein distance.

## Assumptions and scope

Fix an integer \(N\ge2\) and \(0<\mu<1\). Initially \(X_i^N(0)=0\) for all \(1\le i\le N\). Every agent's opinion remains in \([-1,1]\). At the jump times of a Poisson clock of total rate \(N/2\), select a uniformly random ordered pair of distinct agents \((i,j)\). Conditional on all opinions, choose \(\xi\in\{-1,+1\}\) with \(\mathbb P(\xi=1\mid X)=(1+X_j)/2\), and update only the listener via

\[
X_i\longleftarrow (1-\mu)X_i+\mu\xi.
\]

This is the symmetric specialization of the finite-system update rule (1.1) in [1], with its stated total Poisson rate \(N/2\). If instead each listener updates at rate one, every time variable and inverse decay exponent in the formulas below is divided by two; the stationary and population-scale conclusions are otherwise unchanged. Throughout, \(\log\) means natural logarithm.

Write

\[
M_N(t)=\frac1N\sum_{i=1}^N X_i^N(t),\qquad
S_N(t)=\frac1N\sum_{i=1}^N\bigl(X_i^N(t)-M_N(t)\bigr)^2.
\]

Define, for the fixed parameters,

\[
\begin{aligned}
a_N&=\frac{\mu(2-\mu)}2+\frac{\mu(1-\mu)}{N-1},\\
b_N&=\frac{\mu(1-\mu)N}{N-1},\\
d_N&=\frac{\mu^2}{N-1},\\
e_N&=\frac{\mu^2(N+1)}{2N(N-1)},
\end{aligned}
\]

and

\[
\begin{aligned}
r_{s,N}&=-\frac{a_N+d_N}{2}+\frac12\sqrt{(a_N-d_N)^2+4b_Ne_N},\\
r_{f,N}&=-\frac{a_N+d_N}{2}-\frac12\sqrt{(a_N-d_N)^2+4b_Ne_N}.
\end{aligned}
\]

The terms \(s\) and \(f\) denote slow and fast modes; the parameter \(s>0\) appearing in the population-scale limit is a dimensionless time variable and is unrelated to either mode label.

## Proof

**1. Exact two-moment generator.** Write \(m=N^{-1}\sum_i x_i\), \(v=N^{-1}\sum_i x_i^2\) in a deterministic state \(x\in[-1,1]^N\). An ordered pair has event rate \(1/[2(N-1)]\). Since \(\mathbb E(\xi\mid x)=x_j\) and \(\mathbb E(\xi^2\mid x)=1\), direct summation over all distinct ordered pairs gives

\[
\mathcal Lm=0,
\]

\[
\mathcal L(m^2)=\frac{\mu^2}{2N}+e_N v-d_Nm^2,
\qquad
\mathcal Lv=\frac{\mu^2}{2}+b_Nm^2-a_Nv.
\]

For instance the quadratic variation contribution to \(\mathcal L(m^2)\) is \(\mu^2\sum_{i\ne j}\mathbb E[(\xi-x_i)^2\mid x]/[2N^2(N-1)]\). The exact sums use \(\sum_{i\ne j}x_ix_j=N^2m^2-Nv\). Bounded jumps justify applying the generator and taking expectations for every finite time.

Set \(U_N(t)=\mathbb E[M_N(t)^2]\) and \(V_N(t)=\mathbb E[N^{-1}\sum_i X_i^N(t)^2]\). Then

\[
\begin{aligned}
\dot U_N&=\frac{\mu^2}{2N}+e_NV_N-d_NU_N,\\
\dot V_N&=\frac{\mu^2}{2}+b_NU_N-a_NV_N,
\end{aligned}\qquad U_N(0)=V_N(0)=0.
\]

**2. Exact two-exponential disagreement.** With \(A_N=1-U_N\) and \(B_N=1-V_N\), constant terms cancel exactly, leaving

\[
\frac{d}{dt}\begin{pmatrix}A_N\\B_N\end{pmatrix}=
\begin{pmatrix}-d_N&e_N\\b_N&-a_N\end{pmatrix}
\begin{pmatrix}A_N\\B_N\end{pmatrix},\qquad(A_N(0),B_N(0))=(1,1).
\]

The determinant of the matrix is the strictly positive quantity

\[
a_Nd_N-b_Ne_N=\frac{\mu^3}{2(N-1)},
\]

and its trace is negative. Its off-diagonal entries are positive, so its two eigenvalues are the distinct strictly negative numbers \(r_{s,N}\) and \(r_{f,N}\). Since \(\mathbb ES_N=V_N-U_N=A_N-B_N\), it solves the associated scalar second-order equation and vanishes initially. Its initial derivative is exactly \(\mu^2(N-1)/(2N)>0\). These two initial data force the asserted two-exponential formula; they also prove \(\mathbb ES_N(t)>0\) for \(t>0\).

**3. Unique peak and population-scale collapse.** Differentiate the exact formula. The derivative vanishes if and only if \(e^{(r_{s,N}-r_{f,N})t}=r_{f,N}/r_{s,N}>1\). Thus the peak is unique and is exactly

\[
t_{\mathrm{peak}}=\frac{\log(r_{f,N}/r_{s,N})}{r_{s,N}-r_{f,N}}.
\]

The trace and determinant above imply, at fixed \(\mu\in(0,1)\),

\[
r_{f,N}=-\frac{\mu(2-\mu)}2+O(N^{-1}),\qquad
r_{s,N}=-\frac{\mu^2}{(2-\mu)N}+O(N^{-2}).
\]

Substitution proves the full displayed logarithmic peak-time expansion, including its constant term and \(o(1)\) remainder. The exact amplitude tends to \(\mu/(2-\mu)\); at time \(Ns\), the fast exponential disappears and the slow exponential tends to \(\exp[-\mu^2s/(2-\mu)]\), giving the stated collapse profile. Because \(t_{\mathrm{peak}}/N\to0\) and the peak-to-fast-mode exponential vanishes, its height tends to \(\mu/(2-\mu)\). For each fixed \(t\), the formula instead yields

\[
\lim_{N\to\infty}\mathbb ES_N(t)=\frac{\mu}{2-\mu}\bigl(1-e^{-\mu(2-\mu)t/2}\bigr).
\]

**4. Endpoint unanimity and nonuniformity.** Since \(\mathcal LM_N=0\) and \(M_N\) is bounded, it is a martingale converging almost surely to \(M_\infty\). Both eigenvalues are negative, hence \(U_N(t)\to1\); bounded convergence gives \(\mathbb E M_\infty^2=1\), hence \(M_\infty\in\{-1,+1\}\) almost surely. As all \(X_i\le1\) and all \(X_i\ge-1\), the convergence of their average to either endpoint forces each coordinate to converge to the same endpoint. The martingale starts at mean zero, so each endpoint occurs with probability \(1/2\).

For the corresponding zero-mean infinite-population limit, the stationary one-agent law \(\rho_\infty\) is the Bernoulli convolution from [1], with second moment \(\mu/(2-\mu)\). At finite population, the tagged opinion converges in law to \((\delta_{-1}+\delta_{+1})/2\). The test function \(x\mapsto x^2/2\) is 1-Lipschitz on \([-1,1]\). Kantorovich–Rubinstein duality therefore yields, for every finite \(N\),

\[
\liminf_{t\to\infty}W_1\bigl(\operatorname{Law}(X_1^N(t)),\rho_t\bigr)
\ge\frac{1-\mu}{2-\mu}>0,
\]

where \(\rho_t\) is the zero-mean mean-field one-agent law with the same half-rate normalization. In particular \(\liminf_{N\to\infty}\sup_{t\ge0}W_1(\operatorname{Law}(X_1^N(t)),\rho_t)\) obeys the same positive lower bound. Thus even one-particle marginal convergence cannot be uniform in time.

## Verification

The standalone script `verify.py` uses exact rational arithmetic to independently enumerate the generator for heterogeneous states and check all the moment coefficients and determinant identity. It then checks the exact spectral modes, uniqueness of the predicted maximum and the large-population time scales numerically over multiple population sizes and interaction parameters. Run `python3 verify.py` using Python 3 standard library; it reports 240 generator/spectral/asymptotic assertions passed. The analytical proof, not these finite tests, establishes all-population and infinite-time claims.

## Relationship to prior work

Cao and Cortez [1] introduced the finite-agent Poisson persuasion process, rigorously derived its finite-horizon mean-field limit, and identified the symmetric mean-field stationary law as a Bernoulli convolution. Their Section 5 explicitly lists uniform-in-time propagation of chaos as a desirable future result. The present theorem provides an exact finite-size disagreement trajectory and shows that such uniform-in-time convergence is impossible in the original conformist model, even for one marginal with deterministic zero initial opinions. The mean-field moment calculation in their Lemma 3.1 is a known input and not claimed here.

Lanchier and Mercer [2] studied related finite-graph kindness dynamics, particularly asymmetric response strengths, and proved endpoint convergence. This supplies qualitative precedent for eventual finite-system consensus, but does not imply the two finite-size eigenvalues, logarithmic peak, or precise crossover obtained here. Cao and Cortez [3] subsequently studied a variant with a different persuader-dependent sign rule and uniform-in-time estimates; that later variant is not the update rule analyzed here. Standard voter-model fixation and martingale methods inform the last part of the proof; none of these classical ideas is claimed as new.

## Limitations

The exact formula and constants are established only for the complete-graph symmetric-response Poisson dynamics, deterministic all-zero initial conditions, and fixed \(\mu\in(0,1)\). The theorem measures expected empirical variance, not the distribution or concentration of the random empirical variance. It does not assert a full critical-window limit theorem for the random opinion histogram. No sharp Wasserstein convergence rate at times proportional to \(N\) is claimed. The exact time constants depend on the explicit Poisson clock convention, while the stationary second moment does not. Independent publication-priority verification beyond the inspected literature remains possible.

## References

[1] F. Cao and R. Cortez, *Fractal opinions among interacting agents*, arXiv:2408.01624v1 (public 2024-08-03); SIAM Journal on Applied Dynamical Systems 24 (2025), 1529–1552, DOI:10.1137/24M1682269. See the finite-agent rule (1.1), Proposition 2.1, Lemma 3.1, Section 4, and Section 5. https://arxiv.org/html/2408.01624v1

[2] N. Lanchier and M. Mercer, *Limiting behavior of a kindness model*, arXiv:2402.02579v1 (2024-02-04), Theorem 1 and Section 2. https://arxiv.org/abs/2402.02579

[3] F. Cao and R. Cortez, *The fractal geometry of opinion formation*, arXiv:2601.21023v2 (2026-07-27), model definition and uniform-in-time estimates for a distinct variant. https://arxiv.org/abs/2601.21023
