# Universal nonlinear period slowing at the Brusselator Hopf boundary

## Finding

Consider the classical Brusselator chemical oscillator
\[
\dot x=A-(B+1)x+x^2y,\qquad \dot y=Bx-x^2y,
\]
with \(A>0\) fixed and \(B=1+A^2+\mu\). For every fixed \(A>0\) there is \(\epsilon_A>0\) such that, for \(0<\mu<\epsilon_A\), a unique small-amplitude periodic orbit exists near the equilibrium \((A,B/A)\), up to phase. It is orbitally asymptotically stable, and its least period satisfies
\[
T_A(\mu)=\frac{2\pi}{A}\left[1+\frac{4A^4-7A^2+4}{6A^2(A^2+2)}\,\mu+O_A(\mu^2)\right].
\]
The period has a **strictly positive right derivative** at Hopf for **every** \(A>0\). Equivalently, increasing the reaction-feed parameter \(B\) through the Hopf surface strictly lengthens the newly born oscillation to first order, even though the equilibrium's linearized determinant \(A^2\) is independent of \(B\).

## Assumptions and scope

The phase variables and parameters are real; \(A>0\), and \(\mu\) is restricted to a sufficiently small, \(A\)-dependent neighborhood of zero. The equilibrium \((A,B/A)\) has Jacobian trace \(\mu\), determinant \(A^2\), and eigenvalues \(\pm iA\) at \(\mu=0\); the trace crosses transversely at speed one. The statement concerns the local branch of positive-parameter periodic orbits with \(\mu\downarrow0\), not all periodic orbits or large-parameter behavior. \(O_A(\mu^2)\) is a remainder with a constant that may depend on \(A\); no uniform estimate as \(A\to0\) or \(A\to\infty\) is asserted.

## Proof

Write \(u=x-A\), \(v=y-B/A\), \(w=u+v\), and \(p=\dot w\). Adding the two original equations gives \(\dot w=A-x=-u\), so the change of coordinates is invertible: \(x=A-p\) and \(y=B/A+w+p\). With \(B=1+A^2+\mu\), differentiating \(p=A-x\) gives the **exact** second-order polynomial identity
\[
\ddot w+A^2w=\mu\dot w+2Aw\dot w+\left(A-A^{-1}-\mu A^{-1}\right)(\dot w)^2-w(\dot w)^2-(\dot w)^3. \tag{1}
\]
This identity is global in the translated state variables; no approximation has been made.

Seek a near-Hopf branch using a phase variable \(\tau=\Omega t\) and the standard Lyapunov--Schmidt/Poincaré--Lindstedt reduction for the analytic periodic-orbit boundary-value problem:
\[
\begin{aligned}
w(\tau)&=\rho\cos\tau+\rho^2 W_2(\tau)+O_A(\rho^3),\\
\mu&=\kappa\rho^2+O_A(\rho^4),\qquad
\Omega=A+\nu\rho^2+O_A(\rho^4).
\end{aligned}
\]
Choose the phase so the fundamental cosine coefficient is \(\rho\), with zero fundamental sine coefficient. At order \(\rho^2\), equation (1) yields the uniquely specified zero-first-harmonic particular solution
\[
W_2(\tau)=\frac{A-A^{-1}}{2}+\frac{A-A^{-1}}{6}\cos(2\tau)+\frac13\sin(2\tau).
\]
At order \(\rho^3\), the required vanishing of the cosine and sine resonant forcing coefficients is exactly
\[
\frac{4A^4-7A^2+24A\nu+4}{12}=0,\qquad
-\frac A4(4\kappa-A^2-2)=0.
\]
Consequently,
\[
\kappa=\frac{A^2+2}{4}>0,\qquad
\nu=-\frac{4A^4-7A^2+4}{24A}.
\]
Nonvanishing \(\kappa\), along with the transverse eigenvalue crossing, is the nondegeneracy condition in the analytic Hopf reduction. It determines a supercritical, orbitally stable local cycle for \(\mu>0\), unique locally up to phase. Its frequency is
\[
\Omega=A-\frac{4A^4-7A^2+4}{6A(A^2+2)}\,\mu+O_A(\mu^2).
\]
Taking \(2\pi/\Omega\) gives the claimed period formula. Strict positivity follows from the elementary, globally valid identity
\[
4A^4-7A^2+4=4\left(A^2-\frac78\right)^2+\frac{15}{16}>0.
\]
Analytic Hopf reduction also justifies the claimed remainder powers (rather than treating the formal harmonic equations alone as an existence proof).

## Verification

The standalone `verify_brusselator.py` reconstructs (1) by symbolic substitution and checks the second-order Fourier equation and both independent third-order resonance equations exactly in SymPy. It then checks the frequency-to-period conversion and positivity decomposition. Execute with `python verify_brusselator.py` in a Python environment with SymPy installed. These finite symbolic identities support the coefficients; local existence, stability, uniqueness and the asymptotic remainder follow analytically from the standard nondegenerate Hopf theorem, not from finite numerical sampling.

## Relationship to prior work

The underlying two-variable autocatalytic model was published by Prigogine and Lefever (1968). Chen, Li, Hou and Zuo (2017) reproduce the classical equations and analyze forced/fractional slow--fast bursting, including Hopf thresholds. Player and collaborators (2021) examine limit-cycle amplitudes and periods numerically when changing \(A\) at fixed \(B\), particularly canard-associated large responses. Those published numerical plots do not themselves establish the **closed, all-\(A\), fixed-\(A\) derivative** above. Larter, Rabitz and Kramer (1984) directly study parameter sensitivity of Brusselator limit cycles; the available abstract documents their general Fourier sensitivity method but does not determine whether their full text contains the present exact local coefficient. This historical priority question remains open pending access to that full text. The result is not a claim of global period monotonicity.

## Limitations

There is no global uniqueness theorem, no assertion about canard regimes, large-amplitude cycles, period changes along paths with varying \(A\), or dynamics far from Hopf. The 1984 parameter-sensitivity paper and the 1973 Tyson analysis were not available in full text for an exhaustive historical comparison; an equivalent older calculation cannot be excluded. The derivation is a self-review, not an independent audit.

## References

1. I. Prigogine and R. Lefever, *Symmetry Breaking Instabilities in Dissipative Systems. II*, J. Chem. Phys. **48**, 1695--1700 (1968), doi:10.1063/1.1668896.
2. R. Larter, H. Rabitz and M. A. Kramer, *Sensitivity analysis of limit cycles with application to the Brusselator*, J. Chem. Phys. **80**, 4120--4128 (1984), doi:10.1063/1.447293.
3. J. Chen, X. Li, J. Hou and D. Zuo, *Bursting oscillation and bifurcation mechanism in fractional-order Brusselator with two different time scales*, J. Vibroeng. (2017), https://www.extrica.com/article/18109.
4. T. C. Player, E. D. A. Baxter, S. Allatt and P. J. Hore, *Amplification of weak magnetic field effects on oscillating reactions*, Sci. Rep. **11**, 9615 (2021), doi:10.1038/s41598-021-88871-8.
5. J. J. Tyson, *Some further studies of nonlinear oscillations in chemical systems*, J. Chem. Phys. **58**, 3919--3930 (1973), doi:10.1063/1.1679748.
