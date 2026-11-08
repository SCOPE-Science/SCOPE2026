# A harmonic-sign trichotomy and fourth-root flip at bipartite Huygens equilibria

## Finding
For an arbitrary finite connected weighted bipartite oscillator graph, adding a third harmonic to a repulsive sinusoidal interaction changes the direction and stability of the local period-doubling branch at the **exact universal parameter** \(\kappa=-1/27\). The branch is supercritical and attracting for \(\kappa>-1/27\), subcritical and a saddle for \(-1/3<\kappa<-1/27\), and at equality is attracting with a fourth-root rather than square-root amplitude law.

Let \(G=(V,E)\) be any connected simple bipartite graph with \(|V|\ge2\) and positive symmetric edge weights \(a_e\), with an arbitrarily oriented incidence column \(b_e\) for each edge. Define \(L=\sum_e a_e b_eb_e^T\). Let \(\Lambda=\lambda_{\max}(L)\) and fix any unit eigenvector \(v\in\mathbf1^\perp\) for \(\Lambda\). Define
\[
Q_4=\sum_e a_e(b_e^Tv)^4>0,\qquad Q_6=\sum_e a_e(b_e^Tv)^6>0.
\]
Set \(\alpha=1+3\kappa>0\), \(\beta=1+27\kappa\), \(h_*=2/(\alpha\Lambda)\), and \(\varepsilon=h-h_*\). There is a sufficiently small neighborhood of the bipartite phase-opposition equilibrium in which the symmetric nontrivial two-cycle, if present, consists of \(\theta^*+u\) and \(\theta^*-u\), modulo common phase, with the following precise alternatives:

1. **Positive cubic coefficient \(\beta>0\):** exactly one such pair for all sufficiently small \(\varepsilon>0\), none for sufficiently small \(\varepsilon<0\). It is an attracting two-cycle on the common-phase quotient. Writing \(u=sv+w\) with \(w\perp v,\mathbf1\), \(s>0\), one has \(w=O(s^3)\) and
\[
s^2=\frac{3\alpha^2\Lambda^2}{\beta Q_4}\varepsilon+O(\varepsilon^2).
\]
2. **Negative cubic coefficient \(\beta<0\), with \(\alpha>0\):** exactly one such pair for all sufficiently small \(\varepsilon<0\), none for sufficiently small \(\varepsilon>0\). The same expansion holds; its one critical direction is unstable, with all remaining non-neutral directions stable.
3. **Vanishing cubic coefficient \(\beta=0\), equivalently \(\kappa=-1/27\):** exactly one such pair for all sufficiently small \(\varepsilon>0\), none for sufficiently small \(\varepsilon<0\). It is attracting modulo common phase, \(w=O(s^5)\), and
\[
s^4=\frac{15\alpha^2\Lambda^2}{2Q_6}\varepsilon+O(\varepsilon^{3/2}).
\]
The nondegenerate critical one-step multiplier is \(-1+2\alpha\Lambda\varepsilon+O(\varepsilon^2)\); the degenerate critical multiplier is \(-1+4\alpha\Lambda\varepsilon+O(\varepsilon^{3/2})\). The other \(|V|-2\) non-neutral one-step multipliers tend to \(1-2\lambda_j/\Lambda\) with \(0<\lambda_j<\Lambda\). Thus every stated stability conclusion applies to the full phase quotient, not merely a special one-dimensional invariant set.

## Assumptions and scope
The phase variables lie in \((\mathbb R/2\pi\mathbb Z)^{|V|}\), and the discrete network map is
\[
(F_{h,\kappa}(\theta))_i=\theta_i+h\sum_{j:\{i,j\}\in E}a_{ij}\{\sin(\theta_i-\theta_j)+\kappa\sin[3(\theta_i-\theta_j)]\}\pmod{2\pi}.
\]
The graph is finite, connected, bipartite, with all edge weights strictly positive; \(\kappa>-1/3\), \(h>0\). The two-colour equilibrium \(\theta^*\) takes phase \(0\) on one class and \(\pi\) on the other. Small real lifts of perturbations lie in \(H=\{u:\mathbf1^Tu=0\}\), which models the quotient locally. Uniqueness means uniqueness of the nearby nonzero solutions of the symmetric half-return equation \(F(\theta^*+u)=\theta^*-u\) modulo identifying \(u\) with \(-u\); no global uniqueness of every two-cycle is claimed. Constants implicit in the asymptotics may depend on the fixed graph and \(\kappa\).

## Proof
**1. Simple critical mode.** Let \(S\) be diagonal, with entries \(+1\) and \(-1\) on the two bipartite classes. Then \(SLS=D+A_{\rm adj}\), the weighted signless Laplacian, a nonnegative irreducible symmetric matrix because the graph is connected. Perron–Frobenius implies that its largest eigenvalue \(\Lambda\) is simple and positive. The graph Laplacian has one simple zero eigenvalue and all its other eigenvalues are positive; hence every other eigenvalue on \(H\) is strictly below \(\Lambda\). Moreover, \(Q_4,Q_6>0\), since a top eigenvector cannot be constant along every edge of a connected graph.

**2. Exact odd local map.** Choosing the edge orientations arbitrarily and \(A=\operatorname{diag}(a_e)\), one has \(F(\theta^*+u)=\theta^*+G_h(u)\) near the equilibrium, where
\[
G_h(u)=u-hBA f_\kappa(B^Tu),\qquad f_\kappa(t)=\sin t+\kappa\sin(3t).
\]
The function \(G_h\) is odd and preserves \(H\). Consequently \(G_h(u)=-u\) produces a genuine symmetric prime-two orbit for every \(u\ne0\) small. Its equation is
\[
\mathcal E(u,h):=BA f_\kappa(B^Tu)-\frac2h u=0.
\]
Because
\[
f_\kappa(t)=\alpha t-\frac\beta6t^3+\frac\gamma{120}t^5+O(t^7),\quad \gamma=1+243\kappa,
\]
the equation becomes
\[
(\alpha L-2h^{-1}I)u-\frac\beta6BA(B^Tu)^{\circ3}+\frac\gamma{120}BA(B^Tu)^{\circ5}+O(\|u\|^7)=0.
\]
At \(h=h_*\), the linear operator has exactly the one-dimensional kernel \(\operatorname{span}(v)\) within \(H\).

**3. Lyapunov–Schmidt reduction.** Write \(u=sv+w\), \(w\in H\cap v^\perp\). The transverse derivative is invertible at \((s,h)=(0,h_*)\), so the analytic implicit-function theorem gives a unique odd analytic \(w=w(s,h)\), with \(w=O(s^3)\) for \(\beta\ne0\). If \(\beta=0\), the cubic term vanishes in every coordinate, improving this to \(w=O(s^5)\). Projecting \(\mathcal E=0\) onto \(v\) and dividing by \(s\ne0\) yields, if \(\beta\ne0\),
\[
0=\alpha\Lambda-\frac2h-\frac{\beta Q_4}{6}s^2+O(s^4).
\]
Since \(\alpha\Lambda-2/h=\alpha^2\Lambda^2\varepsilon/2+O(\varepsilon^2)\), the implicit-function theorem in \(s^2\) gives precisely the two stated signs, one positive \(s^2\) root on the appropriate side, and the square-root asymptotics. At \(\beta=0\), one has \(\gamma=1+243(-1/27)=-8\), and the reduced equation is
\[
0=\alpha\Lambda-\frac2h-\frac{Q_6}{15}s^4+O(s^6).
\]
It has exactly one small positive value of \(s^2\) for \(\varepsilon>0\) and none for \(\varepsilon<0\); solving for \(s^4\) gives the fourth-root formula with \(O(\varepsilon^{3/2})\) remainder.

**4. All transverse multipliers.** At both points \(\pm u\), the Jacobian is the same real symmetric matrix,
\[
DG_h(u)=I-hBA\,\operatorname{diag}\bigl(f_\kappa'(B^Tu)\bigr)B^T,
\]
because \(f_\kappa'\) is even. For \(\beta\ne0\), the critical Rayleigh expansion is
\[
1-h\alpha\Lambda+\frac{h\beta Q_4}{2}s^2+O(\varepsilon^2)=-1+2\alpha\Lambda\varepsilon+O(\varepsilon^2).
\]
For \(\beta=0\), using \(f_\kappa'(t)=\alpha+\gamma t^4/24+O(t^6)\) instead gives
\[
1-h\alpha\Lambda-\frac{h\gamma Q_6}{24}s^4+O(\varepsilon^{3/2})=-1+4\alpha\Lambda\varepsilon+O(\varepsilon^{3/2}).
\]
The other mean-zero eigenvalues converge to \(1-2\lambda_j/\Lambda\in(-1,1)\) by step 1. The single critical eigenvalue lies inside the unit circle in either supercritical case and below \(-1\) in the subcritical case, while the others remain stable. The two-step return Jacobian is the square of the one-step Jacobian. This proves sink or one-unstable-direction saddle classification. The neutral common-phase multiplier is \(1\) and is deliberately removed by quotienting. \(\square\)

## Verification
The standalone file `verify_two_harmonic.py` evaluates the antisymmetric half-return equation, computes eigenvalues of the full Jacobian, and tests the square-root and fourth-root amplitude laws on an edge, a nonuniformly weighted path, and a nonuniformly weighted star, in all three regimes. Running `python verify_two_harmonic.py` with NumPy and SciPy printed `VERIFY_OK graphs=3 regimes=3 checks=72`. The analytic proof above, not those finite tests, establishes the claim for arbitrary graphs and real parameters.

## Relationship to prior work
Buescu–D'Aniello–Oliveira (2026) introduces the general odd periodic network interaction and rigorous Lyapunov and Morse–Smale results, including the sinusoidal case; its results concern the small-step regime, not this harmonic-dependent local period-doubling trichotomy. Buescu–Oliveira (2026) treats phase-locking in nearest-neighbor rings in the descent regime, not higher-harmonic flip degeneracy. Hénot–Lessard (2026) describes generic map period-doubling conditions and computes nonzero cubic coefficients for a different model; its generic normal form does not evaluate the sign-change threshold or the fifth-order coefficient for these bipartite graph networks. The present calculation is a model-specific, all-graph coefficient evaluation and exact fourth-root bifurcation boundary; it does not claim originality of Lyapunov–Schmidt reduction or the generic theory of flip bifurcations.

## Limitations
The theorem is local in phase and coupling and applies only to common first-plus-third harmonic interactions on finite, connected, positively weighted bipartite graphs. It classifies **symmetric** two-cycles near phase opposition, without asserting there are no distant or nonsymmetric cycles, global attraction, or a global bifurcation diagram. The case \(\kappa\le-1/3\) is excluded. The normal-form asymptotics are at fixed \(\kappa\), not uniform in a joint \((h,\kappa)\) blow-up. Historical priority relative to specialized earlier high-harmonic maps is not independently established.

## References
1. J. Buescu, E. D'Aniello, H. M. Oliveira, *Morse–Smale dynamics in discrete Huygens networks*, arXiv:2610.10993v1, first posted 2026-10-07, https://arxiv.org/abs/2610.10993.
2. J. Buescu, H. M. Oliveira, *Almost-global convergence to twisted states in discrete Huygens rings*, arXiv:2610.19953v1, first posted 2026-10-14, https://arxiv.org/abs/2610.19953.
3. O. Hénot, J.-P. Lessard, *Rigorous verification of period-doubling bifurcations in maps*, arXiv:2610.22986v1, first posted 2026-10-16, https://arxiv.org/abs/2610.22986.
