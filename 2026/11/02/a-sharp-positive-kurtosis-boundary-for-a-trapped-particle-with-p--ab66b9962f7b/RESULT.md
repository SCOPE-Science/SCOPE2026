# A sharp positive-kurtosis boundary for a trapped particle with preferred tumbles

## Finding

A planar run-and-tumble particle whose orientation jumps by a symmetric but nonuniform angle distribution can have **positive stationary positional excess kurtosis**, unlike the uniformly reorienting harmonic-trap case. The sign is characterized exactly by only two angular Fourier modes, and the same two modes can be reconstructed from the stationary second and fourth moments of one position coordinate when the physical parameters are known.

Precisely, write the first two cosine coefficients of a symmetric turn-angle distribution \(\Pi\) as \(m_j=\int\cos(j\psi)\,\Pi(d\psi)\), and define \(A=\alpha(1-m_1)\), \(B=\alpha(1-m_2)\). With a trap relaxation rate \(\kappa>0\), propulsion \(v>0\), tumble rate \(\alpha>0\), and independent translational Brownian diffusivity \(D\ge0\), the stationary one-coordinate excess kurtosis is

\[
\mathcal K=\frac{\kappa(A-2B-3\kappa)}{(2\kappa+B)(3\kappa+A)}\left(\frac{v^2}{v^2+2D(\kappa+A)}\right)^2.
\]

Consequently \(\mathcal K>0\) if and only if \(A>2B+3\kappa\), and the thermal diffusivity cannot change its sign. In the canonical mixture of a direction reversal and a completely randomized direction,

\[
\Pi_p=p\,\delta_{\pi}+(1-p)\,\mathrm{Unif}(-\pi,\pi),\qquad 0\le p<1,
\]

positive kurtosis holds **exactly** when

\[
p>\frac13\quad\text{and}\quad\alpha>\frac{3\kappa}{3p-1}.
\]

No positional resetting is involved. For any symmetric admissible turn law, positivity requires \(\alpha>3\kappa/2\), with this lower bound sharp as an infimum over the above mixtures. If \(\alpha\) is also unknown in that mixture, the two positional moments recover both \(\alpha\) and \(p\).

## Assumptions and scope

Let \((X_t,\theta_t)\in\mathbb R^2\times(\mathbb R/2\pi\mathbb Z)\) satisfy

\[
dX_t=[-\kappa X_t+v(\cos\theta_t,\sin\theta_t)]\,dt+\sqrt{2D}\,dW_t.
\]

Independently of planar Brownian motion \(W\), at the times of a rate-\(\alpha\) Poisson process the heading changes by an independent increment \(\psi\sim\Pi\), modulo \(2\pi\). Assume \(\Pi\) is even under \(\psi\mapsto-\psi\) and has a positive uniform component: \(\Pi\ge\varepsilon\,\mathrm{Unif}(-\pi,\pi)\) for some \(\varepsilon>0\). These conditions ensure unique isotropic stationarity, \(A>0\), and \(B\ge0\). All results hold for arbitrary real \(\kappa,v,\alpha>0\) and \(D\ge0\) satisfying these assumptions. No small-rate, large-rate, or asymptotic limit is used in the moment formula.

Let \(Y=X_1\) denote the first Cartesian coordinate under the stationary law. Define its conventional excess kurtosis by \(\mathcal K=\mathbb E[Y^4]/(3\mathbb E[Y^2]^2)-1\). Under isotropy the equivalent radial formula is \(\mathcal K=\mathbb E[\|X\|^4]/(2\mathbb E[\|X\|^2]^2)-1\). Both formulas refer to the same normalized, **central** fourth cumulant because \(\mathbb E X=0\).

## Proof

**Existence, stationarity, and decoupling.** The uniform component of the turn law couples two heading chains at their first common fully randomized turn; thereafter they can use the same increments. The stable linear equation for \(X\) forgets its initial condition exponentially. A unique stationary law therefore exists, and rotational invariance forces uniform heading and isotropic position. In a two-sided stationary construction, identify the plane with \(\mathbb C\) and decompose \(X=Z+G\), where

\[
Z_t=v\int_{-\infty}^{t}e^{-\kappa(t-s)}e^{i\theta_s}\,ds,
\qquad
G_t=\sqrt{2D}\int_{-\infty}^{t}e^{-\kappa(t-s)}dW_s.
\]

These variables are independent. The centered isotropic Gaussian \(G\) has per-coordinate variance \(D/\kappa\). Also \(\lvert Z\rvert\le v/\kappa\), so all polynomial generator calculations below are justified.

**Closed co-rotating moment hierarchy.** Set \(U_t=Z_te^{-i\theta_t}\), and write \(M_{pq}=\mathbb E[U^p\overline U^{\,q}]\). Between tumbles \(\dot U=-\kappa U+v\), and each jump multiplies \(U\) by \(e^{-i\psi}\). For \(\lambda_j=\alpha(1-m_j)\), the stationary generator on \(U^p\overline U^{\,q}\) gives the exact identity

\[
[\kappa(p+q)+\lambda_{|p-q|}]M_{pq}
=v[pM_{p-1,q}+qM_{p,q-1}],\qquad M_{00}=1,
\]

where \(\lambda_0=0\), \(\lambda_1=A\), \(\lambda_2=B\). Evenness of \(\Pi\) makes these eigenvalues real; symmetry also makes the relevant moments real. Successively,

\[
M_{10}=\frac{v}{\kappa+A},\quad
M_{20}=\frac{2v^2}{(\kappa+A)(2\kappa+B)},\quad
M_{11}=\frac{v^2}{\kappa(\kappa+A)},
\]

\[
M_{21}=\frac{v(2M_{11}+M_{20})}{3\kappa+A},\qquad
M_{22}=\frac{vM_{21}}{\kappa}
=\frac{2v^4(3\kappa+B)}{\kappa^2(\kappa+A)(2\kappa+B)(3\kappa+A)}.
\]

Because \(\lvert U\rvert=\lvert Z\rvert\), we have \(s_Z=\mathbb E|Z|^2=M_{11}\) and \(f_Z=\mathbb E|Z|^4=M_{22}\). A separate check uses the ordered four-time angular correlations: among the six ordered sign words with two positive and two negative Fourier exponents, two have second-gap relaxation \(B\) and four have second-gap relaxation zero; the first and third gaps relax at rate \(A\). The four-time integral is

\[
f_Z=\frac{4v^4}{4\kappa(3\kappa+A)(\kappa+A)}
\left[\frac{2}{2\kappa+B}+\frac{4}{2\kappa}\right],
\]

identical to the moment hierarchy. This second expression does not use the co-rotating generator recursion.

**Kurtosis and its sign.** Gaussian isotropy and independence give, with \(s_G=2D/\kappa\),

\[
\mathbb E|X|^2=s_Z+s_G,\qquad
\mathbb E|X|^4=f_Z+4s_Zs_G+2s_G^2.
\]

Consequently the normalized excess kurtosis is \((f_Z/(2s_Z^2)-1)(s_Z/(s_Z+s_G))^2\). Substitution and simplification yield the formula in the Finding section. Every denominator and the dilution factor are strictly positive for the stated assumptions, proving the exact three-way sign classification.

Since \(-1\le m_1\le1\) and \(B\ge0\), the inequality \(A>2B+3\kappa\) implies \(2\alpha>3\kappa\). For the mixture \(\Pi_p\), one has \(m_1=-p\), \(m_2=p\), so \(A=\alpha(1+p)\), \(B=\alpha(1-p)\), and \(A-2B-3\kappa=\alpha(3p-1)-3\kappa\). This proves the asserted exact phase boundary. Taking \(p\uparrow1\) approaches the necessary \(3\kappa/2\) rate threshold, without using the nonergodic endpoint \(p=1\).

**Stationary inverse identification.** Suppose \(\kappa,v,D\) are known, and observe exact stationary \(V_2=\mathbb E[Y^2]\) and \(V_4=\mathbb E[Y^4]\). Put \(u=V_2-D/\kappa>0\), \(K=V_4/(3V_2^2)-1\), and \(K_a=K(V_2/u)^2\). From \(V_2=v^2/[2\kappa(\kappa+A)]+D/\kappa\), recover

\[
A=\frac{v^2}{2\kappa u}-\kappa.
\]

Now set \(c=(1+K_a)(3\kappa+A)/(\kappa+A)\). The fourth-moment formula gives \(c=(3\kappa+B)/(2\kappa+B)\); hence

\[
B=\kappa\frac{3-2c}{c-1}.
\]

Here \(1<c\le3/2\), so the inversion has no zero denominator. If \(\alpha\) is known, the coefficients are \(m_1=1-A/\alpha\), \(m_2=1-B/\alpha\). For the specific mixture \(\Pi_p\), even without known \(\alpha\), the parameters are uniquely recovered as \(\alpha=(A+B)/2\) and \(p=(A-B)/(A+B)\). This identifies the two Fourier modes only, not the entire turning-angle distribution.

## Verification

The included standalone \(\texttt{verify.py}\) uses exact rational arithmetic, evaluates the stationary complex-moment recursion and an independent ordered four-time integral, checks the Gaussian-convolution fourth moment, verifies the threshold and inversion identities for 1,532 admissible parameter cases, and reports two exact benchmarks. Running \(\texttt{python3 verify.py}\) yields:

```text
PASS: 1532 exact-rational model and inversion cases
Positive-kurtosis benchmark: 7/68 ; negative benchmark: -215/2714
```

The positive benchmark uses \(\kappa=v=1\), \(D=0\), \(\alpha=8\), \(p=3/4\). The negative benchmark uses the same parameters except \(p=1/10\). The exact identities are proved for all admissible parameters above; checking finitely many fractions does not replace those proofs.

## Relationship to prior work

Britton et al. (2026) derive free-space spatial moments under nonuniform turning-angle laws and explicitly recognize that the fourth spatial moment probes the second angular Fourier mode. The **new claim here is not** that these Fourier modes affect fourth moments in general; it is their exact *confined stationary* kurtosis formula, sharp sign boundary, and closed reconstruction from single-coordinate stationary moments. Guéneau, Majumdar, and Schehr (2026) derive the full harmonically confined stationary law for a run-and-tumble particle with *complete uniform* heading resampling. Their turning law corresponds to \(m_1=m_2=0\), which produces strictly negative kurtosis in the current formula. Sun, Ye, and Podgornik (2024/2025) provide an exact moment method with a separate zero-propulsion tumble state followed by an independent uniform run velocity; this is not a direction-preserving, increment-correlated jump kernel. Smith et al. (2022) analyze a particular \(90^\circ\) turning rule in a trap, rather than the general symmetric mixture with arbitrary second angular mode. Garcia-Millan and Pruessner (2021) treat the one-dimensional harmonic run-and-tumble problem with diffusion. We credit each prior formula and model rather than claiming the generic moment technique is new.

## Limitations

The result assumes a harmonic isotropic trap, constant propulsion speed and tumble rate, an even turn-angle law with a strictly positive uniform component, and independent isotropic translational Brownian noise. Chiral (asymmetric) turning laws, anisotropic traps, full position resets, time-dependent parameters, and interactions are outside scope. The reconstruction requires known \(\kappa,v,D\), and extracting individual Fourier coefficients also requires known \(\alpha\), except in the specified two-parameter mixture. Low activity or high thermal noise can make empirical recovery ill-conditioned, although the exact inverse remains valid. No experimental detectability bound or complete distributional reconstruction is claimed. Some broader moment frameworks may subsume the calculation by specialization; the precise novel-coverage boundary and publication priority require independent expert confirmation. Numerical checks are finite and are not independent proof certification.

## References

1. C. Britton, Z. Zhang, S. Han, and T. Bertrand, *Run-and-tumble particles with preferred reorientation* (2026), arXiv:2608.23519, first publicly submitted 2026-08-24. https://arxiv.org/abs/2608.23519
2. M. Guéneau, S. N. Majumdar, and G. Schehr, *Exact Stationary State of a d-dimensional Run-and-Tumble Particle in a Harmonic Potential* (2026), arXiv:2602.08436. https://arxiv.org/abs/2602.08436
3. A. Sun, F. Ye, and R. Podgornik, *Exact moments for a run and tumble particle in a harmonic trap with a finite tumble time* (2024/2025), arXiv:2409.00578. https://arxiv.org/html/2409.00578v2
4. N. R. Smith, P. Le Doussal, S. N. Majumdar, and G. Schehr, *Exact position distribution of a harmonically-confined run-and-tumble particle in two dimensions* (2022), arXiv:2207.10445. https://arxiv.org/abs/2207.10445
5. R. Garcia-Millan and G. Pruessner, *Run-and-tumble motion in a harmonic potential: field theory and entropy production* (2021), Journal of Statistical Mechanics 063203. https://doi.org/10.1088/1742-5468/ac014d
