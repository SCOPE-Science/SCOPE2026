# Exact RMS rigidity for the quadratic-only chaotic flow
## Finding
Consider the quadratic-only flow
\[
\dot x=a_1y^2-a_2z^2,\qquad
\dot y=b_1x^2-b_2z^2,\qquad
\dot z=c_1y^2+c_2z^2-1,
\]
with \(a_1,a_2,b_1,b_2,c_1,c_2>0\). Every bounded forward solution has coordinate-wise time-averaged squares that converge without any ergodicity assumption. Writing \(D=a_1c_2+a_2c_1\),
\[
\lim_{T\to\infty}\frac1T\int_0^T x(t)^2\,dt=\frac{a_1b_2}{b_1D},\qquad
\lim_{T\to\infty}\frac1T\int_0^T y(t)^2\,dt=\frac{a_2}D,
\]
\[
\lim_{T\to\infty}\frac1T\int_0^T z(t)^2\,dt=\frac{a_1}D.
\]
The vector of limiting mean squares is exactly the vector of squared coordinate magnitudes of each of the eight equilibria. Consequently every compactly supported invariant probability measure has these same second moments, and every periodic orbit satisfies the corresponding identities exactly over one period.

At the nominal parameters \(a_1=a_2=b_2=c_2=1\), \(b_1=2\), \(c_1=3\), every bounded forward solution satisfies
\[
\langle x^2\rangle=\frac18,\qquad \langle y^2\rangle=\langle z^2\rangle=\frac14.
\]
At the multistable setting used in the source, \(c_1=13/5\) with the other parameters unchanged, both the reported chaotic branch and the reported period-three branch necessarily satisfy
\[
\langle x^2\rangle=\frac5{36},\qquad \langle y^2\rangle=\langle z^2\rangle=\frac5{18}.
\]
Thus coexistence changes orbit geometry and temporal organization but cannot change these three RMS amplitudes.

## Assumptions and scope
The claim concerns classical forward solutions of the displayed autonomous ODE with all six parameters strictly positive. Boundedness of the forward trajectory is the only dynamical assumption needed for the time-average conclusion. No assumption of periodicity, ergodicity, chaos, or existence of a physical measure is used. The invariant-measure corollary is restricted to compactly supported invariant Borel probability measures. The result does not prove that a given bounded attractor exists, is chaotic, or is unique.

## Proof
For \(T>0\), define
\[
X_T=\frac1T\int_0^T x(t)^2\,dt,\quad
Y_T=\frac1T\int_0^T y(t)^2\,dt,\quad
Z_T=\frac1T\int_0^T z(t)^2\,dt.
\]
Integrating the three differential equations gives the exact finite-time linear system
\[
a_1Y_T-a_2Z_T=\frac{x(T)-x(0)}T,
\]
\[
b_1X_T-b_2Z_T=\frac{y(T)-y(0)}T,
\]
\[
c_1Y_T+c_2Z_T-1=\frac{z(T)-z(0)}T.
\]
If the trajectory is bounded, each right-hand side tends to zero. The coefficient matrix for \(X_T,Y_T,Z_T\) has determinant \(-b_1(a_1c_2+a_2c_1)\neq0\). Therefore the limiting linear system has the unique solution
\[
Z_\infty=\frac{a_1}D,\qquad
Y_\infty=\frac{a_2}D,\qquad
X_\infty=\frac{a_1b_2}{b_1D},
\]
which proves convergence of all three mean squares.

For a compactly supported invariant probability measure \(\mu\), invariance gives \(\int Lx\,d\mu=\int Ly\,d\mu=\int Lz\,d\mu=0\), where \(L\) is the flow generator. Substituting the three displayed vector-field components gives the same nonsingular linear system and hence the same moments. On a periodic orbit, integrating over one full period makes all endpoint differences vanish exactly.

The source's equilibrium formulas have squared coordinate magnitudes
\[
\frac{a_1b_2}{b_1D},\qquad \frac{a_2}D,\qquad \frac{a_1}D,
\]
so the equality between the RMS vector and equilibrium-coordinate magnitudes is exact.

## Verification
The bundled `verify.py` checks the three algebraic balance substitutions exactly with rational arithmetic, verifies the nominal and multistable specializations, and checks that the equilibrium-coordinate squares match the limiting moments. Its recorded output is `VERIFY_OK`.

A direct numerical test is not used as proof. The proof is the exact integration and inversion above; numerical trajectories would only illustrate it.

## Relationship to prior work
Almatroud, Rajagopal, Pham, and Grassi introduce this exact quadratic-only flow, give its eight equilibria, analyze their instability at selected parameters, and report bifurcation, Lyapunov, basin, chaotic, periodic, and multistable behavior. Their showcased multistable case has \(c_1=2.6=13/5\) and coexisting chaotic and period-three solutions. The source does not state the closed time-average system or the resulting universal second-moment vector.

Targeted searches for the article title and DOI together with “mean square”, “time average”, “RMS”, and “invariant measure” found the source and bibliographic/citation records but no statement of these identities. Semantic searches for the exact vector field and for quadratic-only chaotic systems with exact second moments returned balance-law results for other dynamical systems, not this model. Generic facts that invariant measures annihilate flow derivatives explain the method, but they do not supply this model-specific closed moment vector or its consequence for the source's coexisting attractors without applying the three equations and solving the resulting nonsingular system.

## Limitations
The law applies only to bounded forward trajectories. It does not bound trajectories a priori, prove existence of the reported attractors, distinguish chaos from periodicity, determine basins, or imply that two invariant measures with the same second moments are otherwise similar. The originality assessment is literature-based rather than a proof of global uniqueness in all unpublished work; later or poorly indexed analyses could contain the same observation.

## References
1. O. A. Almatroud, K. Rajagopal, V.-T. Pham, G. Grassi, “A Novel Chaotic System with Only Quadratic Nonlinearities: Analysis of Dynamical Properties and Stability,” *Mathematics* 12 (2024), 612. DOI: 10.3390/math12040612. Published 19 February 2024.
2. The same article, Section 2 for the vector field and equilibria; Section 3 and Figures 3–5 for the bifurcation and multistability analysis.
