# Uniform global entropy decay under arbitrarily switching stage-antagonistic ecological interactions

## Finding
For any integer \(n\ge3\), there is a natural two-stage generalized Lotka–Volterra network in which opposing predator–prey interactions may have arbitrarily large, rapidly switching strengths without impairing global convergence to the positive homogeneous equilibrium. The network admits an explicit entropy-decay rate independent of all interaction coefficients.

Let \(s\ge0\) denote time. For any \(n\times n\) matrix \(A(s)\), let \([A(s)u]_i=\sum_{j=1}^n a_{ij}(s)u_j\). Consider
\[
\begin{aligned}
\dot u_i&=m(s)(v_i-u_i)+u_i\bigl(2-u_i-v_i+[A(s)u]_i\bigr),\\
\dot v_i&=m(s)(u_i-v_i)+v_i\bigl(2-u_i-v_i-[A(s)v]_i\bigr).
\end{aligned}
\]
Suppose that almost everywhere \(A(s)^\mathsf T=-A(s)\), \(A(s)\mathbf1=0\), and \(m(s)\ge m_0\ge2\). Every positive solution exists globally and converges to \((\mathbf1,\mathbf1)\). More quantitatively, set
\[
\Phi(z)=z-1-\log z,\qquad V(s)=\sum_{i=1}^n\bigl[\Phi(u_i(s))+\Phi(v_i(s))\bigr].
\]
For \(V_0=V(0)>0\), define \(\ell\in(0,1)\) and \(L\in(1,\infty)\) by \(\Phi(\ell)=\Phi(L)=V_0\). Then the exact bound is
\[
V(s)\le V_0\exp(-\kappa s),\qquad
\kappa=4\ell^2\min\left\{1,\frac{m_0}{L^2}\right\}>0.
\]
For \(V_0=0\) the solution remains at equilibrium. At fixed \(V_0\), the rate bound is independent of \(n\), \(A(s)\), its amplitude, temporal switching, and any upper bound on \(m(s)\). The small-perturbation limit \(\kappa\to4\) is the sharp interaction-uniform linear entropy rate, as seen when \(A=0\) and \(u=v\).

## Assumptions and scope
Each coefficient function is Lebesgue measurable and locally essentially bounded on \([0,\infty)\). The initial data satisfy \(u_i(0)>0\), \(v_i(0)>0\) for every \(i\). The skew and zero-row-sum hypotheses hold almost everywhere; no continuity or common bound in time is required for \(A\). The balance condition \(A(s)\mathbf1=0\) is essential to keep the reference equilibrium fixed with the chosen stage-independent demographic parameters.

These equations specialize the two-life-stage formulation of Garmire and O'Dwyer [1]: same-species stage interactions are \(-1\), for distinct species \(i,j\) the stage-interaction block is \(\operatorname{diag}(a_{ij},-a_{ij})\), the two demographic conversions are both \(m(s)\), and the two stage-specific mortality parameters both equal \(2-m(s)\le0\). The off-diagonal stage block has zero sum, but this deterministic balanced class is **not asserted** to be the equicorrelated random ensemble of [1]. Allowing time-dependent coefficients is a further deterministic extension of that model.

There are genuinely nonzero examples with fixed \(m\): for \(n=3\) take
\[
A(s)=h(s)\begin{pmatrix}0&1&-1\\-1&0&1\\1&-1&0\end{pmatrix},
\]
where \(h(s)\) is any locally essentially bounded real scalar, however large or rapidly varying. No small-interaction hypothesis is imposed. For \(n=2\), the simultaneous row-balance and skew conditions force \(A=0\), which motivates the nontrivial range \(n\ge3\).

## Proof
**1. Positive solutions and exact identity.** The vector field is measurable in time, locally bounded on bounded time intervals, and locally Lipschitz in states. It therefore has a unique maximal Carathéodory solution from positive initial values. On its positive lifetime, differentiating \(\Phi\) yields
\[
\dot V=\sum_i\left[\left(1-\frac1{u_i}\right)\dot u_i+
\left(1-\frac1{v_i}\right)\dot v_i\right].
\]
Write \(a=u-\mathbf1\), \(b=v-\mathbf1\). Since \(A\mathbf1=0\), the contribution from the interactions is \(a^\mathsf T A a-b^\mathsf T A b=0\), using skew-symmetry separately for both stages. The common density regulation contributes \(-\sum_i(a_i+b_i)^2\). The paired conversion contributes \(-m(s)\sum_i(u_i-v_i)^2/(u_i v_i)\). Thus the **exact dissipation identity** is
\[
\boxed{\ \dot V(s)=-\sum_i(u_i+v_i-2)^2-
 m(s)\sum_i\frac{(u_i-v_i)^2}{u_i v_i}\ }
\]
for almost every \(s\) along positive solutions. Both sums vanish simultaneously if and only if all \(u_i=v_i=1\).

**2. Global existence.** The scalar function \(\Phi(z)\) is nonnegative on \((0,\infty)\), is zero only at \(1\), and tends to infinity at either boundary \(z\downarrow0\) or \(z\uparrow\infty\). The identity implies \(V(s)\le V_0\) before any possible exit. Thus each coordinate lies in the compact positive interval \([\ell,L]\), where the endpoints are as stated (if \(V_0=0\), the state is equilibrium). Such a state cannot reach the boundary of the positive orthant or diverge in finite time. Standard continuation for locally bounded Carathéodory vector fields proves existence on all \([0,\infty)\).

**3. Quantitative decay.** On \([\ell,L]\), the second derivative satisfies \(\Phi''(z)=1/z^2\le1/\ell^2\). Taylor's theorem around \(1\) gives
\[
 V(s)\le\frac1{2\ell^2}\sum_i\bigl[(u_i-1)^2+(v_i-1)^2\bigr].
\]
Set \(p_i=(u_i-1)+(v_i-1)\) and \(q_i=(u_i-1)-(v_i-1)\). Since \(u_i v_i\le L^2\) and \(m(s)\ge m_0\), the exact identity gives
\[
-\dot V\ge \min\{1,m_0/L^2\}\sum_i(p_i^2+q_i^2)
=2\min\{1,m_0/L^2\}\sum_i[(u_i-1)^2+(v_i-1)^2]
\ge4\ell^2\min\{1,m_0/L^2\}V.
\]
Gronwall's inequality gives the asserted exponential estimate for every \(s\ge0\). The bound \(\Phi''\ge1/L^2\) also gives \(\sum_i[(u_i-1)^2+(v_i-1)^2]\le2L^2V(s)\), so each coordinate converges exponentially to its equilibrium value.

**4. Sharp interaction-uniform local benchmark.** When \(A=0\), the linearized sum and difference modes have eigenvalues \(-2\) and \(-2m\). The slow eigenmode decays like \(e^{-2s}\), so its quadratic entropy decays like \(e^{-4s}\). As initial perturbations vanish, \(\ell,L\to1\); because \(m_0\ge2\), the certified entropy rate tends to \(4\). No interaction-uniform bound can improve this limiting exponent.

## Verification
The standalone checker `checker.py` evaluates the exact entropy identity with rational arithmetic for 48 independently generated nontrivial balanced skew matrices, population sizes \(3,4,5,7\), and positive rational states and maturation rates. It also integrates a five-population system with strong, rapidly varying balanced skew interactions and time-varying maturation, checking that the computed entropy satisfies the displayed uniform exponential bound. Run `python checker.py` with NumPy and SciPy installed. These finite computations are corroborative; the proof above establishes the infinite-time assertion.

## Relationship to prior work
Garmire and O'Dwyer [1] introduce the two-stage generalization with strong within/between-stage self competition. They derive random-matrix **local** stability thresholds, particularly in a fast-demography limit, and explicitly identify finite demographic rates and biased interaction types as directions for further analysis. The present result instead gives a deterministic, nonlinear, all-positive-initial-data, **time-dependent** convergence guarantee with an explicit coupling-independent entropy rate in a balanced skew subfamily. It neither claims a stochastic stability threshold nor equates this subfamily with their random equicorrelation ensemble.

Anish, De Baets, and Rao [2] study global convergence by detailed-balanced migration between separately antisymmetric Lotka–Volterra patches. The present equations have additional nonlinear *within-species cross-stage crowding* and an arbitrary time-dependent interaction matrix; the particular uniform exponential estimate does not appear in the inspected material from [2]. Márton, Hangos, and Magyar [3] analyze migration-linked controlled Lotka–Volterra networks, using general storage functions and controlled skew-negative interactions. The entropy function and skew cancellation used here share this classical lineage; the new statement is the precise quantitative switching-robust conclusion for the stated biological two-stage model. Goh [4] is a foundational antecedent for global stability of unstructured Lotka–Volterra systems, but the off-diagonal linear stage-conversion terms make those unstructured models distinct.

## Limitations
The row-balanced skew structure is restrictive and does not imply that arbitrary biased, random, or equicorrelated stage-dependent networks are globally stable. The theorem does not cover negative initial states, logistic coefficients other than the stated normalized values, nonsymmetric maturation between stages, delayed maturation, or stochastic perturbations. The rate \(\kappa\) may be conservative for finite disturbances; its sharpness claim concerns its infinitesimal **interaction-uniform** limit only. Earlier general dissipativity/migration theorems are related and could potentially give alternative proofs or stronger generalizations; novelty is asserted for the specific nonautonomous quantitative claim, not for the entropy function or the skew-symmetry trick.

## References
[1] G. Garmire and J. P. O'Dwyer, *Heterogeneity among and competition between life stages together extend the stability boundary of complex ecological communities*, arXiv:2610.23557v1, first submitted 2026-10-16, https://arxiv.org/abs/2610.23557.

[2] A. S. Anish, B. De Baets, and S. Rao, *Metapopulation models with anti-symmetric Lotka–Volterra systems*, Journal of Biological Dynamics 18 (2024), 2397404, https://doi.org/10.1080/17513758.2024.2397404.

[3] L. Márton, K. M. Hangos, and A. Magyar, *Migration-connected networks of Lotka–Volterra and quasi-polynomial systems: modeling and decentralized control*, Nonlinear Dynamics (published online 2024; 2025 volume), https://doi.org/10.1007/s11071-024-10619-6.

[4] B. S. Goh, *Global Stability in Many-Species Systems*, American Naturalist 111 (1977), 135–143, https://doi.org/10.1086/283144.
