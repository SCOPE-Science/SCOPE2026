# Independent audit — 2026-09-30

**Record:** `2026/09/21/point-deletion-inertia-ladder-chen-li-graphs--0ceea66ee9ab`  
**Repository:** `SCOPE-Science/SCOPE2026` at `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
**Audited tree:** `a445f75c2783f8c830e64abe50acc42ffb24f4d9`  
**Disposition:** **PASSED**

## Correctness

**PASS.** The Kneser-block calculation is correct: with the point--2-subset incidence matrix C, CC^T=(k-2)I+J and the KG(k,2) adjacency matrix is J+I-C^TC, giving inertia (binom(k,2)-k+1,0,k-1). Cauchy interlacing from W_k after deleting t point vertices gives n^+>=binom(k,2)+1-t and n^-<=k-1, while the untouched Kneser principal subgraph forces n^->=k-1; dimension counting then forces the claimed nonsingular inertia. Connectivity and twin-freeness arguments check out. An independent numerical reconstruction checked 40 graphs for 5<=k<=9 and every deletion count with no inertia or reducedness mismatch.

## Originality

**PASS (literature-bounded).** Chen--Li (2026) state the W_k inertia family and only the special one-vertex deletion W_5-a_1 with inertia (10,0,4); the checked source does not state the all-k, all-t deletion ladder, its interval-realization consequence, or the all-k equality subfamily. Targeted web searches and a repository code search found no duplicate theorem. Priority remains bounded by very recent or differently indexed spectral-graph work.

## Scientific value

**PASS.** The theorem converts a single counterexample construction into an exact k+1-step inertia ladder, realizes a full interval of nonsingular inertias for every negative index q>=4, and supplies an infinite family on the former equality boundary. This directly sharpens the structural picture after the conjectured bound failed.

## Literature and evidence

- Chen and Li, Counterexamples to a conjecture on graph inertia: https://arxiv.org/abs/2605.07196
- Akbari et al., A new conjecture on the inertia of graphs: https://doi.org/10.1016/j.disc.2025.114953

## Limitations

- The result does not determine the true extremal positive inertia for fixed negative inertia.
- It does not classify all reduced equality graphs or establish uniqueness of the point-deletion mechanism.
- Originality is to the best of the checked literature; very recent or differently indexed work remains a residual risk.


This audit was performed independently of the same-model review. GitHub was used only as evidence; no repository write was made by the auditor.
