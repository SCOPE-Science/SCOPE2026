# Sharp high-coordinate transfer and self-similar resonances on a dyadic infinite hypercube

## Finding

For the bounded dyadically weighted adjacency Hamiltonian on the countable Boolean hypercube, starting from the empty vertex, the probability of arriving at the single-coordinate vertex \(\{m\}\) has the exact formula

\[
P_m(t)=\left(\frac{\sin t}{t}\right)^2\tan^2\!\left(\frac{t}{2^{m+1}}\right),\qquad m\in\mathbb N_0,\ t\in\mathbb R,
\]

interpreted by continuous extension at removable singularities. The resonant time \(t_m=\pi 2^m\) has exactly

\[
P_m(t_m)=\frac4{\pi^2}.
\]

At this time the measured vertex consists of the certainly present coordinate \(m\), no coordinates below \(m\), and an independent, translated random upper tail: for every \(j\geq1\), the coordinate \(m+j\) is present with probability \(\sin^2(\pi/2^{j+1})\). This law is independent of \(m\) after translating the indices.

Let \(M_m=\sup_{t\geq0}P_m(t)\). For all sufficiently large integers \(m\), there is a unique maximizing positive time \(t_m^*\), with the sharp expansions

\[
\begin{aligned}
t_m^*&=\pi2^m-\frac{3}{\pi2^m}+O(2^{-3m}),\\
M_m&=\frac4{\pi^2}\left(1+\frac3{\pi^2 4^m}+O(16^{-m})\right).
\end{aligned}
\]

In particular, \(M_m\to4/\pi^2\); the exact resonant fidelity is not the exact finite-index optimum, because \(M_m>4/\pi^2\) for every \(m\). For each finite \(m\), \(M_m<1\), so no single coordinate is a perfect-transfer target.

## Assumptions and scope

Let \(\Gamma\) be the set of finite subsets of \(\mathbb N_0=\{0,1,\ldots\}\), and work in \(\mathcal H=\ell^2(\Gamma)\), with orthonormal basis \(\delta_\sigma\). For every \(k\geq0\), let the commuting unitary involution \(X_k\) act by \(X_k\delta_\sigma=\delta_{\sigma\triangle\{k\}}\). Define the norm-convergent self-adjoint operator and continuous-time propagator by

\[
A=\sum_{k=0}^{\infty}2^{-(k+1)}X_k,\qquad U(t)=e^{-itA}.
\]

The initial vector is precisely \(\delta_\varnothing\); the target is \(\delta_{\{m\}}\), and \(P_m(t)=|\langle\delta_{\{m\}},U(t)\delta_\varnothing\rangle|^2\). All probabilities are computational-basis measurements at a *fixed time*, not first-passage probabilities. The only weight sequence asserted here is \(2^{-(k+1)}\), not general summable weights. The asymptotic regime is \(m\to\infty\) with no additional scaling parameter.

## Proof

**Product law.** The operators \(X_k\) commute and satisfy \(X_k^2=I\). Their weighted sum is norm-convergent, so for each fixed real \(t\), the finite products

\[
U_N(t)=\prod_{k=0}^{N}\left[\cos\!\left(\frac{t}{2^{k+1}}\right)I-i\sin\!\left(\frac{t}{2^{k+1}}\right)X_k\right]
\]

converge in operator norm to \(U(t)\). For any fixed finite subset \(\sigma\), expansion of the product gives

\[
|\langle\delta_\sigma,U(t)\delta_\varnothing\rangle|^2=
\prod_{k\in\sigma}\sin^2\!\left(\frac{t}{2^{k+1}}\right)
\prod_{k\notin\sigma}\cos^2\!\left(\frac{t}{2^{k+1}}\right).
\]

Indeed, the finite products give independent Bernoulli coordinate occupations. They remain supported on finite subsets in the limit, since \(\sum_k\sin^2(t/2^{k+1})<\infty\). The classical Viète product \(\prod_{k=0}^\infty\cos(t/2^{k+1})=\sin(t)/t\), including its continuous extensions, proves the displayed singleton formula. At its poles the unsimplified product defines the exact value.

**Dyadic resonance.** At \(t_m=\pi2^m\), the angles for \(k<m\) are integral multiples of \(\pi\), the angle at \(k=m\) is \(\pi/2\), and the angle at \(k=m+j\) is \(\pi/2^{j+1}\). Hence the claimed translation-invariant tail is exact. Its empty-tail probability is

\[
\prod_{j=1}^\infty\cos^2\!\left(\frac\pi{2^{j+1}}\right)=\left(\frac2\pi\right)^2
\]

by Viète's identity at \(\pi/2\). This is precisely the singleton probability at resonance.

**Global localization of the optimum.** Put \(h=2^{-m}\) and \(y=ht/2\). The product law can alternatively be written

\[
P_m(t)=F_m(y),\qquad F_m(y)=\frac{\sin^4y}{y^2}\prod_{j=1}^{m}\cos^2(2^jy),\quad y>0.
\]

For \(y\geq2\), \(F_m(y)\leq y^{-2}\leq1/4<4/\pi^2\). For small \(y\), \(F_m(y)\leq y^2\). On any closed subset of \((0,2]\) excluding \(\pi/2\), use the finite duplication identity

\[
\prod_{j=1}^{m}\cos(2^jy)=\frac{\sin(2^{m+1}y)}{2^m\sin(2y)}
\]

to obtain \(F_m(y)=O(4^{-m})\) uniformly. The only zero of \(\sin(2y)\) in \((0,2]\) besides the removed origin is \(\pi/2\). Since \(F_m(\pi/2)=4/\pi^2\), any global maximizer \(y_m\) satisfies \(y_m\to\pi/2\). A global maximum exists for each \(m\), since \(F_m\) is continuous, tends to zero at both endpoints \(y=0\) and \(y=+\infty\), and is positive somewhere.

Write the corresponding physical time as \(t=\pi/h+\delta\). The exact local identity is

\[
P_m(\pi/h+\delta)=\frac4{(\pi+h\delta)^2}
\left(\frac{\sin\delta}{\delta}\right)^2
\left[\frac{h\delta}{2}\cot\!\left(\frac{h\delta}{2}\right)\right]^2,
\]

with the continuous value \(4/\pi^2\) at \(\delta=0\). Every global maximizing \(\delta_m\) is bounded: if \(h\delta_m\to0\), the last bracket is bounded and \(\pi+h\delta_m\to\pi\), while an unbounded \(|\delta_m|\) forces the displayed probability to zero. Any finite limit \(\delta\) of such maximizers must satisfy \((\sin\delta/\delta)^2\geq1\), because the maximum is at least \(4/\pi^2\); the only possibility is \(\delta=0\). Thus \(\delta_m\to0\) for every selection of global maximizers.

**Unique optimizer and correction.** In a fixed sufficiently small neighborhood of \(\delta=0\), the logarithm of the preceding expression is real analytic in \((h,\delta)\), and has the expansion

\[
\log\frac{P_m(\pi/h+\delta)}{4/\pi^2}=-\frac{2h\delta}{\pi}-\frac{\delta^2}{3}
+O(h^2\delta^2+|h\delta|^3+\delta^4).
\]

Its second derivative with respect to \(\delta\) tends uniformly to \(-2/3\) as \(h,\delta\to0\), so the logarithm is strictly concave there. All global maxima eventually lie in this neighborhood; hence the global maximum is unique for sufficiently large \(m\). The stationarity equation and the analytic implicit-function theorem yield

\[
\delta_m=-\frac{3h}{\pi}+O(h^3).
\]

(The branch is odd in \(h\), by simultaneous sign reversal of \((h,\delta)\).) Substituting gives

\[
\log\frac{M_m}{4/\pi^2}=\frac{3h^2}{\pi^2}+O(h^4),
\]

which proves both stated expansions. Moreover, differentiating the exact local identity at \(\delta=0\) gives \(\partial_\delta\log P_m=-2h/\pi<0\), so a slightly *earlier* time strictly improves upon the resonant value for each finite \(m\).

Finally, \(P_m(t)=1\) would force every upper-coordinate Bernoulli probability to vanish. In particular, \(\sin(t/2^{k+1})=0\) for all \(k>m\), which implies \(t=0\). But \(P_m(0)=0\). Since a global maximizer is attained, \(M_m<1\) for each fixed \(m\).

## Verification

The standalone file `verify_transfer.py` uses only Python's standard library. Run `python3 verify_transfer.py`. It compares independently calculated finite-dimensional Walsh-character spectral sums against coordinate-product amplitudes; checks the dyadic tail and its explicit truncation-error estimate; verifies translated packet marginals; and tests the two optimization asymptotics numerically. The program reports 142 passing finite computational cross-checks in a reference execution. These checks corroborate formulas, while the proof of uniqueness and the all-index asymptotic limit is analytic and does not rely on finite enumeration.

## Relationship to prior work

Wang [1] introduced the countable locally infinite graph Hamiltonian \(A_w\), characterized its spectrum and time reversal, and explicitly identified the ideal weight \(w(k)=2^{-(k+1)}\) in Remark 3.1. The construction and its involutions are prior facts, not new claims here. The present finding addresses its as-yet-unquantified *site-specific, time-optimized transport*: an exact self-similar resonant distribution and a globally optimized high-coordinate fidelity law.

Wang [2] studied an earlier **finite equal-weight** Bernoulli-functional walk that exhibits perfect antipodal transfer; those finite subspace and uniform coupling hypotheses do not imply the dyadic, countably infinite singleton result. Coutinho, Guo and Schmeits [3] established finite-graph peak-state-transfer methods and examples, including weighted paths. Their finite weighted paths, transfer targets, and limiting probability differ from the present infinite cubelike graph. General commuting-involution tensor factorizations are elementary antecedents; the nontrivial new portion is the *global* maximization and its sharp scaling, together with the exact translated infinite tail.

## Limitations

This result is specific to the empty initial vertex, singleton targets, the exactly geometric positive weights, and exact unitary evolution. It does not prove a robustness or perturbation theorem, optimal multivertex transfer, or an analogous law for arbitrary summable weights. The optimizer expansion holds as the target coordinate tends to infinity; uniqueness is asserted only for sufficiently large coordinate indices. General finite-graph transfer theory could subsume structural portions of the calculation, and literature-wide priority has not been independently established.

## References

[1] C. Wang, *Continuous-Time Quantum Walk on Locally Infinite Graph*, arXiv:2602.23970v1 (first public 2026-02-27), Sections 2--4 and Remark 3.1. https://arxiv.org/html/2602.23970v1

[2] C. Wang, *Abstract Model of Continuous-Time Quantum Walk Based on Bernoulli Functionals and Perfect State Transfer*, arXiv:2212.00020 (first public 2022-11-30), Sections 3.1--3.4. https://arxiv.org/abs/2212.00020

[3] G. Coutinho, K. Guo, V. Schmeits, *Peak state transfer in continuous quantum walks*, arXiv:2505.11986 (first public 2025-05-17), Sections 3--6. https://arxiv.org/html/2505.11986v2
