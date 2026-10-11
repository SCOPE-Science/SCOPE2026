# Sharp stationary transport strip for the Zaslavsky map
## Finding
Consider the classical dissipative Zaslavsky map on \(\mathbb T\times\mathbb R\), written with \(q=e^{-r}\), \(r>0\), \(\nu>0\), \(\varepsilon>0\), and \(\eta=(1-q)/r\):
\[
y_{n+1}=q\bigl(y_n+\varepsilon\cos(2\pi x_n)\bigr),
\]
\[
x_{n+1}=x_n+\nu(1+\eta y_n)+\varepsilon\nu\eta\cos(2\pi x_n)\pmod 1.
\]
For the canonical lift \(X_n\in\mathbb R\), set \(\Delta_n=X_{n+1}-X_n\). Then every trajectory obeys the exact pointwise transport identity
\[
\Delta_n=\nu+\kappa y_{n+1},\qquad
\kappa=\frac{\nu(e^r-1)}{r},
\]
and hence, for every \(N\ge1\),
\[
X_N-X_0-N\nu=\kappa\sum_{j=1}^N y_j.
\]
If \(\pi\) is any compactly supported invariant Borel probability measure, then
\[
|y|\le \frac{q\varepsilon}{1-q}\quad\text{for }\pi\text{-almost every }(x,y),
\]
so its measure drift
\[
\rho(\pi)=\int \Delta_0\,d\pi
\]
satisfies the sharp strip
\[
\nu-\frac{\nu\varepsilon}{r}\le \rho(\pi)\le
\nu+\frac{\nu\varepsilon}{r}.
\]
Writing \(c=\int\cos(2\pi x)\,d\pi\), the drift is calibrated exactly by
\[
\rho(\pi)=\nu+\frac{\nu\varepsilon}{r}c.
\]
Moreover the entire one-step lift-increment distribution is the affine image of the stationary \(y\)-marginal: for every bounded Borel function \(\Phi\),
\[
\int \Phi(\Delta_0)\,d\pi=
\int \Phi(\nu+\kappa y)\,d\pi.
\]
Consequently, for stationary initial data and every \(N\ge1\),
\[
\operatorname{Var}(X_N-X_0)=
\kappa^2\operatorname{Var}\!\left(\sum_{j=1}^N y_j\right).
\]
The upper drift endpoint is attained exactly when \(\nu+\nu\varepsilon/r\in\mathbb Z\), in which case the attaining invariant measure is the Dirac mass at
\[
\left(0,\frac{q\varepsilon}{1-q}\right).
\]
The lower endpoint is attained exactly when \(\nu-\nu\varepsilon/r\in\mathbb Z\), in which case the attaining invariant measure is the Dirac mass at
\[
\left(\frac12,-\frac{q\varepsilon}{1-q}\right).
\]
In particular every non-Dirac compactly supported invariant measure has strict drift inequalities.

## Assumptions and scope
The torus coordinate is represented by the canonical lift in the displayed map. The measure \(\pi\) is assumed invariant and compactly supported; compact support is used only to justify the stationary support bound without additional integrability hypotheses. The quantity \(\rho(\pi)\) is the mean lift displacement. If \(\pi\) is ergodic, Birkhoff's theorem additionally identifies \(\rho(\pi)\) with the almost-sure long-time lift velocity. No claim is made about existence of a diffusion coefficient or a central limit theorem.

## Proof
Since \(q=e^{-r}\) and \(\eta=(1-q)/r\), the second coordinate gives
\[
y_{n+1}=q\bigl(y_n+\varepsilon\cos(2\pi x_n)\bigr).
\]
The lifted first-coordinate increment is
\[
\Delta_n=\nu+\nu\eta\bigl(y_n+\varepsilon\cos(2\pi x_n)\bigr)
=\nu+\frac{\nu\eta}{q}y_{n+1}.
\]
Because \(\nu\eta/q=\nu(e^r-1)/r=\kappa\), this proves the pointwise identity and its finite-time sum.

Let \(K=\operatorname{supp}\pi\). Continuity and invariance imply \(F(K)=K\). If \(M=\max_K|y|\), then
\[
M\le q(M+\varepsilon),
\]
so \(M\le q\varepsilon/(1-q)\). Applying the pointwise lift identity on \(K\) gives
\[
\nu-\frac{\nu\varepsilon}{r}\le\Delta_n\le
\nu+\frac{\nu\varepsilon}{r},
\]
and integration yields the drift strip.

Invariance of the first moment of \(y\) gives, with \(\bar y=\int y\,d\pi\),
\[
(1-q)\bar y=q\varepsilon c.
\]
Using \(\rho(\pi)=\nu+\kappa\bar y\) therefore gives
\[
\rho(\pi)=\nu+\frac{\nu\varepsilon}{r}c.
\]
Since \(y_{n+1}\) and \(y_n\) have the same distribution under \(\pi\), the pointwise identity also proves the stated distributional identity and the finite-\(N\) variance identity.

If the upper mean-drift bound is an equality, then \(c=1\). Since \(\cos(2\pi x)\le1\), this forces \(x=0\pmod1\) almost surely. On that fiber the \(y\)-dynamics is the strict affine contraction \(y\mapsto q(y+\varepsilon)\); its only invariant probability measure is the Dirac mass at \(q\varepsilon/(1-q)\). Preservation of the fiber then requires the lift increment \(\nu+\nu\varepsilon/r\) to be an integer. Conversely that integer condition makes the displayed point a fixed point and its Dirac mass attains the upper bound. The lower endpoint is identical with \(x=1/2\), \(\cos(2\pi x)=-1\), and fixed \(y=-q\varepsilon/(1-q)\).

## Verification
The algebraic substitutions defining \(\kappa\), the stationary mean relation, and both endpoint increments were checked symbolically by the accompanying script `verify_zaslavsky.py`; its captured output is `ALGEBRA_OK`. The proof of the support bound and endpoint rigidity is analytic and does not rely on finite enumeration.

## Relationship to prior work
Zaslavsky's 1978 paper derives the dissipative kicked map and studies the onset and geometry of its strange attractor. Later work on the dissipative standard map studies the Hamiltonian-to-dissipative transition, periodic and quasi-periodic attractors, Arnold tongues, and transport including ballistic and superdiffusive regimes. The result here is different in statement: it is an exact measure-level and finite-time transport calibration, valid for every compact stationary state, with a sharp universal drift strip and complete endpoint rigidity. The commonly used external drift parameter in conformally symplectic formulations is not the same object as the realized mean lift displacement \(\rho(\pi)\) defined here.

## Limitations
The result is specific to the classical two-dimensional dissipative Zaslavsky normalization above. It does not establish existence, uniqueness, mixing, or regularity of any non-atomic invariant measure. It does not determine which interior drift values are realized, nor does it prove normal or anomalous diffusion. A highly relevant 2008 transport paper was available only through its abstract during the literature comparison; its inaccessible full text remains a residual overlap risk, although the abstract concerns numerical transport regimes rather than the exact universal identities proved here.

## References
1. G. M. Zaslavsky, “The simplest case of a strange attractor,” *Physics Letters A* 69 (1978), 145–147. DOI: 10.1016/0375-9601(78)90195-0.
2. G. M. Zaslavsky, “Zaslavsky map,” *Scholarpedia* 2(5):2662 (2007). DOI: 10.4249/scholarpedia.2662.
3. G. Schmidt and B. W. Wang, “Dissipative standard map,” *Physical Review A* 32 (1985), 2994. DOI: 10.1103/PhysRevA.32.2994.
4. A. Celletti and S. Di Ruzza, “Periodic and quasi-periodic orbits of the dissipative standard map,” *Discrete and Continuous Dynamical Systems B* 16 (2011), 151–171. DOI: 10.3934/dcdsb.2011.16.151.
5. G. M. Zaslavsky and M. Edelman, “Superdiffusion in the dissipative standard map,” *Chaos* 18 (2008), 033116. DOI: 10.1063/1.2967851.
