# Exact angular risk law and sharp sketch-design bound for rank-one Nyström

## Finding
For each real \(a\ge b>0\), let \(A=\operatorname{diag}(a,b)\). Given a nonzero real probe \(g\), the one-column, unshifted Nyström approximation is
\[
\widehat A=Ag(g^{\mathsf T}Ag)^{-1}g^{\mathsf T}A.
\]
Set \(\kappa=a/b\) and \(R=\lVert A-\widehat A\rVert_{\mathrm F}/b\). For a standard two-coordinate Gaussian probe, \(R\) has the exact law
\[
R\overset d=\frac{\kappa}{1+(\kappa-1)T},\qquad T\sim\operatorname{Beta}(1/2,1/2).
\]
For \(\kappa>1\), its distribution function on \(1\le r\le\kappa\) is
\[
\mathbb P(R\le r)=1-\frac2\pi\arcsin\sqrt{\frac{\kappa/r-1}{\kappa-1}}.
\]
In particular, \(\mathbb E R=\sqrt\kappa\) and
\[
\mathbb E R^2=\frac{(\kappa+1)\sqrt\kappa}{2}.
\]
Since the best rank-one squared Frobenius error is \(b^2\), the last expression is the exact expected squared-error competitive ratio. It grows as \(\kappa^{3/2}/2\), even though every fixed \(\kappa\) has bounded error.

More generally, for every \(q>0\), the moment \(M_q(\kappa)=\mathbb E R^q\) satisfies the sharp high-contrast trichotomy
\[
\begin{aligned}
\lim_{\kappa\to\infty}M_q(\kappa)&=\frac{\Gamma(1/2-q)}{\sqrt\pi\,\Gamma(1-q)}&& (0<q<1/2),\\
M_{1/2}(\kappa)&=\frac{\log\kappa}{\pi}+O(1),\\
M_q(\kappa)&\sim\frac{\Gamma(q-1/2)}{\sqrt\pi\,\Gamma(q)}\kappa^{q-1/2}&& (q>1/2).
\end{aligned}
\]

Among all random unit probes \(u\) with \(\mathbb E[uu^{\mathsf T}]=I_2/2\), for each \(\kappa>1\) and each \(q>0\), the unique minimizing **angular-energy condition** is \(u_1^2=u_2^2=1/2\) almost surely, and the sharp common minimum is
\[
\inf\mathbb E R^q=\left(\frac{2\kappa}{\kappa+1}\right)^q.
\]
Independent two-coordinate Rademacher signs, normalized to unit length, attain the minimum simultaneously for all positive moments. Consequently their expected squared-error competitive ratio is \(4\kappa^2/(\kappa+1)^2<4\), in contrast to the unbounded Gaussian ratio. Equality here describes squared coordinate energies, not a unique distribution over the four signs.

## Assumptions and scope
All statements concern exact real arithmetic, an unshifted single-probe Nyström approximation, a strictly positive two-by-two diagonal matrix, and a nonzero probe. The directional isotropy condition is \(\mathbb E uu^{\mathsf T}=I_2/2\), with \(\lVert u\rVert_2=1\) almost surely. Gaussian probes are independent standard real normals; Rademacher probes have independent equiprobable signs. The choice of eigenbasis is explicit: the coordinate-sign benchmark is **not** claimed to remain optimal after an unknown orthogonal rotation. At \(\kappa=1\), every probe gives \(R=1\), so the strict uniqueness assertion is inapplicable. The quantity \(R\) is a Frobenius-norm error divided by the *optimal* rank-one Frobenius-norm error \(b\).

## Proof
**Residual identity.** Write \(u=g/\lVert g\rVert_2\), \(d=au_1^2+bu_2^2>0\), and \(v=(-u_2,u_1)^{\mathsf T}\). Multiplying out the Nyström formula yields
\[
A-\widehat A=\frac{ab}{d}\begin{pmatrix}u_2^2&-u_1u_2\\-u_1u_2&u_1^2\end{pmatrix}=\frac{ab}{d}vv^{\mathsf T}.
\]
The residual is positive semidefinite of rank one, and \(\lVert v\rVert_2=1\). Therefore its Frobenius, spectral, and trace norms all equal \(ab/d\). Substituting \(T=u_1^2\) and \(a=\kappa b\) gives \(R=\kappa/[1+(\kappa-1)T]\). The Eckart--Young theorem, or the diagonal spectrum directly, gives the optimal rank-one error \(b\).

**Gaussian distribution.** For independent standard normals \(g_1,g_2\), the direction is uniform on the unit circle, so \(T=g_1^2/(g_1^2+g_2^2)\) has density \([\pi\sqrt{t(1-t)}]^{-1}\) for \(0<t<1\). Monotonic inversion gives the displayed cumulative distribution function. For any \(q>0\),
\[
M_q(\kappa)=\frac{\kappa^q}{\pi}\int_0^1\frac{dt}{[1+(\kappa-1)t]^q\sqrt{t(1-t)}}.
\]
The elementary angular integrals
\[
\frac2\pi\int_0^{\pi/2}\frac{d\theta}{\kappa\cos^2\theta+\sin^2\theta}=\kappa^{-1/2},\quad
\frac2\pi\int_0^{\pi/2}\frac{d\theta}{(\kappa\cos^2\theta+\sin^2\theta)^2}=\frac{\kappa+1}{2\kappa^{3/2}}
\]
follow by \(z=\tan\theta\) and, for the second integral, differentiation of the first with respect to the coefficients. Multiplication by \(\kappa\) and \(\kappa^2\) proves the first and second moments.

**Moment asymptotics.** If \(q<1/2\), the integrand defining \(M_q\) converges pointwise to \(t^{-q}/[\pi\sqrt{t(1-t)}]\) and is bounded by the same integrable function. Its beta integral equals the stated gamma ratio. If \(q>1/2\), substitute \(t=s/\kappa\) on \([0,1/2]\); dominated convergence after division by \(\kappa^{q-1/2}\) gives
\[
\frac1\pi\int_0^\infty s^{-1/2}(1+s)^{-q}\,ds=\frac{\Gamma(q-1/2)}{\sqrt\pi\,\Gamma(q)}.
\]
The contribution from \(t\ge1/2\) is bounded uniformly in \(\kappa\), hence negligible at this scale. At \(q=1/2\), splitting the integral into \(t\lesssim\kappa^{-1}\), \(\kappa^{-1}\ll t\ll1\), and \(t\gtrsim1\) gives the logarithmic coefficient \(1/\pi\) and a bounded remainder; equivalently, the integral is \((2/\pi)K(1-\kappa^{-1})\) in complete-elliptic-integral parameter convention and the classical endpoint expansion is \(K(1-\varepsilon)=\log(4/\sqrt\varepsilon)+o(1)\).

**Directional minimization.** For a unit probe, isotropy implies \(\mathbb E T=1/2\). For \(\kappa>1\) and \(q>0\), the function \(t\mapsto[\kappa/(1+(\kappa-1)t)]^q\) has strictly positive second derivative on \([0,1]\). Jensen's inequality gives \(M_q\ge[2\kappa/(\kappa+1)]^q\), with equality exactly when \(T=1/2\) almost surely. The uniform four-sign law has \(u=(\pm1,\pm1)/\sqrt2\), fulfills isotropy and attains equality for every \(q\). Taking \(q=2\) proves the squared-error ratio and the bound strictly below four at every finite \(\kappa\).

## Verification
The standalone `verify.py` checks the residual identity with rational arithmetic for several matrix/probe choices, the Jensen inequality on explicit isotropic discrete directional laws, and the Gaussian first- and second-moment integrals by deterministic angular quadrature. It also prints the exact high-contrast ratios for selected square contrasts. Its finite checks corroborate but do not replace the analytic proof; no inference about arbitrary distributions is made from enumeration.

## Relationship to prior work
Persson, Boullé, and Kressner (arXiv:2404.00960, sections 2.1--2.4 and appendix) define Gaussian Nyström sketches and establish finite-/infinite-dimensional norm bounds with target rank at least two and positive oversampling (their Frobenius expectation theorem assumes at least four extra columns). Those bounds neither specialize to the one-column no-oversampling law nor compare angle-balanced sign probes. Tropp, Yurtsever, Udell, and Cevher (arXiv:1706.05736, sections 2 and 4 and Appendix A) analyze fixed-rank Nyström truncation with sketch size exceeding the target rank; their deterministic projector identity is compatible with the residual identity here but their relative-error theorem does not cover equal sketch and target rank one. Carson and Daužickaitė (arXiv:2205.13355, sections 1--4) analyze finite-precision single-pass Nyström and exhibit no-oversampling experiments, not the present exact-arithmetic one-column angular distribution or all-moment classification. A deterministic projector identity and standard beta integrals are established tools; the specific full risk law and isotropic-law comparison are the asserted contribution, not the Nyström construction itself.

## Limitations
The result is two-dimensional and diagonal in the sampling basis; it is not a general-purpose assertion that sign probes outperform Gaussian probes on arbitrarily oriented matrices. The minimizer can require knowledge of the eigenbasis and thus is a benchmark rather than an automatically deployable oblivious sketch. All moments remain finite for each fixed \(0<b\le a<\infty\); only *relative* risk grows with contrast. The result does not address oversampling, rank truncation after larger sketches, stabilized finite-precision implementations, or higher-dimensional spectra. Published bounds at larger sketch sizes remain applicable in their settings. Exhaustiveness of all historical specialized literature is not claimed.

## References
1. David Persson, Nicolas Boullé, and Daniel Kressner, *Randomized Nyström approximation of non-negative self-adjoint operators*, arXiv:2404.00960, first public 2024-04-01, https://arxiv.org/html/2404.00960v2.
2. Joel A. Tropp, Alp Yurtsever, Madeleine Udell, and Volkan Cevher, *Fixed-Rank Approximation of a Positive-Semidefinite Matrix from Streaming Data*, arXiv:1706.05736, first public 2017-06-18, https://arxiv.org/html/1706.05736v1.
3. Erin Carson and Ieva Daužickaitė, *Single-pass Nyström approximation in mixed precision*, arXiv:2205.13355, first public 2022-05-26, https://arxiv.org/abs/2205.13355.
