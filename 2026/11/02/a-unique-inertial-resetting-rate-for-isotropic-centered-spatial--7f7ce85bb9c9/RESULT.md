# A unique inertial resetting rate for isotropic centered spatial fluctuations

## Finding

A two-dimensional inertial active Brownian particle undergoing complete Poisson resetting has a **single nonzero resetting rate at which its centered stationary spatial covariance becomes isotropic**, although the resetting direction remains fixed. Its exact value differs from the overdamped threshold and varies strictly with the momentum-relaxation rate.

Let \(d>0\) be rotational diffusivity, \(\gamma>0\) velocity relaxation rate, \(v>0\) active speed, \(r>0\) resetting rate, and \(\kappa\ge0\) isotropic velocity-noise diffusivity. For the stationary position \(Z=X+iY\), define the complex centered anisotropy \(Q=\mathbb E[(Z-\mathbb EZ)^2]\). Then

\[
Q=\frac{\gamma^2v^2P(r;\gamma,d)}{(r+d)^2(r+4d)(r+\gamma)^2(r+2\gamma)(r+d+\gamma)},
\]

where

\[
P(r;\gamma,d)=5r^3+(5d+7\gamma)r^2+2\gamma^2r-4d\gamma(d+\gamma).
\]

There is exactly one positive root \(r_*(\gamma,d)\), and \(0<r_*(\gamma,d)<2d\). For \(0<r<r_*\), the centered variance transverse to the reset direction exceeds that along it; for \(r>r_*\), the inequality is reversed. Equality occurs only at \(r=r_*\). The threshold is independent of \(v\) and \(\kappa\). It increases strictly with \(\gamma\), with the sharp limits

\[
r_*(\gamma,d)=\frac{2}{\sqrt5}\sqrt{d\gamma}+O(\gamma)
\quad(\gamma\downarrow0),\qquad
r_*(\gamma,d)=2d-\frac{12d^2}{\gamma}+O(\gamma^{-2})
\quad(\gamma\to\infty).
\]

At the critical rate the **centered second moment** is isotropic, not necessarily the full stationary density or the uncentered second moment.

## Assumptions and scope

Take independent standard real Brownian motions \(B_x,B_y,B_\theta\) and independent rate-\(r\) Poisson reset times. Between resets, write \(U=V_x+iV_y\) and \(N=e^{i\theta}\), and impose

\[
dZ_t=U_t\,dt,\qquad
dU_t=-\gamma U_t\,dt+\gamma vN_t\,dt+\sqrt{2\kappa}(dB_x+i\,dB_y),
\qquad d\theta_t=\sqrt{2d}\,dB_\theta.
\]

At each reset, \((Z,U,\theta)\mapsto(0,0,0)\). All parameters are fixed, not scaled with time. The resetting orientation is aligned with the positive real axis, and velocity is reset along with position and angle; position-only or orientation-only resets are excluded. Brownian noises and reset times are mutually independent. The theorem is about the unique stationary law and its finite second moments, for every \(d,\gamma,v,r>0\) and \(\kappa\ge0\).

Define the centered spatial trace \(S=\mathbb E|Z-\mathbb EZ|^2\). Its exact value is

\[
\begin{aligned}
S={}&\frac{2\gamma^2v^2(2d+2\gamma+3r)}{r(r+d)(r+\gamma)(r+2\gamma)(r+d+\gamma)}
+\frac{8\kappa}{r(r+\gamma)(r+2\gamma)}\\
&-\frac{\gamma^2v^2}{(r+d)^2(r+\gamma)^2}.
\end{aligned}
\]

Reflection symmetry implies \(\mathbb EY=\operatorname{Cov}(X,Y)=0\), so the complete centered covariance tensor is \(\Sigma=\tfrac12\operatorname{diag}(S+Q,S-Q)\). The mean is \(\mathbb EZ=\gamma v/[(r+d)(r+\gamma)]>0\), even at the isotropy rate.

## Proof

**Stationarity and renewal representation.** Couple any two trajectories after their first common complete resetting event, using the same driving noises thereafter. The rate-\(r\) reset process regenerates from the deterministic state, providing a unique stationary law. At a stationary observation time its elapsed reset age \(A\) has the exponential law with rate \(r\), independently of the Brownian increments since that reset. All second moments are finite: the active displacement magnitude is bounded by \(vA\), while the integrated Ornstein–Uhlenbeck noise has at most linearly growing variance in \(A\).

For a reset-free excursion of age \(a\), variation of constants gives

\[
Z_a=v\int_0^a [1-e^{-\gamma(a-s)}]e^{i\theta_s}\,ds+H_a,
\]

where \(H_a\) is an independent, centered isotropic Gaussian. Thus \(\mathbb EH_a^2=0\), so isotropic velocity noise does not contribute to \(\mathbb E[Z^2]\) or \(\mathbb EZ\). The Brownian angular identities, for \(0\le s\le t\), are

\[
\mathbb Ee^{i\theta_s}=e^{-ds},\qquad
\mathbb E[e^{i\theta_s+i\theta_t}]=e^{-d(t+3s)},\qquad
\mathbb E[e^{i\theta_s-i\theta_t}]=e^{-d(t-s)}.
\]

**First complex moment.** Integrating over exponential age and exchanging the nonnegative-time integrals gives

\[
\mathbb EZ=vr\int_0^\infty e^{-(r+d)s}\,ds
\int_0^\infty e^{-rh}(1-e^{-\gamma h})\,dh
=\frac{v\gamma}{(r+d)(r+\gamma)}.
\]

**Second complex moment.** For \(s\le t\), integrating the two displacement kernels over all exponential ages \(a\ge t\) yields

\[
\begin{aligned}
&r\int_t^\infty e^{-ra}
(1-e^{-\gamma(a-s)})(1-e^{-\gamma(a-t)})\,da\\
&\quad=e^{-rt}\frac{\gamma}{r+\gamma}
\left[1-\frac{r}{r+2\gamma}e^{-\gamma(t-s)}\right].
\end{aligned}
\]

Using the symmetry of the \((s,t)\) integral and substituting \(t=s+h\) gives

\[
\begin{aligned}
\mathbb EZ^2
&=\frac{2v^2\gamma}{r+\gamma}
\int_0^\infty e^{-(r+4d)s}\,ds
\int_0^\infty e^{-(r+d)h}
\left[1-\frac{r}{r+2\gamma}e^{-\gamma h}\right]dh\\
&=\frac{2\gamma^2v^2(2d+2\gamma+3r)}{(r+d)(r+4d)(r+\gamma)(r+2\gamma)(r+d+\gamma)}.
\end{aligned}
\]

Subtracting \((\mathbb EZ)^2\) and reducing to a common denominator yields precisely the displayed rational expression for \(Q\), with cubic numerator \(P\). Since the law is invariant under \((Y,V_y,\theta)\mapsto(-Y,-V_y,-\theta)\), the imaginary part of \(Q\) vanishes. In particular \(Q=\operatorname{Var}(X)-\operatorname{Var}(Y)\).

**Trace.** Replacing the orientation identity in the preceding calculation by \(\mathbb E[e^{i\theta_s-i\theta_t}]=e^{-d|t-s|}\) shows that the active contribution to \(\mathbb E|Z|^2\) is

\[
\frac{2\gamma^2v^2(2d+2\gamma+3r)}{r(r+d)(r+\gamma)(r+2\gamma)(r+d+\gamma)}.
\]

Ito isometry for the two independent velocity noises, followed by the exponential-age average, adds \(8\kappa/[r(r+\gamma)(r+2\gamma)]\). Subtracting \(|\mathbb EZ|^2\) proves the displayed formula for \(S\) and hence the covariance tensor.

**Uniqueness, strict shift and limits.** Every denominator in \(Q\) is positive. Moreover

\[
P(0;\gamma,d)=-4d\gamma(d+\gamma)<0,\quad
P(2d;\gamma,d)=60d^3+24d^2\gamma>0,
\]

and \(\partial_rP=15r^2+2(5d+7\gamma)r+2\gamma^2>0\) for \(r\ge0\). Thus there is exactly one positive root, lying below \(2d\), and its sign determines the strict variance ordering.

To prove strict monotonicity of \(r_*\) with \(\gamma\), fix \(0<r<2d\). As a polynomial in \(\gamma\),

\[
P=(2r-4d)\gamma^2+(7r^2-4d^2)\gamma+5r^2(r+d)
\]

has negative quadratic coefficient and positive constant coefficient, so it has exactly one positive root in \(\gamma\) and changes from positive to negative there. Increasing \(\gamma\) past the value corresponding to \(r=r_*\) therefore makes \(P(r)<0\), which strictly increases the unique \(r\)-root. The two asymptotic expansions follow from dominant balance in \(P=0\): \(5dr^2\sim4d^2\gamma\) as \(\gamma\downarrow0\), and \(2\gamma^2(r-2d)+24d^2\gamma+o(\gamma)=0\) as \(\gamma\to\infty\). Repeated expansion or the implicit-function theorem gives the stated error orders.

## Verification

The standalone `verify.py` requires only Python 3's standard library. Run `python3 verify.py` from the extracted package directory. It performs 550 exact-rational and numerical consistency checks, comparing the closed moments to an independently constructed stationary generator hierarchy for several positive parameter combinations. It also checks the full covariance trace, positive variance components, sign of the cubic, monotonic numerical roots, and limiting scalings. The script was executed from the actual new package contents before review. Exact-rational finite checks validate the displayed algebra at their tested inputs but do not replace the analytic proof for all parameters.

As a further normalization test, substituting \(d=1\), \(\gamma=1/M\), \(\kappa=1/M^2\), and \(v=\mathrm{Pe}\) into the raw mean squared displacement above reproduces the published complete-resetting scalar formula of Patel and Shee (2026), their equation (7). The overdamped limit \(\gamma\to\infty\) gives \(Q\to v^2(r-2d)/[(r+d)^2(r+4d)]\), matching the isotropic-diffusion specialization of Ghosh, Mandal and Chaki's 2025 position-orientation reset covariance formulas.

## Relationship to prior work

Patel and Shee, arXiv:2602.21134 (first public version February 24, 2026, revised October 11, 2026), develop the same fully resetting inertial active Brownian model and determine scalar second- and fourth-order moments. Their full-text model section, second-moment section, and derivation appendices were inspected. Scalar \(\mathbb E|Z|^2\) and scalar fourth moments alone do not determine the centered tensor difference \(\operatorname{Var}(X)-\operatorname{Var}(Y)\), nor do they state the inertia-dependent critical reset rate. Their renewal method and underlying model are foundational prior results, not claimed as new here.

Ghosh, Mandal and Chaki, arXiv:2501.05149 (2025), supply longitudinal and transverse stationary variances for an **overdamped**, shape-anisotropic ABP under resetting. For isotropic thermal diffusion their formulas imply the already-known overdamped threshold \(r=2d\). The finite-inertia cubic root and strict monotonic shift here are not corollaries obtained by setting particle-shape anisotropy to zero in that overdamped model.

Patel and Chaudhuri, arXiv:2310.00802 (2023), establish a broad moment-generating method for inertial ABP trajectories **without resetting**. Combining such a method with renewal theory is a possible alternative derivation of the raw moments. The characterized finite-inertia centered-covariance zero, its exact cubic, and its rate dependence were not located in their inspected study. Shee, arXiv:2508.12223 (2025), treats a distinct overdamped chiral resetting model and supplies context for reset-induced anisotropy; its zero-chirality centered threshold is the overdamped boundary of the present result.

## Limitations

This is a stationary second-moment statement under complete state resetting to a fixed orientation; it is not a classification of full spatial densities, dynamic convergence rates, non-Poisson resets, anisotropic thermal velocity noise, position-only resets, or nontrivial velocity at reset. Full density isotropy is **not** asserted at the covariance threshold: in fact \(\mathbb EZ>0\) there. The limit \(\gamma\downarrow0\) is an asymptotic of positive-relaxation models, not an assertion of the same stationary active process at \(\gamma=0\). The literature comparison supports only best-knowledge originality, not an independent priority certification: a wider unstated tensor identity in an unlocated treatment could cover the characterization.

## References

1. M. Patel and A. Shee, *Controlling inertial active Brownian motion via stochastic resetting*, arXiv:2602.21134, first publicly submitted 2026-02-24, revised 2026-10-11, https://arxiv.org/abs/2602.21134.
2. A. Ghosh, S. Mandal and S. Chaki, *Anisotropic active Brownian particle in two dimensions under stochastic resetting*, arXiv:2501.05149, https://arxiv.org/abs/2501.05149.
3. M. Patel and D. Chaudhuri, *Exact moments and re-entrant transitions in the inertial dynamics of active Brownian particles*, arXiv:2310.00802, https://arxiv.org/abs/2310.00802.
4. A. Shee, *Steering chiral active Brownian motion via stochastic position-orientation resetting*, arXiv:2508.12223, https://arxiv.org/abs/2508.12223.
