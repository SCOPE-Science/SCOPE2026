# Sharp diffusion gain from localized direction reversals in two-zone run-and-reverse motion

## Finding

Fix a spatial fraction \(0<f<1\), a mean swimming speed \(\bar v>0\), and a mean direction-reversal rate \(\bar\lambda>0\). A particle on the real line has orientation \(S_t\in\{-1,+1\}\), follows \(\dot X_t=S_tv(X_t)\), and reverses orientation at local Poisson intensity \(\lambda(X_t)\). Both coefficients are periodic in space with a two-zone period: zone 1 occupies fraction \(f\), zone 2 fraction \(1-f\), the respective velocities satisfy \(v_1\ge v_2>0\), and local reversal intensities obey \(\lambda_i\ge0\). Constrain the **spatial arithmetic means**, not travel-time averages, by
\[
fv_1+(1-f)v_2=\bar v,\qquad f\lambda_1+(1-f)\lambda_2=\bar\lambda.
\]

Let \(D_{\mathrm{hom}}=\bar v^2/(2\bar\lambda)\) be the homogeneous run-and-reverse diffusivity. Define the actual long-time dispersion by \(D_{\mathrm{eff}}=\lim_{t\to\infty}\operatorname{Var}(X_t)/(2t)\). Then, for any fixed pair of speeds with \(v_1>v_2\), the **unique** reversal-rate allocation maximizing diffusion places all reversals in the faster zone:
\[
\lambda_1=\bar\lambda/f,\qquad \lambda_2=0.
\]
The resulting exact enhancement at speed contrast \(r=v_1/v_2\ge1\) is
\[
R_f(r):=\frac{D_{\mathrm{eff}}}{D_{\mathrm{hom}}}
=\frac{r^2}{(fr+1-f)^2[f+(1-f)r]}.
\]
For each fixed \(0<f<1\), there is one global optimal contrast
\[
r_*(f)=\frac{1-f+\sqrt{9f^2-2f+1}}{2f},\qquad
\sup R_f=R_f(r_*(f))>1.
\]
The equality configuration is unique subject to zone 1 being the faster zone. In equal-length zones the sharp gain is \(32/27\), with \(v_1=4\bar v/3\), \(v_2=2\bar v/3\), \(\lambda_1=2\bar\lambda\), \(\lambda_2=0\). Conversely, even with both spatial mean resources fixed,
\[
\sup_{0<f<1}\;\sup_{v_i,\lambda_i}D_{\mathrm{eff}}/D_{\mathrm{hom}}=\infty,
\qquad R_f(r_*(f))=\frac1{4f}+\frac12+O(f)
\quad(f\downarrow0).
\]
Thus the optimal, increasingly narrow high-speed, high-reversal patch eliminates any universal enhancement ceiling under the stated mean constraints.

For equal fractions another exact design boundary is available. Writing \(v_{1,2}=\bar v(1\pm\epsilon)\), \(\lambda_{1,2}=\bar\lambda(1\pm\eta)\), where \(0<\epsilon<1\) and \(-1\le\eta\le1\), gives
\[
D_{\mathrm{eff}}/D_{\mathrm{hom}}=\frac{(1-\epsilon^2)^2}{1-\epsilon\eta}.
\]
The dispersion exceeds its homogeneous benchmark exactly when \(\eta>2\epsilon-\epsilon^3\). Such enhancement is possible for \(0<\epsilon<(\sqrt5-1)/2\) and impossible for larger speed contrasts, including equality at the critical contrast.

## Assumptions and scope

The switching process is a **direction reversal** at intensity \(\lambda(x)\), not a random reorientation which might preserve the incoming sign. Coefficients are strictly positive speeds, nonnegative reversal intensities, periodic with any physical period length \(L>0\), and have positive total reversal intensity. At zero-rate portions the process travels ballistically; it remains irreducible because one zone has positive intensity. At zone interfaces the particle crosses without reflection, delay, or random redirection; its instantaneous speed changes to the speed on the new side. The probability laws may start from any deterministic position and orientation. The coefficient and optimizer statements are for the class of *spatially piecewise-constant two-zone profiles only*, with fixed fraction \(f\) unless explicitly optimized over fractions.

## Proof

**1. Exact stationary measure and corrector.** For a general positive bounded periodic speed \(v(x)\) and nonnegative bounded periodic switching intensity \(\lambda(x)\), put
\[
I=\int_0^L\frac{dx}{v(x)},\qquad J=\int_0^L\frac{\lambda(x)}{v(x)}\,dx>0.
\]
The Markov process \((X_t\bmod L,S_t)\) has generator
\[
(\mathcal L h)_s=s v(x)\partial_x h_s+\lambda(x)(h_{-s}-h_s).
\]
The stationary distribution has both orientation densities equal to \((2Iv(x))^{-1}\). Indeed both directed stationary currents \(\pm v\pi_\pm=\pm(2I)^{-1}\) have zero derivative and their reversal exchange balances. Irreducibility from the positive-rate zone makes this stationary law unique and ergodic. For the centered velocity observable \(g_s(x)=s v(x)\), find a periodic Poisson corrector \(-\mathcal L\chi=g\) by setting \(c=L/J\), \(\chi_+-\chi_-=c\), and
\[
\chi'_+(x)=\chi'_-(x)=-1+\frac{c\lambda(x)}{v(x)}.
\]
The right side integrates to \(-L+cJ=0\), so the corrector is periodic, continuous across interfaces, and bounded. Direct substitution verifies both generator equations, including in each piecewise-constant zone.

The process \(M_t=X_t+\chi_{S_t}(X_t\bmod L)-\chi_{S_0}(X_0\bmod L)\) is a square-integrable martingale, whose only jumps are orientation reversals of amplitude \(\pm c\). Accordingly, its predictable quadratic variation is \(\langle M\rangle_t=c^2\int_0^t\lambda(X_s)\,ds\). Ergodicity gives the asymptotic rate \(c^2 J/I\). Boundedness of the corrector transfers this variance rate to \(X_t\), yielding the exact nonlocal spatial homogenization formula
\[
\boxed{D_{\mathrm{eff}}=\frac{L^2}{2IJ}}
\]
for every initial state. This corrector proof does not rely on a small-persistence approximation. It supplies the analytical input for the design result; general velocity-jump homogenization itself is known prior work.

**2. Two-zone resource allocation.** For constants on the two zones, divide the integrals by \(L\) to obtain
\[
D_{\mathrm{eff}}=
\bigl[2(f/v_1+(1-f)/v_2)(f\lambda_1/v_1+(1-f)\lambda_2/v_2)\bigr]^{-1}.
\]
For fixed positive unequal speeds, minimize the second parenthesis under \(f\lambda_1+(1-f)\lambda_2=\bar\lambda\) and \(\lambda_i\ge0\). A unit of reversal budget costs \(1/v_i\) in that parenthesis, so every unit must go to the faster phase, uniquely. For equal speeds every admissible reversal allocation gives the same dispersion, a harmless degeneracy at \(r=1\).

**3. Optimization over speeds.** Set \(r=v_1/v_2\ge1\). The mean speed constraint gives \(v_2=\bar v/(fr+1-f)\), yielding the displayed \(R_f(r)\). Its logarithmic derivative has the same sign as
\[
-\bigl(fr^2+(f-1)r-2f\bigr).
\]
The quadratic is negative at \(r=1\), increases through exactly one positive root \(r_*(f)>1\), and tends to positive infinity. Therefore \(R_f\) increases strictly to its unique global maximum and then decreases to zero as \(r\to\infty\). Direct substitution of \(f=1/2\) gives \(r_*=2\), \(R_*=32/27\) and the stated unique coefficients.

**4. Narrow-patch limit and sign boundary.** Expand the explicit root near \(f=0\) to get \(r_*(f)=f^{-1}-1+2f+O(f^2)\). Substitution into \(R_f\) gives \(R_*(f)=1/(4f)+1/2+O(f)\), proving unbounded enhancement while each individual configuration has finite, positive speeds and finite rates. The equal-half identity follows by substituting the contrast parametrization into the exact two-zone formula. The strict inequality \((1-\epsilon^2)^2/(1-\epsilon\eta)>1\) is equivalent to \(\eta>2\epsilon-\epsilon^3\). The requirement \(\eta\le1\) and factorization \(1-2\epsilon+\epsilon^3=(1-\epsilon)(1-\epsilon-\epsilon^2)\) establish the golden-ratio threshold, with equality never yielding strict improvement.

## Verification

The standalone `verify_two_phase_motility.py` verifies the symbolic derivative, critical-point identity, exact equal-half optimum, and gain-threshold algebra; checks 240 randomly sampled fractions, speeds and switching rates, comparing optimized gains against 40 randomly sampled contrasts per case; and independently constructs nine finite-state upwind velocity-jump chains at three spatial resolutions. For each chain it constructs the entire Markov generator, solves the Poisson corrector numerically, and compares its quadratic-variation diffusivity against the continuum formula. The lattice approximation converges as expected with shrinking cell size. Run `python verify_two_phase_motility.py` with Python 3, NumPy, SciPy and SymPy. These finite diagnostics are *not* used as an infinite proof; the argument above establishes the stated quantifiers.

## Relationship to prior work

Solon, Cates and Tailleur (2015) explain variable motility and coarse-grained local diffusivity in run-and-tumble active matter. Angelani, Di Leonardo and Paoluzzi (2015) solve first-passage problems with spatially variable swimming speed and tumbling rates; their objective and boundary conditions are different from the present fixed-spatial-mean infinite-line design problem. Lutscher and Hillen (2021) directly address correlated random walks in periodic, two-patch heterogeneous landscapes and establish homogenization theory. **The general homogenization framework and the existence of effective diffusivity are not claimed as new.** The claim here is solely the sharp *simultaneous fixed-mean allocation and contrast optimization*, the exact two-patch gain ceiling for fixed fraction, and the absence of a universal ceiling as that fraction shrinks. The article by Angelani and Garra (2019) treats spatially variable-speed RTPs; its accessible abstract describes propagators, confined first-passage, and relaxation but its full paper could not be inspected here, leaving a genuine historical-priority risk. No previously inspected source or targeted research record supplied an exact equivalent budget envelope. This does not certify absolute novelty.

## Limitations

This theorem does not establish an optimal design among arbitrary continuously varying motility profiles, heterogeneous thermal diffusion, asymmetric direction-specific reversals, or partially reflecting interfaces. Concentrating switching into a vanishing zone requires unbounded local switching intensity and local speed despite fixed means; practical engineering bounds will impose a finite ceiling. The optimization addresses asymptotic *variance diffusivity*, not finite-time transport, reaction capture, energetic cost, or persistence at a fixed observation time. Some supporting studies are more recent than the archival focal paper and do not determine archival membership. No independent audit has been performed.

## References

1. A. P. Solon, M. E. Cates and J. Tailleur, *Active Brownian Particles and Run-and-Tumble Particles: a Comparative Study*, arXiv:1504.07391, first submitted 2015-04-28, https://arxiv.org/abs/1504.07391.
2. L. Angelani, R. Di Leonardo and M. Paoluzzi, *First-passage time of run-and-tumble particles*, arXiv:1506.08046, first submitted 2015-06-26, https://arxiv.org/abs/1506.08046.
3. F. Lutscher and T. Hillen, *Correlated random walks in heterogeneous landscapes: Derivation, homogenization, and invasion fronts*, AIMS Mathematics 6 (2021), 8920–8948, https://doi.org/10.3934/math.2021518.
4. L. Angelani and R. Garra, *Run-and-tumble motion in one dimension with space-dependent speed*, Physical Review E 100 (2019), 052147, https://doi.org/10.1103/PhysRevE.100.052147.
