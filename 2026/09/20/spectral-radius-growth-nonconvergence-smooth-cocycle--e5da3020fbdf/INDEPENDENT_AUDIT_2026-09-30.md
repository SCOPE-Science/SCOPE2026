# Independent audit — 2026-09-30 UTC

Record: `2026/09/20/spectral-radius-growth-nonconvergence-smooth-cocycle--e5da3020fbdf`  
Assigned and audited source tree: `9a245d02eb82b4dde16977510e30d6f10e1edad3`  
Audited repository state: `SCOPE-Science/SCOPE2026` `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
Current RESULT.md blob: `c210fa45f0222482d52824a32e053f8420c7a4e7`  
Disposition: **passed**

## Correctness

**independently_supported**. The smooth cocycle counterexample is exact. Along the invariant circle, derivatives are block diagonal and the fiber product telescopes to R_{theta+L*pi/2}D^L R_{-theta}. For odd L, the fiber matrix is similar to ±R_{pi/2}D^L and squares to -I, so its spectral radius is 1; for even L its spectral radius is s^L. Singular values are always s^L and s^{-L}, giving the strict Lyapunov spectrum log s,0,-log s. The smooth frame change H(theta,v)=(theta,R_{-theta}v) conjugates the cocycle to constant D and makes every finite-L spectral rate log s, proving the coordinate dependence. All conclusions are algebraic and do not rely on numerical verification.

## Originality

**qualified_source_specific_counterexample**. General nonconvergence of n^{-1}log rho(A^(n)) is established prior art; Martínez Ramos 2026 proves convergence only under additional locally-constant strong-irreducibility hypotheses and explicitly situates the problem against earlier limsup results. Sornette–Saiprasad–Troude introduced the ordered-product diagnostic in September 2026. The audited contribution is therefore the explicit smooth periodic tangent-cocycle counterexample, exact parity oscillation, and coordinate-conjugacy failure directed at the unrestricted source claim, not discovery of spectral-radius nonconvergence in general.

## Scientific value

**high_corrective_value**. The example cleanly separates singular-value/Oseledets growth from finite-horizon spectral-radius growth and identifies endpoint-frame mismatch as the failure mechanism. It materially narrows how the recent diagnostic may be interpreted without disputing the source’s numerical experiments.

## Independent checks

- Re-derived the telescoping product and parity spectrum.
- Checked the singular values and Lyapunov exponents.
- Verified the smooth conjugacy and endpoint-frame transformation law.

## Literature and evidence checked

- https://arxiv.org/abs/2609.18017
- https://arxiv.org/abs/2507.19624
- https://doi.org/10.1093/imrn/rnag038
- https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/20/spectral-radius-growth-nonconvergence-smooth-cocycle--e5da3020fbdf

## Limitations

- Does not challenge the source’s reported fixed-coordinate numerical experiments.
- Does not characterize weakest sufficient hypotheses for convergence.
- General nonconvergence is prior art; novelty is the explicit smooth source-specific construction and conjugacy diagnostic.
