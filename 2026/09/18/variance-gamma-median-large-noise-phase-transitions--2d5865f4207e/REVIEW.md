# Review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

The proof starts from the normal variance-mean mixture representation already used by Gaunt and Ouimet:
\[
Y_\kappa=2G_s+\sqrt{2\kappa G_s}\,N,
\qquad s=r/2.
\]
Conditioning on \(G_s\) gives the cdf formula in RESULT.md. Two quantities control the median.

First, the cdf imbalance at zero has the exact Student-\(t\) representation
\[
\frac12-F_\kappa(0)
=
\frac12-\Pr\!\left(
T_{2s}\le-\sqrt{2s/\kappa}
\right),
\]
hence
\[
\frac12-F_\kappa(0)
\sim
\frac{\Gamma(s+1/2)}
{\sqrt{\pi}\Gamma(s)}\kappa^{-1/2}.
\]

Second, direct differentiation of the conditional-normal cdf and the standard integral
\[
\int_0^\infty x^{\nu-1}e^{-\beta x-\gamma/x}\,dx
=
2(\gamma/\beta)^{\nu/2}K_\nu(2\sqrt{\beta\gamma})
\]
give the exact slope
\[
D_\kappa(q)
=
\frac{2e^{2q/\kappa}}
{\sqrt{\pi\kappa}\Gamma(s)}
\left(\frac q{\sqrt{\kappa+1}}\right)^{s-1/2}
K_{s-1/2}\!\left(
\frac{2q\sqrt{\kappa+1}}{\kappa}
\right).
\]
These formulas independently reproduce every asymptotic regime.

For \(s<1/2\), the small-argument \(K_{1/2-s}\) singularity gives
\(D_\kappa(q)\asymp\kappa^{-s}q^{2s-1}\); integrating the slope up to the median yields the stated power and constant.

For \(s=1/2\), the slope contains \(K_0\). Using
\(K_0(z)=-\log(z/2)-\gamma_E+o(1)\) gives
\[
q_\kappa[
\log\kappa-2\log q_\kappa+2-2\gamma_E+o(1)
]=1.
\]
Iterating once gives the displayed
\(\log\kappa+2\log\log\kappa+2-2\gamma_E\) denominator.

For \(s>1/2\), the known limiting half-median is \(a=s-1/2\). At that point the linear normal perturbation cancels exactly because
\[
a\,\Gamma(s-1/2)=\Gamma(s+1/2).
\]
The residual cdf is therefore governed by
\(H(x)=\Phi(x)-1/2-\phi(0)x\).
For \(1/2<s<3/2\), a \(G_s=z/\kappa\) boundary layer has order \(\kappa^{-s}\); the integral
\[
\int_0^\infty H(x)x^{-2s-1}\,dx
=
-\frac{2^{-s}\Gamma(3/2-s)}
{2s(2s-1)\sqrt{\pi}}
\]
gives the constant. At \(s=3/2\) this integral develops a logarithmic divergence, producing
\(-2(3\pi)^{-1}\kappa^{-3/2}\log\kappa\) in the cdf and the stated \(r=3\) median correction. For \(s>3/2\), cubic dominated convergence is valid because
\(\mathbb E G_s^{-3/2}<\infty\); the gamma recurrence reduces the resulting cubic expectation to
\[
(s-1/2)\Gamma(s-3/2)/\Gamma(s).
\]

The known exact \(r=2\) asymmetric-Laplace median expands as
\[
\theta+\theta^2/(2\sigma)+O(\sigma^{-2}),
\]
which agrees with the general \(1<r<3\) coefficient \(a_2=1/2\).

No computational output is required for the proof.

## Originality

Gaunt and Ouimet (2026) prove the monotonicity and limiting value of the large-\(\sigma\) VG median. Their stated result is the endpoint
\[
0\vee(r-1)\theta;
\]
their proof distinguishes \(r>1\) from \(r\le1\) to establish the sign needed for the limit but does not state the convergence rates above.

Fischer, Gaunt and Sarantsev (2025) provide an extensive VG survey, including median theory. They record the exact \(r=2\) asymmetric-Laplace median but no general exact formula. The \(r=2\) case is therefore treated only as a check, not as a new result.

The VG density's local threshold at \(r=1\) is known. Li (2024) explicitly records a power singularity for \(0<r<1\), a logarithmic singularity at \(r=1\), and bounded behavior for \(r>1\). Standard Bessel-\(K\) asymptotics are likewise prior art. The originality claim is not the existence of those analytic thresholds, but the sharp median asymptotics and their constants.

Targeted literature searches covered variance-gamma and generalized-Laplace medians, large-noise and large-scale asymptotics, quantile asymptotics, the critical values \(r=1\) and \(r=3\), and equivalent normal variance-mean mixture formulations. No inspected source stated the five-regime expansion, the \(r=3\) median transition, or the \(r=1\) two-logarithm refinement.

The principal residual risk is the older generalized-Laplace literature, especially the 2001 monograph by Kotz, Kozubowski and Podgórski, which was identified as relevant but not inspected in full. This uncertainty is material because the VG distribution appears there under the generalized-Laplace name. Against this risk, the much newer 2025 review explicitly surveys median theory and does not report these large-noise rates. The originality assessment is therefore to the best of our knowledge.

## Value

The result upgrades a recently proved endpoint limit into a sharp phase diagram across the entire VG shape range. It shows that no single polynomial correction describes large-noise medians: the rate changes at \(r=1\), acquires an inverse-logarithmic law at that first critical shape, changes power for \(1<r<3\), acquires a second logarithmic anomaly at \(r=3\), and only for \(r>3\) settles to the regular \(\sigma^{-2}\) correction.

The constants are explicit. The \(r=1\) result also resolves the next slowly varying term, \(2\log\log\kappa\), while the \(r=3\) transition identifies a separate inverse-moment mechanism not visible from the endpoint limit alone.

## Limitations

The asymptotics are pointwise in fixed \(r\) and fixed nonzero \(\theta\). They are not uniform when \(r\) approaches \(1\) or \(3\) with \(\kappa\). No general second-order expansion is derived away from \(r=1\), and no extension to non-VG generalized hyperbolic distributions is claimed. Older generalized-Laplace literature remains a residual originality risk.
