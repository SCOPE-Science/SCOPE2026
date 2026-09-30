# Independent Audit — 2026-09-28

**Record:** `2026/09/11/020`  
**Title:** Rank-1 correction at the mod-5 Moore-space Adams cell (3,50)  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Audited tree:** `03e2261d2dbb87970a9e6141359fe2f7e2228d79`  
**Disposition:** **PASSED**

## Independent checks

- Rebuilt the dual Steenrod algebra through the required degree with Milnor coproducts and the Moore coaction e3↦tau0⊗e2.
- Constructed the relevant cobar matrices over GF(5), checked d^2=0, ranks, kernel membership and the explicit k0 vector.
- Searched exact/equivalent literature formulations rather than treating a failed exact-title search as proof of novelty.

## Three-axis assessment

- **Correctness — PASS**: A fresh exact reconstruction of the normalized mod-5 dual-Steenrod cobar differential, rather than executing the filed verifier, reproduces the headline cells: at (s,t)=(3,50), dim C=10, outgoing rank 6 and incoming rank 3, so Ext^{3,50} has dimension 1; at (5,51), dim C=400 with ranks 327 and 73, so Ext^{5,51}=0. The same reconstruction gives Ext^{3,51}=1, Ext^{4,51}=0 and Ext^{2,50}=0. The stated k0=[1,2,2,1,0,0,0,0,0,0] is killed by d and raises the incoming augmented rank from 3 to 4, so it is not a boundary. Direct matrix products give d^2=0 in the claimed cells under the filed simplicial cobar sign convention. Since an Adams d2 from (3,50) lands in (5,51), its target vanishes.
- **Originality — PASS**: Focused searches under P^3(5), V(0), cof(5), filtration 3/stem 47 and Ext^{3,50} did not locate a prior source tabulating this exact mod-5 Moore-comodule cell or the explicit k0 representative. The located Moore-space Adams literature supplies machinery and periodic context rather than this finite cell certificate. This supports a specific-computation priority claim, not a claim that no obscure unpublished table exists.
- **Scientific Value — PASS**: The calculation corrects the rank-two E2 premise that motivated the associated Toda/Moss investigation and supplies a reusable exact low-dimensional anchor: one surviving class and a zero d2 target. Its scope is narrow and E2-level, but it materially changes any downstream argument that assumed two classes or a nonzero d2 from this bidegree.

## Findings

- Current main tree exactly equals the assigned source-tree SHA.
- Independent sparse/dense GF(5) linear algebra reproduced all five quoted rank computations and the k0 non-boundary test.
- The filed ext_cobar.py contains unfinished diagnostic stubs, but those stubs are not needed for the result and the audited mathematics was reconstructed independently.
- No Moss convergence, Toda-bracket nontriviality, or higher-differential claim was inferred.

## Sources compared

- Repository record 020 RESULT.md: https://github.com/SCOPE-Science/SCOPE2026/blob/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/11/020/RESULT.md — States the rank-1 cell, k0 certificate and zero d2 target audited here.
- H. R. Miller, On relations between Adams spectral sequences, with an application to the stable homotopy of a Moore space (1981): https://doi.org/10.1016/0022-4049(81)90064-5 — Provides Moore-space Adams-spectral-sequence machinery; it was not located as a table of this exact p=5 cell.
- Panchev, On the v1-periodicity of the Moore space: https://math.mit.edu/~hrm/thesis/panchev-thesis.pdf — Provides Moore-space v1-periodic context, not the explicit Ext^{3,50} cocycle/rank certificate found here.

## Limitations

- Priority assessment is based on focused accessible literature/search and cannot logically exclude an obscure unpublished computation.
- Audit establishes the Adams E2 cell and d2-target vanishing only; it does not validate Moss convergence or a Toda-bracket conclusion.

This audit is independent of the repository’s pre-existing audit material. GitHub was read only as evidence; no repository changes were made by this audit run.
