# Sharp fourth-cumulant range at optimal diffusion for chiral tumblers

## Finding

A planar active particle undergoes continuous rotational diffusion, constant angular drift, and independent Poisson-distributed angular tumbles. At the rate that maximizes long-time positional diffusion, *every symmetric tumble law* has a negative longitudinal fourth-cumulant growth rate, but its magnitude is not universal. The exact attainable interval and its equality cases are as follows.

Let \(D>0\) be rotational diffusivity, \(\Omega>D\) the positive intrinsic angular drift, \(v>0\) the propulsion speed, and \(\nu\) any symmetric probability measure on the circle for the independent angular increments at tumbles. Write
\[
c_j=\int_{\mathbb T}\cos(j\eta)\,\nu(d\eta),\quad j=1,2,\qquad c_1<1,
\]
and select the positive tumbling rate
\[
\lambda_* = \frac{\Omega-D}{1-c_1}.
\]
For an initially uniform orientation, let \(X_T=v\int_0^T\cos\Theta_s\,ds\), and define
\[
K_4(\nu)=\lim_{T\to\infty}\frac{\mathbb E X_T^4-3(\mathbb E X_T^2)^2}{T}.
\]
Then the limit exists, and with
\[
B_*=4D+(\Omega-D)\frac{1-c_2}{1-c_1}
\]
it is precisely
\[
\boxed{K_4(\nu)=-\frac{3v^4}{\Omega(B_*^2+4\Omega^2)}.}
\]
Moreover, the following is the exact range over *all* such symmetric tumble measures:
\[
\boxed{
-\frac{3v^4}{\Omega(16D^2+4\Omega^2)}
\ \le\ K_4(\nu)\ <\ -\frac{3v^4}{20\Omega^3}.}
\]
The lower endpoint is attained exactly by measures supported on zero-angle and half-turn tumbles, with a strictly positive probability of half-turns. Every interior value is attained by a symmetric fixed-angle pair \(\nu=\tfrac12(\delta_{\varphi}+\delta_{-\varphi})\) for a suitable \(0<\varphi<\pi\). The upper endpoint is a supremum, approached by \(\varphi\downarrow0\) and \(\lambda_*\to\infty\), but is never attained at any finite optimizing rate. The ratio between the largest possible absolute fourth-cumulant rate and its infimum is exactly
\[
\frac{5\Omega^2}{4D^2+\Omega^2}\in(1,5).
\]
Thus diffusivity-optimal symmetric reorientation strategies are identical at the two-point transport level but remain distinguishable by a sharp non-Gaussian fluctuation invariant.

## Assumptions and scope

The angular process on \(\mathbb T=\mathbb R/(2\pi\mathbb Z)\) is
\[
\Theta_t=\Theta_0+\Omega t+\sqrt{2D}\,W_t+\sum_{j=1}^{N_t}\eta_j\pmod{2\pi},
\]
where \(W\) is standard real Brownian motion, \(N\) is an independent Poisson process of rate \(\lambda\), the jumps \(\eta_j\) are independent with common law \(\nu\), and \(\Theta_0\) is independent and uniform on the circle. There is no translational Brownian noise in the definition of \(X_T\); adding independent Gaussian translational diffusion leaves \(K_4\) unchanged. All claims hold for every real \(D>0\), \(\Omega>D\), \(v>0\), and every symmetric probability measure with \(c_1<1\), including atomic measures. No assumption of a smooth angular density is imposed. We use the fourth *cumulant*, not the raw fourth moment.

The longitudinal variance rate for arbitrary \(\lambda\ge0\), with \(A=D+\lambda(1-c_1)\), is
\[
\lim_{T\to\infty}\frac{\operatorname{Var}(X_T)}{T}
=\frac{v^2A}{A^2+\Omega^2}.
\]
Hence the per-coordinate effective diffusion coefficient, defined by dividing this rate by two, is maximized uniquely over \(\lambda\ge0\) at \(A=\Omega\), giving \(\lambda_*\) above and maximal coordinate diffusivity \(v^2/(4\Omega)\). In the alternative convention \(\mathbb E|\boldsymbol X_T|^2/(2T)\), the maximum is \(v^2/(2\Omega)\). This second-moment optimization is prior work and is not claimed as new.

## Proof

**1. Tilted angular generator and cumulant rate.** For a smooth periodic test function \(f\), the angular generator is
\[
Lf(\theta)=D f''(\theta)+\Omega f'(\theta)
+\lambda\int_{\mathbb T}[f(\theta+\eta)-f(\theta)]\,\nu(d\eta).
\]
The Fourier functions \(e_n(\theta)=e^{in\theta}\) diagonalize \(L\):
\[
Le_n=-[Dn^2+\lambda(1-c_n)-in\Omega]e_n.
\]
Because \(D>0\), the stationary eigenvalue zero is simple and the remaining spectrum is separated from zero in real part by at least \(D\). Multiplication by \(v\cos\theta\) is bounded, so the perturbed operator \(L_k=L+kv\cos\theta\) has a simple eigenvalue \(\Lambda(k)\) analytic near \(k=0\). The Feynman--Kac semigroup and its spectral gap show that, for the stationary angular start, every finite cumulant per unit time converges to the corresponding derivative of \(\Lambda\) at zero. Explicitly,
\[
\lim_{T\to\infty}\frac{\kappa_j(X_T)}T=\Lambda^{(j)}(0)
\quad\text{for }j=2,4.
\]
Spatial rotation by \(\pi\) changes \(\cos\theta\) to its negative without changing \(L\), so \(\Lambda(k)=\Lambda(-k)\).

**2. Exact fourth-order Fourier perturbation.** Put
\[
r_n=[Dn^2+\lambda(1-c_n)-in\Omega]^{-1},\qquad n=\pm1,\pm2,
\]
and expand the eigenpair with the eigenfunction normalized to have circle average one:
\[
\Lambda(k)=a_2k^2+a_4k^4+O(k^6),\qquad
f_k=1+kf_1+k^2f_2+k^3f_3+\cdots.
\]
At order one, the \(\pm1\) coefficients of \(f_1\) are \(vr_{\pm1}/2\). At order two, the \(\pm2\) coefficients of \(f_2\) are \(v^2r_{\pm1}r_{\pm2}/4\), with constant coefficient fixed at zero by normalization. Projecting the order-two equation onto the constant mode yields
\[
a_2=\frac{v^2}{4}(r_1+r_{-1}).
\]
At order three, the \(\pm1\) coefficients are
\[
(f_3)_{\pm1}=\frac{v^3}{8}r_{\pm1}^2r_{\pm2}-\frac{a_2v}{2}r_{\pm1}^2.
\]
Projecting the order-four equation onto the constant mode therefore yields the *exact* coefficient
\[
a_4=\frac{v^4}{16}\left[r_1^2r_2+r_{-1}^2r_{-2}
-(r_1+r_{-1})(r_1^2+r_{-1}^2)\right].
\]
Only the first and second angular harmonics can occur in a closed four-step Fourier path. In particular, finite-mode truncation to these harmonics is exact at this derivative order, not an approximation to an infinite-order expansion.

**3. Substitution at the transport optimum.** Let \(B=4D+\lambda(1-c_2)\). At \(\lambda=\lambda_*\), the first-harmonic damping is \(A=\Omega\), so
\[
r_1=\frac{1+i}{2\Omega},\quad
r_{-1}=\frac{1-i}{2\Omega},\quad
r_2=\frac1{B-2i\Omega}.
\]
Consequently \(r_1^2+r_{-1}^2=0\) and
\[
a_4=-\frac{v^4}{8\Omega(B^2+4\Omega^2)}.
\]
Since \(\Lambda^{(4)}(0)=24a_4\), this gives the advertised formula for \(K_4\). The variance rate is \(\Lambda''(0)=2a_2=v^2/(2\Omega)\) at the optimum.

**4. Sharp distributional range and equality.** Write \(t=\cos\eta\). The elementary identity \(1-\cos(2\eta)=2(1-t)(1+t)\) gives
\[
R_\nu:=\frac{1-c_2}{1-c_1}=
2\frac{\int (1-t)(1+t)\,\nu(d\eta)}{\int(1-t)\,\nu(d\eta)}.
\]
This is twice the average of \(1+t\) under the nonzero probability measure proportional to \((1-t)\nu(d\eta)\). Therefore \(0\le R_\nu<4\). Equality at zero holds exactly when the original law is supported on \(\{0,\pi\}\), with positive mass at \(\pi\); equality at four is impossible because \(1-t>0\) precisely off \(t=1\). Hence
\[
4D\le B_*=4D+(\Omega-D)R_\nu<4\Omega.
\]
The function \(B\mapsto-3v^4/[\Omega(B^2+4\Omega^2)]\) is strictly increasing for \(B>0\), proving both sharp bounds and equality cases. For \(\nu=\tfrac12(\delta_\varphi+\delta_{-\varphi})\),
\[
R_\nu=2(1+\cos\varphi),\quad
B_*=4D+2(\Omega-D)(1+\cos\varphi),
\]
which ranges continuously over the entire half-open interval as \(\varphi\) goes from \(\pi\) toward zero. Comparing the two magnitude endpoints gives the final sharp ratio.

## Verification

The accompanying standalone `verify.py` checks the analytic fourth-order coefficient with symbolic algebra, the optimized simplification, exact rational cases for half-turn, quarter-turn and symmetric \(\pi/3\) tumbles, and the sharp endpoint identities. It independently diagonalizes a nine-mode Fourier truncation at two small tilts using high precision and compares the recovered quartic Taylor coefficient with the exact expression. All checks passed. The finite Fourier calculation provides a diagnostic only; the infinite-dimensional eigenvalue and full-law extremal statements follow from the proof above.

For example, at \((D,\Omega,v)=(1,3,2)\), the three angular laws and their optimally chosen rates yield
\[
\begin{array}{c|c|c|c}
\text{law}&\lambda_*&B_*&K_4\\\hline
\pi\text{-reversal}&1&4&-4/13\\
\pm\pi/2&2&8&-4/25\\
\pm\pi/3&4&10&-2/17
\end{array}
\]
while all have the same coordinate diffusivity \(v^2/(4\Omega)=1/3\).

## Relationship to prior work

Olsen and Löwen (arXiv:2405.14326, first public 2024-05-23) established the general angular propagator, velocity correlation and universal maximum of the long-time diffusivity for symmetric tumbles. Those ingredients and the rate \(\lambda_*\) are accepted as known. Their analysis does not state a fourth-cumulant rate or an extremal range across all maximizing tumble laws.

Villa-Torrealba and collaborators (arXiv:2002.02872, 2020) computed fourth displacement moments and excess kurtosis for partial reorientations of *nonchiral* run-and-tumble particles and separately analyzed rotationally diffusing direction reversals. Their fourth-moment expressions are relevant precedent for harmonic dependence, but neither the intrinsically chiral combined model nor the sharp optimally tuned distributional range is implied by their displayed results.

Britton, Zhang, Han and Bertrand (arXiv:2608.23519, first public 2026-08-24) supply a general field-theoretic method to calculate fourth and higher moments of a preferred-reorientation run-and-tumble process. Their treatment demonstrates sensitivity of fourth moments to the second angular harmonic. This overlaps the broad mechanism, but their published statements do not identify the positive rotational-diffusion, intrinsic-chirality, max-diffusivity subclass and its exact sharp fourth-cumulant range and equality law. Some component formulas might be derivable by applying their general formalism; no claim is made that the underlying perturbative technique is new.

## Limitations

The conclusion concerns the asymptotic fourth-cumulant growth of one Cartesian displacement coordinate, not its sign for every finite time and not higher-order cumulants. The result requires \(D>0\), \(\Omega>D\), a symmetric angular increment law, independent homogeneous Poisson tumbles, constant propulsion, no interactions and a stationary initial orientation. It does not optimize fourth cumulants under a prescribed fixed tumbling rate, and the upper extremum is not attained at a finite rate. No independent validation or proof of publication priority is asserted.

## References

1. K. Stølevik Olsen and H. Löwen, *Optimal diffusion of chiral active particles with strategic reorientations*, arXiv:2405.14326 (2024), https://arxiv.org/abs/2405.14326. First public: 2024-05-23.
2. A. Villa-Torrealba, C. Chávez Raby, P. de Castro and R. Soto, *Run-and-tumble bacteria slowly approaching the diffusive regime*, arXiv:2002.02872 (2020), https://arxiv.org/abs/2002.02872.
3. C. Britton, Z. Zhang, S. Han and T. Bertrand, *Run-and-tumble particles with preferred reorientation*, arXiv:2608.23519 (2026), https://arxiv.org/abs/2608.23519.
