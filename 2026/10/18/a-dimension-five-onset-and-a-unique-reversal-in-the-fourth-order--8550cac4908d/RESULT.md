# A dimension-five onset and a unique reversal in the fourth-order time arrow of a trapped run-and-tumble particle

## Finding

A harmonically confined particle with isotropically refreshed persistent propulsion has a stationary fourth-order temporal contrast that is always positive in dimensions one through four. Beginning in dimension five, sufficiently rapid orientation refresh makes the same contrast cross zero **exactly once**, from positive at short lag to negative at long lag. The critical refresh-to-confinement ratio is determined sharply for every integer spatial dimension.

Here is a complete quantitative statement. For integer \(d\ge1\), define the stationary dimensionless Cartesian coordinate \(Z_t\) under the generator in the following section, and the time-order contrast
\[
 A_{d,\alpha}(t)=\mathbb E[Z_t^3Z_0]-\mathbb E[Z_tZ_0^3],\qquad t>0.
\]
For \(d\le4\), this contrast is strictly positive for every \(\alpha>0\) and \(t>0\). For \(d\ge5\), put
\[
 \alpha_c(d)=\begin{cases}
 \dfrac{6}{d-4},&5\le d\le10,\\
 \dfrac{\sqrt{9(d-2)^2+12(d-1)(d+1)}-3(d-2)}{2(d-1)},&d\ge11.
 \end{cases}
\]
For \(0<\alpha\le\alpha_c(d)\), the contrast is strictly positive at **every finite positive lag**. For \(\alpha>\alpha_c(d)\), there exists a **unique** \(t_*(d,\alpha)>0\) with \(A_{d,\alpha}(t)>0\) for \(0<t<t_*\), \(A_{d,\alpha}(t_*)=0\), and \(A_{d,\alpha}(t)<0\) for all \(t>t_*\). The zero is simple. In particular the first possible reversal occurs in dimension five, at \(\alpha>6\); in dimension eleven the threshold is approximately \(0.978626204439\).

The complete unilateral Laplace transform is
\[
 \int_0^\infty e^{-st}A_{d,\alpha}(t)\,dt
 =\frac{12\alpha\bigl[(4-d)\alpha^2+3\alpha(s+3)+3(d+1)(s+1)\bigr]}
 {d^2(d+2)(\alpha+1)(\alpha+2)(\alpha+3)(s+\alpha)(s+1)(s+3)(s+\alpha+1)(s+\alpha+2)}
 \quad(s>0).
\]

## Assumptions and scope

Fix an integer \(d\ge1\), a confinement rate \(\kappa>0\), propulsion speed \(v>0\), and Poisson orientation-redraw rate \(\gamma>0\). In physical time the particle obeys the pathwise equation
\[
 \dot{\mathbf X}_t=-\kappa\mathbf X_t+v\mathbf n_t,
\]
where \(\mathbf n_t\) is piecewise constant and, independently at each rate-\(\gamma\) Poisson event, is replaced by a fresh uniform unit vector on \(S^{d-1}\). In dimension one, the sphere is the equally weighted pair \(\{-1,+1\}\). All noises driving successive directions and the Poisson clock are independent. There is no additional translational Brownian noise. Exponential contraction gives the unique joint stationary law.

Write \(\alpha=\gamma/\kappa\), measure time in units \(1/\kappa\), and set \(Z=\kappa X_1/v\), \(U=n_1\). A refresh draws \(U\) from the first-coordinate law of a uniform point on \(S^{d-1}\), whose second and fourth moments are \(h_2=1/d\) and \(h_4=3/[d(d+2)]\). The dimensional contrast equals \((v/\kappa)^4A_{d,\alpha}(\kappa t)\). The claim is for the stationary process and strictly positive finite lags, not for initialization at an orientation redraw.

## Proof

**Step 1: a closed polynomial generator.** The dimensionless generator on polynomials is
\[
 \mathcal Lf(z,u)=(u-z)\partial_z f(z,u)
 +\alpha\bigl(\mathbb E_{U'}f(z,U')-f(z,u)\bigr).
\]
Odd moments of a refreshed direction vanish. Stationarity applied to monomials gives
\[
 m_2=\mathbb E[Z^2]=\frac{h_2}{1+\alpha},\qquad
 m_4=\mathbb E[Z^4]
 =\frac{3(2h_4+\alpha h_2^2)}{(\alpha+1)(\alpha+2)(\alpha+3)},
\]
\[
 \mathbb E[Z^3U]=m_4,\quad
 \mathbb E[Z^2U^2]=\frac{\alpha+3}{3}m_4,\quad
 \mathbb E[ZU^3]=\frac{h_4}{\alpha+1},\quad
 \mathbb E[ZU]=m_2.
\]
The monomial column \(F=(z^3,z^2u,zu^2,u^3,z,u)^\mathsf T\) is invariant under the generator, with matrix
\[
 R=\begin{pmatrix}
 -3&3&0&0&0&0\\
 0&-2-\alpha&2&0&0&0\\
 0&0&-1-\alpha&1&\alpha h_2&0\\
 0&0&0&-\alpha&0&0\\
 0&0&0&0&-1&1\\
 0&0&0&0&0&-\alpha
 \end{pmatrix}.
\]
Consequently \(\mathbb E[Z_t^3Z_0]\) is the first coordinate of \(e^{Rt}e\), with
\[
 e=\left(m_4,m_4,\frac{\alpha+3}{3}m_4,
 \frac{h_4}{\alpha+1},m_2,m_2\right)^\mathsf T.
\]
For \(\mathbb E[Z_tZ_0^3]\), restrict to \((z,u)\), whose generator matrix is \(R_1=\left(\begin{smallmatrix}-1&1\\0&-\alpha\end{smallmatrix}\right)\) and initial vector \((m_4,m_4)^\mathsf T\). Resolvents \((sI-R)^{-1}\) and \((sI-R_1)^{-1}\), subtracting their first entries and substituting \(h_2,h_4\), give the displayed rational transform. This computation is reproducible by the accompanying verifier and also follows by backward substitution in the triangular systems.

**Step 2: a positive convolution and a monotone ratio.** Set
\[
 K=\frac{12\alpha}{d^2(d+2)(\alpha+1)(\alpha+2)(\alpha+3)},\qquad
 B=\alpha\bigl[6-(d-4)\alpha\bigr],\qquad H=3(\alpha+d+1).
\]
Let \(f_4\) be the convolution on \([0,\infty)\) of the four nonnegative functions \(e^{-\alpha t}\), \(e^{-3t}\), \(e^{-(\alpha+1)t}\), and \(e^{-(\alpha+2)t}\); write \(f_5=e^{-t}*f_4\). Decomposing the transform numerator as \(H(s+1)+B\) yields exactly
\[
 A_{d,\alpha}(t)=K\bigl[Hf_4(t)+Bf_5(t)\bigr]
 =Kf_4(t)\bigl[H+BR(t)\bigr],\qquad R(t)=f_5(t)/f_4(t).
\]
For \(t>0\), \(f_4(t)>0\). Each one-sided exponential is log-concave in its extended-real support, and convolution preserves log-concavity. Thus \(f_4\) is log-concave. The representation
\[
 R(t)=\int_0^t e^{-u}\frac{f_4(t-u)}{f_4(t)}\,du
\]
shows that \(R\) increases strictly: for each fixed \(0<u<t\), the ratio \(f_4(t-u)/f_4(t)\) is nondecreasing in \(t\) by concavity of \(\log f_4\), and increasing \(t\) adds a strictly positive interval of integration. Since \(f_4(t)\sim t^3/6\), \(R(0^+)=0\). Exponential-convolution tails give
\[
 \lim_{t\to\infty}R(t)=
 \begin{cases}1/(1-\alpha),&0<\alpha<1,\\+\infty,&\alpha\ge1.\end{cases}
\]
Indeed, for \(0<\alpha<1\), the unique slowest decay within \(f_4\) is \(e^{-\alpha t}\), and convolution with \(e^{-t}\) multiplies its tail coefficient by \(1/(1-\alpha)\). For \(\alpha\ge1\), the new \(e^{-t}\) factor is at least as slow as every factor in \(f_4\), making the ratio unbounded (including the equal-rate case).

**Step 3: exact phase boundary and simplicity.** If \(d\le4\), then \(B>0\), giving strict positivity. For \(d\ge5\), if \(B\ge0\), positivity persists. If \(B<0\), the function \(H+BR(t)\) decreases strictly from \(H>0\), and has precisely one zero if and only if its limiting value is negative. For \(\alpha\ge1\), the ratio diverges, so the condition is simply \(\alpha>6/(d-4)\), which yields the dimensions \(5\) through \(10\) thresholds. When \(0<\alpha<1\), the limiting-sign numerator is
\[
 (1-\alpha)H+B=3(d+1)-3(d-2)\alpha-(d-1)\alpha^2.
\]
For \(d\le10\) this expression is nonnegative on \((0,1)\); for \(d\ge11\) it has exactly one root inside \((0,1)\), given by the stated radical formula. At equality the finite-time value remains positive, since \(R(t)\) approaches its supremum strictly from below. Whenever the limiting value is negative, the strict increase of \(R\) gives exactly one crossing, and its derivative is negative there because \(B<0\) and \(R'(t)>0\) for positive finite \(t\). This proves the complete classification.

The small-lag expansion supplies the independent positivity check
\[
 A_{d,\alpha}(t)=\frac{K(\alpha+d+1)}2t^3+O(t^4).
\]

## Verification

Run `python3 verify.py` with Python, SymPy, NumPy, and SciPy. The standalone checker reconstructs both resolvents from the displayed generator matrices; symbolically verifies the exact rational transform and its convolution decomposition; checks the dimension-threshold inequalities for twenty-two integer dimensions; and independently compares twelve finite-lag parameter sets via numerical matrix exponentials. The analytic argument above, not numerical sampling, proves every infinite-parameter statement and the uniqueness of the crossing.

## Relationship to prior work

Frydel's 2023 moment analysis establishes the run-and-tumble oscillator and stationary one-time moment hierarchy, and thus supplies the model and a route to \(m_2,m_4\). Sun, Ye, and Podgornik (2024) provide time-dependent moment recurrences for a related finite-duration tumble model, but do not identify this stationary fourth-order lag-ordering transition. Guéneau, Majumdar, and Schehr (2026) give a broad exact treatment of one-time stationary distributions in arbitrary spatial dimensions; no stationary **two-time oriented fourth-order contrast** or its dimension-five sign boundary was identified in the inspected material. Knight and Pruessner (2026) investigate temporal irreversibility in a one-dimensional active-particle model, including multitime correlations, but their stated setting does not imply the dimension-dependent spherical-refresh threshold established here. Existing moment and resolvent frameworks can implicitly generate aspects of these formulas; the assessed result is the explicit exact sign classification with the dimension-five onset and at-most-one crossing, not the underlying generator method or the stationary even moments.

## Limitations

This statement is restricted to isotropic independent Poisson refreshes of a fixed-speed direction, exact harmonic confinement, the stationary law, and the specified Cartesian fourth-order contrast. The high-dimensional sign reversal does not, by itself, classify stochastic entropy production, full pathwise time reversibility, or other fourth-order observables. Zeros of this single witness must not be interpreted as time-reversal invariance. No analog for continuous rotational diffusion, nonlinear traps, thermal translational noise, or non-Poisson renewals is proved. Independence of the full mathematical priority assessment has not been established; general published moment machinery may subsume intermediate calculations, and further source comparison is warranted.

## References

1. D. Frydel, *Run-and-tumble oscillator: moment analysis of stationary distributions*, arXiv:2309.12537, first publicly available September 21, 2023. https://arxiv.org/abs/2309.12537
2. A. Sun, F. Ye and R. Podgornik, *Exact moments for a run and tumble particle with a finite tumble time in a harmonic trap*, arXiv:2409.00578, first publicly available September 1, 2024. https://arxiv.org/abs/2409.00578
3. B. Guéneau, S. N. Majumdar and G. Schehr, *Exact Stationary State of a d-dimensional Run-and-Tumble Particle in a Harmonic Potential*, arXiv:2602.08436, 2026. https://arxiv.org/abs/2602.08436
4. J. Knight and G. Pruessner, *Partial Entropy production of active particles with hidden states in potentials*, arXiv:2605.29201, 2026. https://arxiv.org/abs/2605.29201
5. P. Garcia-Millan and G. Pruessner, *Run-and-tumble motion in a harmonic potential: field theory and entropy production*, arXiv:2012.02900, 2020. https://arxiv.org/abs/2012.02900
