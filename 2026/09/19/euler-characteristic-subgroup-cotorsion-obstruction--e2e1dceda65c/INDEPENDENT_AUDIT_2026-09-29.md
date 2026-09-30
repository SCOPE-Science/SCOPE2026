# Independent audit — 2026-09-29

Record: `2026/09/19/euler-characteristic-subgroup-cotorsion-obstruction--e2e1dceda65c`  
Assigned and audited source tree: `7f4c2a7eb6ec68fde6d46ec8ebad100bd4039d50`  
Audited repository state: `SCOPE-Science/SCOPE2026` `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
Current RESULT.md blob: `69738b76fb967db5a72fe8e78e4afd33a6182272`  
Disposition: **repaired**

## Correctness

**independently_supported**. The theorem is mathematically correct. Euler characteristic makes A_B extension closed and weakly idempotent complete, and the standard contractible cone sequences give its Frobenius structure. The correction stalks R_-(r), R_+(r) do have arbitrary prescribed Euler characteristic while staying in the required low/high cohomological ranges, so they prove I_B=<F_B> and J_B=<C_B> uniformly for every subgroup B≤Z. The degreewise-split Ext^1 formula is correct and zero-Euler two-stalk test objects give both reverse ideal orthogonality inclusions. The explicit cone-plus-correction constructions give special ideal approximations for every A. At object level, the long exact sequence forces the truncated Euler conditions, and the ordinary cone sequence proves their sufficiency. The zero-Euler witnesses S^0(k)⊕S^1(k) and S^1(k)⊕S^2(k) obstruct both object approximation sides for every proper B. The idempotent-completion argument is also valid.

## Originality

**requires_repository_provenance_repair**. The result is not a separate SCOPE discovery. Repository history shows that the substantively identical record `euler-subgroup-cotorsion-obstruction--9b38fc18ec20` was committed at 2026-09-19 14:38:25 UTC (commit 81c308dba558c2b01e559071d8b93a2dc2c4e76e), whereas this record first appears in the later `Add Euler-characteristic subgroup cotorsion obstruction` commit sequence beginning at 15:01:20 UTC (a3ae9bd05f06929391752cb5ca88b6c423e39f30). The two records state the same subgroup theorem, same sharp object-completeness boundary B=Z, same truncated-Euler criteria, and same idempotent-completion conclusion. Ren–Wang remains prior external art for B=2Z. This later record is therefore retained only as an alternate, more uniform correction-stalk proof and corroboration of the earlier same-day SCOPE theorem.

## Scientific value

**useful_alternate_proof_after_repair**. The correction-stalk presentation is concise and genuinely useful: it treats finite-index and zero subgroups in one proof and cleanly isolates the K_0/Euler mechanism. Its value after provenance repair is expository, corroborative, and reproducibility-oriented rather than a second independent mathematical advance.

## Literature and evidence checked

- https://github.com/SCOPE-Science/SCOPE2026/commit/81c308dba558c2b01e559071d8b93a2dc2c4e76e
- https://github.com/SCOPE-Science/SCOPE2026/commit/a3ae9bd05f06929391752cb5ca88b6c423e39f30
- https://arxiv.org/abs/2609.18681
- https://arxiv.org/abs/2609.14382
- https://doi.org/10.1016/j.aim.2013.05.020

## Limitations

- The repaired record makes no separate priority claim relative to the earlier same-day SCOPE record.
- Ren–Wang's B=2Z parity case is prior art.
- Equivalent abstraction in older K_0/exact-category language remains a residual prior-art risk.
- The result is specific to bounded finite-dimensional complexes with the degreewise split exact structure.
