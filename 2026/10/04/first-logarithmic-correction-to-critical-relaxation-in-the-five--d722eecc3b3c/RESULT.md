# First logarithmic correction to critical relaxation in the five-dimensional Lorenz model
## Finding
Consider the five-dimensional Lorenz system
\[
\dot x=\sigma(y-x),\qquad
\dot y=-xz+rx-y,
\]
\[
\dot z=xy-xy_1-bz,\qquad
\dot y_1=xz-2xz_1-dy_1,\qquad
\dot z_1=2xy_1-4bz_1,
\]
with \(\sigma,b,d>0\). At the first critical Rayleigh value \(r=1\), parameterize a sufficiently smooth local center manifold by the physical first amplitude \(x=\xi\). Its Taylor jet through the orders needed below is
\[
y=\xi-\frac{\xi^3}{b(\sigma+1)}+B\xi^5+O(\xi^7),
\]
\[
z=\frac{\xi^2}{b}+D\xi^4+O(\xi^6),\qquad
y_1=\frac{\xi^3}{bd}+G\xi^5+O(\xi^7),\qquad
z_1=\frac{\xi^4}{2b^2d}+O(\xi^6),
\]
where
\[
B=\frac{-2bd\sigma+bd+b\sigma^2+2b\sigma+b-2d\sigma^2-2d\sigma}{b^3d(\sigma+1)^3},\qquad D=-\frac{bd+b\sigma+b-2d\sigma}{b^3d(\sigma+1)},\qquad G=\frac{-bd+b\sigma-2b+2d\sigma}{b^3d^2(\sigma+1)}.
\]
Therefore
\[
\dot\xi=-c\xi^3+q\xi^5+O(\xi^7),\qquad c=\frac{\sigma}{b(\sigma+1)},
\]
with
\[
q=\frac{\sigma(-2bd\sigma+bd+b\sigma^2+2b\sigma+b-2d\sigma^2-2d\sigma)}{b^3d(\sigma+1)^3}.
\]
Every nonzero center-manifold solution that tends to the origin as \(t\to\infty\) consequently has
\[
\xi(t)^{-2}=2ct-\frac{q}{c}\log t+C+o(1).
\]
For \(\sigma=10\), \(b=8/3\), and \(d=19/3\),
\[
c=\frac{15}{44},\qquad q=-\frac{140895}{1618496},
\]
and hence
\[
\xi(t)^{-2}=\frac{15}{22}t+\frac{9393}{36784}\log t+C+o(1).
\]
The leading cubic term, and therefore the leading \(t^{-1/2}\) scale, is implicit in the previously published first-transition normal form. The logarithmic coefficient requires the quintic center-manifold jet. In particular, the higher-mode damping \(d\) is absent from the leading coefficient \(c\) but enters the first logarithmic correction.

## Assumptions and scope
The statement concerns the classical integer-order autonomous system above with strictly positive \(\sigma\), \(b\), and \(d\), exactly at \(r=1\). The asymptotic formula is local and applies to nonzero trajectories on a local center manifold that converge to the origin. It does not assert a uniform rate for the four-dimensional strong-stable manifold or for finite-time transients far from the origin. Center manifolds need not be unique as sets, but their finite Taylor jet solving the invariance equation is fixed to the displayed orders; flat differences do not alter the stated coefficients or asymptotic law.

## Proof
At \(r=1\), the linearization has one zero eigenvalue and four strictly negative eigenvalues. Since the center eigenvector has nonzero first component, a local center manifold may be written as a graph over \(x=\xi\). The symmetry \((x,y,z,y_1,z_1)\mapsto(-x,-y,z,-y_1,z_1)\) gives the parity ansatz
\[
y=\xi+A\xi^3+B\xi^5+O(\xi^7),\quad z=C\xi^2+D\xi^4+O(\xi^6),
\]
\[
y_1=F\xi^3+G\xi^5+O(\xi^7),\quad z_1=H\xi^4+O(\xi^6).
\]
Writing \(\dot\xi=\sigma(y-\xi)=p\xi^3+q\xi^5+O(\xi^7)\), the center-manifold invariance equations give, successively,
\[
C=\frac1b,\qquad A=-\frac1{b(\sigma+1)},\qquad p=\sigma A=-\frac{\sigma}{b(\sigma+1)},
\]
\[
F=\frac1{bd},\qquad H=\frac1{2b^2d},
\]
\[
D=-\frac{bd+b\sigma+b-2d\sigma}{b^3d(\sigma+1)},\qquad
B=\frac{-2bd\sigma+bd+b\sigma^2+2b\sigma+b-2d\sigma^2-2d\sigma}{b^3d(\sigma+1)^3},\qquad
G=\frac{-bd+b\sigma-2b+2d\sigma}{b^3d^2(\sigma+1)}.
\]
Thus \(q=\sigma B\), which is the displayed quintic coefficient.

For a nonzero center-manifold solution converging to zero, put \(W=\xi^{-2}\). Since \(c=-p>0\),
\[
\dot W=2c-\frac{2q}{W}+O(W^{-2}).
\]
First this implies \(W=2ct+O(\log t)\). Substitution back into the right-hand side gives
\[
\frac{d}{dt}\left(W-2ct+\frac{q}{c}\log t\right)=O\!\left(\frac{\log t}{t^2}\right),
\]
which is integrable. Hence that bracket converges to a finite constant \(C\), proving
\[
W=2ct-\frac{q}{c}\log t+C+o(1).
\]
Exact substitution of \(\sigma=10\), \(b=8/3\), \(d=19/3\) yields the stated rational coefficients.

## Verification
The accompanying `verify.py` reconstructs the center-manifold ansatz symbolically, substitutes it into all five invariance equations, checks that the determining coefficients vanish at the required orders, verifies \(q=\sigma B\), and checks the exact rational specialization \(2c=15/22\) and \(-q/c=9393/36784\). The analytic asymptotic step uses only the displayed scalar differential equation and the integrability of \(O((\log t)/t^2)\).

## Relationship to prior work
Zhang and Deng derive the same five-dimensional Lorenz system, identify \(r=1\) as the first transition, prove global asymptotic stability of the origin at the critical value, and reduce the first transition to a cubic center-manifold equation. Their center coordinate is the coefficient of the eigenvector \(e_1=(\sigma,\sigma,0,0,0)\) at \(r=1\); converting to the physical amplitude \(x\) gives exactly the cubic coefficient \(-\sigma/[b(\sigma+1)]\) above. Their first-transition calculation stops at the cubic term and does not provide the quintic coefficient or a logarithmically corrected critical relaxation law. Mao et al. subsequently study the same model's numerical regimes, Hamilton energy, attractive sets, bounds, and synchronization, but do not supply this critical asymptotic. Shen's original five-dimensional model analyzes critical points and stability but likewise does not provide the quintic critical-relaxation coefficient.

The new content is therefore not the known threshold \(r=1\), the known global stability there, or the leading cubic normal form. It is the explicit quintic coefficient in the physical amplitude and the induced logarithmic correction, including the structural fact that \(d\) first enters the critical relaxation at that subleading order.

## Limitations
The finding is an asymptotic local statement at one distinguished parameter surface. It does not quantify the size of a center-manifold neighborhood, give a uniform entrance time from the global basin, or analyze the later Hopf transition and chaotic regime. Generic center-manifold theory explains why the calculation is possible, but the coefficient itself is model-specific. A broad search found no same-model publication or database record stating the displayed quintic or logarithmic coefficient; this is evidence of noncoverage, not a proof that no unpublished or unindexed derivation exists.

## References
1. D. Zhang and D. Deng, “Dynamical transition and chaos for a five-dimensional Lorenz model,” *Mathematical Methods in the Applied Sciences* 45 (2022), 1612–1631. DOI: 10.1002/mma.7877. First published 2021-11-03.
2. X. Mao, H. Feng, M. A. Al-Towailb, and H. Saberi-Nik, “Dynamical analysis and boundedness for a generalized chaotic Lorenz model,” *AIMS Mathematics* 8 (2023), 19719–19742. DOI: 10.3934/math.20231005.
3. B.-W. Shen, “Nonlinear Feedback in a Five-Dimensional Lorenz Model,” *Journal of the Atmospheric Sciences* 71 (2014), 1701–1723. DOI: 10.1175/JAS-D-13-0223.1.
