# Independent audit — 2026-09-29

Record: `2026/09/18/spectral-gap-contractions-duality-self-adjoint--db9d68568bf9`  
Assigned and audited source tree: `955617ea9b64a3686b453f257500384676243336`  
Audited repository state: `SCOPE-Science/SCOPE2026` `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
Current RESULT.md blob: `f4da85b8b3dc00ba1bbfcd71b8295401540eb606`  
Disposition: **passed**

## Correctness

**independently_supported**. The spectral-gap repair is mathematically coherent. Duality self-adjointness gives ||T^2||=||T||^2 and hence r(T)=||T||; nonzero eigenvalues are real. A length-two Jordan chain contradicts the eigenvector's norming functional, so nonzero spectral values are semisimple. On the Riesz complement N_lambda, T-lambda I is invertible, giving Jm(N_lambda)=0 and therefore contractivity of each nonzero Riesz projection. For a finite completed modulus block, the strict spectral gap makes Jz annihilate every removed eigenspace by iterating (T*)^k Jz=J(T^kz); this proves the residual Riesz projection is contractive. Restricting T to that smooth invariant residual then gives norm equal to its spectral radius, yielding the exact next-modulus tail. The at-most-two signs at a modulus level justify the stated uniform intermediate bounds.

## Originality

**qualified_gap_closure**. The August 2026 Shameem--Deepesh preprint already claims operator-norm spectral representation, but a public Pith review identifies the same load-bearing gap addressed here: the original proof assumes contractivity or uniform boundedness of residual Auerbach projections without proving it. Searches did not locate the record's spectral-gap Riesz-projection mechanism or exact modulus-block tail formula in the accessible prior literature. García-Pacheco's 2024 open-access adjoint paper establishes the surrounding duality-map framework. The 2020 García-Pacheco selfadjoint paper remained unavailable in full text after OA attempts; authorized Oxford access reached a human-verification gate, which was not bypassed. Originality is therefore accepted only as a qualified repair/refinement, with that older source retained as a residual prior-art risk.

## Scientific value

**high_value_proof_gap_repair**. The record supplies a concrete mechanism that repairs the exact step publicly flagged as missing in the recent compact spectral theorem and strengthens it with contractive canonical projections and exact completed-block tails. Its value is specifically tied to the duality-map notion of self-adjointness and does not extend automatically to arbitrary Banach-space Hermitian notions.

## Literature and evidence checked

- https://arxiv.org/abs/2608.06873
- https://www.pith.science/paper/2608.06873
- https://doi.org/10.1007/s13348-023-00414-8
- https://doi.org/10.1016/j.na.2019.111696
- https://arxiv.org/abs/2605.15898
- https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/18/spectral-gap-contractions-duality-self-adjoint--db9d68568bf9
## Access note

Open-access searches did not yield readable full text of García-Pacheco (2020), DOI 10.1016/j.na.2019.111696. Authorized Oxford retrieval was attempted and stopped at a publisher human-verification gate. That gate was not bypassed, and the paper is not claimed to have been read in full.

## Limitations

- The result concerns self-adjointness defined by T*J=JT on a smooth complex Banach space.
- Exact tail norms are stated after complete eigenvalue-modulus blocks; a split +/- block only gets the uniform two-times-modulus remainder bound.
- The 2020 García-Pacheco full text could not be read: Oxford institutional retrieval stopped at human verification and was not bypassed.
- The public Pith review is machine-generated evidence of the source proof gap, not a human referee report.
