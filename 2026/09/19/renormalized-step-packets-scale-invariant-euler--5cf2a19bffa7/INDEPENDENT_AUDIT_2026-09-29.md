# Independent Audit — 2026/09/19/renormalized-step-packets-scale-invariant-euler--5cf2a19bffa7

- Audit date: 2026-09-29 (UTC)
- Repository: `SCOPE-Science/SCOPE2026`
- Audited branch: `main`
- Inventory commit: `e9ed144c13b7834896a844cc4f9cac3c25a168a6`
- Source-tree checked commit: `253a0fe5d0217455660a277f9adb940030e567ad`
- Audited record tree: `78254be8ae2e0e6ec535f4d09f2c0a156d9fa5c2`
- Disposition: **PASSED**

## Correctness

**PASS** — The sharpened asymptotics follow from the source endpoint estimates and exact transport ODEs. Every endpoint other than b_n is nonnegative, nonincreasing and time-integrable, hence t x(t)->0; with b_n asymptotic to t^{-1}, all inner endpoints are o(b_n). In the exact b_n equation, every inner step contributes o(b_n^2), while the outer step contributes -2 c_* b_n^2+o(b_n^2) and the trigonometric prefactor tends to 1/2. Thus b_n'=-c_* b_n^2+o(b_n^2), giving c_* t b_n->1. Rescaling then collapses every inner interval to the origin and sends the outer interval to (0,1], proving the L1 top-hat limit and the moment constants. For one step, differentiating R=tan(a)/tan(b)^2 gives an integrable logarithmic derivative O(a+b^2), so R->Lambda in (0,infinity); substituting a=Lambda b^2+o(b^2) into the exact b equation gives (1/b)'=c-2c cot(2pi/m)b+O(b^2), and integration yields the stated logarithmic correction. The m=4 cancellation is exact.

## Originality

**PASS** — Suleiman's September 2026 source proves the finite-step topology, b_n comparable to (1+t)^{-1}, integrability of every other endpoint, and for one step only a nonsharp polynomial separation a/b. The inspected source does not state the exact coefficient c_* t b_n->1, a renormalized top-hat attractor, the moment limits, the limit a/b^2, or the logarithmic denominator correction. Targeted searches did not locate those formulas in the earlier scale-invariant Euler literature. The contribution is therefore a genuine asymptotic sharpening of the source's packet dynamics rather than a restatement of its coarse estimates.

## Scientific value

**PASS** — The result converts coarse decay control into a universal renormalized profile and exact clock, with explicit moment limits independent of all packet details except the outer height. The single-step Lambda invariant and geometry-dependent logarithmic correction expose a second asymptotic scale invisible in the source estimates. These are useful structural asymptotics for the same finite packets that underpin the dense-orbit construction.

## Sources

- **Dense orbits for scale-invariant rotationally symmetric solutions of the 2D Euler equations** — Ibrahim Suleiman. https://arxiv.org/abs/2609.20674 — Primary 2026 source; Proposition 2.4 supplies finite-step decay/integrability and the paper gives the exact endpoint dynamics.
- **On the long-time behavior of scale-invariant solutions to the 2d Euler equation and applications** — Tarek M. Elgindi; Ryan W. Murray; Ayman R. Said. https://doi.org/10.24033/asens.2621 — Earlier long-time scale-invariant Euler background; no matching finite-packet top-hat or logarithmic endpoint law was located.

## Limitations

- The universal top-hat statement is for finite positive step packets only, not arbitrary bounded, sign-changing, or infinite-step data.
- The a/b^2 invariant and logarithmic correction are proved only for one interval; multi-step subleading asymptotics may depend on interactions.
- The source preprint is very recent, so near-simultaneous unindexed observations remain a residual originality risk.

## Independent checks

```json
{
  "source_pdf_checked": true,
  "source_pdf_screenshots_checked": true,
  "proposition_2_4_decay_and_integrability_checked": true,
  "outer_endpoint_expansion_reconstructed": true,
  "single_step_ratio_derivative_reconstructed": true,
  "logarithmic_coefficient_checked": "-2*cot(2*pi/m)",
  "open_access_first": true,
  "oxford_used": false
}
```

The assigned source tree was unchanged between the inventory commit and the audited source-tree-check commit. GitHub was used only as read-only evidence and no repository mutation was performed. Preprints and lawful open-access sources were checked first; no decisive comparison remained inaccessible, so Oxford Download was not required.
