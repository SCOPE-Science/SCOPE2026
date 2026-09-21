# Closed energy-stability boundary for Lorenz-96-like quadratic advection

## Result

Let \(\mathbf e=(1,\ldots,1)^T\in\mathbb R^N\). Let
\(G:\mathbb R^N\to\mathbb R^N\) be quadratic, energy-preserving, and equivariant
under cyclic coordinate shifts:
\[
x^T G(x)=0,\qquad G(\rho x)=\rho G(x).
\]
Consider the homogeneous forced-damped system
\[
\dot x=G(x)-x+F\mathbf e,\qquad F\in\mathbb R.
\]
Equivariance and energy preservation imply \(G(\lambda\mathbf e)=0\), so
\(x_F=F\mathbf e\) is an equilibrium. Write \(A=DG(\mathbf e)\). Since \(A\) is
real circulant, let
\[
r_k=\Re\lambda_k(A),\qquad 0\le k<N.
\]

**Theorem.** The equilibrium \(F\mathbf e\) is globally asymptotically stable if
and only if
\[
\max_{0\le k<N}\bigl(F r_k-1\bigr)\le 0.
\]
If the inequality is strict, then every solution satisfies the global exponential
estimate
\[
\|x(t)-F\mathbf e\|_2
\le
e^{-\eta(F)t}\|x(0)-F\mathbf e\|_2,
\qquad
\eta(F)=1-\max_k F r_k>0.
\]
If equality holds, \(F\mathbf e\) is still globally asymptotically stable even
though the linearization has spectral abscissa zero. Hence the closed
energy-stability boundary, not merely its interior, contains no nontrivial compact
recurrent dynamics.

The strict part of this statement is already contained in Proposition 1 of
Kerin--Engler for Lorenz-96-like \(G\)-maps. The contribution here is the
nonhyperbolic equality case and the resulting exact local/global stability
criterion.

## Proof

Set \(y=x-F\mathbf e\). Quadraticity and \(G(\mathbf e)=0\) give
\[
G(F\mathbf e+y)=F Ay+G(y),
\]
and therefore
\[
\dot y=G(y)+(FA-I)y.
\]
With
\[
S=\frac{A+A^T}{2},\qquad H=I-FS,
\]
energy preservation gives the exact identity
\[
\frac12\frac{d}{dt}\|y\|_2^2=-y^T H y. \tag{1}
\]

Because \(A\) is circulant, it is unitarily diagonalizable by the discrete Fourier
transform, and the eigenvalues of \(S\) are precisely \(r_k\). Thus
\(H\succeq0\) exactly when \(Fr_k\le1\) for every \(k\). If all inequalities are
strict, \(H\succeq\eta(F)I\), and (1) gives the stated exponential estimate.

It remains to treat the boundary case \(H\succeq0\) with \(\ker H\ne\{0\}\).
A second identity forced by energy preservation supplies the missing strictness.
For any \(z\),
\[
0=(\mathbf e+\varepsilon z)^TG(\mathbf e+\varepsilon z).
\]
Since
\[
G(\mathbf e+\varepsilon z)=\varepsilon Az+\varepsilon^2G(z),
\]
comparison of the \(\varepsilon\) and \(\varepsilon^2\) coefficients gives
\[
\mathbf e^TA=0,\qquad
\mathbf e^TG(z)=-z^TAz. \tag{2}
\]
Also \(A\mathbf e=0\), hence \(S\mathbf e=0\) and \(H\mathbf e=\mathbf e\).

Let
\[
Z=\{y:y^THy=0\}=\ker H.
\]
For \(y\in Z\), symmetry of \(H\) and \(H\mathbf e=\mathbf e\) imply
\[
\mathbf e^Ty=(H\mathbf e)^Ty=\mathbf e^THy=0.
\]
At a nonzero \(y\in Z\), equality \(Hy=0\) gives
\[
y^TSy=\frac{\|y\|_2^2}{F},
\]
where \(F\ne0\) in the boundary case. Since \(y^TAy=y^TSy\), (2) yields
\[
\left.\frac{d}{dt}\mathbf e^Ty\right|_{y}
=
\mathbf e^TG(y)+F\mathbf e^TAy-\mathbf e^Ty
=
-\frac{\|y\|_2^2}{F}\ne0. \tag{3}
\]
Therefore no nonzero trajectory can remain entirely in \(Z\): every nonzero
zero-dissipation state instantaneously generates the damped mean mode. The largest
invariant subset of \(Z\) is \(\{0\}\). Equation (1) makes every sublevel set of
\(\|y\|_2^2\) positively invariant and compact, so LaSalle's invariance principle
gives \(y(t)\to0\) for every initial condition. Equation (1) also gives Lyapunov
stability, hence global asymptotic stability.

Conversely, if some \(Fr_k-1>0\), the circulant linearization \(FA-I\) has an
eigenvalue with positive real part, so \(F\mathbf e\) is unstable. This proves the
equivalence.

## Standard Lorenz-96 corollary

For
\[
\dot x_j=x_{j-1}(x_{j+1}-x_{j-2})-x_j+F
\quad (j\ {\rm mod}\ N,\ N\ge4),
\]
the linearization of the quadratic advection at \(\mathbf e\) has Fourier symbol
\[
p(\theta)=e^{i\theta}-e^{-2i\theta},
\]
so
\[
s(\theta):=\Re p(\theta)=\cos\theta-\cos2\theta
=\frac98-2\left(\cos\theta-\frac14\right)^2.
\]
Define
\[
\alpha_N=\max_{0\le k<N}s(2\pi k/N),\qquad
\beta_N=\min_{0\le k<N}s(2\pi k/N).
\]
Then the homogeneous equilibrium is globally asymptotically stable exactly for
\[
\boxed{\frac1{\beta_N}\le F\le\frac1{\alpha_N}},
\]
and convergence is global exponential in the open interval.

The endpoints have explicit forms
\[
\alpha_N=\frac98-2\delta_N^2,\qquad
\delta_N=\min_{0\le k<N}
\left|\cos\frac{2\pi k}{N}-\frac14\right|,
\]
and
\[
\beta_N=
\begin{cases}
-2,&N\ \text{even},\\[2mm]
-\left(\cos\frac{\pi}{N}+\cos\frac{2\pi}{N}\right),&N\ \text{odd}.
\end{cases}
\]
Thus the familiar dimension-uniform band
\[
-\frac12\le F\le\frac89
\]
lies inside the global stability region for every finite \(N\ge4\). More
importantly, at each *finite-\(N\) exact* first linear-stability boundary, the
equilibrium remains globally attracting at the critical parameter itself; only
after the boundary is crossed can the equilibrium become unstable.

For positive forcing, the first instability beyond the upper endpoint is the
Hopf or Hopf--Hopf mechanism studied in the Lorenz-96 bifurcation literature.
The theorem therefore rules out a hidden finite-amplitude attractor at or before
that first linear threshold.

## Context and originality

Lorenz introduced the model as a predictability test system, and Lorenz--Emanuel
made the 40-variable version a standard benchmark. Later bifurcation work
identified the circulant linear spectrum and the first Hopf bifurcations.

The closest prior result is Kerin--Engler, *On the Lorenz '96 model and some
generalizations*. Their Proposition 1 uses the same centered Euclidean energy and
proves global asymptotic stability under the **strict** conditions
\(Fp_+<1\) and \(Fp_-<1\). Their paper also treats the Fourier spectrum, special
all-forcing-stable advections, and small-forcing stability for inhomogeneous
extensions. The equality case is not included in that proposition. The argument
above closes those marginal cases by combining LaSalle's principle with the
polarized identity \(\mathbf e^TG(y)=-y^TAy\), and consequently turns the strict
sufficient condition into an exact if-and-only-if global criterion for the
homogeneous \(G\)-map class.

Searches for Lorenz-96 global stability, energy stability, marginal stability,
nonhyperbolic stability, and the first bifurcation threshold did not locate this
closed-boundary statement. To the best of our knowledge, the endpoint theorem and
the exact global/local equivalence above are not stated in the inspected
literature.

## Limitations

The result concerns homogeneous forcing and unit homogeneous damping in the
\(G\)-map form \(\dot x=G(x)-x+F\mathbf e\). It uses exact quadratic energy
preservation and cyclic equivariance. It does not provide a quantitative decay
rate at a marginal endpoint, and it does not describe dynamics after the
stability boundary is crossed.

The strict-interior global stability theorem is prior work and is not claimed as
new here. The new claim is narrow: closure of the global stability region at the
nonhyperbolic endpoint and the consequent exact equivalence with absence of a
positive-real-part linear mode. Because the proof uses ingredients already present
near one another in the Lorenz-96 literature, an implicit or unindexed earlier
observation remains a residual originality risk.

## References

1. E. N. Lorenz, *Predictability: A Problem Partly Solved*, ECMWF Seminar on
   Predictability, 1995.
   https://www.ecmwf.int/en/elibrary/75462-predictability-problem-partly-solved

2. E. N. Lorenz and K. A. Emanuel, *Optimal Sites for Supplementary Weather
   Observations: Simulation with a Small Model*, Journal of the Atmospheric
   Sciences 55 (1998), 399--414.
   https://doi.org/10.1175/1520-0469(1998)055%3C0399:OSFSWO%3E2.0.CO;2

3. D. L. van Kekem and A. E. Sterk, *Travelling waves and their bifurcations in
   the Lorenz-96 model*, Physica D 367 (2018), 38--60.
   https://doi.org/10.1016/j.physd.2017.11.008

4. J. Kerin and H. Engler, *On the Lorenz '96 model and some generalizations*,
   Discrete and Continuous Dynamical Systems - B 27 (2022), 769--797.
   https://doi.org/10.3934/dcdsb.2021064
   Preprint: https://arxiv.org/abs/2005.07767
