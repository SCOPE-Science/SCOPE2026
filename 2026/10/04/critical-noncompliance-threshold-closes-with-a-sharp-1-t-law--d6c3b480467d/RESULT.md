# Critical noncompliance threshold closes with a sharp \(1/t\) law
## Finding
Consider the constant-control six-compartment SIR model with compliant classes \(S,I,R\), noncompliant classes \(S^*,I^*,R^*\), no noncompliant inflow at birth \(\xi=0\), and
\[
q=\mu^*-\mu>0,\qquad K=\frac b\delta.
\]
The recent stability theorems split the behavioral reproduction ratio into the strict cases below and above one. The equality case has a zero behavioral eigenvalue and is not covered by the cited linear threshold theorem.

At the omitted critical value
\[
\frac{Kq}{\nu+\delta}=1,
\]
the equality case can nevertheless be solved sharply. Let
\[
T=S+I+R+S^*+I^*+R^*,\qquad X=S^*+I^*+R^*.
\]
For every nonnegative solution,
\[
T'=b-\delta T,\qquad X'=\bigl(q(T-X)-(\nu+\delta)\bigr)X.
\]
Writing \(Y=T-K\), the critical equations reduce exactly to
\[
Y'=-\delta Y,\qquad X'=q(Y-X)X.
\]
If \(X(0)>0\), then
\[
\frac1{X(t)}=\exp\!\left[-A(1-e^{-\delta t})\right]
\left(
\frac1{X(0)}+q\int_0^t \exp\!\left[A(1-e^{-\delta s})\right]ds
\right),
\qquad
A=\frac{q(T(0)-K)}{\delta},
\]
and therefore
\[
tX(t)\longrightarrow \frac1q.
\]
If \(T(0)=K\), this simplifies to the exact critical logistic law
\[
X(t)=\frac{X(0)}{1+qX(0)t}.
\]

Now assume the disease reproduction ratio at the fully compliant disease-free equilibrium satisfies
\[
\mathcal R_D=\frac{K\beta(1-\alpha)^2}{\gamma+\eta+\delta}<1.
\]
Then the full equilibrium
\[
E=(K,0,0,0,0,0)
\]
is globally asymptotically stable in the biologically feasible nonnegative state space. Moreover, for every solution with \(X(0)>0\),
\[
tS^*(t)\longrightarrow\frac1q,
\qquad
t\bigl(K-S(t)\bigr)\longrightarrow\frac1q,
\]
while \(I,I^*,R,R^*\) decay exponentially. Thus the critical behavioral direction is algebraically slow even though the epidemiological and recovered directions remain exponentially damped. If \(\mathcal R_D>1\), the equilibrium is unstable because the disease linearization has a positive eigenvalue.

The same equality closure applies to the earlier Parkinson--Wang deterministic model by setting \(\eta=0\) and replacing \(q\) by its noncompliance transmission parameter \(\mu\).
## Assumptions and scope
All controls are fixed nonnegative constants, as in the autonomous disease-free-equilibrium analysis in the cited papers. The parameters satisfy \(b,\delta,\beta,\gamma>0\), \(q>0\), \(\nu,\eta\ge0\), \(0\le\alpha\le1\), \(\xi=0\), and the critical behavioral identity \(Kq=\nu+\delta\). Initial data are finite and componentwise nonnegative.

The sharp \(1/t\) law is asserted only when \(X(0)>0\). If \(X(0)=0\), the noncompliant population remains identically zero. The disease-critical case \(\mathcal R_D=1\) is not classified here.
## Proof
Summing all six equations cancels infection, recovery, treatment, and behavioral-transfer terms, giving
\[
T'=b-\delta T.
\]
Summing only the three noncompliant equations gives
\[
X'=q(S+I+R)X-(\nu+\delta)X
   =\bigl(q(T-X)-(\nu+\delta)\bigr)X.
\]
At \(qK=\nu+\delta\), with \(Y=T-K\), this becomes
\[
Y'=-\delta Y,\qquad X'=q(Y-X)X.
\]
Hence \(Y(t)=Y(0)e^{-\delta t}\). For \(X(0)>0\), setting \(U=1/X\) gives the linear equation
\[
U'+qY(0)e^{-\delta t}U=q.
\]
Its integrating factor is
\[
E(t)=\exp\!\left[\frac{qY(0)}\delta(1-e^{-\delta t})\right],
\]
which yields the displayed exact reciprocal formula. Since \(E(t)\) converges exponentially to a finite positive limit, \(\int_0^t E(s)ds=E(\infty)t+O(1)\), so \(U(t)=qt+O(1)\) and therefore \(tX(t)\to1/q\).

For the disease variables \(z=(I,I^*)^\top\), the equations form a cooperative linear system \(z'=M(t)z\) along any given solution, with
\[
M(t)=\begin{pmatrix}
\beta(1-\alpha)^2S-(\gamma+\eta+\delta)-qX & \beta(1-\alpha)S+\nu\\
\beta(1-\alpha)S^*+qX & \beta S^*-(\gamma+\nu+\delta)
\end{pmatrix}.
\]
We already know \(T\to K\), \(X\to0\), and \(0\le S^*\le X\). For every sufficiently small \(\varepsilon>0\), all sufficiently large times therefore satisfy the componentwise upper bound \(M(t)\le B_\varepsilon\), where
\[
B_\varepsilon=
\begin{pmatrix}
\beta(1-\alpha)^2(K+\varepsilon)-(\gamma+\eta+\delta) & \beta(1-\alpha)(K+\varepsilon)+\nu\\
(\beta(1-\alpha)+q)\varepsilon & \beta\varepsilon-(\gamma+\nu+\delta)
\end{pmatrix}.
\]
At \(\varepsilon=0\), this matrix is upper triangular and Hurwitz exactly when \(\mathcal R_D<1\). Hurwitz stability is open, so some positive \(\varepsilon\) leaves the Metzler matrix \(B_\varepsilon\) Hurwitz. Cooperative comparison then gives exponential decay of \(I\) and \(I^*\).

The recovered pair \((R,R^*)\) is another cooperative linear system forced by the exponentially decaying infections; its limiting coefficient matrix is
\[
\begin{pmatrix}-\delta&\nu\\0&-(\delta+\nu)\end{pmatrix},
\]
which is Hurwitz. The same small-perturbation comparison gives exponential decay of \(R,R^*\). Consequently \(S^*=X-I^*-R^*=X+o(1/t)\), while
\[
S=T-X-I-R=K-X+o(1/t),
\]
which proves the two susceptible asymptotic limits.

Local stability of \(E\) follows from the same estimates: near \(E\), \(Y\) decays exponentially, \(X(t)\le X(0)\exp(qY(0)^+/\delta)\), and the disease and recovery comparison matrices can be kept uniformly Hurwitz. Combined with global attraction, this gives global asymptotic stability for \(\mathcal R_D<1\).

If \(\mathcal R_D>1\), the disease block at \(E\) is upper triangular with eigenvalue
\[
\beta(1-\alpha)^2K-(\gamma+\eta+\delta)>0,
\]
so \(E\) is unstable.
## Verification
The bundled `verifier.py` checks an exact rational point on the critical surface: \(b=\delta=\beta=\gamma=\nu=1\), \(q=2\), \(\alpha=1/2\), \(\eta=0\). It verifies \(Kq/(\nu+\delta)=1\), \(\mathcal R_D=1/8<1\), the zero behavioral linear eigenvalue, the negative disease eigenvalues, and the exact invariant-slice solution \(X(t)=1/(4+2t)\) for \(X(0)=1/4\). The universal asymptotic statement is proved analytically above rather than inferred from these finite checks.
## Relationship to prior work
Parkinson and Wang's 2025 deterministic theorem treats \(b/\delta<(\delta+\nu)/\mu\) and \(b/\delta>(\delta+\nu)/\mu\), and its proof reduces the needed hypothesis to a strict eigenvalue condition. Their abstract describes the local disease-free stability as fully characterized, but the equality makes that eigenvalue zero and falls outside the stated theorem. Ngo, Parkinson, and Wang's later controlled SIR model likewise treats the behavioral reproduction ratio strictly below or strictly above one and explicitly identifies that ratio as governing the compliance--noncompliance SIS-type dynamics.

The 2023 reaction--diffusion predecessor proves asymptotic behavior under strict sufficient conditions that force exponential decay of noncompliance; it does not give this ODE critical equality law. The older SIAR noncompliance model is structurally related but uses a different compartment architecture. Generic SIS theory explains why a quadratic critical term can produce \(1/t\) decay, but it does not by itself provide the exact full-six-compartment profile, the disease/recovery exponential separation, or the equality closure for these recent theorems.
## Limitations
This result concerns the autonomous constant-control systems used for the disease-free-equilibrium threshold analysis. It does not assert a \(1/t\) law under time-varying optimal controls, stochastic forcing, spatial diffusion, or the doubly critical case \(\mathcal R_D=1\). It also does not claim that critical algebraic decay is a new phenomenon for SIS equations in general; the contribution is the exact equality closure and full-state asymptotic profile for these noncompliance models.
## References
1. C. Parkinson and W. Wang, “A Compartmental Model for Epidemiology with Human Behavior and Stochastic Effects,” arXiv:2507.01046; Mathematical Biosciences 392, 109588, DOI 10.1016/j.mbs.2025.109588.
2. C. Ngo, C. Parkinson, and W. Wang, “Optimal Control of an SIR Model with Noncompliance as a Social Contagion,” arXiv:2509.09075.
3. C. Parkinson and W. Wang, “Analysis of a Reaction-Diffusion SIR Epidemic Model with Noncompliant Behavior,” SIAM Journal on Applied Mathematics 83 (2023), 1969–2002, DOI 10.1137/23M1556691.
4. M. Bongarti et al., “Alternative SIAR models for infectious diseases and applications in the study of non-compliance,” Mathematical Models and Methods in Applied Sciences 32 (2022), 1987–2015, DOI 10.1142/S0218202522500464.
