# Periodic prey oscillations raise the predator invasion threshold in a Ricker-refuge model
## Finding
Consider the normalized discrete predator-prey system studied in the recent Ricker-refuge/cooperative-hunting literature, restricted to the two model identities needed here: on the predator-free boundary,
\[
x_{n+1}=x_n\exp(r(1-x_n)),
\]
and the predator equation linearized at \(y=0\) has the form
\[
y_{n+1}=R_0x_ny_n+O(y_n^2).
\]
For every positive period-\(k\) orbit \((x_0,\ldots,x_{k-1})\) of the boundary Ricker map,
\[
\frac1k\sum_{j=0}^{k-1}x_j=1,
\qquad
\Lambda_k=R_0^k\prod_{j=0}^{k-1}x_j,
\]
where \(\Lambda_k\) is the transverse predator Floquet multiplier. Hence a nonconstant prey-only cycle has geometric mean strictly below one and therefore the sharp linear invasion threshold
\[
R_{0,c}=\left(\prod_{j=0}^{k-1}x_j\right)^{-1/k}>1.
\]
The cooperation coefficient does not enter this first-order threshold. In particular, \(R_0>1\) is enough to invade the carrying-capacity equilibrium but need not be enough to invade an oscillatory prey-only boundary attractor.

For \(r=2.2\), the stable Ricker 2-cycle is
\[
x_1=0.497059425055358\ldots,\qquad x_2=1.502940574944642\ldots,
\]
with \(x_1x_2=0.747050778074353\ldots\). Thus
\[
R_{0,c}=1.1569775681472\ldots.
\]
At \(R_0=1.1\), the prey two-step multiplier is \(0.215725765879869\ldots\) and the predator two-step multiplier is \(0.903931441469967\ldots\), both of modulus below one. The predator-free 2-cycle is therefore locally asymptotically stable even though \(R_0>1\).

## Assumptions and scope
The theorem is conditional only on the two displayed model identities: the normalized Ricker map on \(y=0\), and transverse derivative \(\partial_yG(x,0)=R_0x\). These are the structural ingredients used in the Ricker prey-growth, proportional-refuge, cooperative-hunting model family motivating the calculation. Positivity of the period points is assumed. The conclusion concerns linear invasion and local Floquet stability of predator-free periodic orbits; it does not claim global attraction, persistence, or extinction for arbitrary initial conditions.

## Proof
Let \((x_0,\ldots,x_{k-1})\) be a positive period-\(k\) orbit of \(f_r(x)=x\exp(r(1-x))\), with indices taken modulo \(k\). Dividing the recurrence by \(x_j\), taking logarithms, and summing over one period gives
\[
0=\sum_{j=0}^{k-1}\log\frac{x_{j+1}}{x_j}
 =r\sum_{j=0}^{k-1}(1-x_j).
\]
Since \(r>0\), this yields \(\sum_jx_j=k\), proving the arithmetic-mean identity.

The linear predator recurrence along the boundary orbit is \(v_{j+1}=R_0x_jv_j\). Multiplying over one period yields
\[
v_k=R_0^k\left(\prod_{j=0}^{k-1}x_j\right)v_0,
\]
so the transverse Floquet multiplier is the stated \(\Lambda_k\). For a nonconstant positive orbit, the strict arithmetic-geometric mean inequality gives
\[
\left(\prod_jx_j\right)^{1/k}<\frac1k\sum_jx_j=1,
\]
and the threshold \(\Lambda_k=1\) is therefore \(R_{0,c}>1\).

For period two, write the cycle as \((u,2-u)\). The nontrivial root of
\[
2-u=u\exp(r(1-u))
\]
at \(r=2.2\) gives the numerical values reported above. The derivative of the Ricker map is \(f_r'(x)=\exp(r(1-x))(1-rx)\), so the prey multiplier over the two-cycle is
\[
f_r'(x_1)f_r'(x_2)=(1-rx_1)(1-rx_2),
\]
because the exponential ratios cancel around the cycle. Direct substitution gives the reported prey multiplier. The transverse predator multiplier is \(R_0^2x_1x_2\). Both are inside the unit disk at \(R_0=1.1\); the two-step Jacobian is triangular on the predator-free boundary, so these are its two eigenvalues and local asymptotic stability follows.

## Verification
The accompanying checker independently solves the nontrivial 2-cycle equation by bisection, checks the exact period-sum identity numerically, recomputes both two-step multipliers, verifies the strict threshold inequalities, and prints `VERIFY_OK` only if all tolerances pass. The proof of the general period-\(k\) formula is symbolic and does not depend on finite enumeration.

## Relationship to prior work
De Silva and Jang study a 2026 discrete predator-prey model with Ricker prey growth, prey refuge, and cooperative hunting. Their public abstract states that for moderate prey growth the predator reproduction number above one gives uniform persistence, while at higher prey growth predator-free boundary dynamics, including a 2-cycle, becomes relevant; it also states a sufficient global-stability condition for a predator-extinct 2-cycle. The result here isolates a different structural statement: for every positive Ricker boundary cycle of arbitrary period, the invasion multiplier is governed by the cycle's geometric mean, and every nonconstant cycle raises the invasion threshold strictly above the carrying-capacity value one.

The earlier Ricker cooperative-hunting paper of Chou, Chow, Hu, and Jang focuses on equilibria, reproduction numbers, and bifurcation of coexistence states. The 2023 refuge/cooperation model of Jang and Yousef uses Beverton-Holt prey growth, whose predator-free dynamics do not create the nonconstant Ricker cycles considered here. A 2025 conference abstract on the later Ricker-refuge model discusses fixed points, Neimark-Sacker behavior, and a predator-free threshold but does not state the period-\(k\) geometric-mean invasion law.

## Limitations
The accessible publisher material for the 2026 article exposed its abstract, bibliographic metadata, reference list, and figure captions, but not the full article body in the available text interface. Therefore there is a residual originality risk that the body contains an algebraically equivalent arbitrary-period statement not visible in the accessible material. The public abstract explicitly mentions only the equilibrium threshold and a predator-extinct 2-cycle, not the all-period formula. The claim is restricted to the displayed normalized boundary and transverse-linearization identities and does not extend automatically to delayed, stage-structured, stochastic, or differently normalized predator equations.

## References
1. T. M. M. De Silva and S. R.-J. Jang, “Persistence, extinction, and chaotic dynamics in a predator-prey system with cooperative hunting and prey refuge,” *AIMS Mathematics* 11 (2026), 21412–21440. DOI: 10.3934/math.2026868.
2. W. L. D. P. Tharushika and T. M. M. De Silva, “Cooperative hunting and prey refuge in the dynamics of predator-prey interaction,” *Proceedings of RESCON 2025*, p. 58, public repository date 2025-11-07.
3. Y. H. Chou, Y. Chow, X. Hu, and S. R.-J. Jang, “A Ricker-type predator-prey system with hunting cooperation in discrete time,” *Mathematics and Computers in Simulation* 190 (2021), 570–586. DOI: 10.1016/j.matcom.2021.06.003.
4. S. R.-J. Jang and A. M. Yousef, “Effects of prey refuge and predator cooperation on a predator-prey system,” *Journal of Biological Dynamics* 17 (2023), 2242372. DOI: 10.1080/17513758.2023.2242372.
