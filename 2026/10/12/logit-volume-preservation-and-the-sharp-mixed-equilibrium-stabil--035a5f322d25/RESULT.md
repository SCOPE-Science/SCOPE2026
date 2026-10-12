# Logit-volume preservation and the sharp mixed-equilibrium stability boundary
## Finding
Consider the directed-cycle binary game with players indexed modulo \(N\ge 2\), where player \(i\)'s payoff difference between actions \(1\) and \(0\) is the affine function \(\Delta_i(p_{i-1})\). Assume the robust no-dominance regime \(\Delta_i(0)\Delta_i(1)<0\) for every \(i\). The source proves that there is a unique fully mixed Nash equilibrium \(q\), with
\[
q_i=rac{\Delta_{i+1}(0)}{\Delta_{i+1}(0)-\Delta_{i+1}(1)}\in(0,1).
\]
Under the standard multi-population replicator dynamics
\[
\dot p_i=p_i(1-p_i)\Delta_i(p_{i-1}),
\]
the interior flow preserves Lebesgue volume in logit coordinates \(x_i=\log(p_i/(1-p_i))\), even though the game need not be zero-sum.

Let \(b_i=\Delta_i(1)-\Delta_i(0)\), \(a_i=q_i(1-q_i)b_i\), \(P=\prod_{i=1}^N a_i\), and let \(\kappa\) be the number of inverters, namely players with \(\Delta_i(0)>0>\Delta_i(1)\). The Jacobian at \(q\) has characteristic polynomial
\[
\chi(\lambda)=\lambda^N-P,
\qquad
\operatorname{sgn}P=(-1)^\kappa.
\]
The exact number of eigenvalues with positive real part, counted with algebraic multiplicity, is
\[
u_+(N,\kappa)=
egin{cases}
2\left\lfloor\dfrac{N-1}4ightfloor+1,&\kappa\ 	ext{even},\[4pt]
2\left\lfloor\dfrac{N+1}4ightfloor,&\kappa\ 	ext{odd}.
\end{cases}
\]
Consequently the mixed equilibrium is linearly unstable for every even \(\kappa\), and for every odd \(\kappa\) when \(N\ge3\). The unique exceptional robust no-dominance case is \(N=2\) with odd \(\kappa\): the mixed equilibrium is a nonlinear Lyapunov-stable center, not an asymptotically stable state. In that case every nonstationary interior trajectory is periodic.

When \(\kappa\) is even, the source's two pure Nash equilibria are strict. Under the same replicator dynamics both are hyperbolic sinks.
## Assumptions and scope
The claim concerns exactly the source's robust no-dominance directed cycle, with \(N\ge2\), binary actions, affine local marginal incentives, and the standard continuous-time multi-population replicator equation. It does not assert that the source itself adopted replicator dynamics. It does not cover non-robust boundary-indifference cases, discrete learning rules, best-response dynamics, logit dynamics, mutation, noise, or delays.

The volume statement is for the open cube \((0,1)^N\) after the smooth logit change of coordinates; it does not say Euclidean volume in the original \(p\)-coordinates is preserved. The global periodicity statement is only for the exceptional two-player odd-inverter-parity case.
## Proof
For \(p_i\in(0,1)\), set \(x_i=\log(p_i/(1-p_i))\). Since \(\dot x_i=\dot p_i/[p_i(1-p_i)]\),
\[
\dot x_i=\Delta_i(p_{i-1}).
\]
The right-hand side depends on \(x_{i-1}\) through \(p_{i-1}=(1+e^{-x_{i-1}})^-1\), but not on \(x_i\). Hence
\[
\operatorname{div}_x\dot x=
\sum_{i=1}^Nrac{\partial\dot x_i}{\partial x_i}=0.
\]
Liouville's formula therefore gives exact preservation of logit-coordinate volume for every finite flow segment staying in the interior.

At the fully mixed equilibrium, \(\Delta_i(q_{i-1})=0\). Because \(\Delta_i\) is affine,
\[
\Delta_i(p_{i-1})=b_i(p_{i-1}-q_{i-1}).
\]
Differentiating the replicator vector field at \(q\), the only nonzero entry in row \(i\) is
\[
J_{i,i-1}=q_i(1-q_i)b_i=a_i,
\]
with indices modulo \(N\). Thus \(J\) is a weighted cyclic shift and
\[
J^N=P I.
\]
All \(a_i
e0\), so \(J\) is nonsingular and its characteristic polynomial is \(\lambda^N-P\). A conformist has \(b_i>0\), while an inverter has \(b_i<0\); therefore \(\operatorname{sgn}P=(-1)^\kappa\).

If \(P>0\), the eigenvalues are \(|P|^{1/N}e^{2\pi i k/N}\). Counting the roots whose cosine is positive gives \(2\lfloor(N-1)/4floor+1\). If \(P<0\), the eigenvalues are \(|P|^{1/N}e^{(2k+1)\pi i/N}\), and the positive-real-part count is \(2\lfloor(N+1)/4floor\). This is positive for odd \(\kappa\) whenever \(N\ge3\), but is zero for \(N=2\). For \(N=2\) and odd \(\kappa\), the linear eigenvalues are the purely imaginary pair \(\pm i\sqrt{|P|}\).

The nonlinear two-player case has more structure. Write
\[
\dot p_1=b_1p_1(1-p_1)(p_2-q_2),
\qquad
\dot p_2=b_2p_2(1-p_2)(p_1-q_1),
\]
where \(b_1b_2<0\). Define
\[
F_q(p)=-q\log p-(1-q)\log(1-p).
\]
Then \(F_q'(p)=(p-q)/[p(1-p)]\), and hence
\[
rac{d}{dt}F_{q_1}(p_1)=b_1(p_1-q_1)(p_2-q_2),
\qquad
rac{d}{dt}F_{q_2}(p_2)=b_2(p_1-q_1)(p_2-q_2).
\]
Therefore
\[
K=|b_2|F_{q_1}(p_1)+|b_1|F_{q_2}(p_2)
\]
is conserved. Each \(F_q\) is strictly convex, has its unique minimum at \(p=q\), and diverges at both endpoints. Thus \(K\) has a strict interior minimum at \(q\); every nonminimal level set is a compact smooth simple closed curve. The mixed equilibrium is the only interior rest point, so the vector field has no zero on such a level curve. The flow on each level curve is therefore periodic. This proves Lyapunov stability, non-asymptotic stability, and the center statement.

Finally, at a pure profile \(s\), the coupling derivatives vanish because \(p_i(1-p_i)=0\). The Jacobian is diagonal with entry \(\Delta_i(s_{i-1})\) when \(s_i=0\) and \(-\Delta_i(s_{i-1})\) when \(s_i=1\). At a strict pure Nash equilibrium these quantities are all negative. The two pure equilibria in the robust even-parity regime are strict, so both are hyperbolic sinks.
## Verification
The bundled script `artifacts/verify.py` checks with exact rational arithmetic that a weighted cyclic Jacobian satisfies \(J^N=(\prod_i a_i)I\) for dimensions \(2\) through \(20\), verifies the two positive-real-part root-count formulas through dimension \(40\), and checks exact cancellation in the derivative of the two-player conserved quantity. It was executed from the packaged path and returned `VERIFY_OK`.

These finite checks are regression checks for the algebra; the proof above is the infinite-dimensional-in-\(N\) argument. No numerical experiment is used as a substitute for the theorem.
## Relationship to prior work
Sánchez-Sáez, Odishelidze and Criado-Aldeanueva derive the source class's static Nash-equilibrium taxonomy: in the robust no-dominance regime there is a unique fully mixed equilibrium for every parity, and even inverter parity also gives two pure equilibria. Their full text contains no replicator equation. Their table labels the even-parity pure equilibria as attractors and the mixed equilibrium as unstable, but does not supply a dynamical system establishing those labels.

Boone and Piliouras prove volume-conservation and recurrence results for zero-sum evolutionary and graphical polymatrix games. Geiger, Knebel and Frey study antisymmetric zero-sum replicator systems and network topology. Those results require zero-sum/antisymmetric structure and do not imply the present divergence identity for arbitrary unidirectional binary cycles, nor the exact characteristic polynomial and inverter-parity unstable-dimension formula. The two-population two-strategy center phenomenon is classical; it is not claimed here as a standalone novelty. The new point is the exact source-specific dynamical classification, including volume preservation without a zero-sum assumption and the sharp \(N=2\), odd-\(\kappa\) center exception.
## Limitations
For \(N\ge3\), linear instability of the mixed equilibrium does not by itself classify all global limit sets or exclude lower-dimensional stable manifolds. Volume preservation in logit coordinates precludes an asymptotically stable interior equilibrium but does not determine boundary behavior. The result does not cover the source's non-robust regimes, and it makes no claim about stochastic, discrete-time, or perturbed learning dynamics.
## References
1. J.-M. Sánchez-Sáez, N. Odishelidze, F. Criado-Aldeanueva, “N-Player Binary Games with Unidirectional Dependencies: Cycle Stability and Induced Indifference,” arXiv:2606.06625v1, first public 2026-06-04; related DOI 10.1016/j.cnsns.2026.110151.
2. V. Boone, G. Piliouras, “From Darwin to Poincaré and von Neumann: Recurrence and Cycles in Evolutionary and Algorithmic Game Theory,” arXiv:1910.01334.
3. P. M. Geiger, J. Knebel, E. Frey, “Topologically robust zero-sum games and Pfaffian orientation,” arXiv:1806.07339; Physical Review E 98, 062316 (2018), DOI 10.1103/PhysRevE.98.062316.
