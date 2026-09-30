# Independent audit — 2026-09-29

Record: `2026/09/19/all-vector-levy-traces-dirichlet-bidisc--ef9eba5e3f64`  
Assigned and audited source tree: `f4ea69a3d212e8eea4adb55f1bd8fb6ada93ca9b`  
Audited repository state: `SCOPE-Science/SCOPE2026` `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
Current RESULT.md blob: `36b0411da3a961fb3ea980edaf4e7433b83a3d44`  
Disposition: **passed**

## Correctness

**independently_supported**. The trace-map and tomography calculations are consistent. The polynomial defect identity is a bounded quadratic form because the coordinate multiplier is bounded, so literal polynomial restriction extends uniquely to an L2 trace Gamma_i; polynomial density also extends Gamma_i M_i=M_a Gamma_i. Applying this to M_i^n h gives the exact Hausdorff moment sequence with representing measure S_*eta_i,h. Splitting the t=1 atom from the [0,1) part produces the one-variable Levy density (1-t)^(-1)dmu and the drift atom, and the source paper's zero-pair-defect decomposition then places the two coordinate measures on the two faces. For polynomial probes depending on one coordinate, 1, 1+z^k, and 1-i z^k recover the real and imaginary parts of S_*(a^k rho). Disintegration over t=|a|^2 converts these Radon-Nikodym derivatives into every angular Fourier coefficient on almost every interior circle; the t=0 fiber is a singleton. The same polarization applied to the drift recovers all boundary Fourier coefficients. Thus the full defining measures are determined by the stated countable Levy-plus-drift data, while the delta_r/delta_-r example correctly shows that the cyclic-vector radial data alone lose angle.

## Originality

**qualified_direct_answer**. Bera-Sequeira's September 17, 2026 public abstract gives the explicit defining-measure formula only for the cyclic vector h=1. The record uses the paper's abstract all-vector face mechanism together with Bera's published polynomial defect identity to obtain an explicit arbitrary-vector trace formula and then a countable tomography theorem. Targeted current searches did not locate the trace/tomography statement. Older one-variable completely-hyperexpansive theory remains a background risk for individual ingredients, so novelty is claimed only for the bidisc all-vector synthesis and reconstruction consequence.

## Scientific value

**meaningful_model_identification**. The theorem answers the current arbitrary-vector identification problem in a concrete form and pinpoints the information boundary between the Levy measure and drift. The countable probe family upgrades the formula to a reconstruction theorem for both defining measures.

## Literature and evidence checked

- https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/19/all-vector-levy-traces-dirichlet-bidisc--ef9eba5e3f64
- https://arxiv.org/abs/2609.20346
- https://nyjm.albany.edu/j/2026/32-4.html
- https://doi.org/10.4153/S0008414X24000300
- https://doi.org/10.1023/A:1009719803199
## Limitations

- For general h the trace maps are L2 completions; no pointwise boundary trace is asserted.
- The tomography theorem requires the full countable probe family and uses drift as well as the Levy measure.
- No higher-polydisc or nonzero-pair-defect analogue is proved.
- The motivating preprint is extremely recent, and older one-variable trace formulations remain a residual attribution risk.
