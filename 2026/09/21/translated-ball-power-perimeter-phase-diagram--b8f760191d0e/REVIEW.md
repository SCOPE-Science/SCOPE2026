# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

PASS.

For
\[
\Phi_{n,p}(t)=\frac1{\omega_{n-1}}\int_{S^{n-1}}|t e_1+\theta|^p\,d\sigma(\theta),
\]
the identity
\[
\Delta |x|^p=p(p+n-2)|x|^{p-2}
\]
implies, for \(0<t<1\),
\[
(t^{n-1}\Phi_{n,p}'(t))'
=
p(p+n-2)t^{n-1}\Phi_{n,p-2}(t).
\]
The factor \(\Phi_{n,p-2}\) is positive and finite because the translated unit sphere stays away from the origin. Radial regularity supplies zero initial flux at \(t=0\), so the sign of the derivative inside the sphere is exactly the sign of \(p(p+n-2)\).

For \(t>1\),
\[
\Phi_{n,p}'(t)
=
\frac{p}{\omega_{n-1}}
\int_{S^{n-1}}
(t+\theta_1)|t e_1+\theta|^{p-2}\,d\sigma(\theta),
\]
and \(t+\theta_1>0\), so the sign is exactly the sign of \(p\).

At \(p=2-n\) the interior profile is therefore constant. Its value is \(1\) at \(t=0\). Outside, radial harmonicity together with decay/asymptotics gives \(t^{2-n}\), recovering the Newton-shell identity. The touching value is finite exactly for \(p>1-n\); the beta integral evaluates to
\[
2^{p+n-2}
\frac{\Gamma(n/2)\Gamma((p+n-1)/2)}
{\sqrt\pi\,\Gamma(n-1+p/2)}.
\]
These facts give all monotonicity and endpoint statements in the result.

A compact numerical artifact independently checks representative regimes, the critical profile, and the beta-integral boundary formula.

## Originality

PASS, to the best of our knowledge, with a deliberately narrow claim.

Csató's 2018 paper was inspected at Theorem 9 and Example 11. Example 11 computes first and second translation variations and records the local sign threshold \(p=2-n\); it does not state the full global translated-ball phase diagram or the entire critical flat family.

Searches covered translated balls/spheres, weighted perimeter with radial power density, the exact threshold \(p=2-n\), spherical means of power/Riesz kernels, Newton-shell formulations, and synonymous potential-theoretic language. No source was located that packages the complete monotonicity diagram with the weighted-isoperimetric consequences stated here.

The full 2026 preprint by Csató, Giovagnoli and Roy was inspected around its translation arguments. It again uses translations and the sign of the Laplacian of a radial power, and its Corollary 2.10 treats a weighted barycentric condition for \(p>2-n\). Searches within the full text for spherical means, the Newton-shell identity, and the translated-ball profile did not locate the statement proved here.

The spherical-mean differential equation and Newton's shell theorem are classical and are not claimed as new. The originality claim is limited to the complete translated-ball phase diagram in this weighted-perimeter setting and its consequences for the stable-but-not-global range.

Residual risk remains because classical Riesz-potential literature may contain an equivalent spherical-mean monotonicity theorem under terminology not surfaced by the searches.

## Value

PASS.

The result explains, with one analytic mechanism, all translation regimes adjacent to Csató's second-variation calculation. It upgrades local stability to global stability among origin-containing ball translates for \(1-n<p<2-n\), identifies a unique touching maximum there, and resolves the degenerate exponent \(p=2-n\) into an exact continuum of equal-perimeter translates. It also confirms globally the monotone decrease of translated balls for \(2-n<p<0\).

## Limitations

- Only translations of a fixed ball are classified; arbitrary shape variations are not.
- The result does not change the global isoperimetric classification for arbitrary admissible sets.
- The critical \(p=2-n\) formula is classical potential theory; novelty is not claimed for Newton's shell theorem itself.
- Equivalent prior coverage in Riesz-potential language remains a residual originality risk.
- Independent audit has not been performed.
