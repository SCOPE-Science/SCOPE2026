# Independent Audit — 2026-09-29

**Record:** `2026/09/19/fgm-block-substitution-validity-and-entropy-failure--f5661be14848`  
**Disposition:** **PASSED**

## Correctness

**PASS** — Repeated differentiation gives g=1+θ(1-2^rU)(1-2^sV). Since the two factors range independently over [-(2^r-1),1] and [-(2^s-1),1], their product has exact range [-max(2^r-1,2^s-1),(2^r-1)(2^s-1)], giving the stated necessary-and-sufficient interval. The explicit r=2,s=1,θ=1 test gives -99/125 exactly. For entropy, A_r=1-2^r∏X_i is a martingale; strict conditional Jensen for (1+θab)log(1+θab) shows KL divergence strictly increases whenever a block is enlarged in the interior of the valid parameter range. I independently recomputed H''(0)=-[((4/3)^r)-1][((4/3)^s)-1], including -1/9 at (1,1) and -7/27 at (2,1).

## Originality

**PASS** — Lu's current arXiv version still states unrestricted copula substitution closure, a simple density-product formula, and entropy additivity. The proof treats a multivariate copula value as though it were uniform, which fails already for a product copula. General nesting restrictions and Kendall-distribution phenomena are established prior art; they are not the novelty claimed here. Searches did not locate this exact FGM/product-block two-sided threshold together with the global strict entropy monotonicity. Broad multivariate-FGM literature remains a residual risk for the threshold in another parametrization.

## Scientific value

**PASS** — This is a sharp correction to central claims of a current preprint: it supplies not just a counterexample, but the exact surviving parameter window and a second independent failure of entropy additivity even inside that valid window. The global entropy strictness is stronger than a local Taylor counterexample.

## Evidence checked

- X. Lu, Copula Operad and Copula Entropy: https://arxiv.org/abs/2609.20512 — Current v1 source; its unrestricted closure, proposed density formula, and entropy-additivity theorem are the claims directly tested.
- A. J. McNeil, Sampling nested Archimedean copulas: https://doi.org/10.1080/00949650701255834 — Prior art that nested copulas require compatibility conditions; not claimed as new here.

Repository evidence was read at inventory commit `e9ed144c13b7834896a844cc4f9cac3c25a168a6` / source-check commit `253a0fe5d0217455660a277f9adb940030e567ad`. A later repository-head comparison through `eff2c6312cec5b0dee5115e5f42211a853092dfb` found no changes under this record path, so the assigned source-tree SHA `971de7c7b15557e991ad4d48cca6c9fe6638effb` is the tree audited. GitHub was used only as read-only evidence.

## Limitations

- The exact interval is for a bivariate FGM outer copula with product independence inner blocks, not arbitrary substitutions.
- General nesting restrictions and non-uniform Kendall transforms are prior art.
- Broad multivariate-FGM literature may contain the interval in an equivalent parametrization; current searches did not establish otherwise definitively.

## Audit conclusion

This independent audit is scientifically complete on correctness, originality, and value. The record may remain at its source path without substantive research-file edits.
