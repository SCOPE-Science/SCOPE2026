# Independent Audit — 2026/09/18/frequency-matched-shifted-erlang-enso-feedback--c5273aabd245

- Audit date: 2026-09-29 (UTC)
- Repository: `SCOPE-Science/SCOPE2026`
- Audited commit: `253a0fe5d0217455660a277f9adb940030e567ad`
- Audited record tree: `5fe29581c9346ccd4d8376e86fe33734941661c5`
- Disposition: **PASSED**

## Correctness

**PASS** — The primary arXiv HTML states exactly that alpha(n,Delta)=1/|G(2*pi*i)| and then sets tilde a=a/alpha. Since |G(i omega)|=q(omega), linearization of -A tanh(kappa x) sends a sinusoid to magnitude A*kappa*q, so the printed choice indeed produces a*kappa*q^2 rather than a*kappa; amplitude compensation requires A=a/q. The phase-equivalent delay follows from arg G, and arctan(x)<x gives the strict mean-minus-phase mismatch. I independently recomputed the quoted source parameters: q=0.784672478417 and 0.450424982227, post-filter ratios q^2=0.615710898385 and 0.202882664614, delay mismatches 0.010601772283 and 0.067042812370 years. Solving the characteristic equation reproduces the Hopf frequencies, delays and the Delta=8/99 admissibility threshold to roundoff.

## Originality

**PASS** — Shifted-gamma transfer functions and stability-crossing calculations are classical and are not new here. The novel point is source-specific: the September 2026 ENSO preprint explicitly motivates its scaling as attenuation compensation yet uses the reciprocal direction. Searches for the arXiv identifier together with correction, attenuation and feedback-rescaling terms found no independent correction or later source revision addressing this mismatch.

## Scientific value

**PASS** — The normalization is central to the source's claimed like-for-like comparison across kernel widths. At the wider example it leaves only about 20.3 percent of the nominal constant-delay small-signal feedback magnitude, and the mean/phase mismatch is about 24.5 days. Correcting the interpretation and giving exact one-frequency gain/phase and autonomous Hopf anchors materially changes how the reported width-dependence should be read, while carefully leaving the source's numerical continuation curves themselves intact.

## Sources

- A distributed-delay model for the El Niño Southern Oscillation with a minimum delay: a case study of the shifted linear chain trick (Joe Steele; Andrew Keane; Bernd Krauskopf): https://arxiv.org/html/2609.08127v1 — Primary open-access HTML; equations (10)-(11) define alpha=1/|G| and tilde a=a/alpha and describe this as accounting for attenuation.
- Stability Crossing Curves of Shifted Gamma-Distributed Delay Systems (C.-I. Morărescu; S.-I. Niculescu; K. Gu): https://doi.org/10.1137/060670766 — Prior general shifted-gamma stability-crossing background; not a source-specific correction of the 2026 ENSO normalization.

## Limitations

- The correction is a linear-response and unforced-equilibrium statement; it does not recompute the full nonlinear seasonally forced bifurcation diagram.
- A one-frequency complex match cannot make the distributed and constant-delay nonlinear systems globally equivalent because nonlinear harmonics remain.
- The source is a recent preprint and could be revised after this audit.

## Independent exact check

```json
{
  "method": "fresh direct evaluation of transfer function and bisection of the Hopf amplitude equation",
  "q_Delta_1_15": 0.784672478417091,
  "q_Delta_2_15": 0.450424982226959,
  "mean_minus_phase_years": [
    0.0106017722831541,
    0.0670428123696304
  ],
  "hopf_omega": [
    11.0,
    7.727648837642446,
    5.628363629550838
  ],
  "critical_Delta": "8/99",
  "all_characteristic_residuals_below": 5e-15
}
```

GitHub was read only as evidence; no repository mutation was performed. The assigned source tree was unchanged between the inventory commit and the audited source-tree-check commit. Open-access/preprint material was checked before other sources; no Oxford Download was needed for this record.
