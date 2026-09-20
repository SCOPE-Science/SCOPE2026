# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness — PASS

The source gives the shifted-Erlang frequency response
\[
G(i\omega)=e^{-i\omega\tau_m}(1+i\omega\Delta)^{-n},
\]
and hence
\[
q(\omega)=|G(i\omega)|=(1+(\omega\Delta)^2)^{-n/2}.
\]
It defines \(\alpha=q(2\pi)^{-1}\) and then sets the distributed-feedback coefficient to \(\widetilde a=a/\alpha=a q(2\pi)\).

The source's Fourier-filter argument is linear. Linearization of its nonlinear feedback
\[
-A\tanh(\kappa x)
\]
at the origin is \(-A\kappa x\). Therefore a sinusoid at frequency \(\omega\) is transmitted with magnitude \(A\kappa q(\omega)\). Substitution of the printed coefficient at \(\omega=2\pi\) gives \(a\kappa q(2\pi)^2\), not \(a\kappa\). Thus the printed operation compounds the attenuation. The amplitude-compensating coefficient is uniquely \(a/q(\omega)\).

The phase calculation follows immediately from the same transfer function:
\[
\arg G(i\omega)
=-\omega\tau_m-n\arctan(\omega\Delta).
\]
Hence
\[
\tau_{\rm ph}(\omega)
=\tau_m+\frac{n}{\omega}\arctan(\omega\Delta).
\]
Because \(\arctan x<x\) for \(x>0\), the phase-equivalent delay is strictly less than the mean \(\tau_m+n\Delta\) whenever \(\omega,\Delta>0\). The exact complex matching formulas in RESULT.md then follow by separately matching modulus and phase.

The autonomous Hopf formulas were rederived directly from the characteristic equation
\[
\lambda+a\kappa e^{-\lambda\tau_m}(1+\lambda\Delta)^{-n}=0.
\]
At \(\lambda=i\Omega\), modulus and argument give the two boxed conditions in RESULT.md. The positive frequency is unique because
\[
\Omega\mapsto \Omega(1+(\Omega\Delta)^2)^{n/2}
\]
is strictly increasing on \((0,\infty)\). The compact verification script evaluates the numerical examples and substitutes them back into the characteristic equation; the residuals are at floating-point roundoff.

An adversarial check was made against an alternative interpretation of the source scaling. The record does not claim that the source's continued bifurcation curves are numerically wrong: they are valid for the coefficients actually used. The claim is only that the printed scaling cannot be an amplitude compensation in the linear-filter sense used to motivate it. If the authors intended a different empirical normalization objective, the numerical family may still be useful, but the stated Fourier attenuation rationale does not establish a like-for-like gain match.

## Originality — PASS, to the best of our knowledge

The novelty claim is narrow. Fourier responses of Erlang kernels, gain/phase decomposition, linear-chain reductions, and stability crossing curves for shifted gamma delays are established mathematics and are not claimed as new. In particular, the 2007 paper by Morărescu, Niculescu and Gu treats stability crossing curves for shifted gamma-distributed delay systems; its accessible abstract was inspected, but the full text was not independently inspected. This is why the general Hopf algebra is treated only as prior background and a verification device.

The originality claim is the source-specific diagnosis of the normalization in arXiv:2609.08127v1: combining its own \(G(i\omega)\), \(\alpha=1/|G|\), and \(\widetilde a=a/\alpha\) shows that the intended attenuation compensation has the reciprocal direction. The record also supplies the corresponding corrected frequency-matched amplitude/phase mapping and applies the exact characteristic equation to the GZT parameters used in that paper.

Searches covered the exact title and arXiv identifier, combinations with correction, attenuation factor, feedback rescaling, phase delay, frequency response, shifted Erlang stability, gamma distributed delay Hopf conditions, and equivalent formulations. The arXiv page inspected lists only v1, submitted 8 September 2026. No correction, comment, or source-specific note identifying this normalization issue was located.

The main residual originality risk is the recency of the source: an author revision or discussion may exist before broad indexing. The inaccessible full text of Morărescu–Niculescu–Gu could contain equivalent general formulas, but that does not threaten the deliberately excluded general claim; it would matter only if it specifically anticipated the normalization used in this 2026 ENSO paper, for which no evidence was found.

## Value — PASS

The normalization is central to the source's comparison across delay widths. At the two widths highlighted there, the printed scaling leaves only about \(61.6\%\) and \(20.3\%\), respectively, of the constant-delay linear feedback magnitude at the annual frequency, while the mean-versus-phase delay mismatch is about \(3.9\) and \(24.5\) days. The distinction is therefore large enough to affect interpretation of width-dependent shifts.

The exact autonomous Hopf formulas provide a separate spectral anchor and show why one-frequency amplitude scaling cannot preserve all dynamical features. They also identify when the lowest physically admissible Hopf branch disappears because the minimum delay required by the phase condition becomes negative.

## Limitations

The result is a statement about small-signal frequency response and the unforced equilibrium spectrum. It does not provide a conjugacy between the nonlinear seasonally forced models, does not recompute the source's full resonance-tongue diagram under the corrected normalization, and does not assert that any continuation curve reported in the source is numerically erroneous. Nonlinear harmonics make global equivalence by a single scalar normalization impossible in general.

The source is a recent preprint and may be revised.
