# Independent audit — 2026-09-30

Record: `2026/09/19/nonvanishing-schatten-zero-divisors-fock-toeplitz--c8def62ac799`  
Assigned and audited source tree: `49f2356f461b4e6b0660017f3f6efeb29bf730ca`  
Audited repository state: `SCOPE-Science/SCOPE2026` `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
Current RESULT.md blob: `f377fc952b845d3b064622eeb9262bed33875bb5`  
Disposition: **passed**

## Correctness

**independently_supported**. The deformed Gaussian zero-product construction is coherent. For each quaternionic unitary U with U+U*=I, the Gaussian integral gives T_{σ_U}K_b=κK_{D_U* b} with D_U=diag(U/[2(1+q)],I/(1+ρ)); its symbol modulus is exactly exp(-q|ξ|²-ρ|z'|²). The sixteen coefficient pairs group by the product U_jV_k and cancel within each product class, and composition of the kernel maps depends on the pair through that same product, so T_fT_g=0 on the dense kernel span. A linear Fock composition operator is the symmetric second quantization of its matrix, so its singular values are all monomials in the matrix singular values and the S_p sum is ∏(1-s_j^p)^(-1). Thus the active directions are all-Schatten even at q=0, while passive directions require ρ>0 unless n=2. At ρ=0 and n>2 the exact tensor factorization with an infinite-dimensional identity proves noncompactness. The explicit rays show both endpoint symbols remain macroscopic at infinity, and the finite exponential-sum kernel argument rules out finite rank.

## Originality

**qualified_with_inaccessible_zero_product_prior**. Qin's September 2026 preprint supplies the quaternionic bounded-Schwartz zero-product construction but does not state the nondecaying q=0 endpoint, all-p Schatten conclusion, or passive compactness boundary in its public result. Lin–Lu–Zu provide a broad bounded-symbol Toeplitz representation criterion for weighted composition operators, so the single building-block representation is not new. Bauer–Le (2011) is the most important older zero-product prior: open-access searches did not yield its full text, and authorized institutional retrieval stopped at a human-verification gate that was not bypassed. Qin's discussion of Bauer–Le describes different bounded/unbounded zero-product examples, and targeted searches found no exact endpoint/all-Schatten pair. Originality is therefore supported only for this combined endpoint and ideal statement, with Bauer–Le retained as an explicit residual risk.

## Scientific value

**meaningful_operator_ideal_sharpening**. The example sharply separates symbol-side decay from operator-side smoothing: in two active dimensions the symbols need not decay at infinity while both zero divisors belong to every Schatten ideal and have infinite rank. In higher dimensions the same family exhibits an exact compact/noncompact transition controlled solely by passive Gaussian damping, clarifying the mechanism behind the recent zero-product construction.

## Literature and evidence checked

- https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/19/nonvanishing-schatten-zero-divisors-fock-toeplitz--c8def62ac799
- https://arxiv.org/abs/2609.20555
- https://doi.org/10.1016/j.jfa.2011.07.006
- https://arxiv.org/abs/2607.04102
- https://doi.org/10.1007/s00020-010-1768-9
## Literature access note

The prior source `10.1016/j.jfa.2011.07.006` was not available as lawful open full text. Authorized institutional retrieval reached a publisher human-verification gate; it was not bypassed. It is **not** claimed to have been read in full.

## Limitations

- The construction is specific to n≥2 and this quaternionic Gaussian family; it does not settle the one-dimensional bounded-symbol zero-product problem.
- The single weighted-composition/Toeplitz representation mechanism has related prior art and is not claimed as novel.
- Bauer–Le (2011) could not be read in full because authorized retrieval required human verification; no inaccessible theorem text is claimed.
- No optimal Schatten quasi-norm for the four-term sums or classification of nondecaying compact-symbol phenomena is proved.
