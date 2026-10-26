# Exact non-Gevrey derivatives and a log-periodic Fourier fingerprint of proportional Brownian resetting

## Finding
For Brownian motion of diffusivity \(D>0\), subject at Poisson rate \(r>0\) to proportional resets \(x\mapsto qx\), \(0<q<1\), let \(f\) be the stationary density and \(\alpha=\sqrt{r/D}\). Two exact, complementary fingerprints of the contraction are established:

1. For every integer \(n\geq0\),
\[
f^{(2n)}(0)=(-1)^n f(0)\alpha^{2n}q^{-n^2}\prod_{j=0}^{n-1}(1-q^{2j+1}),\qquad f^{(2n+1)}(0)=0.
\]
In particular \(f\) is smooth and real analytic away from the resetting fixed point \(0\), but is not Gevrey of any finite order in any neighborhood of \(0\).

2. Set \(a=\log(1/q)\), \(t=\log(|k|/\alpha)>0\), and \(s=\{t/a\}\). The stationary Fourier transform \(\phi(k)=\int_{\mathbb R} e^{ikx}f(x)\,dx\) obeys
\[
\log\phi(k)=-\frac{t^2}{a}-t-P_q(s)+R_q(t,s),
\quad 0<R_q(t,s)\leq\frac{q^2e^{-2t}}{1-q^2}.
\]
The smooth one-periodic profile \(P_q\) has the absolutely convergent Fourier series
\[
P_q(s)=\overline P_q-\sum_{\ell=1}^\infty\frac{\cos(2\pi\ell s)}{\ell\sinh(\pi^2\ell/a)}.
\]
Thus the normalized logarithmic spectrum retains a strictly nonconstant periodic modulation in \(\log|k|/\log(1/q)\) for every fixed genuine partial-reset factor \(q\in(0,1)\).

## Assumptions and scope
The Brownian generator is \(D\partial_{xx}\), corresponding to variance \(2Dt\) in free evolution; resetting is instantaneous and globally independent of the Brownian motion. Every reset maps the current position to \(q\) times that position, with no additive noise. The invariant density is centered and even. All constants are for a fixed \(0<q<1\); no uniformity as \(q\to0\) or \(q\to1\) is asserted. The order-zero empty product equals \(1\).

Define \((z;Q)_m=\prod_{j=0}^{m-1}(1-zQ^j)\), with \((z;Q)_\infty\) the corresponding convergent infinite product. A useful absolutely convergent definition of the profile is
\[
P_q(s)=a s(1-s)
+\sum_{m=0}^{\infty}\log(1+e^{-2a(s+m)})
+\sum_{m=1}^{\infty}\log(1+e^{-2a(m-s)}),\quad 0\leq s\leq1.
\]
Its endpoint values coincide, and periodic extension is smooth.

## Proof
**Existence, characteristic function, and smoothness.** At stationarity, the generator yields
\[
D f''(x)-rf(x)+\frac rq f(x/q)=0.
\]
Equivalently, the stationary characteristic function satisfies
\(\phi(k)=\phi(qk)/(1+k^2/\alpha^2)\), hence
\[
\phi(k)=\prod_{j=0}^{\infty}\big(1+q^{2j}k^2/\alpha^2\big)^{-1}.
\]
This is the characteristic function of the convergent independent sum \(\sum_{j\ge0}q^j L_j\) with iid centered Laplace variables \(L_j\) of scale \(1/\alpha\); this proves existence and uniqueness of the stationary law by contraction. For every fixed exponent \(m\ge0\), the product satisfies \(|k|^m\phi(k)\to0\) rapidly enough for Fourier inversion of any order: indeed, choosing arbitrarily many initial factors bounds \(\phi(k)=O(|k|^{-2N})\) for each \(N\). Consequently \(f\in C^\infty(\mathbb R)\), even, and \(f(0)>0\).

**Exact derivatives and the Gevrey obstruction.** Differentiating the stationary equation \(2n\) times at \(0\) is legitimate and yields
\[
f^{(2n+2)}(0)=-\alpha^2q^{-(2n+1)}(1-q^{2n+1})f^{(2n)}(0).
\]
Iteration gives the stated derivative formula. Since \(\prod_{j\ge0}(1-q^{2j+1})=(q;q^2)_\infty>0\), the magnitude is asymptotic to \(f(0)(q;q^2)_\infty\alpha^{2n}q^{-n^2}\). For arbitrary finite Gevrey order \(\sigma\), arbitrary \(C,R>0\), and all sufficiently large \(n\), this exceeds \(CR^{2n}((2n)!)^\sigma\), because its logarithm has leading term \(n^2\log(1/q)\), while the logarithm of a factorial Gevrey bound is \(O(n\log n)\). Thus no finite-order Gevrey estimate holds at the origin.

**Analyticity off the origin.** Partial fractions of the product give the inverse Fourier representation, for \(x\ne0\),
\[
f(x)=\frac{\alpha}{2(q^2;q^2)_\infty}
\sum_{j=0}^\infty\frac{(-1)^j q^{j^2}}{(q^2;q^2)_j}
 e^{-\alpha q^{-j}|x|}.
\]
The series converges locally normally for complex \(x\) on either half-plane \(\operatorname{Re}x>0\) or \(\operatorname{Re}x<0\), with the sign in the exponential chosen accordingly. It therefore defines holomorphic continuations on those half-planes, proving real analyticity away from \(0\). The partial-fraction coefficient follows explicitly from
\(\prod_{h\ne j}(1-q^{2(h-j)})^{-1}=(-1)^j q^{j(j+1)}/[(q^2;q^2)_j(q^2;q^2)_\infty]\).

**Sharp high-frequency law.** For \(t=a(N+s)\), integer \(N=\lfloor t/a\rfloor\) and \(0\le s<1\), take the logarithm of the exact product. Split the terms at \(j=N\) and rewrite \(\log(1+e^{2u})=2u+\log(1+e^{-2u})\) when \(u\ge0\). The elementary sum is
\(2\sum_{j=0}^N(t-aj)=t^2/a+t+a s(1-s)\).
Completing the finite remainder to the infinite sum defining \(P_q(s)\) leaves exactly
\[
R_q(t,s)=\sum_{m=N+1}^\infty\log(1+e^{-2a(s+m)}).
\]
Every summand is positive, and \(\log(1+u)\le u\) gives the displayed upper bound.

To prove nonconstancy without a numerical resolution argument, twice differentiate the profile and sum its translated logistic kernels:
\[
P_q''(s)=-2a+a^2\sum_{j\in\mathbb Z}\operatorname{sech}^2(a(s+j)).
\]
Poisson summation, justified by exponential integrability with derivatives, and
\(\int_{\mathbb R}\operatorname{sech}^2(u)e^{-i\xi u}\,du=\pi\xi/\sinh(\pi\xi/2)\), give the stated Fourier cosine coefficients. Their absolute summability and strictly nonzero first harmonic show \(P_q\) is smooth and not constant for any finite \(a>0\). This completes the theorem.

## Verification
The standalone `verify.py` performs 104 independent numerical assertions: direct Fourier-inversion moments against the derivative recurrence; real-space residue-series values against Fourier inversion; the phase contrast against its Poisson-summation Fourier coefficients; and the positive exact remainder against its bound. Execute `python verify.py` with NumPy, SciPy and mpmath. Its finite checks corroborate identities; the proof above establishes the claims for all allowed parameters.

## Relationship to prior work
Pierce (2022, arXiv:2204.07215) derives the proportional-reset master equation and real-space stationary series. Tal-Friedman, Roichman and Reuveni (2022, arXiv:2205.03363) derive the stationary Fourier product and independent-Laplace representation. Those antecedents, including existence and low-order moments, are not claimed as original. Di Bello and coauthors (2023, arXiv:2305.13722) treat more general time-dependent partial resetting. Grzywny and collaborators (2024, arXiv:2412.15626) establish general stationary smoothness for stable partial resetting, so smoothness alone is also not claimed as original. The present point is the exact superfactorial fixed-point derivative growth together with a nonconstant, quantitatively controlled logarithmic spectral phase. Classical q-product and theta identities supply related general analytic machinery; their possible implication of the spectral phase is a priority risk rather than a claim of independent invention of those identities.

## Limitations
The fixed-point Gevrey conclusion assumes strictly positive Brownian diffusivity and a single deterministic contraction factor between zero and one. The high-frequency phase can be exponentially small for factors close to one; its nonvanishing is mathematical, not a claim of practical observability at a specified noise floor. No finite-sample detection theorem, finite-frequency minimax bound, multi-dimensional extension, drift case, or novel invariant-distribution formula is established. Novelty is a same mathematical model literature assessment, not independent peer review; standard theta/q-product asymptotic results may supply a shorter alternate proof.

## References
- J. Kevin Pierce, *An advection-diffusion process with proportional resetting* (arXiv:2204.07215, first submitted 14 April 2022). https://arxiv.org/abs/2204.07215
- O. Tal-Friedman, Y. Roichman and S. Reuveni, *Diffusion with Partial Resetting* (arXiv:2205.03363, first submitted 6 May 2022; Physical Review E 106, 054116). https://arxiv.org/abs/2205.03363
- C. Di Bello and collaborators, *Time-dependent probability density function for partial resetting dynamics* (arXiv:2305.13722, first submitted 2023). https://arxiv.org/abs/2305.13722
- T. Grzywny and collaborators, *Stationary states for stable processes with partial resetting* (arXiv:2412.15626, first submitted 2024). https://arxiv.org/abs/2412.15626
- Standard q-Pochhammer and Jacobi-theta identities (background mathematical identities, not claimed as new).
