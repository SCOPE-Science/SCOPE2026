# A sharp mean-step reversal for adaptive Euler--Maruyama on the Ornstein--Uhlenbeck sampler

## Finding

Consider a scalar Ornstein--Uhlenbeck diffusion
\[
dX_t=-\lambda X_t\,dt+\sigma\,dW_t,
\qquad \lambda,\sigma>0,
\]
whose equilibrium second moment is \(v=\sigma^2/(2\lambda)\). Its state-dependent Euler--Maruyama mesh-point chain is
\[
Y_{n+1}=(1-\lambda h(Y_n))Y_n+\sigma\sqrt{h(Y_n)}Z_{n+1},
\quad Z_n\stackrel{\rm iid}{\sim}N(0,1).
\]
Assume a continuous, even step function \(h:\mathbb R\to(0,\infty)\), nonincreasing with \(|x|\), satisfying \(0<m\le h(x)\le M<2/\lambda\). This chain has a unique symmetric, full-support invariant law \(\pi\) with finite fourth moment. Let \(H=\mathbb E_\pi h(Y)\), \(V=\mathbb E_\pi Y^2\), and define
\[
\Delta= -\operatorname{Cov}_\pi(h(Y),Y^2)\ge0,
\qquad S=\mathbb E_\pi[(h(Y)-H)^2Y^2]\ge0.
\]
The constant-step Euler--Maruyama sampler with step \(H\) has stationary second moment \(V_{\rm fixed}(H)=v/(1-\lambda H/2)\). The adaptive sampler obeys the **exact two-defect identity**
\[
\boxed{\displaystyle
V-V_{\rm fixed}(H)=
\frac{(1-\lambda H)\Delta+(\lambda/2)S}
{H(1-\lambda H/2)}.}
\]
Consequently, whenever \(H\le1/\lambda\), every nonconstant admissible step function has \(V>V_{\rm fixed}(H)\); equality holds exactly for constant step functions. The boundary is sharp: for **each** \(h_0\in(1/\lambda,2/\lambda)\) and \(k>0\), the nonconstant decreasing-tail policy
\[
h_\varepsilon(x)=h_0+\varepsilon e^{-kx^2},
\qquad 0<\varepsilon<2/\lambda-h_0,
\]
produces \(V_\varepsilon<V_{\rm fixed}(H_\varepsilon)\) for every sufficiently small positive \(\varepsilon\). In particular, the sign of the *best universal* mean-step comparison reverses at \(\lambda H=1\).

More quantitatively, setting \(V_0=v/(1-\lambda h_0/2)\), one has the attained first-order comparison
\[
\boxed{\displaystyle
V_\varepsilon-V_{\rm fixed}(H_\varepsilon)
=\varepsilon\frac{(1-\lambda h_0)\,2kV_0^2}
{h_0(1-\lambda h_0/2)(1+2kV_0)^{3/2}}+o(\varepsilon).}
\]
The stationary law is symmetric, so these second moments are variances. Average step length \(H\) is the ergodic physical-time advance per gradient evaluation; the comparison holds this quantity fixed, not the minimum allowed step.

## Assumptions and scope

The noise is independent standard Gaussian at successive mesh points. The coefficients \(\lambda\), \(\sigma\) are fixed positive reals; state-dependent steps are chosen from the pre-step state, not from the next Brownian increment. The step function is continuous and even, monotone nonincreasing with radius, and uniformly bounded below and strictly below \(2/\lambda\). The comparison is between **mesh-point stationary laws** at an equal average physical-time increment per evaluation, not between physical-time path laws, nor between wall-clock costs. For the perturbative witness only, \(k>0\), \(h_0\in(1/\lambda,2/\lambda)\), and \(\varepsilon\downarrow0\).

## Proof

**Existence, uniqueness, moments and symmetry.** Write \(a(x)=1-\lambda h(x)\). Compactness of \([m,M]\subset(0,2/\lambda)\) gives \(q=\sup_x|a(x)|<1\). The conditional inequality \(\mathbb E(Y_{n+1}^2\mid Y_n=x)\le q^2x^2+\sigma^2M\) is a geometric Foster--Lyapunov drift. The Gaussian transition density has positive variance \(\sigma^2h(x)\) and is strictly positive for every pair of states. Continuity makes the chain Feller, and compacts are small sets; consequently there is a unique geometrically ergodic invariant probability with finite second moment and full support. Expanding its fourth conditional moment gives a leading term \(a(x)^4x^4\) with uniform coefficient at most \(q^4<1\); absorb the lower powers of \(|x|\) into a constant and a coefficient strictly below one to obtain a finite fourth moment. As \(a\) and \(h\) are even, the transition kernel is equivariant under reflection, so uniqueness forces \(\pi\) symmetric and \(\mathbb E_\pi Y=0\).

**Exact balance.** Denote \(Z=\mathbb E_\pi[h(Y)Y^2]\) and \(Q=\mathbb E_\pi[h(Y)^2Y^2]\). Conditional Gaussian second moments and stationarity give
\[
0=\mathbb E_\pi(Y_{n+1}^2-Y_n^2)=-2\lambda Z+\lambda^2 Q+\sigma^2H.
\]
Equivalently \(Z=vH+(\lambda/2)Q\). Since \(Z=HV-\Delta\) and \(Q=H^2V-2H\Delta+S\), elementary rearrangement yields
\[
H(1-\lambda H/2)V-vH=(1-\lambda H)\Delta+(\lambda/2)S.
\]
Dividing by the positive quantity \(H(1-\lambda H/2)\) proves the claimed identity. For fixed step \(H\), solving the scalar autoregression Lyapunov equation gives exactly \(V_{\rm fixed}(H)=v/(1-\lambda H/2)\).

**Nonnegative mechanisms and rigidity.** For independent copies \(Y,Y'\) with law \(\pi\),
\[
2\operatorname{Cov}_\pi(h(Y),Y^2)
=\mathbb E[(h(Y)-h(Y'))(Y^2-(Y')^2)]\le0
\]
by radial nonincrease, hence \(\Delta\ge0\). If \(H\le1/\lambda\), both terms in the identity are nonnegative. If \(h\) is nonconstant, its continuity and the full support of \(\pi\) imply \(S>0\); the inequality is then strict, including at \(H=1/\lambda\). Conversely, constant \(h\equiv H\) gives \(\Delta=S=0\), hence equality.

**Sharp reversal and quantitative witness.** Fix \(h_0\in(0,2/\lambda)\), \(k>0\), and \(h_\varepsilon(x)=h_0+\varepsilon e^{-kx^2}\) with sufficiently small \(\varepsilon>0\). These kernels have a common uniform second- and fourth-moment drift and converge uniformly on compact state sets to the constant-step Gaussian kernel. Any weak subsequential limit of their invariant laws is invariant for that limiting kernel. Uniqueness of the fixed-step Gaussian invariant, together with moment uniform integrability, yields \(\pi_\varepsilon\Rightarrow N(0,V_0)\) with convergence of all expectations used below. In particular,
\[
\frac{\Delta_\varepsilon}{\varepsilon}
=-\operatorname{Cov}_{\pi_\varepsilon}(e^{-kY^2},Y^2)
\longrightarrow\frac{2kV_0^2}{(1+2kV_0)^{3/2}}>0,
\]
using Gaussian integration \(\mathbb E[e^{-kX^2}]=(1+2kV_0)^{-1/2}\) and \(\mathbb E[X^2e^{-kX^2}]=V_0(1+2kV_0)^{-3/2}\). Moreover \(H_\varepsilon\to h_0\) and \(0\le S_\varepsilon\le\varepsilon^2\mathbb E_{\pi_\varepsilon}Y^2=O(\varepsilon^2)\). Substitution into the exact identity gives the stated first-order coefficient. Its sign is that of \(1-\lambda h_0\); taking \(h_0>1/\lambda\) proves that no universal nonnegative comparison can extend to mean steps beyond \(1/\lambda\). The strictly smaller variance is compared to the fixed Euler chain with *exactly its own* value \(H_\varepsilon\), not \(h_0\).

## Verification

The independent algebraic cross-check and reproducible deterministic quadrature experiments are in `verify.py`. Running `python verify.py` tests the balance identity over exact rational finite distributions and computes both signs of the sharp reversal for \(\lambda=1\), \(\sigma=\sqrt2\), \(k=1\). Those finite checks support the implementation but cannot replace the argument for arbitrary continuous step policies and all positive parameters. The Gaussian integration and uniform invariant-law limit are proved analytically above.

## Relationship to prior work

Wen, Huang and Li (2026, arXiv:2608.10855, Sections 3 and 8--9) introduce and analyze the state-dependent Euler--Maruyama mesh chain and its invariant measure; their result is the motivating source, not a novelty claim here. Leroy, Leimkuhler, Latz and Higham (2024, arXiv:2403.11993, especially equation (2.10), Sections 2 and 4) discuss how direct time rescaling changes the invariant law and develop corrected dynamics. Those existing insights explain why adaptive sampling has a residence-time bias. The present claim instead resolves the **finite-step OU mean-step-matched second-moment comparison**, including its exact two-defect decomposition, a one-sided universal domain, and an opposite-sign example beyond the sharp boundary. Standard Gaussian autoregression variance and Gaussian integration are used as known tools. No general correction of invariant measures or ergodicity theorem is claimed as new.

## Limitations

This is a scalar quadratic, additive-noise, exact-arithmetic model with independent normal increments and continuous radially decreasing positive steps bounded away from zero and from the Euler stability endpoint. The result does not prove adaptive methods are generally inferior: the perturbative regime above the threshold exhibits the opposite sign. The physical-time invariant distribution, integrated autocorrelation, total computational cost, arbitrary potentials, stochastic step-size rejection, and unboundedly small adaptive steps are outside the theorem. Bibliographic search cannot rule out a prior specialized OU identity; independent review has not been performed.

## References

1. X. Wen, S. Huang, X. Li, *Adaptive Time-Stepping Euler--Maruyama Scheme for SDEs with Non-Globally Lipschitz Coefficients: Uniform Convergence, Stability and Ergodicity* (2026), arXiv:2608.10855, first public 2026-08-11, https://arxiv.org/abs/2608.10855.
2. A. Leroy, B. Leimkuhler, J. Latz, D. J. Higham, *Adaptive Stepsize Algorithms for Langevin Dynamics* (2024), arXiv:2403.11993, SIAM Journal on Scientific Computing 46(6), https://arxiv.org/pdf/2403.11993.
3. H. Lamba, J. C. Mattingly, A. M. Stuart, *An Adaptive Euler--Maruyama Scheme for SDEs: Convergence and Stability* (2007), https://arxiv.org/abs/math/0601029.
4. W. Fang, M. B. Giles, *Adaptive Euler--Maruyama Method for SDEs with Non-globally Lipschitz Drift* (2020), doi:10.1007/s11075-019-00816-9, https://ora.ox.ac.uk/objects/uuid:765dff54-33c5-42c5-a907-0d800c64cbc7.
