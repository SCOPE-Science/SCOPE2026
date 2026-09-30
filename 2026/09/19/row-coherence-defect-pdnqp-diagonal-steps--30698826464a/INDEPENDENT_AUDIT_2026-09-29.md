# Independent audit — 2026-09-30

Record: `2026/09/19/row-coherence-defect-pdnqp-diagonal-steps--30698826464a`  
Assigned and audited source tree: `e2aef22608be9a7be734599a2d789d546fcdb663`  
Audited repository state: `SCOPE-Science/SCOPE2026` `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
Current RESULT.md blob: `5a2393545db91b92a50785eea0f22ec5fc44cb09`  
Disposition: **passed**

## Correctness

**independently_supported**. The normalized-row obstruction is correct. The source dual mass makes every row of K=M_y^{-1/2}BM_w^{-1/2} have Euclidean norm one, hence ||K||_F^2=m and 1<=||K||_2<=sqrt(m). The source balancing parameter cancels from S^{1/2}BT^{1/2}, leaving the factor 0.99||K||_2. For B=[1_{m×p},I_m,-I_m] with the displayed admissible masses, direct multiplication gives KK^T=(a/(a+1))11^T+(1/(a+1))I and top squared singular value (ma+1)/(a+1), approaching m. In the top singular direction all componentwise products have aligned signs, so the coupling term alone is 0.99||K||_2 while the metric energy is one; whenever this exceeds one the source acceptance inequality necessarily fails because the remaining Hessian contribution is nonnegative. The row-l1 comparison scale also has norm at most one by the weighted AM-GM/Schur estimate.

## Originality

**qualified_source_specific_diagnostic**. Chen–Lu's September 2026 PDNQP paper introduces the residual-form solver, diagonal scaling and adaptive acceptance mechanism. Classical Pock–Chambolle diagonal preconditioning, Ruiz equilibration and Schur-type operator bounds are prior art. Current searches did not locate the source-specific coherence classification, the full-row-rank equilibrated sharp family, or the explicit accepted-metric failure direction. The contribution is therefore a focused worst-case analysis of the new initialization, not a new general preconditioning theorem.

## Scientific value

**meaningful_algorithmic_stress_test**. The result identifies a precise structural quantity—normalized row coherence—that is invisible to rowwise mass normalization and can force an O(sqrt(m)) coupling amplification even after ordinary infinity-norm equilibration. It explains why PDNQP's adaptive reduction safeguard can be necessary and gives a concrete comparison scale, without overclaiming algorithmic divergence.

## Literature and evidence checked

- https://arxiv.org/abs/2609.19557
- https://doi.org/10.1109/ICCV.2011.6126441
- http://purl.org/net/epubs/work/29557
- https://arxiv.org/abs/2106.04756
- https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/19/row-coherence-defect-pdnqp-diagonal-steps--30698826464a

## Limitations

- The construction is a worst-case family and does not show that typical benchmark instances exhibit sqrt(m) amplification.
- The result concerns the initial diagonal scaling and an explicit rejected trial direction; it does not prove divergence after PDNQP's adaptive reduction.
- The row-l1 alternative is only a coupling-safe comparison and is not a complete replacement for the source acceptance test.
- General diagonal preconditioning and equilibration principles are prior art; novelty is source-specific.
