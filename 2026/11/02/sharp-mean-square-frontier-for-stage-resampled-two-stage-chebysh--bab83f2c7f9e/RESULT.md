# Sharp mean-square frontier for stage-resampled two-stage Chebyshev descent

## Finding

The two-stage, undamped Runge–Kutta–Chebyshev descent recurrence has sharply different mean-square stability when it uses **one shared random client across its internal stages** and when it instead samples a **fresh independent client at each stage**. The latter is a variant of the originally published same-client algorithm, not the original algorithm itself.

Let \(C\) be any random curvature supported in the open interval \((0,8)\), with mean \(\mu=\mathbb E C\), variance \(v=\operatorname{Var}(C)\), and independent copies \(C_{n,1},C_{n,2}\) for different macro-steps and stages. For the stage-resampled method defined below, write \(Q=\mathbb E[(x_{n+1}/x_n)^2]\) for its squared amplification (interpreted via the multiplier when \(x_n=0\)). Then

\[
Q-1=\frac{(\mu^2-4\mu+v)(\mu^2-12\mu+v+32)}{64}.
\]

Its mean square strictly contracts geometrically precisely when

\[
\begin{cases}
0<\mu<4\quad\text{and}\quad v<\mu(4-\mu),\\
\text{or}\\
4<\mu<8\quad\text{and}\quad v<(\mu-4)(8-\mu).
\end{cases}
\]

Equality in the appropriate variance threshold makes the mean square constant; larger variance makes it grow geometrically. At \(\mu=4\), \(Q=1+v^2/64\), so any nonzero curvature variance creates mean-square divergence. In contrast, the published same-client version contracts in mean square for any law on \((0,8)\) with no atom at curvature \(4\).

A fully explicit two-client instance has \(\Pr(C=1)=\Pr(C=6)=1/2\). For any deterministic \(x_0\ne0\), independent stage-resampling yields

\[
\mathbb E[x_n]=(-31/32)^n x_0,\qquad
\mathbb E[x_n^2]=(409/256)^n x_0^2,
\]

while \(x_n\to0\) exponentially almost surely, with

\[
\lim_{n\to\infty}\frac1n\log\left|\frac{x_n}{x_0}\right|=\log(\sqrt7/4)<0
\quad\text{almost surely}.
\]

Under the original same-client implementation, the corresponding second moment is instead \(\mathbb E[x_n^2]=(17/128)^n x_0^2\). Both deterministic single-client amplification factors have absolute value less than one. Hence a natural stage-resampling implementation can destroy mean-square stability without destroying convergence of the mean or typical sample paths.

## Assumptions and scope

For every \(c\in(0,8)\), let the component objective be \(f_c(x)=cx^2/2\) on \(\mathbb R\). The population loss is \(F(x)=\mu x^2/2\), with unique minimizer zero. We choose the first-order Chebyshev family with exactly two stages, damping parameter \(\varepsilon=0\), and fixed outer step size \(\alpha=1\). Its coefficients are \(\widetilde\mu_1=1/4\), \(\widetilde\mu_2=1/2\), and \(\nu_2=-1\). With independent client curvatures at both stages, a macro-step is

\[
y_n=x_n-\frac14C_{n,1}x_n,\qquad
x_{n+1}=2y_n-x_n-\frac12C_{n,2}y_n.
\]

All the client draws are independent and identically distributed from \(C\). This is explicitly **stage-resampled SRKCD**, whereas Stillfjord–Williamson's published algorithm reuses one client \(C_n\) in both stages. The curvature support is bounded, so every required moment exists. All results are exact-arithmetic statements with deterministic initial data.

## Proof

**1. Coefficient and random multiplier calculation.** For \(s=2\), \(T_2(z)=2z^2-1\), \(\omega_0=1\), and \(\omega_1=T_2(1)/T'_2(1)=1/4\). Substitution into the published Chebyshev coefficient definitions gives the three coefficients stated above. Eliminating the internal state \(y_n\) gives

\[
x_{n+1}=M_nx_n,\qquad
M_n=1-\frac{C_{n,1}+C_{n,2}}2+\frac{C_{n,1}C_{n,2}}8.
\]

Because the two draws are independent, with \(\mathbb EC^2=\mu^2+v\), expansion and collection of terms yield

\[
\mathbb EM_n=1-\mu+\frac{\mu^2}{8},\qquad
\mathbb EM_n^2=1+\frac{(\mu^2-4\mu+v)(\mu^2-12\mu+v+32)}{64}.
\]

This is an identity for the **entire** class of curvature laws in the stated support, not an approximation. In particular the recurrence is independent across macro-steps and therefore

\[
\mathbb E x_n=x_0(\mathbb EM_0)^n,\qquad
\mathbb Ex_n^2=x_0^2(\mathbb EM_0^2)^n.
\]

**2. Necessary and sufficient mean-square condition.** The first factor in \(Q-1\) is \(\mu(\mu-4)+v\), and the second is \((\mu-4)(\mu-8)+v\). If \(0<\mu<4\), the second factor is strictly positive, and \(Q<1\) precisely when \(v<\mu(4-\mu)\). If \(4<\mu<8\), the first factor is strictly positive and \(Q<1\) precisely when \(v<(\mu-4)(8-\mu)\). For \(\mu=4\), both factors equal \(v\), giving \(Q=1+v^2/64\). Since \(Q\ge0\), at \(Q=1\) the second moment is constant for nonzero initial data, and at \(Q>1\) it grows geometrically. These cases exhaust the parameter range.

**3. Why common-client reuse is different.** Using the same curvature in both stages gives multiplier

\[
R(c)=1-c+\frac{c^2}{8}=\frac{(c-4)^2}{8}-1.
\]

For each \(0<c<8\), one has \(|R(c)|\le1\), with equality only at \(c=4\) within this open interval. Thus \(\mathbb ER(C)^2<1\) whenever \(\Pr(C=4)=0\); the squared error contracts geometrically in that originally published same-client method.

**4. Exact counterexample including almost-sure behavior.** For equally probable curvature values \(1\) and \(6\), the four equally likely ordered stage pairs yield

\[
M(1,1)=1/8,\quad M(1,6)=M(6,1)=-7/4,\quad M(6,6)=-1/2.
\]

Averaging gives \(\mathbb EM=-31/32\) and \(\mathbb EM^2=409/256\). In contrast, \(R(1)=1/8\) and \(R(6)=-1/2\), so \(\mathbb ER(C)^2=17/128\). None of the four stage-resampled multipliers is zero, and their log-magnitudes are integrable. The ordinary strong law for independent identically distributed log-magnitudes therefore gives

\[
\lim_{n\to\infty}\frac1n\log\left|\frac{x_n}{x_0}\right|
=\frac14\log(1/8)+\frac12\log(7/4)+\frac14\log(1/2)
=\log(\sqrt7/4)<0
\quad\text{almost surely}.
\]

This shows exponentially decaying typical trajectories alongside exponentially diverging expected squared error. Since the population excess objective equals \(\mu x_n^2/2\), its expectation diverges at exactly the same factor \(409/256\).

## Verification

Run `python verify.py` after installing the pinned-compatible symbolic dependency described in `requirements.txt`. The script verifies the multiplier and distribution-free moment factorization symbolically, tests exact rational two-client probability grids and diverse finite-support distributions, reconstructs all four client-pair stage updates, and checks the rational first/second moments and exact log-product certificate. The universal claims rest on the preceding algebra and the strong law, rather than on finite experimentation.

## Relationship to prior work

Stillfjord and Williamson (arXiv:2201.12782v1, sections 3–4) define the SRKCD Chebyshev coefficients and explicitly use one sampled batch for all internal stages of a macro-step. Their discussion of deterministic scalar RKC stability and their decreasing-step convergence results are credited. The new theorem concerns the **different, independently stage-resampled implementation**; it gives a sharp distribution-free mean–variance stability phase diagram for the two-stage undamped specialization and compares that variant against the source's same-batch implementation. It does not contradict an original stability guarantee.

Bochacik, Goćwin, Morkisz and Przybyłowicz (arXiv:2006.12131) analyze mean-square and probabilistic stability for a randomized two-stage Runge–Kutta ODE solver under inexact information. The general fact that independent random multipliers have an expected-square criterion is established background; their randomization of stage time and information model does not supply the independently sampled client-curvature Chebyshev factorization, its sharp variance boundary, or the shared-versus-fresh sampling comparison. Results on stochastic differential equation stabilized methods use a different stochastic forcing model.

## Limitations

The phase diagram requires scalar positive quadratic component curvatures supported strictly between zero and eight, exactly two stages, zero damping, a unit outer step, and independent sampling at both stages of the **variant**. The same-batch comparison requires no point mass at curvature four for strict contraction. The result does not cover nonlinear objectives, damping, arbitrary stage counts, arbitrary minibatch correlation, decreasing step sizes, finite precision, or the published algorithm with different hyperparameters. The almost-sure convergence claim is for the displayed two-point example, not every unstable law. Priority relative to older treatments of random-coefficient Runge–Kutta schemes under other terminology remains a literature risk; no independent scientific audit has been performed.

## References

1. Tony Stillfjord and Måns Williamson, *SRKCD: a stabilized Runge–Kutta method for stochastic optimization*, arXiv:2201.12782v1 (first public version, 2022-01-30), https://arxiv.org/html/2201.12782v1, especially equations (3.1)–(3.2), section 3.4, and section 4.
2. Tomasz Bochacik, Maciej Goćwin, Paweł M. Morkisz, and Paweł Przybyłowicz, *Randomized Runge–Kutta method — stability and convergence under inexact information*, arXiv:2006.12131 (first public version, 2020-06-22), https://arxiv.org/abs/2006.12131.
3. Assyr Abdulle, Gilles Vilmart, and Konstantinos C. Zygalakis, *Weak second order explicit stabilized methods for stiff Itô stochastic differential equations* (2013), background for stochastic stabilized integrators with Brownian forcing, not an implication claim.
