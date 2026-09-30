# Independent Audit — 2026-09-29

**Record:** `2026/09/19/concavity-logarithmic-harmonic-distortion-constant--a851edb91438`  
**Title:** Strict concavity and logarithmic endpoint asymptotics of the harmonic distortion constant  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Audited tree:** `31698728893f7bb715c8b76325cbc0876b0808b0`  
**Disposition:** **PASSED**

## Three-axis assessment

- **Correctness — PASS:** The derivative, concavity, and endpoint calculations are correct. From the source identities β=2J′, α=2J−2τJ′ and Q=J/J′−τ one gets Q′=−JJ′′/(J′)²<0 and M′=2τ(J′)²/J. Differentiating this last expression with respect to τ gives a positive derivative, hence M′′<0 because τ_K decreases with K. The values at τ=1 yield M′′(1+) = −1. Standard complementary-modulus elliptic expansions give Q(τ)=1/(τ log(4/(eτ)))(1+O(τ² log(1/τ))), whose inversion is the stated W_{−1} scale; the deficit and exact L² identity follow. Independent numerical solution of the elliptic equations gave negative second differences and deficit/asymptotic ratios 0.9973 at K=10 and 0.999985 at K=100.
- **Originality — PASS:** The primary September 2026 source determines M_K, the unique parameter, strict monotonicity, the endpoint 4/π, qualitative boundary convergence, and a first-order conformal expansion. Searches of the current source and related harmonic-map literature did not locate strict concavity, the exact derivative law, the second conformal coefficient, Lambert-W inversion, the 2/(πK²log K) deficit, or the exact quantitative L² degeneration. Wegmann’s older ellipse/Fourier formulas and Li’s global quasiconformal estimates are adjacent prior art but address different extremal formulations.
- **Scientific value — PASS:** This is a substantive quantitative sharpening of a new sharp constant: it determines global shape (strict concavity), both endpoint scales, and the convergence rate of extremizers. The logarithmic boundary layer is not visible from the source’s qualitative limit and gives useful asymptotic information about the extremal family.

## Independent checks

- Re-derived Q′, α′, M′ and the strict-concavity sign from J,J′,J′′.
- Checked the τ→0 elliptic expansions and Lambert-W inversion error scale algebraically.
- Solved the exact elliptic equations numerically at K=1.2,2,10,100; finite-difference M′′ was negative and the stated deficit asymptotic converged as predicted.

## Literature and evidence

- Knežević and Mateljević, Target Geometry in Prescribed-Value Schwarz Lemmas for Harmonic Maps — Primary source determines M_K and strict monotonicity with limit 4/π; indexed abstract does not state the audited concavity or large-K rates. (https://arxiv.org/abs/2609.19609)
- NIST DLMF §19.12, Asymptotic Approximations for Legendre’s Integrals — Standard complementary-modulus expansions used in the large-K derivation. (https://dlmf.nist.gov/19.12)
- Wegmann, Extremal problems for harmonic mappings from the unit disc to convex regions — Older ellipse/Fourier-coefficient context; not the same constrained pointwise-distortion theorem. (https://doi.org/10.1016/0377-0427(93)90293-K)
- Li, An asymptotically sharp coefficients estimate for harmonic K-quasiconformal mappings — Global quasiconformal coefficient estimates, not the source’s pointwise-at-origin optimization. (https://doi.org/10.1186/s13660-016-1033-0)

## Limitations

- The result concerns the source’s center constant and extremal family only.
- No off-center, general-target, or global quasiconformal analogue is claimed.
- Originality remains qualified because the primary theorem is very recent and older equivalent asymptotic observations under different terminology cannot be excluded absolutely.

**Independent-audit disposition:** passed.

GitHub was read only as evidence; no repository writes were made by this audit run.
