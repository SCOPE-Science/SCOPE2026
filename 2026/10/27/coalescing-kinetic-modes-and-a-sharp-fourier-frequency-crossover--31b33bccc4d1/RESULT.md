# Coalescing kinetic modes and a sharp Fourier-frequency crossover in a dephased lattice gas

## Finding

For a spatially localized, momentum-uniform initial state of the one-dimensional BGK continuum limit of a dephased nearest-neighbor lattice gas, the spatial Fourier response has an exact decomposition into a pair of elementary damped modes and a smaller branch-spectrum remainder. For every collision rate \(\lambda>0\), the two modes change from nonoscillating real exponential rates to an oscillatory conjugate pair at the **sharp spatial frequency** \(|k|=\lambda\). At the collision point the leading response is \(2\lambda t e^{-\lambda t}\), rather than a simple exponential. In a frequency window of width \(t^{-2}\), its normalized profile is an explicit entire hyperbolic-sine/sine crossover.

Precisely, write \(\Phi_\lambda(k,t)=\int_{\mathbb R}e^{-ikx}\rho(x,t)\,dx\). For \(k\ne0\), let \(\kappa=|k|\), \(a^2=\lambda^2-\kappa^2\), and define the *entire* real function
\[
\mathcal S(z)=\sum_{j=0}^{\infty}\frac{z^j}{(2j+1)!}.
\]
The response admits the exact real identity
\[
\boxed{\Phi_\lambda(k,t)=e^{-\lambda t}\bigl(2\lambda t\mathcal S((\lambda^2-\kappa^2)t^2)+R_{\lambda,\kappa}(t)\bigr),}
\]
where the remainder has the oscillatory-integral representation, for \(t>0\),
\[
R_{\lambda,\kappa}(t)=\frac2\pi\int_{\kappa}^{\infty}
\frac{\sqrt{y^2-\kappa^2}}{\lambda^2+y^2-\kappa^2}\sin(yt)\,dy.
\]
The integral is an ordinary conditionally convergent improper oscillatory integral. At every fixed \(\lambda>0\), \(\kappa>0\), its sharp leading behavior is
\[
\boxed{R_{\lambda,\kappa}(t)=\frac{\sqrt{2\kappa/\pi}}{\lambda^2t^{3/2}}\sin(\kappa t+3\pi/4)+O_{\lambda,\kappa}(t^{-5/2}).}
\]
The estimate is uniform when \(\kappa\) ranges over a compact positive interval.

Consequently, defining \(a=\sqrt{\lambda^2-\kappa^2}\) when \(0<\kappa<\lambda\) and \(b=\sqrt{\kappa^2-\lambda^2}\) when \(\kappa>\lambda\),
\[
\Phi_\lambda(k,t)=
\begin{cases}
 e^{-\lambda t}\bigl[(2\lambda/a)\sinh(at)+O(t^{-3/2})\bigr],&0<\kappa<\lambda,\\
 e^{-\lambda t}\bigl[2\lambda t+O(t^{-3/2})\bigr],&\kappa=\lambda,\\
 e^{-\lambda t}\bigl[(2\lambda/b)\sin(bt)+O(t^{-3/2})\bigr],&\kappa>\lambda.
\end{cases}
\]
All displayed fixed-frequency asymptotic errors are absolute errors inside the square brackets.

More sharply, for any \(M>0\), for every \(\eta\in[-M,M]\) and sufficiently large \(t\), set
\[
\kappa_t=\sqrt{\lambda^2-\eta/t^2}.
\]
Then uniformly on that interval,
\[
\boxed{\frac{e^{\lambda t}}t\Phi_\lambda(\kappa_t,t)
=2\lambda\mathcal S(\eta)+O_{\lambda,M}(t^{-5/2}).}
\]
Thus \(\mathcal S(\eta)=\sinh(\sqrt\eta)/\sqrt\eta\) for positive \(\eta\), is \(1\) at zero, and is \(\sin(\sqrt{-\eta})/\sqrt{-\eta}\) for negative \(\eta\). The Fourier response at \(k=0\) is exactly \(1\) and is deliberately excluded from the fixed-nonzero-frequency edge statement.

## Assumptions and scope

Fix arbitrary \(\lambda>0\). Let \(n(x,p,t)\) be the distributional solution of
\[
\partial_t n(x,p,t)+\sin(p)\partial_x n(x,p,t)=\lambda[\rho(x,t)-n(x,p,t)],\qquad
\rho(x,t)=\frac1{2\pi}\int_{-\pi}^{\pi}n(x,p,t)\,dp,
\]
with \(n(x,p,0)=\delta_0(x)\) for all \(p\in[-\pi,\pi]\). The initial spatial measure has mass one. Equivalently, the position starts at zero, its velocity is \(\sin p\) with initially uniform \(p\), and the momentum is refreshed independently and uniformly at Poisson rate \(\lambda\). The theorem concerns this continuum kinetic model, not the unapproximated microscopic quantum chain. The spatial Fourier convention is \(e^{-ikx}\), and the time Laplace convention is \(e^{-st}\).

The limits above hold for each fixed nonzero \(k\), with stated compact-uniformity, and for the specifically tuned \(t^{-2}\) frequency window. No uniform asymptotic statement across \(k=0\), or for collision rate tending to zero simultaneously, is asserted.

## Proof

**1. Renewal transform.** Averaging the deterministic velocity \(\sin p\) over uniform momentum gives \(J_0(\kappa t)\) for a collision-free flight. Conditioning on the first refresh yields the exact renewal identity
\[
\Phi_\lambda(k,t)=e^{-\lambda t}J_0(\kappa t)
+\lambda\int_0^t e^{-\lambda s}J_0(\kappa s)\Phi_\lambda(k,t-s)\,ds.
\]
Since \(\int_0^\infty e^{-ut}J_0(\kappa t)\,dt=(u^2+\kappa^2)^{-1/2}\) for \(\operatorname{Re}u>0\), its Laplace transform is
\[
\widehat\Phi_\lambda(k,s)=\frac1{\sqrt{(s+\lambda)^2+\kappa^2}-\lambda},\qquad \operatorname{Re}s>0.
\]
The principal analytic continuation of the square root is normalized to be positive for real \(s+\lambda>0\). This transform itself is already implicit in Coppola's published renewal solution; novelty is not claimed for it.

**2. Exact pole/branch separation.** With \(u=s+\lambda\), and \(a^2=\lambda^2-\kappa^2\), algebraic rationalization gives
\[
\frac1{\sqrt{u^2+\kappa^2}-\lambda}
=\frac{2\lambda}{u^2-a^2}+\frac1{\sqrt{u^2+\kappa^2}+\lambda}.
\]
The first inverse Laplace transform is exactly \(2\lambda t\mathcal S(a^2t^2)\), including at \(a=0\). For the second term the square-root branch points lie at \(u=\pm i\kappa\). Deforming the Bromwich contour around cuts \(i[\kappa,\infty)\) and \(-i[\kappa,\infty)\), and pairing the complex-conjugate jumps, gives
\[
\mathcal L^{-1}_u\bigl[(\sqrt{u^2+\kappa^2}+\lambda)^{-1}\bigr](t)
=\frac2\pi\int_{\kappa}^\infty\frac{\sqrt{y^2-\kappa^2}}{\lambda^2+y^2-\kappa^2}\sin(yt)\,dy.
\]
The positive-frequency integral is conditionally convergent: its integrand equals \(y^{-1}\sin(yt)+O(y^{-3})\) at infinity; Dirichlet's test applies for each \(t>0\). The complementary Laplace transform has no poles on this sheet, so no residue is omitted.

**3. Sharp cut-edge estimate.** Put \(z=y-\kappa\). The amplitude in the integral has the endpoint expansion
\[
\frac{\sqrt{y^2-\kappa^2}}{\lambda^2+y^2-\kappa^2}
=\frac{\sqrt{2\kappa}}{\lambda^2}z^{1/2}+O_{\lambda,\kappa}(z^{3/2}).
\]
Choose a smooth cutoff near \(z=0\). The standard Abel-regularized Fourier integral \(\int_0^\infty z^{1/2}e^{itz}\,dz=e^{3\pi i/4}\Gamma(3/2)t^{-3/2}\) produces the leading coefficient \(\sqrt{2\kappa/\pi}/\lambda^2\). The endpoint remainder is \(O(t^{-5/2})\). Outside the cutoff, repeated integrations by parts produce an arbitrarily small inverse-power error, because the amplitude is smooth and its positive-order derivatives are integrable; the \(1/y\) tail has no finite-endpoint boundary term after using a smooth partition. All estimates are uniform when \(\kappa\) stays in a fixed compact subset of \((0,\infty)\).

**4. Root classification and critical window.** The elementary term has exponents \(-\lambda\pm\sqrt{\lambda^2-\kappa^2}\). For \(\kappa<\lambda\), these are two real decay rates; for \(\kappa>\lambda\) they are a complex conjugate pair and the elementary contribution is \(2\lambda e^{-\lambda t}\sin(bt)/b\). At equality, the coincident simple poles become a second-order pole and contribute \(2\lambda t e^{-\lambda t}\). The cut-edge term is only \(O(e^{-\lambda t}t^{-3/2})\) at every fixed nonzero \(\kappa\).

For \(\kappa=\kappa_t\) above, the exact pole term becomes \(2\lambda t\mathcal S(\eta)\), *without approximation*. Compact-uniform control of the remainder from step 3, together with division by \(t\), proves the stated \(O(t^{-5/2})\) uniform error. This also proves the full sign-changing sine profile on the oscillatory side, not just convergence of absolute values.

## Verification

The standalone script `verify.py` numerically reconstructs the Fourier response independently by inverse Laplace transformation and by the Bessel-renewal convolution; it checks the exact separation and asymptotic residual coefficient for positive and negative sides of the threshold, and the time-dependent critical frequency window. The proof above, not a finite collection of numerical tests, establishes the uniform statements. Run `python verify.py` using Python 3 and `mpmath`.

## Relationship to prior work

Coppola, *Exact solution to a Bhatnagar–Gross–Krook-type equation for quantum lattice gases with dephasing noise* (arXiv:2501.12155; Phys. Rev. B 112, 024315, 2025), establishes this kinetic equation and its exact renewal solution, including Appendix A's Fourier–Laplace kernel. Its principal long-time application is the ballistic-to-diffusive *spatial density* crossover. Those results are prior art; they imply the starting transform of the present proof. The new assertion is the wave-number-resolved pole-coalescence classification with an explicit algebraic cut-edge correction and a compact-uniform \(t^{-2}\) critical layer.

Romatschke, *Retarded correlators in kinetic theory: branch cuts, poles and hydrodynamic onset transitions* (2016), previously identified pole/branch-cut reorganizations for a different, higher-dimensional relaxation-time Boltzmann system. The broad existence of kinetic onset transitions is not new. The arcsine-velocity dispersion relation, its two-mode critical merging at \(|k|=\lambda\), the explicit cut-edge amplitude, and the sine/hyperbolic-sine finite-time window are model-specific statements not established in that source.

## Limitations

All statements refer to the continuum BGK approximation, not an exact equality with the underlying finite-lattice quantum evolution. The input is initially uniform in momentum; other momentum preparations modify the response. The analysis is for a strictly positive fixed rate and one-dimensional cosine-band velocity. The asymptotics at fixed nonzero frequency are absolute: at zeros of an oscillating leading term no relative error bound is asserted. Uniformity is confined to compact positive-frequency sets and the specified critical window. The elementary transform and the general physics of kinetic poles were already available in the cited literature, so independent evaluation of the degree of mathematical novelty of the sharper coefficient and crossover remains warranted.

## References

1. Michele Coppola, *Exact solution to a Bhatnagar–Gross–Krook-type equation for quantum lattice gases with dephasing noise*, arXiv:2501.12155v1 (first public 2025-01-21), *Physical Review B* **112**, 024315 (2025), https://arxiv.org/abs/2501.12155 ; https://doi.org/10.1103/29z8-3t16 .
2. Paul Romatschke, *Retarded correlators in kinetic theory: branch cuts, poles and hydrodynamic onset transitions*, arXiv:1512.02641, *European Physical Journal C* **76**, 352 (2016), https://arxiv.org/abs/1512.02641 ; https://doi.org/10.1140/epjc/s10052-016-4169-7 .
3. P. B. Warren, O. Behrend and R. Harris, *Hydrodynamic behavior of lattice Boltzmann and lattice Bhatnagar-Gross-Krook models*, *Physical Review E* **50**, 4586 (1994), https://doi.org/10.1103/PhysRevE.50.4586 .
