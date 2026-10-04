# Review

## Correctness

PASS. Substituting a sign-alternating eigenvector state into the source NovoGrad recurrence gives the exact cycle radius
\[
r_\lambda^2
=
\frac{\alpha^2}{4(1+\beta_1)^2}
-
\frac{\varepsilon}{\lambda^2}.
\]
For an orthogonal eigenmode, the derivative of the layerwise squared-gradient norm is zero, so the transverse first-order dynamics close on a constant \(2\times2\) position-momentum block. Its determinant is \(\beta_1\), its trace is \((1+\beta_1)(1-2\mu/\lambda)\), and the exact Jury conditions reduce to \(\mu<\lambda\).

Risk: no claim is made about the radial Floquet multiplier along the generating eigenvector.

## Originality

PASS. The Jasper and dedicated NovoGrad papers define the normalize-current-gradient-then-momentum ordering and motivate layerwise robustness, but their inspected full text contains no period-two quadratic orbit or transverse eigenmode classification. ND-Adam uses a different first-moment ordering together with spherical renormalization. The inspected normalized-gradient saddle literature states the discrete direction-only update but focuses its rigorous analysis on continuous time and explicitly leaves discrete stable-manifold analysis open.

Focused published-record searches for NovoGrad period-two cycles, scalar or SPD quadratic stability, normalized-momentum eigencycles, and relative-curvature transverse spectra returned no covering result.

Residual risk: a fixed-step normalized-gradient cycle may be folklore in nonsmooth optimization, but the momentum-dependent radius, epsilon existence threshold, and curvature-ratio Floquet law are specific to the NovoGrad state ordering.

## Value

PASS. Layerwise gradient normalization is NovoGrad's defining mechanism. The theorem shows a precise consequence of that normalization that is invisible in first-order origin analysis: nonzero oscillatory states exist on eigendirections, and the layerwise scalar normalizer makes their transverse stability depend only on curvature ordering. The result explains why high-curvature directions are dynamically privileged and supplies an exact relative-curvature rate plateau controlled solely by momentum.

Same-model review: passed. Independent audit: not yet performed.
