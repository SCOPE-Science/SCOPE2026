# Review

**Same-model review: passed. Cross-model review: not yet performed.**

## Correctness

The two benchmark chaoses were checked directly from their exact moment-generating functions. For the all-positive spectrum,
\[
K_+(t)=-t\sqrt{m/2}-\frac m2\log(1-\sqrt{2/m}\,t),
\]
which gives \(\kappa_3=2\sqrt2/\sqrt m\) and \(\kappa_4=12/m\). For the perfectly balanced spectrum,
\[
K_0(t)=-\frac m4\log(1-2t^2/m),
\]
so all odd cumulants vanish and \(\kappa_4=12/m\). In both cases equal-magnitude eigenvalues give \(r_4=m\).

The positive-spectrum maximum reduces exactly to the growing-shape Gamma triangular array treated by Bose, Dasgupta and Maulik. Expanding their explicit centering equation yields the Gaussian-Gumbel-scale displacement
\[
\frac43\frac{(\log p)^{3/2}}{\sqrt m},
\]
with the next correction smaller by \(O(\sqrt{\log p/m})\).

For the balanced spectrum, the exact saddle point and Legendre transform were recomputed from \(K_0\):
\[
t_x=x-2x^3/m+8x^5/m^2+O(x^7/m^3),
\]
\[
I_m(x)=x^2/2-x^4/(2m)+4x^6/(3m^2)+O(x^8/m^3).
\]
The same law is a normalized sum of \(m/2\) i.i.d. normal products, so standard analytic Cramer/saddlepoint tilting supplies the Gaussian Mills prefactor uniformly for \(x\asymp\sqrt{\log p}\) when \(m/\log p\to\infty\). This gives a tail-ratio exponent \(2(\log p)^2/m\) at the Gaussian extreme threshold. Higher terms are negligible at the stated critical scale because their relative size is \(O(\log p/m)\).

The shifted-Gumbel Kolmogorov profile was differentiated explicitly. For \(F(y)=e^{-e^{-y}}\),
\[
\sup_y\{F(y)-F(y-\delta)\}
=\exp[-\delta/(e^\delta-1)](1-e^{-\delta}).
\]
Potential failure modes examined included normalization by \(m\) versus \(m/2\), a missing factor two in the balanced mgf, confusing the fourth cumulant with kurtosis, and using the general sufficient \((\log p)^6\) condition as though it were necessary. The constants and normalizations are consistent after these checks.

## Originality

The immediate literature target is Cai and Hu (2026). Their Section 3 defines the fourth-order effective rank \(r_4=(\sum\lambda_r^2)^2/\sum\lambda_r^4\), proves
\[
d_K(\max_j Q_j,\max_j Z_j)\lesssim r_{4,\min}^{-1/6}\log p,
\]
and records \(r_{4,\min}/(\log p)^6\to\infty\) as a sufficient Gaussianization condition. Their text permits arbitrary spectral signs and identifies the fourth cumulant \(12/r_4\) as the coordinatewise fourth-moment obstruction. The paper does not state a third-cumulant or sign-balance refinement, and its phase boundary figure is explicitly described as schematic.

The positive-spectrum ingredient is not claimed as new extreme-value theory. Bose, Dasgupta and Maulik (2008) prove a Gumbel theorem for Gamma triangular arrays with growing shape and give the centering equation used here. They explicitly relate their proof to Anderson, Coles and Hüsler (1997), whose broader Cramer-series framework covers maxima of normalized sums. Thus the cubic and quartic moderate-deviation mechanisms are classical in isolation.

Targeted searches for chi-square maxima versus Gaussian maxima, signed or balanced second-chaos maxima, variance-gamma triangular maxima, effective-rank sign balance, and third-cumulant phase corrections did not locate the paired statement proved here: two flat spectra with the same \(r_4=m\) but distinct sharp thresholds \((\log p)^3\) and \((\log p)^2\), together with their explicit critical Kolmogorov profiles.

Anderson, Coles and Hüsler (1997) could not be inspected in full text; its abstract, bibliographic record, and Bose et al.'s detailed description were inspected. Because general Cramer-series theory can encode high-order corrections under different notation, that paper and related older triangular-array extreme-value work are the principal residual originality risk. The originality assessment is therefore to the best of our knowledge and is confined to the fixed-effective-rank sign comparison and its sharp maximum-calibration consequences.

## Value

The result sharpens the interpretation of a very recent high-dimensional chaos phase-transition theorem. It shows constructively that fourth-order effective rank, while a valid uniform control parameter, is not a complete sharp phase coordinate: cancellation of the third cumulant changes the required rank by one power of \(\log p\). The explicit shifted-Gumbel limits quantify not only whether Gaussian calibration fails but how much it fails at the critical scales.

This also suggests a concrete direction for stronger general theory: a hierarchy based on signed spectral power sums, with the first nonvanishing standardized cumulant determining the relevant extreme moderate-deviation scale.

## Limitations

The result treats independent coordinates and flat equal-magnitude spectra. It does not classify partially balanced signs, unequal eigenvalue magnitudes, dependent coordinates, or general spectral decay. The equivalences are stated inside \(m/\log p\to\infty\), and the result concerns the Gaussian-chaos target rather than the preceding finite-sample approximation from a canonical U-statistic. The external literature check cannot certify absence of an equivalent older formulation.
