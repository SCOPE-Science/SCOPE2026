# First logarithmic correction to critical relaxation in the classical Lorenz system
## Finding
For the classical Lorenz equations at the pitchfork threshold \(\rho=1\), \[\dot x=\sigma(y-x),\qquad \dot y=x-y-xz,\qquad \dot z=xy-\beta z,\] with \(\sigma,\beta>0\), a sufficiently smooth local center manifold parameterized by the physical amplitude \(x=\xi\) has reduced dynamics \[\dot\xi=-\frac{\sigma}{\beta(\sigma+1)}\xi^3-\frac{\sigma(2\beta\sigma-\beta+2\sigma^2+2\sigma)}{\beta^3(\sigma+1)^3}\xi^5+O(\xi^7).\] Consequently every nonzero center-manifold solution tending to the origin satisfies \[\xi(t)^{-2}=\frac{2\sigma}{\beta(\sigma+1)}t+\frac{2\beta\sigma-\beta+2\sigma^2+2\sigma}{\beta^2(\sigma+1)^2}\log t+C_\infty+o(1).\] For the standard Lorenz parameters \(\sigma=10\) and \(\beta=8/3\), this becomes \[x(t)^{-2}=\frac{15}{22}t+\frac{609}{1936}\log t+C_\infty+o(1).\] The cubic critical decay scale is classical; the accepted claim is the explicit classical three-dimensional quintic coefficient and the resulting first logarithmic correction in the physical \(x\)-amplitude.

## Assumptions and scope
The system is the classical three-dimensional Lorenz flow at \(\rho=1\), with \(\sigma>0\) and \(\beta>0\). The statement is local: it concerns a sufficiently smooth one-dimensional center manifold through the origin, parameterized by the physical coordinate \(x=\xi\), and nonzero trajectories on that manifold that converge to the origin as \(t\to\infty\). It does not assert a uniform asymptotic for all initial conditions or for the two-dimensional strong-stable manifold. Center manifolds need not be unique as sets, but their finite Taylor jet solving the invariance equation is fixed to the displayed order; flat differences do not alter the cubic, quintic, or logarithmic coefficients.

## Proof
At \(\rho=1\), the linearization at the origin has eigenvalues \(0\), \(-(\sigma+1)\), and \(-\beta\), so the center space is one-dimensional. The symmetry \((x,y,z)\mapsto(-x,-y,z)\) permits the graph
\[
y=\xi+A\xi^3+B\xi^5+O(\xi^7),\qquad
z=C\xi^2+D\xi^4+O(\xi^6).
\]
Since \(\dot\xi=\sigma(y-\xi)\), substitution into the two center-manifold invariance equations gives successively
\[
C=\frac1\beta,\qquad
A=-\frac1{\beta(\sigma+1)},
\]
\[
D=-\frac{\beta-2\sigma}{\beta^3(\sigma+1)},\qquad
B=-\frac{2\beta\sigma-\beta+2\sigma^2+2\sigma}{\beta^3(\sigma+1)^3}.
\]
Therefore
\[
\dot\xi=-c\xi^3+q\xi^5+O(\xi^7),
\]
where
\[
c=\frac{\sigma}{\beta(\sigma+1)}>0,\qquad
q=-\frac{\sigma(2\beta\sigma-\beta+2\sigma^2+2\sigma)}{\beta^3(\sigma+1)^3}.
\]
For a nonzero solution on the center manifold that tends to the origin, put \(W=\xi^{-2}\). Then
\[
\dot W=2c-\frac{2q}{W}+O(W^{-2}).
\]
The positive constant \(c\) first gives \(W=2ct+O(\log t)\). Hence
\[
\frac1W=\frac1{2ct}+O\!\left(\frac{\log t}{t^2}\right),
\]
and so
\[
\frac d{dt}\left(W-2ct+\frac qc\log t\right)
=O\!\left(\frac{\log t}{t^2}\right).
\]
The right-hand side is integrable. Thus the bracket converges and
\[
W(t)=2ct-\frac qc\log t+C_\infty+o(1),
\]
which is the stated formula. At \(\sigma=10\), \(\beta=8/3\), exact arithmetic gives
\[
C=\frac38,\quad A=-\frac3{88},\quad D=\frac{117}{1408},\quad
B=-\frac{1827}{170368},
\]
\[
q=-\frac{9135}{85184},\qquad 2c=\frac{15}{22},\qquad -\frac qc=\frac{609}{1936}.
\]

## Verification
The accompanying `verify.py` uses only Python's standard-library exact rational arithmetic. It checks the center-manifold invariance equations through the required orders at the standard Lorenz parameters and verifies the exact coefficients \(15/22\) and \(609/1936\). Its recorded output is `VERIFY_OK`. The asymptotic step is analytic and follows from the displayed scalar equation for \(W\); no finite numerical trajectory is used as evidence for an infinite-time statement.

## Relationship to prior work
Lorenz's 1963 article introduced the classical three-variable system. A fully inspected modern treatment, *How to compute invariant manifolds and their reduced dynamics in high-dimensional finite element models* (DOI 10.1007/s11071-021-06957-4), uses the classical Lorenz equations at \(\rho=1\) and computes the center-manifold reduced dynamics through cubic order. That establishes a close same-object comparison but does not state the quintic coefficient or logarithmically corrected relaxation law above.

A published SCOPE record on the five-dimensional Lorenz extension, `2026/10/4/SCOPE-first-logarithmic-correction-to-critical-relaxation-in-the-five--d722eecc3b3c`, obtains a logarithmic correction by a quintic center-manifold calculation for a different vector field with two additional modes. Its standard-parameter logarithmic coefficient is \(9393/36784\), whereas the classical three-dimensional coefficient here is \(609/1936\). The two claims therefore share a method and leading cubic mechanism but neither statement implies the other.

Exact and synonymous searches for the classical Lorenz system, \(\rho=1\), fifth-order center manifolds, critical relaxation, and the coefficient \(609/1936\) did not locate a prior statement of this three-dimensional formula. A same-family mathematical article, *Homoclinic orbits and chaos in the generalized Lorenz system* (DOI 10.3934/dcdsb.2019210), lists primary MSC 34C37, which is the classification used here.

## Limitations
The originality conclusion is to the best of the checked published evidence, not a proof that no unpublished or unindexed derivation exists. The original Lorenz article was verified bibliographically at the publisher, but its full text was not retrievable through the checked route; the same-object 2022 article was inspected in full and gives the relevant cubic comparison. The result is local at \(\rho=1\), does not quantify the size of the center-manifold neighborhood, and does not describe chaotic dynamics for larger \(\rho\). The constant \(C_\infty\) depends on the trajectory, while the linear and logarithmic coefficients are fixed by the center-manifold jet.

## References
1. E. N. Lorenz, *Deterministic Nonperiodic Flow*, Journal of the Atmospheric Sciences 20 (1963), 130–141. DOI: 10.1175/1520-0469(1963)020<0130:DNF>2.0.CO;2. First published 1963-03-01.
2. *How to compute invariant manifolds and their reduced dynamics in high-dimensional finite element models*. Nonlinear Dynamics (2022). DOI: 10.1007/s11071-021-06957-4.
3. *Homoclinic orbits and chaos in the generalized Lorenz system*. Discrete and Continuous Dynamical Systems - B. DOI: 10.3934/dcdsb.2019210.
4. *First logarithmic correction to critical relaxation in the five-dimensional Lorenz model*. Published SCOPE record `2026/10/4/SCOPE-first-logarithmic-correction-to-critical-relaxation-in-the-five--d722eecc3b3c`.
