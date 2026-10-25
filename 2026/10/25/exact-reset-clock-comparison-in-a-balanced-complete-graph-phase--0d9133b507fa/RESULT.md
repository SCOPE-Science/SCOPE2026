# Exact reset-clock comparison in a balanced complete-graph phase network

## Finding

Consider a complete-graph, linearly coupled network of \(N\ge 2\) real phase deviations. At an equal **per-node reset rate**, independent resets of individual nodes strictly reduce stationary mean-square relative-phase disagreement compared with simultaneous resets of every node; however, they introduce nonzero collective-phase fluctuations, which simultaneous resets eliminate exactly.

Let \(A=\sum_{i=1}^N\omega_i^2>0\), \(\sum_i\omega_i=0\), let \(r,\gamma>0\), and define the stationary disagreement
\[
\mathcal D=\mathbb E\sum_{i=1}^N(X_i-\overline X)^2,
\qquad \overline X=N^{-1}\sum_{i=1}^N X_i.
\]
For a common Poisson clock of rate \(r\) resetting all nodes to zero (protocol S), and separate independent rate-\(r\) Poisson clocks resetting one corresponding node at a time (protocol I), the exact formulas are
\[
\mathcal D_S=\frac{2A}{(r+\gamma)(r+2\gamma)},
\qquad
\mathcal D_I=\frac{A(2N-1)}{(r+\gamma)[Nr+(2N-1)\gamma]}.
\]
In particular, the strict protocol gap and its universal ratio are
\[
\boxed{\mathcal D_S-\mathcal D_I
=\frac{Ar}{(r+\gamma)(r+2\gamma)[Nr+(2N-1)\gamma]}>0},
\]
\[
\frac{\mathcal D_I}{\mathcal D_S}
=\frac{(2N-1)(r+2\gamma)}{2[Nr+(2N-1)\gamma]}
\in\left(1-\frac1{2N},1\right).
\]
The two protocols have identical individual stationary means
\(\mathbb E X_i=\omega_i/(r+\gamma)\), but their collective modes differ:
\[
\mathbb E_S[\overline X^2]=0,
\qquad
\mathbb E_I[\overline X^2]=
\frac{A}{N(r+\gamma)[Nr+(2N-1)\gamma]}>0.
\]
Writing \(\mathcal V=\mathcal D-\sum_i(\mathbb E X_i-\mathbb E\overline X)^2\) for the centered fluctuation energy in relative-phase directions, one further has
\[
\mathcal V_S=\frac{Ar}{(r+\gamma)^2(r+2\gamma)},
\quad
\mathcal V_I=\frac{A(N-1)r}{(r+\gamma)^2[Nr+(2N-1)\gamma]},
\]
so \(\mathcal V_I/\mathcal V_S=(N-1)(r+2\gamma)/[Nr+(2N-1)\gamma]<1\).

## Assumptions and scope

The state is \(X(t)=(X_1(t),\ldots,X_N(t))\in\mathbb R^N\), **not** phases reduced modulo \(2\pi\). Between resets, it solves the deterministic linearized all-to-all phase equations
\[
\frac{dX_i}{dt}=\omega_i-\gamma(X_i-\overline X),
\qquad \sum_{i=1}^N\omega_i=0.
\]
The frequencies are arbitrary fixed balanced real numbers, not all zero. The complete-graph coupling is normalized so that \(\gamma\) is the nonzero transverse relaxation eigenvalue. Each protocol has the same rate \(r\) of zero-reset operations **per node**. A simultaneous event resets all nodes, whereas an independent event resets only its associated node and retains the other coordinates. Both clocks and the deterministic dynamics are Markovian. All parameters \(N\ge2\), \(r>0\), \(\gamma>0\) are arbitrary as quantified above. The theorem concerns unique stationary distributions of these exact piecewise-deterministic systems, not a claim that a nonlinear circle-valued Kuramoto network obeys these identities exactly.

## Proof

**1. Stationarity and second moments.** Let \(P=I-\mathbf1\mathbf1^{\mathsf T}/N\). The deterministic part is \(\dot X=\omega-\gamma PX\), with \(P\omega=\omega\). If two copies share all reset events, their difference evolves between events as \(\dot Z=-\gamma PZ\), hence its Euclidean norm does not increase. In protocol S the first common event erases the difference. In protocol I, the independent rate-\(r\) reset of node \(i\) removes exactly \(Z_i^2\), giving
\[
\frac d{dt}\mathbb E\|Z_t\|^2\le-r\mathbb E\|Z_t\|^2.
\]
A quadratic Foster bound follows from \(2\omega\cdot X\le(r/2)\|X\|^2+2A/r\): for either protocol the quadratic generator has negative drift outside a compact set. The resulting tight occupation measures provide a stationary law of finite second moment, and the coupling contraction gives uniqueness among such laws. The same bound and finite-time moment equations imply uniqueness of the stationary law reached from any fixed initial state.

**2. First moments.** In both protocols a coordinate is reset to zero at rate \(r\). Let \(m_i=\mathbb E X_i\). Summing the stationary mean equations and using \(\sum_i\omega_i=0\) yields \(\sum_i m_i=0\). Thus
\[
0=\omega_i-\gamma(m_i-\overline m)-rm_i,
\qquad m_i=\frac{\omega_i}{r+\gamma}.
\]

**3. Common-clock protocol.** Put \(U=\mathbb E\|X\|^2\), \(S=\sum_iX_i\), and \(D=\mathbb E\|PX\|^2\). Since \(\dot S=0\) between jumps and every common jump sets \(S=0\), stationarity forces \(S=0\) almost surely. Therefore \(D=U\). The stationary quadratic generator identity gives
\[
0=2\mathbb E(\omega\cdot X)-2\gamma D-rU
=\frac{2A}{r+\gamma}-(2\gamma+r)D,
\]
proving the formula for \(\mathcal D_S\). Equivalently, with the stationary exponential backward age \(T\sim\mathrm{Exp}(r)\), \(X=(1-e^{-\gamma T})\omega/\gamma\); direct integration gives the same result.

**4. Independent-clock protocol.** The deterministic sum \(S\) remains constant between events; resetting coordinate \(i\) changes \(S^2\) by \(-2SX_i+X_i^2\). Therefore stationarity gives the exact, forcing-independent identity
\[
0=r\sum_i\mathbb E(-2SX_i+X_i^2)
=r[-2\mathbb E S^2+U],
\quad\text{i.e.}\quad\mathbb E S^2=\frac U2.
\]
As \(D=U-\mathbb E S^2/N\), this yields \(D=U(1-1/(2N))\). The quadratic generator equation for \(U\) remains
\[
0=\frac{2A}{r+\gamma}-2\gamma D-rU.
\]
Solving gives
\[
U=\frac{2A}{(r+\gamma)(r+2\gamma-\gamma/N)},
\qquad
D=\frac{A(2N-1)}{(r+\gamma)[Nr+(2N-1)\gamma]},
\]
and
\(\mathbb E\overline X^2=\mathbb E S^2/N^2=U/(2N^2)\).

**5. Comparison and centered covariance.** Subtracting the two explicit expressions for \(D\) yields the strictly positive gap displayed in the finding. Both mean vectors equal \(\omega/(r+\gamma)\), so subtracting their common squared transverse mean \(A/(r+\gamma)^2\) yields the two \(\mathcal V\) formulas. Strict inequalities follow from \(A,r,\gamma>0\) and \(N\ge2\). As a boundary check, both protocols coincide in the \(r\downarrow0\) limit; as \(r\to\infty\), \(\mathcal D_I/\mathcal D_S\to (2N-1)/(2N)\). These are limits only; the hypotheses require positive finite \(r\).

## Verification

The accompanying `verify.py` implements the **full independent stationary second-moment linear system** rather than imposing the summed generator identities derived above. It solves the rational linear equations for every symmetric \(\mathbb E X_iX_j\) using exact `fractions.Fraction` Gaussian elimination. It independently checks \(\mathcal D\), common-mode energy, centered transverse energy and the strict protocol gap for 45 combinations of size \(N=2,3,4,5,6\), reset rate \(r\in\{1/3,1,4\}\), damping \(\gamma\in\{1/2,2,5\}\), and deliberately nonconstant balanced natural-frequency vectors. Execute with `python verify.py`; no nonstandard packages are required. The numerical-exact tests verify these finite cases, while the algebraic generator proof supplies the quantification over all sizes and positive parameters.

## Relationship to prior work

Paramero-Arias and Riascos, arXiv:2610.21842v1 (2026), investigate synchronized simultaneous resetting of chosen network subsystems, emphasizing infinite-reset-rate grounding and network placement. Their fully accessible manuscript, especially Sec. II.1 and Conclusions, uses a single common Poisson clock for all reset nodes; it does not state an all-node comparison with independently ticking clocks or exact finite-rate stationary quadratic-energy identities. The previous subsystem-resetting framework of Majumder, Chattopadhyay and Gupta, arXiv:2402.14921v1 (2024), likewise uses simultaneous resetting of a subsystem. Closest in protocol is Bressloff, arXiv:2401.03501v1 (2024), which **already explicitly distinguishes independent local and global simultaneous resetting** for interacting Brownian particles and Kuramoto oscillators, and derives general exact empirical-density (Dean–Kawasaki) equations. Its Sec. V studies the nonlinear Kuramoto density, McKean–Vlasov limits, and macroscopic order parameters; those generic stochastic equations are established prerequisites and not claimed as new here. The current all-finite-size closed stationary quadratic disagreement identities and strict inequality require an additional solvable balanced real-linear model and its square-of-sum generator closure; they are not stated in Bressloff’s analysis. Majumder, Acharya and Gupta, arXiv:2604.04769v1 (2026), generalize this simultaneous-subsystem model through collective order-parameter self-consistency equations. Their Sec. IV protocol description and introduction retain a collective reset event, rather than independent per-node clocks. These works provide the motivating and established physics; no novelty is claimed for linearizing Kuramoto interactions, the use of Poisson resetting, or standard moment-generator techniques. The precise candidate contribution is the parameter-complete, cost-matched **comparison** of two clock-correlation protocols and the opposing relative/common mode energy laws.

## Limitations

The dynamics is an exact **real-valued linear approximation** with a complete-graph transverse Laplacian eigenvalue, not the full nonlinear circle-valued Kuramoto system. The results apply only to balanced constant natural frequencies, identical reset rates, deterministic zero reset targets and memoryless independent or common clocks. There is no thermal phase diffusion, quenched coupling disorder, partial resets, or network topology beyond the complete graph. The stationary statements are exact for this specified model; they do not assert synchronization transitions or entropy-production comparisons in larger nonlinear systems. Broader existing linear-resetting covariance theorems may implicitly encompass the exact identities; independent priority assessment has not been carried out.

## References

1. K. Paramero-Arias and A. P. Riascos, *Synchronization induced by stochastic subsystem resetting in complex networks*, arXiv:2610.21842v1, first public 2026-10-15, https://arxiv.org/abs/2610.21842.
2. R. Majumder, A. Acharya and S. Gupta, *Analytical approach to subsystem resetting in generalized Kuramoto models*, arXiv:2604.04769v1, first public 2026-04-06, https://arxiv.org/abs/2604.04769.
3. R. Majumder, R. Chattopadhyay and S. Gupta, *Kuramoto model subject to subsystem resetting: How resetting a part of the system may synchronize the whole of it*, arXiv:2402.14921v1, first public 2024-02-22, https://arxiv.org/abs/2402.14921.
4. P. C. Bressloff, *Global density equations for interacting particle systems with stochastic resetting: from overdamped Brownian motion to phase synchronization*, arXiv:2401.03501v1, first public 2024-01-07, https://arxiv.org/abs/2401.03501.
