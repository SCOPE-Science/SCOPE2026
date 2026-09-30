# Independent audit — 2026-09-30 UTC

Record: `2026/09/21/fisher-lossless-fixed-quantizer-location-sumsets--f9e323def0af`  
Assigned and audited source tree: `799c96fe70c4cd2dbfe7e5eee45dae2e87843a15`  
Repository/branch: `SCOPE-Science/SCOPE2026` / `main`  
Current RESULT.md blob: `6c0e13a348ff89e0efc2ad9c4fdc8c8c91b40530`  
Disposition: **passed**

## Correctness

**independently_supported**. The information-loss identity and all combinatorial consequences are correct. The quantized score is the conditional expectation of the full location score on each interval cell, so equality of Fisher information is equivalent to zero conditional score variance on every shifted cell. Positivity of f then makes exact preservation equivalent to every essential score knot lying among T-θ, i.e. K+θ⊆T. Unioning translated knot sets gives the exact threshold budget for several target locations, and the real-line sumset inequality gives |Λ|≤m-κ with the stated arithmetic-progression sharpness construction. Integrability excludes κ=0; κ=1 forces opposite-sign tail scores and hence exactly the asymmetric-Laplace family, proving the universal m-1 classification.

## Originality

**qualified_supported_after_full_close-source_inspection**. Pötzelberger–Felsenstein 1993 was obtained through authorized institutional access after open-access retrieval failed and was inspected across all 21 pages. It develops Fisher information under finite interval discretization, including the double-exponential location example where a threshold at the true location is lossless, but it does not state the fixed-one-quantizer multi-location translate-incidence law, exact sumset threshold budget, |Λ|≤m-κ bound, or asymmetric-Laplace uniqueness classification. Hobza–Molina–Vajda and Cabral Farias–Brossier provide the one-location equality/projection mechanism, which is prior art. The audited contribution is therefore the global fixed-quantizer multi-location rigidity and design law.

## Scientific value

**meaningful_exact_quantizer_design_law**. The theorem converts a local equality criterion into an exact finite combinatorial design problem, identifies the minimum number of cells for prescribed locations, and sharply characterizes the unique full-support family attaining the maximal number of lossless locations.

## Independent checks

- Re-derived the quantized-score conditional-expectation identity from cell probabilities.
- Checked both infinite outer cells and the a.e. knot argument under f>0.
- Verified the real-line sumset lower bound and arithmetic-progression equality construction.
- Derived the κ=1 asymmetric-Laplace form and its exact lossless-location set.
- Inspected the complete Pötzelberger–Felsenstein 1993 article through authorized institutional access and found no multi-location sumset theorem.

## Literature and evidence checked

- https://doi.org/10.1080/00949659308811499
- https://doi.org/10.1007/s001840100178
- https://doi.org/10.1007/BF02595401
- https://arxiv.org/abs/1310.6945
- https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/21/fisher-lossless-fixed-quantizer-location-sumsets--f9e323def0af
## Literature access note

`https://doi.org/10.1080/00949659308811499` was obtained through authorized institutional access after lawful open-access retrieval failed. Inspected pages: 1-21.

## Limitations

- One-dimensional full-support location models and deterministic interval quantizers only.
- Exact Fisher-information equality is local and does not imply equality of statistical experiments.
- Adaptive, randomized, non-interval and multidimensional quantizers are outside scope.
- Approximate information retention and finite-sample risk are not analyzed.
