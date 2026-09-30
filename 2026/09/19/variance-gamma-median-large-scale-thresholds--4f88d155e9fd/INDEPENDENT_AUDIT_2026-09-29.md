# Independent audit — 2026-09-29 UTC

Record: `2026/09/19/variance-gamma-median-large-scale-thresholds--4f88d155e9fd`  
Assigned and audited source tree: `40d8b10645161fd92469cdd83c2b7e8792a962fb`  
Audited repository state: `SCOPE-Science/SCOPE2026` `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
Current RESULT.md blob: `a4483e513ae47457daf5f5d1d6cf9948dd8097fe`  
Disposition: **repaired**

## Correctness

**independently_supported**. The five regimes and constants are algebraically identical to the earlier repository theorem. The beta zero-CDF imbalance and Bessel-K small-argument expansion produce the thresholds at r=1 and r=3; the r=2 coefficient is 1/2 as required by the exact asymmetric-Laplace median. Substituting the Wishart off-diagonal VG parameters reproduces the stated n=1,2,3 and n>3 small-correlation formulas.

## Originality

**requires_repository_provenance_repair**. The same five-regime variance-gamma theorem, including both critical thresholds and constants, already appears in variance-gamma-median-large-noise-phase-transitions--2d5865f4207e, first committed 2026-09-18T17:10:12Z. This record first appeared 2026-09-19T04:05:38Z. It is therefore retained only as an alternate derivation plus Wishart corollary package.

## Scientific value

**useful_corroborating_statistical_corollary**. The main theorem is duplicate internally, but the Bessel-density derivation and direct Wishart interpretation are useful for reproducibility and applications.

## Evidence and literature checked

- https://arxiv.org/abs/2609.20212
- https://doi.org/10.1214/24-STS929
- https://doi.org/10.1007/978-1-4612-0173-1
- https://github.com/SCOPE-Science/SCOPE2026/commit/3ca64cb0df89fe7cffb094de6455e7a810eb22cc
## Literature access note

Publisher and bibliographic sources exposed only subscription/preview material; no lawful full text located. Authorized Oxford retrieval was queued, revisited, and timed out without returning a verified PDF. The source is not claimed to have been read in full.

## Limitations

- No separate priority claim survives repository chronology.
- Pointwise in fixed r and theta, not uniform near r=1 or r=3.
- The Kotz-Kozubowski-Podgorski monograph was not read in full; authorized retrieval timed out after OA search failed.
