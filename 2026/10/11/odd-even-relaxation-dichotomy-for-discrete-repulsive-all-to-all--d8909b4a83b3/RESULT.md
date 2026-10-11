# Odd-even relaxation dichotomy for discrete repulsive all-to-all phase networks

## Finding
Consider identical phase oscillators with complete repulsive sinusoidal coupling, updated once per time step. For every odd network size, a uniform order-parameter neighborhood of the balanced manifold has an explicit exponential attraction bound. For every even network size, the same neighborhood contains nonstationary invariant trajectories with algebraic, logarithmically corrected relaxation. The discrete-step logarithmic coefficient cancels at the admissible step \(h=1/6\) only in the four-node case.

**Theorem.** For every integer \(N\ge3\) and real \(0<h<1/N\), let
\[
\theta_{i,n+1}=\theta_{i,n}+h\sum_{j\ne i}\sin(\theta_{i,n}-\theta_{j,n})\pmod{2\pi},\qquad
Z(\theta)=\sum_{j=1}^{N}e^{i\theta_j}.
\]
When \(N\) is odd, any initial state with \(|Z(\theta_0)|\le 1/2\) satisfies, for every integer \(n\ge0\),
\[
|Z(\theta_n)|\le (1-h/4)^n |Z(\theta_0)|.
\]
Every coordinate has a compatible unwrapped real sequence converging to a phase \(\widetilde\theta_{i,\infty}\). Its remaining displacement satisfies
\[
|\widetilde\theta_{i,\infty}-\widetilde\theta_{i,n}|\le 4|Z(\theta_n)|.
\]
In particular, the limit is balanced: \(Z(\theta_\infty)=0\).

When \(N=2m\ge4\) is even, the one-parameter family
\[
\theta(u)=(u,-u,\underbrace{0,\ldots,0}_{m-2},\underbrace{\pi,\ldots,\pi}_{m}),\quad 0<u<\pi,
\]
is invariant, with exact scalar map
\[
u_{n+1}=u_n-2h\sin u_n(1-\cos u_n).
\]
For every initial \(0<u_0<\pi\), its iterates tend strictly downward to zero, and there is a finite real constant \(C=C(h,u_0)\) such that
\[
\frac1{u_n^2}=2hn+\left(\frac{3h}{2}-\frac14\right)\log n+C+o(1),\quad n\to\infty.
\]
Consequently \(u_n\sim(2hn)^{-1/2}\) and \(|Z(\theta(u_n))|\sim(2hn)^{-1}\). This excludes a uniform exponential estimate \(|Z(\theta_n)|\le C_0q^n|Z(\theta_0)|\), with fixed finite \(C_0\) and \(q<1\), throughout any positive-radius neighborhood \(|Z|<\varepsilon\) of the balanced set for even sizes.

## Assumptions and scope
The phase space is the \(N\)-torus, and the interaction is homogeneous, symmetric, undelayed and **repulsive**. The result covers every integer \(N\ge3\), every step \(0<h<1/N\), and all initial states in the specified odd-size order-parameter sublevel set. For even sizes, the asymptotic is proved for the displayed exact invariant family, not for all initial data. All phase convergence claims use continuous real lifts of each discrete orbit, not a globally fixed branch of angle.

The normalized squared order-parameter potential is \(V(\theta)=|Z(\theta)|^2/2\), differing by a constant from the sum of pairwise cosines. The balanced set is exactly \(Z^{-1}(0)\). The primary MSC2020 classification of this discrete dynamical theorem is \(37C05\).

## Proof
**1. Gradient identity and Gram matrix.** Write \(z=(\Re Z,\Im Z)\in\mathbb R^2\). The real Jacobian \(J=D_\theta z\in\mathbb R^{2\times N}\) has columns \(j_i=(-\sin\theta_i,\cos\theta_i)^\top\), hence \(\nabla V=J^\top z\). The stated update is exactly \(\theta^+=\theta-hJ^\top z\). Set \(G=JJ^\top\); its spectrum is contained in \([0,N]\) because each column has norm one and \(\operatorname{tr}G=N\).

**2. A parity Gram inequality.** Suppose \(N\) is odd. For an arbitrary unit direction \(v\in\mathbb R^2\), rotate the phases so that \(v\cdot j_i=\sin\varphi_i\), and let \(x_i=\cos\varphi_i\), \(y_i=\sin\varphi_i\). Select \(s_i\in\{-1,+1\}\) with \(|s_i-x_i|=1-|x_i|\). Oddness implies \(|\sum_i s_i|\ge1\). Therefore
\[
1\le\left|\sum_i s_i\right|\le\left|\sum_i x_i\right|+\sum_i(1-|x_i|)
\le |Z|+\sum_i y_i^2.
\]
It follows for every unit \(v\) that \(v^\top Gv=\sum_i(v\cdot j_i)^2\ge1-|Z|\), so
\[
\lambda_{\min}(G)\ge 1-|Z|.
\]
This bound is uniform across all odd sizes. The underlying odd/even smooth-versus-singular geometry of balanced configurations is known from the Kuramoto equilibrium literature; the explicit quantitative inequality and discrete-time consequences are the assertions used here.

**3. Odd-size contraction.** Each phase increment satisfies \(|\Delta\theta_i|=h|j_i\cdot z|\le h|z|\). By the elementary complex exponential remainder \(|e^{it}-1-it|\le t^2/2\), the next order parameter obeys
\[
z^+=(I_2-hG)z+R,\qquad |R|\le\tfrac12\sum_i|\Delta\theta_i|^2\le\tfrac12 Nh^2|z|^2.
\]
For \(|z|\le 1/2\), the spectrum of \(I_2-hG\) lies in \([1-hN,\ 1-h(1-|z|)]\subset[0,1]\). Thus
\[
|z^+|\le\left(1-h(1-|z|)+\tfrac12 Nh^2|z|\right)|z|
\le\left(1-\tfrac h2+\tfrac14 Nh^2\right)|z|
\le (1-h/4)|z|.
\]
Iteration preserves \(|Z|\le1/2\) and yields the asserted contraction. For any coordinate the sum of future real increments is absolutely bounded by
\[
\sum_{k=n}^{\infty}|\Delta\theta_{i,k}|\le h\sum_{k=n}^{\infty}|Z(\theta_k)|
\le \frac{h}{1-(1-h/4)}|Z(\theta_n)|=4|Z(\theta_n)|.
\]
The limits therefore exist and have vanishing order parameter.

**4. Exact even-size invariant arc.** For \(N=2m\ge4\), pair the two phase values \(+u\) and \(-u\), put \(m-2\) remaining oscillators at zero and \(m\) at \(\pi\). At every zero or \(\pi\) coordinate, the contributions from \(+u\) and \(-u\) cancel; the remaining two coordinates move by opposite amounts. Direct substitution gives the exact scalar law
\[
u^+=u-2h\sin u(1-\cos u),\qquad Z(\theta(u))=2(\cos u-1).
\]
For \(0<u<\pi\), positivity of \(\sin u\) gives \(u^+<u\), and
\[
0< 2h\sin u(1-\cos u)<4hu\le u
\]
because \(4h<4/N\le1\). Thus \(0<u^+<u\), and its limit must be zero (there are no interior fixed points).

**5. Logarithmically corrected inverse-square law.** Taylor expansion at zero, with remainder controlled on a sufficiently small interval, yields
\[
u^+=u-hu^3+\frac h4u^5+O_h(u^7).
\]
For \(y_n=u_n^{-2}\), this implies
\[
y_{n+1}-y_n=2h+\frac{3h^2-h/2}{y_n}+O_h(y_n^{-2}).
\]
Since \(u_n\downarrow0\), first \(y_{n+1}-y_n\to2h\), hence \(y_n\sim2hn\); the displayed recurrence then gives \(y_n=2hn+O_h(\log n)\). Consequently
\[
\frac1{y_n}-\frac1{2hn}=O_h\!\left(\frac{\log n}{n^2}\right),\qquad y_n^{-2}=O_h(n^{-2}),
\]
which are summable. Subtracting \(2hn+[(3h^2-h/2)/(2h)]\log n\) and telescoping shows convergence to a finite constant because \(\log(n+1)-\log n=1/n+O(n^{-2})\). The stated asymptotic follows. Finally \(|Z|=2(1-\cos u)\sim u^2\), proving the algebraic order-parameter law. For \(0<h<1/N\), the logarithmic coefficient vanishes when \(h=1/6\), admissible only for \(N=4\).

## Verification
Run the included standalone Python 3 standard-library program `verify.py`: it deterministically checks the exact invariant family against the full \(N\)-body map, the even-family order parameter, one-step odd contractions in tested cases, coordinate step bounds, strict scalar monotonicity, and stabilization of finite-cutoff asymptotic residuals. It prints `VERIFY_OK; deterministic assertions: 2864`. These numerical tests are finite diagnostics, not the universal proof. The universal proof is the parity Gram inequality and scalar asymptotic analysis given above.

## Relationship to prior work
Buescu and Oliveira (arXiv:2503.13230v1, first submitted 17 March 2025), Section 2.1 Eq. (4), analyze an exactly compatible three-clock all-to-all discrete sine interaction in phase-difference coordinates and show Morse–Smale sinks at three-clock staggered phases. Their scope is the three-clock diffeomorphism and perturbations; it does not include this arbitrary-size odd/even quantitative dichotomy or even-size critical slowing.

Sclosa (arXiv:2207.08182, particularly its discussion of balanced configurations and their singularities) cites and develops prior geometry: for odd cardinality the balanced configurations have no fully two-cluster collinear singular points, whereas even cardinality allows singular balanced configurations. That geometric observation is prior work and **not** asserted to be new. Here the new claim concerns the concrete all-size finite-step contraction estimate, a specified invariant slow orbit, its exact logarithmic second term, and the failure of any uniform geometric order-parameter attraction in even networks.

Kalmár-Nagy, Horváth and Vincze (2025, DOI 10.1142/S0218127425300320) study small fully coupled discrete-time Kuramoto oscillators. Their accessible abstract/preview emphasizes two- and three-oscillator bifurcations; the complete article could not be materially read, and an unseen equivalent result is a residual priority risk. The full material examined from the named 2025 preprint, including its model, main theorems and conclusions, did not imply the present all-size parity-rate theorem.

## Limitations
No claim is made about global attraction outside the odd-size \(|Z|\le1/2\) sublevel set, convergence rates for all even-size initial conditions, nonlinear perturbations or non-complete graphs. Algebraic relaxation occurs along an explicitly specified invariant family, not generically at every balanced state. The rate estimates depend on the exact full-step map and \(0<h<1/N\). The coefficient cancellation at \(h=1/6\) is meaningful only for the even four-node admissible case. Independent audit has not been performed. Earlier equivalent statements may exist in specialized discrete Kuramoto literature, including full text not available for one closely related article.

## References
1. J. Buescu and H. M. Oliveira, *Lyapunov functions for Morse-Smale synchronisation diffeomorphisms*, arXiv:2503.13230v1 (first public 2025-03-17), https://arxiv.org/html/2503.13230v1.
2. D. Sclosa, *Kuramoto Networks with Infinitely Many Stable Equilibria*, arXiv:2207.08182v1 (2022), https://arxiv.org/abs/2207.08182.
3. T. Kalmár-Nagy, D. A. Horváth, and B. Vincze, *Synchronization in Small, Fully Coupled Systems of Discrete-Time Kuramoto Oscillators*, International Journal of Bifurcation and Chaos (2025), DOI:10.1142/S0218127425300320 (partly accessible).
