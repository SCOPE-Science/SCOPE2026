# Independent Audit — 2026/09/18/all-order-gamma-memory-bifurcation-geometry--1c8a8bf2a700

- Audit date: 2026-09-29 (UTC)
- Repository: `SCOPE-Science/SCOPE2026`
- Audited inventory commit: `e9ed144c13b7834896a844cc4f9cac3c25a168a6`
- Source-tree checked commit: `253a0fe5d0217455660a277f9adb940030e567ad`
- Audited record tree: `62dfcef7a86c91416bec11799cc5b8cf11b6a18b`
- Disposition: **PASSED**

## Correctness

**PASS** — The Erlang-chain elimination is correct: on a Neumann mode the k+1 memory stages contribute (z+B)^(k+1), so the modal characteristic polynomial is (z+X)(z+M)(z+B)^(k+1)+C. For z=iω, the phase and modulus are strictly increasing because X,M,B>0. Counting odd and positive even multiples of π below (k+3)π/2 gives exactly N_+(k)=ceil((k+1)/4) and N_-(k)=floor((k+2)/4); I checked these counts directly for k=0,…,29. At a nonzero imaginary crossing, implicit differentiation gives dz/dC=1/[C L(iω)], whose real part has the sign of C because Re L(iω)>0, proving simplicity and transversality. Every negative-C oscillatory threshold has magnitude R_k(ω)>R_k(0)=|C_S|, so the stationary crossing is first on that side; the first positive phase π crossing is first on the other side. The fixed-mean scaling τ=T/(k+1) gives (1+T(z+d_1λ)/(k+1))^(k+1)→exp(T(z+d_1λ)) locally uniformly, yielding the stated discrete-delay characteristic equation and branchwise phase limits.

## Originality

**PASS** — Liang-Wang-Zhang analyze the exponentially decaying weak kernel and peak-type strong kernel, corresponding to the first two Gamma/Erlang orders. The linear-chain trick itself is classical, but the located source and related searches do not state the all-order factorization, exact crossing counts, primary stability interval, or fixed-mean phase-ladder limit for this cognitive-map PDE. The record's contribution is therefore a model-specific completion rather than a claim of inventing Erlang chains.

## Scientific value

**PASS** — The factorization replaces order-by-order Routh-Hurwitz calculations by one monotone phase law, reveals when additional secondary crossings first appear, and connects finite Gamma memory to the discrete-delay ladder. This is a reusable spectral description for the source model and meaningfully extends the two kernel orders previously analyzed.

## Sources

- Bifurcation Analysis of a Reaction-Diffusion System with a Cognitive Map Memory Kernel (Jie Liang; Xiaoli Wang; Guohong Zhang): https://arxiv.org/abs/2606.02250 — Primary model source; its abstract states bifurcation analyses for the weak exponential and peak-type strong kernels.
- Generalizations of the 'Linear Chain Trick': incorporating more flexible dwell time distributions into mean field ODE models (Paul J. Hurtado; Adam S. Kirosingh): https://doi.org/10.1007/s00285-019-01412-w — General Erlang/linear-chain background; not a source for the model-specific all-order phase geometry.

## Limitations

- The theorem is a local spectral result; a full PDE Hopf theorem additionally needs the stated simple-mode and nonlinear nondegeneracy assumptions.
- Noninteger Gamma shapes are not covered by the finite chain.
- The fixed-mean result is spectral convergence, not nonlinear trajectory convergence.

## Independent checks

```json
{
  "method": "symbolic modal elimination and phase-count reconstruction",
  "k_checked_for_count_formula": [
    0,
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    11,
    12,
    13,
    14,
    15,
    16,
    17,
    18,
    19,
    20,
    21,
    22,
    23,
    24,
    25,
    26,
    27,
    28,
    29
  ],
  "count_formula_match": true,
  "transversality_sign_checked": true,
  "fixed_mean_limit_checked": true,
  "all_ok": true
}
```

The assigned source tree was unchanged between the inventory commit and the source-tree-check commit. GitHub was read only as evidence and no repository mutation was performed. Open-access/preprint sources were checked first; Oxford Download was not needed in this record.
