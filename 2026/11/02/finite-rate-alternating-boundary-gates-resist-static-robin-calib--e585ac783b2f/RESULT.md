# Finite-rate alternating boundary gates resist static Robin calibration

## Finding

A Brownian particle on a finite interval experiences a jointly switching pair of terminal gates: exactly one endpoint absorbs while the other reflects. When the gate state initially has its symmetric stationary distribution, the mean absorption time and left-exit probability are, for every starting point \(0\leq x\leq L\),

\[
\mathbb E_x\tau=\frac{x(L-x)}{2D}+\frac{L}{2D\alpha}\tanh\!\left(\frac{\alpha L}{2}\right),\qquad
\mathbb P_x\{\text{left exit}\}=\frac12+\frac{L/2-x}{L+(2/\alpha)\coth(\alpha L/2)},
\]

where \(\alpha=\sqrt{2\kappa/D}\), \(D>0\) is the diffusivity, \(L>0\) is the interval length, and \(\kappa>0\) is the switching rate in each direction. These two exact observables cannot **both** be reproduced at every initial point by a static Brownian model with any fixed, positive Robin reactivities at the two endpoints.

Indeed, to reproduce the mean time the static model must use the **same** reactivity at both ends,

\[
h_{\mathrm{time}}=D\alpha\coth\!\left(\frac{\alpha L}{2}\right),
\]

whereas to reproduce the splitting probability it must use

\[
h_{\mathrm{split}}=D\alpha\tanh\!\left(\frac{\alpha L}{2}\right),\qquad
\frac{h_{\mathrm{time}}}{h_{\mathrm{split}}}=\coth^2\!\left(\frac{\alpha L}{2}\right)>1.
\]

Consequently, mean-lifetime calibration and exit-side calibration are incompatible at every finite positive switching rate; their inferred reactivities agree only asymptotically in the infinite-switching-rate limit. The stochastic-gate penalty in the mean time is independent of the particle's starting position. This provides a simple, exact two-observable test for finite-rate boundary intermittency.

## Assumptions and scope

Take a reflected diffusion with infinitesimal generator \(D\partial_x^2\) in \([0,L]\). An independent continuous-time two-state Markov chain changes state at rate \(\kappa\) in both directions. In state \(0\), the boundary \(x=0\) is perfectly absorbing and \(x=L\) perfectly reflecting. In state \(1\), the assignments reverse. A particle is killed upon reaching an endpoint while it is open, with the usual absorbing/Neumann boundary conventions. At time zero the gate state is sampled uniformly from the two states, independently of particle position. The assertion covers all real \(D,L,\kappa>0\) and all \(x\in[0,L]\). Initial positions at an open boundary are absorbed at time zero. A static comparison model has the same \(D,L\), no internal state, and positive time-independent radiation/Robin parameters \(h_0,h_L\), with backward mean-time conditions \(D T'(0)=h_0T(0)\) and \(-DT'(L)=h_LT(L)\).

## Proof

**Finite absorption and uniqueness.** On any time interval of fixed length, the gate has a uniform positive chance of remaining in its current state while reflected Brownian motion reaches the corresponding absorbing endpoint. Compactness of \([0,L]\) makes the chance uniform in the initial position and gate state. Iteration via the Markov property gives a geometric tail for survival in fixed-length time blocks and hence finite mean time. The standard bounded-solution backward boundary problems therefore characterize the actual mean and exit probabilities uniquely.

**Mean time.** Write \(u_j(x)=\mathbb E_{x,j}\tau\). Backward equations and boundary data are

\[
D u_0''+\kappa(u_1-u_0)=-1,\quad D u_1''+\kappa(u_0-u_1)=-1,
\]
\[
u_0(0)=0,\quad u_1'(0)=0,\quad u_0'(L)=0,\quad u_1(L)=0.
\]

For \(S=(u_0+u_1)/2\) and \(V=(u_0-u_1)/2\), the equations decouple as \(DS''=-1\) and \(DV''-2\kappa V=0\). Left-right interchange gives \(S(L-x)=S(x)\) and \(V(L-x)=-V(x)\), so

\[
S(x)=\frac{x(L-x)}{2D}+C,\qquad V(x)=B\sinh(\alpha(x-L/2)).
\]

From \(u_1'(0)=0\) one finds \(B=L/[2D\alpha\cosh(\alpha L/2)]\). From \(u_0(0)=0\) one obtains \(C=B\sinh(\alpha L/2)\), giving the displayed mean-time identity for uniformly sampled initial gates.

**Splitting probability.** Let \(p_j(x)=\mathbb P_{x,j}\{\text{left exit}\}\). These satisfy the corresponding homogeneous backward equations with boundary data

\[
p_0(0)=1,\quad p_1'(0)=0,\quad p_0'(L)=0,\quad p_1(L)=0.
\]

With \(P=(p_0+p_1)/2\), \(Q=(p_0-p_1)/2\), the equations read \(P''=0\) and \(Q''-\alpha^2Q=0\). Reflected interchange gives \(P(x)=1-P(L-x)\) and \(Q(x)=Q(L-x)\). Hence

\[
P(x)=\frac12+c(x-L/2),\qquad Q(x)=A\cosh(\alpha(x-L/2)).
\]

The left boundary yields \(A=[2(\cosh t+t\sinh t)]^{-1}\), \(c=-\alpha\sinh t/[2(\cosh t+t\sinh t)]\), where \(t=\alpha L/2\). Rearrangement produces the displayed affine left-exit probability.

**Robin obstruction.** For a static interval with a common positive radiation reactivity \(h\), direct solution of the backward equations gives

\[
T_h(x)=\frac{x(L-x)}{2D}+\frac{L}{2h},\qquad
P_h(x)=\frac12+\frac{L/2-x}{L+2D/h}.
\]

Even if different \(h_0,h_L>0\) are initially allowed, equality of the static mean \(T\) with the displayed switching mean for **all** starting positions forces \(T(x)\) to be symmetric. Its derivatives at the endpoints then require \(h_0=h_L=L/[2T(0)]\). The mean-time identity therefore forces \(h=h_{\mathrm{time}}\), while equality of the nonconstant splitting profile forces \(h=h_{\mathrm{split}}\). For finite \(t>0\), \(0<\tanh t<1\); thus these values differ and no such static model exists.

**Switching limits.** The mean penalty is \((L^2/(4D))(\tanh t/t)\), a strictly decreasing function of \(\kappa>0\): \(\tanh t-t\operatorname{sech}^2t>0\) follows by differentiating it, since its derivative is \(2t\operatorname{sech}^2t\tanh t>0\). As \(\kappa\downarrow0\), the penalty approaches \(L^2/(4D)\), whereas \(h_{\mathrm{time}}\to 2D/L\) and \(h_{\mathrm{split}}\to0\). As \(\kappa\to\infty\), the penalty is asymptotic to \(L/[2\sqrt{2D\kappa}]\) and both calibrated reactivities are asymptotic to \(\sqrt{2D\kappa}\); the exit probability approaches \(1-x/L\).

## Verification

The included standalone Python checker `check_alternating_gates.py` constructs independent finite-state approximations to the joint particle-gate Markov process. It solves separate linear systems for the mean stopping time and the left-absorption probability, compares both with the continuum formulas for 24 grid/parameter/starting-site instances, and tests the strict Robin-calibration mismatch. Run `python check_alternating_gates.py` with Python, NumPy and no external datasets. The observed largest absolute differences were below \(0.00083\) for the mean and \(0.00026\) for the probability. These are finite-mesh diagnostics; the preceding differential-equation argument proves the stated continuum identities for the complete parameter range.

## Relationship to prior work

Alternating absorbing gates and the decay of mean exit time with switching rate have already been studied by Ammari, Garnier, Kang, Lee and Sølna [2] for small boundary gates in planar domains. Reingruber and Holcman [1] analyze two-state ligand gating, including an exactly solvable one-dimensional model with a single reactive window and state-dependent diffusivities. Bressloff and Lawley [3] treat switching boundaries, potentials, and multiple small gates; they derive general backward-equation and asymptotic frameworks. Those background mechanisms and monotonicity phenomena are not claimed as new. The present result isolates a finite-length, two-endpoint one-dimensional geometry and compares **two simultaneously exact observables** to establish the no-static-Robin-calibration obstruction. Lawley and Keener [4] establish Robin boundary conditions in a separate fast-switching homogenization regime; their abstract does not establish an exact finite-rate two-observable match. Sezik and coauthors [5] study joint and conditional splitting probabilities for hidden-state processes with fixed boundary conditions, rather than an oppositely switching pair of absorbing endpoints. The derived formulas should not be described as novel merely because other sources parameterize the gate dynamics differently.

## Limitations

The result concerns one Brownian particle, symmetric Poisson switching, an initially stationary gate state, perfect open-state absorption, and a constant diffusion coefficient. It does not characterize every time-dependent boundary process or the full first-passage-time distribution. The obstruction concerns exact equality of mean and side-exit probability **functions for all starting positions** with a static Robin model; it does not preclude fitting individual measurements or more general nonlocal effective boundary models. Relevant historical literature is substantial; some exact finite-rate formulations could remain unrecognized. In particular, the complete text of [4] could not be inspected, so the priority comparison remains provisional. No independent validation or claim of certified historical priority is made.

## References

[1] J. Reingruber and D. Holcman, *The Gated Narrow Escape Time for molecular signaling*, first public arXiv version 14 September 2009, arXiv:0909.2521, https://arxiv.org/abs/0909.2521.

[2] H. Ammari, J. Garnier, H. Kang, H. Lee and K. Sølna, *The Mean Escape Time for a Narrow Escape Problem with Multiple Switching Gates*, Multiscale Modeling & Simulation 9 (2011), 817–833, https://doi.org/10.1137/100817103.

[3] P. C. Bressloff and S. D. Lawley, *Escape from Subcellular Domains with Randomly Switching Boundaries*, Multiscale Modeling & Simulation 13 (2015), 1420–1445, https://doi.org/10.1137/15M1019258.

[4] S. D. Lawley and J. P. Keener, *A New Derivation of Robin Boundary Conditions through Homogenization of a Stochastically Switching Boundary*, SIAM Journal on Applied Dynamical Systems 14 (2015), 1845–1867, https://doi.org/10.1137/15M1015182.

[5] E. Sezik et al., *Conditional splitting probabilities for hidden-state inference in drift-diffusive processes*, Proceedings of the Royal Society A 482 (2026), 20250716, https://doi.org/10.1098/rspa.2025.0716.
