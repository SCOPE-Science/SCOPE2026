# A persistent Lorentzian memory footprint under arbitrarily rapid probe-only resetting

## Finding
For a Brownian probe harmonically coupled to one Brownian bath coordinate, with Poisson resets of **the probe only**, the stationary probe autocovariance is a positive sum of two exact exponentials at every positive bath-friction ratio and reset rate. In the strong-reset limit, a fast correlation layer and a suppressed but persistent bath-memory component coexist. The latter survives after multiplying the fixed-positive-lag covariance by the square of the resetting rate, and produces a nonzero Lorentzian addition to the correspondingly rescaled stationary power spectrum.

More precisely, let the dimensionless reset rate be \(r>0\) and the bath-friction ratio be \(g>0\). Define
\[
 M=\frac{2(gr+g+1)}{r(gr+2g+1)},\qquad
 K=\frac{gr+2g+2}{r(gr+2g+1)},\qquad
 d=1+r-\frac KM,
\]
\[
 \Delta=\sqrt{(1+r+g^{-1})^2-4r/g},\qquad
 \lambda_{\mathrm s,\mathrm f}=\frac{1+r+g^{-1}\mp\Delta}{2},
\]
\[
 a_{\mathrm s}=M\frac{\lambda_{\mathrm f}-d}{\Delta},\qquad
 a_{\mathrm f}=M\frac{d-\lambda_{\mathrm s}}{\Delta}.
\]
Both coefficients are strictly positive, and the stationary covariance at lag \(t\in\mathbb R\) is exactly
\[
 C_r(t)=\mathbb E[X_0X_t]=a_{\mathrm s}e^{-\lambda_{\mathrm s}|t|}
 +a_{\mathrm f}e^{-\lambda_{\mathrm f}|t|}.
\]
With the two-sided angular-frequency convention \(S_r(\nu)=\int_{\mathbb R}e^{-i\nu t}C_r(t)\,dt\),
\[
 S_r(\nu)=2\sum_{j\in\{\mathrm s,\mathrm f\}}
 \frac{a_j\lambda_j}{\lambda_j^2+\nu^2}.
\]
For fixed \(g>0\), the strong-reset limits are
\[
 \lim_{r\to\infty}rC_r(u/r)=2e^{-u}\quad (u\ge0),\qquad
 \lim_{r\to\infty}r^2C_r(t)=e^{-t/g}\quad(t>0),
\]
\[
 \lim_{r\to\infty}r^2S_r(\nu)=4+\frac{2g}{1+g^2\nu^2}
 \quad(\nu\in\mathbb R\text{ fixed}).
\]
These limits are locally uniform within the indicated domains, but the fixed-positive-lag limit does not extend to \(t=0\). In particular, the rescaled spectrum retains a bath-specific Lorentzian even though the leading, rapidly reset stationary position distribution is bath-independent.

The normalized integrated correlation time has the exact identity
\[
 \tau_{\mathrm{int}}(r,g)=\frac1{C_r(0)}\int_0^\infty C_r(t)\,dt
 =\frac1r\left(1+g\frac KM\right)>\frac1r,
 \qquad \lim_{r\to\infty}r\tau_{\mathrm{int}}=1+\frac g2.
\]
Moreover, for all sufficiently large \(r\), the two positive covariance components contribute equally at exactly one positive lag \(t_*(r)\); it obeys
\[
 t_*(r)=\frac{\log(a_{\mathrm f}/a_{\mathrm s})}{\lambda_{\mathrm f}-\lambda_{\mathrm s}}
 =\frac{\log(2r)}r+O_g\!\left(\frac{\log r}{r^2}\right).
\]

## Assumptions and scope
The process is the stationary version of the dimensionless overdamped coupled Langevin system
\[
 dX_t=(-X_t+Q_t)\,dt+\sqrt2\,dW_t,\qquad
 dQ_t=\frac{X_t-Q_t}{g}\,dt+\sqrt{\frac2g}\,dB_t,
\]
where \(W,B\) are independent standard Brownian motions. At points of an independent rate-\(r\) Poisson process, \(X_t\) is instantaneously set to zero and \(Q_t\) is left unchanged. All assertions concern arbitrary \(g,r>0\), except the stated asymptotics, which hold at fixed positive \(g\) as \(r\to\infty\). The covariance is centered: stationarity gives \(\mathbb E[X_t]=\mathbb E[Q_t]=0\). The result is specific to instantaneous probe-only reset, a single bath coordinate, and these thermal-noise normalizations.

## Proof
**Existence and stationary covariances.** For the generator including the probe reset, apply it to \(V(x,q)=x^2+gq^2\). Direct calculation yields
\[
 \mathcal LV=-2(x-q)^2-rx^2+4.
\]
Because \(r,g>0\), the negative quadratic part is coercive relative to \(V\). Together with independent nondegenerate diffusion in both coordinates this gives a unique invariant distribution with finite second moments by the standard Foster--Lyapunov/irreducibility argument. Applying the generator to \(x,q,x^2,xq,q^2\) first shows zero stationary means and then yields
\[
 0=-(2+r)M+2K+2,\qquad
 0=\frac Mg-(1+g^{-1}+r)K+H,\qquad
 0=\frac2g(K-H+1),
\]
where \(M=\mathbb E[X^2]\), \(K=\mathbb E[XQ]\), \(H=\mathbb E[Q^2]\). Solving gives the displayed \(M,K\) and \(H=(r+2)M/2\). The one-time variance \(M\) agrees with the value previously computed by Santra and Das; its derivation here is not asserted to be new.

**Two-time semigroup.** On linear observables the generator acts through
\[
 A=\begin{pmatrix}-(1+r)&1\\g^{-1}&-g^{-1}\end{pmatrix}.
\]
Its eigenvalues are \(-\lambda_{\mathrm s}\) and \(-\lambda_{\mathrm f}\), which are real, distinct and negative since \(\det(-A)=r/g>0\), \(\operatorname{tr}(-A)>0\), and \(\Delta^2=(1+r-g^{-1})^2+4/g>0\). Stationary Markov regression gives
\[
 C_r(t)=(1,0)e^{At}(M,K)^T\quad(t\ge0).
\]
The initial value is \(C_r(0)=M\); the right derivative is \(C_r'(0+)=-(1+r)M+K=-Md\). The two eigenvalues and these initial conditions uniquely fix the displayed amplitudes \(a_{\mathrm s},a_{\mathrm f}\).

**Strict positive weights.** The number \(d=r(2gr+3g+2)/[2(gr+g+1)]\) lies strictly between the two positive roots of
\[
 p(z)=gz^2-[g(1+r)+1]z+r.
\]
Indeed a direct exact factorization gives
\[
 p(d)=-\frac{gr\bigl(2g^2r^2+7g^2r+6g^2+8gr+12g+6\bigr)}{4(gr+g+1)^2}<0.
\]
Hence \(\lambda_{\mathrm s}<d<\lambda_{\mathrm f}\), proving both exponential weights strictly positive. Integrating the two exponentials also proves that the normalized covariance is completely monotone on positive lags.

**Integrated lag and high-rate singular layer.** The matrix \(-A\) is invertible, with first row of \((-A)^{-1}\) equal to \((1/r,g/r)\). Integration of the semigroup therefore gives
\[
 \int_0^\infty C_r(t)\,dt=\frac{M+gK}{r},
\]
proving the exact integrated correlation time, the strict inequality, and its limit because \(K/M\to1/2\) as \(r\to\infty\). Elementary expansions at fixed \(g>0\) give
\[
 \lambda_{\mathrm s}=g^{-1}+O_g(r^{-1}),\quad
 \lambda_{\mathrm f}=r+1+O_g(r^{-1}),\quad
 a_{\mathrm s}=r^{-2}+O_g(r^{-3}),\quad
 a_{\mathrm f}=2r^{-1}+O_g(r^{-2}).
\]
Substitution proves the two distinct covariance scalings, their stated compact uniformities, and the unique equal-contribution lag for sufficiently large \(r\). Finally, Fourier transforming each integrable exponential yields \(S_r\). In the fixed-frequency limit its fast term tends, after multiplication by \(r^2\), to \(4\), while its slow term tends to \(2g/(1+g^2\nu^2)\). This proves the spectral law without interchanging an uncontrolled Fourier integral and a nonuniform time-domain limit.

## Verification
A complete Python 3 standard-library checker is provided as `verify.py`. Run it from this directory with `python3 verify.py`. It performs 268 deterministic assertions, including 125 exact rational stationary-balance, mode-placement, and integrated-lag checks; comparisons between a direct matrix-exponential formula and the independent spectral decomposition; and quantitative checks of the strong-reset limits at several positive bath ratios and frequencies. The finite computations are consistency checks only. The infinite-lag and strong-reset statements follow from the displayed exact algebra and asymptotic expansions.

## Relationship to prior work
Santra and Das, arXiv:2603.17027v1 (later published as New Journal of Physics 28, 074601), introduce and analyze this exact probe-only resetting model, derive stationary one-time moments, characterize spatial distributions, and study relaxation of transient variances. Their full accessible preprint and journal text do not state the present stationary two-time covariance, its positive-mode theorem, the exact integrated lag, or the singular strong-reset spectral Lorentzian.

Goswami, arXiv:2412.19564, independently studies harmonic probe--bath coupling with the bath left unreset, including one-time marginals, relaxation, and first passage. Its model can contain the present thermal parameter specialization, but its inspected text does not state a stationary two-time spectral limit or the displayed strong-reset coefficient. The more general underlying model is credited, not claimed as new here.

Biswas, Dubbeldam, Sandev, and Pal, arXiv:2412.09260, compute two-time correlations in a viscoelastic generalized-Langevin setting under *full renewal of the memory-bearing dynamics*. Their derivation expressly resets the memory along with the position, and its exponential reset factor does not imply the surviving fixed-lag mode for a bath left unreset. Classical linear Markov-semigroup theory provides the basic regression method and is not new; the claimed contribution is the singular two-scale and frequency-resolved statement in the specific nonrenewing resetting model.

## Limitations
The result does not cover multiple bath relaxation modes, non-Poisson resetting, finite-speed returns, nonlinear coupling, or nonthermal colored driving. The limit \(r^2C_r(t)\to e^{-t/g}\) is only for fixed strictly positive lags, not at zero; the spectral limit holds at each fixed frequency, not uniformly as frequency scales with \(r\). Spectral amplitudes are second-order observables and do not identify the full stationary distribution. Independent mathematical and originality audits have not been performed. Broader partial-reset spectral theory could contain an equivalent specialization; the literature comparisons cannot establish absolute novelty.

## References
1. I. Santra and D. Das, *Resetting in a viscoelastic bath: the bath remembers*, arXiv:2603.17027v1, first posted 2026-03-17; *New Journal of Physics* **28**, 074601 (2026), DOI:10.1088/1367-2630/ae868c.
2. K. Goswami, *Stochastic resetting in a nonequilibrium environment*, arXiv:2412.19564, *Physical Review E* **111**, 014150 (2025), DOI:10.1103/PhysRevE.111.014150.
3. A. Biswas, J. L. A. Dubbeldam, T. Sandev, and A. Pal, *A resetting particle embedded in a viscoelastic bath*, arXiv:2412.09260, *Chaos* **35**, 031102 (2025), DOI:10.1063/5.0253019.
4. D. C. Rose, H. Touchette, I. Lesanovsky, and J. P. Garrahan, *Spectral properties of simple classical and quantum reset processes*, *Physical Review E* **98**, 022129 (2018), DOI:10.1103/PhysRevE.98.022129. Its state-resetting spectral framework is general background, not a result for the present partial reset.
