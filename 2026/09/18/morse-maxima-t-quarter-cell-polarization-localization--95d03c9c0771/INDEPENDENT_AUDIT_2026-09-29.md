# Independent Audit — 2026/09/18/morse-maxima-t-quarter-cell-polarization-localization--95d03c9c0771

- Audit date: 2026-09-29 (UTC)
- Repository: `SCOPE-Science/SCOPE2026`
- Audited commit: `253a0fe5d0217455660a277f9adb940030e567ad`
- Audited record tree: `08ef10c44e1cd47d2e956c4fd68bececdcaa6b5d`
- Disposition: **PASSED**

## Correctness

**PASS** — The asymptotic argument is correct. From the exact slow-limit representation u=[u0+A-(t+A)h]_+ and tau=t+A, q=A/tau, a Morse minimum h(z)=z^T H_j z/2+o(|z|^2) gives G(s)=int(s-h)_+=pi s^2/sqrt(det H_j) per maximum, hence G(s)=C s^2+o(s^2) with the submitted C=pi sum_j(det H_j)^(-1/2). Mass conservation squeezes C tau q^2 to 1, so q~(Ct)^(-1/2), A~sqrt(t/C), and the support radius is sqrt(q), i.e. t^(-1/4). The same local calculation gives |S|~2Cq and int_S h~Cq^2, therefore phi=int_S h/int_S(1-h)~q/2. Under z=sqrt(q)H_j^(-1/2)y, u/(tau q) converges to (1-|y|^2/2)_+, and the Jacobian together with tau q^2->1/C gives exactly the stated determinant-weighted limiting masses. An independent exact radial quadratic reconstruction also reproduces the submitted constants.

## Originality

**PASS** — The immediate source establishes localization and characterizes the slow-time concentration process, while the earlier small-mass stationary paper establishes an elliptic obstacle-profile geometry near nondegenerate maxima. The audited theorem adds a different quantitative statement for the time-dependent zero-diffusion slow dynamics: the explicit t^(-1/4), t^(1/2), and t^(-1/2) rates and the parabolic-cap rescaled profile. Those statements are not part of the cited stationary obstacle result, and the source paper's published abstract does not state these temporal laws. Targeted literature searches found no covering pre-record theorem, so the claim is a defensible source-specific refinement rather than a rebranding of the stationary ellipse result.

## Scientific value

**PASS** — The result upgrades qualitative concentration to sharp rates, support geometry, peak growth, multiplier decay, and a universal local profile. These quantities are directly useful for comparing the slow-limit model with finite-diffusion or finite-mass dynamics, and the profile explains the determinant weights as integrated local mass rather than only as subsequential weights. The theorem is narrow but supplies a complete quantitative asymptotic description in the generic Morse case.

## Sources

- Localization properties of a free boundary problem for cell polarization (B. Niethammer; M. Röger; J. J. L. Velázquez): https://arxiv.org/abs/2609.20609 — Primary slow-limit localization source; submitted 2026-09-17 and states concentration on the appropriate slow time scale.
- On the shape of the positivity region for a free boundary problem describing cell polarization (Sebastián Flores Sepúlveda; Barbara Niethammer; Juan J. L. Velázquez): https://arxiv.org/abs/2605.03553 — Prior small-mass stationary obstacle analysis; proves an elliptic limiting interface at nondegenerate maxima in a different regime.

## Limitations

- The theorem applies only to the D=infinity slow-limit model with a time-independent signal and finitely many nondegenerate maxima.
- It does not give a uniform-in-small-mass theorem for the original positive-mass parabolic system or finite cytosolic diffusion.
- Degenerate maxima can change the localization exponent and are excluded.
- Originality is the quantitative dynamical refinement, not the Hessian-ellipse observation by itself.

## Independent exact check

```json
{
  "implementation": "exact radial quadratic model plus direct Morse-cap integration",
  "times": [
    100.0,
    10000.0,
    1000000.0
  ],
  "observed_A_normalized": [
    1.0286072874094225,
    1.0028249267834004,
    1.0002821345805089
  ],
  "observed_q_normalized": [
    0.9721883290546474,
    0.9971830309479228,
    0.9997179449969612
  ],
  "observed_phi_normalized": [
    0.9996023499564259,
    0.9999960211501698,
    0.9999999602112666
  ],
  "all_ok": true
}
```

The assigned source tree was unchanged between the inventory commit and the audited source-tree-check commit. GitHub was read only as evidence and no repository mutation was performed. Open-access/preprint sources were checked first; no needed source remained inaccessible, so Oxford Download was not required.
