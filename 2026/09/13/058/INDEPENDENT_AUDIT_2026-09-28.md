# Independent audit — SCOPE-20260913-058

Date: 2026-09-28 (UTC)  

## Disposition: REPAIRED

### Correctness
The positive-determinant laminate calculation and the diagonal two-atom covariance reduction reproduce exactly, including t*=0.335349626559518 and E*=0.030120427271913. The filed global formula W(F)=min_c sum_i(sigma_i-c)^2 was nevertheless false for det F<0 because the wells are c SO(3), not c O(3). The repaired RESULT inserts the special-orthogonal Procrustes correction +4c sigma_min on orientation-reversing matrices and proves that every negative axis point has energy >1.03, far above E*. The laminate bound, restricted classification, and trace obstruction therefore survive after repair.

### Originality
The explicit hydrostatic laminate and exact two-atom diagonal reduction are a specialized calculation. The targeted literature check retrieved the established two-dimensional two-well relaxation of Conti–Dolzmann but no source resolving this three-dimensional F0 problem. That absence is not a priority proof, so originality is assessed as modest-to-moderate rather than claimed as a new general theorem.

### Scientific value
The corrected result gives a rigorous benchmark upper bound and an exact restricted classification that any full PW-versus-QW analysis must respect. It is useful intermediate structure, but the central envelope equality/gap question remains open.

### Repair applied
RESULT.md is replaced to use the correct SO(3) distance formula, to exclude the orientation-reversing axis branch analytically, and to state PW<=QW<=E* correctly. METADATA.json is replaced only to fix repository-relative artifact paths and add the Procrustes source.

### Sources checked
- Schoenemann, A generalized solution of the orthogonal Procrustes problem: https://doi.org/10.1007/BF02289451 — Classical SVD/Procrustes background; the SO(3) determinant constraint is what forces the orientation correction missed by the filed formula.
- Conti and Dolzmann, Relaxation of a model energy for the cubic to tetragonal phase transformation in two dimensions: https://arxiv.org/abs/1403.4877 — Nearest retrieved two-well relaxation comparison; it treats a two-dimensional model and does not settle the present three-dimensional hydrostatic point.

### Limitations
- The full equality PW(F0)=QW(F0), or a strict separating gap, remains unproved.
- Only two-atom diagonal minors-matched competitors are classified; non-diagonal and higher-atom measures are outside the theorem.
- The numerical catalog/refinement scripts are supporting evidence, not global optimality proofs.
