# A sharp center-to-periphery covariance boundary for a reset Thomas–Fermi condensate

## Finding

Consider the exactly self-similar Thomas–Fermi hydrodynamic approximation for the freely expanding, Poisson-reset weakly interacting Bose condensate described in [1]. Let \(x_0>0\) be its initial support radius, \(\omega>0\) its original longitudinal trap frequency, and \(r>0\) its independent reset rate. At a stationary observation, the age \(T\) since the most recent reset is exponential of rate \(r\). Denote the random hydrodynamic *single-realization density profile* by \(\rho_T(x)\), and set
\[
 C_r(z)=\operatorname{Cov}\bigl(\rho_T(0),\rho_T(zx_0)\bigr),\qquad z\ge0.
\]
**The sharp spatial classification is**
\[
\boxed{\quad C_r(z)>0\ \text{for every }r>0\ \Longleftrightarrow\ 0\le z\le 1/\sqrt3.\quad}
\]
More precisely, for every fixed \(z>1/\sqrt3\), \(C_r(z)>0\) for all sufficiently small positive \(r\), and \(C_r(z)<0\) for all sufficiently large \(r\). Hence at least one positive reset rate gives \(C_r(z)=0\). No assertion of uniqueness of that rate is made. The formulas are symmetric under \(z\mapsto-z\).

There are three different *rapid-reset* laws, with \(z\) fixed:
\[
 C_r(z)\sim \frac{9}{16x_0^2}\,5(1-3z^2)\frac{\omega^4}{r^4}
 \quad(0\le z\le1,\ z\ne1/\sqrt3),
\]
\[
 C_r(1/\sqrt3)\sim \frac{9}{16x_0^2}\,84\frac{\omega^6}{r^6},
\]
\[
 C_r(z)\sim\frac{9}{16x_0^2}\left(\frac1z-1\right)
 \frac{2\sqrt2\,\omega}{z^2}\sqrt{1-\frac1z}\,
 \frac{e^{-rt_z}}r \quad(z>1),
\]
where \(t_z\) is the first age at which the expanding support reaches \(zx_0\), given explicitly in the proof. At the *slow-reset* endpoint, for every fixed finite \(z\ge0\),
\[
 C_r(z)\sim\frac{9r}{16x_0^2}A_z,\qquad
 A_z=\frac1{\sqrt2\,\omega}\int_0^{\min\{1,1/z\}}
 \frac{1-z^2y^2}{\sqrt{1-y}}\,dy>0.
\]
For \(0\le z\le1\), this coefficient simplifies to
\[
 A_z=\frac1{\sqrt2\,\omega}\left(2-\frac{16}{15}z^2\right).
\]
At \(z=0\), interpret \(\min\{1,1/z\}=1\). All statements concern the mean-field density's variability across the *reset age*, rather than microscopic quantum density-density correlations.

## Assumptions and scope

The continuum density is the normalized, one-dimensional Thomas–Fermi profile (integral over space equals one)
\[
 \rho_t(x)=\frac{3}{4x_0\lambda(t)}\left(1-\frac{x^2}{x_0^2\lambda(t)^2}\right)_+,
\]
with \(a_+=\max(a,0)\). Its deterministic expansion factor satisfies
\[
 \ddot\lambda(t)=\omega^2/\lambda(t)^2,\quad
 \lambda(0)=1,\quad\dot\lambda(0)=0.
\]
The reset protocol restores this profile completely and instantaneously, with exponentially distributed inter-reset times of rate \(r\). At stationarity the last-reset age \(T\) is \(\operatorname{Exp}(r)\). These are the large-particle-number, Thomas–Fermi hydrodynamic assumptions of [1]; finite-particle corrections, quantum pressure near the edge, physical finite-time recooling, and particle-number shot noise are excluded. Every limit changes the reset rate at fixed positive \(x_0,\omega\) and fixed finite \(z\). Only the primary MSC2020 area 82C21 (time-dependent continuum particle models) is asserted.

## Proof

**1. Reduction to a single scalar covariance.** Multiply the expansion ODE by \(\dot\lambda\) to obtain
\[
 \dot\lambda(t)=\sqrt2\,\omega\sqrt{1-1/\lambda(t)},
\quad
 t(\ell)=\frac{\sqrt{\ell(\ell-1)}+
 \operatorname{arsinh}\sqrt{\ell-1}}{\sqrt2\,\omega}
 \quad(\ell\ge1).
\]
Thus \(\lambda\) rises continuously and strictly from one to infinity. Put \(U(t)=1/\lambda(t)\), so \(U(0)=1\), \(0<U(t)<1\) for \(t>0\), and \(U\) strictly decreases to zero. Write
\[
 G_z(t)=U(t)\bigl(1-z^2U(t)^2\bigr)_+,\qquad K=\frac{3}{4x_0}.
\]
Then \(\rho_T(0)=KU(T)\), \(\rho_T(zx_0)=KG_z(T)\), and
\[
 C_r(z)=K^2\{\mathbb E_r[U(T)G_z(T)]-
   \mathbb E_r[U(T)]\,\mathbb E_r[G_z(T)]\}.
\tag{1}
\]
All expectations exist since \(0<U\le1\) and \(0\le G_z\le1\).

**2. Sharp all-rate positivity zone.** For \(0\le z\le1/\sqrt3\), truncation is inactive and \(G_z(t)=U(t)-z^2U(t)^3\). The function \(u\mapsto u-z^2u^3\) has derivative \(1-3z^2u^2\ge0\) on \((0,1]\), and is strictly increasing there except possibly at its endpoint. Hence \(U(t)\) and \(G_z(t)\) are both strictly decreasing in age. For independent ages \(T,T'\),
\[
 2\operatorname{Cov}(U(T),G_z(T))=
 \mathbb E[(U(T)-U(T'))(G_z(T)-G_z(T'))]>0.
\]
The strict inequality uses the nondegenerate continuous age distribution. This proves positivity at every rate, including at the boundary \(z=1/\sqrt3\).

**3. Universal slow-reset positivity and its exact coefficient.** From the integral for \(t(\ell)\), \(\lambda(t)/(\sqrt2\omega t)\to1\) as \(t\to\infty\), so \(U(t)=O((1+t)^{-1})\) and \(G_z(t)=O((1+t)^{-1})\) for each fixed \(z\). Consequently, \(UG_z\) is integrable on \([0,\infty)\), and dominated convergence gives
\[
 \mathbb E_r[UG_z]=r\int_0^\infty UG_z\,dt+o(r)=rA_z+o(r).
\]
Since \(\mathbb E_r[U]\) and \(\mathbb E_r[G_z]\) are each \(O(r\log(1/r))\) as \(r\downarrow0\), their product is \(o(r)\). To evaluate \(A_z\), substitute \(\ell=\lambda(t)\), then \(y=1/\ell\) and use
\[
 \frac{dt}{d\ell}=\frac1{\sqrt2\,\omega}
 \sqrt{\frac{\ell}{\ell-1}}.
\]
The result is the positive integral in the Finding. For \(z\le1\), Euler beta integrals \(B(1,1/2)=2\) and \(B(3,1/2)=16/15\) give the displayed closed form. Because the integrand is positive on an interval of positive length for each finite \(z\), \(A_z>0\).

**4. Rapid reset inside the original support.** For fixed \(0\le z\le1\), truncation remains inactive. Let \(a=\omega^2/2\). Taylor expansion of the ODE at the initial conditions gives
\[
 U(t)=1-at^2+O(t^4),\qquad
 G_z(t)=U(t)-z^2U(t)^3.
\]
For \(T\sim\operatorname{Exp}(r)\), \(\mathbb E[T^k]=k!/r^k\). Thus
\[
 \operatorname{Var}(U(T))=a^2\operatorname{Var}(T^2)+O(r^{-6})
 =5\omega^4r^{-4}+O(r^{-6}).
\]
For \(z\ne1/\sqrt3\), expansion around \(U=1\) gives
\[
 \operatorname{Cov}(U,G_z)=(1-3z^2)\operatorname{Var}(U)+O(r^{-6}),
\]
which proves the first rapid-reset law. At \(z=1/\sqrt3\), write \(\delta=U-1\). The cancellation is exact:
\[
 G_{1/\sqrt3}=\frac23-\delta^2-\frac13\delta^3
 =\frac23-a^2t^4+O(t^6).
\]
Hence
\[
 \operatorname{Cov}(U,G_{1/\sqrt3})
 =a^3\operatorname{Cov}(T^2,T^4)+O(r^{-8})
 =a^3\frac{6!-2!4!}{r^6}+O(r^{-8})
 =84\omega^6r^{-6}+O(r^{-8}).
\]
These expansions are justified under the exponential age density by splitting at any fixed small age: Taylor remainders are integrable against the exponentially concentrated density, while the large-age contribution is exponentially suppressed.

**5. Rapid reset beyond the initial support.** Fix \(z>1\) and set \(t_z=t(z)>0\). Then \(G_z(t)=0\) for \(t\le t_z\), and immediately above that threshold
\[
 G_z(t)=b_z(t-t_z)+O((t-t_z)^2),\qquad
 b_z=\frac{2\sqrt2\,\omega}{z^2}\sqrt{1-1/z}>0.
\]
This uses the chain rule at \(\lambda(t_z)=z\). Endpoint Laplace asymptotics therefore give
\[
 \mathbb E_r[G_z(T)]\sim b_z e^{-rt_z}/r,\qquad
 \frac{\mathbb E_r[U(T)G_z(T)]}{\mathbb E_r[G_z(T)]}\longrightarrow U(t_z)=1/z.
\]
Moreover \(\mathbb E_r[U(T)]\to1\). Substituting in (1) proves the third rapid-reset law; its coefficient is strictly negative.

**6. Sign existence and sharpness.** Parts 2–5 show all-rate positivity precisely on \([0,1/\sqrt3]\), whereas every larger \(z\) has positive slow-rate covariance and negative rapid-rate covariance. The expectation in (1) varies continuously in \(r>0\) by dominated convergence on each bounded interval of positive rates. Thus the intermediate-value theorem gives at least one sign-changing rate for each \(z>1/\sqrt3\). This concludes the classification.

## Verification

The included `verify.py` evaluates (1) by two mathematically different quadratures: a Jacobian-weighted integral over \(s=\sqrt{\lambda-1}\), and a direct exponential-age integral with a separately inverted \(t(\lambda)\). They agree to numerical precision on both sides of the sign change. The checker tests positivity below \(1/\sqrt3\), low/high-rate sign reversals beyond it, exact beta-integral coefficients, and the coefficients of the \(r^{-4}\) and critical \(r^{-6}\) laws. Execute `python verify.py` with Python 3.10 or newer and SciPy 1.10 or newer. The all-rate and asymptotic results are proved above; finite evaluations are corroboration, not a replacement for these arguments.

Selected density-covariance values with \(x_0=\omega=1\): for \(z=0.8\), \(C_{0.03}=+0.01017881890580\), \(C_{1}=+0.00321830938013\), and \(C_{5}=-0.000862908220260\). For \(z=1.5\), \(C_{0.03}=+0.00223410838592\) and \(C_1=-0.01170422242709\). At \(z=1/\sqrt3\), \(C_{20}=+5.620466988696\times10^{-7}\).

## Relationship to prior work

[1] derives the deterministic self-similar density, the exponential mixing distribution of reset ages, the stationary *mean* density, the support-edge distribution and full counting statistics of the count in a symmetric interval (its Secs. 3–4 and Appendices B–C). This work uses those established model inputs, not a newly derived expansion law. Its distinct conclusion concerns the *joint* reset-age fluctuations of densities at the center and at an arbitrary second point: the exact universal positivity boundary, the inevitable sign reversal outside, and the three rapid-reset regimes (including the boundary \(r^{-6}\) law). Those are not asserted in [1]; the main source's general mixture formula determines them only after the covariance and asymptotic analysis here.

[2] analyzes a different noninteracting boson protocol that shifts a harmonic trap center; its Sec. 3.2 computes covariances of particle *positions* as variances of a shared random center, rather than covariances of local density profiles for an expanding, interacting Thomas–Fermi cloud. [3] obtains positive and negative density correlations during *diffusive expansion in a static random potential*, without stochastic resetting or the radial threshold of this theorem; those long-range speckle correlations originate from disorder-induced interference. The generic possibility of negative density correlation in cold gases is therefore not claimed as new here.

## Limitations

The theorem does not cover microscopic quantum fluctuations, generic Gross–Pitaevskii initial states, interacting stochastic particle positions beyond the hydrodynamic density, non-Poissonian reset ages, or time correlations between two different stationary observations. The theorem guarantees at least one positive reset rate at which the covariance vanishes outside the sharp spatial zone, but does not prove uniqueness or monotonicity of the crossing rate. The exact numerical rate is not claimed. The positive critical covariance is asymptotic to a sixth-order decay, not a zero for finite resetting rates. The mathematical result derives a consequence of the self-similar solution in [1]; an unindexed prior treatment of that consequence remains an originality risk.

## References

[1] N. Mesquita, M. Kulkarni, S. N. Majumdar, S. Sabhapandit, *Weakly interacting Bose-Einstein condensate with stochastic resetting*, arXiv:2609.37110v1 (first submitted 2026-09-29), https://arxiv.org/html/2609.37110v1.

[2] M. Kulkarni, S. N. Majumdar, S. Sabhapandit, *Dynamically emergent correlations in bosons via quantum resetting*, arXiv:2407.20342v2, J. Phys. A: Math. Theor. 58 (2025) 105003, https://arxiv.org/html/2407.20342v2.

[3] N. Cherroret, S. E. Skipetrov, *Long-Range Correlations of Density in a Bose-Einstein Condensate Expanding in a Random Potential*, Phys. Rev. Lett. 101 (2008) 190406, DOI:10.1103/PhysRevLett.101.190406, https://lpmmc.cnrs.fr/IMG/pdf/prl08b.pdf.
