# Noise-blind moment stability fails in a stochastic agri-food evolutionary game
## Finding
Wen and Mo's stochastic tripartite evolutionary game is
\[
dx=A(y,z)x\,dt+\sigma x\,dW,
\]
\[
dy=B(x,z)y\,dt+\sigma y\,dW,
\]
\[
dz=C(x,y)z\,dt+\sigma z\,dW,
\]
with one common Brownian motion \(W\), where
\[
A(y,z)=\beta Q\Delta P+y(\theta-1)\beta Q\Delta P+z(S_g+F)+C_l-C_g,
\]
\[
B(x,z)=(\theta-1)\beta Q\!\left[x(P_{dg}-P_l-\Delta P)+(1-x)(P_n-P_l)\right]+zS_d-C_d,
\]
and
\[
C(x,y)=-xy(S_g+C_G)-x(F-C_G)-yS_d+F-C_G.
\]

The source states that under its drift inequalities (16)-(18), which do not contain \(\sigma\), the zero solution is moment exponentially stable. The printed stochastic system itself gives an exact obstruction to such a noise-blind conclusion.

The three coordinate axes are invariant. Define
\[
a_x=A(0,0)=\beta Q\Delta P+C_l-C_g,
\]
\[
a_y=B(0,0)=(\theta-1)\beta Q(P_n-P_l)-C_d,
\qquad
a_z=C(0,0)=F-C_G.
\]
On the \(x\)-axis, for example,
\[
dx=a_xx\,dt+\sigma x\,dW,
\]
and for every \(p>0\),
\[
\mathbb E|x(t)|^p
=
|x_0|^p
\exp\!\left(
\left[p a_x+\frac{p(p-1)}2\sigma^2\right]t
\right).
\]
The analogous formulas hold on the other two axes. Hence a necessary boundary condition for \(p\)-th-moment exponential stability of the full zero state is
\[
a_i+\frac{p-1}2\sigma^2<0
\quad\text{for every }i\in\{x,y,z\}.
\]
For mean-square stability this becomes
\[
2a_i+\sigma^2<0.
\]

The source's own Parameter Set 1 has
\[
Q=10,\quad \beta=0.2,\quad \Delta P=0.1,\quad C_l=2,\quad C_g=5,
\]
so
\[
a_x=0.2\cdot10\cdot0.1+2-5=-2.8.
\]
Along the invariant \(x\)-axis, its three displayed drift inequalities (16)-(18) reduce to
\[
-2.8x\le -x,\qquad 0\le0,\qquad0\le0.
\]
Thus the displayed drift test is satisfied there for every \(x>0\). But the model places no upper restriction on the disturbance intensity in the stability statement. Taking \(\sigma=3\) gives
\[
\mathbb E[x(t)^2]=x_0^2e^{(2(-2.8)+9)t}
=x_0^2e^{3.4t},
\]
which grows exponentially. Therefore the zero state is not mean-square exponentially stable.

The same counterexample simultaneously shows why a pathwise convergence observation cannot substitute for a moment calculation. Here
\[
x(t)=x_0\exp\!\left[\left(-2.8-\frac92\right)t+3W_t\right],
\]
so
\[
\lim_{t\to\infty}\frac1t\log x(t)=-7.3
\]
almost surely, even though its second moment grows like \(e^{3.4t}\). Noise can improve the almost-sure exponent while worsening higher moments.

## Assumptions and scope
The result concerns equations (10)-(12) exactly as printed in the source and the nonnegative strategy state space containing the pure-strategy boundary point \((0,0,0)\). The axis calculation uses only multiplicative absorption of zero: if \(y(0)=z(0)=0\), then \(y(t)=z(t)=0\) for all \(t\), and the \(x\)-equation becomes scalar geometric Brownian motion.

The necessary condition is stated for any \(p>0\). The direct contradiction is given for \(p=2\), the standard mean-square notion emphasized in the stochastic evolutionary-game literature cited by the source.

The counterexample does not claim that the source's simulations at their chosen disturbance levels are wrong. It shows that conditions (16)-(18), being independent of \(\sigma\), cannot by themselves imply moment exponential stability across the stochastic model family.

## Proof
Suppose \(y(0)=z(0)=0\). Because the \(y\)- and \(z\)-equations each contain their state variable as a factor in both drift and diffusion, pathwise uniqueness for the scalar multiplicative equations gives
\[
y(t)=z(t)=0.
\]
Hence the \(x\)-axis is invariant, and there
\[
dx=a_xx\,dt+\sigma x\,dW.
\]
Its exact solution is
\[
x(t)=x_0\exp\!\left[
\left(a_x-\frac{\sigma^2}{2}\right)t+\sigma W_t
\right].
\]
Raising to the \(p\)-th absolute power and using
\[
\mathbb E e^{p\sigma W_t}
=
e^{p^2\sigma^2t/2}
\]
gives
\[
\mathbb E|x(t)|^p
=
|x_0|^p
e^{[pa_x+p(p-1)\sigma^2/2]t}.
\]
The \(y\)- and \(z\)-axes give the same formula with \(a_y\) and \(a_z\).

If the origin were \(p\)-th-moment exponentially stable, then in particular every sufficiently small initial condition on each invariant axis would have an exponentially decaying \(p\)-th moment. The displayed exact formulas therefore force
\[
pa_i+\frac{p(p-1)}2\sigma^2<0,
\]
equivalently
\[
a_i+\frac{p-1}2\sigma^2<0.
\]

For Parameter Set 1, the source gives \(Q=10\), \(\beta=0.2\), \(\Delta P=0.1\), \(C_l=2\), and \(C_g=5\), so \(a_x=-2.8\). Conditions (16)-(18) evaluated on the \(x\)-axis are exactly
\[
-2.8x\le-x,\quad 0\le0,\quad0\le0.
\]
For \(\sigma=3\), however,
\[
2a_x+\sigma^2=-5.6+9=3.4>0.
\]
The exact second moment grows, contradicting mean-square exponential stability.

Finally, \(W_t/t\to0\) almost surely, so the same exact solution has pathwise Lyapunov exponent
\[
a_x-\frac{\sigma^2}{2}=-2.8-4.5=-7.3<0.
\]
This proves that the defect is specifically a moment-stability defect, not merely a failure of deterministic drift to point toward the origin.

## Verification
The bundled script `verification/verify.py` reconstructs the Parameter Set 1 boundary drift, checks all three source drift inequalities on the invariant \(x\)-axis, evaluates the exact \(p=2\) moment exponent for \(\sigma=3\), and evaluates the almost-sure exponent. It prints `VERIFY_OK` only if the source inequalities are satisfied while the second moment grows.

The proof is analytic. No Monte Carlo estimate is used to establish the moment exponent.

## Relationship to prior work
The motivating paper explicitly states that the zero solution of its stochastic game is moment exponentially stable when its drift inequalities (16)-(18) hold, then derives state regions \(X_1\), \(Y_1\), and \(Z_1\). Those inequalities contain no stochastic-intensity term even though equations (10)-(12) have diffusion coefficient \(\sigma\) in every coordinate.

Wang et al. (2024), which the motivating paper cites in its stochastic-game literature review, defines \(p\)-exponential stability in the mean square through decay of \(\mathbb E|x(t)|^p\). Its fixed-point sufficient condition explicitly contains the noise coefficient through an integral of \(G^2\). That prior work therefore supports the need for noise-aware moment conditions, but it studies a different two-player supply-chain-finance model and does not give the exact invariant-axis obstruction or counterexample for the 2025 agri-food system.

Wang et al. (2025) studies a four-player stochastic evolutionary game for prefabricated-building carbon reduction and numerically varies disturbance intensity. Its conclusion that larger disturbance intensity increases fluctuations is consistent with noise affecting stability behavior, but it does not provide the exact boundary moment exponent or correct the 2025 agri-food stability statement.

## Limitations
The result gives exact necessary conditions from invariant boundary directions; it is not a complete necessary-and-sufficient classification of the nonlinear three-dimensional stochastic system.

The explicit \(\sigma=3\) counterexample is chosen to test the source's unrestricted stability statement. It does not assert that the source used \(\sigma=3\) in its numerical figures, nor that those figures fail to reproduce their finite-time simulations.

The stochastic equations as printed omit the complement factors present in the preceding deterministic replicator equations. That separate modeling issue is not used in this finding.

No conclusion is drawn about other stochastic stability notions unless their definition is explicitly reduced to the corresponding geometric-Brownian exponent.

## References
1. Z. Wen, M. Mo, “The impact of environmental regulations and digital empowerment on agri-food supply chains under stochastic market demand conditions,” AIMS Mathematics 10 (2025), 22731–22768. DOI: 10.3934/math.20251011.
2. C. Wang, J. Weng, J. He, X. Wang, H. Ding, Q. Zhu, “Stability Analysis of the Credit Market in Supply Chain Finance Based on Stochastic Evolutionary Game Theory,” Mathematics 12 (2024), 1764. DOI: 10.3390/math12111764.
3. H. Wang, L. Li, C. Guo, R. Zhu, “Research on Stochastic Evolutionary Game and Simulation of Carbon Emission Reduction Among Participants in Prefabricated Building Supply Chains,” Applied Sciences 15 (2025), 4982. DOI: 10.3390/app15094982.
