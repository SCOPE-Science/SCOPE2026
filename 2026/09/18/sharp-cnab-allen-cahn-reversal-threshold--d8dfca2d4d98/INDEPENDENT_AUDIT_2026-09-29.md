# Independent Audit — 2026/09/18/sharp-cnab-allen-cahn-reversal-threshold--d8dfca2d4d98

- Audit date: 2026-09-29 (UTC)
- Repository: `SCOPE-Science/SCOPE2026`
- Audited commit: `253a0fe5d0217455660a277f9adb940030e567ad`
- Audited record tree: `028b196db5160741187f4fd2297b40cc3c40879c`
- Disposition: **PASSED**

## Correctness

**PASS** — For homogeneous states the Laplacian vanishes and the stabilization appears only in the positive prefactor tau/(epsilon^2+S tau^2), so the sign is controlled solely by 3 f(b)-f(a). With g=-f on (0,1), reversal is equivalent to 3g(b)<g(a). The exact starter b(h) increases strictly from a to 1, while g has one maximum at 1/sqrt(3); therefore the level g(a)/3 is crossed exactly once on the decreasing branch. Solving the exact-flow identity gives h*=0.5 log(3 b_*^3/a^3), and the cubic/trigonometric formula is correct. The crossing derivative is positive and hence transverse. Independent numerical checks at a=0.1,0.5,1/sqrt(3),0.9 reproduced the sign change on opposite sides of h*. The generalized alpha>1 formula follows from replacing 1/3 by q=(alpha-1)/alpha. The source's perturbation argument depends only on a strict homogeneous sign margin, so replacing its conservative sufficient threshold by the exact one for sufficiently small nonhomogeneous perturbations is legitimate.

## Originality

**PASS** — The primary 2026 pointwise-monotonicity paper introduces the stabilized CN/AB counterexample and derives a sufficient large-step condition, but the inspected full-text material does not state the exact if-and-only-if crossing, its cubic root, the exact gap to the published threshold, or the alpha>1 over-extrapolation law. The original 2013 stabilized CN/AB work concerns energy stability/error estimates, and Li-Wang's earlier phase-field step-size work treats other schemes. Targeted searches found no earlier exact threshold formula for this exact-starter CN/AB reversal.

## Scientific value

**PASS** — The result converts a sufficient failure certificate into a sharp bifurcation law, shows that stronger stabilization cannot shift the homogeneous sign threshold, and expands the active-diffusion perturbative failure regime to the exact boundary. The general extrapolation formula isolates over-extrapolation rather than stabilization as the mechanism.

## Sources

- Pointwise Monotonicity of the Allen-Cahn Flow and Dynamical Limitations of Energy-Stable Schemes (Pansheng Li; Dongling Wang): https://arxiv.org/abs/2609.19023 — Primary source for the stabilized CN/AB homogeneous recurrence, large-step reversal and nonhomogeneous persistence; the searched full-text copy describes a sufficient rather than exact onset.
- Stabilized Crank-Nicolson/Adams-Bashforth Schemes for Phase Field Models (X. Feng; T. Tang; J. Yang): https://doi.org/10.4208/eajam.200113.220213a — Original stabilized CN/AB phase-field scheme; focuses on energy stability and error analysis rather than the audited pointwise reversal threshold.
- Asymptotic Stability of Many Numerical Schemes for Phase-Field Modeling (Pansheng Li; Dongling Wang): https://arxiv.org/abs/2411.06943 — Earlier step-size/monotonicity analysis for related phase-field discretizations, not the exact-starter stabilized CN/AB threshold here.

## Limitations

- The exact threshold classifies only the first post-starter increment and assumes the exact homogeneous starter used by the source.
- The nonhomogeneous statement is perturbative, not a universal sharp threshold for arbitrary spatial data.
- A different numerical starter or different nonlinearity changes the crossing.

## Independent checks

```json
{
  "proof_reconstructed": true,
  "numeric_a_values": [
    0.1,
    0.5,
    0.5773502691896258,
    0.9
  ],
  "sign_change_verified": true,
  "max_source_gap_at_a": 0.5773502691896258,
  "max_dimensionless_gap": 0.1115537285050405
}
```

The assigned source tree was unchanged between the inventory commit and the audited source-tree-check commit. GitHub was read only as evidence and no repository mutation was performed. Open-access/preprint sources were checked first.
