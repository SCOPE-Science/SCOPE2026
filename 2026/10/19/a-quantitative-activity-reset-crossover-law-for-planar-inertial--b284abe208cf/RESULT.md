# A quantitative activity–reset crossover law for planar inertial active Brownian motion

## Finding

For a completely reset, two-dimensional inertial active Brownian particle, the competition between thermal acceleration and self-propulsion has a distinguished joint limit as the reset rate \(r\to\infty\) and the propulsion strength \(\mathrm{Pe}_r\) grows on the scale \(\sqrt r\). Unlike an approximation based on second or fourth moments, the result determines the **entire planar limiting law**, including its anisotropic correlations, with a quantitative Wasserstein bound.

Fix \(M>0\) and let \(\alpha_r=\mathrm{Pe}_r/\sqrt r\). At stationarity write \(X_r\in\mathbb R^2\) for the position, and \(Y_r=Mr^{3/2}X_r\). For every sequence \(\alpha_r\to\alpha\in[0,\infty)\),
\[
Y_r\xrightarrow{W_2}Y_\alpha:=\frac{\alpha E^2}{2}e_1+\sqrt2\int_0^E(E-z)\,dB_z,
\]
where \(E\sim\mathrm{Exp}(1)\), \(B\) is independent standard planar Brownian motion, and \(e_1=(1,0)\). More precisely, at every \(r>0\),
\[
W_2(\mathcal L(Y_r),\mathcal L(Y_\alpha))\le
\sqrt6\lvert\alpha_r-\alpha\rvert+
\frac{16\sqrt{15}\,\alpha}{15\sqrt r}+
\frac{2\sqrt5\,\alpha+2\sqrt6}{Mr}.
\tag{1}
\]
The convergence also holds for every fixed polynomial moment. The limit has the explicit conditional Gaussian representation
\[
Y_\alpha\mid E=s\ \sim\ N_2\left(\left(\tfrac{\alpha s^2}{2},0\right),\tfrac{2s^3}{3}I_2\right), \qquad s>0.
\]
Consequently its characteristic function and (almost-everywhere) density are
\[
\Phi_\alpha(k_1,k_2)=\int_0^\infty\! e^{-s+i\alpha s^2k_1/2-s^3(k_1^2+k_2^2)/3}\,ds,
\]
\[
f_\alpha(x,y)=\int_0^\infty \frac{3e^{-s}}{4\pi s^3}
\exp\left[-\frac{3((x-\alpha s^2/2)^2+y^2)}{4s^3}\right]ds.
\]
(The density may diverge at the reset point, which is a measure-zero location.) In particular,
\[
\mathbb E Y_\alpha=(\alpha,0),\quad
\operatorname{Cov}(Y_\alpha)=\operatorname{diag}(4+5\alpha^2,4),\quad
\mathbb E\lvert Y_\alpha\rvert^2=8+6\alpha^2,
\]
\[
\mathbb E[(Y_{\alpha,1}-\alpha)^3]=108\alpha+74\alpha^3,
\qquad
\mathbb E[(Y_{\alpha,1}-\alpha)Y_{\alpha,2}^2]=36\alpha.
\]
If \(\alpha_r\to\infty\), the thermal scale is no longer tight; instead
\[
\frac{Mr^2}{\mathrm{Pe}_r}X_r\longrightarrow \frac{E^2}{2}e_1
\]
in every fixed \(L^p\) under the coupling below. Thus the scale \(\mathrm{Pe}_r\asymp\sqrt r\) separates thermal-dominated, genuinely mixed, and propulsion-dominated reset profiles.

## Assumptions and scope

Between complete resets, the dimensionless stochastic differential equations are
\[
dX_t=V_t\,dt,\qquad M\,dV_t=(-V_t+\mathrm{Pe}_r U_t)\,dt+\sqrt2\,dB_t,
\qquad d\theta_t=\sqrt2\,dW_t,
\]
where \(U_t=(\cos\theta_t,\sin\theta_t)\), the planar Brownian motion \(B\) and scalar Brownian motion \(W\) are independent, and every reset sets \((X,V,\theta)=(0,0,0)\). Independent Poisson resets have rate \(r>0\). Parameters: fixed \(M>0\), arbitrary nonnegative \(\mathrm{Pe}_r\), no rotational inertia, and independent Gaussian thermal and angular noises. The reset orientation is **fixed along \(e_1\)**, not uniform. For the limit, \(r\to\infty\) with the specified activity ratio. The stationary state exists by regeneration.

## Proof

**Exact renewal representation.** At stationarity the time \(T\) since the last complete reset is independent exponential with rate \(r\). Starting from zero velocity and position, stochastic convolution of the free inertial equation gives
\[
X(T)=\mathrm{Pe}_r\!\int_0^T\![1-e^{-(T-t)/M}]U_t\,dt+
\sqrt2\int_0^T\![1-e^{-(T-t)/M}]\,dB_t.
\tag{2}
\]
Set \(E=rT\), rescale the noises by Brownian scaling, and write
\[
h_{r,M}(w)=Mr(1-e^{-w/(Mr)}),\qquad
U_r(z)=(\cos(\sqrt{2/r}W_z),\sin(\sqrt{2/r}W_z)).
\]
On a shared probability space, (2) becomes the exact equality in distribution
\[
Y_r=\alpha_r\int_0^E h_{r,M}(E-z)U_r(z)\,dz+
\sqrt2\int_0^E h_{r,M}(E-z)\,dB_z.
\tag{3}
\]
The same \(E,B,W\) can be used for every reset rate. In particular \(E\) is independent of the Brownian motions.

**Deterministic and orientation errors.** For \(w\ge0\), elementary Taylor inequalities show
\[
0\le w-h_{r,M}(w)\le\frac{w^2}{2Mr}, \qquad
\lvert U_r(z)-e_1\rvert\le\sqrt{2/r}\lvert W_z\rvert.
\tag{4}
\]
The \(L^2\)-norm of the coefficient-change term in (3) is at most
\(\lvert\alpha_r-\alpha\rvert\{\mathbb E(E^4/4)\}^{1/2}=\sqrt6\lvert\alpha_r-\alpha\rvert\).
For the orientation term, condition on \(E=s\) and apply the triangle inequality in \(L^2(W)\):
\[
\left\|\int_0^s(s-z)(U_r(z)-e_1)\,dz\right\|_2
\le\sqrt{2/r}\int_0^s(s-z)\sqrt z\,dz
=\frac{4\sqrt{2}}{15\sqrt r}s^{5/2}.
\]
Averaging over exponential \(E\), with \(\mathbb E E^5=120\), yields \(16\sqrt{15}\,\alpha/(15\sqrt r)\). For the deterministic active kernel defect, (4) gives \(\alpha E^3/(6Mr)\), whose \(L^2\) norm is \(2\sqrt5\,\alpha/(Mr)\) because \(\mathbb E E^6=720\). For the thermal kernel defect, two-dimensional Itô isometry gives
\[
\mathbb E\left\lvert\sqrt2\int_0^E\bigl(h_{r,M}(E-z)-(E-z)\bigr)dB_z\right\rvert^2
\le\frac{\mathbb E E^5}{5M^2r^2}=\frac{24}{M^2r^2}.
\]
Adding the four \(L^2\) error bounds proves (1), since the Wasserstein distance is bounded by the root-mean-square distance under any coupling.

**Limiting law and moments.** Conditional on \(E=s\), the Brownian integral is centered Gaussian with covariance \(2s^3I_2/3\). Integrating its Gaussian characteristic function and density against \(e^{-s}ds\) gives the displayed formulas. Exponential factorial moments \(\mathbb E E^j=j!\) give the stated variance, third-cumulant and mixed-moment identities. The bounds \(h_{r,M}(w)\le w\), \(\lvert U_r\rvert=1\), and Itô/BDG inequalities control moments of every fixed order by powers of \(E\), which all have finite expectation. Thus the common coupling yields \(L^p\) convergence and moment convergence for all finite \(p\) when \(\alpha_r\to\alpha\).

**Above crossover.** If \(\alpha_r\to\infty\), divide (3) by \(\alpha_r\). The orientation and kernel errors tend to zero in every \(L^p\), and the thermal stochastic convolution divided by \(\alpha_r\) tends to zero. The limit is \(E^2e_1/2\); this has strictly positive magnitude almost surely, proving that \(\lvert Y_r\rvert\to\infty\) in probability on the original thermal scale.

## Verification

The included standalone standard-library program `verify.py` independently evaluates the finite-reset passive propagator, compares it with the published finite-parameter mean-square displacement formula, verifies the factorial limit identities, checks large-reset asymptotics in the mixed and propulsion-dominated regimes, tests the deterministic kernel bound on a finite grid, and simulates complete reset excursions with independent Brownian angular and translational noises. A successful execution prints its own exact assertion count. The program supplies reproducible finite tests; it is **not** used as a substitute for the proof of convergence or the bound.

## Relationship to prior work

Patel and Shee [1] give the complete-reset dynamics, the exact finite-rate stationary second/fourth scalar moments, and the \(r^{-3}\) stationary position mean-square suppression at fixed activity. Their Eq. (7), a finite-rate second-moment identity, is re-used here only as a check. The current result treats a **joint** high-reset and high-activity limit, gives the full limiting planar probability law and a quantitative \(W_2\) comparison, and separates the three activity scalings. It does not claim the source's renewal dynamics, finite-rate moments, or resetting model as new. Franke and Sokolov [2] analyze inertial passive resetting; Singh [3] considers a random acceleration process with resetting, and Kumar, Sadekar and Basu [4] study the overdamped planar active problem. Their stated scopes do not directly provide the inertial active joint-scaling law above. Possible coverage by more general stochastic-convolution limit theory remains a scientific originality risk.

## Limitations

The result is for exact full-state Poisson resetting to a fixed orientation, fixed positive inertia, isotropic independent Brownian thermal forcing and angular diffusion, and the stationary one-time position law. It does not cover position-only resetting, random reset orientations, resetting of only a subset of variables, rotational inertia, joint position–velocity distributions, first-passage statistics, or finite-data parameter inference. The stationary density is a singular Gaussian mixture near the reset point. The limiting mixed profile is generally non-Gaussian; a Gaussian approximation matching its variance would miss its third moments. This mathematical work has not received independent audit.

## References

[1] M. Patel and A. Shee, *Controlling inertial active Brownian motion via stochastic resetting*, arXiv:2602.21134 (first public February 24, 2026; v2 October 11, 2026), https://arxiv.org/html/2602.21134v2 and https://arxiv.org/abs/2602.21134.

[2] H. Franke and I. M. Sokolov, *Resetting of underdamped Brownian motion*, Physical Review E **113**, 064125 (2026), DOI 10.1103/qyl8-6q9h.

[3] P. Singh, *Random acceleration process under stochastic resetting*, arXiv:2007.05576 (2020).

[4] V. Kumar, O. Sadekar and U. Basu, *Active Brownian Motion in two-dimensions under Stochastic Resetting*, arXiv:2008.03294 (2020).
