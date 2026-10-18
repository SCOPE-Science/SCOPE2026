# Exact finite-rate spectroscopy of Fourier force power in a telegraph-driven tracer

## Finding

The effective diffusivity of a passive tracer driven by an **exogenous** run-and-tumble particle on a periodic ring determines the power spectrum of the periodic forcing. If the force has at most \(N\) positive Fourier harmonics and its unknown thermal baseline is not calibrated separately, **any \(N+1\) distinct positive tumbling rates determine all \(N\) powers and the baseline uniquely; \(N\) rates cannot guarantee that recovery.** For square-integrable forcing with infinitely many harmonics, exact knowledge of diffusivity over any open interval of positive tumbling rates determines every power by a meromorphic-residue formula. A strict complete-monotonicity law gives a testable obstruction to interpreting a nonmonotone tumbling-rate scan within this one-way-coupled model.

Let \(q_n=2\pi n/L\), \(P_n=2|\widehat F_n|^2\), and \(B_n=v^2+D^2q_n^2\). For the precise model below,
\[
\mathcal D(\alpha)=D_0+\sum_{n\ge1}P_n\frac{Dq_n^2+2\alpha}{q_n^2(B_n+2D\alpha)},
\qquad
\mathcal D_\infty-\mathcal D(\alpha)=\frac{v^2}{D}\sum_{n\ge1}\frac{P_n}{q_n^2(B_n+2D\alpha)}.
\]
For \(v>0\), a nonzero force makes the deficit strictly completely monotone and the diffusivity strictly increasing and concave as a function of tumbling rate.

## Assumptions and scope

Fix \(L,D,v>0\), \(D_0\ge0\), and a real mean-zero periodic force \(F\in L^2(\mathbb T_L)\). Let \(\sigma_t\in\{-1,+1\}\) flip signs at the event times of an independent rate-\(\alpha>0\) Poisson process. Drive the circle coordinate by
\[
 dR_t=v\sigma_t\,dt+\sqrt{2D}\,dB_t\pmod L,
\]
starting from uniform position and independent symmetric orientation. The unwrapped passive coordinate is
\[
 X_t=X_0+\sqrt{2D_0}\,W_t+\int_0^t F(R_s)\,ds,
\]
where \(B,W\) are independent standard Brownian motions, also independent of \(\sigma\). Define
\[
 \widehat F_n=\frac1L\int_0^L F(r)e^{-iq_n r}\,dr,
 \qquad
 \mathcal D(\alpha)=\lim_{t\to\infty}\frac{\operatorname{Var}(X_t-X_0)}{2t}.
\]
The limit exists and is finite. No feedback from \(X\) to \(R\) is present; this is an exact one-way-coupled tracer model, not an exact solution for two mutually interacting particles.

## Proof

**Stationarity and covariance.** Uniform position and symmetric orientation are invariant. Mean-zero forcing gives \(\mathbb E F(R_t)=0\). For \(n\ne0\), write the Markov generator restricted to the \(n\)-th spatial Fourier mode and the two orientation states as
\[
 Q_n=\begin{pmatrix}
 -Dq_n^2-\alpha+ivq_n & \alpha\\
 \alpha & -Dq_n^2-\alpha-ivq_n
 \end{pmatrix}.
\]
With \(u=(1,1)^\mathsf T\), stationary Fourier correlation is \(C_n(t)=u^\mathsf T e^{tQ_n}u/2\). Because \(D>0\), the semigroup satisfies an integrable exponential bound. Direct two-by-two inversion gives
\[
 \int_0^\infty C_n(t)\,dt
 =\tfrac12u^\mathsf T(-Q_n)^{-1}u
 =\frac{Dq_n^2+2\alpha}{q_n^2(v^2+D^2q_n^2+2D\alpha)}.
\]
Fourier orthogonality and the reality of \(F\) yield
\[
 \operatorname{Cov}(F(R_t),F(R_0))
 =\sum_{n\ge1}P_nC_n(t).
\]
The spectral gap from translational diffusion and Parseval summability \(\sum_nP_n<\infty\) justify exchanging the time integral and series. The stationary variance identity \(\operatorname{Var}(\int_0^tF(R_s)ds)=2\int_0^t(t-s)\operatorname{Cov}(F(R_s),F(R_0))ds\) proves the diffusivity formula. In particular \(\mathcal D_\infty=D_0+\sum_{n\ge1}P_n/(Dq_n^2)\).

**Monotonicity and boundary cases.** The exact identity
\[
 \frac1{Dq_n^2}-\frac{Dq_n^2+2\alpha}{q_n^2(B_n+2D\alpha)}
 =\frac{v^2}{Dq_n^2(B_n+2D\alpha)}
\]
proves the deficit representation. Differentiation term by term is locally uniformly valid for \(\alpha>0\). For all integers \(k\ge0\),
\[
 (-1)^k\frac{d^k}{d\alpha^k}(\mathcal D_\infty-\mathcal D(\alpha))
 =\frac{v^2}{D}(2D)^k k!\sum_{n\ge1}\frac{P_n}{q_n^2(B_n+2D\alpha)^{k+1}}>0
\]
when \(F\ne0\). Thus \(\mathcal D' >0\), \(\mathcal D''<0\). For \(v=0\), the diffusivity is independent of \(\alpha\). For \(D=0\) and \(v,\alpha>0\), the two-orientation resolvent instead gives \(\mathcal D(\alpha)=D_0+(2\alpha/v^2)\sum_{n\ge1}P_n/q_n^2\), so different spectra sharing that weighted sum cannot be distinguished by an \(\alpha\)-scan.

**Recovery from an open interval.** The deficit is a normally convergent meromorphic series away from the discrete real poles \(\alpha_n=-B_n/(2D)\); distinctness follows from \(q_n^2\) being strictly increasing. The identity theorem and the large-positive-rate limit recover the same meromorphic function from its restriction to any open positive-rate interval. Its residue at \(\alpha_n\) is
\[
 \operatorname{Res}_{\alpha=\alpha_n}(\mathcal D_\infty-\mathcal D(\alpha))
 =\frac{v^2P_n}{2D^2q_n^2}.
\]
A zero residue means the harmonic is absent. Therefore the scan determines every \(P_n\), but not the phases of \(\widehat F_n\): translations, reflections, and further phase alterations with identical powers are indistinguishable.

**Sharp finite-rate reconstruction.** Suppose \(P_n=0\) for \(n>N\), with \(N\ge1\), and choose pairwise distinct \(\alpha_0,\ldots,\alpha_N>0\). For \(1\le i,n\le N\), set
\[
 b_i=\frac{\mathcal D(\alpha_i)-\mathcal D(\alpha_0)}{2v^2(\alpha_i-\alpha_0)},
 \quad A_{in}=\frac1{B_n+2D\alpha_i},
 \quad z_n=\frac{P_n}{q_n^2(B_n+2D\alpha_0)}.
\]
The rational kernel identity implies \(b=Az\). The Cauchy determinant is nonzero since \(B_n\) and \(\alpha_i\) are pairwise distinct and all denominators are positive. Hence \(z=A^{-1}b\) and
\[
 P_n=q_n^2(B_n+2D\alpha_0)z_n,
 \quad D_0=\mathcal D(\alpha_0)-\sum_{n=1}^N P_n\frac{Dq_n^2+2\alpha_0}{q_n^2(B_n+2D\alpha_0)}.
\]
These expressions reconstruct all unknowns. Conversely, \(m\le N\) diffusion readings yield at most \(m\) linear conditions on the \(N+1\) real unknowns \((D_0,P_1,\ldots,P_N)\). Choose an interior point with \(D_0>0\) and all \(P_n>0\), and perturb it a sufficiently small amount along a nonzero null vector. The perturbed parameters remain nonnegative and produce identical readings. Thus \(N+1\) samples are the exact minimum for uniform identifiability when \(D_0\) is not otherwise known. Cauchy inversion need not be numerically stable as \(N\) grows.

## Verification

Run `python verification/verify.py` from the extracted package with Python 3 and `numpy`, `scipy`, `sympy`. The standalone verifier independently reconstructs the Fourier generator, algebraically checks the Green--Kubo integral and its derivatives, compares 16 matrix-exponential time-integrals against their exact resolvents, and reconstructs four randomized band-limited spectra plus an exact-rational six-mode spectrum. Finite checks corroborate, rather than replace, the analytical results.

## Relationship to prior work

The motivating active/passive interaction study by Patel, Sarkar, Basu and Chaudhuri (arXiv:2607.25902v1) analyzes nonmonotone diffusivity of coupled active/passive particles and uses free-driver approximations in a strong-drive regime. The present theorem explicitly fixes that **free driver as an exact one-way-coupled process** and asks an inverse question: what forcing harmonics can be inferred from a tumbling-rate diffusivity scan? It does not assert that nonmonotonic transport in the interacting model is impossible.

The general Green--Kubo-resolvent representation of diffusion for run-and-tumble motion is established by van Ginkel, van Gisbergen and Redig (arXiv:2101.09046). That general method is acknowledged, not claimed new. The narrower contribution is the complete identification map for the periodic force spectrum, sharp finite-sample count, and loss of identifiability at the noise and propulsion boundaries. Work on intermittent active motion and confined run-and-tumble optimization addresses different observables and geometry.

## Limitations

The inference assumes exact noiseless measurements, known ring size \(L\), propulsion speed \(v\), and driver noise diffusivity \(D\). It identifies Fourier **powers**, not phases or the force itself. The finite-sample formula requires a known harmonic cutoff \(N\); unbounded spectra require ideal continuum-rate data and analytic continuation, both ill-conditioned in practice. It excludes feedback coupling and finite-range interactions between tracer and driver. The uniqueness claim is mathematical identifiability within this model, not an experimental noise-robust estimation theorem.

## References

1. M. Patel, R. Sarkar, U. Basu and D. Chaudhuri, *Non-monotonic diffusion from nonequilibrium driving*, arXiv:2607.25902v1 (2026-07-28), https://arxiv.org/abs/2607.25902.
2. B. van Ginkel, R. van Gisbergen and F. Redig, *Run-and-Tumble Motion: The Role of Reversibility*, arXiv:2101.09046 (2021), https://arxiv.org/abs/2101.09046.
3. S. Pietrangeli, C. Ybert, L. Cottin-Bizonne and J.-F. Detcheverry, *Optimal run-and-tumble in slit-like confinement* (2024), https://arxiv.org/search/?query=Optimal+run-and-tumble+in+slit-like+confinement&searchtype=all.
4. I. Santra, J. Olsen and S. Gupta, *Dynamics of switching processes: general results and applications in intermittent active motion*, arXiv:2408.16643 (2024), https://arxiv.org/abs/2408.16643.
